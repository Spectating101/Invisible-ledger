# Number audit of the 16 October edits (follow-up to AUDIT_NUMBERS.md)

Scope: every number in every line added or changed between commit `601e477` (the 15 Oct audit) and `HEAD` (`3984b0e`, branch `claude/happy-pascal-uc2eya`) in `papers/thesis_2026-10/` ch1–ch5, drafts/ch6, drafts/ch7 and appendix_notes.md, plus the new files `abstract.md` and `symbols.md`, read whole. Line numbers are those of the files at `3984b0e`. No chapter file was edited. No licensed data were opened.

Method and sources of truth are those of `AUDIT_NUMBERS.md` (top of file): `tables/` (CSV/JSON, `claims_ledger*.csv`), `FINDINGS.md`, `PART1`–`PART7`, `PREREGISTRATION.md` (with the 15 and 16 Oct addenda), and `materials_2026-10-15/` (`CH6_SOURCES.md`, `INCENTIVE_ACCOUNTING.md`, `FINANCE_FRAMING.md`, `REFERENCE_CHECK.md`). FX: World Bank yearly rate (2022 Rp14,849.85; 2023 Rp15,236.88; 2024 Rp15,855.45). Read-only reruns, output to the session scratchpad only: `h2_coverage_adjusted.py` (identical to the committed `tables/h2_coverage_adjusted.json`), the Mann–Whitney p without the eight expensing platforms (0.00353), and a text extract of the committed public file `sources/core_public_documents/goto_annual_report_2023.pdf`. `git status` was clean after the reruns.

Counting rule: one item per number, stated range, year that carries a claim, US$ conversion, or label that carries a number. Citation years, equation and section cross-references in prose are not counted (the cross-references in `symbols.md` are counted, because that file exists to state them). Appendix table cells were also compared cell by cell with the 15 Oct version: every numeric cell in A.1–A.4 and B is unchanged (54, 15, 49, 102 and 88 cells); only names, labels and dashes changed.

## Summary counts

| Category | Count |
|---|---|
| Checked | 461 |
| MATCH (equal at the stated precision) | 456 |
| ROUNDING-OK (acceptable; optional tightening noted) | 2 |
| MISMATCH (wrong value, period, scope or label) | 3 |
| NO SOURCE FOUND | 0 |
| Wording that claims more than the source (number itself matches) | 5 |

By file: abstract 11, symbols 16, ch1 3, ch2 0, ch3 0, ch4 15, ch5 86, ch6 29, ch7 40, appendix 261.

Task 2 (the 18 items of 15 Oct): 16 fixed, 1 partly fixed (N1), 1 not fixed (N2).

Task 3 (headline consistency): all headline values agree across abstract, Ch5 and Ch7. Two framing problems sit in the abstract (O1, F1); one scope slip in Ch7 (F2).

## MISMATCH, overclaims and ROUNDING-OK, with proposed sentences

### MISMATCH

**F1. abstract.md:7 (period label on the three-times result).**
- Text: "Between 2022 and 2024, Indonesian and regional platforms changed that share about three times as much as 27 platforms abroad."
- Source: the ratio is 0.201 / 0.062 = 3.3 (`h1_extended_results.json`; ledger H01, H02). It uses all 15 Indonesian and regional pairs, from 2020–21 to 2024–25 (Table 4.1: Bukalapak 2020–23, Blibli 2021–25, Grab 2020–24, GoTo 2022–25, Tokopedia 2022–23), against 158 foreign pairs from all reported years. Four of the 15 pairs lie outside 2022–24. The period 2022–24 is where the large moves cluster (`timing_check.json`: 4 of 4 platforms larger in 2022–24, medians 0.32 against 0.06; exploratory), not the window of the ratio.
- Proposed: "Indonesian and regional platforms changed that share about three times as much as 27 platforms abroad. Most of their large changes came in the years from 2022 to 2024."

**F2. drafts/ch7_draft_2026-10-14.md:21 (scope).**
- Text: "In Indonesia, the take rate accounted for about two thirds of a revenue move at the typical pair, against about a quarter abroad."
- Source: 0.658 is the median over the 15 pairs of the Indonesian and regional group, which includes Grab on-demand across Southeast Asia; 0.238 over 158 foreign pairs (`take_rate_share_full.json`). Ch5:85 says "Indonesian and regional platforms". The values match; the scope label does not.
- Proposed: "At the Indonesian and regional platforms, the take rate accounted for about two thirds of a revenue move. At the typical pair abroad, the take rate accounted for only about a quarter of it."

**F3. appendix_notes.md:75–91 (Table A.4 labels).**
- Text: Grab and Shopee rows labelled "Derived value"; Blibli and Bukalapak rows "Direct disclosure" (15 Oct: "conditional country reconstruction" and "direct issuer scope pending").
- Source: AGENTS.md label set and `take_rate_levels.csv`. Shopee's transaction value is an external estimate (Momentum Works) and its revenue is a scenario (assumed take rate 8.4, 10 and 10.8 percent, A.4 note at line 71). Grab's revenue is a direct country disclosure and its transaction value a derived value. Blibli is a segment whose figure includes travel (ch5:46). Bukalapak reports for its whole group. The new labels drop "scope pending" and hide the external estimate.
- Proposed labels: Grab "Revenue direct country disclosure; transaction value derived"; Shopee "Transaction value external estimate; revenue scenario"; Blibli "Direct segment disclosure, scope includes travel"; Bukalapak "Direct company-wide disclosure, scope pending". Optional note sentence: "Each label names the source type of the transaction value and of the revenue in that row."

### Wording that claims more than the source

**O1. abstract.md:9 ("about half" attributed to the registered test).**
- Text: "A test registered before the survey files were opened shows that first-time entry explains only about half of that rise."
- Source: the registered entry test (E5, 2 Oct; run 7 Oct) shows only that too few sellers were new: 13.45 against the 21.5 percent required (ledger B01; Appendix C line 153). "About half" comes from the accounting of the rise, designed after the files were opened and labelled exploratory (Table 5.1 line 22; Ch7:55): 37 to 56 percent of the rise is not explained by entry, so entry net of exits explains 44 to 63 percent (`bps_rise_accounting.json`, Table 5.5). "Registered before the survey files were opened" is itself correct.
- Proposed: "A test registered before the survey files were opened finds too few new sellers to produce that rise. A later, exploratory count shows that first-time entry explains only about half of it."

**O2. drafts/ch7_draft_2026-10-14.md:13 (same period issue as F1, milder).**
- Text: "On the inner link, the choice of revenue changed the conclusion between 2022 and 2024. The Indonesian and regional platforms changed their take rates about three times as much as platforms abroad ..."
- Source: as F1. Ch5:71 supports reading the rejection as a 2022–24 episode, but the next sentence's "three times" covers 2020–25.
- Proposed: "On the inner link, the choice of revenue changed the conclusion, above all from 2022 to 2024."

**O3. drafts/ch7_draft_2026-10-14.md:17 (and ch5:221).**
- Text: "The national figures agree that growth was small where they cover the same sellers."
- Source: BPS's marketplace slice grew 0.2 percent (middle scenario), 2.8 percent (high) and 13.2 percent (low) from 2022 to 2023 (`gel_checks.json` bps_marketplace_value_tn), against Bank Indonesia's −4.7 percent. "Small" holds in two of three scenarios. Ch5:223 gives the range right after its sentence; Ch7 does not.
- Proposed: "Where the national figures cover the same sellers, they agree on small growth in two of three scenarios."

**O4. ch5_results.md:67 (what the shuffle shuffles).**
- Text: "A shuffle of platform labels on pairs of years comes close without passing (p = 0.06)."
- Source: p = 0.0606 (`test_battery.csv` firm_perm_p) matches. The shuffle (`build_numbers.py`, `perm_firm`) moves labels across platforms, each summarised by the median of its pairs, so it works on one median per platform, not on pairs.
- Proposed: "A shuffle of platform labels, using one median per platform, comes close without passing (p = 0.06)."

**O5. drafts/ch7_draft_2026-10-14.md:15 (label missing).**
- Text: "Read as wider coverage, it leaves H2 on its threshold. With those sellers and their sales taken out, more businesses account for about 42 to 54 percent of the growth ..."
- Source: values match (`h2_coverage_adjusted.json`: 41.5–43.0 with 5 percent exits, 53.3–54.5 with none; middle scenario 42.1 and 53.8). The analysis was designed on 16 Oct after all results were known; Ch5:171 and Table 5.1 label it exploratory, Ch7 does not. The abstract (line 9) puts it as a condition, which is fine.
- Proposed: "Read as wider coverage, an exploratory check, the extra count leaves H2 on its threshold."

### ROUNDING-OK (optional tightening)

**R1. drafts/ch6_draft_2026-10-14.md:39.** "At GoTo ... the same arithmetic gives about 1 to 1.4 points on a take rate of about 22 percent." The same arithmetic gives 1.4 (7 percent of group net revenue, Rp0.40tn a quarter, cut by 60 percent, over Rp16.7tn; `cap_prediction.py` docstring; CH6_SOURCES §2). The lower bound, 0.9, is GoTo management's EBITDA estimate (Rp300bn over two quarters), a different source (grade C). Proposed: "At GoTo, where two-wheel rides weigh more, the same arithmetic gives at most about 1.4 points. GoTo's own cost estimate implies about 0.9 points, on a take rate of about 22 percent."

**R2. ch5_results.md:233.** "BPS counted about 0.7 million marketplace sellers that year." Derived: 17.81 percent marketplace use (`bps_descriptives.json`, 2023) × 3.81 million = 0.68 million. No committed row holds it, and the only citation in the sentence is GoTo's. The 14 million is now sourced (see N1 below). Proposed: "Tokopedia alone reported more than 14 million merchants on its marketplace in 2023 (GoTo Gojek Tokopedia 2024b). BPS's survey files put marketplace sellers at about 0.7 million that year, on the author's calculation."

### Other notes (no number change)

- drafts/ch6:49 "who apply for the discount (Ayudiana 2026)": the need to apply comes from Katadata, 12 Aug 2026 (CH6_SOURCES line 96), not from Ayudiana. "Halve" matches Ayudiana ("potongan sebesar 50 persen"). Cite Katadata for the application, or drop "who apply".
- Three different tests print "p = 0.004": the main H1 test (ch5:57, 65; 0.0038), the second market-value run (ch5:119; 0.0039) and H1 without the eight expensing platforms (ch7:49; 0.00353 on rerun). All are right; a reader may confuse them.
- ch6:39 "Grab's on-demand take rate is about 13 percent" is the 2Q26 value (13.3, `cap_prediction.py` BASE). The 2024 annual value in A.3 is 13.83. Say "in the second quarter of 2026" if the period matters.
- ch5:73 listing check: the foreign comparison uses the 15 foreign platforms with years in both windows (`listing_check.json`), not all 27. State the sample if Prof. Kong's scope rule is applied.
- appendix A.4: Blibli revenue cells keep ".00" (122.00, 199.00) while others dropped it. Cosmetic.
- abstract.md:7 states H1 as rejected without the exploratory label of the main test. The registered narrower test points the same way (p = 0.024), and labels live in Table 5.1, so no change is proposed.

## Task 2: status of the 15 Oct MISMATCH and NO SOURCE items

| # | 15 Oct location | Status | Current line and text |
|---|---|---|---|
| M1 | ch5:230 | Fixed | ch5:235 "while its revenue grew by about 20 percent" |
| M1b | ch6:39 | Fixed | ch6:43 "on-demand revenue rose by about 20 percent in the second quarter of 2026" |
| M2 | ch4:69 | Fixed | ch4:69 "A second run adds five segment series and Mercado Libre as a robustness check." (34 firms, `m1_market_value_results.json`) |
| M2b | ch5:116 | Fixed | ch5:119 "A second run adds five segment series, including Grab, GoTo and Sea, and Mercado Libre." |
| M3 | ch6:53 | Fixed | ch6:57 "So the tax reaches at most about 18 to 24 percent of online sales value" |
| M4 | appendix:67 | Fixed | appendix:67 "(about 60 and 40 percent in the text)" |
| M5 | appendix:120 | Fixed | appendix:120 "Three marketplaces, dropping all three 2022–23 comparisons (5 pairs)" |
| M6 | ch5:16 | Fixed | ch5:16 "Extreme values capped (winsorised); a second run" |
| M6b | ch5:114 | Fixed | ch5:117 "or p = 0.16 with extreme values capped" |
| M6c | appendix:164 | Fixed | appendix:165 "and with extreme values capped (p = 0.16)" |
| M7 | ch5:70 | Fixed | ch5:71 "while the large moves came between 2022 and 2024" |
| M7b | ch7:3 | Fixed | ch7:3 "Between 2022 and 2024 the platforms' take rates moved" |
| M7c | ch7:13 | Fixed (see O2) | ch7:13 "the choice of revenue changed the conclusion between 2022 and 2024" |
| M7d | ch7:33 | Fixed | ch7:33 "the rejection of H1 describes a period, 2022 to 2024" |
| M8 | ch5:40 | Fixed | ch5:41 "at 9 or 11 percent, the total wedge is US$40.3 or US$39.9 billion" |
| N1 | ch5:228 | Partly | ch5:233 "Tokopedia alone said that it had more than 14 million merchants in 2023, while BPS counted about 0.7 million marketplace sellers that year (GoTo Gojek Tokopedia 2024b)." The 14 million is verified in `sources/core_public_documents/goto_annual_report_2023.pdf` ("Our e-commerce marketplace connects consumers with over 14 millions merchants"; Indonesian "lebih dari 14 juta merchant"). Still missing: a source-extract row in `tables/src/`, and a label for the derived 0.7 million (R2) |
| N2 | ch1:19 | Not fixed | ch1:19 "Decisions worth trillions of dollars rest on numbers that show a fraction of the activity they are taken to describe." Proposed: "Online sales worth trillions of dollars are described by numbers that show only part of the activity." (UNCTAD's almost US$27 trillion, ch1:11) |
| N3 | ch6:45 | Fixed | ch6:49 "It later required marketplaces to halve the service fee for small sellers of local products who apply for the discount (Ayudiana 2026)." The unsupported late-August claim is gone (see the citation note above) |

## Task 3: headline numbers across abstract, Ch5 and Ch7

| Headline | Source value | Abstract | Ch5 | Ch7 (and others) | Verdict |
|---|---|---|---|---|---|
| US$43bn / 3bn / 40bn | 43.23 / 3.16 / 40.07 (C34–C36) | :7 (43, 3) | :12, :30 | :9 | Consistent |
| About 7 percent | 7.31 | — | :12, :30 | — | Consistent |
| About three times | 0.201 / 0.062 = 3.3 | :7, with a 2022–24 label (F1) | :13, :51, :75 | :13 (O2) | Value consistent; period label wrong in abstract |
| 27 percent rise | 27.40 | :9 | :3, :135, :139, :143 | — | Consistent |
| 13.45 against 21.5 | 13.45; 21.5 (B01, E5) | — | :21, :143 ("about 13") | :31; appendix:153; ch3:156–158; ch4:93 | Consistent |
| About half | 37–56 percent not explained; entry 44–63 (exploratory) | :9, attributed to the registered test (O1) | :3 | :3, :15; ch1:27; ch6:73 | Value consistent; abstract attribution wrong |
| 42 to 54 percent; 71 percent (H2) | 41.5–43.0 / 53.3–54.5; 71.07 (log) | :9 in words only | :23, :171 (42, 54); :139 (71), :141 (71 on the other count, 2023–24) | :15 (42 to 54, unlabelled, O5) | Consistent |
| 1 in 20 | 5.42 (T6-03) | :11 | — | :25; ch6:5, :55 | Consistent |
| About 8 percent | 17.8 × 0.47 = 8.4 | — | — | :25; ch6:61 | Consistent |
| 0.6 and p = 0.002 | 0.600; 0.0016 (M12) | — | :115 | :21 (0.6 only); appendix:166 | Consistent |
| p = 0.004 / 0.022 | 0.0038 / 0.0221 | — | :57–58, :65 | appendix:101 | Consistent (see note on three p = 0.004 values) |
| Two thirds against a quarter | 0.658 / 0.238 | — | :85 | :21, scope "In Indonesia" (F2) | Value consistent; Ch7 scope wrong |

## All checked numbers (file:line → source)

Tags: no tag = MATCH; [R] = ROUNDING-OK; [X] = MISMATCH; [O] = wording flag on a matching number.

### abstract.md (11)
- :7 — 2023; three platforms; about US$3bn (3.16, C35); US$43bn (43.23, C34); "between 2022 and 2024" [X] F1; about three times (3.3, H01/H02); 27 platforms abroad (`h1_extended_firms.csv`).
- :9 — 27 percent (27.40, `bps_recompute.json`); 2023; about half (37–56 not explained, `bps_rise_accounting.json`) [O] O1.
- :11 — 1 in 20 (5.42, `gel_checks.json`, T6-03).

### symbols.md (16)
- :6–20 — Table 3.1 for V, R, m, f, s, g (ch3:31–39); Equation (1) W (ch3:57); (2) E and E = 1/m − 1 (ch3:65; ch3:38 "author's own measure"); (3) D (ch3:73); (5) Δln (ch3:97); (7) N, Y (ch3:141); (8) MV, β_V, β_m (ch3:188); Section 3.4 H1, H2 (ch3:112). All 16 agree.

### ch1 (3)
- :7 — 2022–2023; 53 percent (53.2, C13); 9 percent (−8.9, C12). Only the word "commerce" changed.

### ch2, ch3 (0)
- Changed lines carry citation years and cross-references only.

### ch4 (15)
- :5 — three marketplaces; GoTo controlled Tokopedia until 2024 (`tables/src/policy_timeline_web.csv` 2024-01-31: TikTok takes 75.01 percent).
- :7 — three survey rounds (`LICENSED_DATA.md`).
- :9 — five platform series; three report incentives.
- :43 — 10 percent; 9 to 11 percent; 2020 to 2025 (`take_rate_levels.csv`).
- :69 — five segment series and Mercado Libre (`m1_market_value_results.json` firms_robust_added; 34 firms, 162 firm-years).
- :75 — two counts for 2023 (3,816,750 and 3,934,981); 2023–24 split with both (90.29 and 70.95, C29); 2022–23 on the matched count (`bps_microdata_results.json`).
- :113 — 2022 rate; about US$20,000 (Rp300m / 14,849.85 = 20,202); about US$34,000 (Rp500m = 33,670).

### ch5 (86)
- :3 — 27 percent; 2023; about half (37–56).
- :13 — about three times (3.3).
- :23 — about 42 to 54 percent (middle 42.1 and 53.8; range 41.5–54.5, `h2_coverage_adjusted.json`).
- :41 — 9 or 11 percent; US$40.3bn (40.29); US$39.9bn (39.86); 11.5 percent (11.465); US$39.8bn (39.754). Pairing now correct.
- :67 — three marketplaces; eight foreign; p = 0.024 (C47); p = 0.06 (0.0606) [O] O4; 0.10 (C48); 0.98 (C49).
- :71 — p = 0.19 (Q03); 2023 to 2026; 2022 to 2024 (PART3:48, PREREG 8 Oct, `timing_check.json`).
- :73 — one or two years after listing (`listing_check.json`: Bukalapak 1, Grab 1, Tokopedia 1, Blibli 1, GoTo 2); first three years; median 0.07 (0.0697); 0.08 (0.0837); p = 0.24 (0.244); 2022 to 2024; one of seven (`timing_check.json` 2022-24 lower-income firms_larger_in_window 1 of 7); all four (4 of 4).
- :85 — about two thirds (0.658); about a quarter (0.238); about 95 percent (94.5) (`take_rate_share_full.json`).
- :117 — 1 percent → about 0.3 (0.334); p = 0.20 (0.202); p = 0.16 (0.162 winsorised).
- :119 — five segment series; p = 0.004 (0.0039); about 0.6 (0.630); about 0.1 (0.071).
- :121 — after the 2000 crash (Davis 2002 abstract, `FINANCE_FRAMING.md` §1b).
- :167 — about 1.4 percent (1.37, C11-02); 306 thousand (305.6); 4.6 (C11-03); 2024 edition.
- :169 — 2023; 41 percent (40.6); about US$53bn (Rp783tn / 14,849.85 = 52.7); about US$72bn (Rp1,100.87tn / 15,236.88 = 72.25); 2022 file; 2022 starters; 25 to 30 (25.5–29.8); 15 to 17 (14.6–16.7); about −4 (−4.3); 53 to 59 (53.4–59.4) (`gel_checks.json` value_increase_split_pct).
- :171 — about 54 (53.3–54.5, no exits); about 42 (41.5–43.0, 5 percent exits); 5 percent a year (`bps_rise_accounting.json` reference); more than 50 percent (H2 threshold, ch3 Table 3.2); 34 to 47 (33.6, 46.6 count only).
- :177 — 2023 count; 2022 count; 2020 to 2022; about 450 thousand (449.6, `bps_newly_counted_profile.json`); 458 thousand (458.0).
- :201 — 2023; about 29 (28.63); about 12 (12.25); 2020 to 2022 fall (23.5 → 20.7); 2023 fall (15.2) (`bps_descriptives.json`).
- :209 — 26 to 40 (25.7–40.4, E1); 2022; 79 (79.3); half to double (validation rule, ch4:107); about twice (1.95, PREREG 3 Oct); about 23 times (23.38).
- :215 — about 40 (39.9); seven countries (`wb_crosscountry.csv`, 7 rows); about 9 (Malaysia 9.1, Thailand 8.7).
- :221 — 2023; about −5 (−4.7); about 41 (40.6).
- :233 — more than 14 million merchants in 2023 (GoTo annual report 2023, local PDF; no extract row); about 0.7 million (0.68 derived) [R] R2; 2023.
- :235 — four quarters to mid-2026 (R06); 2 percent (R02); 8 percent (8.3, R05); about 20 percent (20.3, CH6_SOURCES §2).

### ch6 (29)
- :39 — 20 to 8 percent (CH6_SOURCES §2, Kompas quote "80 ... minimal 92 persen"); about 2 percent (0.06 × 2,214 / 6,463 = 2.06); at most about a quarter of a point (2.06 × 0.12 = 0.247; `cap_prediction.py` v1 docstring); about 13 percent (13.3, 2Q26); about 1 to 1.4 points [R] R1; about 22 percent (21.52).
- :41 — May Day 2026 (1 May 2026); "must be below 10 percent" (CNN Indonesia 9 Oct 2026, CH6_SOURCES line 77).
- :43 — about 20 percent (20.3); second quarter of 2026; 2 percent (2.0); "8%" quote (GoTo call); about 22 (21.52); about 18 (18.25).
- :49 — mid-2025 (20 Jul / 11 Aug 2025); 2026 rises (May 2026); TikTok Shop took over Tokopedia in 2024; halve (50 persen, Ayudiana).
- :53 — 0.5 percent; about US$34,000; October 2026 (DJP 2026c); four marketplaces; begun in August 2026, stopped, refunded (DJP 2026b, PENG-46).
- :57 — 23 to 26 (22.6–25.6); 2022; 77 to 94 (77.4–93.8, E8); about 18 to 24 (17.52–23.58, `part6_checks.json`); about a fifth; four collectors.

### ch7 (40)
- :3 — 2022 to 2024; 2023; about half.
- :13 — 2022 to 2024 [O] O2; about three times (3.3).
- :15 — about half; 2023; about 42 to 54 [O] O5; 50 percent; five of six (V10).
- :17 — 2023 [O] O3.
- :21 — about two thirds (0.658) [X] F2 scope; about a quarter (0.238); 28 listed platforms (M12-01); 1 percent → about 0.6 (0.600).
- :33 — p = 0.19; 2023 to 2026; 2022 to 2024.
- :37 — 5.8 points; 2020 to 2022; limit 5; 3.3 points; about US$7,300 (Rp111m / 15,236.88 = 7,285, the 2023 rate as in ch5:213); about US$6,600 (Rp100m = 6,563); about US$4,000 (Rp60m = 3,938); two of three scenarios.
- :41 — 2026 rules; a day before (1 Oct collection, 2 Oct registration); seven countries (X3 withdrawn, PREREG 16 Oct addendum).
- :49 — eight of the 27 (`INCENTIVE_ACCOUNTING.md`); p = 0.004 (0.00353 on rerun, rounds to 0.004).
- :51 — 2021 and 2023 files; 2020 and 2022; 2024 file describes 2023; about US$3.4m (Rp50bn / 14,849.85 = 3.37m); 19 sample rows (P02); 18 to 39 percent (P06, P07).
- :55 — 2023 rise; 10 to 15 percent (305.6 and 458.0 over 2,996 thousand).
- :67 — 2026 results.

### appendix_notes.md (261)
- :13–31 (A.1, 19 renamed rows) — 38 values (pairs, medians) unchanged and matching `h1_extended_firms.csv`. Ticker-to-name mapping checked (ASAPQ Waitr, DIBS 1stDibs, RBA RB Global, SEAT Vivid Seats, VCSA Vacasa, etc.).
- :41 — six own-goods and four no-V exclusions.
- :47, :51 (A.2) — 6 values unchanged (Blibli 4 / 0.25 / 0.00; Tokopedia 1 / 0.52 / 0.00).
- :59–65 (A.3) — 7 window labels and 49 values unchanged, matching `growth_decomposition.csv`.
- :67 — 8 rupiah values, 2,144,271, 60.6 / 39.4, "about 60 and 40" (M4 fixed): 12 items.
- :75–91 (A.4) — 102 values (year, V, R, W, m, E for 17 rows) unchanged, matching `take_rate_levels.csv`; row labels [X] F3 (one item).
- :110, :114 (B) — Blibli and Tokopedia leave-one-out rows: 0.169 / 0.0137 / 0.0364; 0.169 / 0.0164 / 0.0409.
- :120 — 14.411; 7.105; 0.0248; 0.2222; 5 pairs; all three 2022–23 comparisons (`test_battery.csv`; M5 fixed).
- :131 — one third (0.333); 67 to 69 (0.674, 0.69); 0.10; 26 foreign platforms.
- :153 (E5) — 21.5; 2023; 2 Oct; 13.45; 2024 publication; near 18 percent (17.9, PREREG 16 Oct (2)); first used 8 Oct; test ran 7 Oct.
- :161 (F3) — one third; 3 Oct; 39.9; 13.0 under the first coding (PREREG 3 Oct night).
- :162 (X3) — 3 Oct; 16 Oct addendum; Malaysia 9.1; Thailand 8.7.
- :165 (M1) — 8 Oct; p = 0.20; p = 0.16 (M6c fixed); 34 platforms; p = 0.004.
- :167 (L) — L of 1; 2 Oct (commit 95a322b, 2 Oct 00:07 +0800); 2 of 2; 0.117 against 0.10 (`l_test.csv`); rank correlation 0.20 (0.195); p = 0.43 (0.432, `l_rank_test.csv`).
