#!/usr/bin/env python3
"""Build robustness diagnostics for the certified Indonesia direct-candidate series.

This module does not choose the final thesis sample. It asks a narrower question:
is the descriptive transaction-versus-revenue divergence in the current direct
candidate inventory being driven entirely by one extreme transition, one
platform series, or the ordinary percentage-growth transformation?

Inputs are the certified advisor-facing candidate table. Conditional Grab and
Shopee reconstructions are excluded from the direct-candidate robustness set.
"""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv"

DIRECT_ADMISSIONS = {
    "candidate_scope_pending",
    "candidate_geography_pending",
    "strongest_direct_candidate",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"no rows for {path}")
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def pct_growth(new: float, old: float) -> float:
    if old <= 0 or new <= 0:
        raise ValueError("positive values required for retained robustness transitions")
    return (new / old - 1.0) * 100.0


def log_growth(new: float, old: float) -> float:
    if old <= 0 or new <= 0:
        raise ValueError("positive values required for log growth")
    return 100.0 * math.log(new / old)


def canonical_platform(name: str) -> str:
    if name == "Blibli/GDN":
        return "Blibli"
    return name


def build_direct_levels() -> list[dict]:
    rows = read_csv(SOURCE)
    levels = []
    for r in rows:
        if r["certified_admission"] not in DIRECT_ADMISSIONS:
            continue
        if r["ratio_status"] != "eligible_direct_pair":
            # Blibli FY2019 is retained in the candidate census but has negative
            # net revenue and cannot define a positive-base growth transition.
            continue
        levels.append(
            {
                "record_id": r["record_id"],
                "platform": canonical_platform(r["platform"]),
                "business_scope": r["business_scope"],
                "year": int(r["period"].replace("FY", "")),
                "transaction_value": float(r["transaction_value"]),
                "revenue_value": float(r["revenue_value"]),
                "evidence_tier": r["evidence_tier"],
                "certified_admission": r["certified_admission"],
                "key_caveat": r["key_caveat"],
            }
        )
    return levels


def build_transitions(levels: list[dict]) -> list[dict]:
    groups: dict[tuple[str, str], list[dict]] = {}
    for r in levels:
        groups.setdefault((r["platform"], r["business_scope"]), []).append(r)

    out = []
    for (platform, scope), group in sorted(groups.items()):
        group = sorted(group, key=lambda r: r["year"])
        for a, b in zip(group, group[1:]):
            if b["year"] != a["year"] + 1:
                continue
            tg = pct_growth(b["transaction_value"], a["transaction_value"])
            rg = pct_growth(b["revenue_value"], a["revenue_value"])
            tl = log_growth(b["transaction_value"], a["transaction_value"])
            rl = log_growth(b["revenue_value"], a["revenue_value"])
            out.append(
                {
                    "transition_id": f"{platform}_{a['year']}_{b['year']}",
                    "platform": platform,
                    "business_scope": scope,
                    "from_year": a["year"],
                    "to_year": b["year"],
                    "transaction_growth_pct": tg,
                    "revenue_growth_pct": rg,
                    "revenue_minus_transaction_growth_pp": rg - tg,
                    "absolute_growth_gap_pp": abs(rg - tg),
                    "transaction_log_growth_x100": tl,
                    "revenue_log_growth_x100": rl,
                    "absolute_log_growth_gap_x100": abs(rl - tl),
                    "opposite_sign": (tg < 0) != (rg < 0),
                    "revenue_grows_faster": rg > tg,
                    "key_caveat": a["key_caveat"],
                }
            )
    return out


def summarize(name: str, rows: list[dict], note: str) -> dict:
    return {
        "scenario": name,
        "transitions": len(rows),
        "series": len({r["platform"] for r in rows}),
        "opposite_sign_transitions": sum(bool(r["opposite_sign"]) for r in rows),
        "revenue_grows_faster": sum(bool(r["revenue_grows_faster"]) for r in rows),
        "transaction_grows_faster": sum(not bool(r["revenue_grows_faster"]) for r in rows),
        "median_absolute_growth_gap_pp": median(r["absolute_growth_gap_pp"] for r in rows),
        "median_absolute_log_growth_gap_x100": median(r["absolute_log_growth_gap_x100"] for r in rows),
        "maximum_absolute_growth_gap_pp": max(r["absolute_growth_gap_pp"] for r in rows),
        "interpretation_note": note,
    }


def scenario_rows(transitions: list[dict]) -> list[dict]:
    out = [
        summarize(
            "all_direct_candidates",
            transitions,
            "Direct issuer/segment candidates only; final Indonesia admission remains advisor-pending.",
        )
    ]

    largest = max(transitions, key=lambda r: r["absolute_growth_gap_pp"])
    out.append(
        summarize(
            "exclude_largest_raw_gap_transition",
            [r for r in transitions if r["transition_id"] != largest["transition_id"]],
            f"Drops {largest['transition_id']}, the largest ordinary percentage-growth gap; diagnostic for extreme-base sensitivity.",
        )
    )

    platforms = sorted({r["platform"] for r in transitions})
    for excluded in platforms:
        out.append(
            summarize(
                f"leave_out_{excluded}",
                [r for r in transitions if r["platform"] != excluded],
                f"Leave-one-series-out diagnostic; removes all {excluded} transitions.",
            )
        )
    return out


def leave_one_transition_rows(transitions: list[dict]) -> list[dict]:
    out = []
    for dropped in transitions:
        kept = [r for r in transitions if r["transition_id"] != dropped["transition_id"]]
        out.append(
            {
                "dropped_transition": dropped["transition_id"],
                "remaining_transitions": len(kept),
                "remaining_reversals": sum(bool(r["opposite_sign"]) for r in kept),
                "median_absolute_growth_gap_pp": median(r["absolute_growth_gap_pp"] for r in kept),
                "median_absolute_log_growth_gap_x100": median(r["absolute_log_growth_gap_x100"] for r in kept),
            }
        )
    return out


def build_summary(transitions: list[dict], scenarios: list[dict], loo: list[dict]) -> str:
    base = next(r for r in scenarios if r["scenario"] == "all_direct_candidates")
    no_extreme = next(r for r in scenarios if r["scenario"] == "exclude_largest_raw_gap_transition")
    loo_medians = [r["median_absolute_growth_gap_pp"] for r in loo]
    leave_series = [r for r in scenarios if r["scenario"].startswith("leave_out_")]

    lines = [
        "# Indonesia longitudinal robustness — 10 September 2026",
        "",
        "**Status:** robustness diagnostic for the certified direct-candidate inventory. It does not choose the final thesis sample and does not turn scope-pending observations into Indonesia-only observations.",
        "",
        "## Question",
        "",
        "Is the observed transaction-versus-revenue divergence being driven entirely by one extreme transition, one platform series, or the ordinary percentage-growth transformation?",
        "",
        "## Baseline direct-candidate result",
        "",
        f"The retained positive-base direct candidates yield **{base['transitions']} adjacent annual transitions**, **{base['opposite_sign_transitions']} sign reversals**, and a median absolute ordinary growth-rate gap of **{base['median_absolute_growth_gap_pp']:.2f} percentage points**.",
        f"Using log changes instead of ordinary percentage growth gives a median absolute log-growth gap of **{base['median_absolute_log_growth_gap_x100']:.2f} log-points ×100**. The direction rankings and sign-reversal classification are unchanged by the monotone growth transformation.",
        "",
        "## Extreme-transition sensitivity",
        "",
        f"Dropping the single largest ordinary growth-gap transition leaves **{no_extreme['transitions']} transitions**, still **{no_extreme['opposite_sign_transitions']} sign reversals**, and a median absolute gap of **{no_extreme['median_absolute_growth_gap_pp']:.2f} percentage points**.",
        "",
        "The largest raw gap is Blibli FY2022→FY2023, where a low starting net-revenue base and major monetization/promotion changes generate an unusually large percentage-growth difference. The descriptive divergence therefore does not disappear when that observation is removed.",
        "",
        "## Leave-one-transition-out sensitivity",
        "",
        f"Across all nine leave-one-transition-out exercises, the median absolute ordinary growth gap ranges from **{min(loo_medians):.2f}pp to {max(loo_medians):.2f}pp**. No single transition is necessary for the qualitative conclusion that transaction and revenue growth can differ materially.",
        "",
        "## Leave-one-series-out sensitivity",
        "",
        "| Excluded series | Remaining transitions | Reversals | Median abs. ordinary gap | Median abs. log gap |",
        "|---|---:|---:|---:|---:|",
    ]
    for r in leave_series:
        name = r["scenario"].replace("leave_out_", "")
        lines.append(
            f"| {name} | {r['transitions']} | {r['opposite_sign_transitions']} | {r['median_absolute_growth_gap_pp']:.2f}pp | {r['median_absolute_log_growth_gap_x100']:.2f} |"
        )

    lines += [
        "",
        "Every leave-one-series-out construction retains at least one sign reversal and a non-trivial median growth gap. This means the descriptive non-equivalence is not mechanically dependent on one platform series. However, the **geographic/business-scope quality changes sharply across these scenarios**, so this is robustness of the measurement phenomenon—not evidence of a representative Indonesia population effect.",
        "",
        "## What this strengthens",
        "",
        "> The direct-candidate result is not solely an artifact of the single largest percentage-growth observation, a single issuer series, or the use of ordinary percentage growth rather than log change.",
        "",
        "## What it does not strengthen",
        "",
        "- It does not resolve whether Blibli 3P belongs in the final Indonesia sample.",
        "- It does not resolve Bukalapak's overseas Group scope.",
        "- It does not make Tokopedia a literal country geographic line.",
        "- It does not establish a population mean effect, statistical treatment effect, missing GDP, hidden income, or tax gap.",
        "- The small candidate count means these summaries should remain descriptive robustness diagnostics rather than conventional inferential statistics.",
        "",
        "## Decision consequence",
        "",
        "The empirical question for Professor Kong is now less about whether the divergence disappears under obvious robustness checks and more about **which business/geographic boundary is acceptable for the thesis's Indonesia longitudinal design**.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "outputs/empirical_robustness_2026-09-10")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    levels = build_direct_levels()
    transitions = build_transitions(levels)
    if len(transitions) != 9:
        raise ValueError(f"expected 9 direct transitions, found {len(transitions)}")
    scenarios = scenario_rows(transitions)
    loo = leave_one_transition_rows(transitions)

    write_csv(args.output / "direct_transition_metrics.csv", transitions)
    write_csv(args.output / "robustness_scenarios.csv", scenarios)
    write_csv(args.output / "leave_one_transition_out.csv", loo)
    (args.output / "SUMMARY.md").write_text(build_summary(transitions, scenarios, loo), encoding="utf-8")

    print(f"direct transitions: {len(transitions)}")
    print(f"sign reversals: {sum(bool(r['opposite_sign']) for r in transitions)}")
    print(f"median ordinary gap: {median(r['absolute_growth_gap_pp'] for r in transitions):.6f}pp")
    print(f"median log gap: {median(r['absolute_log_growth_gap_x100'] for r in transitions):.6f}")


if __name__ == "__main__":
    main()
