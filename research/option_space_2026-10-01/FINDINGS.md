# Findings: the whole thesis evidence in one place (7 Oct 2026)

This file gathers every result the thesis will use. It follows the order of the approved 27 September proposal: same title, same question, same H1 and H2, same measures. Nothing here changes the concept.
Every number below is recomputed by a claims ledger (`tables/claims_ledger*.csv`, all PASS) or comes from the proposal itself. Pre-registered tests and their verdicts are in `PREREGISTRATION.md`. Licensed data (BPS, World Bank, LSEG) is never committed; only weighted totals are.

**Read with** `PART1_PROBLEM_AND_STAKES.md` (problem and why it matters) and `PART2_FRAMEWORK.md` (the framework: what each indicator covers and how it counts; frozen 7 Oct 2026).

**The thesis in one sentence.** Indicators of Indonesia's online economy move with both what they cover and how they count it; in 2022-24, much of the movement in platform revenue, and in 2023 much of the rise in the official count of online sellers, came from how they count, not from the activity.

**Words used once and kept.** V = transaction value, everything sold through a platform (the firm's GMV, GTV, TPV or bookings). R = revenue, what the platform keeps. m = R / V, the platform's cut. W = V - R, the wedge: the part of the sales that revenue does not show. E = W / R. D = growth of R minus growth of V.

## The verdict for 2023 (the year of the official boom)

5 of 6 Indonesia-only measures of buying through platforms grew less than household spending (+9.4%), and 3 fell (Tokopedia -8.9%, GoTo on-demand -10.5%, Bank Indonesia -4.7%). In the same year platform revenue rose fast (Tokopedia +53%) and BPS published +40.6% e-commerce value and +27.4% online sellers, while its own survey answers allow at most about +15.5% more sellers from entry and show the typical existing seller flat. Sellers themselves named lack of demand as their main obstacle in 2023 (41%, up from 35% in 2022; 58% among those whose online revenue fell), and existing sellers' own reports turned from net up in 2022 (37% up, 24% down) to net down in 2023 (24% up, 32% down). Exhibit `6_verdict_2023.png`. On BPS's value figure: newly counted sellers account for about 15-17% of the published increase and entrants about 25-30% (scenarios); the remaining 53-59% would have to come from existing sellers, who reported a mean change of -4.3% in online revenue. Where indicators measure the same slice (marketplaces), they roughly agree on slow growth; the disagreement sits outside marketplaces. Details and limits: `PART3_H1_GROUNDWORK.md`, `PART4_H2_GROUNDWORK.md` (`h1_groundwork.py`, `gel_checks.py`, ledgers v6-v8).

## The answer in five sentences

1. Inside the app, revenue and sales split apart about three times more in Indonesia than abroad (H1 rejected).
2. Revenue moved mainly because platforms raised their cut, by cutting discounts and raising fees (discounts were the larger part in 4 of 7 Indonesian windows, fees in 2); the wedge itself moved with sales.
3. Rulers that see only the apps say the online economy grew about 5% a year; BPS, the one Indonesia-wide count of all online sellers, says much faster, and regional parcel counts point the same way. Part of BPS's growth is its survey design (point 4), so the gap comes from both what each ruler sees and how it counts.
4. National growth on paper came from "more businesses" (H2 holds on BPS's published numbers), but BPS's own survey answers show most of the 2023 jump was not new sellers: it was more sellers being counted.
5. Most sellers keep no books and leave no digital trail, and the share keeping books is falling; the new marketplace tax can reach most of the money but few of the sellers.

## 1. How big is the wedge? (Objective 1)

- 2023, three platforms (Shopee, Tokopedia, Grab Indonesia): V US$43.23bn, R US$3.16bn, W US$40.07bn, E = 12.7 (proposal Table 5).
- The wedge is about 2.9% of Indonesia's 2023 GDP in size only; it is sales, not value added.
- Shopee's assumed cut of 9-11% moves W only between US$39.86bn and US$40.29bn; dropping any one platform leaves at least US$20.70bn (proposal section 5.1).
- Full platform-year table of m and E: `tables/take_rate_levels.csv`.

## 2. Inside the app: H1 (do V and R grow together?)

- Main sample (Tokopedia, Blibli, Bukalapak; 8 comparisons): median |D| 38.9 points vs 7.1 abroad; Mann-Whitney p = 0.002 (proposal; `tables/test_battery.csv`).
- Bigger benchmark (5 Indonesian and regional firms vs 27 foreign firms): the typical yearly swing in the cut is 0.20 vs 0.06 (log points), firm-level p = 0.004 (`h1_extended.py`).
- Same on the proposal's D measure: 27.0 vs 6.5 points, p = 0.005. Dropping any one Indonesian firm: worst p = 0.016.
- Revenue tracks sales (cut moves less than 0.10) in 12.5% of Indonesian comparisons vs 69% abroad (Fisher p = 0.012).
- Quarterly pairs (proposal section 8): **falsified**, 0.071 vs 0.049, p = 0.19. The Indonesian quarterly data mostly cover 2023-2026, after the big repricing jumps: Grab's cut was flat from 2023, while GoTo's and Blibli's kept rising, but in smaller steps. So the large swings are concentrated in 2022-2024 (GoTo's incentive cut came in 2024); the cut has not been fully stable since. The 2022-24 swings are specific to the Indonesian and regional platforms (all listed in 2021-22), not seen in foreign platforms in lower-income or high-income markets (exploratory, `timing_check.py`).
- **Verdict: H1 is rejected.** Revenue did not grow in proportion to sales in Indonesia's platforms during 2020-2025. The weight rests on the 5-vs-27 platform comparison; the main sample alone gives p = 0.06 under the strictest platform-shuffle test (0.03 for the take-rate change). Grab's 2022-23 rise was mostly repricing (+3.5 of +3.9 points); Blibli's was partly travel mix.
- Why Indonesia (exploratory, formed after seeing data): young platforms in lower-income, price-sensitive markets swing more (0.16 vs 0.05; holds without Indonesia, p = 0.03). It is not a worldwide law: the spin-off tests S1 and S2 were falsified.

## 3. Why the cut moved (Objective 2)

- Revenue growth split into more sales, higher fees and fewer discounts (`growth_decomposition.py`):
  - Grab on-demand 2021-2024: revenue +321%; about one third each from sales, fees and fewer discounts.
  - GoTo on-demand 2023-2025: revenue +114%; 67% from fewer discounts, 27% from sales.
  - Tokopedia 2022-2023: sales -8.9%, revenue +53%; incentives fell 32%.
  - Blibli 3P 2022-2023: revenue +465%; 63% from fewer discounts.
- The wedge vs revenue (`wedge_split.py`): in Indonesia about 96% of each change in the wedge comes from sales volume. For revenue it is the other way round: two thirds of each change comes from the cut (66.5%, vs 26.7% abroad).
- In plain words: **the wedge follows sales; revenue follows the cut.** An investor reading revenue sees pricing decisions, not commerce.
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
  - Only 13.4% of 2023 sellers started selling online in 2023. Even if nobody quit, that explains at most +15.5% seller growth, against the published +27.4% (E5 falsified). In growth terms, at least 40% of the published rise is not explained by entry (a lower bound).
  - Sellers already online had a median change of 0% in online revenue: 24% up, 44% same, 32% down (E6 holds).
  - Same cohorts across surveys (exploratory, `bps_cohort_check.py`): sellers who started selling online by 2020 shrank 9.9% between the 2020 and 2022 surveys (as they should), then grew 6.0% between the 2022 and 2023 surveys. The 2023 survey counts 306 thousand more pre-2023 sellers than the whole 2022 count: 37% of the published rise, net of exits. Direct evidence that the 2023 survey counted existing sellers it had not counted before. The extra sellers were all off-marketplace (chat or social only +13%; marketplace users +0.3%). From 2023 to 2024 the count behaves normally (published 2024 table: pre-2020 sellers -10.2%, at least 754 thousand new sellers against a rise of 584 thousand), so 2023 was a break year, not a permanent bias. See `PART4_H2_GROUNDWORK.md`.
- **What this means for H2:** the 2022-2023 "more businesses" is largely more businesses counted, not more businesses selling. H2 still holds as arithmetic on BPS's numbers. Its meaning changes: national growth on paper came from wider counting more than from new sellers or existing sellers growing. The thesis states this plainly, as registered.

## 6. Channels and records (the proposal's two additional analyses)

- Channels: in 2023-2024 BPS's marketplace value grew 1.45% and other channels 20.57%, so 98.5% of the increase was outside marketplaces (published).
- Marketplace use fell each time it was measured: 21.6% of sellers (2020), 19.8% (2022), 17.8% (2023), 17.2% (2024, published).
- BPS's "marketplace" is mostly food and ride apps: among its marketplace sellers in 2023, 45% use Gojek, 42% Shopee, 42% Grab, 13% Tokopedia.
- Records: 28.6% of marketplace sellers keep complete financial statements vs 12.3% of others (published; the microdata reproduces this exactly).
- The share keeping financial statements fell: 23.5% (2020), 20.7% (2022), 15.2% (2023). The 2022-23 step partly reflects who was newly counted: within the same pre-2020 cohort the share went from 23.4% to 16.8% between surveys, as chat-only sellers were added; the 2020-22 decline happened while coverage was stable.
- Sellers without financial statements hold 30-40% of 2022 online value (E1, range consistent with BPS's own total).
- Unregistered firms (World Bank, six cities, 2023): 27% sell through social media; their median sales are Rp60m a year; 70% keep no written records.
- Formal firms: 39.9% in Indonesia have neither a website nor online tax filing, the highest of seven Southeast Asian countries (Malaysia 9.1%, Thailand 8.7%, Viet Nam 0.4%).

## 7. Why it matters: the state (proposal section 6)

- 2023-2026 policy acts on these numbers: the 8% ride-hailing cut cap, the June 2026 discount rule, the marketplace tax (PMK 37/2025), the data-handover rule and the 2026 census (34 events in `tables/src/policy_timeline_web.csv`; most are news-sourced, see its status column).
- The marketplace tax base differs about 5x by ruler: Rp204tn (BPS marketplace) to Rp983tn (e-Conomy). At 0.5% that is Rp1.0-4.9tn, 0.04-0.21% of the 2026 tax target.
- Who the tax reaches (E8): sellers with Rp300m+ a year are 28% of marketplace sellers but hold 77-92% of marketplace value. So the tax can reach most of the money while exempting most sellers. It is small money; its larger effect is records.
- Scope rule: we criticise only platform-economy numbers we tested. No causal claims about policy.

## 8. What failed (reported, not hidden)

S1 and S2 (spin-off: not a worldwide law); W3 (informal sellers' mean sales above Rp100m; median Rp60m); E5 (entry too small for BPS's count growth); E7 (records share of value fell 5.8 points, limit 5); Q1 (quarterly H1); the discount-leverage rule is too thin out of sample. Coding fixes were disclosed (j36, S3, E6 wording).

## 9. Limits (stated once, in the limitations chapter)

- Small sample: 3 main platforms, 8 comparisons. With one result per firm, a firm-label shuffle gives p = 0.06 for the main sample alone; the 5-vs-27 version gives p = 0.004.
- Grab's and Shopee's Indonesian figures are constructed; Grab's quarterly data are group-wide.
- BPS revenue comes in brackets. Our bracket values overshoot BPS's total, so value shares are ranges, not points.
- BPS's 2024 file does not release revenue amounts; the 2023 file has no business ID to follow sellers over time.
- World Bank informal data cover six cities, not the nation.
- Rulers measure different things; we compare growth, not levels, except where definitions were reconciled.
- Policy texts: Perpres 27/2026 and parts of the timeline are news-sourced until the primary texts are read.

## 10. Still open (dated)

| Date | What | File |
|---|---|---|
| 27 Oct 2026 | GoTo 3Q26: score P1-P5, R1, R2 | `score_q3_2026.py`, `cap_prediction.py` |
| 1 Nov 2026 | Does the marketplace tax start on time? (registered: it slips again) | `PREREGISTRATION.md` section C |
| early Nov 2026 | BPS 3Q26 GDP: score R2 | `score_q3_2026.py` |
| mid Nov 2026 | Grab and Sea 3Q26: score P4, R3 | `score_q3_2026.py` |
| next BPS release | Marketplace share at or below 15.79% | `PREREGISTRATION.md` section C |
| before writing | Read primary legal texts; check the reference list; get the YZU template | `AGENTS.md` open items |
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
| Exhibits, one per layer | Done (5) | `exhibits.py` |
