# ASEAN corroboration data

This directory is a supporting empirical module for *Invisible Ledger*. It
does not replace the proposed Indonesia main analysis and does not pool ASEAN
countries into a common tax or regulatory sample.

## Files

| File | Rows | Grain and role |
|---|---:|---|
| `economy_sea_source_vintages_2019_2025.csv` | 450 | One country × observation year × metric × report vintage. Preserves revised estimates. |
| `asean_country_year_canonical_2019_2025.csv` | 42 | One country × year, using the latest available publication vintage and adding World Bank scale variables. |
| `economy_sea_revision_diagnostics.csv` | 210 | One country × year × metric, comparing publication vintages. |
| `asean_growth_corroboration_2023_2025.csv` | 6 | One within-country 2023–2025 growth comparison. |
| `platform_structure_2025.csv` | 6 | One country-level platform-market structure record from Momentum Works. |
| `asean_tax_platform_context.csv` | 6 | Country-specific tax object, platform role, timing, and scope boundary from official sources. |
| `asean_country_heterogeneity_profile.csv` | 6 | Joins market composition, platform structure, and tax architecture without pooling countries. |
| `cross_source_ecommerce_gmv_2025.csv` | 6 | e-Conomy SEA versus Momentum Works definition/coverage diagnostic. |
| `asean_corroboration_design_rules.csv` | 8 | Explicit admission, pooling, and interpretation rules. |

## Evidence classes

- e-Conomy SEA values are external market estimates credited to Bain analysis.
- Momentum Works values are external platform-market estimates.
- World Bank values are official context series, not measures of platform GMV.
- No row estimates tax non-compliance, unpaid tax, hidden income, or omitted GDP.
- Current tax rules are not applied retrospectively: the profile explicitly records whether each identified instrument was active in FY2023.

## Reproduction

Run:

```bash
python3 scripts/analysis/build_asean_corroboration.py
```

The source-report acquisition script is:

```bash
python3 scripts/acquisition/acquire_economy_sea_reports.py
```

Source chart values are reviewed manual transcriptions. The analysis script
does not claim OCR extraction. It validates row uniqueness, archived-source
existence, positive values, component reconciliation within chart-rounding
tolerance, and balanced canonical coverage for the retained years.
