# Empirical backend package tree

This working bundle contains evidence, extracts, code, audit outputs, and documentation. Row counts below describe each file/module in its own grain and are not additive as one analytical N.

```text
Invisible-ledger/
├── data/                                         (~16 MB before latest additions)
│   ├── indonesia_fy2023/                         3 main cases; 11 source inputs; 14 sensitivity scenarios
│   ├── longitudinal/
│   │   ├── indonesia_platform_year_extension.csv 9 platform-years, FY2021–FY2024
│   │   ├── blibli_*                               2019–2025 annual plus overlapping quarterly/cumulative source records
│   │   ├── blibli_q1_2023_corrected_extract.csv   15 verified table cells/rows; 10 unique quarterly scope-period records
│   │   ├── bukalapak_annual_candidates.csv        5 records; 4 matched annual periods
│   │   └── historical_within_platform_ratios.csv  8 annual records; 7 positive-denominator ratios
│   ├── quarterly/
│   │   ├── clean_event_panel_accounting.csv       47 company/segment quarters
│   │   └── quarterly_panel_source_coverage.csv    47 source-reconciled rows
│   ├── bps_official/
│   │   ├── bps_ecommerce_2023_*                   38 provinces + national; 36 complete province records
│   │   ├── bps_ecommerce_2024_*                   38 provinces + national; 38 complete province records
│   │   └── bps_ecommerce_national_indicators_*    available national indicators, 2020–2024
│   ├── market/                                    22,393 security-days across 9 symbols
│   ├── measurement/                               accounting/scope reconciliations
│   ├── asean_context/                             2,860 World Bank slots; 2,617 numeric
│   └── legacy_not_active/                         preserved; prohibited as active evidence
├── sources/
│   ├── core_public_documents/                     issuer filings/releases and BPS 2024 source PDF
│   └── manifests/                                 source URLs, hashes, and procurement lineage
├── scripts/
│   ├── acquisition/                               public-source and market retrieval
│   ├── extraction/                                issuer/OCR extraction and reconciliation
│   └── analysis/                                  measurement, validation, event, and audit code
├── outputs/empirical_backend_2026-09-09/
│   ├── candidate_observation_census.csv           195 source records; 169 canonical; 165 ratio-eligible
│   ├── candidate_research_designs.csv             5 non-equivalent design options
│   ├── bps_province_panel_2023_2024.csv           78 rows including two national totals; 74 complete province-years
│   ├── bps_province_associations_by_year.csv      2 annual descriptive estimates
│   ├── bps_within_province_changes_2023_2024.csv  36 matched provinces
│   ├── quarterly_panel_summary.csv                3 platform summaries covering 47 quarters
│   ├── data_quality_issues.csv                     explicit defects and treatments
│   └── charts/                                    six validated analytical figures
├── notebooks/
│   ├── empirical_backend_audit_2026_09_09.ipynb
│   └── empirical_backend_audit_2026_09_09.executed.ipynb
└── reports/
    ├── EMPIRICAL_BACKEND_AUDIT_2026-09-09.md
    ├── empirical_backend_audit_2026_09_09.html
    └── EMPIRICAL_BACKEND_PACKAGE_TREE.md
```

## The key count distinction

- **9** = proposed unbalanced Grab/Tokopedia/Shopee Indonesia platform-years.
- **14** = direct annual Indonesia-aligned issuer/segment matched periods before final geography/scope admission.
- **47** = source-reconciled company/segment quarters, not country observations.
- **74** = complete official BPS province-years across 2023–2024, not firms.
- **22,393** = market security-days, not platform-accounting observations.
- **37,304** = all validated CSV rows in the repository, including source, context, market, intermediate, and output layers—not the thesis sample N.

