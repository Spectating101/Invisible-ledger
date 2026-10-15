# Consistency audit of the thesis draft, 15 October 2026

Read-only audit. No chapter was edited. Scope: `papers/thesis_2026-10/` Chapters 1 to 5, `drafts/ch6_draft_2026-10-14.md`, `drafts/ch7_draft_2026-10-14.md`, `appendix_notes.md`, `references.md`, checked against the README "Writing rules" and "Vocabulary" sections and the AGENTS.md "Thesis story and writing standard".

Short names used below: `ch1` to `ch5` = the chapter files; `ch6`, `ch7` = the 14 Oct drafts; `app` = `appendix_notes.md`; `refs` = `references.md`. `ch5:40` means line 40 of that file.

Items marked **(open in COLD_READ / FIX_LIST)** were already raised in this folder and are still in the text. Every other item is new in this audit. Numbers were checked against `tables/bps_recompute.json`, `tables/bps_microdata_results.json`, `tables/h1_points_vs_log.json`, `PREREGISTRATION.md` and `FINDINGS.md` where noted.

---

## Part 1. Errors a committee would catch first

Ranked by how quickly an examiner would find them and how much they would damage trust.

| # | Where | Problem | Closest fix |
|---|---|---|---|
| 1 | ch6:45, ch7:65 vs ch6:95, ch7:59 | Contradiction on what the 2026 predictions can show. 6.2 ends "How far the cap moves the companies' take rates is the subject of the predictions in Section 6.5", and 7.5 says "The outcomes will show how far the commission cap moved the companies' take rates". But 6.5 says "The predictions describe company numbers, not the effect of the cap", and 7.4 says the thesis "makes no claim about its effects". | Make 6.2 and 7.5 say the outcomes show how the companies' take rates moved in the first quarter under the cap, not how far the cap moved them. |
| 2 | ch5:40 | Table 5.2 note reverses the Shopee scenarios. A lower assumed take rate means lower revenue and a larger wedge. At 9 percent the total wedge is about US$40.3 billion, and at 11 percent about US$39.9 billion. The note says "at 9 or 11 percent, the total wedge is US$39.9 or US$40.3 billion". The 11.5 percent case (US$39.8 billion) is right. | "At 9 percent, the total wedge is US$40.3 billion; at 11 percent, US$39.9 billion." |
| 3 | app:67 vs ch1:9, ch5:102 | Appendix A.3 says the Tokopedia line-by-line split appears as "61 and 39 percent in the text". The text says "about 60 percent" (ch1:9, ch5:102) and "about 40 percent" (ch5:102). | Change the appendix note to "(about 60 and 40 percent in the text)". |
| 4 | ch5:66 vs app:115-116 | Wrong pairing of a p-value. 5.2 gives the narrower test "with one median per platform" (Mann–Whitney p = 0.024) and then says "The shuffle of platform labels comes close without passing (p = 0.06)". In Appendix B, the one-median-per-platform row (app:116) has no shuffle value. The 0.0606 belongs to the pairs-of-years version (app:115). | Report the shuffle for the one-median version, or say that 0.06 comes from the pairs-of-years version. |
| 5 | ch7:47 vs app:123 | Ch7 says Shopee's and Grab's constructed Indonesian amounts "stay out of the tests". Appendix B has a check that includes them ("Five Indonesian and regional series including constructed Grab and Shopee (12 pairs)", p = 0.0006). | "...stay out of the main tests; one check in Appendix B adds them." |
| 6 | ch7:53 vs ch4:79, ch5:162, app:140 | Ch7 says "The files carry no area or design variables". Ch4 says there is "no area variable below the province", and 5.7 and Appendix B.2 run a 34-province analysis. | "The files carry no area variable below the province and no design variables." |
| 7 | ch5:166, ch5:226 | The currency conversion makes the growth figures look wrong. 5.7 converts BPS's online sales to "about US$53 billion" (2022) and "about US$72 billion" (2023). That is +36 percent, while the same chapter says +41 percent four times. In 5.10, US$72 billion (2023) and US$81 billion (2024) imply +12 percent, against the stated +17 percent. Each year is converted at its own World Bank rate, and the rupiah fell. | Add one note at first use: growth is computed in rupiah, and the dollar amounts use each year's rate, so they do not reproduce the growth. |
| 8 | ch4:75 vs ch5:136-138 | Promise only half kept. Ch4 says "BPS prints two counts of businesses for 2023, so the thesis computes the split with both and reports both." 5.6 reports both counts only for 2023 to 2024 (90 or 71 percent). For 2022 to 2023 it gives one value (71 percent). `bps_recompute.json` holds no second-count split for 2022 to 2023. The two different 71s (2022–23 main; 2023–24 alternative) also read like a copying error. | Compute the 2022–23 split on the other count and report it, or narrow the promise in 4.6 to 2023–24. Then say that the two 71s are a coincidence. |
| 9 | ch4:137 vs app:142-168 | Ch4 says registration "applies to the entry test, the scenario rules for value, the comparison with Bank Indonesia and the market-value test ... Appendix C lists them with their dates." Appendix C has no row for the bracket scenario rules or the validation rule. They were registered (PREREGISTRATION.md:35-36). | Add a row "Scenario rules and validation (2 Oct 2026): passes, annual reading, 1.95 times". |
| 10 | ch5:13, ch5:66, ch7:45 vs ch4:137, app:142 | A fourth evidence label. Table 5.1 and 5.2 call the narrow H1 test "planned in advance". That label is not one of the three defined in 4.10 (registered, exploratory, descriptive), and Appendix C has no row for the test. Ch4.3 never says that the narrow test came first. 4.10 says the larger test "was set up after a first test on the three marketplaces", but 4.3 lists the three-marketplace version only as a check. | Choose one: list the narrow test in Appendix C with its date and call it registered, or call it "the first test" everywhere. Also add one sentence to 4.3 saying the main test is exploratory. |
| 11 | ch5:188, ch5:208 vs app:158, PREREGISTRATION.md:73-75 | The text reports a different statistic from the registered test. 5.9 says the World Bank results "were registered" and "show the same thin records" (70 percent keep no written records). Registered W1 predicted the opposite direction of comparison: social-media users keep written records *more* often than other firms (29.9 against 12.3 percent), and it held. Also, W3 was registered as "calibration, not a test of the thesis", yet Appendix C ("Falsified"), 5.9:208 and 7.3:37 treat it as a failed prediction. | Report W1 as registered (more often than other informal firms, though 70 percent still keep none). Label W3 as a registered calibration check that missed. |
| 12 | ch7:47, ch7:49, ch7:51 | Results appear for the first time in the Conclusion, with no method in Ch4 and no result in Ch5. (a) The check on how foreign platforms book discounts ("Eight of the 27 ... p = 0.004"; app:104-105). (b) Top sellers above US$3.4 million holding 18 to 39 percent of marketplace value on 19 rows (also app:138). (c) "Grab revised some figures between filings. The thesis takes each year from the latest filing" is a data rule missing from 4.1 and 4.10. It also sits uneasily with 4.10's "A restatement ... is reported and never overwritten" (ch4:135). (d) The education coding (ch7:51) concerns a result that Ch5 never reports. **(b, c, d open in COLD_READ)** | Move (a) into 4.3 and Appendix B, and give it one sentence in 5.2. Move (b) into 5.9 with a pointer to Appendix B.2. Put (c) in 4.1 or 4.10. Drop (d), or report the education result in 5.8. |
| 13 | ch6:35, ch6:49, ch6:59, ch6:61, ch6:43; refs | Ch6 has claims without a source or a Ch4 method. Unsourced: the cap's terms ("From July 2026 ... 8 percent", ch6:35); the presidential regulation sending delivery fees to another ministry (ch6:35); the August 2026 start, stop and refund of the tax (ch6:49); "0.2 percent of the government's tax target for 2026" (ch6:61); the census "news reports" row in Table 6.1 (ch6:20). Table 6.1 names Transport Minister Decree KP-PHB 532/2026 and Presidential Regulation 27/2026, and `refs` has no entry for either. Survey results with no Ch4 method or Ch5 home: 13 percent of off-marketplace sellers want to join a marketplace (ch6:59); GoTo incentives falling from 11 to 4 percent of transaction value and Grab's 10 percent (ch6:43). Ch4.4 covers annual windows, not these quarterly series. | Add citations and reference entries (CH6_SOURCES.md has the sources). Add one sentence each to 4.4 and 4.8, or move the survey number to 5.9. |
| 14 | ch1:5 vs ch6:21, ch6:29 | The 2023 rule is worded two ways. Ch1 says "The government then banned transactions on social media platforms". Ch6 says "Ban on payments on social media" and "Bars social media platforms from handling payments for sales". **(open in COLD_READ)** | One wording in both chapters. Ch6's wording matches the primary text. |
| 15 | ch6:45 | Inside one paragraph: "It later required marketplaces to halve the service fee for small sellers" is followed by "The rules on the take rate ... leave the largest marketplace fees free". The claim "a rule not yet in force by late August 2026" is cited to an article dated 8 July 2026 (Ayudiana 2026; refs:13). | "...and leave the largest marketplace fees uncapped." Cite a source dated after August, or say "not yet in force in July 2026". |
| 16 | ch6:85, ch6:95 | Table 6.2, P5: "grows by at least 5 percent; the prediction fails only below 2 percent". The table does not say what an outcome between 2 and 5 percent counts as. **(open in FIX_LIST C)** | "Holds at 5 percent or more; fails below 2 percent; undecided in between." |
| 17 | ch4:35 vs app:9 | The own-goods rule is stated two ways. Ch4: "drops any year in which own goods exceed half of revenue". Appendix A.1: a pair counts when "the later year is not one in which own goods exceed half". The Ozon exception (ch4:37) follows only from the appendix version. | Use the appendix wording in 4.1. |
| 18 | app:55 | Appendix A.3 says Blibli's incentives "are marked `out` of the main sample in the panel". Blibli is in the main H1 sample (Table 4.1, app:47, Table 5.3) and in Table 5.4. | Say which sample Blibli is out of (the incentive split with audited data). |
| 19 | ch4:135, ch5:37, ch4:25-29, app:75-91 | Source labels do not match. The 4.10 list (direct company disclosure, direct segment disclosure, external estimate, derived value, conversion, scenario) has no "direct country disclosure", which Table 5.2 uses for Grab. Appendix A.4 uses panel codes ("conditional country reconstruction", "direct issuer scope pending", "direct indonesia aligned segment"). For Bukalapak and Blibli these conflict with Table 4.1 ("Direct company disclosure", "Direct segment disclosure"). | Add "direct country disclosure" to 4.10. Map the A.4 labels to the 4.10 list. |
| 20 | app:136-140 | Appendix B.2 ("Where the 2023 break sits") is filed under "Appendix B. The checks on the test of H1", and no chapter points to it. 5.7 reports its province and sampling-error results with no appendix pointer. | Move B.2 into its own Appendix (survey checks) and point to it from 5.7. |
| 21 | ch3:88 | "Equation (4) shows that D is the change in the take rate divided by its starting level." Equation (4) also has the factor (1 + g(V)). **(open in COLD_READ)** | "...divided by its starting level, scaled by one plus the growth of transaction value." |
| 22 | ch5:204 | "The annual reading of the brackets passes the validation rule, at about twice BPS's total." The rule (ch4:107) allows "between half and double". "About twice" reads as a fail. The actual value is 1.95 (`bps_microdata_results.json`). | "...at just under twice BPS's total, inside the limit." |
| 23 | ch5:218 | "grew by about 0.2 percent in the middle scenario. Across the scenarios it grew by 0.2 to 13 percent." The middle scenario sits at the bottom of the range. PREREGISTRATION.md:112 gives the high scenario as 2.8 percent, so the scenarios are not ordered low to high. **(open in COLD_READ)** | Give all three values, or explain the order. |
| 24 | ch6:57 vs ch5:192, ch5:190 | Two different 18s. Ch6 says "Marketplace sellers were about 18 percent of online sellers in 2023". In 5.9, 18 percent is the *value* share in 2023, and the 2023 *seller* share (17.8) appears only in Figure 5.5 and app:176. "About a fifth" also names both the marketplace value share (5.9) and the value the tax can reach, 17 to 24 percent (ch6:5, ch6:53). **(first half open in COLD_READ)** | In 5.9, give the 2023 seller share in the text. In 6.3, write "17 to 24 percent" without "about a fifth", or say it is the same order as the marketplace share. |
| 25 | ch5:166 | The value accounting has no method in 4.7 and the arithmetic is hidden. Entrants account for 25 to 30 percent and unexplained sellers for 15 to 17 percent. That leaves 53 to 60 percent, not "53 to 59", unless the ranges pair differently. **(arithmetic open in COLD_READ)** | Add one sentence to 4.7 (size proxies from the 2022 file). Show which ends of the ranges pair. |
| 26 | ch7:37 | "Three predictions on sellers' records and sales failed" includes the Bank Indonesia comparison (RBI), which is not about sellers' records or sales. | "Three further predictions failed narrowly or in part." |
| 27 | ch1:25 vs ch1:43, ch3:168 | "A further analysis estimates how many sellers..." against "four further analyses" two paragraphs later. **(open in COLD_READ)** | "Four further analyses follow; one estimates how many sellers..." |
| 28 | ch4:43 vs app:69-91 | Ch4 says the thesis "repeats the exercise for every platform-year between 2020 and 2025 that the filings allow". Appendix A.4 gives each series separately and no three-platform sum for any other year. All three platforms have 2022 values, so a 2022 sum is possible. | Report the 2022 sum, or reword the promise as "gives the wedge of each series for every year". |
| 29 | ch7:21; ch3:120 | "In Indonesia, the take rate accounted for about two thirds" (ch7:21) and "Changes in Indonesia far larger than abroad" (Table 3.2). The group is "Indonesian and regional" everywhere else. **(ch7 open in COLD_READ)** | "In the Indonesian and regional group..." |
| 30 | ch5:50, ch5:56 vs ch4:47 | Log units are converted two ways. Ch4 turns a log change of 0.52 into "68 percent". 5.2 calls log changes of 0.20 and 0.06 "about 20 percent" and "about 6 percent". By Ch4's rule, 0.20 is about 22 percent. | Say "about a fifth" (or 22 percent) and "about 6 percent", or note that small log changes are read as percent. |
| 31 | refs:3, refs:7; ch1:5; ch2:29; ch2:41 | Citation keys. Ch1 cites "AFP 2023", but the entry is "Agence France-Presse". Ch2 has "Gombovic" where `refs` has "Gombović". Table 2.1 has "IASB 2014" where the text uses the full name. The `refs` header says "cited works only", but three entries have no author-year citation anywhere: BPS-Statistics Indonesia (2023), Government of the Republic of Indonesia (2026), Ministry of Trade (2026). Table 6.1 refers to them only by regulation number. | Cite them author-year in the Table 6.1 note. Align the keys. |

### Cross-reference check (task item 1): result

Every pointer of the form "Section X.Y", "Table X.Y", "Figure X.Y", "equation (n)" and "Appendix X" resolves to an existing target. None points to a missing item. The pointers that are wrong in substance are rows 4, 9, 12, 20 and 28 above, plus these smaller ones:
- ch6:17 (Table 6.1, "Measured in 5.9" for the marketplace tax). The tax's reach (1 in 20 sellers, 17 to 24 percent of value) is measured in 6.3 from the method in 4.8. Section 5.9 gives only the inputs.
- ch5:216 and ch6:29 each claim to be the event "with which Chapter 1 began". Chapter 1 opens on a general paragraph, then Tanah Abang (ch1:3-5). The BPS against Bank Indonesia disagreement and the ban both appear in ch1:5. Acceptable, but say "the disagreement Chapter 1 described".
- ch6:31: "in the order of Figure 3.1, from the take rate outward". Figure 3.1 shows revenue, platform commerce and all online commerce; it does not show the take rate.
- ch4:137: "The test with the larger groups in Section 4.3 belongs here". Section 4.3 does not say that the test is exploratory or that it came second (see row 10).
- Figures 5.4 and 5.5 have values in Appendix D, but only Figure 5.3's caption (ch5:128) points there.

---

## Part 2. Numbering, placement and explanation of tables and figures (item 2)

- **Numbering is clean.** Tables 2.1; 3.1 to 3.3; 4.1 to 4.3; 5.1 to 5.5; 6.1 and 6.2. Figures 3.1 and 5.1 to 5.5. Equations (1) to (8), in order, with no gaps or duplicates. Every figure file exists in `figures/`. The README line "Figure 3.1 still to be drawn" (README:43) is out of date.
- **Placement.** Figure 5.5 (ch5:196) appears before its first mention in the text (ch5:200). The three paragraphs above it (ch5:190-194) discuss its content without pointing to it. Every other table and figure is mentioned before or next to where it sits.
- **Explanation.**
  - Figure 5.2 is mentioned only in parentheses (ch5:102). Its two panels are explained, but the figure is never named in a sentence of its own.
  - Figure 5.4: the text (ch5:172-178) names long-running businesses, older owners and places outside Java. The fourth bar, food and lodging or making goods (app:174), is never mentioned. **(open in COLD_READ)**
  - Figure 5.1 is introduced as "the three measures side by side" (ch5:74). "The three measures" already means the wedge, the ecosystem ratio and growth divergence (ch3:52-86). See Part 4.
  - Table 4.3 has no sentence on its rows beyond "with what each one counts" (ch4:117). The adjacent figures row is explained only in 5.10.
  - The six measures behind Figure 5.3 are listed only in Appendix D (app:172), not in 4.9 or 5.5. **(open in COLD_READ)**
  - Table 6.2 lists predictions in date order (P1, P3, P5, R1, R2, P2, P4, R3), and the text never explains the P and R prefixes. **(open in COLD_READ)**
  - Table 5.3 gives group values in log units (0.20, 0.06) under a "percent" reading in the text (row 30).

---

## Part 3. Promises, and results without a method (item 3)

Promises not kept, or kept only in part: rows 1, 8, 9, 12, 13, 20 and 28 above, plus:
- ch4:113: "labels each rule by the status of its text: primary text read, announced, or reported in the news only". In Table 6.1 (ch6:15) the commission-cap row reads "Decree in force from July 2026; presidential regulation released 8 October 2026; neither text public". That is none of the three labels, and "released" sits next to "not public". The census row says "News reports" in place of "reported in the news only".
- ch4:139: "Chapter 7 states what these data cannot show." Ch7:61 says only where the licensed data are held. The limits of the data themselves are spread over ch7:49-55. Acceptable, but point to 7.4 by name.
- ch4:11 promises that Ch4 follows Ch5's order. The method for 5.5 (six measures against household spending) sits in 4.9, the last methods section, while 5.5 comes before H2.
- ch4:53 lists the checks in Appendix B. The two incentive-booking rows (app:104-105) are not on the list (row 12a).

Results reported without a method in Chapter 4:
- ch5:132: obstacles to selling ("lack of demand ... 41 percent against 35 percent"), and the shares of sellers whose sales rose or fell.
- ch5:166: value accounting of the 2023 rise (row 25).
- ch5:162: channel split of cohort growth (chat-only +13 percent, marketplace +0.3 percent). Ch4.7 mentions "channels" in one clause. Fine.
- ch5:222: "Those that cover mainly platforms grew by 5 to 7 percent". The figures are never named (they are Bank Indonesia +7.3, Momentum Works +5.2 and e-Conomy +5.1, per PREREGISTRATION.md:112).
- ch6:43, ch6:59, and ch7:47-51 (rows 12 and 13).

---

## Part 4. Terms and vocabulary (item 4)

**Defined more than once**
- BPS: ch1:5 ("the national statistics office, BPS"), ch3:13, ch3:41 (Table 3.1), ch4:7. Keep ch1:5 only, plus Table 3.1 if the glossary stays.
- OECD: ch2:19 ("[OECD]") and again ch2:27 ("The OECD, a group of mostly high-income countries").
- Invisible wedge: ch1:7, ch3:37 (Table 3.1), ch3:54, and again at ch7:43 with a different meaning: "the part of each sale that a platform passes on to sellers, drivers and others". That is the right idea, but it is a new wording of the definition. Keep the caveat and drop the redefinition.
- Ecosystem ratio, "the author's own measure": stated at ch3:38 and again at ch3:68.
- Take rate: ch3:33 (Table 3.1) and again at ch3:68 ("the take rate, the share of each sale that the platform keeps").
- Growth divergence: ch3:40 (Table 3.1) and ch3:70. A glossary plus a text definition is defensible. Make the glossary the single definition and let the text say "growth divergence (Table 3.1)".

**Used before it is defined**
- "registered": used at ch1:33 and ch4:101, defined at ch4:137.
- "rank correlation": used at ch4:99, defined at ch5:162, one sentence after its first use in that paragraph. **(open in COLD_READ)**
- "window": used at ch4:63 and ch5:84, never defined. **(open in COLD_READ)**
- Momentum Works: named at ch4:43, described only in Table 4.3 (ch4:128).
- QRIS: defined only in Table 4.3 (ch4:130); used bare in prose at ch5:224.
- "Blibli 3P Retail" (app:47, app:64): "3P" is never explained. The text says "third-party retail".
- Correctly ordered: transaction value (ch1:7), the wedge (ch1:7), H1 and H2 (ch1:25), the entry test (ch1:25), first-time entry (ch1:25-27), take rate (first use in Table 3.1), ecosystem ratio and growth divergence (first use in Table 3.1), GMV, GTV and TPV (Table 3.1 only, never used again; good).

**Used inconsistently (README Vocabulary)**
- "Sales" used for a platform's transaction value (README: never): ch1:7 ("revenue and sales moving apart inside one company"), ch2:7 (twice), ch2:9, ch2:13, ch2:21 ("platform sales"), ch2:41 and ch2:42 (Table 2.1, "Platform sales and platform revenue differ"), ch2:47, ch5:230 ("Platform sales do not always keep pace"). Chapter 2 does this throughout. Use "transaction value" or "the commerce it carries".
- "Pricing", "repricing" and "price changes" used for a change in the take rate: ch5:15 (Table 5.1, "Pricing, not more commerce, moved revenue"), ch5:70, ch5:102, ch5:118, ch7:13 ("pricing moved revenue"; "price changes of a similar size in points"), ch7:17, ch7:33, ch7:35, ch7:71. The same idea is "growth from a higher take rate" at ch3:175, ch5:17 and ch5:114. Pick one. **(open in FIX_LIST D)**
- "Thin take rate" (ch4:53, ch5:14, ch5:72, ch5:78) against "a much thinner share of each sale" (ch7:13).
- "Records" (README: a platform's data on sales) is also used for sellers' bookkeeping: ch3:197 ("Record keeping"), ch5:24 and ch5:188 ("records are thinner there"), ch7:37 ("sellers' records"). Use "financial statements" or "bookkeeping" for sellers.
- "Measure" (README: a yardstick, or one of the thesis's three): Figure 5.1's panels are called "the three measures" (ch5:74). **(open in COLD_READ)**
- "Discounts and incentives" (ch1:9). Table 3.1 defines incentives as including discounts. Elsewhere the text alternates "fees or discounts" (ch1:33, ch3:90) and "fees or incentives" (ch7:21).
- BPS's total Y has five names: "national e-commerce value" (ch3:121, ch3:146, H2), "online sales value" (ch5:136), "online sales" (ch1:5, ch1:15), "BPS e-commerce value" (app:172), and "BPS's" alone (ch5:216). Fix one name in Table 3.1.
- Sample name: "Indonesian and regional" in most places; "Indonesia" at ch3:120 and ch7:21 (row 29).
- "Chain" appears only in Ch3's sense or as "supply chain" (ch2:29) and "chain restaurants" (ch6:107). No violation.
- "Gap" is never used for the wedge. ch5:114 and ch5:116 use it for the difference between β_V and β_m, a different quantity. Acceptable, but "difference" would avoid any echo.

---

## Part 5. Evidence labels across Table 5.1, the sections, Chapter 7 and Appendix C (item 5)

| Result | Table 5.1 | Section text | Ch7 | Appendix C | Match? |
|---|---|---|---|---|---|
| Wedge about US$40 billion | Descriptive | 5.1, no label (default) | 7.1, no label | none | Yes |
| H1 rejected, main test | Exploratory, "narrower test planned in advance" | 5.2:64 exploratory; 5.2:66 "planned in advance" | 7.4:45 exploratory | narrow test absent | **No**: "planned in advance" is not a defined label (row 10) |
| Thin take rate explains much of it | Exploratory | 5.2:72 exploratory | 7.1:13, stated as fact | app:133 exploratory | Partly: Ch7 drops the label |
| Take rate, not commerce, moved revenue | Descriptive | 5.3, no label | 7.1:13 | none | Yes |
| Quarterly H1 test | a check only | 5.2:70 "registered prediction" | 7.3:33, failed prediction | Q1, "a robustness check" | Partly: one result, three names |
| Market value moves with transaction value | Registered; holds | 5.4:112 | 7.2:21 | M2 holds | Yes |
| Take-rate growth valued less | Registered; does not hold | 5.4:114 | 7.3:35 | M1 falsified | Yes |
| No boom in 2023 | Descriptive; registered for sellers' sales | 5.5:130 | 7.1:15 | E6 holds | Yes |
| H2 holds | Descriptive | 5.6, no label | 7.1:15 | none | **Tension**: 4.10 defines descriptive as "numbers without a test", but H2 is one of the two hypotheses. Say "descriptive: an arithmetic split, not a statistical test". |
| Entry test fails | Registered; fails | 5.6:140 | 7.3:31 | E5 falsified | Yes |
| About half the rise unexplained | Exploratory | 5.7:146 | 7.4:53 | none | Yes |
| Profile of the extra sellers | Exploratory | 5.8:172 | 7.1:15, no label | none | Partly |
| Channels and records | Registered and descriptive | 5.9:188 also names an exploratory finding (5.9:202) | 7.3:37 | E1, E2, E2b, E2c, E7, W1 to W3, F, X | **No**: Table 5.1 omits the exploratory part. W1 is reported against its registered direction, and W3 was a calibration (row 11). |
| National figures agree only on the same sellers | Registered, mixed, and descriptive | 5.10:220 | 7.3:37 | RBI mixed | Yes |
| Incentive-booking check | absent | absent | 7.4:47 exploratory | none | **No** (row 12a) |
| 2026 predictions | — | 6.5 registered | 7.3:39, 7.5:65 | not yet scored; tax start withdrawn | Yes. The withdrawal is consistent at ch6:93, ch7:39 and app:167. |
| Scenario rules for value | — | 4.10 says registered | — | absent | **No** (row 9) |

---

## Part 6. Numbers with more than one home (item 6)

Repeats beyond the Ch1 preview and the Ch7 summary. The first location is the home; the others repeat it.
- GoTo, second quarter of 2026: revenue +21 percent and transaction value +2 percent at ch5:230 and ch6:39 (household spending 8 percent only in ch5). The figures now agree, but there are still two homes.
- 96 percent of sellers use chat or social media: ch5:190 and ch6:29.
- Marketplace value share of 23 to 26 percent in 2022: ch5:192 and ch6:53. The 47 percent who use a shopping marketplace and the 43 percent who use only Gojek or Grab: ch5:194 and ch6:57.
- Tokopedia's incentives fell "about a third": ch5:102 and ch6:43.
- "Four of the seven windows": ch5:100 and ch6:41.
- Tokopedia 2022–23 (+53 percent revenue, −9 percent transaction value, take rate 1.5 to 2.5 percent, +68 percent, log 0.52): ch3:84 (worked example), ch4:47 (worked example), ch5:90 and ch5:124, app:51 and app:63. Ch3 and Ch4 each use it as an example. Keep one worked example (Ch3) and let 4.3 point to it.
- BPS 2022 total of about US$53 billion: ch4:107 and ch5:166.
- Exemption of about US$34,000 and bracket line of about US$20,000: ch4:113, ch6:23, ch6:49 and ch6:51. Ch6 points back to 4.8 once (ch6:49) but repeats the amounts.
- Shares keeping financial statements: 28.63 and 12.25 percent at ch4:79 (a validation check), and about 29 and 12 percent at ch5:200.
- Exit rate of about 5 percent a year: ch4:97 and ch5:146.
- "About a fifth" (marketplace value share): ch1:27, ch5:46, ch5:192, ch6:5, ch6:69, ch7:11, plus ch6:5, ch6:53 and ch7:25 for the tax reach. Ch5 itself says it twice (5.1 and 5.9).
- Marketplace value growth of about 1.5 percent in 2023–24: ch5:194 and ch5:218.
- BPS +41 percent: ch5:124, ch5:136 and ch5:216 (three times inside Ch5).
- Returners equal to 10 to 15 percent of the 2022 count: ch5:184 and ch7:53.
- Ch7.3 restates details, not headlines: 5.8 and 3.3 points (ch7:37 = ch5:206); US$7,300, US$6,600 and US$4,000 (ch7:37 = ch5:208); p = 0.19 and 0.20 (ch7:33-35). Keep the outcome and point to Appendix C for the values.
- ch3:90 uses 17 percent as the thick take rate in a worked example, which is the foreign median result of ch5:74. The match is harmless, but a reader may take it as a result stated early.

---

## Part 7. Style rules (item 7)

**Banned words.** None found: "therefore", "rather than", "indicator" and "Overall" do not occur in Chapters 1 to 7 or the appendix.

**Rhetorical questions.** ch4:95: "A failed entry test raises a second question: how much of the rise does first-time entry not explain?" Make it a statement: "A failed entry test leaves part of the rise unexplained by first-time entry." The research question (ch1:21) and the three numbered questions (ch2:47-49) are allowed.

**Hedging inside the story (Ch1 to 6)**
- ch1:15: "so platform and survey figures are likely to part. The events of 2023 suggest that they did."
- ch5:142: "so the shortfall is, if anything, understated".
- ch5:200: "the survey appears to have counted the same kinds of seller"; "The fall in 2023 may partly reflect the chat-only sellers".
- ch5:184: a whole paragraph of caveats (returners, linked histories, wording change, exits).

Caveats repeated outside the limitations chapter (AGENTS: caveats once, in Ch7):
- The wedge is not missing output: ch1:7, ch3:60, ch7:43.
- Returners cannot be ruled out: ch4:101, ch5:23, ch5:184, ch7:49, ch7:53.
- Market value is not a stock return: ch4:69, ch7:57.
- Company explanations are not tested: ch3:108, ch4:63, ch7:47.
- Assumptions of the sampling-noise check: ch5:164, ch7:53.
- BPS's wording changes: ch5:184, ch5:190, ch5:198, ch7:51.

The Claims rule allows one statement of evidence strength where a result is given. The repeats beyond that are the ones to cut.

**Regulation numbers and exact dates in narrative prose.** None in prose. All regulation numbers and day-level dates are in Table 6.1, the Table 6.2 note or the appendix, which is allowed. Borderline:
- "DAC7 directive" (ch2:27, ch6:103) is a directive code.
- Ch6 prose carries ten month-level dates (ch6:3, ch6:35 twice, ch6:45 twice, ch6:49 twice, ch6:67, ch6:71; also ch5:230). Each passes the rule, but together they make 6.2 and 6.3 read like a timeline.

**Bare rupiah in prose.** None. Rupiah amounts appear only in Table 6.1 and its note, and in the appendix. ch4:61 uses the word "rupiah" without an amount.

**Long sentences.** 13 sentences run over 30 words and 65 over 25, out of 1,047 sentences in Chapters 1 to 7 (mean 15.8 words). Counts exclude author-year citations and bold list labels. The 25 longest:

| Words | Where | Opening |
|---|---|---|
| 45 | ch2:19 | National accounts separate the sale between a buyer and a seller from the platform's fee, and they count only the fee... |
| 39 | ch4:59 | Wherever a company discloses both its gross fees and its incentives, the thesis splits the growth of revenue over a window into three parts... |
| 35 | ch1:21 | Measuring what the current figures miss begins with one question: how much economic activity remains invisible... |
| 34 | ch4:5 | On the platform side, the thesis reads revenue and transaction value from annual reports, audited statements and earnings releases... |
| 33 | ch7:49 | At the top, sellers with sales above about US$3.4 million a year rest on 19 sample rows... |
| 32 | ch4:17 | Under the second rule of Section 3.1, the definition cancels out of a take rate's yearly changes... |
| 32 | ch4:9 | Five platform series report revenue and transaction value in the same year, three of them report what they pay out in incentives... |
| 32 | ch1:19 | The ambition of this thesis is to bring the rest into view: to show how much of the online economy the current figures miss... |
| 31 | ch7:37 | The value share of sellers without financial statements fell by 5.8 points between 2020 and 2022... |
| 31 | ch4:113 | The thesis reads each legal text where it is published, and it labels each rule by the status of its text... |
| 31 | ch2:48 | This follows from Section 2.2, which shows that figures differ but does not test whether they grow for the same reasons... |
| 31 | ch1:33 | It shows why this matters for growth as well as scale: the larger the wedge is next to revenue... |
| 31 | ch1:19 | Most online commerce is missing from the platform figures on which companies are valued and sellers are taxed... |
| 30 | ch7:5 | It then says what the answer adds for those who use the figures, reports the predictions that failed... |
| 30 | ch4:139 | The repository records the size and checksum of each BPS and LSEG file and of the World Bank cross-country query... |
| 30 | ch4:7 | BPS publishes a few totals, and the thesis obtained the answers behind them for three survey rounds... |
| 30 | ch3:195 | The reach of a rule built on platform records depends on how online selling divides between marketplaces and channels... |
| 30 | ch3:136 | Growth driven by new sellers can take place in channels that platform accounts do not cover... |
| 29 | ch7:25 | Each of the other recent rules acts on one part of the take rate or of the national figure... |
| 29 | ch7:15 | In the same year, five of six measures of buying through platforms grew more slowly than household spending... |
| 29 | ch3:86 | The wedge gives the size of what revenue leaves out, and at a marketplace that keeps a few percent of each sale... |
| 29 | ch2:47 | This follows from Section 2.1, which explains why the share is small and can move but does not test... |
| 28 | ch7:59 | The reach of the marketplace tax is an upper limit, because BPS's bracket line sits below the exemption... |
| 28 | ch7:59 | The legal texts behind the commission cap were not public when the thesis was written... |
| 28 | ch7:37 | The mean sales of unregistered firms that use social media were about US$7,300 a year... |

With citations counted, ch1:15 (38 words), ch2:9 (36), ch2:13 (34) and ch1:7 (32) also pass 30.

**Openers that lean on the previous paragraph** (README: openers stand alone):
- "This follows from..." starts each of the three numbered items (ch2:47-49).
- ch2:11: "Accounting rules add a second reason."
- ch3:110: "Equation (6) also shows..."
- ch3:160: "Sellers who stopped would have to be replaced as well..."
- ch4:37: "Two platforms sit close to that line."
- ch4:59: "The second step splits..."
- ch5:74: "The two groups differ..."
- ch5:114: "The second registered prediction..."
- ch5:116: "A second run adds..."
- ch5:160: "The count behaved normally again..."
- ch6:25: "Equation (6) shows where the first two rules act."
- ch6:31: "The sections that follow take the other rules..."
- ch7:35: "The second market-value prediction..."

No paragraph opens on "These", "Both" or "Such". "This thesis" (ch1:19) and "This chapter" (ch7:5) name their subject and pass.

**Other rule checks**
- ch1:27: the "In brief" answer runs to four sentences. The README asks for three.
- Working notes left in the appendix: "Details moved from Chapter 5." (app:131), "full company names are to be added" (app:9), and script paths throughout. Fine while drafting; strip them before assembly.

---

## Part 8. Section endings (item 8)

Sections that end flat, on a fact or a table with no handover and nothing left open:
- Ch3 opening (ch3:21): ends on "The third question is answered by a further analysis." The same paragraph maps objective 3 to question 2 and question 3 to a further analysis, which is hard to follow.
- 4.1 (ch4:37) ends on the pair counts. 4.2 (ch4:43) ends on the robustness list. 4.3 (ch4:53) ends on the list of checks. 4.5 (ch4:69) ends on "as a robustness check". 4.8 (ch4:113) ends on the labels for legal texts.
- 4.6 and 4.9 end on a table, with no closing line.
- 5.2: the last text sentence (ch5:74) hands over well, but the section ends on Figure 5.1's caption.
- 5.4 (ch5:118): "Revenue and transaction value come from the platforms' own reports, and market value from share prices. The national figures give a separate view of the same commerce." This is a weak bridge to 5.5. **(open in COLD_READ)**
- 7.1 (ch7:17): the market-value result is attached to the end of the outer-link paragraph, although it belongs to the inner link.
- 7.4 (ch7:61): ends on "regional series labelled as such".
- 1.2 (ch1:39) and 6.6 (ch6:109) end on summary statements without a handover. That is acceptable for 1.2, the last content section before the map, and for 6.6, the end of the chapter.

Sections that end well: 2.1 to 2.3, 3.1, 3.3 to 3.6, 4.7, 4.10, 5.1, 5.3, 5.5 to 5.10, 6.1 to 6.4, and 7.5.

---

## Part 9. Chapters 6 and 7 against Chapters 1 to 5 (item 9)

Contradictions in fact or wording (details above):
1. The cap's effect: the predictions are said both to show how far the cap moved take rates and not to show its effect (row 1).
2. The 2023 rule: "banned transactions" (ch1:5) against "ban on payments" (ch6:21, ch6:29) (row 14).
3. Shopee and Grab constructions "stay out of the tests" (ch7:47), but Appendix B includes them (row 5).
4. "No area variables" (ch7:53) against the province analysis (ch4:79, ch5:162) (row 6).
5. 18 percent means sellers in ch6:57 and value in ch5:192 (row 24).
6. "In Indonesia" (ch7:21) against "Indonesian and regional" (row 29).
7. New facts first seen in Ch7: Grab revisions, top-seller concentration, education coding, incentive booking (row 12).
8. ch7:37 groups the Bank Indonesia comparison under sellers' records (row 26).

Checked and consistent:
- **Tax reach.** At most 1 in 20 sellers and about a fifth of value: ch6:5, ch6:51-53, ch7:25, matching the method in ch3:195 and ch4:113.
- **Record reach.** At most about 8 percent of sellers: ch6:57 and ch7:25. 17.8 × 0.47 = 8.4.
- **Grab's share under the cap.** 6 percent of regional rides, about 2 percent of on-demand: ch6:37, used only there.
- **Tax start.** 1 October 2026: ch6:17, ch6:93, ch7:39, app:167, refs:41. The withdrawn prediction is described the same way in all three places.
- **Tax revenue.** US$60 million and US$300 million: ch1:15 and ch6:61.
- **Repricing period.** 2021 to 2024: ch5:70, ch7:3, ch7:33.
- **Entry share.** 13 percent: ch5:140, ch7:31.
- **Tokopedia's incentives.** "Only marketplace that reported its incentives" (ch6:43) fits ch4:9 and ch4:63.
- **TikTok Shop and Tokopedia.** TikTok Shop's takeover of Tokopedia in 2024 (ch6:45) fits Tokopedia's series ending in 2023 (Table 4.1). Chapter 1 still leaves TikTok Shop closed (ch1:5) and never mentions the takeover. **(open in COLD_READ)**
- **Commission cap timing.** July 2026 (ch6:15, ch6:35), with the texts not public (ch6:15, ch7:59). The Table 6.1 cell pairs "in force" with "not public"; one plain clause would avoid a defence question.
- **GoTo's take rate of about 22 percent in the second quarter of 2026** (ch6:39) fits 5.2's revised sentence that Grab and GoTo keep shares closer to those abroad (ch5:74).
