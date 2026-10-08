# Part 3: H1, inside the platforms (groundwork, version 2, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026, version 4** (git tag `parts-1-7-v4-frozen-2026-10-08`). Version 3 corrected the size of the 2023 seller-count finding (about half the rise was sellers counted for the first time, 37-56%, not "mostly"; `bps_rise_accounting.py`, ledger v10), fixes stale lines and folds in the dated notes; version 2 is at tag `parts-1-4-v2-frozen-2026-10-08`. Version 4 (8 Oct, after the independent review in `../independent_review_2026-10-08/REVIEW.md`): stated as stand-in conditions; the 2023 seller gap stated as not explained by first-time entry, with returning sellers named; the market multiples treated as arithmetic; H1 test wording corrected; version 3 is at tag `parts-1-7-v3-frozen-2026-10-08`. Version 3 also adds the Objective 1 block. Groundwork only: points for the writing stage. Further changes only as dated notes at the end.
Builds on `PART1_PROBLEM_AND_STAKES.md` and `PART2_FRAMEWORK.md` (Level 1). Numbers: `h1_extended.py`, `build_numbers.py` (`test_battery.csv`), `h1_quarterly.py`, `growth_decomposition.py`, `wedge_split.py`, `goto_on_demand.py`, `h1_groundwork.py`, `timing_check.py`, `gel_checks.py`; checked by claims ledgers v1 to v8.

## Objective 1: how big the invisible wedge is (the proposal's numbers, unchanged)

- 2023, three platforms (Shopee, Tokopedia, Grab Indonesia): transaction value US$43.23bn, revenue US$3.16bn, invisible wedge US$40.07bn, ecosystem ratio 12.7 (proposal Table 5). About 2.9% of Indonesia's 2023 GDP in size only: it is transaction value, not value added.
- Robust to construction: Shopee's assumed take rate of 9-11% moves the wedge only between US$39.86bn and US$40.29bn; dropping any one platform leaves at least US$20.70bn. Blibli's and Bukalapak's wedges (US$3.20bn, US$10.50bn) are left out of the total for scope reasons (proposal section 5.1).
- Platform-year take rates and ecosystem ratios: `tables/take_rate_levels.csv`.
- What the wedge is for: size. It moves with transaction value (about 96% of each change in the main sample; arithmetic, because the take rate is small). Whether revenue stays a reliable guide is growth divergence's job: about two thirds of Indonesian revenue movement came from the take rate, against about a quarter abroad (`wedge_split.py`).

## Punchline and verdict

- **Punchline (whole thesis, H1 is the first half):** Indonesia's two biggest online-economy growth stories in 2023, platform revenue booming and the official count of online sellers surging, were in large part about how things were measured: revenue rose through pricing rather than more buying, and about half of the rise in sellers is not explained by first-time entry.
- **Verdict for 2023:**
  - 5 of 6 Indonesia-only measures of buying through platforms grew less than household spending (+9.4% nominal), and 3 fell: Tokopedia -8.9%, GoTo on-demand -10.5%, Bank Indonesia's e-commerce figure -4.7%. Momentum Works +3.5%, Bukalapak +6.9%; Blibli +34.7% is the one exception.
  - Platform revenue rose fast (Tokopedia +53%, Bukalapak +23%, Blibli 3P +465%), and BPS published +40.6% e-commerce value and +27.4% online sellers.
  - Sellers' own view agrees with the buying measures: existing sellers' online revenue was net up in 2022 (37% up, 24% down) and net down in 2023 (24% up, 32% down; mean reported change -4.3%); lack of demand became the main obstacle (35% to 41%). BPS's own marketplace slice was roughly flat (0-13% across scenarios, 0.2% mid).
  - Exhibit: `exhibits/6_verdict_2023.png` (all Indonesia-only measures, Blibli labelled as the exception).
- **Scope:** Indonesia-only measures, 2023. Group-wide Grab and Sea figures grew strongly in 2024-26 but cover the region or Asia. In 2024-25 Indonesian measures are mixed. No claim that total online buying in Indonesia fell.

## H1 result

- H1 (transaction value and revenue grow in proportion) is rejected for Indonesia.
- Main sample (Tokopedia, Blibli, Bukalapak; 8 comparisons): revenue grew faster in 6 of 8; opposite directions in 2; median growth divergence 38.9 points vs 7.1 for the proposal's 8 foreign platforms; revenue tracked transaction value in 1 of 8 Indonesian comparisons vs 69% abroad.

## Which test carries the weight

- Indonesia and region (5 platforms, adding Grab and GoTo on-demand) vs 27 foreign platforms: Mann-Whitney p = 0.004 (one median per platform), platform shuffle p = 0.022; leave-one-out p = 0.003 to 0.016 (shuffle 0.007 to 0.041).
- Main sample alone, platform shuffle against the proposal's 8 foreign platforms (a different measure, benchmark and statistic from the 5-vs-27 test, not a stricter version of it): p = 0.06 for growth divergence, 0.03 for the take-rate change; without Sea in the benchmark p = 0.008 to 0.017.
- Shared issuer (independent review): Tokopedia and GoTo on-demand both belong to GoTo; grouped as one issuer (two summary rules), the 4-vs-27 comparison gives Mann-Whitney p = 0.003 and exact permutation p = 0.007. Appendix robustness.
- The proposal's p = 0.002 counts comparisons, not platforms; the writing leads with the platform-level results.
- Sea (Shopee) sits in the proposal's foreign benchmark although Indonesia is a main market, and it swings like the Indonesian platforms (median 0.25); keeping it makes the test harder; both versions reported.

## Why it happened (per platform)

- Mechanism: take rate = service fee rate minus customer incentive rate; IFRS 15 deducts incentives from revenue. Revenue can rise without more buying through incentive cuts, fee increases or a change in business mix.
- Grab on-demand 2022-23: take rate +3.9 points, of which +3.5 pricing within rides and deliveries (deliveries 6.8% to 11.7%; rides steady at about 16%) and +0.35 mix: mostly repricing (group scope).
- Tokopedia 2022-23, two views that agree: of the extra Rp2.15 trillion net revenue, 60.5% came from lower incentives (the proposal's 60.6%, rounding) and 39.5% from higher gross fees; per rupiah of transaction value (which fell 8.9%), gross fees rose 21% and incentives fell 25%.
- GoTo on-demand 2024: incentives fell from 11.3% to 5.0% of transaction value while gross fees stayed about 22%; reported for the whole segment, so rides vs food cannot be separated.
- Blibli 2022-23: take rate 0.32% (4Q22) to 2.07% (1Q23); releases attribute the revenue rise partly to tiket.com travel and digital products inside the same segment and partly to "optimization of discounting"; no reclassification reported; part pricing, part mix, not separable.
- Bukalapak: group-level reporting including Mitra (offline); mix not separable.
- Across 7 Indonesian windows: incentive cuts the larger part in 4, fee increases in 2 (Tokopedia 2022-23, Blibli 2022-25), about equal thirds in 1 (Grab 2021-24).

## When, and why then

- The large take-rate changes came in 2022-24: Grab and Blibli in 2022-23, GoTo in 2024. Since then: Grab on-demand flat at 13-14% (from 1Q23); GoTo on-demand 16.8% to 20.6% (2024-26); Blibli 2.3% to 3.4% (2023-25).
- The quarterly H1 test was falsified (p = 0.19): it mostly covers the calmer period. H1's rejection describes a repricing period; this is part of the result.
- The 2022-24 swings are specific to the Indonesian and regional platforms: all 4 swung more in 2022-24 than in other years (median 0.32 vs 0.06), while foreign platforms in lower-income markets did not (1 of 7) and neither did high-income ones (5 of 14) (exploratory, `timing_check.py`). So "the end of cheap money worldwide" does not explain it on its own. Listing alone does not either: foreign platforms' take rates do not swing more within 3 years of listing (median 0.070) than later (0.084; Wilcoxon p = 0.24; exploratory, `listing_check.py`). The Indonesian and regional platforms made their largest move 1 year after listing (Bukalapak 2022, Grab 2022, Tokopedia 2023, Blibli 2023) or 2 years (GoTo on-demand 2024).
- What the four share: all listed in 2021-22 (Bukalapak 6 Aug 2021, Grab 2 Dec 2021, GoTo 11 Apr 2022, Blibli 7 Nov 2022) and repriced soon after, while incentives were still large. An observation on four firms, not a test: what is specific to them is the combination of listing at the 2021-22 peak with very large incentives, then repricing within one to two years during the 2022-23 tech winter. Literature: Jain and Kini (1994) document changes in operating performance after IPOs (context only); no academic study of platforms cutting incentives after listing was found; news reports describe the pressure on Indonesian tech firms to show profits in the 2022-23 tech winter.

## How general

- Some foreign platforms swing as much (Alibaba, Mogu, Jumia, Ozon, Sea), mostly young platforms in lower-income markets (exploratory, formed after seeing data; holds without Indonesia).
- Not a universal law: spin-off tests S1 and S2 falsified.
- The timing is local: the 2022-24 repricing is an Indonesian and regional episode.

## Objections and answers

- Tiny take rates make changes look big: the question is whether revenue tracks transaction value; a take rate from 1.5% to 2.5% does mean revenue grows two-thirds faster; small take rates alone do not create swings (Shopify about 3%, barely moves).
- Constructed figures: Grab and Shopee kept out of the main sample; Grab enters the wider comparison as a labelled group-scope series.
- Tokopedia has one comparison: leave-one-out shows the result does not depend on it.
- Business mix, not pricing: Grab mostly pricing; Blibli, Bukalapak and GoTo not separable, stated.

## What H1 does and does not conclude

- Does: in 2022-24, Indonesian platform revenue was not a fair guide to the commerce platforms carried, because the take rate moved a lot, mostly through incentive cuts and fee increases.
- Does not: that revenue is unreliable at all times; that platforms everywhere behave this way; why incentives were cut (listing and the 2022-23 pressure are observations and reports, not tests); that total online buying in Indonesia fell.

## Role in the thesis

- H1 is the foundation: it proves the problem on the number people quote most (company revenue) and shows the "what it covers vs how it counts" test working where both parts are visible, before the same test is applied to BPS's seller count.
- H1 is also the live part: the ride-hailing commission cap and the discount rule act on the take rate; pre-registered predictions are scored from 27 Oct 2026.
- In the writing: solid and short.

## Compared with the proposal

- Same: verdict, test, main sample, 60.6% for Tokopedia.
- Added: Objective 1 restated with the separate jobs of the invisible wedge (size) and growth divergence (reliability); the 5-vs-27 comparison carries the weight; the strict platform-level test reported; cause per platform (Grab pricing, Tokopedia two views, GoTo 2024, Blibli partly mix); the 2022-24 repricing period, local to Indonesian and regional platforms; the general pattern and its limits; the 2023 verdict on buying, sellers' reports, revenue and the official count.

## Dated notes

- **8 Oct 2026, after version 3.** (1) Objective 1 over time (`wedge_over_time.py`): for Tokopedia, Blibli and Bukalapak the wedge is 97-99% of transaction value in every year and grows with it, while revenue swings on its own. (2) **What markets did (M1-M2, pre-registered 8 Oct before the market values were pulled; `m1_market_value.py`, ledger v12).** Across 28 listed platforms (138 firm-years, whole-company figures), changes in market value move with transaction-value growth (b1 = 0.60, p = 0.002; M2 holds): an association, not a causal valuation response. Revenue growth from a higher take rate has a smaller point estimate (b2 = 0.33), but the difference is not significant (p = 0.20; M1 falsified); it is significant only with the segment series added (p = 0.004), which mixes segment figures with group market values. Market-value changes include share issuance, so this is not a stock-return result. Comparing revenue multiples with transaction-value multiples is arithmetic (market value cancels; the gap equals the take-rate change), so it illustrates the choice of denominator and is not evidence about investors (independent review, 8 Oct).
- **9 Oct 2026, what "moved three times more" means (`h1_points_vs_log.py`, `tables/h1_points_vs_log.json`; exploratory, formed after the H1 results, prompted by the oral question on the wedge vs D).** The H1 metric is the relative change in the take rate (log points), which is what growth divergence measures. In points of transaction value, Indonesian platforms changed their take rate by about as much as foreign platforms (firm medians about 1.0 point a year in both; one-sided Mann-Whitney p = 0.65), while in relative terms the gap stands (0.20 vs 0.06, p = 0.003). The difference is the level: median take rate 1.6% for the Indonesian firms vs 16.9% abroad (on-demand: Grab 7.5%, GoTo 10.6%, which also moved more in points). Since D = change in m / m, a one-point change moves revenue growth by about 100/m percent (1 + E). Reading: H1 stands; the reason is mainly a thin slice amplifying ordinary pricing changes, which is the role of the wedge. Plain wording changes from "changed their prices far more" to "the same price changes on a much thinner slice".
