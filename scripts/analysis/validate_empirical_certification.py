#!/usr/bin/env python3
"""Validate the certified empirical status layer.

This validator is intentionally narrow. It checks the established-findings and
advisor-review boundary without choosing the final thesis sample or touching the
hypotheses agenda.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pct(new: float, old: float) -> float:
    return (new / old - 1.0) * 100.0


def validate_indonesia() -> dict[str, float | int]:
    rows = read_csv(ROOT / "data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv")
    direct_admissions = {"candidate_scope_pending", "candidate_geography_pending", "strongest_direct_candidate"}
    direct = [r for r in rows if r["certified_admission"] in direct_admissions]
    assert len(direct) == 13, f"expected 13 direct candidates, got {len(direct)}"
    assert sum(r["ratio_status"] == "eligible_direct_pair" for r in direct) == 12

    extension = [r for r in rows if r["platform"] in {"Grab", "Shopee", "Tokopedia"} and r["certified_admission"] != "exclude_period_mismatch"]
    assert len(extension) == 8, f"expected 8 retained extension observations, got {len(extension)}"
    assert sum(r["certified_admission"] == "conditional_sensitivity" for r in extension) == 6
    assert sum(r["certified_admission"] == "strongest_direct_candidate" for r in extension) == 2

    exclusions = [r for r in rows if r["certified_admission"].startswith("exclude")]
    assert {(r["platform"], r["period"]) for r in exclusions} == {("Tokopedia", "FY2021"), ("Bukalapak", "FY2024")}

    groups: dict[tuple[str, str], list[dict[str, str]]] = {}
    for r in direct:
        groups.setdefault((r["platform"], r["business_scope"]), []).append(r)

    transitions = []
    for key, group in groups.items():
        group = sorted(group, key=lambda x: int(x["period"].replace("FY", "")))
        for a, b in zip(group, group[1:]):
            ya = int(a["period"].replace("FY", ""))
            yb = int(b["period"].replace("FY", ""))
            if yb != ya + 1:
                continue
            tv0, tv1 = float(a["transaction_value"]), float(b["transaction_value"])
            rev0, rev1 = float(a["revenue_value"]), float(b["revenue_value"])
            # Ratio/growth interpretation requires positive bases. This excludes
            # Blibli FY2019→FY2020 because FY2019 net revenue is negative.
            if tv0 <= 0 or rev0 <= 0 or tv1 <= 0 or rev1 <= 0:
                continue
            tg, rg = pct(tv1, tv0), pct(rev1, rev0)
            transitions.append((key, ya, yb, tg, rg, abs(rg - tg)))

    assert len(transitions) == 9, f"expected 9 direct transitions, got {len(transitions)}"
    reversals = [t for t in transitions if (t[3] < 0) != (t[4] < 0)]
    assert len(reversals) == 3, f"expected 3 sign reversals, got {len(reversals)}"
    med = median(t[5] for t in transitions)
    assert math.isclose(med, 42.9401737278, abs_tol=1e-5), med
    assert sum(t[4] > t[3] for t in transitions) == 6
    assert sum(t[3] > t[4] for t in transitions) == 3

    return {
        "direct_candidates": len(direct),
        "positive_denominator_direct": sum(r["ratio_status"] == "eligible_direct_pair" for r in direct),
        "retained_extension": len(extension),
        "direct_transitions": len(transitions),
        "opposite_sign_transitions": len(reversals),
        "median_abs_growth_gap_pp": med,
    }


def validate_bps() -> dict[str, str]:
    rows = {r["item"]: r for r in read_csv(ROOT / "data/bps_official/bps_certification_status_2026-09-10.csv")}
    assert rows["2023_to_2024_total_transaction_growth"]["value_or_result"] == "17.08%"
    assert rows["2024_marketplace_component_value"]["status"] == "established"
    assert rows["2024_marketplace_component_value"]["value_or_result"] == "Rp203.58 trillion"
    assert rows["2023_to_2024_marketplace_component_growth"]["status"] == "established_descriptive_cross_wave"
    assert rows["2023_to_2024_marketplace_component_growth"]["value_or_result"] == "1.45%"
    assert rows["2023_to_2024_nonmarketplace_component_growth"]["value_or_result"] == "20.57%"
    assert rows["financial_report_ownership_cross_wave_trend"]["status"] == "guarded_cross_wave_interpretation"
    assert rows["2024_province_count_reconciliation"]["status"] == "established_source_residual"
    return {
        "marketplace_growth": rows["2023_to_2024_marketplace_component_growth"]["value_or_result"],
        "nonmarketplace_growth": rows["2023_to_2024_nonmarketplace_component_growth"]["value_or_result"],
    }


def validate_global() -> dict[str, int]:
    rows = read_csv(ROOT / "data/global_ecommerce/global_platform_summary.csv")
    vals = {r["metric"]: float(r["value"]) for r in rows}
    assert int(vals["matched_issuer_years"]) == 48
    assert int(vals["annual_transitions"]) == 40
    assert int(vals["clean_scope_transitions"]) == 29
    assert int(vals["opposite_direction_transitions_clean"]) == 4
    return {
        "matched_issuer_years": 48,
        "annual_transitions": 40,
        "clean_scope_transitions": 29,
        "clean_sign_reversals": 4,
    }


def validate_findings_text() -> None:
    text = (ROOT / "docs/EMPIRICAL_FINDINGS_2026-09-10.md").read_text(encoding="utf-8")
    required = [
        "contains **13** economic periods rather than the historical audit headline of 14",
        "retains **8** observations rather than nine",
        "**9 adjacent annual transitions**",
        "marketplace component: **Rp200.68T → Rp203.58T, +1.45%**",
        "non-marketplace component: **Rp900.19T → Rp1,085.35T, +20.57%**",
        "**48 matched issuer-years**",
        "**29 clean-screened transitions**",
    ]
    for phrase in required:
        assert phrase in text, f"findings ledger missing: {phrase}"


def main() -> None:
    i = validate_indonesia()
    b = validate_bps()
    g = validate_global()
    validate_findings_text()
    print("empirical certification OK")
    print(i)
    print(b)
    print(g)


if __name__ == "__main__":
    main()
