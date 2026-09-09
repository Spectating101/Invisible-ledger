#!/usr/bin/env python3
"""Execute the first Invisible Ledger hypothesis tests.

The script keeps direct Indonesia-aligned pairs, issuer pairs with unresolved
scope, and conditional country reconstructions in separate evidence tiers. It
also tests the BPS extensive-margin and province-recordkeeping hypotheses.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUTPUT = ROOT / "outputs" / "hypothesis_tests_2026-09-10"
FIGURES = ROOT / "reports" / "figures"
REPORT = ROOT / "reports" / "HYPOTHESIS_TESTS_2026-09-10.md"


def write_csv(frame: pd.DataFrame, name: str) -> None:
    frame.to_csv(OUTPUT / name, index=False)


def weighted_corr(x: np.ndarray, y: np.ndarray, weights: np.ndarray) -> float:
    weights = weights / weights.sum()
    mean_x = np.sum(weights * x)
    mean_y = np.sum(weights * y)
    covariance = np.sum(weights * (x - mean_x) * (y - mean_y))
    variance_x = np.sum(weights * (x - mean_x) ** 2)
    variance_y = np.sum(weights * (y - mean_y) ** 2)
    return float(covariance / np.sqrt(variance_x * variance_y))


def indonesia_candidate_levels() -> pd.DataFrame:
    extension = pd.read_csv(DATA / "longitudinal" / "indonesia_platform_year_extension.csv")
    extension["year"] = extension["period"].str.extract(r"(\d{4})").astype(int)

    rows: list[dict] = []

    # FY2021 Tokopedia remains excluded because the transaction and revenue
    # periods are not demonstrably matched. FY2022-FY2023 use the same later
    # annual-report comparative basis.
    tokopedia = extension[
        extension["platform"].str.startswith("Tokopedia")
        & extension["year"].isin([2022, 2023])
    ]
    for _, row in tokopedia.iterrows():
        rows.append(
            {
                "series": "Tokopedia e-commerce segment",
                "year": row.year,
                "transaction_value": row.transaction_value_native,
                "revenue_value": row.platform_revenue_native,
                "currency": "IDR",
                "unit": "million",
                "transaction_measure": "e-commerce GTV",
                "revenue_measure": "third-party net segment revenue",
                "evidence_tier": "direct_indonesia_aligned_segment",
                "admission_status": "candidate_core_not_advisor_approved",
                "geography_scope": "Indonesia-aligned segment; not country-labelled",
                "scope_warning": "FY2021 excluded because the archived pair is period-mismatched.",
                "source_dataset": "data/longitudinal/indonesia_platform_year_extension.csv",
            }
        )

    # Blibli 3P Retail: select the latest available publication vintage for each
    # economic year. The segment includes online commerce and travel.
    blibli = pd.read_csv(DATA / "longitudinal" / "blibli_reported_pairs_all_vintages.csv")
    blibli = blibli[(blibli.frequency == "annual") & (blibli.scope == "3P Retail")].copy()
    blibli["year"] = blibli.period.str.extract(r"(\d{4})").astype(int)
    blibli["vintage_year"] = blibli.source_id.str.extract(r"fy(\d{4})").astype(int)
    blibli = blibli.sort_values(["year", "vintage_year"]).drop_duplicates("year", keep="last")
    for _, row in blibli.iterrows():
        rows.append(
            {
                "series": "Blibli 3P Retail",
                "year": row.year,
                "transaction_value": row.tpv,
                "revenue_value": row.revenue,
                "currency": "IDR",
                "unit": "billion",
                "transaction_measure": "3P Retail TPV",
                "revenue_measure": "3P Retail net revenue",
                "evidence_tier": "direct_issuer_scope_pending",
                "admission_status": "candidate_pending_geography_and_scope",
                "geography_scope": "issuer segment; Indonesia eligibility under review",
                "scope_warning": "3P Retail includes online commerce and tiket.com travel.",
                "source_dataset": "data/longitudinal/blibli_reported_pairs_all_vintages.csv",
            }
        )

    bukalapak = pd.read_csv(DATA / "longitudinal" / "bukalapak_annual_candidates.csv")
    bukalapak = bukalapak[
        (bukalapak.tpv_months == 12)
        & (bukalapak.revenue_months == 12)
        & ~bukalapak.status.str.startswith("EXCLUDE")
    ]
    for _, row in bukalapak.iterrows():
        rows.append(
            {
                "series": "Bukalapak Group",
                "year": row.year,
                "transaction_value": row.tpv_idr_million,
                "revenue_value": row.revenue_idr_million,
                "currency": "IDR",
                "unit": "million",
                "transaction_measure": "Group TPV",
                "revenue_measure": "Group revenue",
                "evidence_tier": "direct_issuer_scope_pending",
                "admission_status": "candidate_pending_geography_and_scope",
                "geography_scope": "Group; overseas operations disclosed",
                "scope_warning": "Not established as Indonesia-only; FY2024 excluded for 9M/12M mismatch.",
                "source_dataset": "data/longitudinal/bukalapak_annual_candidates.csv",
            }
        )

    conditional = extension[
        extension.platform.isin(["Grab", "Shopee"])
    ]
    for _, row in conditional.iterrows():
        rows.append(
            {
                "series": row.platform,
                "year": row.year,
                "transaction_value": row.transaction_value_native,
                "revenue_value": row.platform_revenue_native,
                "currency": "USD",
                "unit": "billion",
                "transaction_measure": "derived/estimated Indonesia transaction value",
                "revenue_measure": "direct or derived Indonesia revenue",
                "evidence_tier": "conditional_country_reconstruction",
                "admission_status": "conditional_not_core",
                "geography_scope": "Indonesia anchor plus allocation assumption",
                "scope_warning": row.comparability_note,
                "source_dataset": "data/longitudinal/indonesia_platform_year_extension.csv",
            }
        )

    levels = pd.DataFrame(rows).sort_values(["evidence_tier", "series", "year"])
    levels["monetization_rate_pct"] = 100 * levels.revenue_value / levels.transaction_value
    levels["transaction_to_revenue_ratio"] = levels.transaction_value / levels.revenue_value
    if levels.duplicated(["series", "year"]).any():
        raise ValueError("Duplicate series-year after vintage selection")
    if (levels[["transaction_value", "revenue_value"]] <= 0).any().any():
        raise ValueError("Non-positive value in retained candidate levels")
    return levels


def build_transitions(levels: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for series, group in levels.groupby("series"):
        group = group.sort_values("year")
        for (_, previous), (_, current) in zip(group.iloc[:-1].iterrows(), group.iloc[1:].iterrows()):
            if current.year - previous.year != 1:
                continue
            transaction_growth = 100 * (current.transaction_value / previous.transaction_value - 1)
            revenue_growth = 100 * (current.revenue_value / previous.revenue_value - 1)
            if transaction_growth >= 0 and revenue_growth >= 0:
                direction = "activity_up_revenue_up"
            elif transaction_growth >= 0 and revenue_growth < 0:
                direction = "activity_up_revenue_down"
            elif transaction_growth < 0 and revenue_growth >= 0:
                direction = "activity_down_revenue_up"
            else:
                direction = "activity_down_revenue_down"
            rows.append(
                {
                    "series": series,
                    "transition": f"{int(previous.year)}-{int(current.year)}",
                    "evidence_tier": current.evidence_tier,
                    "admission_status": current.admission_status,
                    "transaction_growth_pct": transaction_growth,
                    "revenue_growth_pct": revenue_growth,
                    "revenue_minus_transaction_growth_pp": revenue_growth - transaction_growth,
                    "absolute_growth_difference_pp": abs(revenue_growth - transaction_growth),
                    "direction_class": direction,
                    "opposite_sign": np.sign(transaction_growth) != np.sign(revenue_growth),
                    "scope_warning": current.scope_warning,
                }
            )
    return pd.DataFrame(rows)


def transition_summary(transitions: pd.DataFrame) -> pd.DataFrame:
    rows = []
    groups = [("all_candidate_tiers", transitions)] + list(transitions.groupby("evidence_tier"))
    for label, group in groups:
        rows.append(
            {
                "evidence_tier": label,
                "transitions": len(group),
                "series": group.series.nunique(),
                "revenue_grows_faster": int((group.revenue_minus_transaction_growth_pp > 0).sum()),
                "transaction_grows_faster": int((group.revenue_minus_transaction_growth_pp < 0).sum()),
                "opposite_sign_transitions": int(group.opposite_sign.sum()),
                "median_signed_difference_pp": group.revenue_minus_transaction_growth_pp.median(),
                "median_absolute_difference_pp": group.absolute_growth_difference_pp.median(),
                "interpretation_limit": "Tiers are summarized separately; all-candidate totals are inventory diagnostics, not an approved pooled Indonesia sample.",
            }
        )
    return pd.DataFrame(rows)


def national_indicator_lookup() -> pd.DataFrame:
    return pd.read_csv(DATA / "bps_official" / "bps_ecommerce_national_indicators_2020_2023.csv")


def indicator_value(national: pd.DataFrame, year: int, indicator: str) -> float:
    row = national[(national.reference_year == year) & (national.indicator == indicator)]
    if len(row) != 1:
        raise ValueError(f"Expected one {indicator} value for {year}, found {len(row)}")
    return float(row.iloc[0].value)


def bps_growth_anatomy(national: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    levels = []
    for year in [2022, 2023, 2024]:
        total = indicator_value(national, year, "ecommerce_transaction_value")
        businesses = indicator_value(national, year, "estimated_number_of_ecommerce_businesses")
        marketplace = np.nan
        marketplace_status = "not_available"
        if year == 2023:
            marketplace = indicator_value(national, year, "marketplace_transaction_value")
            marketplace_status = "direct_official_estimate"
        elif year == 2024:
            share = indicator_value(national, year, "marketplace_share_of_transaction_value") / 100
            marketplace = total * share
            marketplace_status = "derived_from_official_total_and_share"
        levels.append(
            {
                "year": year,
                "transaction_value_idr_trillion": total,
                "estimated_ecommerce_businesses": businesses,
                "implied_idr_million_per_business": total * 1_000_000 / businesses,
                "marketplace_value_idr_trillion": marketplace,
                "nonmarketplace_value_idr_trillion": total - marketplace if pd.notna(marketplace) else np.nan,
                "marketplace_value_status": marketplace_status,
            }
        )
    levels_frame = pd.DataFrame(levels)
    growth_rows = []
    for previous, current in zip(levels[:-1], levels[1:]):
        row = {"transition": f"{previous['year']}-{current['year']}"}
        for label, field in [
            ("total_transaction_value", "transaction_value_idr_trillion"),
            ("estimated_businesses", "estimated_ecommerce_businesses"),
            ("implied_value_per_business", "implied_idr_million_per_business"),
            ("marketplace_component", "marketplace_value_idr_trillion"),
            ("nonmarketplace_component", "nonmarketplace_value_idr_trillion"),
        ]:
            if pd.notna(previous[field]) and pd.notna(current[field]):
                row[f"{label}_growth_pct"] = 100 * (current[field] / previous[field] - 1)
            else:
                row[f"{label}_growth_pct"] = np.nan
        growth_rows.append(row)
    growth = pd.DataFrame(growth_rows)

    financial = national[national.indicator == "ecommerce_businesses_with_financial_reports"][
        ["reference_year", "value", "source_status", "source_locator", "interpretation_limit"]
    ].rename(columns={"reference_year": "year", "value": "financial_reports_have_pct"})
    return levels_frame, growth, financial


def bps_joint_bounds(national: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year in [2023, 2024]:
        marketplace = indicator_value(national, year, "marketplace_sales_media_business_share") / 100
        financial = indicator_value(national, year, "ecommerce_businesses_with_financial_reports") / 100
        intersection_low = max(0.0, marketplace + financial - 1)
        intersection_high = min(marketplace, financial)
        neither_low = 1 - marketplace - financial + intersection_low
        neither_high = 1 - marketplace - financial + intersection_high
        rows.append(
            {
                "year": year,
                "marketplace_use_pct": 100 * marketplace,
                "financial_report_ownership_pct": 100 * financial,
                "joint_marketplace_and_reports_lower_pct": 100 * intersection_low,
                "joint_marketplace_and_reports_upper_pct": 100 * intersection_high,
                "neither_lower_pct": 100 * neither_low,
                "neither_upper_pct": 100 * neither_high,
                "interpretation": "Frechet bounds from separate national marginals; not a measured cross-tabulation.",
            }
        )
    return pd.DataFrame(rows)


def bps_province_tests() -> tuple[pd.DataFrame, pd.DataFrame]:
    p2023 = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_2023_province_financial_records_sales_media.csv")
    c2023 = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_2023_province_sampling_context.csv")
    p2023 = p2023.merge(
        c2023[["province", "estimated_ecommerce_businesses_2023"]],
        on="province",
        how="left",
        validate="one_to_one",
    ).rename(columns={"estimated_ecommerce_businesses_2023": "estimated_ecommerce_businesses"})
    p2024 = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_2024_province_financial_records_sales_media.csv")
    columns = [
        "province",
        "year",
        "financial_reports_have_pct",
        "marketplace_sales_media_pct",
        "estimated_ecommerce_businesses",
    ]
    panel = pd.concat([p2023[columns], p2024[columns]], ignore_index=True)
    panel = panel[panel.province != "Indonesia"]
    panel = panel.dropna(subset=columns[2:]).copy()

    rows = []
    for year, group in panel.groupby("year"):
        pearson = stats.pearsonr(group.marketplace_sales_media_pct, group.financial_reports_have_pct)
        spearman = stats.spearmanr(group.marketplace_sales_media_pct, group.financial_reports_have_pct)
        rows.append(
            {
                "specification": "province_cross_section",
                "year_or_change": str(int(year)),
                "province_n": len(group),
                "pearson_r": pearson.statistic,
                "pearson_p": pearson.pvalue,
                "spearman_rho": spearman.statistic,
                "spearman_p": spearman.pvalue,
                "business_count_weighted_r": weighted_corr(
                    group.marketplace_sales_media_pct.to_numpy(),
                    group.financial_reports_have_pct.to_numpy(),
                    group.estimated_ecommerce_businesses.to_numpy(),
                ),
                "interpretation": "Ecological cross-section; not a business-level marketplace effect.",
            }
        )

    wide = panel.pivot(
        index="province",
        columns="year",
        values=["financial_reports_have_pct", "marketplace_sales_media_pct", "estimated_ecommerce_businesses"],
    ).dropna()
    changes = pd.DataFrame(
        {
            "province": wide.index.to_numpy(),
            "change_financial_reports_pp": wide[("financial_reports_have_pct", 2024)]
            - wide[("financial_reports_have_pct", 2023)],
            "change_marketplace_use_pp": wide[("marketplace_sales_media_pct", 2024)]
            - wide[("marketplace_sales_media_pct", 2023)],
            "average_estimated_businesses": (
                wide[("estimated_ecommerce_businesses", 2024)]
                + wide[("estimated_ecommerce_businesses", 2023)]
            )
            / 2,
        }
    ).reset_index(drop=True)
    pearson = stats.pearsonr(changes.change_marketplace_use_pp, changes.change_financial_reports_pp)
    spearman = stats.spearmanr(changes.change_marketplace_use_pp, changes.change_financial_reports_pp)
    rows.append(
        {
            "specification": "within_province_change",
            "year_or_change": "2023-2024",
            "province_n": len(changes),
            "pearson_r": pearson.statistic,
            "pearson_p": pearson.pvalue,
            "spearman_rho": spearman.statistic,
            "spearman_p": spearman.pvalue,
            "business_count_weighted_r": weighted_corr(
                changes.change_marketplace_use_pp.to_numpy(),
                changes.change_financial_reports_pp.to_numpy(),
                changes.average_estimated_businesses.to_numpy(),
            ),
            "interpretation": "Ecological first difference; still not a business-level or causal effect.",
        }
    )
    return pd.DataFrame(rows), changes


def quality_findings() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "issue": "Tokopedia FY2021 period mismatch",
                "severity": "high",
                "affected_use": "longitudinal net-revenue series",
                "decision": "exclude from executed transitions",
                "reason": "Full-year pro-forma GTV is not matched to a demonstrably equivalent full-year net-revenue period.",
            },
            {
                "issue": "Blibli 3P scope includes online travel",
                "severity": "high",
                "affected_use": "Indonesia goods-marketplace interpretation",
                "decision": "retain in direct issuer scope-pending tier",
                "reason": "The pair is source-reported, but the segment perimeter is broader than marketplace goods commerce.",
            },
            {
                "issue": "Bukalapak overseas operations",
                "severity": "high",
                "affected_use": "Indonesia-only interpretation",
                "decision": "retain in direct issuer scope-pending tier",
                "reason": "Group transaction value and revenue are period-matched but not established as Indonesia-only.",
            },
            {
                "issue": "Bukalapak FY2024 reporting-period mismatch",
                "severity": "critical",
                "affected_use": "FY2024 ratio and transition",
                "decision": "exclude",
                "reason": "Transaction value covers nine months while revenue covers twelve months.",
            },
            {
                "issue": "Grab and Shopee Indonesia allocation dependence",
                "severity": "high",
                "affected_use": "country transaction/revenue interpretation",
                "decision": "retain as conditional tier only",
                "reason": "At least one country quantity is derived using a Group rate or external country-market estimate.",
            },
            {
                "issue": "BPS national business-count conflict for 2023",
                "severity": "medium",
                "affected_use": "business-count level and derived value per business",
                "decision": "use 3,816,750 with conflict disclosed",
                "reason": "The main body/figure value is consistent with the stated growth calculation; another passage reports 3,934,981.",
            },
            {
                "issue": "BPS province evidence is ecological",
                "severity": "high",
                "affected_use": "marketplace participation and recordkeeping hypothesis",
                "decision": "do not infer a business-level relationship",
                "reason": "Province marginals do not identify the joint status of individual businesses.",
            },
        ]
    )


def hypothesis_summary(
    transition_stats: pd.DataFrame,
    bps_growth: pd.DataFrame,
    province_results: pd.DataFrame,
) -> pd.DataFrame:
    overall = transition_stats[transition_stats.evidence_tier == "all_candidate_tiers"].iloc[0]
    latest_growth = bps_growth[bps_growth.transition == "2023-2024"].iloc[0]
    province_change = province_results[province_results.specification == "within_province_change"].iloc[0]
    return pd.DataFrame(
        [
            {
                "hypothesis": "H1 transaction and revenue growth can diverge",
                "status": "supported_in_candidate_inventory_not_final_sample",
                "evidence": f"{int(overall.transitions)} within-series transitions; {int(overall.opposite_sign_transitions)} opposite-sign; median absolute difference {overall.median_absolute_difference_pp:.2f} pp.",
                "boundary": "Evidence tiers include scope-pending and conditional cases; final Indonesia admission is unresolved.",
            },
            {
                "hypothesis": "H2 aggregate growth partly reflects more businesses",
                "status": "supported_for_2022_2024_aggregate_decomposition",
                "evidence": f"2023-2024 transaction value +{latest_growth.total_transaction_value_growth_pct:.2f}%, businesses +{latest_growth.estimated_businesses_growth_pct:.2f}%, implied value/business +{latest_growth.implied_value_per_business_growth_pct:.2f}%.",
                "boundary": "Nominal arithmetic decomposition; not causal entry or productivity evidence.",
            },
            {
                "hypothesis": "H3 marketplace participation predicts financial recordkeeping",
                "status": "not_established_by_province_evidence",
                "evidence": f"2023-2024 within-province change Pearson r={province_change.pearson_r:.3f} (p={province_change.pearson_p:.3f}); Spearman rho={province_change.spearman_rho:.3f} (p={province_change.spearman_p:.3f}).",
                "boundary": "Business-level microdata or an official joint cross-tabulation is required.",
            },
            {
                "hypothesis": "H4 institutional linkage failure",
                "status": "not_yet_tested",
                "evidence": "The repository documents distinct ledgers but not their actual administrative linkage.",
                "boundary": "Requires implementation and identifier/linkage evidence, not only legal rules.",
            },
            {
                "hypothesis": "H5 measurement choices can alter conclusions",
                "status": "supported_by_existing_measurement_modules",
                "evidence": "Reporting vintages, revenue definitions, and business perimeters alter levels and growth comparisons.",
                "boundary": "Economic consequence must be assessed comparison by comparison.",
            },
        ]
    )


def make_charts(
    transitions: pd.DataFrame,
    bps_growth: pd.DataFrame,
    province_results: pd.DataFrame,
) -> None:
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 12, "axes.labelsize": 10})

    colors = {
        "direct_indonesia_aligned_segment": "#1f5f99",
        "direct_issuer_scope_pending": "#d08c26",
        "conditional_country_reconstruction": "#7a7a7a",
    }
    plot_transitions = transitions.sort_values("revenue_minus_transaction_growth_pp")
    labels = [f"{row.series} · {row.transition}" for _, row in plot_transitions.iterrows()]
    fig, ax = plt.subplots(figsize=(10.0, 6.6))
    bars = ax.barh(
        labels,
        plot_transitions.revenue_minus_transaction_growth_pp,
        color=[colors[tier] for tier in plot_transitions.evidence_tier],
        edgecolor="#263238",
        linewidth=0.6,
    )
    for bar, (_, row) in zip(bars, plot_transitions.iterrows()):
        value = row.revenue_minus_transaction_growth_pp
        ax.text(
            value + 6,
            bar.get_y() + bar.get_height() / 2,
            f"{value:+.1f} pp" + (" *" if row.opposite_sign else ""),
            va="center",
            ha="left",
            fontsize=8,
        )
    from matplotlib.patches import Patch

    legend_handles = [
        Patch(facecolor=colors[tier], edgecolor="#263238", label=tier.replace("_", " "))
        for tier in colors
    ]
    ax.axvline(0, color="#303030", linewidth=0.9)
    ax.set_xlabel("Revenue growth minus transaction-measure growth (percentage points)")
    ax.set_ylabel("")
    ax.set_title("Indonesia candidate growth divergence")
    ax.legend(handles=legend_handles, frameon=False, fontsize=7, loc="lower right")
    ax.grid(axis="x", color="#e8e8e8", linewidth=0.6)
    ax.text(
        0.01,
        -0.10,
        "* Transaction and revenue moved in opposite directions. Evidence tiers are not one pooled sample.",
        transform=ax.transAxes,
        fontsize=8,
        color="#4a4a4a",
    )
    fig.tight_layout()
    fig.savefig(FIGURES / "indonesia_candidate_activity_revenue_growth.png", dpi=180)
    plt.close(fig)

    plot_growth = bps_growth.melt(
        id_vars="transition",
        value_vars=[
            "total_transaction_value_growth_pct",
            "estimated_businesses_growth_pct",
            "implied_value_per_business_growth_pct",
        ],
        var_name="measure",
        value_name="growth_pct",
    )
    labels = {
        "total_transaction_value_growth_pct": "Transaction value",
        "estimated_businesses_growth_pct": "Estimated businesses",
        "implied_value_per_business_growth_pct": "Implied value/business",
    }
    plot_growth["measure"] = plot_growth.measure.map(labels)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    pivot = plot_growth.pivot(index="transition", columns="measure", values="growth_pct")
    pivot[["Transaction value", "Estimated businesses", "Implied value/business"]].plot(
        kind="bar",
        ax=ax,
        color=["#1f5f99", "#d08c26", "#d7dde2"],
        edgecolor="#263238",
        linewidth=0.5,
    )
    ax.set_title("BPS national e-commerce growth anatomy")
    ax.set_xlabel("Reference-year transition")
    ax.set_ylabel("Nominal growth (%)")
    ax.tick_params(axis="x", rotation=0)
    ax.legend(frameon=False)
    ax.grid(axis="y", color="#e8e8e8", linewidth=0.6)
    fig.tight_layout()
    fig.savefig(FIGURES / "bps_national_growth_anatomy.png", dpi=180)
    plt.close(fig)

    correlation = province_results.melt(
        id_vars=["specification", "year_or_change", "province_n"],
        value_vars=["pearson_r", "spearman_rho", "business_count_weighted_r"],
        var_name="correlation_type",
        value_name="correlation",
    )
    correlation["label"] = correlation.year_or_change.replace({"2023-2024": "Change 2023-24"})
    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    marker_map = {"pearson_r": "o", "spearman_rho": "s", "business_count_weighted_r": "^"}
    color_map = {"pearson_r": "#1f5f99", "spearman_rho": "#d08c26", "business_count_weighted_r": "#6f7f45"}
    x_positions = {label: index for index, label in enumerate(correlation.label.unique())}
    for correlation_type, group in correlation.groupby("correlation_type"):
        ax.scatter(
            [x_positions[label] for label in group.label],
            group.correlation,
            marker=marker_map[correlation_type],
            color=color_map[correlation_type],
            s=70,
            label=correlation_type.replace("_", " "),
            edgecolor="#263238",
            linewidth=0.5,
        )
    ax.axhline(0, color="#303030", linewidth=0.8)
    ax.set_xticks(list(x_positions.values()), list(x_positions.keys()))
    ax.set_ylabel("Province-level correlation")
    ax.set_xlabel("Cross-section or within-province change")
    ax.set_title("Marketplace use and financial-report ownership")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(axis="y", color="#e8e8e8", linewidth=0.6)
    fig.tight_layout()
    fig.savefig(FIGURES / "bps_marketplace_recordkeeping_stability.png", dpi=180)
    plt.close(fig)


def write_report(
    levels: pd.DataFrame,
    transitions: pd.DataFrame,
    transition_stats: pd.DataFrame,
    bps_growth: pd.DataFrame,
    joint_bounds: pd.DataFrame,
    province_results: pd.DataFrame,
    hypotheses: pd.DataFrame,
) -> None:
    all_stats = transition_stats[transition_stats.evidence_tier == "all_candidate_tiers"].iloc[0]
    growth_2223 = bps_growth[bps_growth.transition == "2022-2023"].iloc[0]
    growth_2324 = bps_growth[bps_growth.transition == "2023-2024"].iloc[0]
    province_2023 = province_results[province_results.year_or_change == "2023"].iloc[0]
    province_2024 = province_results[province_results.year_or_change == "2024"].iloc[0]
    province_change = province_results[province_results.year_or_change == "2023-2024"].iloc[0]
    opposite = transitions[transitions.opposite_sign]
    growth_display = bps_growth.copy()
    for column in growth_display.columns.drop("transition"):
        growth_display[column] = growth_display[column].map(
            lambda value: "not available" if pd.isna(value) else f"{value:.2f}"
        )

    report = f"""# First executed hypothesis tests for *Invisible Ledger*

## Technical summary

The first tests produce a mixed but useful result. The expanded Indonesia
candidate inventory contains {len(levels)} matched annual levels across
{levels.series.nunique()} series and generates {len(transitions)} consecutive
within-series transitions. Transaction and revenue growth differ materially:
the median absolute difference is {all_stats.median_absolute_difference_pp:.2f}
percentage points and {int(all_stats.opposite_sign_transitions)} transitions
move in opposite directions. However, only the Tokopedia FY2022–FY2023
transition is currently in the direct Indonesia-aligned tier; the remaining
transitions are scope-pending issuer pairs or conditional country
reconstructions.

The official BPS aggregate evidence supports a second result. From 2022–2023,
nominal e-commerce transaction value grew {growth_2223.total_transaction_value_growth_pct:.2f}%
while estimated businesses grew {growth_2223.estimated_businesses_growth_pct:.2f}%,
leaving {growth_2223.implied_value_per_business_growth_pct:.2f}% growth in
implied value per business. From 2023–2024, the corresponding changes were
{growth_2324.total_transaction_value_growth_pct:.2f}%,
{growth_2324.estimated_businesses_growth_pct:.2f}%, and
{growth_2324.implied_value_per_business_growth_pct:.2f}%. This is consistent
with expansion in business participation contributing importantly to aggregate
growth, but it is an arithmetic decomposition rather than a causal entry or
productivity result.

The province evidence does not establish that marketplace participation predicts
financial-report ownership. The association changes materially between the
2023 and 2024 cross-sections and is weak in within-province changes. A
business-level cross-tabulation or licensed microdata remains necessary.

## Revenue and transaction activity diverge, but evidence tiers matter

The analysis compares growth only within the same platform series. Monetary
levels are never added across companies or currencies. The executed candidates
are divided into three tiers:

- direct Indonesia-aligned segment: Tokopedia FY2022–FY2023;
- direct issuer pairs with unresolved scope: Blibli 3P Retail and Bukalapak Group;
- conditional country reconstructions: Grab and Shopee.

Across all three tiers, {int(all_stats.revenue_grows_faster)} transitions show
revenue growing faster and {int(all_stats.transaction_grows_faster)} show the
transaction measure growing faster. The opposite-sign cases are:

{opposite[['series', 'transition', 'transaction_growth_pct', 'revenue_growth_pct', 'evidence_tier']].to_markdown(index=False, floatfmt='.2f') if len(opposite) else 'None.'}

![Indonesia candidate activity and revenue growth](figures/indonesia_candidate_activity_revenue_growth.png)

The figure is a candidate-coverage diagnostic, not an approved pooled sample.
Positive bars have faster revenue growth; negative bars have faster transaction
growth. Tokopedia FY2021 is excluded for period mismatch,
Bukalapak FY2024 is excluded because TPV covers nine months while revenue covers
twelve, and the Blibli and Bukalapak histories remain outside a strict
Indonesia-only tier.

## BPS growth is substantially associated with expansion in estimated businesses

{growth_display.to_markdown(index=False)}

![BPS national growth anatomy](figures/bps_national_growth_anatomy.png)

The chart separates growth in the aggregate nominal transaction estimate from
growth in the estimated business population and the residual implied value per
business. It does not identify firm entry, survival, inflation-adjusted output,
or productivity. The 2023 business count also retains a documented source
conflict; the executed value is the main-body figure consistent with BPS's
published growth calculation.

The 2023–2024 marketplace component grew approximately
{growth_2324.marketplace_component_growth_pct:.2f}%, while the non-marketplace
component grew {growth_2324.nonmarketplace_component_growth_pct:.2f}%. The 2024
component is derived mechanically from BPS's published total and share. This
supports treating non-marketplace digital commerce as central to the national
measurement question rather than equating e-commerce with platform marketplaces.

## Province evidence does not validate a business-level recordkeeping effect

{province_results.to_markdown(index=False, floatfmt='.3f')}

![BPS province association stability](figures/bps_marketplace_recordkeeping_stability.png)

The 2023 marketplace/financial-report association is modest (Pearson
`r={province_2023.pearson_r:.3f}`, `p={province_2023.pearson_p:.3f}`), while the
2024 cross-sectional association is close to zero (Pearson
`r={province_2024.pearson_r:.3f}`, `p={province_2024.pearson_p:.3f}`). The
within-province change association is positive but uncertain (Pearson
`r={province_change.pearson_r:.3f}`, `p={province_change.pearson_p:.3f}`;
Spearman `rho={province_change.spearman_rho:.3f}`,
`p={province_change.spearman_p:.3f}`).

The instability is substantively important: province marginals cannot tell us
whether the same individual businesses both use marketplaces and maintain
financial reports. The national Fréchet bounds remain wide:

{joint_bounds.to_markdown(index=False, floatfmt='.2f')}

These bounds show what is mathematically possible from the marginals; they are
not observed joint percentages.

## Hypothesis status after execution

{hypotheses.to_markdown(index=False)}

## Scope, methods, and definitions

- Unit for issuer growth: one consecutive annual transition within a single
  platform/segment and stable selected revenue definition.
- Unit for BPS national decomposition: Indonesia reference year.
- Unit for BPS association: province-year or within-province first difference.
- Revenue and transaction growth are nominal and calculated within original
  currencies, so no FX conversion is required for rates.
- Pearson, Spearman, and business-count-weighted correlations are descriptive.
  No causal model is estimated.
- Annual totals, quarters, reporting vintages, and source inputs are not added
  into one observation count.

## Limitations and decision gates

1. The final Indonesia main sample is not advisor-approved.
2. Blibli includes travel and Bukalapak includes overseas activity.
3. Grab and Shopee country series remain model-dependent.
4. BPS province evidence is ecological; survey microdata are still needed for
   business-level inference.
5. The BPS national series contains a documented 2023 business-count conflict.
6. The tests do not measure missing GDP, tax liability, or undeclared income.

## Recommended next steps

1. Resolve Indonesia candidate admission and publication-vintage rules.
2. Recover gross revenue, incentives, and comparable-basis components for every
   admissible issuer transition.
3. Seek an official BPS marketplace-by-financial-report cross-tabulation or
   approved microdata access.
4. Build the institutional visibility matrix only from verified reporting and
   implementation evidence.
5. Take the resulting sample census and the negative BPS province result to
   Kong before restructuring the manuscript.
"""
    REPORT.write_text(report, encoding="utf-8")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    levels = indonesia_candidate_levels()
    transitions = build_transitions(levels)
    transition_stats = transition_summary(transitions)
    national = national_indicator_lookup()
    bps_levels, bps_growth, financial = bps_growth_anatomy(national)
    joint_bounds = bps_joint_bounds(national)
    province_results, province_changes = bps_province_tests()
    quality = quality_findings()
    hypotheses = hypothesis_summary(transition_stats, bps_growth, province_results)

    write_csv(levels, "indonesia_longitudinal_candidate_levels.csv")
    write_csv(transitions, "indonesia_longitudinal_candidate_transitions.csv")
    write_csv(transition_stats, "indonesia_longitudinal_transition_summary.csv")
    write_csv(bps_levels, "bps_national_levels.csv")
    write_csv(bps_growth, "bps_national_growth_anatomy.csv")
    write_csv(financial, "bps_financial_report_timeline.csv")
    write_csv(joint_bounds, "bps_joint_status_bounds.csv")
    write_csv(province_results, "bps_province_hypothesis_results.csv")
    write_csv(province_changes, "bps_within_province_changes.csv")
    write_csv(quality, "data_quality_findings.csv")
    write_csv(hypotheses, "hypothesis_status.csv")

    make_charts(transitions, bps_growth, province_results)
    write_report(levels, transitions, transition_stats, bps_growth, joint_bounds, province_results, hypotheses)

    print(f"candidate_levels={len(levels)}")
    print(f"candidate_transitions={len(transitions)}")
    print(f"province_year_tests={len(province_results)}")
    print(f"report={REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
