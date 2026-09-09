#!/usr/bin/env python3
"""Build source-bounded mechanism checks for selected issuer sign reversals.

This module does not search for a universal cause. It links only mechanisms that are
explicitly supported by current source evidence and preserves unexplained reversals as
unresolved. It is supplementary to build_issuer_movement_bridge.py.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_EXTRACT = ROOT / "research/issuer_movement_bridge/mechanism_source_extract.csv"
TOKOPEDIA_RECON = ROOT / "data/measurement/results/tokopedia_fy2022_2023_revenue_incentive_reconciliation.csv"
INDONESIA_EXTENSION = ROOT / "data/longitudinal/indonesia_platform_year_extension.csv"
BLIBLI_PROSPECTUS = ROOT / "data/longitudinal/blibli_prospectus_2019_2020_candidates.csv"
BLIBLI_REPORTED = ROOT / "data/longitudinal/blibli_reported_pairs_all_vintages.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def one(rows: list[dict[str, str]], predicate, label: str) -> dict[str, str]:
    matches = [r for r in rows if predicate(r)]
    if len(matches) != 1:
        raise ValueError(f"{label}: expected one row, found {len(matches)}")
    return matches[0]


def number(row: dict[str, str], field: str = "value") -> float:
    x = float(row[field])
    if not math.isfinite(x):
        raise ValueError(f"non-finite {field}: {x}")
    return x


def pct_growth(new: float, old: float) -> float:
    if not (math.isfinite(new) and math.isfinite(old)) or old <= 0:
        raise ValueError("growth requires finite values and a positive base")
    return (new / old - 1.0) * 100.0


def metric(rows: list[dict[str, str]], source_id: str, period: str, name: str) -> float:
    r = one(
        rows,
        lambda x: x["source_id"] == source_id and x["period"] == period and x["metric"] == name,
        f"{source_id} {period} {name}",
    )
    return number(r)


def build_cases() -> tuple[list[dict], dict[str, float]]:
    src = read_csv(SOURCE_EXTRACT)

    # Blibli 3P FY2022->FY2023: exact within-release segment revenue identity.
    rev22 = metric(src, "blibli_ar2023_3p", "FY2022", "revenue_before_discount_and_direct_promotion")
    promo22 = metric(src, "blibli_ar2023_3p", "FY2022", "discount_and_direct_promotion")
    net22 = metric(src, "blibli_ar2023_3p", "FY2022", "net_revenue")
    rev23 = metric(src, "blibli_ar2023_3p", "FY2023", "revenue_before_discount_and_direct_promotion")
    promo23 = metric(src, "blibli_ar2023_3p", "FY2023", "discount_and_direct_promotion")
    net23 = metric(src, "blibli_ar2023_3p", "FY2023", "net_revenue")
    if not (math.isclose(rev22 - promo22, net22) and math.isclose(rev23 - promo23, net23)):
        raise ValueError("Blibli 3P revenue identities do not reconcile")
    revenue_increase = rev23 - rev22
    promotion_reduction = promo22 - promo23
    net_increase = net23 - net22
    if not math.isclose(revenue_increase + promotion_reduction, net_increase):
        raise ValueError("Blibli 3P net-revenue change decomposition does not reconcile")

    # Use same-vintage TPV values only to contextualize the movement. FY2023 annual
    # report reports 49,917; the later-comparative canonical series uses 49,912.
    # The mechanism decomposition itself does not depend on that 5bn vintage difference.
    blibli_reported = read_csv(BLIBLI_REPORTED)
    tpv22 = number(one(
        blibli_reported,
        lambda x: x["scope"] == "3P Retail" and x["period"] == "2022FY" and x["source_id"] == "blibli_fy2022_linked_0",
        "Blibli 3P 2022 TPV",
    ), "tpv")
    tpv23 = 49917.0

    cases: list[dict] = [{
        "case_id": "blibli_3p_2022_2023_promotion_reconciliation",
        "platform": "Blibli/GDN",
        "scope": "3P Retail",
        "period": "FY2022->FY2023",
        "activity_growth_pct": pct_growth(tpv23, tpv22),
        "recognized_revenue_growth_pct": pct_growth(net23, net22),
        "other_metric_growth_pct": pct_growth(rev23, rev22),
        "other_metric": "revenue_before_discount_and_direct_promotion",
        "monetization_change_pp": (net23 / tpv23 - net22 / tpv22) * 100.0,
        "mechanism_status": "arithmetic_reconciliation_plus_issuer_context",
        "mechanism_evidence": (
            "Net-revenue increase reconciles to higher segment revenue before discount/direct promotion "
            "plus a reduction in discount/direct promotion. The issuer separately attributes stronger 3P GPBD "
            "to recovered OTA travel/lifestyle activity and higher digital-products contribution."
        ),
        "mechanism_source": "Blibli Annual Report 2023, operational review and segment revenue table",
        "interpretation_limit": "Arithmetic decomposition and issuer explanation; not a causal estimate.",
    }]

    # Blibli 3P FY2024->FY2025: direct sign reversal with issuer-stated margin/mix mechanism.
    tpv24 = metric(src, "blibli_fy25_3p", "FY2024", "tpv")
    net24 = metric(src, "blibli_fy25_3p", "FY2024", "net_revenue")
    gpbd24 = metric(src, "blibli_fy25_3p", "FY2024", "gpbd")
    tpv25 = metric(src, "blibli_fy25_3p", "FY2025", "tpv")
    net25 = metric(src, "blibli_fy25_3p", "FY2025", "net_revenue")
    gpbd25 = metric(src, "blibli_fy25_3p", "FY2025", "gpbd")
    cases.append({
        "case_id": "blibli_3p_2024_2025_margin_mix",
        "platform": "Blibli/GDN",
        "scope": "3P Retail",
        "period": "FY2024->FY2025",
        "activity_growth_pct": pct_growth(tpv25, tpv24),
        "recognized_revenue_growth_pct": pct_growth(net25, net24),
        "other_metric_growth_pct": pct_growth(gpbd25, gpbd24),
        "other_metric": "GPBD",
        "monetization_change_pp": (net25 / tpv25 - net24 / tpv24) * 100.0,
        "mechanism_status": "issuer_documented_business_mix_and_efficiency",
        "mechanism_evidence": (
            "Issuer reports 3P GPBD improvement was mainly driven by a shift in OTA toward higher-margin "
            "accommodation/experiences plus operating-efficiency measures; TPV fell while net revenue and GPBD rose."
        ),
        "mechanism_source": "Blibli FY2025 earnings release, 3P Retail segment overview",
        "interpretation_limit": "Management attribution is evidence of mechanism context, not independent causal identification.",
    })

    # Tokopedia FY2022->FY2023: use existing verified incentive reconciliation.
    tok = one(read_csv(TOKOPEDIA_RECON), lambda x: x["period_change"] == "FY2022_to_FY2023", "Tokopedia reconciliation")
    ext = read_csv(INDONESIA_EXTENSION)
    t22 = one(ext, lambda x: x["platform"].startswith("Tokopedia") and x["period"] == "FY2022", "Tokopedia FY2022")
    t23 = one(ext, lambda x: x["platform"].startswith("Tokopedia") and x["period"] == "FY2023", "Tokopedia FY2023")
    tv22, tv23 = float(t22["transaction_value_native"]), float(t23["transaction_value_native"])
    nr22, nr23 = float(t22["platform_revenue_native"]), float(t23["platform_revenue_native"])
    incentive_share = float(tok["incentive_reduction_share_of_net_change"])
    gross_share = float(tok["gross_revenue_share_of_net_change"])
    if not math.isclose(incentive_share + gross_share, 1.0, abs_tol=1e-12):
        raise ValueError("Tokopedia decomposition shares do not sum to one")
    cases.append({
        "case_id": "tokopedia_2022_2023_incentive_reconciliation",
        "platform": "Tokopedia",
        "scope": "e-commerce segment",
        "period": "FY2022->FY2023",
        "activity_growth_pct": pct_growth(tv23, tv22),
        "recognized_revenue_growth_pct": pct_growth(nr23, nr22),
        "other_metric_growth_pct": gross_share * 100.0,
        "other_metric": "share_of_net_revenue_change_from_higher_gross_revenue_pct",
        "monetization_change_pp": (nr23 / tv23 - nr22 / tv22) * 100.0,
        "mechanism_status": "arithmetic_reconciliation",
        "mechanism_evidence": (
            f"{incentive_share * 100.0:.2f}% of the arithmetic net-revenue increase is associated with lower "
            f"customer incentives and {gross_share * 100.0:.2f}% with higher gross revenue."
        ),
        "mechanism_source": "existing Tokopedia FY2022-FY2023 revenue/incentive reconciliation",
        "interpretation_limit": "Arithmetic decomposition only; not causal.",
    })

    # Blibli 3P FY2020->FY2021: preserve the sign reversal but do not invent a cause.
    prospectus = read_csv(BLIBLI_PROSPECTUS)
    p20 = one(prospectus, lambda x: x["scope"] == "3P Retail" and x["year"] == "2020", "Blibli 3P FY2020")
    r21 = one(
        blibli_reported,
        lambda x: x["scope"] == "3P Retail" and x["period"] == "2021FY" and x["source_id"] == "blibli_fy2022_linked_0",
        "Blibli 3P FY2021",
    )
    tv20 = float(p20["tpv_idr_million"]) / 1000.0
    nr20 = float(p20["net_revenue_idr_million"]) / 1000.0
    gp20 = float(p20["gpbd_idr_million"]) / 1000.0
    tv21, nr21, gp21 = float(r21["tpv"]), float(r21["revenue"]), float(r21["gpbd"])
    cases.append({
        "case_id": "blibli_3p_2020_2021_unresolved",
        "platform": "Blibli/GDN",
        "scope": "3P Retail",
        "period": "FY2020->FY2021",
        "activity_growth_pct": pct_growth(tv21, tv20),
        "recognized_revenue_growth_pct": pct_growth(nr21, nr20),
        "other_metric_growth_pct": pct_growth(gp21, gp20),
        "other_metric": "GPBD",
        "monetization_change_pp": (nr21 / tv21 - nr20 / tv20) * 100.0,
        "mechanism_status": "unresolved",
        "mechanism_evidence": "No reviewed source in this module is sufficient to explain the opposite-sign TPV/net-revenue movement.",
        "mechanism_source": "movement data only; mechanism source not established",
        "interpretation_limit": "Do not infer a cause from the sign reversal alone.",
    })

    diagnostics = {
        "blibli_2022_2023_revenue_increase": revenue_increase,
        "blibli_2022_2023_promotion_reduction": promotion_reduction,
        "blibli_2022_2023_net_revenue_increase": net_increase,
        "blibli_2022_2023_revenue_share": revenue_increase / net_increase,
        "blibli_2022_2023_promotion_share": promotion_reduction / net_increase,
    }
    return cases, diagnostics


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(cases: list[dict], d: dict[str, float]) -> str:
    by_id = {r["case_id"]: r for r in cases}
    b23 = by_id["blibli_3p_2022_2023_promotion_reconciliation"]
    b25 = by_id["blibli_3p_2024_2025_margin_mix"]
    tok = by_id["tokopedia_2022_2023_incentive_reconciliation"]
    unresolved = by_id["blibli_3p_2020_2021_unresolved"]
    return f"""# Mechanism bridge — research checkpoint

This module asks **why** selected activity/revenue divergences occur where the source record permits an answer. It does not force every reversal into one explanation.

## 1. Tokopedia FY2022→FY2023: incentives materially change the revenue story

Transaction value changes **{tok['activity_growth_pct']:.2f}%** while recognized net revenue changes **{tok['recognized_revenue_growth_pct']:.2f}%**. The existing reconciliation attributes **60.56%** of the arithmetic increase in net revenue to lower customer incentives and **39.44%** to higher gross revenue. Monetization measured as net revenue / transaction value rises by **{tok['monetization_change_pp']:.2f} percentage points**.

This is a concrete mechanism for why recognized revenue can rise sharply while transaction activity falls. It is an arithmetic reconciliation, not a causal decomposition.

## 2. Blibli 3P FY2022→FY2023: direct promotions and business mix both matter

Within the same FY2023 annual-report vintage, 3P segment revenue before discount/direct promotion rises from Rp1,314bn to Rp1,978bn, while discount/direct promotion falls from Rp1,115bn to Rp853bn. Net revenue therefore rises from Rp199bn to Rp1,125bn.

The Rp{d['blibli_2022_2023_net_revenue_increase']:.0f}bn net-revenue increase reconciles exactly to:

- **Rp{d['blibli_2022_2023_revenue_increase']:.0f}bn ({d['blibli_2022_2023_revenue_share']*100:.2f}%)** from higher segment revenue before discount/direct promotion; and
- **Rp{d['blibli_2022_2023_promotion_reduction']:.0f}bn ({d['blibli_2022_2023_promotion_share']*100:.2f}%)** from lower discount/direct promotion.

The same annual report says 3P GPBD improvement was mainly driven by greater OTA contribution after travel/lifestyle recovery plus stronger digital-products contribution. TPV rises about **{b23['activity_growth_pct']:.2f}%**, but net revenue rises **{b23['recognized_revenue_growth_pct']:.2f}%**. The point is not that revenue is distorted; it is that promotion intensity and mix can make recognized revenue move very differently from transaction scale.

## 3. Blibli 3P FY2024→FY2025: a documented margin/mix sign reversal

TPV changes **{b25['activity_growth_pct']:.2f}%**, net revenue changes **{b25['recognized_revenue_growth_pct']:.2f}%**, and GPBD changes **{b25['other_metric_growth_pct']:.2f}%**. Net-revenue/TPV monetization rises by **{b25['monetization_change_pp']:.2f} percentage points**.

The FY2025 issuer release attributes improved 3P GPBD mainly to a deliberate shift in OTA toward higher-margin accommodation and experiences plus operating-efficiency measures. This is unusually useful for *Invisible Ledger*: the transaction ledger says slight contraction, while the corporate revenue/margin ledger says improvement, and the issuer provides a business-model explanation for why both can be true.

Management attribution is mechanism evidence, not independent causal identification.

## 4. Blibli 3P FY2020→FY2021 remains unresolved

TPV changes **{unresolved['activity_growth_pct']:.2f}%**, net revenue **{unresolved['recognized_revenue_growth_pct']:.2f}%**, and GPBD **{unresolved['other_metric_growth_pct']:.2f}%**. The source review in this module does not establish why net revenue moved in the opposite direction. It remains an empirical reversal with an **unresolved mechanism**.

This unresolved case is intentional: a strong thesis should distinguish observed divergence from explained divergence instead of assigning every pattern to incentives or accounting choices.

## Thesis implication

Across the explained cases, the evidence supports a sharper proposition than the original transaction-revenue residual:

> **Transaction activity and recognized revenue are related but economically non-equivalent state variables. Changes in incentives, monetization and business mix can make them move at very different rates or in opposite directions.**

That proposition matters because a company-revenue view can give a materially different account of ecosystem movement from a transaction-activity view. It does not imply that either ledger is incorrect, nor does it identify participant income, GDP omission or tax non-compliance.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "research/issuer_movement_bridge/results")
    args = parser.parse_args()
    cases, diagnostics = build_cases()
    args.output.mkdir(parents=True, exist_ok=True)
    write_csv(args.output / "mechanism_cases.csv", cases)
    (args.output / "MECHANISMS.md").write_text(build_markdown(cases, diagnostics), encoding="utf-8")
    print(f"mechanism cases: {len(cases)}")


if __name__ == "__main__":
    main()
