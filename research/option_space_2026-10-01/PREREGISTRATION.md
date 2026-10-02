# Pre-registration (written 2 October 2026, before any Q3 2026 result, before any BPS microdata is opened)

The git commit that adds this file is the timestamp. Nothing below may be edited after the first result it concerns is seen. Changes are made only as dated addenda at the end, never as rewrites.
Everything here is exploratory evidence for the frozen proposal's H1 and H2. None of it is a causal claim.

## A. The 8% commission cap (replaces the v1 ranges in `cap_prediction.py`)

**Facts now taken from primary text** (GoTo 2Q26 earnings call transcript and presentation, local copies): the 8% commission applies to two-wheel passenger transport (GoRide) from 1 July 2026. The legal basis GoTo's CEO names is **Ministerial Decree No. 532 of 2026** (Ministry of Transportation), issued one week after the 23 June announcement, following a presidential directive of 1 May. Earlier notes called the instrument "Perpres 27/2026"; that name was never verified and is withdrawn until a primary text is found. GoRide is "roughly 7% of Group net revenue". Management put the adverse on-demand adjusted EBITDA effect at about Rp300bn (second half of 2026) and says volumes were stable. In 2Q26 on-demand net revenue rose 20% "due to product mix changes and rationalization of incentives as we prepared for the implementation of the 8% commission rate", and management is "shifting our emphasis back towards growth" in Q3.

**Baselines (2Q26, last pre-cap quarter):** GoTo on-demand GTV Rp16.7tn (+2% YoY), net revenue Rp3.6tn (+20% YoY), net take 21.6%; 3Q25 GTV Rp16.7tn, net revenue Rp3.2tn. Grab on-demand net take 13.3% (Mobility 14.95%, Deliveries 12.50%); Grab 2Q26 figures are grade B- (summary), to be re-read from the 6-K.

**Calibration from verified history:** Grab on-demand quarter-on-quarter change in net take has sd 0.41 points (max 0.56) since 2023Q2; Mobility 0.37; Deliveries 0.50; sd of (Mobility change minus Deliveries change) 0.48.

| # | Prediction for 3Q26 | Falsified if |
|---|---|---|
| P1 (v2) | GoTo on-demand net take falls versus 2Q26 by 0.3 to 2.5 points (central 1.4: mechanical cap effect 0.9 to 1.4, plus some reinvestment) | it rises, or falls by more than 2.5 |
| P2 | Grab On-Demand net take within -0.6 to +0.4 points of 2Q26 (two-wheel is under 6% of Mobility) | outside that range |
| P3 (v2) | GoTo on-demand GTV YoY between 0% and +12% (management is shifting back to growth) | negative or above 12% |
| P4 | Grab: change in Mobility net take minus change in Deliveries net take is at or below +0.3 points; central -0.7 | above +0.3. Stated power limit: the noise sd is 0.48, so a result between -1.2 and +0.3 cannot separate a cap effect from noise |
| P5 (reinvestment) | GoTo on-demand GTV YoY in 3Q26 is at least +5% (2Q26 was +2%) | below +2% |

v1 ranges (written 1 Oct 2026, commit f855136) are retained in `cap_prediction.py` as superseded: P1 -1.5 to -0.3, P3 0 to +8%. The v2 changes were made on 2 October after reading the primary call text, before any 3Q26 number exists.
Reading rules: P1 and P5 together confirmed means the cap came with reinvestment; P1 confirmed with P5 falsified means the cap passed through to the take rate. Treated segment is GoRide only, but both firms report Mobility as one segment, so any effect is diluted. Scoring uses the published 3Q26 releases (expected November 2026).

## B. "Headroom" and the discount-leverage flag
L = incentives / revenue kept. If every remaining incentive were cut, the net take rate would rise by exactly L (at constant volume and fee). Registered for the thesis: L is reported as headroom with its failures. Its out-of-sample rank correlation (0.195, 18 transitions, 8 firms) is reported as it is, and L is not described as a predictor.
Exploratory claim to be tested only on future quarters: "discount-driven jumps occur only when L was at least 1". Counts so far: 5 of 5 discount-driven moves above 0.20 had L of 1.07 or more; formed after seeing the data, so it counts as in-sample. A new episode counts only if a platform with L below 0.7 shows a discount-driven take-rate move above 0.20 in log terms within a year; one such case falsifies the claim.

## C. National statistics
- BPS marketplace share of e-commerce value (exclusive split) for the next published reference year (2025) will be **at or below 15.79%** (2024 level). Falsified above it.
- PMK 37/2025 marketplace withholding (0.5% of gross turnover; individuals up to Rp500m exempt) is due to start on **1 November 2026** (DJP PENG-46/PJ.09/2026). Registered expectation: the start date slips again (it has moved from 14 July 2025 to 1 October to 1 November 2026). Falsified if collection starts on 1 November 2026.

## D. BPS microdata estimands (apply only if the files are bought; the 2023 file is the reference)
Files: "Survei E-Commerce 2023" (questions refer to **2022**) and "Survei Usaha/Perusahaan E-Commerce 2024" (refer to **2023**). The 2024 file has no revenue amounts or brackets; the 2023 file has revenue brackets (KATEGORI_P: under Rp300m; Rp300m to 2.5bn; Rp2.5 to 50bn; over Rp50bn).
Online value of a business = bracket revenue x (100 minus offline share R310A) / 100, weighted by W_USAHA_FI. Scenarios for the revenue in each bracket: low 100m, 300m, 2.5bn, 50bn; mid 150m, 1.4bn, 26.25bn, 100bn; high 290m, 2.4bn, 49bn, 500bn (rupiah).
- **Validation (decided before opening):** the mid-scenario total must lie within 0.5x to 2.0x of BPS's published 2022 total of Rp783tn. If it does not, no point estimates are reported, only the low-to-high range, and the paper says the public file is too coarse.
- **E1** Share of online value held by businesses with no financial statements (R306 = 2). Expectation: below the count-based 84.81% (value concentrates in larger firms). Falsified if the mid-scenario share is above 84.81%.
- **E2** Marketplace share of online value in 2022 (R310B). Expectation: above the published 2023 figure of 18.23%. Falsified if below.
- **E3** (2024 file, counts only) Weighted share of businesses selling through Shopee at or above the share through Tokopedia.
- **E4** Entrants: among businesses that began selling online in 2020 or later, the share selling via instant messaging or social media is at least as large as among businesses that began before 2020. Falsified otherwise.
Result reporting: all four reported whatever the sign. No change to scenarios after opening.

## E. What is deliberately not pre-registered
Stock-return tests (null), the analyst-consensus tests (inconclusive), any size for the shadow economy, and any causal reading of the political timing table.

## Addenda
(none yet)
