#!/usr/bin/env python3
"""Lightweight structural validation for the public research repository."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "docs/CURRENT_STATUS.md",
    "data/README.md",
    "data/indonesia_fy2023/fy2023_indonesia_source_inputs.csv",
    "data/indonesia_fy2023/fy2023_indonesia_main_rebuilt.csv",
    "data/longitudinal/annual_extension_panel_preliminary.csv",
    "data/quarterly/clean_event_panel_accounting.csv",
    "data/market/platform_market_daily_2010_2026.csv",
    "sources/manifests/document_manifest.csv",
]


def count_csv(path: Path) -> tuple[int, int]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            return 0, 0
        rows = sum(1 for _ in reader)
    return rows, len(header)


def main() -> int:
    missing = [relative for relative in REQUIRED if not (ROOT / relative).is_file()]
    if missing:
        for relative in missing:
            print(f"MISSING: {relative}")
        return 1

    csv_files = sorted(ROOT.glob("data/**/*.csv")) + sorted(
        ROOT.glob("sources/manifests/*.csv")
    )
    failures = 0
    total_rows = 0
    for path in csv_files:
        try:
            rows, columns = count_csv(path)
            total_rows += rows
            if columns == 0:
                print(f"EMPTY: {path.relative_to(ROOT)}")
                failures += 1
        except (UnicodeDecodeError, csv.Error, OSError) as exc:
            print(f"FAILED: {path.relative_to(ROOT)}: {exc}")
            failures += 1

    print(f"Validated {len(csv_files)} CSV files containing {total_rows:,} data rows.")
    print("This is a file-layer count, not the analytical sample N.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
