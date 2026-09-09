#!/usr/bin/env python3
"""Read-only structural validation for the advisor data-review package.

Created on 2026-09-08. This script does not create data or alter results. It
checks that paths cited by source extracts exist, the observation counts remain
intact, and the rebuilt FY2023 Shopee value uses Sea's disclosed 10.0% rate.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTRACTS = ROOT / "02_SOURCE_EXTRACTS"
RESULTS = ROOT / "05_RESULTS"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    main_inputs = read_rows(EXTRACTS / "fy2023_indonesia_source_inputs.csv")
    extension_inputs = read_rows(EXTRACTS / "indonesia_extension_source_inputs.csv")
    grab_coverage = read_rows(EXTRACTS / "grab_country_revenue_coverage_2021_2024.csv")

    missing = []
    for row in [*main_inputs, *extension_inputs, *grab_coverage]:
        source = row.get("source_file", "")
        if source.startswith("02_SOURCE_EXTRACTS/"):
            continue
        if not (ROOT / source).is_file():
            missing.append(source)
    require(not missing, f"Missing cited source files: {sorted(set(missing))}")

    require(len(main_inputs) == 11, f"Expected 11 FY2023 inputs, found {len(main_inputs)}")
    require(len(extension_inputs) == 24, f"Expected 24 extension inputs, found {len(extension_inputs)}")
    require(len(grab_coverage) == 20, f"Expected 20 Grab country-revenue rows, found {len(grab_coverage)}")
    require({r["period"] for r in grab_coverage} == {"FY2021", "FY2022", "FY2023", "FY2024"}, "Grab coverage periods changed")
    require({r["geography"] for r in grab_coverage} == {"Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand"}, "Grab coverage countries changed")

    main_rows = read_rows(RESULTS / "fy2023_indonesia_main_rebuilt.csv")
    expanded_sensitivity = read_rows(RESULTS / "fy2023_indonesia_main_one_way_sensitivity.csv")
    leave_one_out = read_rows(RESULTS / "fy2023_indonesia_leave_one_platform_out.csv")
    extension_rows = read_rows(RESULTS / "indonesia_platform_year_extension.csv")
    history_rows = read_rows(RESULTS / "historical_within_platform_ratios.csv")
    event_rows = read_rows(ROOT / "07_EVENT_AND_MARKET" / "clean_event_panel_accounting.csv")
    require(len(main_rows) == 3, f"Expected 3 main observations, found {len(main_rows)}")
    require(len(expanded_sensitivity) == 14, f"Expected 14 one-way scenarios, found {len(expanded_sensitivity)}")
    require(len(leave_one_out) == 3, f"Expected 3 leave-one-platform-out checks, found {len(leave_one_out)}")
    require(all("assumption_scenario" in row["assumption_class"] for row in expanded_sensitivity), "Sensitivity labels changed")
    require(len(extension_rows) == 9, f"Expected 9 extension observations, found {len(extension_rows)}")
    require(len(history_rows) == 8, f"Expected 8 historical annual rows, found {len(history_rows)}")
    require(len(event_rows) == 47, f"Expected 47 event-accounting rows, found {len(event_rows)}")

    shopee = next(row for row in main_rows if row["platform"] == "Shopee")
    require(float(shopee["platform_revenue_usd_b"]) == 2.152, "Shopee must use Sea's disclosed 10.0% rate")
    print("PASS: cited paths, counts, and the FY2023 Shopee rate convention validated.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
