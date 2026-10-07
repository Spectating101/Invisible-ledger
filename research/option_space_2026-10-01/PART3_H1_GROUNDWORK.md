# Part 3: H1, inside the platforms (groundwork, version 2, 8 Oct 2026)

**Status: FROZEN 8 Oct 2026, version 2** (git tag `parts-1-4-v2-frozen-2026-10-08`). Version 2 folds in the dated notes of 8 Oct; version 1 is at tag `part-3-groundwork-frozen-2026-10-07`. Groundwork only: points for the writing stage. Further changes only as dated notes at the end.
Builds on `PART1_PROBLEM_AND_STAKES.md` and `PART2_FRAMEWORK.md` (Level 1). Numbers: `h1_extended.py`, `build_numbers.py` (`test_battery.csv`), `h1_quarterly.py`, `growth_decomposition.py`, `wedge_split.py`, `goto_on_demand.py`, `h1_groundwork.py`, `timing_check.py`, `gel_checks.py`; checked by claims ledgers v1 to v8.

## Punchline and verdict

- **Punchline (whole thesis, H1 is the first half):** Indonesia's two biggest online-economy growth stories in 2023, platform revenue booming and the official count of online sellers surging, were in large part about how things were counted, not about more buying or more sellers.
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
- Main sample alone, platform shuffle (strictest): p = 0.06 for growth divergence, 0.03 for the take-rate change; without Sea in the benchmark p = 0.008 to 0.017.
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
- The 2022-24 swings are specific to the Indonesian and regional platforms: all 4 swung more in 2022-24 than in other years (median 0.32 vs 0.06), while foreign platforms in lower-income markets did not (1 of 7) and neither did high-income ones (5 of 14) (exploratory, `timing_check.py`). So "the end of cheap money worldwide" does not explain it on its own.
- What the four share: all listed in 2021-22 (Bukalapak 6 Aug 2021, Grab 2 Dec 2021, GoTo 11 Apr 2022, Blibli 7 Nov 2022) and repriced soon after, while incentives were still large. An observation on four firms, not a test. Literature: Jain and Kini (1994) document changes in operating performance after IPOs (context only); no academic study of platforms cutting incentives after listing was found; news reports describe the pressure on Indonesian tech firms to show profits in the 2022-23 tech winter.

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
- Added: the 5-vs-27 comparison carries the weight; the strict platform-level test reported; cause per platform (Grab pricing, Tokopedia two views, GoTo 2024, Blibli partly mix); the 2022-24 repricing period, local to Indonesian and regional platforms; the general pattern and its limits; the 2023 verdict on buying, sellers' reports, revenue and the official count.

## Dated notes

- **8 Oct 2026, after version 2 (exploratory, `listing_check.py`).** The listing link tested on the foreign firms: their take rates do not swing more within 3 years of listing (median 0.070) than later (0.084; 9 of 15 larger, Wilcoxon p = 0.24). So listing alone is not a general cause. The Indonesian and regional platforms made their largest move 1 year after listing (Bukalapak 2022, Grab 2022, Tokopedia 2023, Blibli 2023) or 2 years (GoTo on-demand 2024). Neither the end of cheap money worldwide nor listing alone explains it; what is specific to them is the combination: listing at the 2021-22 peak with very large incentives, then repricing within one to two years during the 2022-23 tech winter. Descriptive, not a tested cause.
