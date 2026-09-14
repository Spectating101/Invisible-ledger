#!/usr/bin/env python3
"""Build an advisor-facing empirical review package without rewriting the manuscript.

This script is deliberately conservative. It:
- applies explicit candidate sample rules without declaring any rule advisor-approved;
- detects known stale/inconsistent admission statuses in the broader census;
- summarizes within-series issuer movement evidence without pooling levels;
- performs reproducible internal-consistency checks on the public BPS extracts;
- marks cross-wave BPS growth comparisons conditional until source wording/denominators
  are certified at the original-publication level.

It does not alter source files, main datasets, manuscripts, or CURRENT_STATUS.md.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import math
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_movement_module():
    path = ROOT / "scripts/analysis/build_issuer_movement_bridge.py"
    spec = importlib.util.spec_from_file_location("issuer_movement_bridge", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def summarize_transitions(rows: list[dict], label: str, note: str) -> dict:
    if not rows:
        return {
            "rule": label,
            "series_count": 0,
            "annual_rows": 0,
            "adjacent_transitions": 0,
            "opposite_sign_transitions": 0,
            "revenue_growth_outpaces": 0,
            "activity_growth_outpaces": 0,
            "median_abs_growth_gap_pp": "",
            "status": "empty_under_rule",
            "interpretation_note": note,
        }
    series = {(r["platform"], r["scope"], r["evidence_class"]) for r in rows}
    reversals = [r for r in rows if r["movement_pattern"] in {"activity_up_revenue_down", "activity_down_revenue_up"}]
    return {
        "rule": label,
        "series_count": len(series),
        "annual_rows": "",  # populated by caller from source rows when available
        "adjacent_transitions": len(rows),
        "opposite_sign_transitions": len(reversals),
        "revenue_growth_outpaces": sum(r["revenue_growth_pct"] > r["activity_growth_pct"] for r in rows),
        "activity_growth_outpaces": sum(r["activity_growth_pct"] > r["revenue_growth_pct"] for r in rows),
        "median_abs_growth_gap_pp": round(median(r["abs_growth_gap_pp"] for r in rows), 6),
        "status": "candidate_not_approved",
        "interpretation_note": note,
    }


def build_sample_sensitivity() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    mod = load_movement_module()
    series_rows, exclusions = mod.load_series()
    transitions = mod.build_transitions(series_rows)

    direct = [r for r in transitions if r["evidence_class"] == "direct_candidate"]
    conditional = [r for r in transitions if r["evidence_class"] == "conditional_country_reconstruction"]

    rules: list[tuple[str, list[dict], str, set[tuple[str, str, str]]]] = []

    # No direct series in the current reviewed set is an explicit-country direct pair.
    rules.append((
        "R0_strict_explicit_country_direct",
        [],
        "No current direct annual transaction/revenue series is both an explicit Indonesia country line and a direct matched pair. This is a diagnostic, not a recommended final design.",
        set(),
    ))

    tokopedia = [r for r in direct if r["platform"] == "Tokopedia"]
    rules.append((
        "R1_indonesia_aligned_segment_only",
        tokopedia,
        "Tokopedia FY2022→FY2023 only. Direct Indonesia-aligned e-commerce segment; not an explicit geographic country line.",
        {("Tokopedia", "e-commerce segment", "direct_candidate")},
    ))

    blibli_toko = [r for r in direct if r["platform"] in {"Blibli/GDN", "Tokopedia"}]
    rules.append((
        "R2_exclude_overseas_group_keep_segment_candidates",
        blibli_toko,
        "Excludes Bukalapak Group because overseas operations are disclosed; retains Blibli 3P and Tokopedia subject to segment/scope approval. Blibli 3P includes online travel.",
        {("Blibli/GDN", "3P Retail", "direct_candidate"), ("Tokopedia", "e-commerce segment", "direct_candidate")},
    ))

    rules.append((
        "R3_all_direct_candidate_series",
        direct,
        "Blibli 3P, Bukalapak Group, and Tokopedia segment. Direct issuer/segment pairs only, but all retain geography/business-scope caveats.",
        {(r["platform"], r["scope"], r["evidence_class"]) for r in direct},
    ))

    rules.append((
        "R4_conditional_indonesia_country_reconstructions",
        conditional,
        "Grab/Shopee Indonesia reconstructions are sensitivity cases only because transaction/revenue pairs depend on Group monetization rates and/or external country-market estimates.",
        {(r["platform"], r["scope"], r["evidence_class"]) for r in conditional},
    ))

    out = []
    for label, trans, note, series_keys in rules:
        rec = summarize_transitions(trans, label, note)
        rec["annual_rows"] = sum((r["platform"], r["scope"], r["evidence_class"]) in series_keys for r in series_rows)
        out.append(rec)

    # Detect stale census admissions instead of silently changing the generated audit.
    census = read_csv(ROOT / "outputs/empirical_backend_2026-09-09/candidate_observation_census.csv")
    census_issues = []
    for r in census:
        platform = r.get("platform", "")
        period = r.get("period", "")
        admission = r.get("admission_status", "")
        if platform.startswith("Tokopedia") and period == "FY2021" and admission in {"candidate_core", "conditional_case"}:
            census_issues.append({
                "issue_id": "STALE-TOKOPEDIA-FY2021",
                "record_id": r.get("record_id", ""),
                "platform": platform,
                "period": period,
                "census_admission_status": admission,
                "certified_treatment": "EXCLUDE",
                "reason": "Known period mismatch: full-year pro-forma transaction value paired with post-acquisition revenue.",
                "action": "Do not count in advisor-facing eligible sample until a genuinely period-matched pair is recovered.",
            })

    # Carry the hard exclusions from the movement bridge into one advisor-facing list.
    exclusion_rows = [dict(r) for r in exclusions]
    return out, census_issues, exclusion_rows, transitions


def get_indicator(rows: list[dict[str, str]], year: int, indicator: str) -> dict[str, str]:
    hits = [r for r in rows if int(r["reference_year"]) == year and r["indicator"] == indicator]
    if len(hits) != 1:
        raise ValueError(f"Expected one BPS row for {year}/{indicator}, found {len(hits)}")
    return hits[0]


def build_bps_certification() -> tuple[list[dict], dict]:
    national = read_csv(ROOT / "data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv")
    p23 = read_csv(ROOT / "data/bps_official/bps_ecommerce_2023_province_financial_records_sales_media.csv")
    p24 = read_csv(ROOT / "data/bps_official/bps_ecommerce_2024_province_financial_records_sales_media.csv")
    readme = (ROOT / "data/bps_official/README.md").read_text(encoding="utf-8")

    total23 = float(get_indicator(national, 2023, "ecommerce_transaction_value")["value"])
    total24 = float(get_indicator(national, 2024, "ecommerce_transaction_value")["value"])
    mkt23_value = float(get_indicator(national, 2023, "marketplace_transaction_value")["value"])
    mkt23_share = float(get_indicator(national, 2023, "marketplace_share_exclusive_decomposition")["value"])
    mkt24_share = float(get_indicator(national, 2024, "marketplace_share_of_transaction_value")["value"])
    business23 = float(get_indicator(national, 2023, "estimated_number_of_ecommerce_businesses")["value"])
    business24 = float(get_indicator(national, 2024, "estimated_number_of_ecommerce_businesses")["value"])
    fin23 = float(get_indicator(national, 2023, "ecommerce_businesses_with_financial_reports")["value"])
    fin24 = float(get_indicator(national, 2024, "ecommerce_businesses_with_financial_reports")["value"])

    derived_mkt24 = total24 * mkt24_share / 100.0
    total_growth = (total24 / total23 - 1.0) * 100.0
    market_growth = (derived_mkt24 / mkt23_value - 1.0) * 100.0

    common_provinces = sorted(set(r["province"] for r in p23) & set(r["province"] for r in p24))
    complete_common = []
    for prov in common_provinces:
        a = next(r for r in p23 if r["province"] == prov)
        b = next(r for r in p24 if r["province"] == prov)
        required = [a.get("financial_reports_have_pct", ""), a.get("marketplace_sales_media_pct", ""), b.get("financial_reports_have_pct", ""), b.get("marketplace_sales_media_pct", "")]
        if all(x not in {"", None, "NA", "N/A"} for x in required):
            complete_common.append(prov)

    complement_failures = []
    for year, rows in [(2023, p23), (2024, p24)]:
        for r in rows:
            try:
                have = float(r["financial_reports_have_pct"])
                not_have = float(r["financial_reports_not_have_pct"])
            except (ValueError, TypeError):
                continue
            if abs((have + not_have) - 100.0) > 0.02:
                complement_failures.append(f"{year}:{r['province']}")

    province24_count_sum = sum(int(float(r["estimated_ecommerce_businesses"])) for r in p24 if r.get("estimated_ecommerce_businesses"))
    province24_total_diff = province24_count_sum - int(business24)

    checks = [
        {
            "check_id": "BPS-01",
            "dimension": "2023/2024 total transaction-value availability",
            "status": "PASS_INTERNAL",
            "evidence": f"2023={total23:.2f} IDR tn; 2024={total24:.2f} IDR tn",
            "consequence": "Total nominal growth can be calculated from the retained extract.",
        },
        {
            "check_id": "BPS-02",
            "dimension": "exclusive marketplace decomposition across 2023/2024",
            "status": "CONDITIONAL_SOURCE_CONCORDANCE",
            "evidence": f"2023 direct marketplace value={mkt23_value:.2f} IDR tn ({mkt23_share:.2f}%); 2024 marketplace share={mkt24_share:.2f}% and derived value={derived_mkt24:.2f} IDR tn",
            "consequence": f"Conditional comparison: total growth={total_growth:.2f}%, marketplace-component growth={market_growth:.2f}%. Do not promote until original-publication wording/denominators are certified comparable.",
        },
        {
            "check_id": "BPS-03",
            "dimension": "financial-report ownership across 2023/2024",
            "status": "CONDITIONAL_WAVE_COMPARABILITY",
            "evidence": f"2023={fin23:.2f}%; 2024={fin24:.2f}%",
            "consequence": "Both waves report the concept, but stronger trend inference requires questionnaire/reference-population concordance.",
        },
        {
            "check_id": "BPS-04",
            "dimension": "province repeated-cross-section coverage",
            "status": "PASS_INTERNAL",
            "evidence": f"common province labels={len(common_provinces)}; complete common marketplace/financial-report pairs={len(complete_common)}",
            "consequence": "Matched-province descriptive changes are feasible for complete cells only; not a business panel.",
        },
        {
            "check_id": "BPS-05",
            "dimension": "financial-report complement identity",
            "status": "PASS_INTERNAL" if not complement_failures else "FAIL_INTERNAL",
            "evidence": "all numeric province have/not-have pairs sum to 100 within 0.02pp" if not complement_failures else ";".join(complement_failures),
            "consequence": "Supports internal transcription consistency for this item, not survey-design validity.",
        },
        {
            "check_id": "BPS-06",
            "dimension": "2023 national business-count conflict",
            "status": "BLOCKED_SOURCE_CONFLICT",
            "evidence": "README preserves 3,934,981 (executive-summary passage) versus 3,816,750 (main body/figure)." if "3,934,981" in readme and "3,816,750" in readme else "documented conflict text not found",
            "consequence": "Any count-based 2023→2024 decomposition must show both scenarios until the original publisher table/erratum is resolved.",
        },
        {
            "check_id": "BPS-07",
            "dimension": "2024 province-count reconciliation",
            "status": "PASS_WITH_SOURCE_RESIDUAL" if province24_total_diff == 1 else "REVIEW",
            "evidence": f"province sum={province24_count_sum}; national total={int(business24)}; residual={province24_total_diff}",
            "consequence": "Preserve the one-business source residual; do not force-balance province values.",
        },
    ]

    diagnostics = {
        "total23": total23,
        "total24": total24,
        "total_growth_pct": total_growth,
        "marketplace23_value": mkt23_value,
        "marketplace24_derived_value": derived_mkt24,
        "marketplace_growth_pct": market_growth,
        "business23_selected": business23,
        "business24": business24,
        "financial_reports23_pct": fin23,
        "financial_reports24_pct": fin24,
        "common_provinces": len(common_provinces),
        "complete_common_provinces": len(complete_common),
        "province24_count_sum": province24_count_sum,
        "province24_total_diff": province24_total_diff,
    }
    return checks, diagnostics


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def fmt(v) -> str:
    if v in {"", None}:
        return "—"
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def build_kong_review(sample_rows: list[dict], census_issues: list[dict], exclusions: list[dict], bps_checks: list[dict], d: dict) -> str:
    lines = [
        "# Invisible Ledger — empirical data review for advisor discussion",
        "",
        "**Status:** empirical review package only. This is not a manuscript rewrite and does not assert that any expanded sample has been approved.",
        "",
        "## 1. What changed since the FY2023 three-case file",
        "",
        "The evidence base now supports several candidate longitudinal designs rather than a single one-year comparison. The alternatives below are intentionally shown side-by-side so the sample boundary can be approved before another manuscript rewrite.",
        "",
        "## 2. Candidate Indonesia sample rules and sensitivity",
        "",
        "| Rule | Annual rows | Adjacent transitions | Opposite-sign transitions | Revenue growth outpaces | Activity growth outpaces | Median absolute growth gap | Status |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in sample_rows:
        gap = "—" if r["median_abs_growth_gap_pp"] == "" else f"{float(r['median_abs_growth_gap_pp']):.2f} pp"
        lines.append(
            f"| {r['rule']} | {r['annual_rows']} | {r['adjacent_transitions']} | {r['opposite_sign_transitions']} | "
            f"{r['revenue_growth_outpaces']} | {r['activity_growth_outpaces']} | {gap} | {r['status']} |"
        )
    lines += ["", "**Interpretation of the rules:**"]
    for r in sample_rows:
        lines.append(f"- `{r['rule']}` — {r['interpretation_note']}")

    lines += [
        "",
        "The broad direct-candidate rule is descriptive rather than a pooled estimator: levels are never added across currencies or issuers. The within-series result asks whether recognized revenue and accompanying transaction activity tell the same direction/magnitude of annual movement.",
        "",
        "## 3. Known exclusions and census consistency",
        "",
    ]
    for r in exclusions:
        lines.append(f"- **{r['platform']} {r['period']}** — {r['reason']}")
    if census_issues:
        lines += ["", "The comprehensive census still contains a stale admission that the advisor-facing package overrides:"]
        for r in census_issues:
            lines.append(f"- `{r['record_id']}` {r['platform']} {r['period']}: census says `{r['census_admission_status']}`, certified treatment is **{r['certified_treatment']}** because {r['reason']}")
    else:
        lines.append("- No stale admission conflicts detected by the current rule checks.")

    lines += [
        "",
        "## 4. BPS certification state",
        "",
        "| Check | Status | Evidence | Consequence |",
        "|---|---|---|---|",
    ]
    for r in bps_checks:
        lines.append(f"| {r['dimension']} | **{r['status']}** | {r['evidence']} | {r['consequence']} |")

    lines += [
        "",
        "The current extract therefore permits a **conditional** 2023→2024 comparison in which total nominal e-commerce transaction value grows "
        f"{d['total_growth_pct']:.2f}% while the derived exclusive-marketplace component grows about {d['marketplace_growth_pct']:.2f}%. "
        "This comparison should remain outside final thesis claims until the original BPS wording and denominators are certified cross-wave comparable.",
        "",
        "## 5. Decisions requested from the advisor",
        "",
        "1. Is the **Tokopedia e-commerce segment** acceptable as an Indonesia-aligned direct segment even though it is not a literal geographic line?",
        "2. Is **Blibli 3P Retail** admissible in the main longitudinal design despite including online travel, or should it remain a supporting mechanism/sensitivity series?",
        "3. Should **Bukalapak Group** be excluded from the main Indonesia series because overseas operations are disclosed, while retained as supporting evidence?",
        "4. Should **Grab and Shopee conditional Indonesia reconstructions** remain sensitivity cases only rather than core observations?",
        "5. Should the BPS official-statistics module remain supporting evidence, or be elevated after the cross-wave definitions (and, if feasible, licensed microdata) are certified?",
        "",
        "## 6. Recommended empirical boundary pending those decisions",
        "",
        "Do not advertise one final N yet. Report each evidence family separately and preserve the strict/direct/conditional hierarchy. The data package is now sufficient to ask the advisor to choose among explicit sample rules rather than accept a one-year construction by default.",
        "",
        "## 7. Reproduction",
        "",
        "Generated by `scripts/analysis/build_empirical_review_package.py` from the repository's existing issuer and BPS extracts. Source files and manuscripts are not modified by this script.",
    ]
    return "\n".join(lines) + "\n"


def build_decision_sheet(sample_rows: list[dict], bps_checks: list[dict]) -> str:
    by_rule = {r["rule"]: r for r in sample_rows}
    blocked = [r for r in bps_checks if r["status"].startswith("BLOCKED") or r["status"].startswith("CONDITIONAL")]
    lines = [
        "# Kong decision sheet — sample boundary only",
        "",
        "This one-page sheet is intentionally narrower than the full empirical audit.",
        "",
        "## Candidate choices",
        "",
        f"- **Strict explicit-country direct:** {by_rule['R0_strict_explicit_country_direct']['adjacent_transitions']} adjacent transitions. Too strict to provide a longitudinal thesis sample with current public disclosures.",
        f"- **Indonesia-aligned segment only (Tokopedia):** {by_rule['R1_indonesia_aligned_segment_only']['adjacent_transitions']} transition. Clean but still too narrow alone.",
        f"- **Blibli 3P + Tokopedia, excluding Bukalapak overseas Group:** {by_rule['R2_exclude_overseas_group_keep_segment_candidates']['adjacent_transitions']} transitions; {by_rule['R2_exclude_overseas_group_keep_segment_candidates']['opposite_sign_transitions']} opposite-sign movements. Requires approval of Blibli 3P scope.",
        f"- **All direct candidate series:** {by_rule['R3_all_direct_candidate_series']['adjacent_transitions']} transitions; {by_rule['R3_all_direct_candidate_series']['opposite_sign_transitions']} opposite-sign movements. Requires approval of both Blibli and Bukalapak scope.",
        f"- **Conditional Grab/Shopee country reconstructions:** {by_rule['R4_conditional_indonesia_country_reconstructions']['adjacent_transitions']} transitions. Recommended as sensitivity/supporting evidence only.",
        "",
        "## Hard exclusions",
        "",
        "- Tokopedia FY2021: period mismatch; excluded.",
        "- Bukalapak FY2024: 9-month TPV versus 12-month revenue; excluded.",
        "",
        "## BPS items still requiring source-level certification",
        "",
    ]
    for r in blocked:
        lines.append(f"- **{r['dimension']}** — {r['status']}: {r['consequence']}")
    lines += [
        "",
        "## Decision needed",
        "",
        "Please select the acceptable geography/business-scope boundary for the longitudinal Indonesia analysis. No manuscript rewrite is proposed until that boundary is approved.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=ROOT / "build/empirical_review_package")
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    samples, census_issues, exclusions, transitions = build_sample_sensitivity()
    bps_checks, diagnostics = build_bps_certification()

    write_csv(args.output / "sample_rule_sensitivity.csv", samples)
    write_csv(args.output / "census_admission_issues.csv", census_issues)
    write_csv(args.output / "hard_exclusions.csv", exclusions)
    write_csv(args.output / "bps_certification_matrix.csv", bps_checks)
    (args.output / "KONG_DATA_REVIEW.md").write_text(build_kong_review(samples, census_issues, exclusions, bps_checks, diagnostics), encoding="utf-8")
    (args.output / "KONG_DECISION_SHEET.md").write_text(build_decision_sheet(samples, bps_checks), encoding="utf-8")

    print(f"sample rules: {len(samples)}")
    print(f"stale census issues: {len(census_issues)}")
    print(f"hard exclusions: {len(exclusions)}")
    print(f"BPS checks: {len(bps_checks)}")
    print(f"direct candidate transitions: {next(r['adjacent_transitions'] for r in samples if r['rule']=='R3_all_direct_candidate_series')}")


if __name__ == "__main__":
    main()
