# Part 4: H2, national growth and who is outside every indicator (groundwork, version 2, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026, version 3** (git tag `parts-1-7-v3-frozen-2026-10-08`). Version 3 corrects the size of the 2023 seller-count finding (about half the rise was sellers counted for the first time, 37-56%, not "mostly"; `bps_rise_accounting.py`, ledger v10), fixes stale lines and folds in the dated notes; version 2 is at tag `parts-1-4-v2-frozen-2026-10-08`. Groundwork only: points for the writing stage. Further changes only as dated notes at the end.
Order: H2 comes before Objective 3 (between indicators) because Objective 3's explanation uses the H2 result, and H1 plus H2 complete the proposal's two links (Figure 1). Builds on `PART2_FRAMEWORK.md` Level 2.
Numbers: `bps_bridge.py` (`bps_recompute.json`), `bps_microdata_tests.py`, `bps_descriptives.py`, `bps_frame_check.py`, `bps_cohort_check.py`, `bps_cohort_2024_published.py`, `bps_h2_cheap_checks.py`, `gel_checks.py`, `wb_tests.py`, `wb_crosscountry.py`; ledgers v1 to v8.

## Punchline and verdict

- **The 2023 jump in the official count of online sellers was roughly half real entry and half existing sellers counted for the first time (37-56% of the rise, depending on how many sellers stopped); the newly counted were sellers using only chat and social media. The 2024 rise looks like real entry.**
- 2022-23 count: BPS published +27.4% sellers (819 thousand). E5 (pre-registered, falsified): 13% of 2023 sellers started that year, below the 21.5% the published rise requires even if no seller stopped. Direct accounting: 513 thousand sellers started selling online in 2023; the same start-year cohorts grew between the 2022 and 2023 surveys instead of shrinking, so the 2023 survey counts 306 thousand more pre-2023 sellers than the whole 2022 count (37% of the rise, net of exits; about 56%, 458 thousand, if sellers stopped at the 2020-22 rate of about 5% a year; `bps_rise_accounting.py`). Among sellers who started by 2022, marketplace users were flat (+0.3%) while chat-or-social-only sellers rose 13%.
- 2022-23 value: of BPS's published value increase (Rp318tn), newly counted sellers account for about 15-17% and entrants for about 25-30% (scenarios); the remaining 53-59% is not traceable to existing sellers' own answers (mean reported change in online revenue -4.3%; median 0%; 24% up, 44% unchanged, 32% down; firms with 20+ workers about +1%, seller-weighted). So: about half of the count jump is counting; most of the value jump cannot be traced to what respondents reported. The thesis says this and does not guess the cause.
- 2023-24 (published 2024 table): sellers who started before 2020 fell 10.2%, those who started in 2020-22 were flat, and at least 754 thousand sellers were new, more than the published rise of 584 thousand. Normal behaviour: old cohorts shrink, entry drives growth.
- 2023 was a break year in how BPS counted, not a permanent bias.

## H2 result on the published numbers (as in the proposal)

- National e-commerce value = number of businesses x sales per business. More businesses account for 71.0% of 2022-23 growth and 90.3% of 2023-24 growth (71.0% under BPS's other 2023 count). H2 holds on paper for both transitions.
- Meaning by transition: 2022-23, "more businesses" is about half new businesses and about half existing chat and social sellers counted for the first time; 2023-24, more businesses is consistent with real entry.

## How we know (independent angles)

1. Entrant share (E5, pre-registered): new 2023 sellers are 13% of the 2023 count, below the 21.5% the published rise requires with no exits (falsified).
2. Cohorts (exploratory): shrank between the 2020 and 2022 surveys (started by 2020: -9.9%), grew between 2022 and 2023 (+6.0%), shrank again from 2023 to 2024 (before 2020: -10.2%). 2023 is the break.
3. Provinces (exploratory): count growth followed sample-size growth, not the entrant share.
4. Channel (exploratory): the extra pre-2023 sellers were all off-marketplace (chat or social only +13%; marketplace users +0.3%).
5. Sellers' own reports (exploratory): existing sellers net up in 2022 (37% up, 24% down), net down in 2023 (24% up, 32% down); lack of demand rose from 35% to 41% and became the main obstacle.
6. BPS method: each round lists businesses in sampled areas and updates the sampling frame; the revenue questions are worded the same in both rounds (average monthly revenue, months with online sales, channel shares), so a change in wording does not explain the 2023 value growth. BPS's publication defines transaction value but gives no estimation detail.
Pre-registered: E5 (falsified), E6 (holds). Exploratory: 2 to 5 (data already seen when designed).

## Who is outside every administrative indicator (the proposal's additional analyses)

- Channels: about 96% of sellers use chat or social media (2023); marketplace use fell from 21.6% of sellers (2020) to 19.8% (2022), 17.8% (2023) and 17.2% (2024, published) (E2b, E2c hold). BPS's "marketplace" category is about half food and ride merchants (43% of its marketplace sellers use only Gojek or Grab; 47% use a shopping marketplace). 98.5% of 2023-24 value growth outside marketplaces (published). Only 13.5% of off-marketplace sellers want to join a marketplace.
- Records: 28.6% of marketplace sellers keep complete financial statements vs 12.3% of others (published; reproduced exactly). Share with statements: 23.5% (2020), 20.7% (2022) under stable coverage, 15.2% (2023), the last step partly reflecting the newly counted chat-only sellers (same pre-2020 cohort: 23.4% to 16.8% between surveys).
- Size: new sellers are a little smaller (2022 starters 86.5% under Rp300m a year vs 80.7% of pre-2020 sellers). At most about 5% of all online sellers are on marketplaces with Rp300m+ a year.
- Value without statements: sellers without statements hold 30-40% of 2022 online value (E1, range).
- World Bank: unregistered firms in six cities, 27% sell through social media, median sales Rp60m a year, 70% keep no written records (W1, W2 hold; W3 falsified on the mean); formal firms, 39.9% with neither website nor online tax filing, highest of 7 countries (F3, X3 hold).
- These sellers are outside platform records and tax records; only BPS's survey reaches them, and in 2023 it reached many more of them. The jump in the count is itself a lower bound on how many existing sellers sat outside the earlier count.

## Objections and answers

- Exits: they make the cohort and entry gaps larger, not smaller. The 56% figure uses the 2020-22 shrink of the started-by-2020 cohort (about 5% a year), itself measured across two survey rounds; with no exits the share is 37%.
- Respondents misdating their start year: people date events as more recent (forward telescoping), which overstates entrants; our gap is conservative. Misdating cannot create extra pre-2023 sellers in total.
- Misread files: weights match published counts; the 28.63/12.25 split reproduces exactly; codes checked against BPS's layout.
- Channel question wording differs (2023 file "promotion and/or sales", 2024 file "sales"): affects the marketplace split, not the cohort totals.
- Sampling error: cannot be separated from a coverage change at province level (no area or design variables; the researcher decided not to contact BPS); the national cohort pattern (shrink, grow, shrink) and the channel pattern are hard to produce by chance, but they stay exploratory.
- Published 2024 shares are rounded to two decimals: changes of this size are not affected.
- Value-weighted change of existing sellers is not available (the 2024 file has no revenue amounts); a few very large firms growing a lot could account for part of the untraced value growth.

## What H2 does and does not conclude

- Does: national e-commerce growth on BPS's published numbers comes mainly from more businesses (H2 holds on paper); in 2022-23 about half of the rise in businesses (37-56%) reflects BPS counting existing chat-and-social sellers for the first time and the rest real entry, in 2023-24 real entry; most of BPS's 2023 value growth cannot be traced to what respondents reported.
- Does not: that BPS's figures are wrong in general; what produced the untraced value growth; why BPS widened coverage; anything about total online buying.

## Compared with the proposal

- Same: the H2 split for both transitions and both counts; channel and records as additional analyses.
- Added: the business count treated as an estimate and tested from several angles; 2023 identified as a break year and 2024 as normal entry; the newly counted sellers located (chat and social only); the value side split and its untraced part stated; sellers' own reports for 2022 and 2023; the records decline qualified; World Bank informal, formal and cross-country evidence.

## Status of open items

- No contact with BPS (researcher's decision, 8 Oct 2026): the exploratory checks stay exploratory; the 2023-24 cohort check stays on published figures.
- The 2025 survey microdata (2024 activity) is not on SILASTIK as of 8 Oct 2026.

## Dated notes

(none since version 3)
