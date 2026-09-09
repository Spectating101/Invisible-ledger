#!/usr/bin/env python3
"""Certified overlay for the advisor-facing empirical review package.

Builds on build_empirical_review_package.py, but incorporates later official BPS
cross-wave consistency evidence and a certified census overlay without deleting the
historical audit or its preserved source conflicts.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_base():
    path = ROOT / "scripts/analysis/build_empirical_review_package.py"
    spec = importlib.util.spec_from_file_location("empirical_review_base", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def read_notes(base):
    return base.read_csv(ROOT / "research/issuer_movement_bridge/bps_external_certification_notes.csv")


def build_certified_census(base):
    """Overlay certified admission fields without overwriting the historical audit columns."""
    rows = base.read_csv(ROOT / "outputs/empirical_backend_2026-09-09/candidate_observation_census.csv")
    out = []
    for r in rows:
        x = dict(r)
        x["certified_admission_status"] = r.get("admission_status", "")
        x["certified_ratio_eligible"] = r.get("ratio_eligible", "")
        x["certification_reason"] = "inherits historical audit status"

        if r.get("platform", "").startswith("Tokopedia") and r.get("period") == "FY2021":
            x["certified_admission_status"] = "exclude_period_mismatch"
            x["certified_ratio_eligible"] = "False"
            x["certification_reason"] = (
                "full-year pro-forma transaction value paired with post-acquisition revenue; "
                "hard exclusion pending a genuinely period-matched replacement"
            )
        out.append(x)
    return out


def certified_headline_counts(census):
    def yes(v):
        return str(v).lower() in {"true", "1", "yes"}

    # Historical 14-period direct candidate headline consisted of Blibli 3P annual
    # candidate years, Bukalapak matched Group years, and Tokopedia FY2021-23.
    direct_periods = []
    extension_retained = []
    for r in census:
        fam = r.get("sample_family", "")
        if fam in {"indonesia_aligned_direct_segment", "blibli_prospectus_candidates", "blibli_reported_source_universe", "bukalapak_annual_candidates"}:
            # Count only the intended annual candidate scopes, one canonical period each.
            platform = r.get("platform", "")
            seg = r.get("segment_scope", "")
            period = r.get("period", "")
            certified = r.get("certified_admission_status", "")
            canonical = yes(r.get("canonical_record", "True"))
            annual = r.get("frequency") == "annual"
            matched = r.get("period_match") == "yes"
            include_scope = (
                (platform.startswith("Tokopedia") and seg == "e-commerce segment")
                or (platform == "Blibli/GDN" and seg == "3P Retail")
                or (platform == "Bukalapak" and seg == "Group")
            )
            if canonical and annual and matched and include_scope and not certified.startswith("exclude"):
                direct_periods.append(r)

        if r.get("source_dataset") == "data/longitudinal/indonesia_platform_year_extension.csv" and not r.get("certified_admission_status", "").startswith("exclude"):
            extension_retained.append(r)

    # De-duplicate direct candidate periods by platform/scope/year because the Blibli
    # audit preserves multiple source families/vintages.
    direct_unique = {}
    for r in direct_periods:
        key = (r.get("platform"), r.get("segment_scope"), r.get("year"))
        # Prefer rows already marked canonical and ratio-eligible; otherwise retain one.
        current = direct_unique.get(key)
        if current is None or (yes(r.get("certified_ratio_eligible")) and not yes(current.get("certified_ratio_eligible"))):
            direct_unique[key] = r
    direct_unique_rows = list(direct_unique.values())

    return {
        "direct_candidate_periods_after_hard_exclusion": len(direct_unique_rows),
        "direct_candidate_positive_denominator_periods": sum(yes(r.get("certified_ratio_eligible")) for r in direct_unique_rows),
        "retained_indonesia_extension_periods": len(extension_retained),
        "conditional_country_periods": sum(r.get("directness_class") == "mixed_direct_derived_pair" for r in extension_retained),
        "retained_tokopedia_direct_segment_periods": sum(r.get("platform", "").startswith("Tokopedia") for r in extension_retained),
    }


def certified_bps_checks(base):
    checks, d = base.build_bps_certification()
    notes = {r["note_id"]: r for r in read_notes(base)}
    growth_note = notes["BPS-X01"]

    selected_growth = (d["business24"] / d["business23_selected"] - 1.0) * 100.0
    alt_2023 = 3934981.0
    alternative_growth = (d["business24"] / alt_2023 - 1.0) * 100.0
    official_growth = float(growth_note["reported_value"])

    target = next(r for r in checks if r["check_id"] == "BPS-06")
    if abs(selected_growth - official_growth) <= 0.02 and abs(alternative_growth - official_growth) > 1.0:
        target["status"] = "RESOLVED_FOR_CROSS_YEAR_SERIES"
        target["evidence"] = (
            f"2023 publication still contains 3,934,981 versus 3,816,750, but later official BPS reports 2024 business-count growth of {official_growth:.2f}%. "
            f"4,400,972 / 3,816,750 implies {selected_growth:.2f}%; using 3,934,981 implies {alternative_growth:.2f}%."
        )
        target["consequence"] = (
            "Use 3,816,750 as the cross-year series value because it matches the later official growth statement within rounding; preserve 3,934,981 as a documented source-text conflict, not an alternative analytical observation."
        )
    else:
        target["status"] = "REVIEW_LATER_OFFICIAL_CONSISTENCY"

    d["business23_alternative"] = alt_2023
    d["business_growth_selected_pct"] = selected_growth
    d["business_growth_alternative_pct"] = alternative_growth
    d["business_growth_later_official_pct"] = official_growth
    d["business_growth_official_source"] = growth_note["source_url"]
    return checks, d


def build_certified_review(base, samples, census_issues, exclusions, checks, d, counts):
    text = base.build_kong_review(samples, census_issues, exclusions, checks, d)
    count_insert = (
        "\n## Certified headline-count correction\n\n"
        "The historical comprehensive audit is preserved for lineage, but the advisor-facing overlay enforces the Tokopedia FY2021 hard exclusion. "
        f"The resulting direct Indonesia-aligned candidate headline is **{counts['direct_candidate_periods_after_hard_exclusion']} annual periods**, not 14; "
        f"**{counts['direct_candidate_positive_denominator_periods']}** have positive revenue denominators for ratio-style calculations. "
        f"The original nine-row Indonesia extension becomes **{counts['retained_indonesia_extension_periods']} retained periods**: "
        f"{counts['conditional_country_periods']} conditional Grab/Shopee country periods plus {counts['retained_tokopedia_direct_segment_periods']} valid Tokopedia direct-segment periods.\n"
    )
    insert = (
        "\n## BPS cross-year business-count resolution update\n\n"
        f"The 2023 publication's conflicting text is preserved, but the later official BPS 2024 growth statement provides a cross-wave consistency test. "
        f"BPS reports **{d['business_growth_later_official_pct']:.2f}%** year-on-year growth in the number of e-commerce businesses. "
        f"The retained 2023 count 3,816,750 implies **{d['business_growth_selected_pct']:.2f}%** growth to 4,400,972, while the conflicting 3,934,981 figure implies **{d['business_growth_alternative_pct']:.2f}%**. "
        "Accordingly, 3,816,750 is certified for the cross-year series on internal consistency with the later official release; the conflicting executive-summary number remains in the source audit rather than being erased.\n\n"
        f"Later official BPS source: {d['business_growth_official_source']}\n"
    )
    marker = "\n## 5. Decisions requested from the advisor\n"
    if marker in text:
        text = text.replace(marker, count_insert + insert + marker)
    else:
        text += count_insert + insert
    return text


def build_certified_decision_sheet(base, samples, checks, d, counts):
    text = base.build_decision_sheet(samples, checks)
    count_note = (
        "\n## Certified count status\n\n"
        f"After enforcing Tokopedia FY2021 exclusion: **{counts['direct_candidate_periods_after_hard_exclusion']}** direct candidate annual periods remain across Blibli 3P, Bukalapak Group and Tokopedia; "
        f"**{counts['direct_candidate_positive_denominator_periods']}** have positive revenue denominators. "
        f"The Indonesia extension retains **{counts['retained_indonesia_extension_periods']}** periods, not nine.\n"
    )
    note = (
        "\n## BPS count-series status\n\n"
        f"The 2023 main-body count **3,816,750** is the cross-year series value: it implies {d['business_growth_selected_pct']:.2f}% growth to the 2024 total, matching BPS's later official {d['business_growth_later_official_pct']:.2f}% statement. "
        f"The conflicting 3,934,981 passage is retained as a source-text issue but is not treated as a second observation.\n"
    )
    return text + count_note + note


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=ROOT / "build/empirical_review_certified")
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    base = load_base()
    samples, census_issues, exclusions, _ = base.build_sample_sensitivity()
    checks, d = certified_bps_checks(base)
    census = build_certified_census(base)
    counts = certified_headline_counts(census)

    base.write_csv(args.output / "sample_rule_sensitivity.csv", samples)
    base.write_csv(args.output / "census_admission_issues.csv", census_issues)
    base.write_csv(args.output / "hard_exclusions.csv", exclusions)
    base.write_csv(args.output / "certified_candidate_observation_census.csv", census)
    base.write_csv(args.output / "certified_headline_counts.csv", [counts])
    base.write_csv(args.output / "bps_certification_matrix.csv", checks)
    base.write_csv(args.output / "bps_external_certification_notes.csv", read_notes(base))
    (args.output / "KONG_DATA_REVIEW.md").write_text(
        build_certified_review(base, samples, census_issues, exclusions, checks, d, counts), encoding="utf-8"
    )
    (args.output / "KONG_DECISION_SHEET.md").write_text(
        build_certified_decision_sheet(base, samples, checks, d, counts), encoding="utf-8"
    )

    print(f"certified direct candidate periods: {counts['direct_candidate_periods_after_hard_exclusion']}")
    print(f"certified positive-denominator direct periods: {counts['direct_candidate_positive_denominator_periods']}")
    print(f"retained Indonesia extension periods: {counts['retained_indonesia_extension_periods']}")
    print(f"BPS business-count series growth: {d['business_growth_selected_pct']:.4f}%")
    print(f"later official BPS growth statement: {d['business_growth_later_official_pct']:.2f}%")
    print(f"conflicting-count implied growth: {d['business_growth_alternative_pct']:.4f}%")


if __name__ == "__main__":
    main()
