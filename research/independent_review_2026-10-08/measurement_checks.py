#!/usr/bin/env python3
"""Post-result accounting checks and a source-verified drafting example.

Run from any directory. Reads existing analytical rows and source extracts;
writes only beside this script. It does not change source data, hypotheses,
sample admission or the frozen research. The bridge uses ordinary growth and
log growth separately. It adds no statistical test or national estimate.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
import statistics
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLES = ROOT / "research/option_space_2026-10-01/tables"
INPUTS = [
    TABLES / "transitions_master.csv",
    TABLES / "wedge_split_summary.json",
    TABLES / "h1_groundwork.json",
    ROOT / "data/measurement/source_extracts/tokopedia_fy2022_2023_revenue_components.csv",
    ROOT / "data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv",
    ROOT / "sources/core_public_documents/goto_annual_report_2023.pdf",
]


def close(a: float, b: float) -> None:
    assert math.isclose(a, b, rel_tol=1e-10, abs_tol=1e-10), (a, b)


def main() -> None:
    head_at_start = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUTS}
    transitions = list(csv.DictReader(INPUTS[0].open()))
    bridge, excluded = [], []
    for row in transitions:
        v, r = float(row["gV"]) / 100, float(row["gR"]) / 100
        m0, m1 = float(row["m0_pct"]) / 100, float(row["m1_pct"]) / 100
        if not all(math.isfinite(x) for x in (v, r, m0, m1)) or min(1 + v, 1 + r, m0, m1) <= 0:
            excluded.append({"firm": row["firm"], "y0": row["y0"], "y1": row["y1"],
                             "reason": "missing/nonfinite inputs or nonpositive ratio outside log domain"})
            continue
        gm = m1 / m0 - 1
        d = r - v
        lv, lr, lm = math.log1p(v), math.log1p(r), math.log(m1 / m0)
        close(r, v + gm + v * gm)
        close(d, (1 + v) * gm)
        close(lr, lv + lm)
        close(100 * d, float(row["D_pp"]))
        share = abs(lm) / (abs(lv) + abs(lm)) if abs(lv) + abs(lm) else None
        bridge.append({
            "set": row["set"], "firm": row["firm"], "y0": row["y0"], "y1": row["y1"],
            "tier": row["tier"], "transaction_growth_pct": 100 * v,
            "revenue_growth_pct": 100 * r, "take_rate_growth_pct": 100 * gm,
            "growth_divergence_pp": 100 * d,
            "percentage_addition_error_pp": 100 * (r - (v + gm)),
            "interaction_term_pp": 100 * v * gm,
            "log_transaction_change": lv, "log_revenue_change": lr,
            "log_take_rate_change": lm,
            "take_rate_share_of_absolute_log_components": share,
            "take_rate_component_divided_by_net_log_revenue_change": lm / lr if lr else None,
        })

    core = [x for x in bridge if x["set"] == "IDN_main"]
    foreign = [x for x in bridge if x["set"] == "EXT_clean"]
    saved = json.loads(INPUTS[1].read_text())
    summaries = {}
    for name, rows in (("IDN_main", core), ("EXT_clean", foreign)):
        shares = [x["take_rate_share_of_absolute_log_components"] for x in rows]
        assert all(x is not None for x in shares)
        median = statistics.median(shares)
        close(median, saved[name]["median_monetization_share_of_R_change"])
        summaries[name] = {
            "transitions": len(rows), "series_labels": len({x["firm"] for x in rows}),
            "median_signed_growth_divergence_pp": statistics.median(x["growth_divergence_pp"] for x in rows),
            "median_absolute_growth_divergence_pp": statistics.median(abs(x["growth_divergence_pp"]) for x in rows),
            "median_take_rate_share_of_absolute_log_components": median,
            "opposite_component_signs": sum(x["log_transaction_change"] * x["log_take_rate_change"] < 0 for x in rows),
        }

    extracts = list(csv.DictReader(INPUTS[3].open()))
    amounts = {(x["period"], x["component"]): int(x["value_idr_million"]) for x in extracts}
    candidates = list(csv.DictReader(INPUTS[4].open()))
    # Candidate values are source-linked levels, not an approval of admission.
    toko = {x["period"]: x for x in candidates if x["platform"] == "Tokopedia"}
    assert set(toko) >= {"FY2022", "FY2023"}, list(candidates[0])
    v0, v1 = [float(toko[y]["transaction_value"]) for y in ("FY2022", "FY2023")]
    gross0, gross1 = [amounts[(y, "third_party_gross_revenue")] for y in ("FY2022", "FY2023")]
    i0, i1 = [-amounts[(y, "customer_incentives")] for y in ("FY2022", "FY2023")]
    net0, net1 = [amounts[(y, "third_party_net_revenue")] for y in ("FY2022", "FY2023")]
    assert gross0 - i0 == net0 and gross1 - i1 == net1
    assert (gross1 - gross0) + (i0 - i1) == net1 - net0
    checked = {
        "scope": "Tokopedia e-commerce segment, Indonesia-aligned; not an explicit country line",
        "years": [2022, 2023], "units": "IDR million, original disclosure units",
        "V": [v0, v1], "third_party_gross_revenue": [gross0, gross1],
        "customer_incentive_deduction_magnitude": [i0, i1],
        "third_party_net_revenue": [net0, net1],
        "net_revenue_increase": net1 - net0,
        "incentive_reduction": i0 - i1, "gross_revenue_increase": gross1 - gross0,
        "share_of_net_revenue_increase_from_lower_incentives_pct": 100 * (i0 - i1) / (net1 - net0),
        "share_of_net_revenue_increase_from_higher_gross_revenue_pct": 100 * (gross1 - gross0) / (net1 - net0),
        "transaction_growth_pct": 100 * (v1 / v0 - 1),
        "net_revenue_growth_pct": 100 * (net1 / net0 - 1),
        "take_rate_pct": [100 * net0 / v0, 100 * net1 / v1],
        "take_rate_growth_required_for_flat_revenue_pct": 100 * (v0 / v1 - 1),
        "source_pdf_pages_one_based": [144, 475, 476],
        "source_locators": "Operating metrics, printed p.142; Note 29, financial-statement pp.5/111 and 12; 2022 restated",
        "source_verification": "PDF text values asserted below; relevant complete pages also visually inspected on 8 October 2026",
    }
    pdf = subprocess.check_output(["pdftotext", "-layout", str(INPUTS[5]), "-"], text=True).split("\f")
    assert "248.836.156" in pdf[143] and "273.146.166" in pdf[143]
    assert all(f"{x:,}" in pdf[474] for x in (gross1, i1, net1))
    assert all(f"{x:,}" in pdf[475] for x in (gross0, i0, net0))
    matched = next(x for x in core if "Tokopedia" in x["firm"])
    close(checked["transaction_growth_pct"], matched["transaction_growth_pct"])
    close(checked["net_revenue_growth_pct"], matched["revenue_growth_pct"])
    close(checked["take_rate_pct"][1], float(next(x for x in transitions if "Tokopedia" in x["firm"])["m1_pct"]))
    checked["ordinary_growth_bridge"] = matched
    checked["rounded_existing_h1_groundwork_share_pct"] = json.loads(INPUTS[2].read_text())["tokopedia_two_views"]["rupiah_view_share_lower_incentives_pct"]

    # Diagnostic only: no BPS or constructed issuer values are pooled here.
    coverage_example = {"classification": "synthetic identity check; not empirical evidence",
                        "commerce_growth_pct": 0, "take_rate_growth_pct": 25,
                        "covered_share_growth_pct": -20}
    factor = 1.25 * 0.8
    close(factor, 1)
    coverage_example["revenue_growth_pct"] = 100 * (factor - 1)

    assert hashes == {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUTS}, "inputs changed during check; rerun"
    output = {
        "classification": "post-result arithmetic and source checks; no new hypothesis test",
        "repository_head_at_run": head_at_start,
        "input_sha256": hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "identities_checked_on_rows": len(bridge), "excluded_rows": excluded,
        "growth_rate_convention": "ordinary fractional growth; D reported in percentage points; logs separately labelled",
        "component_share_definition": "abs(delta log m) / (abs(delta log V) + abs(delta log m)); median across transitions, not share of net growth or a causal fraction",
        "existing_core_and_original_clean_benchmark_summaries": summaries,
        "tokopedia_source_check": checked,
        "covered_share_cancellation_example": coverage_example,
    }
    (HERE / "measurement_checks.json").write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
    with (HERE / "growth_bridge.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(bridge[0]))
        writer.writeheader()
        writer.writerows(bridge)
    print(json.dumps({"rows_checked": len(bridge), "core_summary": summaries["IDN_main"],
                      "Tokopedia_exact_incentive_share_pct": checked["share_of_net_revenue_increase_from_lower_incentives_pct"]}, indent=2))


if __name__ == "__main__":
    main()
