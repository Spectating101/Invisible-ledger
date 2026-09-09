#!/usr/bin/env python3
"""Read-only checks for the bounded reconciliation extension."""

from __future__ import annotations

import csv
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "10_MEASUREMENT_RECONCILIATION"


def text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return path.read_text(encoding="utf-8", errors="replace")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    goto = text(ROOT / "01_RAW_SOURCES/main_indonesia/goto_annual_report_2023.pdf")
    for token in ("8,988,909", "2,813,719", "6,175,190", "8,143,239", "4,112,320", "4,030,919"):
        require(token in goto, f"GoTo annual report missing {token}")

    grab = text(ROOT / "01_RAW_SOURCES/main_indonesia/grab_2023_results.htm")
    for token in ("full year 2023 Group revenue growth would have been 40%", "Deliveries revenue growth would have been 30%", "Revenue for the full year grew 65%", "by 80% YoY for the full year 2023"):
        require(token in grab, f"Grab FY2023 results missing expected disclosure: {token}")

    trade = text(MODULE / "raw_external_sources/us_trade_indonesia_ecommerce.html")
    omdia = text(MODULE / "raw_external_sources/omdia_sea_ecommerce_country_spotlight.pdf")
    food = text(MODULE / "raw_external_sources/katadata_indonesia_food_delivery_2023.html")
    require("52.93 billion" in trade, "U.S. Trade source missing 2023 estimate")
    require("53.34" in omdia, "Omdia source missing FY2023 chart value")
    require("US$4,6 miliar" in food and "50%" in food, "Katadata food-delivery source missing component inputs")

    tokopedia = read_csv(MODULE / "results/tokopedia_fy2022_2023_revenue_incentive_reconciliation.csv")[0]
    require(float(tokopedia["gross_revenue_change_idr_million"]) + float(tokopedia["incentive_reduction_idr_million"]) == float(tokopedia["net_revenue_change_idr_million"]), "Tokopedia identity does not close")
    scope = read_csv(MODULE / "results/external_scope_triangulation_results.csv")
    require(len(scope) == 4, "Expected 3 market-total checks plus 1 GrabFood component floor")
    require(any(r["check"] == "GrabFood_component_floor" for r in scope), "Missing GrabFood floor diagnostic")
    print("PASS: source tokens and bounded reconciliation identities validated.")


if __name__ == "__main__":
    main()
