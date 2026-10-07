# Part 3: H1, inside the platforms (groundwork, 7 Oct 2026)

**Status: FROZEN 7 Oct 2026** (git tag `part-3-groundwork-frozen-2026-10-07`). Groundwork only: points for the writing stage, not prose. Changes only as dated notes at the end.
Builds on `PART1_PROBLEM_AND_STAKES.md` and `PART2_FRAMEWORK.md` (Level 1). Numbers: `h1_extended.py`, `build_numbers.py` (`test_battery.csv`), `h1_quarterly.py`, `growth_decomposition.py`, `wedge_split.py`, `h1_groundwork.py`; checked by claims ledgers v1 to v6.

## Punchline and verdict

- **Punchline (whole thesis, H1 is the first half):** Indonesia's two biggest online-economy growth stories, platform revenue booming and online sellers surging, were in large part about how things were counted, not about more buying or more sellers.
- **Verdict for 2023 (the year of the official boom):**
  - 5 of 6 Indonesia-only measures of buying through platforms grew less than ordinary household spending (+9.4% nominal), and 3 of them fell: Tokopedia -8.9%, GoTo on-demand -10.5%, Bank Indonesia's e-commerce figure -4.7%. The others: Momentum Works +3.5%, Bukalapak +6.9%. Blibli +34.7% is the one exception.
  - In the same year, platform revenue rose fast (Tokopedia +53%, Bukalapak +23%, Blibli 3P +465%), and BPS published +40.6% e-commerce value and +27.4% online sellers.
  - BPS's own survey answers allow at most about +15.5% more online sellers from entry (less if any sellers stopped), and the typical seller already online did not grow (24% up, 44% unchanged, 32% down).
  - So the boom in revenue and in the official seller count was not matched by the buying that platforms themselves record.
- **Scope of the verdict:** Indonesia-only measures, 2023. Group-wide Grab and Sea figures grew strongly in 2024-26 but cover the region or Asia, not Indonesia. In 2024-25 Indonesian measures are mixed (most below household spending; GoTo on-demand +16.1% in 2024 and e-Conomy +14.5% in 2025 above it). No claim that total online buying in Indonesia fell.

## H1 result

- H1 (transaction value and revenue grow in proportion) is rejected for Indonesia.
- Main sample (Tokopedia, Blibli, Bukalapak; 8 comparisons): revenue grew faster in 6 of 8; opposite directions in 2; median growth divergence 38.9 points vs 7.1 for the proposal's 8 foreign platforms; revenue tracked transaction value in 1 of 8 Indonesian comparisons vs 69% abroad.

## Which test carries the weight

- The weight sits on Indonesia and region (5 platforms, adding Grab and GoTo on-demand) vs 27 foreign platforms: Mann-Whitney p = 0.004 (one median per platform), platform shuffle p = 0.022; leave-one-out p = 0.003 to 0.016 (shuffle 0.007 to 0.041).
- Main sample alone, platform shuffle (strictest): p = 0.06 for growth divergence, 0.03 for the take-rate change; without Sea in the benchmark p = 0.008 to 0.017.
- The p = 0.002 in the proposal counts comparisons, not platforms. The writing leads with the platform-level results.
- Sea (Shopee) is in the proposal's foreign benchmark although Indonesia is a main market; it swings like the Indonesian platforms (median 0.25). Keeping it makes the test harder; both versions are reported.

## Why it happened (per platform)

- Mechanism: take rate = service fee rate minus customer incentive rate; IFRS 15 deducts incentives from revenue. Revenue can rise without more buying through incentive cuts, fee increases, or a change in business mix.
- Grab on-demand 2022-23: take rate +3.9 points, of which +3.5 pricing within rides and deliveries (deliveries 6.8% to 11.7%; rides steady at about 16%) and +0.35 mix. Mostly repricing. (Group scope.)
- Tokopedia 2022-23, two views that agree: of the extra Rp2.15 trillion net revenue, 60.5% came from lower incentives (the proposal's 60.6%, rounding) and 39.5% from higher gross fees; per rupiah of transaction value (which fell 8.9%), gross fees rose 21% and incentives fell 25%.
- Blibli 2022-23: take rate 0.32% (4Q22) to 2.07% (1Q23); releases attribute the revenue rise partly to tiket.com travel and digital products inside the same segment and partly to "optimization of discounting"; no reclassification reported. Part pricing, part mix; not separable.
- Bukalapak: group-level reporting including Mitra (offline); mix not separable.
- Across 7 Indonesian windows: incentive cuts the larger part in 4, fee increases in 2 (Tokopedia 2022-23, Blibli 2022-25), about equal thirds in 1 (Grab 2021-24).

## When

- Large take-rate changes in 2021-23. Since then: Grab on-demand flat at 13-14% (from 1Q23); GoTo on-demand 16.8% to 20.6% (2024-26); Blibli 2.3% to 3.4% (2023-25).
- Quarterly H1 test falsified (p = 0.19): it mostly covers the calmer period. H1's rejection describes a repricing period, part of the result.

## How general

- Some foreign platforms swing as much (Alibaba, Mogu, Jumia, Ozon, Sea): mostly young platforms in lower-income markets. Exploratory pattern (formed after seeing data), holds without Indonesia.
- Not a universal law: spin-off tests S1 and S2 falsified.
- Indonesia is a clear case of a wider pattern among young platforms in price-sensitive markets.

## Objections and answers

- Tiny take rates make changes look big: the question is whether revenue tracks transaction value, and a take rate from 1.5% to 2.5% does mean revenue grows two-thirds faster; small take rates alone do not create swings (Shopify about 3%, barely moves).
- Constructed figures: Grab and Shopee kept out of the main sample; Grab enters the wider comparison as a labelled group-scope series.
- Tokopedia has one comparison: leave-one-out shows the result does not depend on it.
- Business mix, not pricing: Grab mostly pricing; Blibli and Bukalapak not separable, stated.

## What H1 does and does not conclude

- Does: in 2021-23, Indonesian platform revenue was not a fair guide to the commerce platforms carried, because the take rate moved a lot, mostly through incentive cuts and fee increases.
- Does not: that revenue is unreliable at all times; that platforms everywhere behave this way; why incentives were cut (reports point to the 2022 funding squeeze; not tested); that total online buying in Indonesia fell.

## Role in the thesis

- H1 is the foundation: it proves the problem on the number people quote most (company revenue), and it shows the "what it covers vs how it counts" test working where both parts are visible, before the same test is applied to BPS's seller count (the newer, more surprising finding).
- H1 is also the live part: the ride-hailing commission cap and the discount rule act on the take rate; the pre-registered predictions are scored from 27 Oct 2026.
- In the writing: solid and short.

## Compared with the proposal

- Same: verdict, test, main sample, 60.6% for Tokopedia.
- Added: the 5-vs-27 comparison carries the weight; the strict platform-level test reported; cause per platform (Grab pricing, Tokopedia two views, Blibli partly mix); the 2021-23 time boundary; the general pattern and its limits; the 2023 verdict on buying vs revenue and the official count.
