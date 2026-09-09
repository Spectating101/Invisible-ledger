#!/usr/bin/env python3
"""Build the ASEAN corroboration datasets from reviewed e-Conomy SEA charts.

The source rows below are manual transcriptions from the country charts in the
archived e-Conomy SEA reports.  They deliberately preserve overlapping report
vintages: a later report's estimate for an earlier year does not overwrite the
earlier publication.  The canonical view selects the latest available vintage
for each country-year, while retaining every source observation for audit.

This is supporting evidence.  It does not pool countries into a common tax
sample, infer tax non-compliance, or convert GMV into value added.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "asean_corroboration"
FIGURES = ROOT / "reports" / "figures"
WB_PATH = ROOT / "data" / "asean_context" / "asean_worldbank_context_2000_2025.csv"
MOMENTUM_PATH = ROOT / "data" / "asean_context" / "momentum_2025_country_market_estimates.csv"

COUNTRIES = ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Vietnam"]
ISO3 = {
    "Indonesia": "IDN",
    "Malaysia": "MYS",
    "Philippines": "PHL",
    "Singapore": "SGP",
    "Thailand": "THA",
    "Vietnam": "VNM",
}

# report_vintage -> country -> observation_year ->
# (overall digital GMV, ecommerce GMV, transport-and-food GMV,
#  online-travel GMV, online-media GMV)
# Units: current USD billions as displayed. Tildes in chart headings are retained
# through the source_precision field rather than converted into false precision.
TRANSCRIPTIONS = {
    2021: {
        "Indonesia": {2019: (40, 21, 5.7, 10.1, 3.5), 2020: (47, 35, 5.1, 2.6, 4.3), 2021: (70, 53, 6.9, 3.4, 6.4)},
        "Malaysia": {2019: (11, 3, 0.9, 4.7, 1.8), 2020: (14, 8, 1.4, 2.2, 2.1), 2021: (21, 14, 1.8, 2.2, 2.4)},
        "Philippines": {2019: (7, 3, 0.8, 2.0, 1.7), 2020: (9, 5, 1.0, 0.5, 2.1), 2021: (17, 12, 1.4, 0.7, 2.8)},
        "Singapore": {2019: (13, 1.9, 2.9, 6.2, 1.5), 2020: (11, 4.9, 2.5, 1.8, 1.6), 2021: (15, 7.1, 3.4, 2.3, 1.9)},
        "Thailand": {2019: (16, 5, 1.3, 7.2, 3.0), 2020: (20, 12, 1.5, 2.6, 3.4), 2021: (30, 21, 2.0, 2.8, 4.5)},
        "Vietnam": {2019: (12, 5, 1.1, 4.0, 2.8), 2020: (16, 8, 1.8, 2.5, 3.0), 2021: (21, 13, 2.4, 1.4, 3.9)},
    },
    2022: {
        "Indonesia": {2019: (41, 25, 6, 7, 3), 2021: (63, 48, 7, 2, 6.1), 2022: (77, 59, 8, 3, 6.4)},
        "Malaysia": {2019: (12, 3, 1, 5, 2), 2021: (18, 13, 2, 1, 2.6), 2022: (21, 14, 2.5, 2, 2.8)},
        "Philippines": {2019: (8, 3, 1, 2, 2), 2021: (16, 12, 1.5, 0.4, 2.6), 2022: (20, 14, 1.9, 1, 3.1)},
        "Singapore": {2019: (12, 2, 3, 6, 1.6), 2021: (15, 8, 3.2, 2, 2.1), 2022: (18, 8.2, 3.9, 4, 2.3)},
        "Thailand": {2019: (16, 5, 1, 7, 3), 2021: (30, 21, 2.7, 2, 4.6), 2022: (35, 22, 3, 5, 5.1)},
        "Vietnam": {2019: (13, 5, 1, 5, 3), 2021: (18, 11, 2, 1, 4), 2022: (23, 14, 3, 2, 4.3)},
    },
    2023: {
        "Indonesia": {2021: (63, 48, 7, 2, 6), 2022: (76, 58, 8, 3, 6), 2023: (82, 62, 7, 6, 7)},
        "Malaysia": {2021: (19, 13, 2, 1, 3), 2022: (22, 13, 3, 3, 3), 2023: (23, 13, 3, 4, 3)},
        "Philippines": {2021: (17, 12, 2, 0.5, 3), 2022: (22, 15, 2, 1, 3), 2023: (24, 16, 2, 3, 3)},
        "Singapore": {2021: (15, 8, 3, 2, 2), 2022: (20, 8, 4, 5, 2), 2023: (22, 8, 5, 7, 3)},
        "Thailand": {2021: (30, 21, 3, 2, 5), 2022: (31, 20, 3, 3, 5), 2023: (36, 22, 3, 5, 5)},
        "Vietnam": {2021: (18, 11, 2, 1, 4), 2022: (25, 15, 3, 3, 5), 2023: (30, 16, 3, 5, 5)},
    },
    2024: {
        "Indonesia": {2022: (76, 58, 8, 3, 6), 2023: (80, 59, 7, 7, 7), 2024: (90, 65, 9, 9, 8)},
        "Malaysia": {2022: (22, 13, 3, 3, 3), 2023: (26, 13, 3, 6, 3), 2024: (31, 16, 4, 8, 4)},
        "Philippines": {2022: (22, 15, 2, 1, 3), 2023: (26, 17, 3, 3, 4), 2024: (31, 21, 3, 3, 4)},
        "Singapore": {2022: (20, 8, 4, 5, 3), 2023: (26, 8, 5, 10, 3), 2024: (29, 9, 5, 12, 3)},
        "Thailand": {2022: (31, 20, 3, 3, 5), 2023: (39, 22, 4, 8, 6), 2024: (46, 26, 4, 10, 6)},
        "Vietnam": {2022: (25, 15, 3, 3, 5), 2023: (31, 19, 3, 4, 5), 2024: (36, 22, 4, 5, 6)},
    },
    2025: {
        "Indonesia": {2023: (80, 59, 8, 7, 7), 2024: (87, 62, 9, 8, 8), 2025: (99, 71, 10, 9, 9)},
        "Malaysia": {2023: (26, 13, 3, 6, 3), 2024: (33, 17, 4, 9, 3), 2025: (39, 20, 4, 10, 4)},
        "Philippines": {2023: (26, 17, 2, 3, 3), 2024: (31, 20, 3, 4, 4), 2025: (36, 24, 4, 4, 5)},
        "Singapore": {2023: (25, 8, 5, 10, 3), 2024: (27, 8, 5, 11, 3), 2025: (29, 9, 6, 11, 3)},
        "Thailand": {2023: (38, 22, 3, 8, 6), 2024: (49, 27, 4, 11, 6), 2025: (56, 33, 5, 11, 7)},
        "Vietnam": {2023: (30, 19, 3, 3, 5), 2024: (34, 21, 4, 3, 5), 2025: (39, 25, 5, 4, 6)},
    },
}

PAGES = {2021: {"Indonesia": 97, "Malaysia": 103, "Philippines": 109,
                "Singapore": 115, "Thailand": 121, "Vietnam": 127},
         2022: {"Indonesia": 92, "Malaysia": 98, "Philippines": 104,
                "Singapore": 110, "Thailand": 116, "Vietnam": 122},
         2023: {country: 3 for country in COUNTRIES},
         2024: {country: 4 for country in COUNTRIES},
         2025: {country: 3 for country in COUNTRIES}}


def source_file(vintage: int, country: str) -> str:
    if vintage <= 2022:
        return f"sources/asean_economy_reports/economy_sea_{vintage}_regional.pdf"
    return f"sources/asean_economy_reports/economy_sea_{vintage}_{country.lower()}.pdf"


def source_url(vintage: int, country: str) -> str:
    if vintage in (2021, 2022):
        return f"https://services.google.com/fh/files/misc/e_conomy_sea_{vintage}_report.pdf"
    return (
        "https://services.google.com/fh/files/misc/"
        f"{country.lower()}_e_conomy_sea_{vintage}_report.pdf"
    )


def build_source_rows() -> pd.DataFrame:
    rows = []
    for vintage, countries in TRANSCRIPTIONS.items():
        for country, years in countries.items():
            for year, values in years.items():
                for metric, value in zip((
                    "overall_digital_economy_gmv", "ecommerce_gmv",
                    "transport_and_food_gmv", "online_travel_gmv", "online_media_gmv",
                ), values):
                    rows.append({
                        "report_vintage": vintage,
                        "country": country,
                        "iso3": ISO3[country],
                        "observation_year": year,
                        "metric": metric,
                        "value_usd_billion": value,
                        "unit": "current USD billion",
                        "evidence_class": "external_market_estimate",
                        "source_precision": "rounded chart value",
                        "source_file": source_file(vintage, country),
                        "source_url": source_url(vintage, country),
                        "source_locator": f"PDF page {PAGES[vintage][country]}, country GMV chart",
                        "source_method": "Bain analysis",
                        "scope_note": "Country digital-economy estimate; not national accounts, tax base, or issuer disclosure",
                    })
    return pd.DataFrame(rows).sort_values(
        ["country", "observation_year", "metric", "report_vintage"]
    )


def latest_vintage_panel(source: pd.DataFrame) -> pd.DataFrame:
    latest = (
        source.sort_values("report_vintage")
        .groupby(["country", "iso3", "observation_year", "metric"], as_index=False)
        .tail(1)
    )
    wide = latest.pivot(
        index=["country", "iso3", "observation_year", "report_vintage"],
        columns="metric",
        values="value_usd_billion",
    ).reset_index()
    wide.columns.name = None
    wide["ecommerce_share_of_digital_pct"] = (
        100 * wide["ecommerce_gmv"] / wide["overall_digital_economy_gmv"]
    )
    wide["reported_component_sum_usd_billion"] = wide[[
        "ecommerce_gmv", "transport_and_food_gmv", "online_travel_gmv", "online_media_gmv"
    ]].sum(axis=1)
    wide["component_rounding_residual_usd_billion"] = (
        wide["overall_digital_economy_gmv"] - wide["reported_component_sum_usd_billion"]
    )
    wide["selection_rule"] = "latest available publication vintage for the country-year"
    wide["analytical_role"] = "ASEAN corroboration; country retained as separate unit"
    return wide.sort_values(["country", "observation_year"])


def add_world_bank_context(panel: pd.DataFrame) -> pd.DataFrame:
    wb = pd.read_csv(WB_PATH)
    indicators = {
        "NY.GDP.MKTP.CD": "gdp_current_usd",
        "SP.POP.TOTL": "population",
        "NE.CON.PRVT.CD": "household_consumption_current_usd",
        "IT.NET.USER.ZS": "internet_users_pct",
    }
    keep = wb[wb["indicator"].isin(indicators)].copy()
    keep["field"] = keep["indicator"].map(indicators)
    context = keep.pivot_table(index=["iso3", "year"], columns="field", values="value", aggfunc="first").reset_index()
    context.columns.name = None
    merged = panel.merge(
        context,
        left_on=["iso3", "observation_year"],
        right_on=["iso3", "year"],
        how="left",
    ).drop(columns=["year"])
    merged["ecommerce_gmv_pct_of_gdp"] = 100 * merged["ecommerce_gmv"] * 1e9 / merged["gdp_current_usd"]
    merged["ecommerce_gmv_pct_of_household_consumption"] = (
        100 * merged["ecommerce_gmv"] * 1e9 / merged["household_consumption_current_usd"]
    )
    merged["ecommerce_gmv_per_capita_usd"] = merged["ecommerce_gmv"] * 1e9 / merged["population"]
    merged["ratio_warning"] = "GMV intensity only; not value added, GDP contribution, income, or tax base"
    return merged


def revision_diagnostics(source: pd.DataFrame) -> pd.DataFrame:
    grouped = source.groupby(["country", "observation_year", "metric"])
    out = grouped["value_usd_billion"].agg(
        publication_vintages="count", earliest_value="first", latest_value="last", min_value="min", max_value="max"
    ).reset_index()
    vintages = grouped["report_vintage"].agg(
        earliest_vintage="min", latest_vintage="max"
    ).reset_index()
    out = out.merge(vintages, on=["country", "observation_year", "metric"])
    out["latest_minus_earliest_usd_billion"] = out["latest_value"] - out["earliest_value"]
    out["latest_minus_earliest_pct"] = 100 * (
        out["latest_value"] / out["earliest_value"] - 1
    )
    out["revision_interpretation"] = "publication-vintage change; not economic growth"
    return out.sort_values(["country", "observation_year", "metric"])


def growth_summary(panel: pd.DataFrame) -> pd.DataFrame:
    base = panel[panel["observation_year"].isin([2023, 2025])].copy()
    values = base.pivot(index="country", columns="observation_year", values=["ecommerce_gmv", "overall_digital_economy_gmv"])
    rows = []
    for country in COUNTRIES:
        ec23, ec25 = values.loc[country, ("ecommerce_gmv", 2023)], values.loc[country, ("ecommerce_gmv", 2025)]
        de23, de25 = values.loc[country, ("overall_digital_economy_gmv", 2023)], values.loc[country, ("overall_digital_economy_gmv", 2025)]
        rows.append({
            "country": country,
            "ecommerce_gmv_2023_usd_billion": ec23,
            "ecommerce_gmv_2025_usd_billion": ec25,
            "ecommerce_growth_2023_2025_pct": 100 * (ec25 / ec23 - 1),
            "digital_economy_gmv_2023_usd_billion": de23,
            "digital_economy_gmv_2025_usd_billion": de25,
            "digital_economy_growth_2023_2025_pct": 100 * (de25 / de23 - 1),
            "claim_scope": "within-country descriptive change using latest-vintage estimates",
        })
    return pd.DataFrame(rows)


def platform_structure() -> pd.DataFrame:
    data = pd.read_csv(MOMENTUM_PATH)
    share_cols = [
        "shopee_share_pct", "tiktok_including_tokopedia_share_pct", "lazada_share_pct",
        "blibli_share_pct", "amazon_share_pct",
    ]
    names = {
        "shopee_share_pct": "Shopee",
        "tiktok_including_tokopedia_share_pct": "TikTok/Tokopedia",
        "lazada_share_pct": "Lazada",
        "blibli_share_pct": "Blibli",
        "amazon_share_pct": "Amazon",
    }
    rows = []
    for _, row in data.iterrows():
        shares = {names[c]: float(row[c]) for c in share_cols if pd.notna(row[c])}
        top_name, top_share = max(shares.items(), key=lambda item: item[1])
        rows.append({
            "country": row["country"],
            "year": int(row["year"]),
            "market_gmv_usd_billion": row["market_gmv_usd_billion"],
            "top_reported_platform": top_name,
            "top_reported_platform_share_pct": top_share,
            "reported_share_sum_pct": sum(shares.values()),
            "reported_platform_hhi": sum(v * v for v in shares.values()),
            "hhi_scope_warning": "HHI uses reported named shares only; rounding and omitted sub-1% categories remain",
            "source_file": "sources/asean_market_sources/momentum_public_materials/momentum_2026_press_release.pdf",
            "source_url": "https://thelowdown.momentum.asia/wp-content/uploads/2026/04/Embargoed-Press-release-Momentum-Works-Ecommerce-in-SEA-2026.pdf",
            "source_locator": "PDF page 5, embedded report slide 13",
            "evidence_class": row["status"],
            "definition_note": row["definition_note"],
        })
    return pd.DataFrame(rows)


def cross_source_2025(panel: pd.DataFrame, structure: pd.DataFrame) -> pd.DataFrame:
    economy = panel[panel["observation_year"] == 2025][["country", "ecommerce_gmv"]].copy()
    economy = economy.rename(columns={"ecommerce_gmv": "economy_sea_ecommerce_gmv_usd_billion"})
    momentum = structure[["country", "market_gmv_usd_billion"]].rename(
        columns={"market_gmv_usd_billion": "momentum_platform_market_gmv_usd_billion"}
    )
    out = economy.merge(momentum, on="country", how="inner")
    out["economy_sea_minus_momentum_usd_billion"] = (
        out["economy_sea_ecommerce_gmv_usd_billion"] - out["momentum_platform_market_gmv_usd_billion"]
    )
    out["economy_sea_minus_momentum_pct_of_momentum"] = 100 * (
        out["economy_sea_ecommerce_gmv_usd_billion"] / out["momentum_platform_market_gmv_usd_billion"] - 1
    )
    out["interpretation"] = (
        "Cross-source definition/coverage diagnostic only; differences are not measurement error estimates"
    )
    return out


def write_design_rules() -> None:
    rows = [
        ["main_geography", "Indonesia", "ASEAN evidence cannot replace the advisor-requested Indonesia main analysis"],
        ["country_unit", "separate country-year", "Do not treat ASEAN as one tax or regulatory regime"],
        ["tax_inference", "not estimated", "GMV does not reveal taxable income, compliance, or tax liability"],
        ["business_model", "country-specific", "Use platform-share structure descriptively; do not impose one platform mix"],
        ["source_status", "external estimate", "e-Conomy SEA and Momentum Works are market estimates, not issuer or statistical-agency records"],
        ["vintage_policy", "latest available", "Canonical series uses the latest report vintage; all earlier vintages remain auditable"],
        ["pooling", "descriptive only", "Regional totals may summarize scale, but inference is based on within-country results"],
        ["interpretation", "digital commercial intensity", "GMV/GDP and GMV/consumption ratios are scale indicators, not national-accounting residuals"],
    ]
    with (OUT / "asean_corroboration_design_rules.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["design_dimension", "decision", "reason"])
        writer.writerows(rows)


def make_figure(growth: pd.DataFrame) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    plot = growth.sort_values("ecommerce_growth_2023_2025_pct")
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.barh(plot["country"], plot["ecommerce_growth_2023_2025_pct"], color="#2367A8")
    ax.bar_label(bars, fmt="%.1f%%", padding=4, color="#20262E")
    ax.set_xlim(0, max(plot["ecommerce_growth_2023_2025_pct"]) * 1.18)
    ax.set_xlabel("Growth (%)")
    ax.set_title("E-commerce GMV growth by country, 2023–2025", loc="left", pad=34)
    ax.text(0, 1.015, "Latest-vintage e-Conomy SEA estimates; countries remain separate analytical units",
            transform=ax.transAxes, fontsize=9, color="#5D6773")
    ax.grid(axis="x", color="#D9DEE5", linewidth=0.7)
    ax.set_axisbelow(True)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#AAB2BD")
    fig.tight_layout()
    fig.savefig(FIGURES / "asean_ecommerce_growth_2023_2025.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def validate(source: pd.DataFrame, panel: pd.DataFrame, growth: pd.DataFrame) -> None:
    key = ["report_vintage", "country", "observation_year", "metric"]
    assert len(source) == 450, f"unexpected source row count: {len(source)}"
    assert not source.duplicated(key).any(), "duplicate source-vintage metric key"
    assert (source["value_usd_billion"] > 0).all(), "non-positive GMV transcription"
    assert source["source_file"].map(lambda path: (ROOT / path).is_file()).all(), "missing archived report"
    assert len(panel) == 42 and panel["country"].nunique() == 6, "canonical panel coverage changed"
    assert panel.groupby("country")["observation_year"].nunique().eq(7).all(), "unbalanced country-year coverage"
    assert panel["component_rounding_residual_usd_billion"].abs().le(1.1).all(), "component sum inconsistent with rounded total"
    assert len(growth) == 6 and (growth["ecommerce_growth_2023_2025_pct"] > 0).all(), "corroboration growth check failed"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source = build_source_rows()
    panel = latest_vintage_panel(source)
    panel_context = add_world_bank_context(panel)
    revisions = revision_diagnostics(source)
    growth = growth_summary(panel)
    structure = platform_structure()
    cross_source = cross_source_2025(panel, structure)
    validate(source, panel, growth)

    source.to_csv(OUT / "economy_sea_source_vintages_2019_2025.csv", index=False)
    panel_context.to_csv(OUT / "asean_country_year_canonical_2019_2025.csv", index=False)
    revisions.to_csv(OUT / "economy_sea_revision_diagnostics.csv", index=False)
    growth.to_csv(OUT / "asean_growth_corroboration_2023_2025.csv", index=False)
    structure.to_csv(OUT / "platform_structure_2025.csv", index=False)
    cross_source.to_csv(OUT / "cross_source_ecommerce_gmv_2025.csv", index=False)
    write_design_rules()
    make_figure(growth)

    print(f"source_vintage_rows={len(source)}")
    print(f"canonical_country_year_rows={len(panel_context)}")
    print(f"repeated_vintage_diagnostics_rows={len(revisions)}")
    print(f"country_growth_rows={len(growth)}")
    print(f"platform_structure_rows={len(structure)}")
    print(f"cross_source_rows={len(cross_source)}")


if __name__ == "__main__":
    main()
