#!/usr/bin/env python3
"""Verify Sea/Shopee panel rows against filed quarterly-exhibit wording.

Each retained Sea row uses the e-commerce segment's directly reported GMV and
GAAP revenue.  Rather than treating an arbitrary number token as confirmation,
this script extracts the issuer's ``GMV was US$...`` and ``GAAP revenue was
US$...`` statements, retains the matching source wording, and compares those
reported values with the existing accounting panel.  It does not overwrite the
panel or fill its 2023Q1–Q3 disclosure gap.
"""

from __future__ import annotations

import csv
import html
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "07_EVENT_AND_MARKET" / "clean_event_panel_accounting.csv"
COVERAGE = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_panel_source_coverage.csv"
OUT = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "sea_panel_direct_reconciliation.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def source_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = BeautifulSoup(raw, "html.parser").get_text(" ", strip=True)
    return re.sub(r"\s+", " ", html.unescape(text.replace("&nbsp;", " ")))


def extract_statement(text: str, metric: str, target: float) -> tuple[float, str, bool]:
    if metric == "gmv":
        pattern = re.compile(
            r"(?:GMV|Gross\s+merchandise\s+value\s*\([^)]*GMV[^)]*\))\s+was\s+US\$\s*"
            r"([0-9]+(?:\.[0-9]+)?)\s*(billion|million)",
            re.I,
        )
    else:
        pattern = re.compile(r"GAAP\s+revenue\s+was\s+US\$\s*([0-9]+(?:\.[0-9]+)?)\s*(billion|million)", re.I)
    candidates: list[tuple[float, str, bool]] = []
    for match in pattern.finditer(text):
        amount = float(match.group(1))
        if match.group(2).lower() == "million":
            amount /= 1000
        # Releases often place the operating-metric bullets several formatted
        # paragraphs after the e-commerce heading.
        start = max(0, match.start() - 5000)
        context = text[start:match.end()].lower()
        ecomm_context = "e-commerce" in context or "shopee" in context
        candidates.append((amount, match.group(0), ecomm_context))
    for candidate in candidates:
        if abs(candidate[0] - target) < 1e-9 and candidate[2]:
            return candidate
    for candidate in candidates:
        if abs(candidate[0] - target) < 1e-9:
            return candidate
    raise RuntimeError(f"No exact reported {metric} statement for target {target} in source document")


def main() -> None:
    panel = [row for row in read_csv(PANEL) if row["platform"] == "Sea"]
    coverage = {
        (row["platform"], row["fiscal_year"], row["quarter"]): row
        for row in read_csv(COVERAGE)
    }
    rows: list[dict[str, str]] = []
    for row in panel:
        source = coverage[("Sea", row["fiscal_year"], row["quarter"])]
        text = source_text(ROOT / source["archived_file"])
        panel_gmv = float(row["gmv_or_gtv"])
        panel_revenue = float(row["matched_revenue"])
        source_gmv, gmv_wording, gmv_ecomm_context = extract_statement(text, "gmv", panel_gmv)
        source_revenue, revenue_wording, revenue_ecomm_context = extract_statement(text, "revenue", panel_revenue)
        rows.append({
            "platform": "Sea",
            "period": f"{row['fiscal_year']}Q{row['quarter']}",
            "archived_source_file": source["archived_file"],
            "source_url": source["source_url"],
            "panel_gmv_usd_b": row["gmv_or_gtv"],
            "source_gmv_usd_b": f"{source_gmv:g}",
            "gmv_reconciliation": "MATCH" if source_gmv == panel_gmv else "REVIEW",
            "gmv_source_wording": gmv_wording,
            "gmv_ecommerce_or_shopee_context": "yes" if gmv_ecomm_context else "review",
            "panel_revenue_usd_b": row["matched_revenue"],
            "source_revenue_usd_b": f"{source_revenue:g}",
            "revenue_reconciliation": "MATCH" if source_revenue == panel_revenue else "REVIEW",
            "revenue_source_wording": revenue_wording,
            "revenue_ecommerce_or_shopee_context": "yes" if revenue_ecomm_context else "review",
            "scope": "direct issuer-reported e-commerce/Shopee operating GMV and GAAP revenue; not Indonesia-specific",
        })
    if len(rows) != 14:
        raise RuntimeError(f"Expected 14 Sea panel rows; found {len(rows)}")
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    review = [row for row in rows if "REVIEW" in (row["gmv_reconciliation"], row["revenue_reconciliation"])]
    print(f"Re-extracted {len(rows)} Sea panel rows. Exact matches: {len(rows) - len(review)}. Reviews: {len(review)}.")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
