#!/usr/bin/env python3
"""Validate the advisor review package after extraction."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "PACKAGE_CONTENTS.csv"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def csv_rows(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        return sum(1 for _ in reader)


def main() -> int:
    if not INDEX.is_file():
        print("Missing PACKAGE_CONTENTS.csv")
        return 1

    failures = 0
    checked = 0
    with INDEX.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        relative = row["relative_path"]
        if relative == "PACKAGE_CONTENTS.csv":
            continue
        path = ROOT / relative
        if not path.is_file():
            print(f"MISSING: {relative}")
            failures += 1
            continue
        checked += 1
        if path.stat().st_size != int(row["bytes"]):
            print(f"SIZE MISMATCH: {relative}")
            failures += 1
        if digest(path) != row["sha256"]:
            print(f"HASH MISMATCH: {relative}")
            failures += 1
        if path.suffix.lower() == ".csv" and row["data_rows_or_records"]:
            if csv_rows(path) != int(row["data_rows_or_records"]):
                print(f"ROW-COUNT MISMATCH: {relative}")
                failures += 1

    print(f"Checked {checked} package files against the manifest.")
    print("CSV row counts are file-level records, not one pooled sample N.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
