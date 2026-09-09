# IL coverage expansion — working acquisition, 9 September 2026

This folder adds newly located evidence to the existing September 8 empirical base. It does not replace the dataset sent to Kong, revise the manuscript, or establish that the enlarged sample is approved. Raw documents are unchanged downloads; CSVs are explicitly new source extracts, not original downloads.

## What has been recovered

- Blibli/GDN: annual paired transaction/revenue source material spans 2019–2025. Five later years were extracted programmatically from releases; two earlier years were transcribed from the IPO prospectus. These are seven issuer-years, NOT the 98 extraction rows counted as 98 independent firms. Segment detail supports a different unit of analysis and overlaps the group totals.
- Bukalapak: source-reported annual TPV/revenue pairs for 2020–2023. Annual and sustainability reports are issuer documents downloaded from a third-party mirror, not the issuer server. AR2023 printed p65 explicitly discloses overseas operations; none is silently promoted to an Indonesia-only pair. The FY2024 sustainability table's TPV is nine months and revenue twelve months. That row is excluded from paired annual analysis.
- Grab: FY2025 20-F geographic revenue table extracted for 2023–2025: 21 rows, comprising six named countries plus a regional residual in each year. Indonesia FY2025 revenue is USD715m. This does not supply country GTV.
- Shopee: original Momentum Works country GMV anchor for 2020 (USD14.2bn), and 2025 country market/share inputs (USD57.7bn; 54%). The existing Sea FY2025 filing explicitly discloses an 11.4% service monetization rate. Any derived country revenue remains conditional, not directly reported.
- ASEAN: original Momentum Works 2025 country market/share appendix, six countries, retained separately. Its GMV definition includes cancelled, returned and refunded paid orders; it is not automatically comparable with Blibli's paid-and-delivered TPV. Rounded Indonesia shares sum to 101%; do not normalize silently.

## Open checks that affect actual N

The main Indonesia panel has NOT been relabeled with an inflated observation count. Adding these issuers requires country scope and business-scope checks. Blibli's prospectus p88 states historical revenue was from operations in Indonesia, but that is not a statement that every travel transaction occurred within Indonesia, nor proof of the same geographic perimeter through 2025.

The release extraction preserves reporting vintages. Four Q4 2024 scope keys differ between the FY2024 and FY2025 releases; see the conflict CSV. Annual FY2024 totals agree in those two releases. Keep quarterly, nine-month, annual and segment observations separate. Further downloaded releases are image-only and await table extraction/verification. No quarterly value was created by dividing an annual number by four.

Blibli's published take rate is GPBD/TPV, NOT net revenue/TPV. Negative net revenue is preserved, not changed to zero. The 2019 3P ratio cannot be treated as an ordinary positive-denominator comparison.

## Files and reproducibility

- `raw_sources/`: saved source documents; early HTML refetch variants preserved.
- `text_extracts/`: derived text, not source originals.
- `source_extracts/`: source-faithful observations with units, periods, scope and locators.
- `acquire_sources.py`: new downloading code; cache avoids unnecessary repeat downloads. It follows PDF links from the issuer releases. One Bukalapak main-domain URL returns HTTP406; its alternate IR page is only a JavaScript shell.
- `procurement_log.json`: successful and failed acquisition attempts and checksums.
- `extract_blibli_tables.py`: extraction of selected text-readable release tables. Does not silently resolve conflicting vintages.
- `extract_grab_geography.py`: country-revenue extraction with group-total reconciliation.
- `COVERAGE_AND_NEXT_CHECKS.csv`: evidence found and remaining eligibility checks.

Run the two extraction scripts with Python3 after acquisition. Dependencies: beautifulsoup4 and Poppler/pdftotext. Manual prospectus and market-chart transcriptions still require human source review; code success alone is not evidence of geographic compatibility.

This is the first expanded acquisition pass, not an exhaustive search of every available source or a final replication archive. Outstanding work includes the image-only quarterly tables, Bukalapak country allocation, earlier Tokopedia matched financials, Shopee 2021 and definition comparability, and Grab's later transaction-scope reconciliation. None requires changing the original files or presenting supporting observations as the Indonesia main sample.
