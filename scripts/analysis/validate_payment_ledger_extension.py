#!/usr/bin/env python3
"""Validate row identity, coverage and source hashes for the payment extension."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "data/payments/bank_indonesia_spip_national_monthly_2009_2025.csv": 18954,
    "data/payments/bank_indonesia_spip_regional_monthly_2009_2025.csv": 42701,
    "data/payments/bank_indonesia_spip_national_published_annual_2009_2024.csv": 1460,
    "data/payments/bank_indonesia_payments_core_monthly_2009_2025.csv": 3616,
    "data/payments/bank_indonesia_payments_core_published_annual_2009_2024.csv": 278,
    "data/payments/bank_indonesia_payment_report_observations_2023_2025.csv": 14,
    "outputs/payment_ledger_2026-09-11/bps_payment_growth_comparison_2023_2024.csv": 30,
    "outputs/payment_ledger_2026-09-11/bank_indonesia_definition_crosscheck_2023.csv": 4,
}


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def ensure_unique(records: list[dict[str, str]], fields: tuple[str, ...], label: str) -> None:
    keys = [tuple(record[field] for field in fields) for record in records]
    if len(keys) != len(set(keys)):
        raise AssertionError(f"Duplicate {label} keys for {fields}")


def main() -> None:
    for relative, expected in EXPECTED.items():
        actual = len(rows(ROOT / relative))
        if actual != expected:
            raise AssertionError(f"{relative}: expected {expected}, got {actual}")

    national = rows(ROOT / "data/payments/bank_indonesia_spip_national_monthly_2009_2025.csv")
    regional = rows(ROOT / "data/payments/bank_indonesia_spip_regional_monthly_2009_2025.csv")
    annual = rows(ROOT / "data/payments/bank_indonesia_spip_national_published_annual_2009_2024.csv")
    headline = rows(ROOT / "data/payments/bank_indonesia_payment_report_observations_2023_2025.csv")
    ensure_unique(national, ("source_sheet", "source_row", "period"), "national monthly")
    ensure_unique(regional, ("source_sheet", "source_row", "period"), "regional monthly")
    ensure_unique(annual, ("source_sheet", "source_row", "year"), "national annual")
    ensure_unique(headline, ("period", "metric"), "report observation")

    periods = {row["period"] for row in national}
    if min(periods) != "2009-01" or max(periods) != "2025-11" or "2025-12" in periods:
        raise AssertionError("Unexpected national monthly coverage")
    if any(row["year"] == "2025" for row in annual):
        raise AssertionError("Partial 2025 must not appear as a published annual observation")

    manifest = rows(ROOT / "sources/bank_indonesia_payments/source_manifest_2026-09-11.csv")
    for record in manifest:
        path = ROOT / "sources/bank_indonesia_payments" / record["local_file"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != record["sha256"]:
            raise AssertionError(f"Source hash mismatch: {path}")

    print("Payment-ledger validation passed.")
    for relative, expected in EXPECTED.items():
        print(f"{relative}: {expected:,} rows")


if __name__ == "__main__":
    main()
