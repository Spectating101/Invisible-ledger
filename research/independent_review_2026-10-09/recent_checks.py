#!/usr/bin/env python3
"""Independent post-result checks of the 9 October developments.

Runs from anywhere. Reads the existing public panels and, when supplied, local
licensed BPS inputs. Writes only national aggregates and public-panel summaries
beside this script. No sample decision, hypothesis or frozen file is changed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np
import pandas as pd
from scipy import stats


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OCT = ROOT / "research/option_space_2026-10-01"


def comparison(rows: pd.DataFrame) -> dict:
    summary = rows.groupby(["firm", "group"]).agg(
        share_kept_pct=("m0", lambda x: 100 * x.median()),
        change_points=("points", "median"), change_log=("log", "median"),
        transitions=("log", "size"),
    ).reset_index()
    a, b = summary[summary.group == "target"], summary[summary.group == "foreign"]
    return {
        "target_firms": len(a), "foreign_firms": len(b),
        "target_transitions": int(a.transitions.sum()), "foreign_transitions": int(b.transitions.sum()),
        "median_start_take_rate_pct": {"target": float(a.share_kept_pct.median()), "foreign": float(b.share_kept_pct.median())},
        "median_absolute_change_points": {"target": float(a.change_points.median()), "foreign": float(b.change_points.median())},
        "median_absolute_log_change": {"target": float(a.change_log.median()), "foreign": float(b.change_log.median())},
        "mann_whitney_one_sided_p_points": float(stats.mannwhitneyu(a.change_points, b.change_points, alternative="greater").pvalue),
        "mann_whitney_one_sided_p_log": float(stats.mannwhitneyu(a.change_log, b.change_log, alternative="greater").pvalue),
        "foreign_firm_labels": sorted(b.firm.tolist()),
    }


def public_checks() -> dict:
    t = pd.read_csv(OCT / "tables/transitions_master.csv")
    p = pd.read_csv(OCT / "tables/l_panel.csv")
    s = pd.read_csv(OCT / "tables/spinoff_panel.csv").sort_values(["entity", "year"]).copy()
    s["m0"] = s.groupby("entity").m.shift()
    s["previous_flag"] = s.groupby("entity").flag_1p.shift()
    s["previous_year"] = s.groupby("entity").year.shift()
    base = t[t["set"].isin(["IDN_main", "EXT_clean"])].copy()
    rows = [{"firm": r.firm, "group": "target" if r.set == "IDN_main" else "foreign",
             "m0": r.m0_pct / 100, "m1": r.m1_pct / 100} for r in base.itertuples()]
    grab = p[p.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index()
    goto = p[(p.firm == "GoTo") & (p.seg == "On-demand")][["year", "V", "R"]]
    for name, group in (("Grab on-demand", grab), ("GoTo on-demand", goto)):
        group = group[group.R > 0].sort_values("year")
        for a, b in zip(group.itertuples(), group.iloc[1:].itertuples()):
            if b.year - a.year == 1:
                rows.append({"firm": name, "group": "target", "m0": a.R / a.V, "m1": b.R / b.V})

    current = s[(s.flag_1p != "exclude") & s.g_m.notna()].copy()
    assert ((current.year - current.previous_year) == 1).all()
    assert np.allclose(np.log(current.m / current.m0), current.g_m, atol=1e-12)
    expanded = pd.DataFrame(rows + [
        {"firm": r.entity, "group": "foreign", "m0": r.m0, "m1": r.m}
        for r in current.itertuples()
    ])
    excluded_previous = current[current.previous_flag == "exclude"]
    stricter = expanded[~expanded.firm.isin(excluded_previous.entity)].copy()
    # There is only one affected transition/firm in this baseline. Keep the
    # assertion so later inputs cannot silently turn this into a firm-drop rule.
    assert len(excluded_previous) == 1 and excluded_previous.iloc[0].entity == "Ozon"
    for d in (expanded, stricter):
        d["points"] = 100 * (d.m1 - d.m0).abs()
        d["log"] = np.log(d.m1 / d.m0).abs()
    original, restricted = comparison(expanded), comparison(stricter)
    saved = json.loads((OCT / "tables/h1_points_vs_log.json").read_text())
    assert restricted["foreign_firms"] == saved["firms"]["Foreign"] == 26
    assert math.isclose(restricted["median_absolute_change_points"]["foreign"], saved["median_yearly_change_points"]["Foreign"], abs_tol=1e-12)
    assert math.isclose(restricted["mann_whitney_one_sided_p_log"], saved["mannwhitney_p_log"], abs_tol=1e-12)
    ext = json.loads((OCT / "tables/h1_extended_results.json").read_text())["A_vs_all_foreign"]
    assert original["foreign_firms"] == ext["firms_b"] == 27
    assert math.isclose(original["mann_whitney_one_sided_p_log"], ext["mannwhitney_p"], abs_tol=1e-12)

    core = t[t["set"] == "IDN_main"].copy()
    core["gm"] = core.m1_pct / core.m0_pct - 1
    core["exact_D_pp"] = 100 * (1 + core.gV / 100) * core.gm
    assert np.allclose(core.exact_D_pp, core.D_pp, atol=1e-10)
    toko = core[core.firm.str.contains("Tokopedia")].iloc[0]
    return {
        "scope": "existing Indonesia-aligned core plus regional series; heterogeneous foreign firms; exploratory",
        "original_extended_current_endpoint_rule": original,
        "new_points_check_both_endpoint_rule": restricted,
        "reason_for_27_to_26_difference": excluded_previous[["entity", "previous_year", "year", "previous_flag", "flag_1p"]].to_dict("records"),
        "interpretation": "The approximate equality of median point changes survives both selections. The non-significant one-sided test does not establish statistical equivalence or identify a causal country mechanism.",
        "exact_growth_identity": {
            "formula": "D = (1 + gV) * ((m1-m0)/m0), with ordinary fractional growth",
            "core_transitions_checked": len(core),
            "Tokopedia_D_pp": float(toko.D_pp),
            "Tokopedia_take_rate_growth_pct": float(100 * toko.gm),
        },
    }


def licensed_checks(f2023: Path, f2024: Path) -> dict:
    sys.path.insert(0, str(OCT))
    from bps_microdata_tests import read_dbf, num
    a, b = read_dbf(f2023), read_dbf(f2024)
    wa, wb = num(a["w_usaha_fi"]), num(b["w_final"])
    sa, sb = num(a["r305"]), num(b["r307"])
    ma = np.array([len([x for x in v.split(",") if x.strip()]) for v in a["r308"]])
    months = ["jan", "feb", "mar", "apr", "mei", "juni", "juli", "agt", "sept", "okt", "nov", "des"]
    mb = sum((num(b["r311_" + m]) == 1).astype(int) for m in months)
    assert np.isfinite(wa).all() and np.isfinite(wb).all()
    assert np.isfinite(sa).all() and np.isfinite(sb).all()
    assert ((ma >= 1) & (ma <= 12)).all() and ((mb >= 1) & (mb <= 12)).all()
    assert all(set(b["r311_" + m]) <= {"0", "1"} for m in months)
    out = {}
    for cutoff in (2020, 2021, 2022):
        periods = {}
        for year, w, start, m in ((2022, wa, sa, ma), (2023, wb, sb, mb)):
            keep = start <= cutoff
            periods[str(year)] = {
                "active_count_k": float(w[keep].sum() / 1e3),
                "full_year_k": float(w[keep & (m == 12)].sum() / 1e3),
                "part_year_k": float(w[keep & (m < 12)].sum() / 1e3),
                "part_year_pct": float(100 * w[keep & (m < 12)].sum() / w[keep].sum()),
            }
        out[str(cutoff)] = {"start_year_cutoff_in_both_rounds": cutoff, "periods": periods,
                           "part_year_change_k": periods["2023"]["part_year_k"] - periods["2022"]["part_year_k"]}
    saved = json.loads((OCT / "tables/bps_returning_check.json").read_text())
    assert math.isclose(out["2021"]["periods"]["2022"]["part_year_k"], saved["2022 survey (2022 activity)"]["part_year_k"], abs_tol=1e-9)
    assert math.isclose(out["2022"]["periods"]["2023"]["part_year_k"], saved["2023 survey (2023 activity)"]["part_year_k"], abs_tol=1e-9)
    return {
        "classification": "post-result diagnostic; fixed start-year groups, not linked business histories",
        "question_format": "list of months in 2022 versus twelve month flags in 2023",
        "aligned_start_year_checks": out,
        "interpretation": "Part-year selling falls under all three common cutoffs. This supports the descriptive pattern but does not identify returning sellers; exits and changes in incumbent selling duration can offset returning flows.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--f2023", type=Path)
    parser.add_argument("--f2024", type=Path)
    args = parser.parse_args()
    assert bool(args.f2023) == bool(args.f2024), "supply both licensed paths or neither"
    inputs = [OCT / "tables" / name for name in (
        "transitions_master.csv", "l_panel.csv", "spinoff_panel.csv",
        "h1_points_vs_log.json", "h1_extended_results.json", "bps_returning_check.json",
    )]
    if args.f2023:
        inputs += [args.f2023, args.f2024]
    hashes = {str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out = {"date": "2026-10-09", "classification": "independent exploratory review, no adopted decisions",
           "repository_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
           "input_sha256": hashes, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "H1": public_checks()}
    if args.f2023:
        out["BPS"] = licensed_checks(args.f2023, args.f2024)
    assert hashes == {str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}, "inputs changed during run"
    (HERE / "recent_checks.json").write_text(json.dumps(out, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"foreign_counts": [out["H1"][key]["foreign_firms"] for key in ("original_extended_current_endpoint_rule", "new_points_check_both_endpoint_rule")],
                      "point_change_comparison": out["H1"]["original_extended_current_endpoint_rule"]["median_absolute_change_points"],
                      "BPS_aligned_checks_run": "BPS" in out}, indent=2))


if __name__ == "__main__":
    main()
