#!/usr/bin/env python3
"""Build bounded, source-auditable measurement diagnostics.

This module deliberately does not alter the FY2023 Indonesia main sample.
It uses existing or newly archived source extracts to quantify three limited
questions: (1) Tokopedia's gross-revenue/incentive/net-revenue reconciliation,
(2) Grab's issuer-disclosed reported versus comparable growth rates, and
(3) whether alternative external estimates place the Shopee market-total
anchor in a similar broad range.  None of these diagnostics validates a
country allocation or creates additional Indonesia platform observations.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTRACTS = ROOT / "10_MEASUREMENT_RECONCILIATION" / "source_extracts"
OUT = ROOT / "10_MEASUREMENT_RECONCILIATION" / "results"


def read_csv(name: str) -> list[dict[str, str]]:
    with (EXTRACTS / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def value(rows: list[dict[str, str]], period: str, component: str) -> float:
    for row in rows:
        if row["period"] == period and row["component"] == component:
            return float(row["value_idr_million"])
    raise KeyError((period, component))


def main() -> None:
    tokopedia = read_csv("tokopedia_fy2022_2023_revenue_components.csv")
    gross_22 = value(tokopedia, "FY2022", "third_party_gross_revenue")
    gross_23 = value(tokopedia, "FY2023", "third_party_gross_revenue")
    incentives_22 = value(tokopedia, "FY2022", "customer_incentives")
    incentives_23 = value(tokopedia, "FY2023", "customer_incentives")
    net_22 = value(tokopedia, "FY2022", "third_party_net_revenue")
    net_23 = value(tokopedia, "FY2023", "third_party_net_revenue")

    gross_change = gross_23 - gross_22
    incentive_reduction = incentives_23 - incentives_22
    net_change = net_23 - net_22
    if round(gross_change + incentive_reduction, 6) != round(net_change, 6):
        raise AssertionError("Tokopedia net-revenue reconciliation failed")
    write_csv(
        "tokopedia_fy2022_2023_revenue_incentive_reconciliation.csv",
        [
            {
                "platform": "Tokopedia e-commerce segment",
                "period_change": "FY2022_to_FY2023",
                "gross_revenue_change_idr_million": gross_change,
                "incentive_reduction_idr_million": incentive_reduction,
                "net_revenue_change_idr_million": net_change,
                "gross_revenue_share_of_net_change": gross_change / net_change,
                "incentive_reduction_share_of_net_change": incentive_reduction / net_change,
                "identity": "net revenue change = gross revenue change + reduction in incentives",
                "interpretation_limit": "Arithmetic reconciliation only; it is not a causal decomposition or an Indonesia-geographic claim.",
            }
        ],
    )

    grab = read_csv("grab_fy2023_reporting_scope_comparison.csv")
    grouped: dict[str, dict[str, float]] = {}
    for row in grab:
        grouped.setdefault(row["metric"], {})[row["comparison_basis"]] = float(row["reported_value"])
    growth_rows = []
    for metric, basis in grouped.items():
        reported = basis["reported_FY2023_vs_FY2022"]
        comparable = basis["as_if_Q4_2022_business_model_change_had_occurred_in_2022"]
        growth_rows.append(
            {
                "platform": "Grab",
                "period": "FY2023",
                "metric": metric,
                "reported_growth_percent": reported,
                "issuer_comparable_growth_percent": comparable,
                "difference_percentage_points": reported - comparable,
                "interpretation_limit": "Issuer-reported Group comparison; it documents definition dependence, not an Indonesia-specific effect.",
            }
        )
    write_csv("grab_fy2023_reporting_scope_comparison.csv", growth_rows)

    triangulation = read_csv("external_scope_triangulation_2023.csv")
    market = [float(r["value_usd_billion"]) for r in triangulation if r["construct"] in {"Indonesia e-commerce market GMV", "Indonesia e-commerce market estimate", "Indonesia e-commerce GMV estimate"}]
    baseline = market[0]
    market_rows = []
    for row in triangulation:
        if row["construct"] in {"Indonesia e-commerce market GMV", "Indonesia e-commerce market estimate", "Indonesia e-commerce GMV estimate"}:
            v = float(row["value_usd_billion"])
            market_rows.append(
                {
                    "check": "Indonesia_ecommerce_market_total",
                    "source_construct": row["construct"],
                    "value_usd_billion": v,
                    "difference_from_main_anchor_usd_billion": v - baseline,
                    "difference_from_main_anchor_percent": (v / baseline - 1) * 100,
                    "interpretation_limit": row["what_it_cannot_test"],
                }
            )
    food_total = next(float(r["value_usd_billion"]) for r in triangulation if r["check_id"] == "grabfood_component")
    food_share = next(float(r["value_usd_billion"]) for r in triangulation if r["check_id"] == "grabfood_share")
    grab_total = 5.381397
    market_rows.append(
        {
            "check": "GrabFood_component_floor",
            "source_construct": "Indonesia_food_delivery_GMV_times_GrabFood_share",
            "value_usd_billion": food_total * food_share,
            "difference_from_main_anchor_usd_billion": grab_total - food_total * food_share,
            "difference_from_main_anchor_percent": (grab_total / (food_total * food_share) - 1) * 100,
            "interpretation_limit": "A partial-service lower-bound comparison only. It cannot validate the Group-rate allocation used to derive Grab Indonesia GTV.",
        }
    )
    write_csv("external_scope_triangulation_results.csv", market_rows)
    print("PASS: wrote bounded source-auditable reconciliation diagnostics.")


if __name__ == "__main__":
    main()
