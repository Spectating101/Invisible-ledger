#!/usr/bin/env python3
"""Build descriptive payment-ledger diagnostics from certified source extracts.

The outputs compare growth rates and publication definitions.  They never pool
payment observations with issuer or BPS observations as if they were the same
sample, and they do not interpret payment value as e-commerce value.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PAYMENTS = ROOT / "data/payments"
BPS_LEVELS = ROOT / "outputs/hypothesis_tests_2026-09-10/bps_national_levels.csv"
OUT = ROOT / "outputs/payment_ledger_2026-09-11"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def growth(old: float, new: float) -> float:
    return (new / old - 1.0) * 100.0


def annual_core_growth() -> list[dict[str, object]]:
    rows = read(PAYMENTS / "bank_indonesia_payments_core_published_annual_2009_2024.csv")
    indexed = {(row["series_id"], int(row["year"])): row for row in rows}
    output: list[dict[str, object]] = []
    for series in sorted({row["series_id"] for row in rows}):
        if (series, 2023) not in indexed or (series, 2024) not in indexed:
            continue
        old = float(indexed[(series, 2023)]["value_as_published"])
        new = float(indexed[(series, 2024)]["value_as_published"])
        output.append(
            {
                "evidence_layer": "Bank Indonesia SPIP",
                "metric": series,
                "value_2023": old,
                "value_2024": new,
                "unit": indexed[(series, 2024)]["unit"],
                "growth_2023_2024_percent": growth(old, new),
                "interpretive_boundary": "Payment-system activity; not e-commerce-only and not an issuer sample",
                "source_locator": f"SPIP tables {indexed[(series, 2024)]['source_sheet']} row {indexed[(series, 2024)]['source_row']}",
            }
        )
    return output


def bps_growth() -> list[dict[str, object]]:
    rows = read(BPS_LEVELS)
    indexed = {int(row["year"]): row for row in rows}
    old, new = indexed[2023], indexed[2024]
    metrics = {
        "bps_ecommerce_total_value": ("transaction_value_idr_trillion", "BPS national e-commerce estimate"),
        "bps_marketplace_component_value": ("marketplace_value_idr_trillion", "BPS marketplace sales-media component"),
        "bps_nonmarketplace_component_value": ("nonmarketplace_value_idr_trillion", "BPS non-marketplace sales-media component"),
        "bps_estimated_ecommerce_businesses": ("estimated_ecommerce_businesses", "BPS estimated business count"),
        "bps_implied_value_per_business": ("implied_idr_million_per_business", "Arithmetic from BPS national totals"),
    }
    output = []
    for metric, (field, boundary) in metrics.items():
        v23, v24 = float(old[field]), float(new[field])
        unit = "IDR trillion" if "value" in field and "per_business" not in field else "businesses" if field == "estimated_ecommerce_businesses" else "IDR million per business"
        output.append(
            {
                "evidence_layer": "BPS e-commerce statistics",
                "metric": metric,
                "value_2023": v23,
                "value_2024": v24,
                "unit": unit,
                "growth_2023_2024_percent": growth(v23, v24),
                "interpretive_boundary": boundary + "; not a payment-instrument series",
                "source_locator": "outputs/hypothesis_tests_2026-09-10/bps_national_levels.csv",
            }
        )
    return output


def qris_growth() -> list[dict[str, object]]:
    rows = read(PAYMENTS / "bank_indonesia_payment_report_observations_2023_2025.csv")
    indexed = {(row["metric"], int(row["period"])): row for row in rows}
    output = []
    for metric in ("qris_transaction_value", "qris_users", "qris_merchants"):
        old, new = indexed[(metric, 2023)], indexed[(metric, 2024)]
        v23, v24 = float(old["value"]), float(new["value"])
        output.append(
            {
                "evidence_layer": "Bank Indonesia QRIS reports",
                "metric": metric,
                "value_2023": v23,
                "value_2024": v24,
                "unit": new["unit"],
                "growth_2023_2024_percent": growth(v23, v24),
                "interpretive_boundary": "QRIS nationally; not e-commerce-only and not directly comparable to BPS transaction value",
                "source_locator": f"{old['source_file']} p.{old['source_page']}; {new['source_file']} p.{new['source_page']}",
            }
        )
    return output


def definition_crosscheck() -> list[dict[str, object]]:
    annual = read(PAYMENTS / "bank_indonesia_spip_national_published_annual_2009_2024.csv")
    report = read(PAYMENTS / "bank_indonesia_payment_report_observations_2023_2025.csv")
    annual_idx = {(row["source_sheet"], int(row["source_row"]), int(row["year"])): float(row["value_as_published"]) for row in annual}
    report_idx = {(row["metric"], int(row["period"])): float(row["value"]) for row in report}

    comparisons = [
        (
            "digital_banking_headline_vs_spip_proprietary_channel",
            report_idx[("digital_banking_transaction_value", 2023)],
            annual_idx[("7", 9, 2023)] / 1000.0,
            "BI report headline vs SPIP table 7 total proprietary-channel value",
        ),
        (
            "electronic_money_headline_vs_spip_all_transaction_components",
            report_idx[("electronic_money_transaction_value", 2023)],
            annual_idx[("5e", 26, 2023)] / 1000.0,
            "BI report headline vs SPIP table 5e overall value including shopping, transfers, top-ups and other components",
        ),
        (
            "electronic_money_headline_vs_spip_shopping_only",
            report_idx[("electronic_money_transaction_value", 2023)],
            annual_idx[("5e", 27, 2023)] / 1000.0,
            "BI report headline vs SPIP table 5e shopping-only value",
        ),
        (
            "card_headline_vs_spip_atm_debit_plus_credit_totals",
            report_idx[("atm_debit_credit_card_transaction_value", 2023)],
            (annual_idx[("5a", 17, 2023)] + annual_idx[("5c", 17, 2023)]) / 1000.0,
            "BI report combined card headline vs sum of SPIP ATM/debit and credit-card total values",
        ),
    ]
    output = []
    for label, headline, spip, note in comparisons:
        output.append(
            {
                "comparison": label,
                "year": 2023,
                "report_headline_rp_trillion": headline,
                "spip_candidate_rp_trillion": spip,
                "difference_spip_minus_headline_rp_trillion": spip - headline,
                "difference_percent_of_headline": (spip / headline - 1.0) * 100.0,
                "status": "definition_crosscheck_not_a_reconciliation",
                "interpretation": note + "; differences do not establish error without metadata reconciliation",
            }
        )
    return output


def main() -> None:
    growth_rows = bps_growth() + annual_core_growth() + qris_growth()
    write(OUT / "bps_payment_growth_comparison_2023_2024.csv", growth_rows)
    write(OUT / "bank_indonesia_definition_crosscheck_2023.csv", definition_crosscheck())
    print(f"growth_rows={len(growth_rows)}")
    print("definition_crosscheck_rows=4")


if __name__ == "__main__":
    main()
