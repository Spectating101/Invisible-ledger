# Data guide

## Active review layers

| Directory | Role | Important boundary |
|---|---|---|
| `indonesia_fy2023/` | Three-case reviewed construction and sensitivity | One fiscal year; not sufficient as the entire thesis sample |
| `longitudinal/` | Multi-year candidates and filing extracts | Candidate coverage is not final admission |
| `quarterly/` | Company-quarter accounting and source reconciliation | Not an Indonesia country panel |
| `measurement/` | Revenue, incentives and reporting-scope reconciliations | Designed to explain measurement dependence |
| `market/` | Daily prices, events and exploratory event outputs | Event interpretation remains unresolved |
| `bps_official/` | Official Indonesia national and province e-commerce statistics | Different unit from issuer data; province evidence is ecological |
| `asean_context/` | Country-level macro, market and policy context | Must remain separate by country and definition |
| `asean_corroboration/` | Revision-aware SEA-6 market histories and diagnostics | Six country analyses; never a pooled tax sample |
| `global_ecommerce/` | Definition-aware issuer transaction/revenue histories | Global corroboration only; not Indonesia observations or a representative firm sample |
| `payments/` | Bank Indonesia SPIP and QRIS payment-system evidence | Independent payment ledger; not e-commerce-only and never pooled with issuer/BPS observations |
| `institutional/` | Indonesian marketplace tax architecture and market-coverage context | Policy reach, market share, and analytical sample coverage are different quantities |
| `legacy_not_active/` | Superseded or unsafe historical files | Do not use in active analysis |

The first executed tests of the current hypotheses are kept under
`outputs/hypothesis_tests_2026-09-10/` and documented in
`reports/HYPOTHESIS_TESTS_2026-09-10.md`. They preserve the evidence-tier
boundaries above and do not define an approved main sample.

## Known coverage counts

- FY2023 Indonesia construction: 3 platform cases supported by 11 source inputs.
- Historical early filing extracts: Grab annual/segment and geography; Shopee annual revenue and 20 quarterly GMV observations.
- Existing company-quarter accounting inventory: 47 rows (17 Grab, 16 GoTo, 14 Sea).
- Blibli candidates: 7 annual issuer-years (2019–2025) plus quarterly/cumulative and segment records that overlap those years.
- Bukalapak matched annual group candidates: 4 (2020–2023), pending geographic eligibility.
- Platform market data: 22,393 security-days across five platform securities and four comparator/index symbols in the broad collection.
- World Bank ASEAN context: 2,860 country-year-indicator slots, 2,617 populated.
- BPS repeated province evidence: 74 complete province-years across 2023–2024; national indicators extend across available years from 2020–2024.
- Indonesia-aligned direct annual candidate design: 14 matched periods across Blibli, Bukalapak, and Tokopedia, before final geographic/scope admission.
- ASEAN corroboration: 450 source-vintage metric rows yielding 42 latest-vintage country-years across six countries; supporting evidence only.
- Global e-commerce corroboration: 48 matched issuer-years across eight businesses, yielding 40 within-issuer annual transitions; 11 transitions are flagged for known perimeter breaks.
- Bank Indonesia payment extension: 18,954 national monthly SPIP rows, 42,701 regional monthly rows, 1,460 published annual rows, and 14 separate official-report observations. These are metric-period records, not an e-commerce sample N.
- 2023 Indonesia marketplace context: Shopee and Tokopedia account for 70% of the referenced market estimate; adding Blibli gives 74%. The four marketplaces designated for Article 22 withholding in July 2026 correspond to 83% of that 2023 estimate. These are coverage diagnostics, not one analytical N or a contemporaneous policy-impact measure.
- Marketplace expansion context: 22 Indonesia platform-share snapshot rows for 2022–2025 and 19 Southeast Asia platform-GMV rows for 2020–2024. A separate nine-row Lazada/TikTok country inventory records why those activity observations do not yet qualify as matched issuer transaction/revenue pairs.
- Proposal review controls: `quality_control/proposal_preemptive_review_resolution_status_2026-09-11.csv` records 29 anticipated review issues—19 resolved in the backend, five partially resolved, three requiring an advisor decision, one future-data dependency, and one awaiting insertion into the authoritative proposal file.
- Stakes control: `quality_control/stakes_evidence_claim_matrix_2026-09-11.csv` maps six decision domains to observed evidence, defensible consequences, and outcomes that remain untested.

These counts describe different data layers. They must never be added together as a single sample N.

The apparent 227-row YZUC/Refinitiv annual panel is **not** counted: field inspection shows that every `fiscal_year` is missing and the object is an FY0 cross-sectional snapshot.

## Original versus generated files

CSV source extracts and analytical outputs are transformations, even when mechanically produced from primary documents. The selected filings in `sources/core_public_documents/` are the closest repository objects to raw source evidence. Full procurement records are in `sources/manifests/`.
