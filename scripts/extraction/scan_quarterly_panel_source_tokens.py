#!/usr/bin/env python3
"""Run a mechanical token-level check against archived quarterly releases.

This is intentionally a conservative first pass.  A "found" result only means
that the panel value (or its documented unit conversion) appears in the source
document; it does not establish that the value is in the correct source table
or basis.  A "not found" result is a review flag, not an automatic correction.

It is most informative for direct Sea and GoTo fields.  Grab's panel contains
documented segment sums in many periods, so the script labels those as requiring
component-level re-extraction rather than treating absence of the aggregate as a
failure.
"""

from __future__ import annotations

import csv
import html
import re
import subprocess
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COVERAGE = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_panel_source_coverage.csv"
OUT = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_panel_raw_token_scan.csv"


def load_text(relative_path: str) -> str:
    """Normalise issuer HTML enough to search both ordinary and Next.js pages."""
    path = ROOT / relative_path
    if path.suffix.lower() == ".pdf":
        completed = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            check=True,
            capture_output=True,
            text=True,
        )
        raw = completed.stdout
    else:
        raw = path.read_text(encoding="utf-8", errors="replace")
    # GoTo embeds the article body as escaped HTML inside the page payload.
    for before, after in ((r"\u003c", "<"), (r"\u003e", ">"), (r"\u0026", "&"), (r"\n", " ")):
        raw = raw.replace(before, after)
    return html.unescape(raw)


def token_variants(value: str, platform: str) -> list[str]:
    """Generate conservative printed forms for the unit used by each issuer."""
    variants = {value}
    decimal_value = Decimal(value)
    if platform == "GoTo":
        # Panel data are in IDR trillions; releases normally display IDR billions.
        variants.add(f"{int((decimal_value * 1000).quantize(Decimal('1'))):,}")
    elif platform == "Grab":
        variants.add(f"{int(decimal_value.quantize(Decimal('1'))):,}")
    else:  # Sea reports in USD billions in the retained panel.
        variants.add(format(decimal_value, "f"))
    return sorted(variants, key=len, reverse=True)


def token_found(text: str, variants: list[str]) -> tuple[bool, str]:
    for variant in variants:
        if re.search(rf"(?<![0-9]){re.escape(variant)}(?![0-9])", text):
            return True, variant
    return False, ""


def directness(platform: str, fiscal_year: int) -> tuple[bool, bool]:
    """Whether the existing panel's aggregate should itself print in the release."""
    if platform == "Sea" or platform == "GoTo":
        return True, True
    # Grab 2022–23 uses Mobility + Deliveries GMV; all retained revenue values
    # are Mobility + Deliveries sums. From 2024, On-Demand GMV itself is printed.
    return fiscal_year >= 2024, False


def main() -> None:
    with COVERAGE.open(newline="", encoding="utf-8") as handle:
        coverage = list(csv.DictReader(handle))
    output = []
    for row in coverage:
        platform = row["platform"]
        year = int(row["fiscal_year"])
        text = load_text(row["archived_file"])
        gtv_direct, revenue_direct = directness(platform, year)
        gtv_found, gtv_variant = token_found(text, token_variants(row["gmv_or_gtv"], platform))
        rev_found, rev_variant = token_found(text, token_variants(row["matched_revenue"], platform))
        output.append({
            "platform": platform,
            "period": f"{row['fiscal_year']}Q{row['quarter']}",
            "archived_file": row["archived_file"],
            "gmv_or_gtv_panel_value": row["gmv_or_gtv"],
            "gmv_or_gtv_expected_to_print_directly": "yes" if gtv_direct else "no — documented segment construction",
            "gmv_or_gtv_token_found": "yes" if gtv_found else "no",
            "gmv_or_gtv_matched_printed_token": gtv_variant,
            "matched_revenue_panel_value": row["matched_revenue"],
            "revenue_expected_to_print_directly": "yes" if revenue_direct else "no — documented segment construction",
            "revenue_token_found": "yes" if rev_found else "no",
            "revenue_matched_printed_token": rev_variant,
            "interpretation": (
                "direct-source token check only; inspect table/metric label before treating this as numeric verification"
                if gtv_direct or revenue_direct
                else "aggregate is not expected to print directly; component-level source extraction is required"
            ),
        })
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)

    expected = [
        row for row in output
        if (row["gmv_or_gtv_expected_to_print_directly"] == "yes" and row["gmv_or_gtv_token_found"] == "no")
        or (row["revenue_expected_to_print_directly"] == "yes" and row["revenue_token_found"] == "no")
    ]
    print(f"Scanned {len(output)} panel rows. Direct-field token review flags: {len(expected)}. Output: {OUT}")
    for row in expected:
        print(
            f"FLAG {row['platform']} {row['period']}: "
            f"GMV/GTV={row['gmv_or_gtv_token_found']} revenue={row['revenue_token_found']}"
        )


if __name__ == "__main__":
    main()
