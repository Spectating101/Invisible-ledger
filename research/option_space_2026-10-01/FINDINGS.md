# Findings: the whole thesis evidence in one place (updated 8 Oct 2026)

This file gathers every result the thesis will use. It follows the order of the approved 27 September proposal: same title, same question, same H1 and H2, same measures. Nothing here changes the concept.
Every number below is recomputed by a claims ledger (`tables/claims_ledger*.csv`, all PASS) or comes from the proposal itself. Pre-registered tests and their verdicts are in `PREREGISTRATION.md`. Licensed data (BPS, World Bank, LSEG) is never committed; only weighted totals are.

**Read with** the groundwork files, one per chapter: `PART1_PROBLEM_AND_STAKES.md` (problem, who uses the numbers), `PART2_FRAMEWORK.md` (what each indicator covers and how it counts), `PART3_H1_GROUNDWORK.md` (H1), `PART4_H2_GROUNDWORK.md` (H2, channels and records), `PART5_OBJ3_GROUNDWORK.md` (comparing the indicators), `PART6_WHY_IT_MATTERS_GROUNDWORK.md` (the 2026 rules and how far each reaches), `PART7_ANSWER_AND_LIMITS.md` (answer to the research question, what failed, limits). Chapter order: Objective 1 and H1, H2, Objective 3, why it matters, conclusion. Groundwork version 3, tag `parts-1-7-v3-frozen-2026-10-08`.

**The thesis in one sentence.** Each indicator of Indonesia's online economy is a fair guide to another only while a condition holds: revenue tracks transaction value while the take rate is steady, and a survey's seller count tracks entry while its coverage and sellers' participation are steady. In 2022-24 the platforms' take rates moved, so revenue grew far faster than the commerce it carried; in 2023 about half of the rise in BPS's count of online sellers (37-56%) is not explained by first-time entry, which points to wider survey coverage of chat-and-social sellers.

**Words used once and kept.** V = transaction value, everything sold through a platform (the firm's GMV, GTV, TPV or bookings). R = revenue, what the platform keeps. m = R / V, the platform's cut. W = V - R, the wedge: the part of the sales that revenue does not show. E = W / R. D = growth of R minus growth of V.

## The verdict for 2023 (the year of the official boom)

5 of 6 Indonesia-only measures of buying through platforms grew less than household spending (+9.4%), and 3 fell (Tokopedia -8.9%, GoTo on-demand -10.5%, Bank Indonesia -4.7%). In the same year platform revenue rose fast (Tokopedia +53%) and BPS published +40.6% e-commerce value and +27.4% online sellers, while about half of that seller rise (37-56%) is not explained by first-time entry and the typical existing seller was flat. Sellers themselves named lack of demand as their main obstacle in 2023 (41%, up from 35% in 2022; 58% among those whose online revenue fell), and existing sellers' own reports turned from net up in 2022 (37% up, 24% down) to net down in 2023 (24% up, 32% down). Exhibit `6_verdict_2023.png`. On BPS's value figure: sellers not explained by entry account for about 15-17% of the published increase and entrants about 25-30% (scenarios); the remaining 53-59% would have to come from existing sellers, who reported a mean change of -4.3% in online revenue. Where indicators measure overlapping slices (BPS's marketplace slice, which also includes Gojek and Grab food and ride merchants, vs the platform indicators), they agree on slow growth; the disagreement sits outside marketplaces. Details and limits: `PART3_H1_GROUNDWORK.md`, `PART4_H2_GROUNDWORK.md` (`h1_groundwork.py`, `gel_checks.py`, ledgers v6-v8).

## The answer in six sentences

1. Inside the app, revenue and sales split apart about three times more in Indonesia than abroad (H1 rejected).
2. Revenue moved mainly because platforms raised their cut, by cutting discounts and raising fees (discounts were the larger part in 4 of 7 Indonesian windows, fees in 2); the wedge itself moved with sales.
3. Rulers that see only the apps say the online economy grew about 5% a year; BPS, the one Indonesia-wide count of all online sellers, says much faster, and regional parcel counts point the same way. Part of BPS's growth is its survey design (point 4), so the gap comes from both what each ruler sees and how it counts.
4. National growth on paper came from "more businesses" (H2 holds on BPS's published numbers), but BPS's own survey answers show that about half of the 2023 jump in sellers (37-56%) is not explained by first-time entry; the channel and province patterns point to wider survey coverage, with returning sellers the open alternative.
5. Most sellers keep no financial statements (the share fell 2020-22 under stable coverage), and 39.9% of formal firms have neither a website nor online tax filing, the highest of seven countries; about 96% sell through chat or social media and only 13.5% of off-marketplace sellers want to join a marketplace; the new marketplace tax can reach most marketplace value but at most about 5% of online sellers.
6. Where the indicators measure overlapping slices (BPS's marketplace slice is 47% shopping-marketplace sellers and 43% only Gojek or Grab merchants), they agree on slow growth; their sizes cannot be reconciled (platform GMV counts shipping, digital goods, travel and offline sales; BPS's survey is thin at the top, 19 rows for Rp50bn+ sellers).

## 1. How big is the wedge? (Objective 1)

- 2023, three platforms (Shopee, Tokopedia, Grab Indonesia): V US$43.23bn, R US$3.16bn, W US$40.07bn, E = 12.7 (proposal Table 5).
- The wedge is about 2.9% of Indonesia's 2023 GDP in size only; it is sales, not value added.
- Shopee's assumed cut of 9-11% moves W only between US$39.86bn and US$40.29bn; dropping any one platform leaves at least US$20.70bn (proposal section 5.1).
- Full platform-year table of m and E: `tables/take_rate_levels.csv`.
- Over time (`wedge_over_time.py`): for the issuer-reported platforms the wedge is 97-99% of transaction value in every year and grows with it (Blibli 2022-23: transaction value +35%, wedge +32%, revenue +465%; Tokopedia 2022-23: -9%, -10%, +53%).
- Across the online economy (the research question's "how much", second level): in BPS's own survey, its marketplace channel (shopping marketplaces plus food and ride apps) carries about 16-26% of online sales value (22.6-25.6% in 2022, microdata; 18.2% in 2023 and 15.8% in 2024, published). Platform-based measures therefore leave out about three quarters of online sales value (`rq_closing_checks.py`, ledger v11).

## 2. Inside the app: H1 (do V and R grow together?)

- Main sample (Tokopedia, Blibli, Bukalapak; 8 comparisons): median |D| 38.9 points vs 7.1 abroad; Mann-Whitney p = 0.002 (proposal; `tables/test_battery.csv`).
- Bigger benchmark (5 Indonesian and regional firms vs 27 foreign firms): the typical yearly swing in the cut is 0.20 vs 0.06 (log points), firm-level p = 0.004 (`h1_extended.py`).
- Same on the proposal's D measure: 27.0 vs 6.5 points, p = 0.005. Dropping any one Indonesian firm: worst p = 0.016.
- Revenue tracks sales (cut moves less than 0.10) in 12.5% of Indonesian comparisons vs 69% abroad (Fisher p = 0.012).
- Quarterly pairs (proposal section 8): **falsified**, 0.071 vs 0.049, p = 0.19. The Indonesian quarterly data mostly cover 2023-2026, after the big repricing jumps: Grab's cut was flat from 2023, while GoTo's and Blibli's kept rising, but in smaller steps. So the large swings are concentrated in 2022-2024 (GoTo's incentive cut came in 2024); the cut has not been fully stable since. The 2022-24 swings are specific to the Indonesian and regional platforms (all listed in 2021-22), not seen in foreign platforms in lower-income or high-income markets (exploratory, `timing_check.py`).
- **Verdict: H1 is rejected.** Revenue did not grow in proportion to sales in Indonesia's platforms during 2020-2025. The weight rests on the 5-vs-27 platform comparison; the main sample alone gives p = 0.06 on a different test (growth divergence against the proposal's 8 platforms; 0.03 for the take-rate change); grouping GoTo's two segments as one issuer leaves p = 0.003. Grab's 2022-23 rise was mostly repricing (+3.5 of +3.9 points); Blibli's was partly travel mix.
- Why Indonesia (exploratory, formed after seeing data): young platforms in lower-income, price-sensitive markets swing more (0.16 vs 0.05; holds without Indonesia, p = 0.03). It is not a worldwide law: the spin-off tests S1 and S2 were falsified.

- **What markets did (M1-M2, pre-registered 8 Oct before the market values were pulled; `m1_market_value.py`, ledger v12).** Across 28 listed platforms (138 firm-years, whole-company figures), changes in market value move with transaction-value growth (b1 = 0.60, p = 0.002; M2 holds): an association, not a causal valuation response. Revenue growth from a higher take rate has a smaller point estimate (b2 = 0.33), but the difference is not significant (p = 0.20; M1 falsified); it is significant only with the segment series added (p = 0.004), which mixes segment figures with group market values. Market-value changes include share issuance, so this is not a stock-return result. Comparing revenue multiples with transaction-value multiples is arithmetic (market value cancels; the gap equals the take-rate change), so it illustrates the choice of denominator and is not evidence about investors (independent review, 8 Oct).

## 3. Why the cut moved (Objective 2)

- Revenue growth split into more sales, higher fees and fewer discounts (`growth_decomposition.py`):
  - Grab on-demand 2021-2024: revenue +321%; about one third each from sales, fees and fewer discounts.
  - GoTo on-demand 2023-2025: revenue +114%; 67% from fewer discounts, 27% from sales.
  - Tokopedia 2022-2023: sales -8.9%, revenue +53%; incentives fell 32%.
  - Blibli 3P 2022-2023: revenue +465%; 63% from fewer discounts.
- The wedge vs revenue (`wedge_split.py`): in Indonesia about 96% of each change in the wedge comes from sales volume. For revenue it is the other way round: two thirds of each change comes from the cut (66.5%, vs 26.7% abroad).
- In plain words: **the wedge follows sales; revenue follows the cut.** In Indonesia in 2022-24, an investor reading revenue growth was reading pricing decisions more than commerce.
- Discount-leverage rule (pre-registered 2 Oct): it points the right way (2 of 2 high-leverage years moved, vs 10 of 16 others), but there are too few high-leverage cases out of sample to count as evidence.

## 4. Apps vs the nation (Objective 3)

- Eleven rulers of the same online economy (`consistency_grid.py`). In 2024: app-only rulers grew about 5-7% (Momentum Works 5.2%, e-Conomy 5.1%, Bank Indonesia 7.3%). BPS, the only Indonesia-wide count of all online sellers, grew 17.1%. Adjacent rulers point the same way but are not Indonesian e-commerce: Southeast Asia-wide parcels +25.2% (J&T's own SEA parcels +40.8%), and VAT on foreign digital services +24.9%. BPS's growth is partly survey design (section 5), so this gap is part coverage, part counting.
- The two state offices moved in opposite directions in 2023: Bank Indonesia -4.7%, BPS +40.6% (`yardsticks.py`). BPS's level is 1.6x Bank Indonesia's in 2022 and 2.65x in 2024.
- BPS's own microdata reconciles part of this: its marketplace-to-consumer slice for 2022 is only 0.16-0.68x Bank Indonesia's figure (RBI holds). So the gap is not about marketplaces; BPS counts much more outside them.
- Platform sales vs official household spending, by quarter (`three_rulers.py`): GoTo's sales grew slower than nominal household spending in each of the last four quarters (2Q26: sales +2.0%, spending +8.3%), while its revenue grew 20.5%.
- Payment rulers are context only (QRIS +187% in 2024): they include in-person payments and switching from cash.

## 5. Outside the apps: H2 (does national growth come from more businesses?)

- BPS's published numbers, split arithmetically (`bps_bridge.py`, `tables/bps_recompute.json`): more businesses account for 90.3% of 2023-2024 growth (71.0% under BPS's other 2023 count) and 71.0% of 2022-2023 growth.
- **Verdict on the published numbers: H2 holds.**
- BPS's own answers (microdata, 7 Oct; exhibit 5):
  - Only 13.4% of 2023 sellers started selling online in 2023, below the 21.5% the published +27.4% requires even if nobody quit (E5 falsified).
  - Sellers already online had a median change of 0% in online revenue: 24% up, 44% same, 32% down (E6 holds).
  - Same cohorts across surveys (exploratory, `bps_cohort_check.py`): sellers who started selling online by 2020 shrank 9.9% between the 2020 and 2022 surveys (as they should), then grew 6.0% between the 2022 and 2023 surveys. The 2023 survey counts 306 thousand more pre-2023 sellers than the whole 2022 count: 37% of the published rise, net of exits; about 56% if sellers stopped at the 2020-22 rate of about 5% a year (`bps_rise_accounting.py`). The other part of the 819 thousand rise is the 513 thousand sellers who started in 2023. Direct evidence that the 2023 survey counted existing sellers it had not counted before: roughly half the rise. The extra sellers were all off-marketplace (chat or social only +13%; marketplace users +0.3%). From 2023 to 2024 the count behaves normally (published 2024 table: pre-2020 sellers -10.2%, at least 754 thousand new sellers against a rise of 584 thousand), so 2023 was a break year, not a permanent bias. See `PART4_H2_GROUNDWORK.md`.
- **What this means for H2:** the 2022-2023 "more businesses" is about half first-time entry and about half a gap beyond entry among chat-and-social sellers. H2 still holds as arithmetic on BPS's numbers. Its meaning changes: national growth on paper came from first-time entry and a gap beyond it in similar parts, not from the typical existing seller growing. The thesis states this plainly, as registered.

## 6. Channels and records (the proposal's two additional analyses)

- Channels: in 2023-2024 BPS's marketplace value grew 1.45% and other channels 20.57%, so 98.5% of the increase was outside marketplaces (published).
- Marketplace use fell each time it was measured: 21.6% of sellers (2020), 19.8% (2022), 17.8% (2023), 17.2% (2024, published).
- BPS's "marketplace" is about half food and ride apps: of its marketplace sellers in 2023, 43% use only Gojek or Grab and 47% use a shopping marketplace (by app: Gojek 45%, Shopee 42%, Grab 42%, Tokopedia 13%).
- Records: 28.6% of marketplace sellers keep complete financial statements vs 12.3% of others (published; the microdata reproduces this exactly).
- The share keeping financial statements fell: 23.5% (2020), 20.7% (2022), 15.2% (2023). The 2022-23 step partly reflects who was added to the count: within the same pre-2020 cohort the share went from 23.4% to 16.8% between surveys, as chat-only sellers were added; the 2020-22 decline happened while coverage was stable.
- Sellers without financial statements hold 30-40% of 2022 online value (E1, range consistent with BPS's own total).
- Unregistered firms (World Bank, six cities, 2023): 27% sell through social media; their median sales are Rp60m a year; 70% keep no written records.
- Formal firms: 39.9% in Indonesia have neither a website nor online tax filing, the highest of seven Southeast Asian countries (Malaysia 9.1%, Thailand 8.7%, Viet Nam 0.4%).

## 7. Why it matters: the state (proposal section 6)

- 2023-2026 rules each act on one part of what the thesis measures (34 events in `tables/src/policy_timeline_web.csv`, status per row; primary texts in `sources/policy_primary/`): the 8% commission cap on two-wheel ride-hailing (Gojek and Grab rides only; rides are about 36% of Grab's group on-demand GMV); the June 2026 discount rule (customer incentives, the lever behind the take-rate jumps); the marketplace tax (sellers' sales inside marketplaces); the platform-data rule and the 2026 census (BPS's coverage). Full map: Part 6.
- The marketplace tax base differs about 5x by ruler: Rp204tn (BPS marketplace) to Rp983tn (e-Conomy). At 0.5% that is Rp1.0-4.9tn, 0.04-0.21% of the 2026 tax target.
- Who the tax reaches (E8): sellers with Rp300m+ a year are 28% of marketplace sellers but hold 77-92% of marketplace value. Across all online selling, it can collect from at most about 5% of online sellers and about 17-24% of online sales value (2022, upper bounds). It identifies every marketplace seller, exempt or not (PMK 37 Art. 6: tax number or NIK given to the marketplace), about 18% of online sellers; the other four in five are untouched. Small money; its added record covers the marketplace minority only.
- Scope rule: we criticise only platform-economy numbers we tested. No causal claims about policy.

## 8. What failed (reported, not hidden)

S1 and S2 (spin-off: not a worldwide law); W3 (informal sellers' mean sales above Rp100m; median Rp60m); E5 (entry too small for BPS's count growth); E7 (records share of value fell 5.8 points, limit 5); Q1 (quarterly H1); M1 in the main sample (take-rate growth valued below volume growth in the point estimate, not significantly); the discount-leverage rule is too thin out of sample. Coding fixes were disclosed (j36, S3, E6 wording).

## 9. Limits (stated once, in the limitations chapter)

- Small sample: 3 main platforms, 8 comparisons. With one result per firm, a firm-label shuffle gives p = 0.06 for the main sample alone; the 5-vs-27 version gives p = 0.004.
- Grab's and Shopee's Indonesian figures are constructed; Grab's quarterly data are group-wide.
- The 2023 seller-count finding is exploratory; sampling noise is very unlikely to explain it (BPS's published RSEs imply about 1.4% nationally; the surplus is about 4.6 standard errors, 2.3 at twice the RSE), but a frame change cannot be separated from other coverage changes.
- BPS revenue comes in brackets. Our bracket values overshoot BPS's total, so value shares are ranges, not points.
- BPS's 2024 file does not release revenue amounts; the 2023 file has no business ID to follow sellers over time.
- World Bank informal data cover six cities, not the nation.
- Rulers measure different things; we compare growth, not levels, except where definitions were reconciled.
- Policy texts: PMK 37/2025, PENG-46/PJ.09/2026 (via the DDTC mirror), Permendag 19/2026 and 31/2023, Peraturan BPS 4/2023 and PP 20/2026 are read in primary text; Perpres 27/2026 and the transport ministry decree are unpublished or unreachable, so the cap is cited as announced; the rest of the timeline is news-sourced (status per row).

## 10. Still open (dated)

| Date | What | File |
|---|---|---|
| 27 Oct 2026 | GoTo 3Q26: score P1-P5, R1, R2 | `score_q3_2026.py`, `cap_prediction.py` |
| 1 Nov 2026 | Does the marketplace tax start on time? (registered: it slips again) | `PREREGISTRATION.md` section C |
| early Nov 2026 | BPS 3Q26 GDP: score R2 | `score_q3_2026.py` |
| mid Nov 2026 | Grab and Sea 3Q26: score P4, R3 | `score_q3_2026.py` |
| next BPS release | Marketplace share at or below 15.79% | `PREREGISTRATION.md` section C |
| before writing | Check the reference list against the 27 Sep text; get the YZU template (primary legal texts: done, see `sources/policy_primary/MANIFEST.md`) | `../../AGENTS.md` open items |
| after the defense | Send BPS a copy of the thesis (SPPD duty) | - |

## Proposal checklist (every promise and where it is met)

| Proposal promise | Status | Where |
|---|---|---|
| Objective 1: measure W, E, D 2020-2025 | Done | proposal Table 5; `take_rate_levels.csv`; `transitions_master.csv` |
| Objective 2: reconcile big moves with incentives, monetization, recognition, scope | Done | `growth_decomposition.py`, `l_panel.py`, `blibli_discount_split.py`, `v_definition_map.py` |
| Objective 3: compare with national and payment rulers | Done | `consistency_grid.py`, `yardsticks.py`, `three_rulers.py`, `bps_bridge.py` |
| H1 test vs foreign benchmark, one median per firm | Done; rejected | `build_numbers.py`, `h1_extended.py` |
| H2 split for both transitions and both counts | Done; holds on published numbers; meaning qualified by microdata | `bps_bridge.py`, `bps_microdata_tests.py` |
| Channel split and records (additional analyses) | Done, extended to 2020-2024 | `bps_microdata_tests.py`, `bps_descriptives.py`, `wb_tests.py` |
| Section 7 robustness: Shopee rate, drop each platform, drop largest, issuer pairs only | Done | proposal 5.1; `test_battery.csv` |
| Section 8: reconcile BPS and platform levels | Done | `bps_bridge.py`, RBI |
| Section 8: split wedge moves into volume and monetization | Done | `wedge_split.py` |
| Section 8: quarterly pairs | Done; falsified | `h1_quarterly.py` |
| Section 8: alternative sample rules | Done | `h1_regional_tier.py`, `h1_extended.py` (leave-one-out) |
| Section 8: stock-return extension (later) | Exploratory only, not in the thesis core | `event_study*.py` (licensed prices) |
| Exhibits, one per layer | Done (6) | `exhibits.py` |
| Answer to the research question, failures, limits | Done (groundwork) | `PART7_ANSWER_AND_LIMITS.md` |
