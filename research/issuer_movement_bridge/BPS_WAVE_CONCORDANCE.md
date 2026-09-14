# BPS wave and microdata concordance — empirical review

**Status:** source-certification note for the empirical package. It does not elevate any BPS result into the thesis by itself.

## Why this note exists

BPS uses several related year labels: publication title/reference year, survey year, and the year to which individual questionnaire items refer. Treating these as interchangeable would create a false panel. This note records only what the currently inspected official sources support.

## Source-level concordance

| Item | 2023 evidence | 2024 evidence | Current certification |
|---|---|---|---|
| Publication object | *Statistik E-Commerce 2023*, released 30 Jan 2025, annual catalogue 8101004 | *Statistik E-Commerce 2024*, released 28 Nov 2025, annual catalogue 8101004 | **Strong publication-family continuity** |
| Stated perspective | E-commerce business perspective; profile, workers, business activity, and e-commerce business revenue during 2023; province estimates | E-commerce business perspective; profile, workers, business activity, and e-commerce transaction value during 2024; province estimates | **Broad conceptual continuity; individual indicators still require item-level checks** |
| Published transaction value | Rp1,100.87tn in active extract | Rp1,288.93tn in active extract | **Usable for nominal total growth, subject to publication definitions** |
| Financial-report ownership | 15.19% in active extract | 17.15% in active extract | **Conditional cross-wave comparison** until questionnaire/item universe is verified for both waves |
| Marketplace business-use share | 17.80% in active extract | 17.23% in active extract | **Conditional cross-wave comparison**; multiple-response business-use measure |
| Exclusive marketplace transaction-value component | Direct 2023 amount Rp200.68tn / 18.23% in active extract | Active extract stores 15.79% share; 2024 amount is currently derived from rounded share × total | **Conditional source concordance**; do not promote the ~1.42% growth calculation until the 2024 original table wording/denominator is directly verified |
| Province repeated cross-section | 38 province labels after excluding national Indonesia row; two high-RSE cells withheld in focal fields | 38 province labels after excluding national Indonesia row | **36 complete matched provinces** for marketplace/financial-report comparisons; ecological, not a business panel |

Official publication pages:

- 2023: <https://www.bps.go.id/id/publication/2025/01/30/d52af11843aee401403ecfa6/statistik-e-commerce-2023.html>
- 2024: <https://www.bps.go.id/id/publication/2025/11/28/647323224ecc656c2933571b/statistik-e-commerce-2024.html>

## Microdata timing clarification

The currently located SILASTIK object is titled **Survei Usaha/Perusahaan E-Commerce 2024**. Its catalogue says the survey covers businesses using the internet to accept orders or sell goods/services. Its dictionary includes `R325`, explicitly referring to constraints in online-selling activity **during 2023**.

Therefore this file is treated as:

> **survey year 2024 / economic reference year 2023**

rather than as microdata representing economic year 2024.

Catalogue: <https://silastik.bps.go.id/v3/index.php/mikrodata/detail/ODdXeUNNcW5vcVVGVWhTUERuTGNTQT09>

### High-value variables in the located file

- `R308` — financial-report ownership;
- `R309A-E` and named-marketplace subitems — sales channels;
- `R313A-C` — monthly revenue shares from offline, marketplace, and nonmarketplace sales;
- `R314` — average online-sales transaction frequency;
- `R315/R315B` — business revenue relative to previous year and percentage change;
- `R316A-C` — sales-value shares by customer type;
- `R320/R320A` — online export indicator and export-sales share;
- `W_FINAL` — survey weight.

The catalogue currently lists province presentation level, DBF format, 8.91MB size, price Rp186,870, and requires an abstract, signed data-use agreement, and dissemination fee.

## What acquisition would add

If licensed, this reference-year-2023 file could replace several aggregate/ecological approximations with business-level analysis for FY2023:

1. marketplace use × financial-report ownership;
2. marketplace/nonmarketplace revenue share × financial-report ownership;
3. channel use × business size/sector/geography;
4. revenue growth × channel/recordkeeping characteristics;
5. exports × channel/recordkeeping characteristics;
6. weighted estimates using `W_FINAL` rather than treating businesses or provinces as equal observations.

This is unusually well aligned with the original FY2023 platform comparison because the participant-side microdata reference year is also 2023.

## What acquisition would NOT add

The located file does **not** create a business-level 2023→2024 panel. A separately comparable later survey/microdata file corresponding to economic year 2024 would be required for that extension. A current public catalogue search in this review did not locate such a 2025-survey/economic-year-2024 microdata object; this should be treated as **not yet located**, not as proof that BPS will not release or cannot provide it.

## Current empirical treatment

- **Safe now:** published national totals by reference year; province cross-sections with explicit ecological interpretation; reference-year-2023 microdata feasibility as an acquisition option.
- **Conditional:** financial-report and sales-channel trends across 2023/2024; exclusive marketplace-component growth; any inference requiring identical item universes across waves.
- **Not supported:** business-level longitudinal transitions from 2023 to 2024 using the currently located microdata; causal formalization effects; linking BPS respondent records to issuer or DGT records.

## Stop rule

No BPS trend or business-level claim should be promoted merely because variable names look similar. The final empirical package should record, for each item, the reference population, question wording, unit, weighting rule, and reference year before treating observations as comparable across time.
