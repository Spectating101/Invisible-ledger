#!/usr/bin/env python3
"""Reconcile the retained GoTo quarterly panel against issuer PDFs.

This script is intentionally conservative.  It does not turn GoTo's Group
figures into Indonesia data and it does not overwrite the preserved panel.
It checks whether each stored Group GTV and Group net-revenue value is shown
in the issuer's quarterly results document, records the reporting basis, and
labels display-rounding separately from an exact source match.
"""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "07_EVENT_AND_MARKET" / "clean_event_panel_accounting.csv"
COVERAGE = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_panel_source_coverage.csv"
OUT = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "goto_panel_primary_document_reconciliation.csv"

# Values below are the issuer-displayed values in IDR billions, except for the
# two 2022 release tables, which display IDR millions.  They are declarations
# of what the source document says, not corrections to the existing panel.
SOURCE_FACTS = {
    "2022Q2": {"gtv": "150,536,495", "revenue": "1,902,617", "scale": "IDR millions", "class": "ROUNDING-CONFIRMED", "basis": "reported Group GTV and Group net revenue", "note": "Panel stores rounded IDR-trillion values; issuer table reports 150.536495 and 1.902617 trillion."},
    "2022Q3": {"gtv": "160,940,183", "revenue": "4,568,903", "scale": "IDR millions", "class": "ROUNDING-CONFIRMED", "basis": "reported Group GTV and Group net revenue", "note": "Panel stores rounded IDR-trillion values; issuer table reports 160.940183 and 4.568903 trillion."},
    "2022Q4": {"gtv": "161.9", "revenue": "3.4", "scale": "IDR trillions, presentation display", "class": "ROUNDING-DISPLAY-CONFIRMED", "basis": "reported Group GTV and Group net revenue", "note": "Issuer presentation shows rounded headline/display values only; it does not support the panel's three-decimal precision."},
    "2023Q1": {"gtv": "148,538", "revenue": "3,332", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2023Q2": {"gtv": "143,739", "revenue": "3,552", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2023Q3": {"gtv": "151,250", "revenue": "3,627", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2023Q4": {"gtv": "163,020", "revenue": "4,274", "scale": "IDR billions", "class": "ROUNDING-CONFIRMED", "basis": "reported Group GTV and Group net revenue", "note": "Issuer table reports 163.020 trillion; panel retains 163.0 trillion."},
    "2024Q1": {"gtv": "116,506", "revenue": "3,078", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue on comparable/pro-forma basis", "note": "Presentation distinguishes reported, restated and pro-forma GTV; retained panel uses pro-forma/comparable 116.506 and 3.078."},
    "2024Q2": {"gtv": "121,451", "revenue": "3,518", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue on comparable/pro-forma basis", "note": "Retained panel uses presentation's comparable/pro-forma 121.451 and 3.518, not the actual/reported 115.340 and 3.658 shown elsewhere."},
    "2024Q3": {"gtv": "137,363", "revenue": "3,926", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue on comparable/pro-forma basis", "note": "Direct issuer presentation table."},
    "2024Q4": {"gtv": "144,464", "revenue": "4,231", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue on comparable/pro-forma basis", "note": "Direct issuer presentation table."},
    "2025Q1": {"gtv": "144,560", "revenue": "4,231", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2025Q2": {"gtv": "152,873", "revenue": "4,328", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2025Q3": {"gtv": "176,484", "revenue": "4,736", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2025Q4": {"gtv": "211,732", "revenue": "5,027", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
    "2026Q1": {"gtv": "236,316", "revenue": "5,341", "scale": "IDR billions", "class": "EXACT", "basis": "reported Group GTV and Group net revenue", "note": "Direct issuer presentation table."},
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def pdf_pages(path: Path) -> list[str]:
    result = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
    )
    return result.stdout.split("\f")


def locate(page_text: list[str], token: str) -> int | None:
    for page_number, text in enumerate(page_text, start=1):
        if token in text:
            return page_number
    return None


def main() -> None:
    panel = [row for row in read_csv(PANEL) if row["platform"] == "GoTo"]
    coverage = {
        f"{row['fiscal_year']}Q{row['quarter']}": row
        for row in read_csv(COVERAGE) if row["platform"] == "GoTo"
    }
    rows: list[dict[str, str]] = []
    for row in panel:
        period = f"{row['fiscal_year']}Q{row['quarter']}"
        fact = SOURCE_FACTS[period]
        source = coverage[period]
        pages = pdf_pages(ROOT / source["archived_file"])
        gtv_page = locate(pages, fact["gtv"])
        revenue_page = locate(pages, fact["revenue"])
        if gtv_page is None or revenue_page is None:
            raise RuntimeError(f"{period}: source token missing (GTV={gtv_page}, revenue={revenue_page})")
        rows.append({
            "platform": "GoTo",
            "period": period,
            "archived_source_file": source["archived_file"],
            "source_url": source["source_url"],
            "panel_gtv_idr_trillion": row["gmv_or_gtv"],
            "issuer_gtv_display": fact["gtv"],
            "panel_net_revenue_idr_trillion": row["matched_revenue"],
            "issuer_net_revenue_display": fact["revenue"],
            "issuer_display_scale": fact["scale"],
            "gtv_source_page": str(gtv_page),
            "revenue_source_page": str(revenue_page),
            "reconciliation_class": fact["class"],
            "reported_basis": fact["basis"],
            "basis_and_precision_note": fact["note"],
            "scope": "GoTo Group reporting; not Indonesia-only and not a main Indonesia-sample observation",
        })
    if len(rows) != 16:
        raise RuntimeError(f"Expected 16 GoTo panel rows; found {len(rows)}")
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    classes = {kind: sum(r["reconciliation_class"] == kind for r in rows) for kind in sorted({r["reconciliation_class"] for r in rows})}
    print(f"Reconciled {len(rows)} GoTo panel rows against issuer PDFs: {classes}")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
