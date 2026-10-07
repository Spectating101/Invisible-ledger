# Part 4: H2, national growth and who is outside every indicator (groundwork, version 2, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026, version 2** (git tag `parts-1-4-v2-frozen-2026-10-08`). Version 2 folds in the dated notes of 8 Oct; version 1 is at tag `part-4-groundwork-frozen-2026-10-08`. Groundwork only: points for the writing stage. Further changes only as dated notes at the end.
Order: H2 comes before Objective 3 (between indicators) because Objective 3's explanation uses the H2 result, and H1 plus H2 complete the proposal's two links (Figure 1). Builds on `PART2_FRAMEWORK.md` Level 2.
Numbers: `bps_bridge.py` (`bps_recompute.json`), `bps_microdata_tests.py`, `bps_descriptives.py`, `bps_frame_check.py`, `bps_cohort_check.py`, `bps_cohort_2024_published.py`, `bps_h2_cheap_checks.py`, `gel_checks.py`, `wb_tests.py`, `wb_crosscountry.py`; ledgers v1 to v8.

## Punchline and verdict

- **The 2023 jump in the official count of online sellers was mostly sellers newly counted, not newly started; the newly counted were sellers using only chat and social media. The 2024 rise looks like real entry.**
- 2022-23 count: BPS published +27.4% sellers. Entry explains at most +15.5% (E5, pre-registered, falsified). The same start-year cohorts grew between the 2022 and 2023 surveys instead of shrinking: 306 thousand more pre-2023 sellers than the whole 2022 count, 37% of the rise, net of exits. Among sellers who started by 2022, marketplace users were flat (+0.3%) while chat-or-social-only sellers rose 13%.
- 2022-23 value: of BPS's published value increase (Rp318tn), newly counted sellers account for about 15-17% and entrants for about 25-30% (scenarios); the remaining 53-59% is not traceable to existing sellers' own answers (mean reported change in online revenue -4.3%; median 0%; 24% up, 44% unchanged, 32% down; firms with 20+ workers about +1%, seller-weighted). So: the count jump is mostly counting; most of the value jump cannot be traced to what respondents reported. The thesis says this and does not guess the cause.
- 2023-24 (published 2024 table): sellers who started before 2020 fell 10.2%, those who started in 2020-22 were flat, and at least 754 thousand sellers were new, more than the published rise of 584 thousand. Normal behaviour: old cohorts shrink, entry drives growth.
- 2023 was a break year in how BPS counted, not a permanent bias.

## H2 result on the published numbers (as in the proposal)

- National e-commerce value = number of businesses x sales per business. More businesses account for 71.0% of 2022-23 growth and 90.3% of 2023-24 growth (71.0% under BPS's other 2023 count). H2 holds on paper for both transitions.
- Meaning by transition: 2022-23, "more businesses" is largely more businesses counted (chat and social sellers reached by the survey); 2023-24, more businesses is consistent with real entry.

## How we know (independent angles)

1. Entrant share (E5, pre-registered): new 2023 sellers can explain at most +15.5%; at least 40% of the published rise (log terms) is not explained by entry.
2. Cohorts (exploratory): shrank between the 2020 and 2022 surveys (started by 2020: -9.9%), grew between 2022 and 2023 (+6.0%), shrank again from 2023 to 2024 (before 2020: -10.2%). 2023 is the break.
3. Provinces (exploratory): count growth followed sample-size growth, not the entrant share.
4. Channel (exploratory): the extra pre-2023 sellers were all off-marketplace (chat or social only +13%; marketplace users +0.3%).
5. Sellers' own reports (exploratory): existing sellers net up in 2022 (37% up, 24% down), net down in 2023 (24% up, 32% down); lack of demand rose from 35% to 41% and became the main obstacle.
6. BPS method: each round lists businesses in sampled areas and updates the sampling frame; the revenue questions are worded the same in both rounds (average monthly revenue, months with online sales, channel shares), so a change in wording does not explain the 2023 value growth. BPS's publication defines transaction value but gives no estimation detail.
Pre-registered: E5 (falsified), E6 (holds). Exploratory: 2 to 5 (data already seen when designed).

## Who is outside every administrative indicator (the proposal's additional analyses)

- Channels: about 96% of sellers use chat or social media (2023); marketplace use fell from 21.6% of sellers (2020) to 19.8% (2022), 17.8% (2023) and 17.2% (2024, published) (E2b, E2c hold). BPS's "marketplace" category is mostly food and ride merchants (Gojek 45%, Shopee 42%, Grab 42%, Tokopedia 13% of its marketplace sellers). 98.5% of 2023-24 value growth outside marketplaces (published). Only 13.5% of off-marketplace sellers want to join a marketplace.
- Records: 28.6% of marketplace sellers keep complete financial statements vs 12.3% of others (published; reproduced exactly). Share with statements: 23.5% (2020), 20.7% (2022) under stable coverage, 15.2% (2023), the last step partly reflecting the newly counted chat-only sellers (same pre-2020 cohort: 23.4% to 16.8% between surveys).
- Size: new sellers are a little smaller (2022 starters 86.5% under Rp300m a year vs 80.7% of pre-2020 sellers). At most about 5% of all online sellers are on marketplaces with Rp300m+ a year.
- Value without statements: sellers without statements hold 30-40% of 2022 online value (E1, range).
- World Bank: unregistered firms in six cities, 27% sell through social media, median sales Rp60m a year, 70% keep no written records (W1, W2 hold; W3 falsified on the mean); formal firms, 39.9% with neither website nor online tax filing, highest of 7 countries (F3, X3 hold).
- These sellers are outside platform records and tax records; only BPS's survey reaches them, and in 2023 it reached many more of them. The jump in the count is itself a lower bound on how many existing sellers sat outside the earlier count.

## Objections and answers

- Exits: they make the cohort and entry gaps larger, not smaller.
- Respondents misdating their start year: people date events as more recent (forward telescoping), which overstates entrants; our gap is conservative. Misdating cannot create extra pre-2023 sellers in total.
- Misread files: weights match published counts; the 28.63/12.25 split reproduces exactly; codes checked against BPS's layout.
- Channel question wording differs (2023 file "promotion and/or sales", 2024 file "sales"): affects the marketplace split, not the cohort totals.
- Sampling error: cannot be separated from a coverage change at province level (no area or design variables; the researcher decided not to contact BPS); the national cohort pattern (shrink, grow, shrink) and the channel pattern are hard to produce by chance, but they stay exploratory.
- Published 2024 shares are rounded to two decimals: changes of this size are not affected.
- Value-weighted change of existing sellers is not available (the 2024 file has no revenue amounts); a few very large firms growing a lot could account for part of the untraced value growth.

## What H2 does and does not conclude

- Does: national e-commerce growth on BPS's published numbers comes mainly from more businesses (H2 holds on paper); in 2022-23 that mostly reflects BPS counting more existing chat-and-social sellers, in 2023-24 real entry; most of BPS's 2023 value growth cannot be traced to what respondents reported.
- Does not: that BPS's figures are wrong in general; what produced the untraced value growth; why BPS widened coverage; anything about total online buying.

## Compared with the proposal

- Same: the H2 split for both transitions and both counts; channel and records as additional analyses.
- Added: the business count treated as an estimate and tested from several angles; 2023 identified as a break year and 2024 as normal entry; the newly counted sellers located (chat and social only); the value side split and its untraced part stated; sellers' own reports for 2022 and 2023; the records decline qualified; World Bank informal, formal and cross-country evidence.

## Status of open items

- No contact with BPS (researcher's decision, 8 Oct 2026): the exploratory checks stay exploratory; the 2023-24 cohort check stays on published figures.
- The 2025 survey microdata (2024 activity) is not on SILASTIK as of 8 Oct 2026.

## Dated notes

- **8 Oct 2026, after version 2 (`part5_checks.py`).** Qualification: BPS's "marketplace" slice is not the same object as shopping-marketplace GMV. Only 47% of BPS's marketplace sellers use a shopping marketplace (Tokopedia, Shopee, Bukalapak, Lazada); 43% use only Gojek or Grab (food and ride merchants). So the slow growth of BPS's marketplace slice and of the platform indicators is a fact, but the slices overlap rather than match; read "where they measure the same slice" as "where they measure overlapping slices". The disagreement still sits outside marketplaces.
