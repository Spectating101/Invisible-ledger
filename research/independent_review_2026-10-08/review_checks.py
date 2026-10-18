#!/usr/bin/env python3
"""Exploratory review checks, designed after inspecting the October results.

Run from any directory: python3 research/independent_review_2026-10-08/review_checks.py
Reads committed aggregates only. Writes results.json beside this script.
No proposal, preregistration, source extract or approved sample is changed.
The synthetic seller example is an arithmetic demonstration, not survey evidence.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess

import numpy as np
import pandas as pd
from scipy import stats


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLES = ROOT / "research/option_space_2026-10-01/tables"
INPUTS = [
    "transitions_master.csv", "l_panel.csv", "spinoff_panel.csv",
    "h1_extended_results.json", "bps_rise_accounting.json", "gel_checks.json",
    "m1_market_value_results.json",
]


def annual_log_changes(levels: pd.DataFrame) -> pd.DataFrame:
    d = levels.sort_values(["firm", "year"]).copy()
    d = d[(d.V > 0) & (d.R > 0)]
    assert not d.duplicated(["firm", "year"]).any()
    d["m"] = d.R / d.V
    previous = d.groupby("firm").m.shift()
    consecutive = d.groupby("firm").year.diff() == 1
    d["dlnm"] = np.where(consecutive, np.log(d.m / previous), np.nan)
    return d.dropna(subset=["dlnm"])[["firm", "year", "dlnm"]]


def compare(a: pd.Series, b: pd.Series) -> dict:
    """Exact one-sided label permutations for two declared statistics.

    The mean statistic follows build_numbers.py; the median statistic follows
    h1_extended.py. Exact enumeration removes Monte Carlo variation only.
    Exchangeability remains an assumption in this purposive heterogeneous sample.
    """
    xa, xb = a.to_numpy(), b.to_numpy()
    pool = np.concatenate([xa, xb])
    k = len(xa)
    positions = np.asarray(list(itertools.combinations(range(len(pool)), k)))
    selected = pool[positions]
    # Median difference needs each allocation's complement, not only its first group.
    complements = np.asarray([
        np.delete(pool, indices) for indices in positions
    ])
    observed_mean = float(xa.mean() - xb.mean())
    observed_median = float(np.median(xa) - np.median(xb))
    distribution_mean = selected.mean(axis=1) - complements.mean(axis=1)
    distribution_median = np.median(selected, axis=1) - np.median(complements, axis=1)
    mw = stats.mannwhitneyu(xa, xb, alternative="greater")
    return {
        "units_a": len(xa), "units_b": len(xb),
        "median_a": float(np.median(xa)), "median_b": float(np.median(xb)),
        "mann_whitney_one_sided_p": float(mw.pvalue),
        "exact_permutation_mean_difference_p": float(np.mean(distribution_mean >= observed_mean - 1e-12)),
        "exact_permutation_median_difference_p": float(np.mean(distribution_median >= observed_median - 1e-12)),
        "allocations": len(positions),
        "values_a": {str(key): float(value) for key, value in a.items()},
    }


def issuer_sensitivity() -> dict:
    t = pd.read_csv(TABLES / "transitions_master.csv")
    p = pd.read_csv(TABLES / "l_panel.csv")
    s = pd.read_csv(TABLES / "spinoff_panel.csv")
    core = t[t["set"] == "IDN_main"][["firm", "dlnm"]]
    grab = p[p.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab on-demand")
    goto = p[(p.firm == "GoTo") & (p.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo on-demand")
    regional = annual_log_changes(pd.concat([grab, goto], ignore_index=True))[["firm", "dlnm"]]
    target = pd.concat([core, regional], ignore_index=True).assign(abs_change=lambda d: d.dlnm.abs())
    old = t[t["set"] == "EXT_clean"][["firm", "dlnm"]]
    new = s[(s.flag_1p != "exclude") & s.g_m.notna()].rename(columns={"entity": "firm", "g_m": "dlnm"})[["firm", "dlnm"]]
    assert set(old.firm).isdisjoint(new.firm), "benchmark aliases/overlap require review"
    foreign = pd.concat([old, new], ignore_index=True).assign(abs_change=lambda d: d.dlnm.abs()).groupby("firm").abs_change.median()
    segment_medians = target.groupby("firm").abs_change.median()
    expected = json.loads((TABLES / "h1_extended_results.json").read_text())["A_vs_all_foreign"]
    assert len(segment_medians) == expected["firms_a"] == 5
    assert len(foreign) == expected["firms_b"] == 27
    assert math.isclose(segment_medians.median(), expected["median_a"], abs_tol=1e-12)
    assert math.isclose(foreign.median(), expected["median_b"], abs_tol=1e-12)

    parent = {"Tokopedia e-commerce segment": "GoTo issuer", "GoTo on-demand": "GoTo issuer"}
    # These summarize change magnitudes, not pooled accounting levels.
    pooled = target.assign(issuer=lambda d: d.firm.replace(parent)).groupby("issuer").abs_change.median()
    equal_segments = segment_medians.rename(index=parent).groupby(level=0).mean()
    main_only = target[target.firm.isin(core.firm)].groupby("firm").abs_change.median()
    return {
        "metric": "absolute annual change in log(R/V)",
        "scope": "Indonesia-aligned main series plus regional on-demand series; not country-only observations",
        "shared_issuer_rule": "Tokopedia and GoTo on-demand grouped as GoTo; remaining series each form one issuer unit",
        "summary_rules": {
            "pooled_transition_median": "median across all observed segment transitions within each issuer",
            "equal_segment_mean": "mean of segment medians within an issuer, giving each segment equal weight",
        },
        "variants": {
            "original_five_segment_labels": compare(segment_medians, foreign),
            "four_issuers_pooled_transition_median": compare(pooled, foreign),
            "four_issuers_equal_segment_mean": compare(equal_segments, foreign),
            "core_three_series_vs_expanded_benchmark": compare(main_only, foreign),
        },
        "limits": [
            "Post-result sensitivity, not preregistered confirmation.",
            "Issuer aggregation is a robustness summary, not a formally fitted dependence model.",
            "Reporting periods, geographies and business models remain heterogeneous.",
            "Neither permutation statistic is universally the stricter test.",
            "GoTo on-demand's 2022 GTV is estimated in the input panel and remains labelled as such.",
        ],
    }


def returning_seller_sensitivity() -> dict:
    rise = json.loads((TABLES / "bps_rise_accounting.json").read_text())
    gap = rise["pre_2023_above_2022_count_k"]
    baseline = rise["scenarios"]["reference"]["stopped_k"] / (rise["reference_exit_rate_pct"] / 100)
    scenarios = {}
    for name, scenario in rise["scenarios"].items():
        residual_before_returns = gap + scenario["stopped_k"]
        rows = []
        for return_rate in [0.0, 0.025, 0.05, 0.075, 0.10, 0.15]:
            returners = return_rate * baseline
            coverage_residual = residual_before_returns - returners
            rows.append({
                "assumed_returners_as_pct_of_2022_active_count": 100 * return_rate,
                "assumed_returners_k": returners,
                "residual_after_returns_k": coverage_residual,
                "residual_share_of_observed_rise_pct": 100 * coverage_residual / rise["rise_k"],
            })
        scenarios[name] = {
            "assumed_exit_rate_pct": scenario["exit_rate_pct"],
            "returners_needed_for_zero_coverage_residual_k": residual_before_returns,
            "returners_needed_as_pct_of_2022_active_count": 100 * residual_before_returns / baseline,
            "assumption_grid": rows,
        }
    return {
        "identity": "change in estimated active sellers = first-time entrants - exits + returning sellers + residual",
        "observed_residual_before_exit_or_return_adjustment_k": gap,
        "2022_active_count_k": baseline,
        "scenarios": scenarios,
        "classification": "scenario, not an estimate of actual returning sellers or a confidence interval",
        "interpretation": "The residual also absorbs survey coverage, weighting, classification, recall and sampling differences. Its attribution to coverage requires assumptions about returning sellers and those differences.",
    }


def seller_growth_example() -> dict:
    gel = json.loads((TABLES / "gel_checks.json").read_text())
    mean_target = gel["existing_sellers_reported_change_2023"]["all"]["mean_pct"] / 100
    aggregate_target = gel["bps_total_growth_pct"]["2023"] / 100
    # Nine equal small sellers and one large seller. These are invented inputs.
    # Four small sellers decline and five stay unchanged, giving a flat median.
    small_count, declining_count, unchanged_count = 9, 4, 5
    small_initial, large_initial = 1.0, 100.0
    initial_total = small_count * small_initial + large_initial
    large_growth = (initial_total * aggregate_target - 10 * small_initial * mean_target) / (large_initial - small_initial)
    small_growth = (10 * mean_target - large_growth) / declining_count
    initial = np.array([small_initial] * small_count + [large_initial])
    growth = np.array([small_growth] * declining_count + [0.0] * unchanged_count + [large_growth])
    final = initial * (1 + growth)
    aggregate = final.sum() / initial.sum() - 1
    assert np.all(final > 0)
    assert math.isclose(float(growth.mean()), mean_target, abs_tol=1e-12)
    assert math.isclose(float(aggregate), aggregate_target, abs_tol=1e-12)
    assert math.isclose(float(np.median(growth)), gel["existing_sellers_reported_change_2023"]["all"]["median_pct"] / 100, abs_tol=1e-12)
    assert aggregate > 0
    return {
        "classification": "synthetic arithmetic counterexample; not BPS observations or a reconstruction of its aggregate",
        "purpose": "show that negative seller-weighted mean growth and positive sales-weighted aggregate growth can coexist",
        "small_sellers": small_count, "declining_small_sellers": declining_count,
        "unchanged_small_sellers": unchanged_count, "large_sellers": 1,
        "initial_sales_per_small_seller_arbitrary_units": small_initial,
        "initial_sales_of_large_seller_arbitrary_units": large_initial,
        "declining_small_seller_growth_pct": 100 * small_growth,
        "large_seller_growth_pct": 100 * large_growth,
        "equal_seller_weight_mean_growth_pct": float(100 * growth.mean()),
        "median_seller_growth_pct": float(100 * np.median(growth)),
        "aggregate_sales_growth_pct": float(100 * aggregate),
        "interpretation": "This proves compatibility, not that concentration explains the actual BPS increase. The observed mean and median alone cannot reject the published aggregate.",
    }


def valuation_identity() -> dict:
    market = json.loads((TABLES / "m1_market_value_results.json").read_text())
    return {
        "identity": "change log(MV/R) - change log(MV/V) = -change log(R/V)",
        "classification": "algebraic identity, not an independent market-preference test",
        "implied_take_rate_log_changes_from_saved_multiples": {
            firm: row["change_ln_mv_over_V"] - row["change_ln_mv_over_R"]
            for firm, row in market["descriptive_idn_regional_change_since_first_year"].items()
        },
        "main_coefficient_difference_p": market["main"]["p_one_sided_b1_gt_b2"],
        "main_volume_coefficient_p": market["main"]["p_one_sided_b1_gt_0"],
        "market_cap_boundary": "Change in market capitalization includes changes in shares outstanding; it is not stock return. Existing event-return analyses are a separate exploratory module.",
    }


def main() -> None:
    result = {
        "review_date": "2026-10-08",
        "reviewed_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "status": "Independent exploratory review; no sample or thesis wording adopted.",
        "input_sha256": {
            str((TABLES / name).relative_to(ROOT)): hashlib.sha256((TABLES / name).read_bytes()).hexdigest()
            for name in INPUTS
        },
        "h1_issuer_sensitivity": issuer_sensitivity(),
        "bps_returning_seller_sensitivity": returning_seller_sensitivity(),
        "synthetic_seller_growth_example": seller_growth_example(),
        "valuation_identity": valuation_identity(),
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    for name, row in result["h1_issuer_sensitivity"]["variants"].items():
        print(name, "units", row["units_a"], row["units_b"], "MW p", round(row["mann_whitney_one_sided_p"], 5),
              "exact mean p", round(row["exact_permutation_mean_difference_p"], 5),
              "exact median p", round(row["exact_permutation_median_difference_p"], 5))
    for name, row in result["bps_returning_seller_sensitivity"]["scenarios"].items():
        print(name, "returners needed for zero coverage residual (% of baseline)", round(row["returners_needed_as_pct_of_2022_active_count"], 3))
    toy = result["synthetic_seller_growth_example"]
    print("Synthetic example: seller mean", round(toy["equal_seller_weight_mean_growth_pct"], 3),
          "aggregate growth", round(toy["aggregate_sales_growth_pct"], 3))
    print("Wrote", HERE / "results.json")


if __name__ == "__main__":
    main()
