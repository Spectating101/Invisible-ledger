#!/usr/bin/env python3
"""Certified overlay for the advisor-facing empirical review package.

Builds on build_empirical_review_package.py, but incorporates later official BPS
cross-wave consistency evidence without deleting the preserved source conflict.
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


def build_certified_review(base, samples, census_issues, exclusions, checks, d):
    text = base.build_kong_review(samples, census_issues, exclusions, checks, d)
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
        text = text.replace(marker, insert + marker)
    else:
        text += insert
    return text


def build_certified_decision_sheet(base, samples, checks, d):
    text = base.build_decision_sheet(samples, checks)
    note = (
        "\n## BPS count-series status\n\n"
        f"The 2023 main-body count **3,816,750** is the cross-year series value: it implies {d['business_growth_selected_pct']:.2f}% growth to the 2024 total, matching BPS's later official {d['business_growth_later_official_pct']:.2f}% statement. "
        f"The conflicting 3,934,981 passage is retained as a source-text issue but is not treated as a second observation.\n"
    )
    return text + note


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=ROOT / "build/empirical_review_certified")
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    base = load_base()
    samples, census_issues, exclusions, _ = base.build_sample_sensitivity()
    checks, d = certified_bps_checks(base)

    base.write_csv(args.output / "sample_rule_sensitivity.csv", samples)
    base.write_csv(args.output / "census_admission_issues.csv", census_issues)
    base.write_csv(args.output / "hard_exclusions.csv", exclusions)
    base.write_csv(args.output / "bps_certification_matrix.csv", checks)
    base.write_csv(args.output / "bps_external_certification_notes.csv", read_notes(base))
    (args.output / "KONG_DATA_REVIEW.md").write_text(
        build_certified_review(base, samples, census_issues, exclusions, checks, d), encoding="utf-8"
    )
    (args.output / "KONG_DECISION_SHEET.md").write_text(
        build_certified_decision_sheet(base, samples, checks, d), encoding="utf-8"
    )

    print(f"BPS business-count series growth: {d['business_growth_selected_pct']:.4f}%")
    print(f"later official BPS growth statement: {d['business_growth_later_official_pct']:.2f}%")
    print(f"conflicting-count implied growth: {d['business_growth_alternative_pct']:.4f}%")


if __name__ == "__main__":
    main()
