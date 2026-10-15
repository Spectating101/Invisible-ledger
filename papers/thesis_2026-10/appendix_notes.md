# Appendices to Chapters 4 and 5 (working draft, 13 Oct 2026)

Holds the detail that the main text points to. Every number comes from a committed table named in the notes. Nothing here changes a result in Chapter 5.

## Appendix A. Platforms, windows and the wedge by year

### A.1 The foreign group (27 platforms)

Pairs are consecutive years that pass the rules of Chapter 4, section 4.1: for the platforms added, the later year is not one in which own goods exceed half of revenue; for the eight chosen first, the reporting scope did not change. Ozon's one pair starts in a year that fails the own-goods rule (Appendix B). The median is the platform's median size of yearly change in log take rate. Platforms are shown by the ticker or name used in the panel (`tables/spinoff_panel.csv`, `tables/transitions_master.csv`); full company names are to be added.

| Platform | Chosen first or added | Pairs | Median size of yearly change in log take rate |
|---|---|---|---|
| ACVA | Added | 5 | 0.15 |
| ASAPQ | Added | 6 | 0.10 |
| BABA | Added | 7 | 0.21 |
| DESP | Added | 9 | 0.07 |
| DIBS | Added | 6 | 0.03 |
| EXPE | Added | 11 | 0.03 |
| FVRR | Added | 7 | 0.05 |
| GrubHub | Added | 6 | 0.09 |
| HEPS | Added | 5 | 0.03 |
| KSPI | Added | 4 | 0.08 |
| MOGU | Added | 9 | 0.21 |
| Ozon | Added | 1 | 0.18 |
| PDD | Added | 4 | 0.13 |
| RBA | Added | 11 | 0.06 |
| REAL | Added | 8 | 0.04 |
| SEAT | Added | 6 | 0.07 |
| UPWK | Added | 8 | 0.04 |
| VCSA | Added | 5 | 0.03 |
| YTRA | Added | 11 | 0.03 |
| Etsy | Chosen first | 3 | 0.07 |
| Jumia | Chosen first | 3 | 0.16 |
| Mercado Libre | Chosen first | 2 | 0.06 |
| Rakuten | Chosen first | 1 | 0.02 |
| Sea / Shopee | Chosen first | 7 | 0.25 |
| Shopify | Chosen first | 5 | 0.05 |
| Zalando | Chosen first | 4 | 0.02 |
| eBay | Chosen first | 4 | 0.03 |

Left out after examination: DDL, JD, Jumei, LQDT, NEGG and VIPS (own goods are most of revenue in every year); NBIS, TCOM, TOUR and UXIN (no transaction value disclosed).

### A.2 The Indonesian and regional group

| Platform | Pairs | Median size of yearly change in log take rate | Share of pairs with a change of 0.10 or less |
|---|---|---|---|
| Blibli 3P Retail | 4 | 0.25 | 0.00 |
| Bukalapak Group | 3 | 0.14 | 0.33 |
| GoTo on-demand | 3 | 0.09 | 0.67 |
| Grab on-demand | 4 | 0.20 | 0.50 |
| Tokopedia e-commerce segment | 1 | 0.52 | 0.00 |

### A.3 The seven windows traced (Table 5.4 in full)

Shares are of the log growth of revenue. Source: `tables/growth_decomposition.csv`, built from `tables/l_panel.csv` by `growth_decomposition.py`. Tokopedia, GoTo: audited statements. Grab: annual filings, summed over mobility and deliveries. Blibli: incentives are a proxy (gross profit before discounts less net revenue) and are marked `out` of the main sample in the panel. GoTo's 2022 transaction value is an estimate (2022 first and second quarters backed out of 2023 year-on-year comparisons).

| Platform and window | Growth of revenue (%) | Growth of transaction value (%) | Take rate, start (%) | Take rate, end (%) | More commerce | Higher fees | Lower incentives |
|---|---|---|---|---|---|---|---|
| Grab On-demand, 2021-2024 | 320.5 | 62.3 | 5.34 | 13.83 | 33.7 | 33.8 | 32.5 |
| Grab On-demand, 2022-2024 | 85.8 | 30.1 | 9.69 | 13.83 | 42.5 | 10.6 | 46.9 |
| GoTo On-demand, 2023-2025 | 114.2 | 22.4 | 10.62 | 18.58 | 26.6 | 6.1 | 67.3 |
| GoTo On-demand, 2022-2025 | 110.7 | 9.6 | 9.66 | 18.58 | 12.3 | 36.1 | 51.7 |
| Tokopedia E-commerce, 2022-2023 | 53.2 | -8.9 | 1.48 | 2.48 | -21.9 | 76.5 | 45.4 |
| Blibli 3P Retail, 2022-2025 | 679.4 | 43.6 | 0.54 | 2.92 | 17.6 | 62.6 | 19.8 |
| Blibli 3P Retail, 2022-2023 | 465.3 | 34.7 | 0.54 | 2.25 | 17.2 | 20.1 | 62.7 |

Tokopedia, 2022–23, line by line (Rp million, `tables/tokopedia_segment.csv`): gross revenue 8,143,239 to 8,988,909; incentives 4,112,320 to 2,813,719; net revenue 4,030,919 to 6,175,190. Net revenue rose by 2,144,271, of which lower incentives account for 60.6 percent and higher gross revenue for 39.4 percent (61 and 39 percent in the text).

### A.4 Wedge and ecosystem ratio by platform-year, Indonesian series

Original currency and units, as in the filings: Rp million for Tokopedia and Bukalapak, Rp billion for Blibli, and US$ billion for Grab and Shopee, whose Indonesian amounts are derived or estimated. Shopee's revenue assumes a take rate of 8.4 percent in 2022, 10 percent in 2023 and 10.8 percent in 2024. Table 5.2 converts Tokopedia's 2023 rupiah amounts to US dollars. Take rate and ecosystem ratio carry no currency. Source: `tables/take_rate_levels.csv`.

| Series | Year | Transaction value | Revenue | Wedge | Take rate (%) | Ecosystem ratio | Label |
|---|---|---|---|---|---|---|---|
| Grab | 2021 | 1.88 | 0.08 | 1.80 | 4.20 | 22.8 | conditional country reconstruction |
| Grab | 2022 | 3.83 | 0.28 | 3.55 | 7.19 | 12.9 | conditional country reconstruction |
| Grab | 2023 | 5.38 | 0.60 | 4.78 | 11.24 | 7.9 | conditional country reconstruction |
| Shopee | 2022 | 18.68 | 1.57 | 17.11 | 8.40 | 10.9 | conditional country reconstruction |
| Shopee | 2023 | 21.52 | 2.15 | 19.37 | 10.00 | 9.0 | conditional country reconstruction |
| Shopee | 2024 | 25.99 | 2.81 | 23.18 | 10.80 | 8.3 | conditional country reconstruction |
| Tokopedia e-commerce segment | 2022 | 273,146,166.00 | 4,030,919.00 | 269,115,247.00 | 1.48 | 66.8 | direct indonesia aligned segment |
| Tokopedia e-commerce segment | 2023 | 248,836,156.00 | 6,175,190.00 | 242,660,966.00 | 2.48 | 39.3 | direct indonesia aligned segment |
| Blibli 3P Retail | 2021 | 15,746.00 | 122.00 | 15,624.00 | 0.77 | 128.1 | direct issuer scope pending |
| Blibli 3P Retail | 2022 | 37,050.00 | 199.00 | 36,851.00 | 0.54 | 185.2 | direct issuer scope pending |
| Blibli 3P Retail | 2023 | 49,912.00 | 1,125.00 | 48,787.00 | 2.25 | 43.4 | direct issuer scope pending |
| Blibli 3P Retail | 2024 | 54,210.00 | 1,384.00 | 52,826.00 | 2.55 | 38.2 | direct issuer scope pending |
| Blibli 3P Retail | 2025 | 53,187.00 | 1,551.00 | 51,636.00 | 2.92 | 33.3 | direct issuer scope pending |
| Bukalapak Group | 2020 | 85,081,843.00 | 1,351,664.00 | 83,730,179.00 | 1.59 | 61.9 | direct issuer scope pending |
| Bukalapak Group | 2021 | 122,618,794.00 | 1,869,122.00 | 120,749,672.00 | 1.52 | 64.6 | direct issuer scope pending |
| Bukalapak Group | 2022 | 153,738,958.00 | 3,618,366.00 | 150,120,592.00 | 2.35 | 41.5 | direct issuer scope pending |
| Bukalapak Group | 2023 | 164,380,065.00 | 4,438,269.00 | 159,941,796.00 | 2.70 | 36.0 | direct issuer scope pending |

## Appendix B. The checks on the test of H1

### B.1 The checks

The main test is in Table 5.3. This appendix lists each check with both p-values where both exist. Sources: `h1_extended.py` (`tables/h1_extended_results.json`), `tables/test_battery.csv`, `tables/h1_quarterly_results.json`, `tables/h1_points_vs_log.json`, `tables/h1_thesis_drops.json`. The two rows on how platforms book shopper discounts come from `research/option_space_2026-10-01/materials_2026-10-15/incentive_accounting_check.py` (classification and filing quotes in `INCENTIVE_ACCOUNTING.md`); their shuffle uses a different seed.

| Check | Indonesian and regional (median) | Foreign (median) | Mann–Whitney p | Shuffle p |
|---|---|---|---|---|
| Main test, 5 against 27 | 0.201 | 0.062 | 0.0038 | 0.0221 |
| 5 against the 8 chosen first | 0.201 | 0.055 | 0.0225 | 0.0497 |
| 5 against the 19 added | 0.201 | 0.070 | 0.0046 | 0.0175 |
| Without the 8 foreign platforms that book shopper discounts as marketing costs (exploratory, 15 Oct 2026) | 0.201 | 0.062 | 0.0035 | 0.0066 |
| Only the 11 foreign platforms that deduct shopper discounts from revenue (exploratory, 15 Oct 2026) | 0.201 | 0.075 | 0.0043 | 0.0052 |
| Growth divergence in points, 5 against 26 | 27.0 | 6.5 | 0.0055 | |
| Without Ozon, 26 foreign platforms | 0.201 | 0.060 | 0.0030 | 0.0215 |
| Without Zalando, 26 foreign platforms | 0.201 | 0.064 | 0.0045 | 0.0238 |
| Without Ozon and Zalando, 25 foreign platforms | 0.201 | 0.062 | 0.0036 | 0.0230 |
| Without Blibli 3P Retail | 0.169 | | 0.0137 | 0.0364 |
| Without Bukalapak Group | 0.225 | | 0.0049 | 0.0070 |
| Without GoTo on-demand | 0.225 | | 0.0030 | 0.0071 |
| Without Grab on-demand | 0.194 | | 0.0094 | 0.0166 |
| Without Tokopedia e-commerce segment | 0.169 | | 0.0164 | 0.0409 |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute growth divergence in points | 38.917 | 7.105 | 0.0022 | 0.0606 |
| Three marketplaces against the 8 chosen first, one median per platform, absolute growth divergence in points (claims ledger C47, `build_numbers.py`) | | | 0.0242 | |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute growth divergence in points (without Sea) | 38.917 | 4.192 | <0.0001 | 0.0083 |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute change in log take rate | 0.252 | 0.055 | 0.0037 | 0.0303 |
| Three marketplaces against the 8 chosen first, comparing pairs of years, absolute change in log take rate (without Sea) | 0.252 | 0.033 | 0.0001 | 0.0167 |
| Three marketplaces, dropping Tokopedia's 2022–23 comparison (5 pairs), absolute growth divergence in points | 14.411 | 7.105 | 0.0248 | 0.2222 |
| Three marketplaces, dropping the largest comparison (7 pairs), absolute growth divergence in points | 15.738 | 7.105 | 0.0061 | 0.0606 |
| Three marketplaces against all 40 foreign pairs, absolute growth divergence in points | 38.917 | 7.373 | 0.0014 | 0.0121 |
| Five Indonesian and regional series including constructed Grab and Shopee (12 pairs) against the 8 chosen first, absolute growth divergence in points | 42.017 | 7.105 | 0.0006 | 0.0225 |
| Tokopedia and GoTo on-demand as one company, 4 against 27 | | | 0.003 | 0.007 |
| Quarterly pairs, 3 against 8 (same quarter a year earlier) | 0.071 | 0.049 | 0.19 | 0.33 |

Growth in revenue and growth in transaction value had a correlation of 0.10 in the Indonesian main sample and 0.98 in the foreign sample excluding Sea (`tables/claims_ledger.csv`, C48 and C49).

The quarterly sample is Grab on-demand, GoTo on-demand and Blibli against Sea, Airbnb, Booking, DoorDash, eBay, Etsy, Lyft and Uber. Airbnb and Booking use trailing four-quarter sums because they book revenue at check-in. DoorDash pairs ending in 2025Q4 or later are dropped because of an acquisition.

Details moved from Chapter 5. In the pairs of the Indonesian and regional group, the take rate stayed within about 10 percent (0.10 in log terms) in one third of pairs, against 67 to 69 percent in the foreign groups. The version of the test with growth divergence in points has 26 foreign platforms because Ozon has no pair in which both years pass the own-goods rule. The main test keeps Ozon's pair, whose later year passes, and the first rows above show that dropping it, or Zalando, leaves the result in place.

The comparison in points of the take rate (exploratory, `h1_points_vs_log.py`): median yearly change 1.01 points in the Indonesian and regional group and 0.98 points in the foreign group (26 platforms), Mann–Whitney p = 0.65; median share kept 1.59 percent against 16.93 percent.


### B.2 Where the 2023 break sits (exploratory)

At the top of the size distribution, sellers with revenue above Rp50 billion a year (about US$3.4 million at the 2022 rate) were 0.5 percent of BPS's marketplace sellers in 2022 and held between 18 and 39 percent of the marketplace slice's value, resting on 19 sample rows (`tables/part5_checks.json`).

Across the 34 provinces, count growth had a rank correlation of 0.10 (p = 0.59) with the share of new sellers and 0.35 (p = 0.04) with growth in sample size. In 23 provinces count growth exceeded what entry can explain, and these provinces carry 98.5 percent of the increase. The standard error of the national count implied by BPS's published relative standard errors is about 1.4 percent. The 306 thousand newly counted sellers are about 4.6 times the standard error of the change, and 2.3 times if the true error were twice as large (`tables/bps_frame_check.json`, `tables/rq_closing_checks.json`).

## Appendix C. Registered tests and their outcomes

A registered test was written down, dated and stored in the repository before the data it concerns were opened. The dates are those of the commits in `research/option_space_2026-10-01/PREREGISTRATION.md`. Exact wording and thresholds are in that file.

| Test | What it predicted | Registered | Outcome |
|---|---|---|---|
| E1 | Sellers without financial statements hold a smaller share of online value than of the count | 2 Oct 2026 | Holds, as a range (25.7 to 40.4 percent of value against 79.3 percent of the count) |
| E2 | The marketplace share of online value in 2022 is above the published 2023 figure | 2 Oct 2026 | Holds, as a range (22.6 to 25.6 percent) |
| E2b, E2c | Marketplace use did not rise between 2020 and 2024 | 2 Oct and 3 Oct 2026 | Hold (21.6, 19.8, 17.8 and 17.2 percent) |
| E3 | Shopee reaches at least as many sellers as Tokopedia | 2 Oct 2026 | Holds (7.5 against 2.2 percent of all sellers) |
| E4 | Entrants use chat or social media at least as often as earlier sellers | 2 Oct 2026 | Holds, with no power (nearly everyone uses them) |
| E5 | At least 21.5 percent of 2023 sellers began in 2023 (the entry test) | 2 Oct 2026 | Falsified (13.45 percent) |
| E6 | The median change in sales of sellers already online is at most 10.36 percent | 2 Oct 2026 | Holds (median 0 percent) |
| E7 | The share of value held by sellers without statements fell by at most 5 points from 2020 to 2022 | 3 Oct 2026 | Falsified, narrowly (5.8 points; 3.3 on the second version) |
| E8 | Sellers with revenue of Rp300 million a year or more hold over half of marketplace value | 3 Oct 2026 | Holds (92.2 percent, middle scenario, an upper bound) |
| RBI | The marketplace part sold to final consumers is below Bank Indonesia's 2022 figure | 3 Oct 2026 | Holds in the low (0.16) and middle (0.68) scenarios; fails in the high one (1.62) |
| W1, W2 | Unregistered firms using social media keep written records and take digital payments more often | 3 Oct 2026 | Hold (29.9 against 12.3 percent; 11.5 against 2.7 percent) |
| W3 | Their mean annual sales are below Rp100 million (about US$6,600) | 3 Oct 2026 | Falsified (mean Rp111 million; median Rp60 million) |
| F1, F2 | Formal firms with a website take more e-payments and file taxes online more often | 3 Oct 2026 | Hold |
| F3, X3 | More than one third of formal firms have neither a website nor online tax filing, and Indonesia's share is the highest of the countries compared | 3 Oct 2026 | Hold (39.9 percent; Malaysia 9.1, Thailand 8.7) |
| X2 | Firms with a website file taxes online more often, in at least 3 of 4 countries | 3 Oct 2026 | Holds in 4 of 4 |
| Q1 | The test of H1 with quarterly pairs rejects H1 | 7 Oct 2026, before it was run, but after the quarterly series had been built and the annual result was known, so it is a robustness check | Falsified (p = 0.19) |
| M1 | Markets value growth from more transactions more than growth from a higher take rate | 8 Oct 2026, before the market values were pulled | Falsified in the main sample (p = 0.20) and when trimmed (p = 0.16); holds in the second run of 34 platforms (p = 0.004), which mixes segment figures with whole-company values |
| M2 | Market value moves with transaction value | 8 Oct 2026 | Holds (p = 0.002) |
| P1 to P5, R1 to R3 | Predictions on the third-quarter 2026 results of GoTo, Grab and Sea | 2 and 3 Oct 2026 | Not yet scored; first results are due on 27 Oct 2026 |
| Marketplace tax start | The tax start slips again | 2 Oct 2026 | Withdrawn: collection began on 1 Oct 2026, before the prediction was registered (addendum of 15 Oct 2026) |
| BPS marketplace share | The next published marketplace share is at most 15.79 percent | 2 Oct 2026 | Not yet scored |

## Appendix D. The values behind Figures 5.3 to 5.5

**Growth in 2023, percent (Figure 5.3).** Household spending +9.4; Tokopedia transaction value −8.9; GoTo on-demand transaction value −10.5 (rests on an estimated 2022 value); Bank Indonesia e-commerce −4.7; Momentum Works marketplace estimate +3.5 (calculated from its published levels; its 2024 release states 3.7); Bukalapak transaction value +6.9; Blibli third-party retail transaction value +34.7; Tokopedia revenue +53.2; BPS e-commerce value +40.6; BPS online sellers +27.4. Sources: `tables/consistency_grid_growth.csv`, `tables/yardsticks_bi_bps.csv`, `tables/wedge_over_time.csv`, `tables/h1_groundwork.json`, company filings.

**Who the extra sellers were, percent (Figure 5.4).** Share of the 2022 count and share of the extra count: business opened before 2010, 18.3 and 40.5; owner aged 50 or over, 28.9 and 41.2; outside Java, 23.6 and 36.3; food and lodging or making goods, 38.5 and 53.0. Source: `tables/bps_newly_counted_profile.json`.

**Marketplace use and financial statements, percent of sellers (Figure 5.5).** Marketplace use: 21.6 (2020), 19.8 (2022), 17.8 (2023), 17.2 (2024, published). Complete financial statements: 23.5 (2020), 20.7 (2022), 15.2 (2023). Source: `tables/bps_descriptives.json`.

The figures are drawn by `papers/thesis_2026-10/figures/make_figures.py` from committed tables only. The palette is the reference categorical palette (blue and orange). Colour carries the same meaning in each figure only where a legend or label says so.
