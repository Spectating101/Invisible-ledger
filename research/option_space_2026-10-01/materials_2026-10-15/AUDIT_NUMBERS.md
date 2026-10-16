# Number audit of the thesis draft (15 October 2026)

Scope: every number in the prose and tables of `papers/thesis_2026-10/` ch1_introduction.md, ch2_literature.md, ch3_framework.md, ch4_data_methods.md, ch5_results.md, drafts/ch6_draft_2026-10-14.md, drafts/ch7_draft_2026-10-14.md and appendix_notes.md. Line numbers are those of the files as read on 15 Oct 2026. No chapter file was edited. No licensed data were opened. Only committed outputs were used, plus two read-only reruns of scripts that use committed tables alone (`h1_direction_count.py`, and the `growth_decomposition.py` arithmetic at full precision in a scratch session; neither wrote a file).

Sources of truth: `research/option_space_2026-10-01/tables/` (CSV/JSON and claims ledgers `claims_ledger*.csv`, 272 rows, all PASS), `FINDINGS.md`, `PART1`–`PART7` groundwork, `PREREGISTRATION.md`, and `materials_2026-10-15/` (`CH6_SOURCES.md`, `INCENTIVE_ACCOUNTING.md`, `REFERENCE_CHECK.md`). FX: World Bank official rate for the year (`tables/src/worldbank_fx_2022_2024.json`: 2022 Rp14,849.85; 2023 Rp15,236.88; 2024 Rp15,855.45).

Citation years and bibliographic details are not re-audited here (see `REFERENCE_CHECK.md`). Years are counted only where they carry a claim (a period label, an event date, a registration date).

## Summary counts

Items are counted one per number (or per stated range, or per label that carries a number), as listed in the compact list below.

| Category | Count |
|---|---|
| Checked | 920 |
| Match (equal at the stated precision) | 893 |
| Rounding-ok (loose or tie rounding; acceptable, optional tightening noted) | 9 |
| MISMATCH (wrong value, wrong label, or inconsistent with another chapter) | 15 |
| NO SOURCE FOUND | 3 |

By file: ch1 18, ch2 1, ch3 21, ch4 53, ch5 264, ch6 95, ch7 42, appendix 426.

Checks (a) to (d) in brief:
- (a) Round versus activity year: all uses are correct ("survey for 2023" = 2024 file; "survey for 2022" = 2023 file; brackets only in the 2021 and 2023 files). One period label departs from the sources: "2021 to 2024" for the repricing (see M7).
- (b) Every US$ conversion was recomputed at the year's World Bank rate; all pass. Table 5.2 uses 2023; Ch4/Ch6 thresholds use 2022 (and 2024 in the Table 6.1 note, disclosed); Ch5:166 converts 2022 and 2023 at their own rates (so the US$ rise is 37 percent against 40.6 percent in rupiah, which is correct under the rule).
- (c) Cross-chapter consistency: headline values agree everywhere (US$43bn/3bn/40bn, 7 percent, about a fifth, 13.45 against 21.5, 37–56 percent, three times, two thirds against a quarter, 1 in 20, 8 percent, p values). Inconsistencies: M1 (21 percent, wrong in both Ch5 and Ch6), M2 (second-run composition, wrong in Ch4 and Ch5), M4 (appendix says the text uses 61/39; the text says 60/40), M6 (winsorised called trimmed in three places).
- (d) Arithmetic inside sentences: all pass except the reversed pairing in the Table 5.2 note (M8). Passing checks: Table 5.2 sums; Table 5.4 rows add to 99–101; Table 5.5 819 = 513 + 306 = 361 + 458; Ch3:84 0.911 × 0.682 = 0.621; Ch3:90; Ch3:158 27.4/127.4 = 21.5; Ch6:57 17.8 × 0.47 = 8.4; Ch6:53 22.6 × 77.4 = 17.5 and 25.6 × 92.2 = 23.6; Ch7:45 2 × 0.0038 = 0.0076 < 0.01; Ch5:166 100 − 30 − 17 = 53 and 100 − 25.5 − 15.4 = 59.

## MISMATCH and NO SOURCE FOUND

| # | file:line | Text | Source value and file | Fix |
|---|---|---|---|---|
| M1 | ch5:230 | "while its revenue grew by 21 percent" (GoTo on-demand, 2Q26) | Rp3,593bn vs Rp2,987bn = **+20.3%**; GoTo release says +20% (`CH6_SOURCES.md` item 2, appendix table; `PREREGISTRATION.md` §A "+20% YoY"). Ledger v3 R01 = 20.5 comes from the rounded Rp3.6tn (`three_rulers.py` line 7), and even 20.5 does not support "21" | "grew by about 20 percent" |
| M1b | ch6:39 | "on-demand revenue rose by about 21 percent in the second quarter of 2026" | Same: +20.3% (release: +20%) | "by about 20 percent" |
| M2 | ch4:69 | "A second run adds three segment series and three more whole companies" | `m1_market_value.py` lines 24–33 and `PREREGISTRATION.md` (8 Oct): the run adds **five segment series** (Blibli 3P, GoTo on-demand, Grab on-demand, Sea/Shopee e-commerce segment, Rakuten Domestic EC) **and Mercado Libre**; JSON label "main plus segment series and Mercado Libre"; 34 firms, 162 firm-years (`tables/m1_market_value_results.json`) | "A second run adds five segment series and Mercado Libre, for 34 platforms" |
| M2b | ch5:116 | "A second run adds three segment series and three more whole companies" | Same as M2 | Same as M2 |
| M3 | ch6:53 | "So the tax reaches at most 17 to 24 percent of online sales value" | `tables/part6_checks.json` tax_value_reach_pct_2022: low **17.52**, mid 23.58, high 23.38 (ledger v9 T6-01 17.5). 17.52 rounds to 18 | "at most 18 to 24 percent" (or "17.5 to 24") |
| M4 | appendix_notes:67 | "(61 and 39 percent in the text)" | Text says "about 60" and "about 40" (ch1:9, ch5:102); source 60.6/39.4 (ledger C15/C16) | "(about 60 and 40 percent in the text)" |
| M5 | appendix_notes:120 | "Three marketplaces, dropping Tokopedia's 2022–23 comparison (5 pairs)" | `tables/test_battery.csv` row "IDN_main drop 2022-23 (5) vs EXT_clean": drops **all three 2022–23 comparisons** (Blibli, Bukalapak, Tokopedia), leaving 5 pairs from 2 platforms. Dropping only Tokopedia's pair would leave 7. Values 14.411 / 7.105 / 0.0248 / 0.2222 match | "dropping all three 2022–23 comparisons (5 pairs, 2 platforms)" |
| M6 | ch5:16 (Table 5.1) | "Extreme values trimmed" | The robustness run winsorises dlnMV, dlnV and dlnm at the 5th and 95th percentiles (`PREREGISTRATION.md` 8 Oct; JSON key `robust_winsorised_5_95`); no observation is dropped (still 138 firm-years) | "Extreme values capped (winsorised)" |
| M6b | ch5:114 | "or p = 0.16 with extreme values trimmed" | Same; p = 0.162 is correct | "with extreme values capped" |
| M6c | appendix_notes:164 | "and when trimmed (p = 0.16)" | Same | "and when winsorised (p = 0.16)" |
| M7 | ch5:70 | "while the large moves came between 2021 and 2024" | Sources label the repricing **2022–24** (by the year a change ends): `PART3_H1_GROUNDWORK.md`:48 "The large take-rate changes came in 2022-24"; `PREREGISTRATION.md` 8 Oct "The repricing period is 2022-24"; `timing_check` T01–T03 "2022-24 window"; FINDINGS §2. "2021 to 2024" is defensible only as the span from the start of the first changes (Grab and Bukalapak, end-2021 to end-2022). Low severity, but the label differs from every source | "while the large moves came in the yearly changes of 2022 to 2024" (or define once: "from end-2021 to end-2024") |
| M7b | ch7:3 | "Between 2021 and 2024 the platforms' take rates moved" | Same | Same |
| M7c | ch7:13 | "the choice of revenue changed the conclusion between 2021 and 2024" | Same | Same |
| M7d | ch7:33 | "the rejection of H1 describes a period, 2021 to 2024" | Same | Same |
| M8 | ch5:40 (Table 5.2 note) | "With Shopee's take rate at 9 or 11 percent, the total wedge is US$39.9 or US$40.3 billion" | A higher take rate means more revenue and a smaller wedge: 9% → **40.29**, 11% → **39.86** (`FINDINGS.md` §1, `PART3_H1_GROUNDWORK.md`:9; recomputed from `take_rate_levels.csv`). The "or ... or" pairing is reversed | "at 9 or 11 percent, the total wedge is US$40.3 or US$39.9 billion" |
| N1 | ch5:228 | "Tokopedia alone said that it had about 15 million merchants in 2022" | Only `PART5_OBJ3_GROUNDWORK.md`:39 ("company statement"). No extract row in `tables/src/`, no quoted passage, and no citation in the sentence. The BPS side (0.6 million, `part5_checks.json` 591.8 thousand, 2022) matches | Add a source-extract row and a citation (Tokopedia/GoTo document, year), or drop the number |
| N2 | ch1:19 | "Decisions worth trillions of dollars rest on numbers that show a fraction of the activity" | No source quantifies decisions. The nearest number is UNCTAD's almost US$27 trillion of business e-commerce sales in 2022 (ch1:11), which is sales, not decisions | Tie it to the UNCTAD figure ("Online sales worth trillions of dollars are described by numbers ...") or cut "worth trillions of dollars" |
| N3 | ch6:45 | "a rule not yet in force by late August 2026 (Ayudiana 2026)" | Ayudiana (ANTARA, 8 July 2026) says the discount was *targeted* for August 2026. The late-August status rests only on "search summaries of a 27 August 2026 Katadata piece" that was not read (`CH6_SOURCES.md` §4c); Katadata 12 Aug says the rule "starts this month" with application required | Read and cite the 27 Aug Katadata article, or write "targeted for August 2026; whether it was in force by late August is not confirmed (Ayudiana 2026)" |

### Rounding-ok items (no change needed; optional tightening)

| file:line | Text | Source | Note |
|---|---|---|---|
| ch1:15 | "about US$60 million" | Rp203.58tn × 0.5% = Rp1.018tn / 15,855.45 = US$64.2m (`tax_base_rulers.csv`) | One significant figure; "about US$64 million" is closer |
| ch6:61 | "about US$60 million" | Same | Same |
| ch5:226 | "about US$57 billion" (Momentum Works 2024) | US$56.5bn as published (`tax_base_rulers.py` docstring) | Tie rounded up; "about US$56.5 billion" matches the source |
| ch5:37 (Table 5.2), appendix_notes:77 | Grab 2023 revenue 0.60 | 0.605 (`take_rate_levels.csv`) | Tie at two decimals; total 3.16 is right either way |
| ch5:50 | "the take rate moved by about 20 percent a year" | median abs Δln m = 0.201 (`h1_extended_results.json`) | A log change of 0.20 is a 22 percent rise; acceptable as "about" |
| ch5:57 (Table 5.3) | shuffle p 0.022 | 0.0221 (`h1_extended_results.json`), but 0.0212 for the same test in `h1_thesis_drops.json` (different run) | Both round to 0.02; the two source files disagree in the third decimal |
| ch6:39 | "Its take rate rose to about 22 percent" | 3,593 / 16,693 = 21.52% (`CH6_SOURCES.md` C9 suggests "21.5 percent") | Half-up rounding |
| ch7:47 | "the test of H1 still gives p = 0.004" | 0.0035 (`INCENTIVE_ACCOUNTING.md` re-test table) | Half-up rounding of 0.0035 |

### Source notes (no thesis change, but worth knowing)

- ch5:40, Sea's company-wide rate: no committed table computes this sensitivity. Recomputed: Sea/Shopee 2023 take rate 11.465% (`take_rate_levels.csv`) gives Shopee revenue 2.467 and a total wedge of US$39.754bn, so "11.5 percent" and "US$39.8 billion" both match. At exactly 11.5 percent the wedge would be 39.75 (still 39.7–39.8). Consider adding the line to `fy2023_recompute.json`.
- ch5:68 (13 of 15; two opposite; 65 percent abroad) rests on `h1_direction_count.py`, which prints only and writes no table. Rerun on 15 Oct: 13, 2, 103 of 158 (0.65). It reproduces, but no committed output holds it.
- Appendix C, E1: the registered comparison was against BPS's published count share (84.81%), not the microdata count share (79.3%) the row quotes. Both comparisons hold.
- Ledger K01 (60.5) and C15 (60.6) give two values for the same Tokopedia share; the appendix arithmetic (1,298,601 / 2,144,271 = 60.6) supports C15.
- The quarterly H1 note in `PREREGISTRATION.md` (7 Oct) first said the large swings were "2021-2023" and was corrected on 8 Oct to "2022-24"; the thesis text has neither (see M7).

## All checked numbers, by section (file:line → source)

Tags: no tag = match; [R] = rounding-ok; [X] = MISMATCH; [N] = NO SOURCE FOUND. Ledger IDs refer to `tables/claims_ledger*.csv`.

### Chapter 1 (18)
- ch1:5 — BPS online sales +41% → +40.6 (`consistency_grid_growth.csv`, `yardsticks_bi_bps.csv`, Y02); Bank Indonesia −5% → −4.7 (Y01, `yardsticks_bi_bps.csv` 476.3 → 453.75).
- ch1:7 — Tokopedia net revenue +53% → 53.2 (C13); transaction value −9% → −8.9 (C12); 2022–2023 label correct (`tokopedia_segment.csv`).
- ch1:9 — about 60% from smaller incentives → 60.6 (C15).
- ch1:11 — 43 economies; almost US$27 trillion; 2022 → UNCTAD 2024 (`REFERENCE_CHECK.md` row UNCTAD 2024, web-verified).
- ch1:15 — BPS 2024 about US$81bn → Rp1,288.93tn / 15,855.45 = 81.3; BI about US$31bn → Rp487.01tn / 15,855.45 = 30.7; "more than two to one" → 2.65 (N22, Y05); about US$60m [R] → 64.2; about US$300m → US$62bn × 0.5% = 310 (`tax_base_rulers.py`).
- ch1:19 — "trillions of dollars" [N] (N2); "millions of the people ... outside" → derived: 3.81m sellers × 82.2% off marketplaces = 3.1m (`bps_microdata_results.json`, `bps_descriptives.json`).
- ch1:23 — platform histories 2020 to 2025 → `take_rate_levels.csv` (Bukalapak 2020 to Blibli 2025).
- ch1:27 — marketplaces about a fifth of value → 15.8–25.6% (C11-06..09); about half of 2023 rise not entry → 37–56% (A10-04, A10-06).

### Chapter 2 (1)
- ch2:54 — rider pays 100, driver keeps 80, platform records 20: arithmetic correct.

### Chapter 3 (21)
- ch3:37 — wedge summed over three platforms for 2023 → `fy2023_recompute.json`.
- ch3:39 — 0.09 = 9 percent: correct.
- ch3:40 — 0.62 = 62 points → Tokopedia D 62.1 (C14).
- ch3:68 — E = 9 ↔ keeps 10 percent: 1/0.10 − 1 = 9.
- ch3:84 — take rate about 1.5 → 1.4757; about 2.5 → 2.4816 (`take_rate_levels.csv`); "about two thirds more" → 2.4816/1.4757 = 1.682 (68%); V about −9 → −8.9; R about +53 → 53.2; 0.91 × 0.68 = 0.62 → 0.911 × 0.682 = 0.621; 62 points → 62.1 (C14); wedge about 98% of V → 98.5% (2022), 97.5% (2023); wedge fell about 10% → 269,115,247 → 242,660,966 = −9.8% (`appendix A.4`, W12 series).
- ch3:90 — 2% → E = 49; 2% → 3% raises R by 50%; 17% → E = 4.88 ("near 5"); 17% → 18% raises R by 5.9% ("about 6").
- ch3:156 — 21.5 percent → E5 threshold (`PREREGISTRATION.md`, `bps_microdata_results.json`).
- ch3:158 — 27.4 percent → `bps_recompute.json` N_growth 27.40; 127.4; 27.4/127.4 = 21.51.

### Chapter 4 (53)
- ch4:7 — three survey rounds → `LICENSED_DATA.md`.
- ch4:9 — five platform series; three report incentives (Tokopedia, Grab, GoTo; Blibli proxy, Bukalapak none) → Table 4.1, `growth_decomposition.py` docstring.
- ch4:19 — five platforms; three marketplaces and two on-demand; 27 foreign; 8 + 19; ten left out = six own goods + four no V → `h1_extended_firms.csv`, appendix A.1 list.
- ch4:25–29 (Table 4.1) — Tokopedia 2022–2023, 1 pair; Blibli 2021–2025, 4; Bukalapak 2020–2023, 3; Grab 2020–2024, 4; GoTo 2022–2025, 3 → `h1_direction_count.py` rerun (15 pairs by platform), `h1_extended_firms.csv` n.
- ch4:37 — 15 pairs and 158 → `take_rate_share_full.json`.
- ch4:41 — three platforms in 2023 → `fy2023_recompute.json`.
- ch4:43 — Shopee take rate 10%, varied 9–11% → FINDINGS §1, `take_rate_levels.csv`.
- ch4:47 — log change 0.52 → 0.5198 (`h1_extended_firms.csv`); factor 1.68 → e^0.5198 = 1.682; 68 percent.
- ch4:51 — five against 27; 9,999 shuffles → `h1_extended.py` (`range(9999)`).
- ch4:63 — seven windows → `growth_decomposition.csv`.
- ch4:67 — 28 platforms; 138 platform-years (M12-01/02); Bukalapak + 27 abroad; adds Airbnb, Booking, DoorDash, Lyft, Uber and lacks Despegar, Mercado Libre, Ozon, Rakuten, Sea → `m1_market_value_results.json` firms_main.
- ch4:69 — "three segment series and three more whole companies" [X] (M2).
- ch4:79 — within 1 percent; 28.63; 12.25; all three pass → `bps_microdata_results.json` (weights, books_share_*).
- ch4:85–87 (Table 4.2) — rows 11,848 / 31,724 / 39,736 (`LICENSED_DATA.md`, `PREREGISTRATION.md` 7 Oct); weighted totals 2,361,423 / 2,995,986 / 3,814,799 and BPS counts 2,361,423 / 2,995,879 / 3,816,750 (`bps_microdata_results.json`).
- ch4:89 — 27.4 percent; 3,816,750 / 1.274 = 2,995,879.
- ch4:93 — threshold stays 21.5 (alt count 3,934,981 not matched).
- ch4:97 — about 5 percent a year → 5.09 (A10-05).
- ch4:107 — brackets only in 2021 and 2023 files; half to double; about US$53bn → Rp783tn / 14,849.85 = 52.7.
- ch4:111 — six cities, 2023; five or more employees, seven countries → `PREREGISTRATION.md` 3 Oct.
- ch4:113 — about US$20,000 → Rp300m / 14,849.85 = 20,202; about US$34,000 → Rp500m / 14,849.85 = 33,670.
- ch4:119 — six measures → V10 (of 6).
- ch4:135 — 272 automatic checks → 272 ledger rows, 0 failures.

### Chapter 5 (264)
- ch5:3 — count +27% → 27.4; about half → 37–56%.
- ch5:12 (Table 5.1) — about 7% → 7.31 (C11-05); about US$40bn → 40.07 (C36).
- ch5:13 — about three times → 0.201 / 0.062 = 3.3.
- ch5:15 — 15 pairs against 158; seven windows → `take_rate_share_full.json`, `growth_decomposition.csv`.
- ch5:16 — "Extreme values trimmed" [X] (M6).
- ch5:19 — six platform measures → V10.
- ch5:21 — 13.45 against 21.5 → B01, E5.
- ch5:24 — four survey years (2020, 2022, 2023, 2024 published) → `bps_descriptives.json`.
- ch5:25 — three value scenarios → `bps_microdata_results.json` recon_low/mid/high.
- ch5:29 — about US$43bn (43.23, C34); about US$3bn (3.16, C35); about 7% (7.31); about US$40bn (40.07); "almost 13" → E 12.67 (C38).
- ch5:35–38 (Table 5.2) — Tokopedia 16.33 / 0.41 / 15.93 / 39.3 → Rp248,836,156m, 6,175,190m, 242,660,966m at 15,236.88 = 16.331 / 0.405 / 15.926; E 39.30 (C42); Shopee 21.52 / 2.15 / 19.37 / 9.0; Grab 5.38 / 0.60 [R] / 4.78 / 7.9; total 43.23 / 3.16 / 40.07 / 12.7 → `take_rate_levels.csv`, `fy2023_recompute.json`.
- ch5:40 — US$39.9 and US$40.3bn are the right values (11% → 39.86; 9% → 40.29; FINDINGS §1), but the sentence pairs them in the wrong order [X] (M8); 11.5% → 11.465 (Sea 2023, `take_rate_levels.csv`); US$39.8bn → 39.754 (recomputed).
- ch5:42 — Tokopedia about 39 (39.3); Shopee 9; Grab about 8 (7.9); Blibli about 43 (43.4, C40); Bukalapak 36 (36.0, C41).
- ch5:44 — 9–11% keeps near US$40bn (39.86–40.29); dropping any one leaves > US$20bn (20.70, PART3:9); wedge 97–99% of V → 97.08–99.46 (W12-01/02).
- ch5:46 — about a fifth → 15.8–25.6%.
- ch5:50 — about 20% [R] (0.201); about 6% (0.062); about three times (3.3).
- ch5:56–60 (Table 5.3) — 0.20 / 0.06 / 0.004 (H01, H02, H04: 0.0038); shuffle 0.022 [R] (0.0221; 0.0212 in `h1_thesis_drops.json`); 5 vs 26, 27.0 / 6.5 / 0.005 (H06, H07, 0.0055); 0.17 to 0.23 and 0.003 to 0.016 (`h1_extended_results.json` leave-one-out 0.169–0.225, p 0.0030–0.0164; grouped Tokopedia+GoTo p 0.003, PREREG 8 Oct); 3 vs 8, 0.071 / 0.049 / 0.19 (`h1_quarterly_results.json`).
- ch5:64 — p = 0.004 and 0.022; 0.016 or below.
- ch5:66 — p = 0.024 (C47); shuffle p = 0.06 (`test_battery.csv` firm_perm_p 0.0606); correlations 0.10 and 0.98 (C48, C49).
- ch5:68 — 13 of 15; two opposite (Tokopedia 2023, Blibli 2025); about two thirds abroad → 103/158 = 0.65 (`h1_direction_count.py` rerun).
- ch5:70 — p = 0.19 (Q03); quarterly pairs mostly 2023 to 2026 (FINDINGS §2); "between 2021 and 2024" [X] (M7).
- ch5:72 — about 1 point each → 1.01 vs 0.98; p = 0.65 (`h1_points_vs_log.json`).
- ch5:74 — 1.6% vs 17% (1.59, 16.93); 1-point rise lifts R by more than half at 1.6% (62.5%) and about 6% at 17% (5.9%).
- ch5:78 (Fig 5.1 note) — 26 vs 27 foreign platforms (Ozon) → `h1_points_vs_log.json` firms.
- ch5:82 — about two thirds vs about a quarter → 65.8 vs 23.8 (`take_rate_share_full.json`, 15 vs 158 pairs; V02/V03 66.5 vs 26.7 on 8 vs 29); about 95% of a wedge move from V → 1 − 0.055 = 94.5 in both groups.
- ch5:84 — seven windows.
- ch5:90–96 (Table 5.4) — all 28 values match `growth_decomposition.csv` at full precision: Tokopedia +53 / −22 / 76 / 45 (−21.85 / 76.45 / 45.40); Blibli 22–23 +465 / 17 / 20 / 63; Blibli 22–25 +679 / 18 / 63 / 20; Grab 21–24 +321 / 34 / 34 / 33 (33.70 / 33.78 / 32.52); Grab 22–24 +86 / 42 / 11 / 47 (42.50 / 10.60 / 46.90); GoTo 22–25 +111 / 12 / 36 / 52; GoTo 23–25 +114 / 27 / 6 / 67.
- ch5:98 — rows add to 99 or 101 (Tokopedia 99; others 99–101).
- ch5:100 — incentives larger in four windows, fees in two, Grab 2021–24 nearly equal (33.8 vs 32.5) → `PART3_H1_GROUNDWORK.md`:44.
- ch5:102 — incentives fell about a third → 4,112,320 → 2,813,719 = −31.6% (`tokopedia_segment.csv`); 60 / 40 → 60.6 / 39.4 (C15/C16).
- ch5:108 — Blibli 2024–25 V about −2% (−1.9), R about +12% (+12.1) → `take_rate_levels.csv` 54,210 → 53,187; 1,384 → 1,551.
- ch5:112 — 28 platforms, 138 platform-years, about 0.6 (0.600), p = 0.002 (0.0016) → M12-01..03, M12-06.
- ch5:114 — about 0.3 (0.334, M12-04); p = 0.20 (M12-05); p = 0.16 (0.162 winsorised); "trimmed" [X] (M6b).
- ch5:116 — "three segment series and three more whole companies" [X] (M2b); p = 0.004 (M12-07); about 0.6 vs about 0.1 (0.630 vs 0.071).
- ch5:122 — household spending about +9% (9.4, V14); five of six slower (V10); three fell (V11).
- ch5:124 — Tokopedia revenue +53; BPS value +41.
- ch5:128 (Fig 5.3 note) — Momentum Works 3.5 (`consistency_grid_growth.csv`) and its release states 3.7 (`tables/src/indo_market_extraction.csv` row 24, MW 16 Jul 2024).
- ch5:130 — limit about 10% → 10.36 (E6); median zero (B03).
- ch5:132 — about a quarter up (24.5, B04); about a third down (31.9, B05); 2022: more than a third up (36.9, L13), a quarter down (24.4, L14); mean about −4 (−4.3, L10); 41 vs 35 (41.3, 35.3, L01, L15); +27% count.
- ch5:136 — value +41; businesses +27; 71% → `bps_recompute.json` (70.98 sym, 71.06 log).
- ch5:138 — +17 (17.08); 90% (90.29); 71% (70.95, C29).
- ch5:140 — about 13% (13.45); 21.5; at most about 16% (15.54, B02); 27%.
- ch5:146 — 306 thousand (305.6); 37%; 56%; about 5% a year → `bps_rise_accounting.json`.
- ch5:150–154 (Table 5.5) — 819; 513 (63%: 62.7); 361 (44%: 513.2 − 152.4 = 360.8; 44.06); 306 (37%: 37.32); 458 (56%: 55.94) → `bps_rise_accounting.json`.
- ch5:156 — published rise 821 thousand → 3,816,750 − 2,995,879 = 820,871.
- ch5:158 — started by 2020: about −10% (−9.92), +6% (+6.04) → `bps_cohort_check.json`.
- ch5:160 — pre-2020 cohort about −10% (−10.2, C09); at least 754 thousand (C11); rise 584 thousand (C12).
- ch5:162 — 34 provinces; rank correlations 0.10 (0.096) and 0.35 (0.352) → `bps_frame_check.json`; chat/social only +13% (13.0, C14 v7); marketplace users +0.3% (0.26, C13 v7).
- ch5:164 — about 1.4% (1.37, C11-02); 306 thousand; 4.6 (C11-03).
- ch5:166 — about US$53bn (Rp783tn at 2022 rate = 52.7); about US$72bn (72.25, `bps_recompute.json`); entrants 25–30% (25.5–29.8); not explained by entry 15–17% (14.6–16.7); mean about −4% (−4.3); 53–59% (53.4–59.4) → `gel_checks.json` value_increase_split_pct.
- ch5:172 — about 450 thousand (225.8 + 223.8 = 449.6, `bps_newly_counted_profile.json` beyond_normal); 458 thousand.
- ch5:180 — about 470 → 320 thousand (472.0 → 318.1, started by 2021, `bps_returning_check.json`).
- ch5:184 — returners 10 to 15% of 2022 count → 305.6/2,996 = 10.2%, 458.0/2,996 = 15.3% (`PREREGISTRATION.md` 8 Oct; PART4:10).
- ch5:190 — about 96% chat or social (96.19, 2023, `bps_descriptives.json`); about 22% in 2020 (21.64) to about 17% in 2024 (17.23 published).
- ch5:192 — about a fifth; 23–26% in 2022 (22.6–25.6); 18% in 2023 (18.23); 16% in 2024 (15.79) → C11-06..09.
- ch5:194 — marketplace +1.5% (1.45, C23); others about +21% (20.57, C24); 43% only Gojek or Grab (43.1, P05); 47% shopping marketplace (47.0, P04).
- ch5:200 — 29% vs 12% in 2023 → 28.63 vs 12.25 (2024 file).
- ch5:202 — 23% → 17% (23.4 → 16.8, C15/C16 v7).
- ch5:204 — 26–40% of value (25.7–40.4, E1); 79% of count (79.3); annual reading about twice (1.95, B19); monthly about 23 times (23.38).
- ch5:206 — limit 5 points; fell 5.8 and 3.3 points (E7).
- ch5:208 — six cities; 27% (27.3, W05); 70% no written records (100 − 29.9); median about US$4,000 (Rp60m / 15,236.88 = 3,938); limit about US$6,600 (Rp100m = 6,563); mean about US$7,300 (Rp111m = 7,285) → `PREREGISTRATION.md` 3 Oct.
- ch5:210 — about 40% (39.9, F03); seven countries; about 9% Malaysia and Thailand (9.1, 8.7, X02, X03).
- ch5:216 — BI about −5%, BPS about +41%.
- ch5:218 — about 0.2% mid (0.23, L04); 0.2–13% (0.23–13.16, `gel_checks.json`); 2023–24 about 1.5% (1.45).
- ch5:220 — 0.16, 0.68, 1.62 → `bps_microdata_results.json` recon_*.marketplace_b2c_over_BI.
- ch5:222 — platform measures 5–7% (MW 5.2, e-Conomy 5.1, BI 7.3); BPS about 17% (17.1); parcels about 25% (25.2, G02); tax on foreign digital services about 25% (24.9) → `consistency_grid_growth.csv`.
- ch5:224 — e-money about 30% (30.47, C50); mobile banking 83% (82.84, C52); QRIS 187% (186.98, C54).
- ch5:226 — BPS 2024 about US$81bn; BI about US$31bn; BPS marketplace 2023 about US$13bn (13.17, C33); Tokopedia + Shopee about US$38bn (16.33 + 21.52 = 37.85; N20 2.874 × 13.17); less than a quarter in 2024 (Rp203.58tn = US$12.84bn / 56.5 = 0.227); MW about US$57bn [R] (56.5).
- ch5:228 — Tokopedia about 15 million merchants [N] (N1); BPS about 0.6 million marketplace sellers (591.8 thousand, P01).
- ch5:230 — four quarters to mid-2026 (R06: 2025Q3–2026Q2); GoTo V +2% (R02); spending +8% (8.3, R05); revenue +21% [X] (M1).

### Chapter 6 (95)
- ch6:3 — cap and discount rule in 2026 (Permendag 19/2026 set 4 June 2026; decree from 1 July 2026); four marketplaces since October 2026 → `CH6_SOURCES.md` items 1, 5b, 10.
- ch6:5 — at most about 1 in 20 sellers (5.4, T6-03); about a fifth of value (17.5–23.6, T6-01/02).
- ch6:15–21 (Table 6.1) — KP-PHB 532/2026; Perpres 27/2026; 8 percent; 1 July 2026; released 8 October 2026 (`CH6_SOURCES.md` 2c, 2d); Permendag 19/2026 Art. 18 (§10); PMK 37/2025, 0.5%, Rp500m, four collectors since 1 October 2026 (§5a, §5b); PP 20/2026, 0.5%, Rp4.8bn, content creators excluded (`sources/policy_primary/PP_20_2026_pajak_penghasilan_UMKM.txt` lines 128, 161, 903); BPS Regulation 4/2023 (§6); economic census 2026 (§7); Permendag 31/2023 carried into 19/2026 Art. 25(3) (§10).
- ch6:23 — Rp500m about US$32,000 at 2024 rate (31,535); Rp4.8bn about US$300,000 (302,736); about US$34,000 at 2022 rate (33,670).
- ch6:29 — 2023 ban; about 96% in 2023 (96.19).
- ch6:35 — protests since 2025 (20 May 2025); 10 percent, down from 20 (Ronal 2025, `CH6_SOURCES.md` §3); 8 percent from July 2026; presidential regulation October 2026, delivery fees by end of year (31 Dec 2026).
- ch6:37 — GoRide about 7% of group net revenue (§2a); Grab Indonesia two-wheel 6% of Mobility GMV (§1); about 2% of on-demand V (0.06 × 2,214 / 6,463 = 2.1%).
- ch6:39 — revenue +21% [X] (M1b); V +2%; take rate about 22% [R] (21.52); about 18% a year earlier (18.25).
- ch6:41 — four of seven windows.
- ch6:43 — Tokopedia incentives about a third lower (−31.6%); 2023 its last full year of separate reporting; GoTo incentives about 11% (11.3) in 2023 to about 4% (4.0) in 2025 (`goto_ondemand_annual.csv`); Grab about 10% (10.36) in the four quarters to early 2026 (2025Q2–2026Q1, `grab_quarterly_verified.csv`, T6-09).
- ch6:45 — fixed fee mid-2025 (20 Jul / 11 Aug 2025, Islamiati 2025); 2026 increases (May 2026); TikTok Shop took over Tokopedia in 2024 (§5c); "not yet in force by late August 2026" [N] (N3).
- ch6:49 — 0.5%; about US$34,000; October 2026 start; begun in August 2026 then stopped and refunded (§5b).
- ch6:51 — 1 in 20; 2022; about US$20,000; about 5% (5.4); about US$34,000.
- ch6:53 — 23–26% (22.6–25.6); 77–94% (77.4, 92.2, 93.8, E8); "17 to 24" [X] (M3); about a fifth.
- ch6:57 — about 18% in 2023 (17.8, T6-04); 47% (P04); about 8% (17.8 × 0.47 = 8.4).
- ch6:59 — about 13% wanted to join (13.5, L03; 2024 file = survey for 2023).
- ch6:61 — 0.5%; about US$60m [R] (64.2); about five times (4.83, T01 v3); about US$300m (310); about 0.2% of 2026 target (0.208, T03 v3).
- ch6:67 — since 2023; by late 2024; 61 sent; 75 had not (`CH6_SOURCES.md` §6; `REFERENCE_CHECK.md` Republika/Risalah 2024).
- ch6:71 — frame from economic census 2016; census June to August 2026 (15 Jun–31 Aug) → §7.
- ch6:73 — about half of the 2023 rise.
- ch6:77 — nine predictions; eight on 3Q26 results; six on the cap (P1, P2, P3, P4, P5, R1); one on fees (R3); one on buying (R2); ninth on BPS share → `PREREGISTRATION.md` §A, §C, 3 Oct addendum.
- ch6:83–91 (Table 6.2) — P1 0.3–2.5 points; P3 0–12%; P5 ≥5%, fails below 2%; R1 −0.5 to +12.5; R2 below spending; P2 −0.6 to +0.4; P4 ≤ +0.3; R3 ≥ +10; marketplace share ≤ 15.79%; scoring dates late October (27 Oct), early November, mid-November → `PREREGISTRATION.md`, FINDINGS §10.
- ch6:93 — collection began 1 October 2026, a day before registration (2 Oct) → `PREREGISTRATION.md` 15 Oct addendum.
- ch6:103 — OECD 2020 and 2021; DAC7 reports for activity from 2023; Philippines 2023 (RR 16-2023); Viet Nam since 2025 (1 July 2025) → `CH6_SOURCES.md` §8.
- ch6:107 — fourteen US cities and states → §9.

### Chapter 7 (42)
- ch7:3 — "Between 2021 and 2024" [X] (M7b); about half.
- ch7:9 — about US$3bn of US$43bn; about US$40bn.
- ch7:11 — about a fifth.
- ch7:13 — "between 2021 and 2024" [X] (M7c); about three times.
- ch7:15 — five of six; median no change.
- ch7:21 — about two thirds vs about a quarter (65.8 vs 23.8); 28 listed platforms.
- ch7:25 — 1 in 20; about a fifth; at most about 8%.
- ch7:31 — 21.5; about 13% (13.45).
- ch7:33 — p = 0.19; 2023 to 2026; "2021 to 2024" [X] (M7d).
- ch7:35 — p = 0.20.
- ch7:37 — 5.8 points; limit 5; 3.3 points; about US$7,300; about US$6,600; about US$4,000; two of three scenarios.
- ch7:39 — a day before registration.
- ch7:45 — three Indonesian marketplaces; two-sided doubles p, main result below 1% (2 × 0.0038 = 0.0076).
- ch7:47 — eight of the 27 (`INCENTIVE_ACCOUNTING.md`); p = 0.004 [R] (0.0035).
- ch7:49 — 2021 and 2023 files describe 2020 and 2022; about US$3.4m (Rp50bn / 14,849.85 = 3.37m); 19 sample rows (P02); 18–39% (P06, P07).
- ch7:53 — 10 to 15%.
- ch7:57 — 28 listed platforms.
- ch7:77 — BPS about +41%; BI about −5%.

### Appendix notes (426)
- A.1 (lines 13–39): all 27 platforms' pairs and medians (54 values) match `h1_extended_firms.csv` (e.g. ACVA 5 / 0.155; Ozon 1 / 0.177; Sea 7 / 0.254; Zalando 4 / 0.021); pairs sum to 129 added + 29 chosen first = 158; line 41: six own-goods and four no-V exclusions.
- A.2 (lines 47–51): 15 values match `h1_extended_firms.csv` and the rerun (Blibli 4 / 0.25 / 0.00; Bukalapak 3 / 0.14 / 0.33; GoTo 3 / 0.09 / 0.67; Grab 4 / 0.20 / 0.50; Tokopedia 1 / 0.52 / 0.00).
- A.3 (lines 59–65): 49 values match `growth_decomposition.csv` (revenue growth, V growth, start and end take rates, three shares).
- A.3 (line 67): Rp m values 8,143,239; 8,988,909; 4,112,320; 2,813,719; 4,030,919; 6,175,190 (`tokopedia_segment.csv`); rise 2,144,271; 60.6 and 39.4 (C15/C16); "(61 and 39 percent in the text)" [X] (M4).
- A.4 (lines 75–91): 85 values (V, R, W, m, E for 17 platform-years) match `take_rate_levels.csv`; Grab 2023 R 0.60 [R] (0.605); line 71: Shopee assumed 8.4 / 10 / 10.8% match.
- B.1 table (lines 101–125): Main 0.201 / 0.062 / 0.0038 / 0.0221; vs 8: 0.055 / 0.0225 / 0.0497; vs 19: 0.070 / 0.0046 / 0.0175 (`h1_extended_results.json`); without 8 expensing: 0.062 / 0.0035 / 0.0066 (source table 0.007); only 11 deducting: 0.075 / 0.0043 / 0.0052 (source 0.005) (`INCENTIVE_ACCOUNTING.md`); D in points 27.0 / 6.5 / 0.0055; without Ozon 0.060 / 0.0030 / 0.0215; without Zalando 0.064 / 0.0045 / 0.0238; without both 0.062 / 0.0036 / 0.0230 (`h1_thesis_drops.json`); five leave-one-out rows (0.169 / 0.0137 / 0.0364; 0.225 / 0.0049 / 0.0070; 0.225 / 0.0030 / 0.0071; 0.194 / 0.0094 / 0.0166; 0.169 / 0.0164 / 0.0409); three-marketplace rows 38.917 / 7.105 / 0.0022 / 0.0606; 0.0242 (C47); ex-Sea 38.917 / 4.192 / <0.0001 / 0.0083; log 0.252 / 0.055 / 0.0037 / 0.0303; log ex-Sea 0.252 / 0.033 / 0.0001 / 0.0167; drop 2022–23 14.411 / 7.105 / 0.0248 / 0.2222 (values match, label [X] M5); drop largest 15.738 / 7.105 / 0.0061 / 0.0606; vs 40 pairs 38.917 / 7.373 / 0.0014 / 0.0121; incl. constructed 42.017 / 7.105 / 0.0006 / 0.0225 (`test_battery.csv`); Tokopedia+GoTo 0.003 / 0.007 (`PREREGISTRATION.md` 8 Oct); quarterly 0.071 / 0.049 / 0.19 / 0.33 (`h1_quarterly_results.json`).
- B.1 text (lines 127–133): 0.10 and 0.98 (C48, C49); quarterly sample 3 vs 8 (`h1_quarterly_results.json` pairs_by_firm); one third vs 67–69% (`h1_extended_results.json` share_within_010: 0.333, 0.674, 0.69); 26 foreign; 1.01 vs 0.98 points; p = 0.65; 1.59 vs 16.93 (`h1_points_vs_log.json`).
- B.2 (lines 138–140): Rp50bn ≈ US$3.4m (2022 rate); 0.5% (0.53, P03); 18–39% (P06/P07); 19 rows; 34 provinces; 0.10 (p 0.59); 0.35 (p 0.04); 23 provinces; 98.5% (`bps_frame_check.json`); 1.4%; 306 thousand; 4.6; 2.3 (C11-02..04).
- C (lines 148–168): E1 25.7–40.4 vs 79.3; E2 22.6–25.6; E2b/E2c 21.6, 19.8, 17.8, 17.2; E3 7.5 vs 2.2; E5 21.5, 13.45; E6 10.36, 0; E7 5, 5.8, 3.3; E8 Rp300m, 92.2; RBI 0.16, 0.68, 1.62; W1/W2 29.9 vs 12.3, 11.5 vs 2.7; W3 Rp100m ≈ US$6,600, mean Rp111m, median Rp60m; F3/X3 one third, 39.9, 9.1, 8.7; X2 3 of 4 required, holds 4 of 4; Q1 p = 0.19; M1 p = 0.20, 0.16 ("when trimmed" [X] M6c), 34 platforms, 0.004; M2 0.002; P/R first results 27 Oct; tax start registered 2 Oct, collection 1 Oct, addendum 15 Oct; marketplace share 15.79. All 21 registration dates match `PREREGISTRATION.md` (2 Oct: E1–E6, P1–P5, section C; 3 Oct: E2c, E7, E8, RBI, W, F, X, R1–R3; 7 Oct: Q1; 8 Oct: M1, M2).
- D (lines 172–176): Fig 5.3 ten values (+9.4, −8.9, −10.5, −4.7, +3.5 / 3.7, +6.9, +34.7, +53.2, +40.6, +27.4) match `consistency_grid_growth.csv`, ledger v6 and the direction rerun; Fig 5.4 eight values (18.3 / 40.5; 28.9 / 41.2; 23.6 / 36.3; 20.4 + 18.1 = 38.5 / 28.6 + 24.4 = 53.0) match `bps_newly_counted_profile.json`; Fig 5.5 seven values (21.6, 19.8, 17.8, 17.2; 23.5, 20.7, 15.2) match `bps_descriptives.json`.
