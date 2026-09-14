#!/usr/bin/env python3
"""Build a non-pooled longitudinal comparison of transaction activity and revenue.

This analysis is deliberately supplementary. It compares adjacent years only within
one issuer/segment series, keeps direct candidate series separate from conditional
country reconstructions, and never sums levels across currencies or business scopes.

It also hard-excludes the known-invalid Tokopedia FY2021 pairing.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def one(rows: list[dict[str, str]], predicate, label: str) -> dict[str, str]:
    matches = [r for r in rows if predicate(r)]
    if len(matches) != 1:
        raise ValueError(f"{label}: expected one row, found {len(matches)}")
    return matches[0]


def pct_growth(new: float, old: float) -> float:
    if not math.isfinite(new) or not math.isfinite(old) or old <= 0:
        raise ValueError("growth requires finite values and a positive base")
    return (new / old - 1.0) * 100.0


def classify(activity_growth: float, revenue_growth: float) -> str:
    if activity_growth >= 0 and revenue_growth >= 0:
        return "activity_up_revenue_up"
    if activity_growth >= 0 and revenue_growth < 0:
        return "activity_up_revenue_down"
    if activity_growth < 0 and revenue_growth >= 0:
        return "activity_down_revenue_up"
    return "activity_down_revenue_down"


def load_series() -> tuple[list[dict], list[dict]]:
    """Return annual series rows and explicit exclusions."""
    rows: list[dict] = []
    exclusions: list[dict] = []

    # Blibli 3P Retail: one canonical annual vintage per year. 2020 comes from
    # the prospectus in IDR million and is converted to IDR billion. Later years
    # use reviewed issuer tables. Geography/business-scope admission remains pending.
    prospectus = read_csv(ROOT / "data/longitudinal/blibli_prospectus_2019_2020_candidates.csv")
    r = one(
        prospectus,
        lambda x: x["scope"] == "3P Retail" and x["year"] == "2020",
        "Blibli 3P FY2020",
    )
    rows.append({
        "platform": "Blibli/GDN",
        "scope": "3P Retail",
        "year": 2020,
        "transaction_value": float(r["tpv_idr_million"]) / 1000.0,
        "revenue_value": float(r["net_revenue_idr_million"]) / 1000.0,
        "currency_unit": "IDR billion",
        "evidence_class": "direct_candidate",
        "geography_status": "scope_pending; 3P includes online travel",
        "source_dataset": "data/longitudinal/blibli_prospectus_2019_2020_candidates.csv",
        "source_vintage": "prospectus",
    })

    blibli = read_csv(ROOT / "data/longitudinal/blibli_reported_pairs_all_vintages.csv")
    selections = {
        2021: ("2021FY", "blibli_fy2022_linked_0"),
        2022: ("2022FY", "blibli_fy2022_linked_0"),
        2023: ("2023FY", "blibli_fy2024_linked_0"),
        2024: ("2024FY", "blibli_fy2025_linked_0"),
        2025: ("2025FY", "blibli_fy2025_linked_0"),
    }
    for year, (period, source_id) in selections.items():
        r = one(
            blibli,
            lambda x, p=period, s=source_id: (
                x["scope"] == "3P Retail"
                and x["frequency"] == "annual"
                and x["period"] == p
                and x["source_id"] == s
            ),
            f"Blibli 3P FY{year}",
        )
        rows.append({
            "platform": "Blibli/GDN",
            "scope": "3P Retail",
            "year": year,
            "transaction_value": float(r["tpv"]),
            "revenue_value": float(r["revenue"]),
            "currency_unit": "IDR billion",
            "evidence_class": "direct_candidate",
            "geography_status": "scope_pending; 3P includes online travel",
            "source_dataset": "data/longitudinal/blibli_reported_pairs_all_vintages.csv",
            "source_vintage": source_id,
        })

    # Bukalapak: direct Group pairs with matched twelve-month periods only.
    # They remain geography-pending because overseas operations are disclosed.
    bukalapak = read_csv(ROOT / "data/longitudinal/bukalapak_annual_candidates.csv")
    for r in bukalapak:
        year = int(r["year"])
        if year == 2024:
            exclusions.append({
                "platform": "Bukalapak",
                "period": "FY2024",
                "reason": "transaction value covers 9 months while revenue covers 12 months",
                "source_dataset": "data/longitudinal/bukalapak_annual_candidates.csv",
            })
            continue
        if int(r["tpv_months"]) != 12 or int(r["revenue_months"]) != 12:
            raise ValueError(f"Bukalapak FY{year}: unexpected period mismatch")
        rows.append({
            "platform": "Bukalapak",
            "scope": "Group",
            "year": year,
            "transaction_value": float(r["tpv_idr_million"]),
            "revenue_value": float(r["revenue_idr_million"]),
            "currency_unit": "IDR million",
            "evidence_class": "direct_candidate",
            "geography_status": "geography_pending; Group includes overseas operations",
            "source_dataset": "data/longitudinal/bukalapak_annual_candidates.csv",
            "source_vintage": Path(r["source_file"]).name,
        })

    # Original Indonesia extension. Tokopedia FY2021 is explicitly excluded here:
    # full-year pro-forma transaction value was paired with post-acquisition revenue.
    extension = read_csv(ROOT / "data/longitudinal/indonesia_platform_year_extension.csv")
    for r in extension:
        platform = r["platform"]
        year = int(r["period"].replace("FY", ""))
        if platform.startswith("Tokopedia"):
            if year == 2021:
                exclusions.append({
                    "platform": "Tokopedia e-commerce segment",
                    "period": "FY2021",
                    "reason": "exclude: full-year pro-forma transaction value paired with post-acquisition revenue",
                    "source_dataset": "data/longitudinal/indonesia_platform_year_extension.csv",
                })
                continue
            rows.append({
                "platform": "Tokopedia",
                "scope": "e-commerce segment",
                "year": year,
                "transaction_value": float(r["transaction_value_native"]),
                "revenue_value": float(r["platform_revenue_native"]),
                "currency_unit": r["unit"],
                "evidence_class": "direct_candidate",
                "geography_status": "Indonesia-aligned segment; not explicit geographic line",
                "source_dataset": "data/longitudinal/indonesia_platform_year_extension.csv",
                "source_vintage": "reviewed extension",
            })
        elif platform == "Grab":
            rows.append({
                "platform": "Grab",
                "scope": "Indonesia country allocation",
                "year": year,
                "transaction_value": float(r["transaction_value_native"]),
                "revenue_value": float(r["platform_revenue_native"]),
                "currency_unit": r["unit"],
                "evidence_class": "conditional_country_reconstruction",
                "geography_status": "Indonesia revenue direct; transaction value derived from Group monetization rate",
                "source_dataset": "data/longitudinal/indonesia_platform_year_extension.csv",
                "source_vintage": "reviewed extension",
            })
        elif platform == "Shopee":
            rows.append({
                "platform": "Shopee",
                "scope": "Indonesia country allocation",
                "year": year,
                "transaction_value": float(r["transaction_value_native"]),
                "revenue_value": float(r["platform_revenue_native"]),
                "currency_unit": r["unit"],
                "evidence_class": "conditional_country_reconstruction",
                "geography_status": "country GMV external; revenue derived using company-wide service rate",
                "source_dataset": "data/longitudinal/indonesia_platform_year_extension.csv",
                "source_vintage": "reviewed extension",
            })

    return rows, exclusions


def build_transitions(series_rows: list[dict]) -> list[dict]:
    grouped: dict[tuple[str, str, str], list[dict]] = {}
    for r in series_rows:
        key = (r["platform"], r["scope"], r["evidence_class"])
        grouped.setdefault(key, []).append(r)

    transitions: list[dict] = []
    for key, group in sorted(grouped.items()):
        group = sorted(group, key=lambda x: x["year"])
        years = [r["year"] for r in group]
        if len(years) != len(set(years)):
            raise ValueError(f"duplicate years in series {key}: {years}")
        for a, b in zip(group, group[1:]):
            if b["year"] != a["year"] + 1:
                # Do not fabricate annual changes across gaps.
                continue
            ag = pct_growth(b["transaction_value"], a["transaction_value"])
            rg = pct_growth(b["revenue_value"], a["revenue_value"])
            m0 = a["revenue_value"] / a["transaction_value"] * 100.0
            m1 = b["revenue_value"] / b["transaction_value"] * 100.0
            transitions.append({
                "platform": a["platform"],
                "scope": a["scope"],
                "evidence_class": a["evidence_class"],
                "from_year": a["year"],
                "to_year": b["year"],
                "activity_growth_pct": ag,
                "revenue_growth_pct": rg,
                "revenue_minus_activity_growth_pp": rg - ag,
                "abs_growth_gap_pp": abs(rg - ag),
                "monetization_start_pct": m0,
                "monetization_end_pct": m1,
                "monetization_change_pp": m1 - m0,
                "movement_pattern": classify(ag, rg),
                "geography_status": a["geography_status"],
                "source_dataset_start": a["source_dataset"],
                "source_dataset_end": b["source_dataset"],
            })
    return transitions


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"no rows for {path}")
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def fmt(x: float) -> str:
    return f"{x:.2f}"


def build_summary(transitions: list[dict], exclusions: list[dict]) -> str:
    direct = [r for r in transitions if r["evidence_class"] == "direct_candidate"]
    conditional = [r for r in transitions if r["evidence_class"] == "conditional_country_reconstruction"]
    reversals = [
        r for r in direct
        if r["movement_pattern"] in {"activity_up_revenue_down", "activity_down_revenue_up"}
    ]
    revenue_outpaces = [r for r in direct if r["revenue_growth_pct"] > r["activity_growth_pct"]]
    activity_outpaces = [r for r in direct if r["activity_growth_pct"] > r["revenue_growth_pct"]]

    lines = [
        "# Issuer movement bridge — research checkpoint",
        "",
        "This is a supplementary within-series analysis, not an approved main sample. "
        "Levels are never pooled across currencies, issuers, segments, or directness classes.",
        "",
        "## Main descriptive result",
        "",
        f"The direct-candidate series yield **{len(direct)} adjacent annual transitions**. "
        f"Recognized-revenue growth exceeds transaction-activity growth in **{len(revenue_outpaces)}**; "
        f"transaction growth exceeds revenue growth in **{len(activity_outpaces)}**. "
        f"In **{len(reversals)}** transitions the two measures move in opposite directions. "
        f"The median absolute difference between their annual growth rates is **{fmt(median(r['abs_growth_gap_pp'] for r in direct))} percentage points**. "
        "These are descriptive counts across heterogeneous candidate series, not a pooled estimator or significance test.",
        "",
        "The economically relevant implication is bounded: **recognized platform/segment revenue is not a stable one-for-one proxy for the movement of the transaction activity it accompanies.** "
        "The difference can reflect monetization, incentives, business mix, accounting scope, or genuine business-model change.",
        "",
        "## Direct sign reversals",
        "",
        "| Series | Period | Activity growth | Revenue growth | Monetization change |",
        "|---|---:|---:|---:|---:|",
    ]
    for r in reversals:
        lines.append(
            f"| {r['platform']} — {r['scope']} | {r['from_year']}→{r['to_year']} | "
            f"{fmt(r['activity_growth_pct'])}% | {fmt(r['revenue_growth_pct'])}% | "
            f"{fmt(r['monetization_change_pp'])} pp |"
        )

    lines += [
        "",
        "Tokopedia FY2022→FY2023 is especially informative because an existing reconciliation shows that "
        "60.56% of the arithmetic increase in net revenue is associated with lower customer incentives and 39.44% with higher gross revenue. "
        "Thus the direct segment's transaction value can fall while net recognized revenue rises without implying that underlying commerce grew in the same direction as revenue.",
        "",
        "## Conditional Indonesia reconstructions",
        "",
        f"The Grab/Shopee conditional series contribute **{len(conditional)} adjacent transitions**. "
        "They are reported separately because their country transaction/revenue pairs depend on Group monetization rates and/or external market estimates. "
        "They are useful sensitivity cases but do not independently validate the direct-series result.",
        "",
        "## Explicit exclusions",
        "",
    ]
    for r in exclusions:
        lines.append(f"- **{r['platform']} {r['period']}** — {r['reason']}.")

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "This result does **not** establish hidden income, missing GDP, tax non-compliance, or a universal revenue/transaction relationship. "
        "It establishes a narrower but economically useful point for the thesis: when the object of interest is the surrounding commercial activity, corporate recognized revenue can change substantially faster, slower, or even in the opposite direction. "
        "That makes the choice of ledger consequential for how growth is described.",
        "",
        "## Remaining admission caveats",
        "",
        "- Blibli 3P includes online travel and is not yet approved as a strict Indonesia goods-marketplace series.",
        "- Bukalapak Group includes overseas activity.",
        "- Tokopedia is Indonesia-aligned but not an explicit country line.",
        "- No cross-series level aggregation is used here.",
        "- Final thesis promotion still requires the advisor-approved sample rule.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "research/issuer_movement_bridge/results",
    )
    args = parser.parse_args()

    series_rows, exclusions = load_series()
    transitions = build_transitions(series_rows)

    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "annual_series.csv", series_rows)
    write_csv(out / "adjacent_growth_transitions.csv", transitions)
    write_csv(out / "exclusions.csv", exclusions)
    (out / "SUMMARY.md").write_text(build_summary(transitions, exclusions), encoding="utf-8")

    print(f"series rows: {len(series_rows)}")
    print(f"adjacent transitions: {len(transitions)}")
    print(f"exclusions: {len(exclusions)}")


if __name__ == "__main__":
    main()
