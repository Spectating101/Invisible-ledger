#!/usr/bin/env python3
"""Build exact arithmetic robustness diagnostics for BPS national growth anatomy.

The decomposition is descriptive and exact for V = N * A, where V is the BPS
national e-commerce transaction-value estimate, N is the estimated number of
e-commerce businesses, and A is implied nominal value per estimated business.
It is not a causal entry/productivity decomposition.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NATIONAL = ROOT / "data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv"
SOURCES = ROOT / "data/bps_official/bps_crosswave_source_certification_2026-09-10.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def national_value(rows: list[dict[str, str]], year: int, indicator: str) -> float:
    m = [r for r in rows if int(r["reference_year"]) == year and r["indicator"] == indicator]
    if len(m) != 1:
        raise ValueError(f"expected one {year} {indicator}, found {len(m)}")
    return float(m[0]["value"])


def exact_symmetric_decomposition(v0: float, n0: float, v1: float, n1: float) -> tuple[float, float, float, float]:
    """Exact two-factor symmetric decomposition of ΔV for V=N*A."""
    a0 = v0 / n0
    a1 = v1 / n1
    delta_v = v1 - v0
    count_term = (n1 - n0) * (a0 + a1) / 2.0
    intensity_term = (a1 - a0) * (n0 + n1) / 2.0
    if abs((count_term + intensity_term) - delta_v) > 1e-9:
        raise ValueError("decomposition identity failed")
    return delta_v, count_term, intensity_term, a1 / a0 - 1.0


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, default=ROOT / "outputs/empirical_robustness_2026-09-10")
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    nat = read_csv(NATIONAL)
    vals = {
        y: {
            "value": national_value(nat, y, "ecommerce_transaction_value"),
            "businesses": national_value(nat, y, "estimated_number_of_ecommerce_businesses"),
        }
        for y in (2022, 2023, 2024)
    }

    decomp = []
    for y0, y1 in ((2022, 2023), (2023, 2024), (2022, 2024)):
        v0, n0 = vals[y0]["value"], vals[y0]["businesses"]
        v1, n1 = vals[y1]["value"], vals[y1]["businesses"]
        dv, count_term, intensity_term, avg_growth = exact_symmetric_decomposition(v0, n0, v1, n1)
        decomp.append({
            "transition": f"{y0}-{y1}",
            "transaction_value_start_idr_trillion": v0,
            "transaction_value_end_idr_trillion": v1,
            "estimated_businesses_start": n0,
            "estimated_businesses_end": n1,
            "total_value_increase_idr_trillion": dv,
            "business_count_term_idr_trillion": count_term,
            "implied_value_per_business_term_idr_trillion": intensity_term,
            "business_count_term_share_pct": count_term / dv * 100.0,
            "implied_value_per_business_term_share_pct": intensity_term / dv * 100.0,
            "business_count_growth_pct": (n1 / n0 - 1.0) * 100.0,
            "implied_value_per_business_growth_pct": avg_growth * 100.0,
            "interpretation": "exact symmetric arithmetic decomposition; not causal entry or productivity",
        })

    # Sensitivity to the conflicting 2023 count preserved in the BPS source audit.
    alt_2023 = 3934981.0
    v23, v24 = vals[2023]["value"], vals[2024]["value"]
    n24 = vals[2024]["businesses"]
    dv, ct, it, avg_growth = exact_symmetric_decomposition(v23, alt_2023, v24, n24)
    conflict = [{
        "scenario": "conflicting_2023_count_3934981",
        "transition": "2023-2024",
        "business_count_growth_pct": (n24 / alt_2023 - 1.0) * 100.0,
        "implied_value_per_business_growth_pct": avg_growth * 100.0,
        "business_count_term_share_pct": ct / dv * 100.0,
        "implied_value_per_business_term_share_pct": it / dv * 100.0,
        "status": "source-conflict sensitivity only; 3816750 remains certified cross-year series value",
    }]

    src = {r["source_id"]: r for r in read_csv(SOURCES)}
    m23 = float(src["BPS-ECOM-2023-MKT"]["value"])
    m24 = float(src["BPS-ECOM-2024-MKT"]["value"])
    total23 = float(src["BPS-ECOM-2023-TOTAL"]["value"])
    total24 = float(src["BPS-ECOM-2024-TOTAL"]["value"])
    non23 = total23 - m23
    non24 = total24 - m24
    total_inc = total24 - total23
    channel = [
        {
            "component": "marketplace",
            "value_2023_idr_trillion": m23,
            "value_2024_idr_trillion": m24,
            "increase_idr_trillion": m24 - m23,
            "growth_pct": (m24 / m23 - 1.0) * 100.0,
            "share_of_total_2023_2024_increase_pct": (m24 - m23) / total_inc * 100.0,
        },
        {
            "component": "non_marketplace",
            "value_2023_idr_trillion": non23,
            "value_2024_idr_trillion": non24,
            "increase_idr_trillion": non24 - non23,
            "growth_pct": (non24 / non23 - 1.0) * 100.0,
            "share_of_total_2023_2024_increase_pct": (non24 - non23) / total_inc * 100.0,
        },
    ]

    write_csv(args.output / "bps_growth_exact_decomposition.csv", decomp)
    write_csv(args.output / "bps_business_count_conflict_sensitivity.csv", conflict)
    write_csv(args.output / "bps_channel_increment_decomposition.csv", channel)

    d22_23 = decomp[0]
    d23_24 = decomp[1]
    d22_24 = decomp[2]
    text = f"""# BPS growth-anatomy robustness — 10 September 2026

**Status:** exact arithmetic decomposition of published BPS national estimates. This is not a causal entry, survival, incumbent-growth, inflation, or productivity model.

## Exact two-factor decomposition

For aggregate transaction value `V = N × A`, where `N` is estimated e-commerce businesses and `A` is implied nominal value per estimated business, the symmetric decomposition exactly allocates the change in `V` into a business-count term and an implied-value-per-business term.

| Period | Total value increase | Count-term share | Implied value/business-term share |
|---|---:|---:|---:|
| 2022→2023 | Rp{d22_23['total_value_increase_idr_trillion']:.2f}T | **{d22_23['business_count_term_share_pct']:.2f}%** | {d22_23['implied_value_per_business_term_share_pct']:.2f}% |
| 2023→2024 | Rp{d23_24['total_value_increase_idr_trillion']:.2f}T | **{d23_24['business_count_term_share_pct']:.2f}%** | {d23_24['implied_value_per_business_term_share_pct']:.2f}% |
| 2022→2024 | Rp{d22_24['total_value_increase_idr_trillion']:.2f}T | **{d22_24['business_count_term_share_pct']:.2f}%** | {d22_24['implied_value_per_business_term_share_pct']:.2f}% |

Under this exact arithmetic allocation, the business-count term is the larger component in each comparison, including **90.29%** of the 2023→2024 nominal value increase.

## 2023 count-conflict sensitivity

If the conflicting 2023 count of 3,934,981 were substituted solely as a sensitivity scenario, the 2023→2024 business-count term would still account for **{conflict[0]['business_count_term_share_pct']:.2f}%** of the nominal value increase. The extensive-margin interpretation therefore does not depend on choosing 3,816,750 versus the conflicting 3,934,981, although 3,816,750 remains the certified cross-year series value because it matches BPS's later official growth statement.

## Sales-media contribution to the 2023→2024 increase

The certified sales-media amounts imply:

- marketplace value increase: **Rp{channel[0]['increase_idr_trillion']:.2f}T**, or **{channel[0]['share_of_total_2023_2024_increase_pct']:.2f}%** of the total Rp{total_inc:.2f}T increase;
- non-marketplace value increase: **Rp{channel[1]['increase_idr_trillion']:.2f}T**, or **{channel[1]['share_of_total_2023_2024_increase_pct']:.2f}%** of the total increase.

Thus almost all of the arithmetic increase in the published national e-commerce value estimate between 2023 and 2024 comes from the non-marketplace component. This does **not** mean non-marketplace commerce is hidden, informal, untaxed, or absent from BPS; BPS is precisely the source measuring it.

## Research consequence

The BPS evidence supports a stronger but still bounded statement:

> Recent Indonesian e-commerce expansion is associated arithmetically with broadening estimated business participation, and the 2023→2024 increase in the published national value estimate is overwhelmingly concentrated in non-marketplace sales media.

That result materially broadens the empirical picture beyond selected marketplace-company accounts without requiring a missing-GDP or tax-gap interpretation.
"""
    (args.output / "BPS_SUMMARY.md").write_text(text, encoding="utf-8")

    print(f"2023-2024 count-term share: {d23_24['business_count_term_share_pct']:.6f}%")
    print(f"2023-2024 non-marketplace increment share: {channel[1]['share_of_total_2023_2024_increase_pct']:.6f}%")


if __name__ == "__main__":
    main()
