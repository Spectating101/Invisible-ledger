# Invisible Ledger — expanded research collection

9 September 2026. This is the broad research archive requested by Chris, not the compact submission previously sent to Kong and not a claim that the main sample is finalized.

## Open these first

- `CSV_FILE_INDEX.csv`: filenames, row counts, column counts, sizes, and original/new roles for every CSV in this collection.
- `BROAD_COLLECTION_COUNTS.json`: separate source, market, macro, and publisher counts plus validation checks and failed downloads. Do not sum these into sample N.
- `source_extracts/`: platform-specific source extracts from this expansion, including additional Blibli periods and the earlier Grab, Shopee, and Bukalapak findings.
- `broad_archive/issuer_document_index.csv`: Sea and GoTo disclosure links. Sea includes 36 quarterly-release periods from 2017Q3 through 2026Q2. GoTo links are deduplicated on download; selector-page requests are not themselves observations.
- `broad_archive/document_manifest.csv`: saved documents and API files, source URLs, discovery parents, retrieval times, sizes, and hashes.
- `broad_archive/searchable_source_excerpts.csv`: searchable passages with PDF page locations. These are search aids, not numerical observations.

## What the new material contributes

Blibli/GDN now has seven annual issuer-year candidates (2019–2025), and 15 distinct Group quarterly periods across the two extracted release CSVs. Four segment lines overlap Group totals. Half-year and nine-month cumulative amounts also overlap the quarters. Do not count these as independent firms or mix frequencies. The three additional releases have passed segment-sum checks within rounding tolerance, but still need visual cell and geographic eligibility review.

Bukalapak has four matched annual candidates (2020–2023). Overseas operations prevent treating the Group as automatically country-isolated. The FY2024 TPV/revenue pair has unequal periods and remains excluded.

Grab's country-revenue extension and Shopee's additional country-market anchors remain as documented in `README.md`. Neither makes unavailable country GTV or revenue directly observed.

The new Sea release archive contains annual filings, presentations, transcripts and releases; `sea_gmv_disclosure_candidates.csv` extracts explicit rounded GMV statements from 31 release periods. Those 41 statements include annual and quarterly values, and are not 41 independent country observations. Some historical headline amounts differ from later filings: retain the vintage rather than silently overwrite it.

## Other data layers

- `broad_archive/platform_market_daily_2010_2026.csv`: 22,393 security-days, 22,317 with nonmissing close, for GRAB, SE, GOTO.JK, BUKA.JK, BELI.JK, BABA, NASDAQ Composite, S&P 500 and Jakarta Composite. Dates follow saved UTC timestamps; exchange timezone and currency are retained. Raw Yahoo JSON and corporate-action events are saved. These are not recomputed CAR results; event timing, adjustments and contamination still require analysis.
- `broad_archive/asean_worldbank_context_2000_2025.csv`: 2,860 country-year-indicator slots, 2,617 populated; 11 Southeast Asian countries, 10 indicators, 2000–2025. Missing values remain missing. Includes GDP, FX, population, internet/mobile/broadband, consumption, services and tax-revenue context. Indicator units follow their definitions, not a universal currency. These do not enlarge platform N.
- `broad_archive/momentum_publisher_articles.csv`: 875 unique publisher articles returned across two historical topic searches. These are text records, not platform observations. 53 titles are flagged for closer market-report review; public linked charts/reports are preserved separately. The filter is a search aid, not a quality endorsement. Broad query coverage does not mean every article is relevant or every report is freely available.
- `broad_archive/preserved_existing/`: 246 earlier files copied unchanged with checksums. Includes existing source extracts, scripts, results, supporting evidence and explicitly separated `08_LEGACY_NOT_ACTIVE`. Inclusion does not validate old values or make non-final CARs final. `preserved_existing_manifest.csv` records original paths.
- `broad_archive/ocr/`: OCR of image-only Blibli table pages. OCR text is unverified and must be checked against its accompanying source-page image before numerical use.

## YZUC and Refinitiv

Used YZUC catalog, dataset-description and query tools to inspect actual registered holdings, then the source-probe and custom-plan tools for Sea's public resource API. All 227 rows inspected in `refinitiv_fundamental_annual_panel` lack fiscal years and use a current-year snapshot marker; that material is not a historical country panel. Relevant snapshot matches and the finding are saved in `yzuc_refinitiv_inspection.json`.

YZUC archive job `662dbc762ec5` is **pending approval**. It has not run and no Drive archive verification is claimed. Public issuer/API files have been downloaded locally through the newly supplied scripts. Existing licensed-source material should remain within authorized academic use; this folder is not a public redistribution package.

## Reproduction and remaining work

All new acquisition/extraction code is in this parent folder, explicitly distinct from preserved older scripts. Run acquisition scripts sequentially because they share one manifest; individual downloads within each run use bounded concurrency. Then run `index_broad_evidence.py` and `summarize_broad_archive.py` to refresh indexes/counts. The latter verifies source hashes and uniqueness of market and World Bank keys.

The directory now offers a much broader evidence base. Next, numeric table extraction and period/geography/business-scope reconciliation determine which observations enter the longitudinal Indonesia analysis. Country allocation, consolidation changes, negative revenue and rounded/restated releases remain substantive issues. Downloading supporting data does not settle them.

This is a substantial completed acquisition pass, not a claim that every possible source has been exhausted, that the proposal has been approved, or that the resulting main sample is sufficient. No thesis/proposal text was edited and nothing was sent to Kong.
