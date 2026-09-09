# Data guide

## Active review layers

| Directory | Role | Important boundary |
|---|---|---|
| `indonesia_fy2023/` | Three-case reviewed construction and sensitivity | One fiscal year; not sufficient as the entire thesis sample |
| `longitudinal/` | Multi-year candidates and filing extracts | Candidate coverage is not final admission |
| `quarterly/` | Company-quarter accounting and source reconciliation | Not an Indonesia country panel |
| `measurement/` | Revenue, incentives and reporting-scope reconciliations | Designed to explain measurement dependence |
| `market/` | Daily prices, events and exploratory event outputs | Event interpretation remains unresolved |
| `asean_context/` | Country-level macro, market and policy context | Must remain separate by country and definition |
| `legacy_not_active/` | Superseded or unsafe historical files | Do not use in active analysis |

## Known coverage counts

- FY2023 Indonesia construction: 3 platform cases supported by 11 source inputs.
- Historical early filing extracts: Grab annual/segment and geography; Shopee annual revenue and 20 quarterly GMV observations.
- Existing company-quarter accounting inventory: 47 rows (17 Grab, 16 GoTo, 14 Sea).
- Blibli candidates: 7 annual issuer-years (2019–2025) plus quarterly/cumulative and segment records that overlap those years.
- Bukalapak matched annual group candidates: 4 (2020–2023), pending geographic eligibility.
- Platform market data: 22,393 security-days across five platform securities and four comparator/index symbols in the broad collection.
- World Bank ASEAN context: 2,860 country-year-indicator slots, 2,617 populated.

These counts describe different data layers. They must never be added together as a single sample N.

## Original versus generated files

CSV source extracts and analytical outputs are transformations, even when mechanically produced from primary documents. The selected filings in `sources/core_public_documents/` are the closest repository objects to raw source evidence. Full procurement records are in `sources/manifests/`.

