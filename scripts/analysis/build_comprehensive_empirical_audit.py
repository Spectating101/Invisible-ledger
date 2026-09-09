#!/usr/bin/env python3
"""Build a comprehensive, non-destructive census of Invisible Ledger evidence.

The script never edits source data. It separates source/input rows from analytical
observations and keeps incompatible geographic, accounting, and temporal scopes in
different sample families.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "empirical_backend_2026-09-09"
CHARTS = OUT / "charts"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_csv(df: pd.DataFrame, name: str) -> None:
    df.to_csv(OUT / name, index=False)


def numeric_year(value) -> float:
    match = re.search(r"(20\d{2})", str(value))
    return float(match.group(1)) if match else np.nan


def profile_files() -> pd.DataFrame:
    rows = []
    for path in sorted(DATA.rglob("*")):
        if not path.is_file():
            continue
        rec = {
            "path": str(path.relative_to(ROOT)),
            "extension": path.suffix.lower(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "layer": path.relative_to(DATA).parts[0],
            "rows": np.nan,
            "columns": np.nan,
            "exact_duplicate_rows": np.nan,
            "null_cells": np.nan,
            "all_null_columns": "",
            "read_status": "not_tabular",
        }
        try:
            if path.suffix.lower() == ".csv":
                df = pd.read_csv(path)
                rec.update(
                    rows=len(df),
                    columns=len(df.columns),
                    exact_duplicate_rows=int(df.duplicated().sum()),
                    null_cells=int(df.isna().sum().sum()),
                    all_null_columns=";".join(
                        str(c) for c in df.columns if df[c].isna().all()
                    ),
                    read_status="ok",
                )
            elif path.suffix.lower() in {".xlsx", ".xls"}:
                book = pd.ExcelFile(path)
                rec.update(columns=len(book.sheet_names), read_status="workbook")
        except Exception as exc:  # preserve failure as an audit record
            rec["read_status"] = f"error:{type(exc).__name__}"
        rows.append(rec)
    return pd.DataFrame(rows)


def base_record(**kwargs) -> dict:
    defaults = dict(
        platform="",
        segment_scope="",
        period="",
        year=np.nan,
        frequency="",
        geography_scope="",
        geography_evidence="",
        transaction_measure="",
        transaction_value=np.nan,
        revenue_measure="",
        revenue_value=np.nan,
        currency="",
        unit_scale="",
        transaction_status="",
        revenue_status="",
        source_file="",
        source_locator="",
        source_url="",
        reporting_vintage="",
        period_match="",
        scope_match="",
        directness_class="",
        sample_family="",
        canonical_record=True,
        admission_status="",
        admission_reason="",
        structural_break="",
        source_dataset="",
    )
    defaults.update(kwargs)
    return defaults


def build_census() -> pd.DataFrame:
    records: list[dict] = []

    # Proposed country/Indonesia-aligned longitudinal extension.
    path = DATA / "longitudinal" / "indonesia_platform_year_extension.csv"
    df = pd.read_csv(path)
    for _, r in df.iterrows():
        is_tokopedia = str(r.platform).startswith("Tokopedia")
        is_grab = r.platform == "Grab"
        family = (
            "indonesia_aligned_direct_segment"
            if is_tokopedia
            else "conditional_indonesia_country_reconstruction"
        )
        records.append(
            base_record(
                platform=r.platform,
                segment_scope=("e-commerce segment" if is_tokopedia else "country allocation"),
                period=r.period,
                year=numeric_year(r.period),
                frequency="annual",
                geography_scope=r.geographic_scope,
                geography_evidence=(
                    "Indonesia-aligned business segment; not explicit geographic line"
                    if is_tokopedia
                    else "explicit Indonesia anchor plus non-country allocation"
                ),
                transaction_measure="GTV/GMV",
                transaction_value=r.transaction_value_native,
                revenue_measure="platform/segment revenue",
                revenue_value=r.platform_revenue_native,
                currency=str(r.unit).split("_")[0],
                unit_scale="billion" if "billion" in str(r.unit) else "million",
                transaction_status=r.transaction_value_status,
                revenue_status=r.revenue_status,
                period_match="yes",
                scope_match="conditional" if not is_tokopedia else "yes_with_segment_caveat",
                directness_class=(
                    "direct_pair_segment" if is_tokopedia else "mixed_direct_derived_pair"
                ),
                sample_family=family,
                admission_status=("candidate_core" if is_tokopedia else "conditional_case"),
                admission_reason=r.comparability_note,
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Blibli complete reported-pair source universe, preserving vintages.
    path = DATA / "longitudinal" / "blibli_reported_pairs_all_vintages.csv"
    df = pd.read_csv(path)
    key = ["period", "frequency", "scope"]
    df["_duplicate_vintage"] = df.duplicated(key, keep="last")
    for _, r in df.iterrows():
        complete = pd.notna(r.tpv) and pd.notna(r.revenue)
        q1_mapping_error = r.source_id == "blibli_q12023_linked_0"
        records.append(
            base_record(
                platform="Blibli/GDN",
                segment_scope=r.scope,
                period=r.period,
                year=numeric_year(r.period),
                frequency=r.frequency,
                geography_scope="issuer/segment scope; geography under review",
                geography_evidence="not confirmed as explicit Indonesia-only pair",
                transaction_measure="TPV",
                transaction_value=r.tpv,
                revenue_measure="net revenue",
                revenue_value=r.revenue,
                currency="IDR",
                unit_scale="billion",
                transaction_status="direct issuer disclosure" if pd.notna(r.tpv) else "missing",
                revenue_status="direct issuer disclosure" if pd.notna(r.revenue) else "missing",
                source_file=r.source_file,
                source_locator=f"page {r.source_page}" if pd.notna(r.source_page) else "",
                source_url=r.source_url,
                reporting_vintage=r.source_id,
                period_match="yes" if complete else "incomplete_pair",
                scope_match="same issuer table; definition review pending",
                directness_class="direct_pair_issuer_or_segment" if complete else "partial_source_record",
                sample_family="blibli_reported_source_universe",
                canonical_record=(not bool(r._duplicate_vintage)) and not q1_mapping_error,
                admission_status=(
                    "exclude_extraction_mapping_error"
                    if q1_mapping_error
                    else ("candidate_pending_geography_and_scope" if complete else "incomplete")
                ),
                admission_reason=(
                    "The table columns FY22, 1Q23, and 1Q22 were shifted in the legacy extraction; use the manually verified replacement extract."
                    if q1_mapping_error else r.status
                ),
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Manually verified replacement for the mis-mapped Blibli 1Q23 table.
    path = DATA / "longitudinal" / "blibli_q1_2023_corrected_extract.csv"
    df = pd.read_csv(path)
    for _, r in df.iterrows():
        is_annual_duplicate = r.frequency == "annual"
        records.append(
            base_record(
                platform=r.platform,
                segment_scope=r.scope,
                period=r.period,
                year=numeric_year(r.period),
                frequency=r.frequency,
                geography_scope="issuer/segment scope; geography under review",
                geography_evidence="not confirmed as explicit Indonesia-only pair",
                transaction_measure="TPV",
                transaction_value=r.tpv,
                revenue_measure="net revenue",
                revenue_value=r.net_revenue,
                currency="IDR",
                unit_scale="billion",
                transaction_status="direct issuer disclosure; manually remapped",
                revenue_status="direct issuer disclosure; manually remapped",
                source_file=r.source_file,
                source_locator=f"page {r.source_page}; {r.source_column}",
                source_url=r.source_url,
                reporting_vintage=r.source_id,
                period_match="yes",
                scope_match="same issuer table; definition review pending",
                directness_class="direct_pair_issuer_or_segment",
                sample_family="blibli_q1_verified_replacement",
                canonical_record=not is_annual_duplicate,
                admission_status=(
                    "lineage_duplicate_of_fy2022_release"
                    if is_annual_duplicate else "candidate_pending_geography_and_scope"
                ),
                admission_reason=r.definition_note,
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Earlier Blibli prospectus observations, including segment detail.
    path = DATA / "longitudinal" / "blibli_prospectus_2019_2020_candidates.csv"
    df = pd.read_csv(path)
    for _, r in df.iterrows():
        records.append(
            base_record(
                platform="Blibli/GDN",
                segment_scope=r.scope,
                period=f"FY{int(r.year)}",
                year=int(r.year),
                frequency="annual",
                geography_scope="issuer/segment scope; geography under review",
                geography_evidence=r.geography_note,
                transaction_measure="TPV",
                transaction_value=r.tpv_idr_million,
                revenue_measure="net revenue",
                revenue_value=r.net_revenue_idr_million,
                currency="IDR",
                unit_scale="million",
                transaction_status="direct prospectus transcription",
                revenue_status="direct prospectus transcription",
                source_file=r.source_file,
                source_locator=f"{r.tpv_locator}; {r.revenue_locator}",
                period_match="yes",
                scope_match="same segment and year",
                directness_class="direct_pair_segment_or_group",
                sample_family="blibli_prospectus_candidates",
                admission_status="candidate_pending_geography_and_scope",
                admission_reason=r.status,
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Bukalapak annual candidate pairs.
    path = DATA / "longitudinal" / "bukalapak_annual_candidates.csv"
    df = pd.read_csv(path)
    for _, r in df.iterrows():
        matched = int(r.tpv_months) == int(r.revenue_months)
        records.append(
            base_record(
                platform="Bukalapak",
                segment_scope="Group",
                period=f"FY{int(r.year)}" if matched else f"{int(r.tpv_months)}M{int(r.year)}_vs_FY{int(r.year)}",
                year=int(r.year),
                frequency="annual" if matched else "period_mismatch",
                geography_scope="Group; overseas operations disclosed",
                geography_evidence=r.geography_note,
                transaction_measure="TPV",
                transaction_value=r.tpv_idr_million,
                revenue_measure="revenue",
                revenue_value=r.revenue_idr_million,
                currency="IDR",
                unit_scale="million",
                transaction_status="direct issuer disclosure",
                revenue_status="direct issuer disclosure",
                source_file=r.source_file,
                source_locator=r.locator,
                period_match="yes" if matched else "no",
                scope_match="group pair; geography pending",
                directness_class="direct_pair_group" if matched else "invalid_period_pair",
                sample_family="bukalapak_annual_candidates",
                admission_status="candidate_pending_geography" if matched else "exclude",
                admission_reason=r.status,
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Direct company/segment historical annual ratios.
    path = DATA / "longitudinal" / "historical_within_platform_ratios.csv"
    df = pd.read_csv(path)
    for _, r in df.iterrows():
        usable = pd.notna(r.transaction_to_revenue_ratio)
        records.append(
            base_record(
                platform=r.firm,
                segment_scope=r.scope,
                period=r.period,
                year=numeric_year(r.period),
                frequency="annual",
                geography_scope="company/segment scope",
                geography_evidence="not country-specific",
                transaction_measure="GMV/GTV",
                transaction_value=r.transaction_value_usd_m,
                revenue_measure="matched platform revenue",
                revenue_value=r.platform_revenue_usd_m,
                currency="USD",
                unit_scale="million",
                transaction_status="direct company historical extract",
                revenue_status="direct company historical extract",
                period_match="yes",
                scope_match="yes within stated company/segment scope",
                directness_class="direct_pair_company_or_segment",
                sample_family="historical_company_segment",
                admission_status="supporting" if usable else "exclude_ratio_negative_denominator",
                admission_reason=r.note,
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Later annual company-wide/segment panel, keeping alternate GoTo 2024 basis.
    path = DATA / "longitudinal" / "annual_extension_panel_preliminary.csv"
    df = pd.read_csv(path)
    for i, r in df.iterrows():
        alternate = r.platform == "GoTo" and int(r.year) == 2024 and "pro-forma" in str(r.basis)
        records.append(
            base_record(
                platform=r.platform,
                segment_scope=r.basis,
                period=f"FY{int(r.year)}",
                year=int(r.year),
                frequency="annual",
                geography_scope="company/segment scope",
                geography_evidence="not country-specific",
                transaction_measure="GMV/GTV",
                transaction_value=r.gmv_or_gtv,
                revenue_measure="matched revenue",
                revenue_value=r.matched_revenue,
                currency=r.currency,
                unit_scale=r.unit,
                transaction_status="reported/reconstructed from issuer annual inputs",
                revenue_status="reported/reconstructed from issuer annual inputs",
                period_match="yes",
                scope_match="as documented; structural breaks retained",
                directness_class="company_annual_pair_reconstructed",
                sample_family="recent_company_annual",
                canonical_record=not alternate,
                admission_status="supporting_preliminary",
                admission_reason=str(r.notes) if pd.notna(r.notes) else "",
                structural_break=("Tokopedia deconsolidation" if r.platform == "GoTo" and int(r.year) >= 2024 else ""),
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    # Source-reconciled quarterly accounting observations.
    path = DATA / "quarterly" / "quarterly_panel_source_coverage.csv"
    df = pd.read_csv(path)
    for _, r in df.iterrows():
        records.append(
            base_record(
                platform=r.platform,
                segment_scope=r.panel_basis,
                period=f"{int(r.fiscal_year)}Q{int(r.quarter)}",
                year=int(r.fiscal_year),
                frequency="quarterly",
                geography_scope="company/segment scope",
                geography_evidence="not country-specific",
                transaction_measure="GMV/GTV",
                transaction_value=r.gmv_or_gtv,
                revenue_measure="matched revenue",
                revenue_value=r.matched_revenue,
                currency=r.currency,
                unit_scale=r.unit,
                transaction_status=r.gtv_gmv_source_definition,
                revenue_status=r.revenue_source_definition,
                source_file=r.archived_file,
                source_locator="reconciled source document",
                source_url=r.source_url,
                period_match="yes",
                scope_match=r.scope_comparability_flag,
                directness_class=r.panel_field_directness,
                sample_family="quarterly_company_accounting",
                admission_status="supporting_source_reconciled_inventory",
                admission_reason=r.panel_notes if pd.notna(r.panel_notes) else "",
                structural_break=("reporting/scope caveat" if pd.notna(r.panel_notes) else ""),
                source_dataset=str(path.relative_to(ROOT)),
            )
        )

    out = pd.DataFrame(records)
    out.insert(0, "record_id", [f"OBS-{i:04d}" for i in range(1, len(out) + 1)])
    out["full_pair"] = out.transaction_value.notna() & out.revenue_value.notna()
    out["positive_denominator"] = out.revenue_value > 0
    out["ratio_eligible"] = (
        out.full_pair & out.positive_denominator & out.period_match.eq("yes")
    )
    return out


def pair_metrics(census: pd.DataFrame) -> pd.DataFrame:
    x = census.loc[census.ratio_eligible & census.canonical_record].copy()
    x["transaction_to_revenue_ratio"] = x.transaction_value / x.revenue_value
    x["gap_to_revenue_ratio"] = x.transaction_to_revenue_ratio - 1
    x["monetization_rate"] = x.revenue_value / x.transaction_value
    x["transaction_revenue_gap"] = x.transaction_value - x.revenue_value
    return x[
        [
            "record_id", "platform", "segment_scope", "period", "year", "frequency",
            "geography_scope", "directness_class", "sample_family", "transaction_value",
            "revenue_value", "currency", "unit_scale", "transaction_revenue_gap",
            "monetization_rate", "transaction_to_revenue_ratio", "gap_to_revenue_ratio",
            "admission_status", "structural_break", "source_dataset",
        ]
    ]


def sample_summary(census: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for family, g in census.groupby("sample_family", dropna=False):
        canonical = g[g.canonical_record]
        eligible = canonical[canonical.ratio_eligible]
        rows.append(
            {
                "sample_family": family,
                "source_records_all_vintages": len(g),
                "canonical_records": len(canonical),
                "full_matched_pairs": int(canonical.full_pair.sum()),
                "ratio_eligible_pairs": int(canonical.ratio_eligible.sum()),
                "unique_platforms": canonical.platform.nunique(),
                "unique_platform_segment_combinations": canonical[["platform", "segment_scope"]].drop_duplicates().shape[0],
                "unique_period_labels": canonical.period.nunique(),
                "min_year": canonical.year.min(),
                "max_year": canonical.year.max(),
                "direct_pair_records": int(canonical.directness_class.str.startswith("direct_pair", na=False).sum()),
                "derived_or_conditional_records": int(canonical.directness_class.str.contains("derived|reconstructed", case=False, na=False).sum()),
                "excluded_records": int(canonical.admission_status.str.startswith("exclude", na=False).sum()),
                "interpretation": (
                    "Counts are internal to this sample family; do not add across overlapping annual, quarterly, segment, or vintage layers."
                ),
            }
        )
    return pd.DataFrame(rows).sort_values("sample_family")


def source_chain_status() -> pd.DataFrame:
    q = pd.read_csv(DATA / "quarterly" / "quarterly_panel_source_coverage.csv")
    event = pd.read_csv(DATA / "market" / "event_study_results_unfiltered_recomputed.csv")
    contamination = pd.read_csv(DATA / "quarterly" / "contamination_ledger_REVIEWED.csv")
    return pd.DataFrame(
        [
            ["FY2023 Indonesia reconstruction", 3, 3, 3, "yes", "conditional", "Grab and Shopee depend on allocation assumptions; Tokopedia is segment-labelled."],
            ["Indonesia longitudinal extension", 9, 9, 9, "yes", "candidate", "Unbalanced 2021-2024; mixed direct segment and derived country cases."],
            ["Historical direct annual platform series", 8, 8, 7, "yes", "supporting", "Grab FY2019 ratio invalid because revenue denominator is negative."],
            ["Quarterly accounting panel", len(q), int(q.archived_file.notna().sum()), len(q), "yes", "supporting", "Company/segment scope, not Indonesia-only."],
            ["Unfiltered event-study rows", len(event), int(event.car_m1_p1.notna().sum()), int(event.car_m1_p1.notna().sum()), "prices preserved", "exploratory", f"{int(contamination.guidance_contaminated_working.isin(['unknown','candidate']).sum())} contamination flags unresolved."],
            ["ASEAN World Bank context", 2860, 2860, 2617, "yes", "context_only", "Country-year-indicator slots; not platform accounting observations."],
        ],
        columns=["module", "records", "source_linked_records", "usable_numeric_records", "reproduction_status", "analytical_role", "limitation"],
    )


def quality_issues(census: pd.DataFrame, profiles: pd.DataFrame) -> pd.DataFrame:
    issues = [
        ["critical", "main-sample definition", "No expanded longitudinal sample is advisor-approved.", "Treat sample families as alternatives; do not pool them."],
        ["critical", "geography", "No verified strict direct country-level transaction/revenue pair is established for all proposed platforms.", "Separate explicit-country anchors, Indonesia-aligned segments, and company-wide records."],
        ["high", "Grab country construction", "Country transaction value is inferred with a Group monetization rate.", "Keep conditional; show rate sensitivity and avoid calling it direct."],
        ["high", "Shopee country construction", "Country GMV is external and country revenue is derived from a Group service rate.", "Keep conditional; test market-size/share/rate assumptions separately."],
        ["high", "Blibli scope", "3P includes online travel and Group geography is not confirmed Indonesia-only.", "Resolve segment and geographic eligibility before main-sample admission."],
        ["high", "Bukalapak geography", "Group disclosures include overseas activity.", "Use only with explicit issuer-scope framing or a verified Indonesia allocation."],
        ["high", "Bukalapak FY2024", "TPV covers 9 months while revenue covers 12 months.", "Exclude until a matched 9M revenue denominator is found."],
        ["high", "event study", "Contamination classifications remain unresolved for many events.", "Keep results exploratory until classifications and timing are closed."],
        ["medium", "reporting vintages", "Blibli observations repeat across releases and sometimes change slightly.", "Preserve all vintages; designate one canonical record per period/scope."],
        ["high", "Blibli Q1 extraction", "Rows labelled 2023Q1 reproduce FY2022 values in the source line and are likely mapped to the wrong comparative columns.", "Exclude the affected Q1 extraction until the issuer table is manually remapped."],
        ["resolved", "Blibli Q1 extraction", "The official 1Q23 issuer PDF was recovered and FY22/1Q23/1Q22 columns were manually remapped in a separate immutable correction extract.", "Use blibli_q1_2023_corrected_extract.csv; retain the legacy rows only as excluded lineage."],
        ["medium", "revenue definitions", "Gross, net, service, and total revenue are not interchangeable.", "Use a consistent denominator within each comparison and publish reconciliations."],
        ["medium", "structural breaks", "Grab business-model changes and Tokopedia deconsolidation alter comparability.", "Flag or segment time series around breaks; use issuer comparable-basis disclosures."],
        ["medium", "row-count interpretation", "Source rows, inputs, scenarios, annual totals, and quarters overlap.", "Report N separately by observation grain and unique economic period."],
    ]
    return pd.DataFrame(issues, columns=["severity", "area", "finding", "required_treatment"])


def candidate_designs(census: pd.DataFrame) -> pd.DataFrame:
    """Summarize defensible design options without declaring one approved."""
    rows = [
        {
            "design_id": "A",
            "design": "strict explicit-country direct annual pairs",
            "geography": "Indonesia explicitly labelled by issuer",
            "frequency": "annual",
            "eligible_pairs_now": 0,
            "platforms_now": 0,
            "period_window": "none established",
            "strength": "highest directness",
            "binding_problem": "No platform currently provides a direct Indonesia transaction-value and revenue pair.",
            "advisor_decision_needed": "Whether this strict rule is required.",
        },
        {
            "design_id": "B",
            "design": "Indonesia-aligned direct issuer/segment annual panel",
            "geography": "Indonesia-aligned operations; not always explicit country lines",
            "frequency": "annual",
            "eligible_pairs_now": 14,
            "platforms_now": 3,
            "period_window": "2019-2025 unbalanced",
            "strength": "direct reported transaction/revenue pairs",
            "binding_problem": "Blibli 3P includes online travel; Bukalapak Group includes overseas operations; Tokopedia ends at deconsolidation.",
            "advisor_decision_needed": "Whether Indonesia-aligned business scope is acceptable as main geography.",
        },
        {
            "design_id": "C",
            "design": "conditional Indonesia country reconstruction",
            "geography": "Indonesia anchors plus allocation assumptions",
            "frequency": "annual",
            "eligible_pairs_now": 9,
            "platforms_now": 3,
            "period_window": "2021-2024 unbalanced",
            "strength": "preserves original Grab/Tokopedia/Shopee comparison",
            "binding_problem": "Grab and Shopee country pairs are model-dependent; only Tokopedia is a direct segment pair.",
            "advisor_decision_needed": "Whether conditional cases belong in the core or sensitivity section.",
        },
        {
            "design_id": "D",
            "design": "company/segment quarterly accounting panel",
            "geography": "listed platforms serving Indonesia; company/segment scope",
            "frequency": "quarterly",
            "eligible_pairs_now": 47,
            "platforms_now": 3,
            "period_window": "2022Q1-2026Q1, platform-specific",
            "strength": "source-reconciled repeated accounting observations",
            "binding_problem": "Not Indonesia-only; business-model and deconsolidation breaks; repeated observations are not independent firms.",
            "advisor_decision_needed": "Whether it is supporting longitudinal evidence or a redesigned main sample.",
        },
        {
            "design_id": "E",
            "design": "official BPS Indonesia business/statistical evidence",
            "geography": "Indonesia and provinces",
            "frequency": "annual/cross-sectional",
            "eligible_pairs_now": 74,
            "platforms_now": 0,
            "period_window": "national indicators 2020-2024; province repeated cross-sections 2023-2024",
            "strength": "official survey evidence on transactions, sales channels, and financial records",
            "binding_problem": "Different unit of analysis and definitions; province associations are ecological; microdata are not yet licensed.",
            "advisor_decision_needed": "Whether this becomes an independent validation/mechanism module or a revised research design.",
        },
    ]
    return pd.DataFrame(rows)


def _weighted_corr(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> float:
    w = w / w.sum()
    mx, my = np.sum(w * x), np.sum(w * y)
    cov = np.sum(w * (x - mx) * (y - my))
    vx = np.sum(w * (x - mx) ** 2)
    vy = np.sum(w * (y - my) ** 2)
    return float(cov / np.sqrt(vx * vy))


def _weighted_slope(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> tuple[float, float]:
    w = w / w.sum()
    mx, my = np.sum(w * x), np.sum(w * y)
    slope = np.sum(w * (x - mx) * (y - my)) / np.sum(w * (x - mx) ** 2)
    return float(slope), float(my - slope * mx)


def bps_analysis() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    path = DATA / "bps_official" / "bps_ecommerce_2023_province_financial_records_sales_media.csv"
    d = pd.read_csv(path)
    context = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_2023_province_sampling_context.csv")
    d = d.merge(
        context[["province", "ecommerce_business_share_pct", "ecommerce_business_share_rse_pct", "estimated_ecommerce_businesses_2023"]],
        on="province", how="left", validate="one_to_one"
    )
    x = d[(d.province != "Indonesia") & d.financial_reports_have_pct.notna()].copy()
    rows = []
    for variable in [
        "marketplace_sales_media_pct",
        "instant_messaging_sales_media_pct",
        "social_media_sales_media_pct",
        "website_sales_media_pct",
        "email_sales_media_pct",
    ]:
        z = x[["financial_reports_have_pct", variable]].dropna()
        pearson = stats.pearsonr(z[variable], z.financial_reports_have_pct)
        spearman = stats.spearmanr(z[variable], z.financial_reports_have_pct)
        slope, intercept, r, p, se = stats.linregress(z[variable], z.financial_reports_have_pct)
        rows.append(
            {
                "sales_media_variable": variable,
                "province_N": len(z),
                "pearson_r": pearson.statistic,
                "pearson_p": pearson.pvalue,
                "spearman_rho": spearman.statistic,
                "spearman_p": spearman.pvalue,
                "ols_slope_percentage_points": slope,
                "ols_intercept": intercept,
                "ols_slope_se": se,
                "weighted_by_business_share_r": _weighted_corr(
                    z[variable].to_numpy(), z.financial_reports_have_pct.to_numpy(),
                    x.loc[z.index, "ecommerce_business_share_pct"].to_numpy()
                ),
                "weighted_by_business_share_slope": _weighted_slope(
                    z[variable].to_numpy(), z.financial_reports_have_pct.to_numpy(),
                    x.loc[z.index, "ecommerce_business_share_pct"].to_numpy()
                )[0],
                "interpretation": "Ecological descriptive association; no causal or business-level inference.",
            }
        )

    # Robustness for the focal marketplace association: RSE screen and leave-one-out.
    robustness = []
    for label, z in {
        "all_reported_provinces": x,
        "business_share_rse_le_10pct": x[x.ecommerce_business_share_rse_pct <= 10],
        "exclude_papua_outcome_outlier": x[x.province != "Papua"],
        "java_only": x[x.province.isin(["DKI Jakarta", "Jawa Barat", "Jawa Tengah", "D.I. Yogyakarta", "Jawa Timur", "Banten"])],
    }.items():
        pearson = stats.pearsonr(z.marketplace_sales_media_pct, z.financial_reports_have_pct)
        spearman = stats.spearmanr(z.marketplace_sales_media_pct, z.financial_reports_have_pct)
        wslope, wintercept = _weighted_slope(
            z.marketplace_sales_media_pct.to_numpy(), z.financial_reports_have_pct.to_numpy(),
            z.ecommerce_business_share_pct.to_numpy()
        )
        robustness.append({
            "specification": label,
            "province_N": len(z),
            "covered_business_share_pct": z.ecommerce_business_share_pct.sum(),
            "pearson_r": pearson.statistic,
            "pearson_p": pearson.pvalue,
            "spearman_rho": spearman.statistic,
            "spearman_p": spearman.pvalue,
            "business_share_weighted_r": _weighted_corr(
                z.marketplace_sales_media_pct.to_numpy(), z.financial_reports_have_pct.to_numpy(),
                z.ecommerce_business_share_pct.to_numpy()
            ),
            "business_share_weighted_slope": wslope,
            "business_share_weighted_intercept": wintercept,
            "interpretation": "Descriptive province-level robustness only; survey microdata are required for business-level inference.",
        })

    loo = []
    for province in x.province:
        z = x[x.province != province]
        pearson = stats.pearsonr(z.marketplace_sales_media_pct, z.financial_reports_have_pct)
        loo.append({
            "omitted_province": province,
            "province_N": len(z),
            "pearson_r": pearson.statistic,
            "pearson_p": pearson.pvalue,
            "weighted_r": _weighted_corr(
                z.marketplace_sales_media_pct.to_numpy(), z.financial_reports_have_pct.to_numpy(),
                z.ecommerce_business_share_pct.to_numpy()
            ),
        })
    return d, pd.DataFrame(rows), pd.concat(
        [pd.DataFrame(robustness), pd.DataFrame(loo).assign(specification="leave_one_out")],
        ignore_index=True, sort=False
    )


def bps_multiyear_analysis(bps_2023: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Keep BPS province-years distinct from issuer observations and test year-to-year patterns."""
    a = bps_2023.copy()
    a["estimated_ecommerce_businesses"] = a["estimated_ecommerce_businesses_2023"]
    a["ecommerce_business_count_rse_pct"] = a["ecommerce_business_share_rse_pct"]
    b = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_2024_province_financial_records_sales_media.csv")
    cols = [
        "province", "financial_reports_have_pct", "financial_reports_not_have_pct",
        "website_sales_media_pct", "email_sales_media_pct",
        "instant_messaging_sales_media_pct", "social_media_sales_media_pct",
        "marketplace_sales_media_pct", "estimated_ecommerce_businesses",
        "ecommerce_business_count_rse_pct", "year", "source_status",
        "source_locator", "definition_note",
    ]
    panel = pd.concat([a[cols], b[cols]], ignore_index=True)

    annual = []
    for year, g in panel[panel.province != "Indonesia"].groupby("year"):
        z = g.dropna(subset=["financial_reports_have_pct", "marketplace_sales_media_pct", "estimated_ecommerce_businesses"])
        pearson = stats.pearsonr(z.marketplace_sales_media_pct, z.financial_reports_have_pct)
        spearman = stats.spearmanr(z.marketplace_sales_media_pct, z.financial_reports_have_pct)
        annual.append({
            "year": int(year), "province_N": len(z),
            "pearson_r": pearson.statistic, "pearson_p": pearson.pvalue,
            "spearman_rho": spearman.statistic, "spearman_p": spearman.pvalue,
            "business_count_weighted_r": _weighted_corr(
                z.marketplace_sales_media_pct.to_numpy(), z.financial_reports_have_pct.to_numpy(),
                z.estimated_ecommerce_businesses.to_numpy()
            ),
            "interpretation": "Province-level descriptive association; not causal or business-level.",
        })

    w = panel[panel.province != "Indonesia"].pivot(
        index="province", columns="year",
        values=["financial_reports_have_pct", "marketplace_sales_media_pct", "estimated_ecommerce_businesses"]
    ).dropna()
    changes = pd.DataFrame({
        "province": w.index,
        "change_financial_reports_pp": w[("financial_reports_have_pct", 2024)] - w[("financial_reports_have_pct", 2023)],
        "change_marketplace_use_pp": w[("marketplace_sales_media_pct", 2024)] - w[("marketplace_sales_media_pct", 2023)],
        "average_estimated_businesses": (w[("estimated_ecommerce_businesses", 2024)] + w[("estimated_ecommerce_businesses", 2023)]) / 2,
    }).reset_index(drop=True)
    pearson = stats.pearsonr(changes.change_marketplace_use_pp, changes.change_financial_reports_pp)
    spearman = stats.spearmanr(changes.change_marketplace_use_pp, changes.change_financial_reports_pp)
    changes["overall_change_pearson_r"] = pearson.statistic
    changes["overall_change_pearson_p"] = pearson.pvalue
    changes["overall_change_spearman_rho"] = spearman.statistic
    changes["overall_change_spearman_p"] = spearman.pvalue
    changes["overall_change_weighted_r"] = _weighted_corr(
        changes.change_marketplace_use_pp.to_numpy(), changes.change_financial_reports_pp.to_numpy(),
        changes.average_estimated_businesses.to_numpy()
    )
    return panel, pd.DataFrame(annual), changes


def disclosure_matrix(census: pd.DataFrame) -> pd.DataFrame:
    g = census[census.canonical_record].copy()
    g["direct_pair"] = g.directness_class.str.startswith("direct_pair", na=False)
    g["conditional_or_derived"] = g.directness_class.str.contains("derived|reconstructed", case=False, na=False)
    g["explicit_country_scope"] = g.geography_scope.eq("Indonesia")
    return (
        g.groupby(["platform", "sample_family"], dropna=False)
        .agg(
            records=("record_id", "size"),
            full_pairs=("full_pair", "sum"),
            ratio_eligible=("ratio_eligible", "sum"),
            direct_pairs=("direct_pair", "sum"),
            conditional_or_derived=("conditional_or_derived", "sum"),
            explicit_country_records=("explicit_country_scope", "sum"),
            first_year=("year", "min"),
            last_year=("year", "max"),
        )
        .reset_index()
    )


def quarterly_summary() -> pd.DataFrame:
    q = pd.read_csv(DATA / "quarterly" / "clean_event_panel_accounting.csv")
    cov = pd.read_csv(DATA / "quarterly" / "quarterly_panel_source_coverage.csv")
    rows = []
    for platform, g in q.groupby("platform"):
        c = cov[cov.platform == platform]
        rows.append(
            {
                "platform": platform,
                "quarters": len(g),
                "first_period": f"{int(g.fiscal_year.min())}Q{int(g.loc[g.fiscal_year.idxmin(),'quarter'])}",
                "last_year": int(g.fiscal_year.max()),
                "median_ecosystem_ratio": g.ecosystem_ratio.median(),
                "mean_ecosystem_ratio": g.ecosystem_ratio.mean(),
                "archived_source_links": int(c.archived_file.notna().sum()),
                "reextracted_rows": int(c.numeric_fields_reextracted_from_raw_source.astype(str).str.startswith("YES").sum()),
                "geographic_scope": "company/segment; not Indonesia-only",
            }
        )
    return pd.DataFrame(rows)


def market_summary() -> pd.DataFrame:
    p = pd.read_csv(DATA / "market" / "platform_market_daily_2010_2026.csv")
    p["date_utc"] = pd.to_datetime(p.date_utc, errors="coerce")
    rows = []
    for symbol, g in p.groupby("symbol"):
        rows.append(
            {
                "symbol": symbol,
                "rows": len(g),
                "nonmissing_adjusted_close": int(g.adjusted_close.notna().sum()),
                "first_date": g.date_utc.min().date(),
                "last_date": g.date_utc.max().date(),
                "currency_values": ";".join(sorted(g.currency.dropna().astype(str).unique())),
                "source_files": g.source_file.nunique(),
            }
        )
    return pd.DataFrame(rows)


def make_charts(summary: pd.DataFrame, metrics: pd.DataFrame, qsum: pd.DataFrame, bps: pd.DataFrame) -> None:
    plt.rcParams.update({"font.size": 10, "axes.titlesize": 12, "axes.labelsize": 10})
    blue, orange, grey = "#2563EB", "#D97706", "#6B7280"

    # Chart 1: honest counts by non-combinable evidence family.
    s = summary.sort_values("ratio_eligible_pairs")
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.barh(s.sample_family, s.ratio_eligible_pairs, color=blue, edgecolor="#1F2937", linewidth=.6)
    ax.set_title("Ratio-eligible records by evidence family")
    ax.set_xlabel("Records (not additive across overlapping families)")
    ax.grid(axis="x", color="#E5E7EB", linewidth=.7)
    ax.set_axisbelow(True)
    for i, v in enumerate(s.ratio_eligible_pairs):
        ax.text(v + max(s.ratio_eligible_pairs.max() * .01, .2), i, str(int(v)), va="center")
    fig.tight_layout()
    fig.savefig(CHARTS / "sample_family_eligible_counts.png", dpi=180)
    plt.close(fig)

    # Chart 2: quarterly ratios as small multiples (enough temporal observations).
    q = metrics[metrics.sample_family.eq("quarterly_company_accounting")].copy()
    platforms = list(q.platform.drop_duplicates())
    fig, axes = plt.subplots(len(platforms), 1, figsize=(10, 7.5), sharex=False)
    if len(platforms) == 1:
        axes = [axes]
    for ax, platform in zip(axes, platforms):
        g = q[q.platform.eq(platform)].sort_values(["year", "period"])
        ax.plot(g.period, g.gap_to_revenue_ratio, color=blue, marker="o", markersize=3, linewidth=1.5)
        ax.set_title(platform, loc="left")
        ax.set_ylabel("(TV−R)/R")
        ax.grid(axis="y", color="#E5E7EB", linewidth=.7)
        ax.tick_params(axis="x", rotation=45)
    fig.suptitle("Company/segment quarterly transaction–revenue ratios", y=.995)
    fig.text(.5, .005, "Company/segment scope; panels are not Indonesia-only and are not pooled.", ha="center", color=grey)
    fig.tight_layout(rect=[0, .025, 1, .98])
    fig.savefig(CHARTS / "quarterly_ratio_small_multiples.png", dpi=180)
    plt.close(fig)

    # Chart 3: source-reconciled quarterly coverage.
    x = qsum.sort_values("quarters")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ypos = np.arange(len(x))
    ax.barh(ypos, x.quarters, color=orange, edgecolor="#1F2937", linewidth=.6)
    ax.set_yticks(ypos, x.platform)
    ax.set_xlabel("Quarterly accounting observations")
    ax.set_title("Quarterly accounting panel coverage")
    ax.grid(axis="x", color="#E5E7EB", linewidth=.7)
    ax.set_axisbelow(True)
    for i, v in enumerate(x.quarters):
        ax.text(v + .2, i, str(int(v)), va="center")
    fig.tight_layout()
    fig.savefig(CHARTS / "quarterly_platform_coverage.png", dpi=180)
    plt.close(fig)

    # Chart 4: province-level official-statistics association (descriptive only).
    x = bps[(bps.province != "Indonesia") & bps.financial_reports_have_pct.notna()].copy()
    fig, ax = plt.subplots(figsize=(8, 5.5))
    sizes = 25 + 650 * x.ecommerce_business_share_pct / x.ecommerce_business_share_pct.max()
    ax.scatter(x.marketplace_sales_media_pct, x.financial_reports_have_pct,
               s=sizes, color=blue, edgecolor="#1F2937", linewidth=.5, alpha=.78)
    slope, intercept, r, p, _ = stats.linregress(
        x.marketplace_sales_media_pct, x.financial_reports_have_pct
    )
    xx = np.linspace(x.marketplace_sales_media_pct.min(), x.marketplace_sales_media_pct.max(), 100)
    ax.plot(xx, intercept + slope * xx, color=orange, linewidth=1.8)
    for _, row in x.nlargest(3, "financial_reports_have_pct").iterrows():
        ax.annotate(row.province, (row.marketplace_sales_media_pct, row.financial_reports_have_pct),
                    xytext=(4, 4), textcoords="offset points", fontsize=8)
    ax.set_title("Marketplace use and financial-report ownership by province")
    ax.set_xlabel("E-commerce businesses using marketplaces (%)")
    ax.set_ylabel("E-commerce businesses with financial reports (%)")
    ax.grid(color="#E5E7EB", linewidth=.7)
    ax.set_axisbelow(True)
    ax.text(.02, .98, f"N={len(x)} provinces; Pearson r={r:.2f}, p={p:.3f}",
            transform=ax.transAxes, va="top", color=grey)
    fig.text(.5, .01, "BPS 2023 province estimates. Bubble area scales with estimated business share; ecological, not causal.",
             ha="center", color=grey, fontsize=8)
    fig.tight_layout(rect=[0, .035, 1, 1])
    fig.savefig(CHARTS / "bps_province_marketplace_financial_reports.png", dpi=180)
    plt.close(fig)

    # Chart 5: official national indicators through 2024 (distinct scales, indexed growth).
    national = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_national_indicators_2020_2023.csv")
    tv = national[national.indicator.eq("ecommerce_transaction_value")].sort_values("reference_year")
    businesses = national[national.indicator.eq("estimated_number_of_ecommerce_businesses")].sort_values("reference_year")
    reports = national[national.indicator.eq("ecommerce_businesses_with_financial_reports")].sort_values("reference_year")
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, d, title, ylabel in [
        (axes[0], tv, "E-commerce transaction value", "IDR trillion"),
        (axes[1], businesses, "Estimated e-commerce businesses", "Businesses"),
        (axes[2], reports, "Businesses with financial reports", "%"),
    ]:
        ax.plot(d.reference_year, d.value, marker="o", color=blue, linewidth=1.8)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.grid(color="#E5E7EB", linewidth=.7)
        ax.tick_params(axis="x", rotation=45)
    fig.suptitle("BPS official Indonesia e-commerce indicators (available years)")
    fig.tight_layout()
    fig.savefig(CHARTS / "bps_national_indicator_trends.png", dpi=180)
    plt.close(fig)

    # Chart 6: repeated province cross-sections, shown separately by year.
    b24 = pd.read_csv(DATA / "bps_official" / "bps_ecommerce_2024_province_financial_records_sales_media.csv")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True, sharey=True)
    for ax, d, year in [(axes[0], bps, 2023), (axes[1], b24, 2024)]:
        z = d[(d.province != "Indonesia") & d.financial_reports_have_pct.notna()].copy()
        ax.scatter(z.marketplace_sales_media_pct, z.financial_reports_have_pct,
                   color=blue, edgecolor="#1F2937", linewidth=.4, alpha=.75)
        slope, intercept, r, p, _ = stats.linregress(
            z.marketplace_sales_media_pct, z.financial_reports_have_pct
        )
        xx = np.linspace(z.marketplace_sales_media_pct.min(), z.marketplace_sales_media_pct.max(), 100)
        ax.plot(xx, intercept + slope * xx, color=orange, linewidth=1.6)
        ax.set_title(f"{year}: r={r:.2f}, p={p:.3f}")
        ax.set_xlabel("Businesses using marketplaces (%)")
        ax.grid(color="#E5E7EB", linewidth=.7)
    axes[0].set_ylabel("Businesses with financial reports (%)")
    fig.suptitle("Marketplace use and financial-report ownership: BPS province cross-sections")
    fig.text(.5, .01, "Separate annual estimates; descriptive ecological relationships, not a business panel or causal test.",
             ha="center", color=grey, fontsize=8)
    fig.tight_layout(rect=[0, .035, 1, 1])
    fig.savefig(CHARTS / "bps_province_association_by_year.png", dpi=180)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    CHARTS.mkdir(parents=True, exist_ok=True)

    profiles = profile_files()
    census = build_census()
    metrics = pair_metrics(census)
    summary = sample_summary(census)
    chain = source_chain_status()
    issues = quality_issues(census, profiles)
    matrix = disclosure_matrix(census)
    qsum = quarterly_summary()
    msum = market_summary()
    designs = candidate_designs(census)
    bps, bps_assoc, bps_robust = bps_analysis()
    bps_panel, bps_year_assoc, bps_changes = bps_multiyear_analysis(bps)

    write_csv(profiles, "file_profile.csv")
    write_csv(census, "candidate_observation_census.csv")
    write_csv(metrics, "longitudinal_pair_metrics.csv")
    write_csv(summary, "sample_definition_summary.csv")
    write_csv(chain, "source_chain_status.csv")
    write_csv(issues, "data_quality_issues.csv")
    write_csv(matrix, "disclosure_matrix.csv")
    write_csv(qsum, "quarterly_panel_summary.csv")
    write_csv(msum, "market_data_summary.csv")
    write_csv(designs, "candidate_research_designs.csv")
    write_csv(bps_assoc, "bps_province_associations.csv")
    write_csv(bps, "bps_province_merged_analysis.csv")
    write_csv(bps_robust, "bps_marketplace_financial_reports_robustness.csv")
    write_csv(bps_panel, "bps_province_panel_2023_2024.csv")
    write_csv(bps_year_assoc, "bps_province_associations_by_year.csv")
    write_csv(bps_changes, "bps_within_province_changes_2023_2024.csv")
    make_charts(summary, metrics, qsum, bps)

    findings = {
        "generated_on": "2026-09-09",
        "source_files_profiled": int(len(profiles)),
        "csv_files_profiled": int((profiles.extension == ".csv").sum()),
        "source_layer_csv_rows": int(profiles.loc[profiles.extension == ".csv", "rows"].sum()),
        "census_source_records": int(len(census)),
        "census_canonical_records": int(census.canonical_record.sum()),
        "census_ratio_eligible_records": int((census.canonical_record & census.ratio_eligible).sum()),
        "indonesia_extension_records": int((census.sample_family.str.contains("indonesia", case=False)).sum()),
        "quarterly_accounting_records": int((census.sample_family == "quarterly_company_accounting").sum()),
        "strict_explicit_country_direct_pairs": 0,
        "candidate_indonesia_aligned_direct_annual_pairs": 14,
        "bps_provinces_with_complete_pair": int(((bps.province != "Indonesia") & bps.financial_reports_have_pct.notna()).sum()),
        "bps_complete_province_years_2023_2024": int(
            bps_panel[(bps_panel.province != "Indonesia") & bps_panel.financial_reports_have_pct.notna()].shape[0]
        ),
        "interpretation": "Counts belong to different, overlapping evidence families and must not be summed into one sample N.",
    }
    (OUT / "findings_summary.json").write_text(json.dumps(findings, indent=2), encoding="utf-8")
    print(json.dumps(findings, indent=2))


if __name__ == "__main__":
    main()
