#!/usr/bin/env python3
"""Re-extract the retained Grab accounting-panel inputs from SEC exhibits.

The retained Grab series uses a stable *operating scope*, not group revenue:

* through 2023Q3: Deliveries GMV + Mobility GMV and the corresponding revenue;
* from 2023Q4: reported On-Demand GMV and Deliveries + Mobility revenue.

This script reads the archived SEC exhibits directly, records the component
values it obtains, and compares them with the pre-existing 47-row accounting
panel.  It never overwrites that panel.  A mismatch is an audit finding, not an
automatic correction.

Usage from the empirical package root:
    python3 04_SCRIPTS/reextract_grab_panel_components.py
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "07_EVENT_AND_MARKET" / "clean_event_panel_accounting.csv"
COVERAGE = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_panel_source_coverage.csv"
OUT = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "grab_panel_component_reconciliation.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize_label(value: object) -> str:
    """Normalise SEC row labels while retaining metric names, not footnotes."""
    label = re.sub(r"[^a-z0-9]", "", str(value).lower())
    return re.sub(r"[0-9*]+$", "", label)


def number(value: object) -> float | None:
    text = str(value).replace(",", "").replace("$", "").strip()
    if re.fullmatch(r"\(?\d+(?:\.\d+)?\)?", text):
        return float(text.strip("()"))
    return None


def metric_value(table: pd.DataFrame, label: str) -> float | None:
    """Return the current-quarter amount from a labelled SEC table row."""
    for _, row in table.iterrows():
        if normalize_label(row.iloc[0]) == label:
            for cell in row.iloc[1:]:
                value = number(cell)
                if value is not None:
                    return value
    return None


def is_current_quarter_table(table: pd.DataFrame, year: int, quarter: int) -> bool:
    """Exclude FY-only comparison tables from a quarterly extraction."""
    compact = re.sub(r"\s+", " ", table.to_string(index=False))
    return bool(re.search(rf"\bQ{quarter}\s*{year}\b", compact, flags=re.IGNORECASE))


def extract_components(path: Path, year: int, quarter: int) -> dict[str, float | int | str]:
    tables = pd.read_html(path)
    metric_tables: list[tuple[int, float, float]] = []
    ondemand: list[tuple[int, float]] = []
    for index, table in enumerate(tables):
        gmv = metric_value(table, "gmv")
        revenue = metric_value(table, "revenue")
        ondemand_gmv = metric_value(table, "ondemandgmv")
        if gmv is not None and revenue is not None and is_current_quarter_table(table, year, quarter):
            metric_tables.append((index, gmv, revenue))
        if ondemand_gmv is not None and is_current_quarter_table(table, year, quarter):
            ondemand.append((index, ondemand_gmv))

    # Before the On-Demand presentation change, the first combined
    # GMV/revenue table is the Group summary and the following two are
    # Deliveries then Mobility. From 2024, the Group overview labels the
    # numerator On-Demand GMV rather than GMV, so the first two conventional
    # GMV/revenue tables are the two components.
    minimum_tables = 2 if (year, quarter) >= (2024, 1) else 3
    if len(metric_tables) < minimum_tables:
        raise RuntimeError(
            f"Expected {minimum_tables} component metric tables in {path.name}; "
            f"found {len(metric_tables)}: {metric_tables}"
        )
    component_start = 0 if (year, quarter) >= (2024, 1) else 1
    deliveries_table, deliveries_gmv, deliveries_revenue = metric_tables[component_start]
    mobility_table, mobility_gmv, mobility_revenue = metric_tables[component_start + 1]
    component_gmv = deliveries_gmv + mobility_gmv
    component_revenue = deliveries_revenue + mobility_revenue

    source_gmv = component_gmv
    gmv_basis = "reported Deliveries GMV + reported Mobility GMV"
    if (year, quarter) >= (2023, 4):
        if not ondemand:
            raise RuntimeError(f"Expected reported On-Demand GMV in {path.name}")
        source_gmv = ondemand[0][1]
        gmv_basis = "reported On-Demand GMV"
    return {
        "deliveries_table_index": deliveries_table,
        "deliveries_gmv_usd_m": deliveries_gmv,
        "deliveries_revenue_usd_m": deliveries_revenue,
        "mobility_table_index": mobility_table,
        "mobility_gmv_usd_m": mobility_gmv,
        "mobility_revenue_usd_m": mobility_revenue,
        "source_gmv_or_gtv_usd_m": source_gmv,
        "source_matched_revenue_usd_m": component_revenue,
        "source_gmv_basis": gmv_basis,
        "source_revenue_basis": "reported Deliveries revenue + reported Mobility revenue",
    }


def fmt(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:.6f}".rstrip("0").rstrip(".")


def main() -> None:
    panel = [row for row in read_csv(PANEL) if row["platform"] == "Grab"]
    coverage = {
        (row["platform"], row["fiscal_year"], row["quarter"]): row
        for row in read_csv(COVERAGE)
    }
    rows: list[dict[str, str]] = []
    for row in panel:
        key = ("Grab", row["fiscal_year"], row["quarter"])
        source = coverage[key]
        extracted = extract_components(
            ROOT / source["archived_file"], int(row["fiscal_year"]), int(row["quarter"])
        )
        # Grab rows in the preserved panel are already denominated in USD
        # millions (unlike GoTo's IDR-trillion rows), exactly matching the
        # filed exhibit convention.
        if row["currency"] != "USD" or row["unit"] != "millions":
            raise RuntimeError(f"Unexpected Grab panel unit: {row['currency']} {row['unit']}")
        panel_gmv = float(row["gmv_or_gtv"])
        panel_revenue = float(row["matched_revenue"])
        gmv_difference = panel_gmv - float(extracted["source_gmv_or_gtv_usd_m"])
        revenue_difference = panel_revenue - float(extracted["source_matched_revenue_usd_m"])
        rows.append({
            "platform": "Grab",
            "period": f"{row['fiscal_year']}Q{row['quarter']}",
            "archived_source_file": source["archived_file"],
            "source_url": source["source_url"],
            "panel_gmv_or_gtv_usd_m": fmt(panel_gmv),
            "source_gmv_or_gtv_usd_m": fmt(float(extracted["source_gmv_or_gtv_usd_m"])),
            "gmv_difference_panel_minus_source_usd_m": fmt(gmv_difference),
            "gmv_reconciliation": "MATCH" if abs(gmv_difference) < 0.000001 else "REVIEW",
            "panel_matched_revenue_usd_m": fmt(panel_revenue),
            "source_matched_revenue_usd_m": fmt(float(extracted["source_matched_revenue_usd_m"])),
            "revenue_difference_panel_minus_source_usd_m": fmt(revenue_difference),
            "revenue_reconciliation": "MATCH" if abs(revenue_difference) < 0.000001 else "REVIEW",
            **{key: fmt(value) if isinstance(value, float) else str(value) for key, value in extracted.items()},
            "interpretation": (
                "No panel value changed. REVIEW means the retained panel does not exactly equal the filed source extraction."
            ),
        })
    if len(rows) != 17:
        raise RuntimeError(f"Expected 17 Grab panel rows; found {len(rows)}")
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    reviews = [row for row in rows if "REVIEW" in (row["gmv_reconciliation"], row["revenue_reconciliation"])]
    print(f"Re-extracted {len(rows)} Grab panel rows. Exact matches: {len(rows) - len(reviews)}. Reviews: {len(reviews)}.")
    for row in reviews:
        print(
            f"REVIEW {row['period']}: GMV diff={row['gmv_difference_panel_minus_source_usd_m']}m; "
            f"revenue diff={row['revenue_difference_panel_minus_source_usd_m']}m"
        )
    print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
