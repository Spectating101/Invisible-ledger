# October 2026 research package (index)

Status: research evidence for the frozen proposal (`papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`). It is not a plan to change the concept. `ATLAS.md` is an older options map; its spine options are superseded and its numbers are checked by `tables/claims_ledger.csv`.
Rebuild everything: `bash research/option_space_2026-10-01/rebuild_all.sh` (about 3 minutes; deterministic; checks `claims_ledger.csv` 55/55, `claims_ledger_v2.csv` 32/32, `claims_ledger_v3.csv` 20/20, `claims_ledger_v4.csv` 29/29, `claims_ledger_v5.csv` 30/30, `claims_ledger_v6.csv` 14/14, `claims_ledger_v7.csv` 26/26 and `claims_ledger_v8.csv` 27/27, `claims_ledger_v9.csv` 9/9, `claims_ledger_v10.csv` 7/7).
**All results in one place, in the proposal's order: `FINDINGS.md` (7 Oct 2026).**
**Groundwork, version 3 (8 Oct 2026, tag `parts-1-7-v3-frozen-2026-10-08`; the 2023 seller-count finding corrected to about half, stale lines fixed, dated notes folded in):** `PART1_PROBLEM_AND_STAKES.md` (problem, who uses the numbers, timing, gaps, publication assessment), `PART2_FRAMEWORK.md` (what each indicator covers vs how it counts; chapter order), `PART3_H1_GROUNDWORK.md` (H1 and the 2023 verdict), `PART4_H2_GROUNDWORK.md` (H2: 2023 a break year in BPS's count; who is outside every indicator); `PART5_OBJ3_GROUNDWORK.md` (comparing the indicators; frozen 8 Oct, tag `part-5-groundwork-frozen-2026-10-08`); `PART6_WHY_IT_MATTERS_GROUNDWORK.md` (the 2026 rules, how far each reaches, scheduled tests); `PART7_ANSWER_AND_LIMITS.md` (answer to the research question, what failed, limits). Groundwork complete; next: the cut list and writing.
Pre-registered tests (cap, headroom flag, BPS statistics, microdata estimands): `PREREGISTRATION.md`. Do not edit it; add dated addenda only.

## Evidence map
| Question | Script | Output | Verified inputs |
|---|---|---|---|
| How much revenue growth is commerce, fee or discount pull-back | `growth_decomposition.py` | `tables/growth_decomposition.csv` | `tables/l_panel.csv` |
| Discount leverage L and the pre-registered test | `l_rule_preregistration.py`, `l_panel.py` | `tables/l_*.csv` | `tables/src/*_extraction.csv` |
| H1 headline and robustness (3 firms and regional tier) | `build_numbers.py`, `h1_regional_tier.py` | `tables/test_battery.csv`, `tables/h1_*.csv` | repo `outputs/`, `data/` |
| Blibli marketplace repricing, Shopee drift | `blibli_discount_split.py`, `shopee_quarterly.py` | `tables/blibli_3p_quarterly.csv`, `tables/shopee_quarterly_take_rate.csv` | Blibli and Sea extractions |
| Platforms vs BPS | `bps_bridge.py`, `bps_scope_digital_goods.py` | `tables/bps_bridge*.csv` | BPS levels, GoTo, Momentum Works |
| Rulers across ASEAN | `asean_ruler_table.py`, `h2_malaysia.py` | `tables/asean_ruler_table.csv` | `tables/src/asean_*_extraction.csv`, World Bank FX |
| Timing: funding vs company vs policy | `timing_table.py` | `tables/timing_table.csv` | `tables/src/events_extraction.csv` |
| Definitions of V (GMV/GTV/TPV) | `v_definition_map.py` | `tables/v_definition_map.csv` | quotes from filings |
| Cap forward test | `cap_prediction.py` (`score_v2`) | printed | Q3 2026 releases (GoTo 27 Oct; Grab and Sea November) |
| Three rulers: official household spending vs platform sales vs revenue, by quarter | `three_rulers.py` | `tables/three_rulers_quarterly.csv` | `tables/src/oecd_qna_idn_2021_2026.csv` (BPS national accounts via OECD), GoTo, Grab, Sea series |
| Two state rulers: Bank Indonesia vs BPS e-commerce | `yardsticks.py` | `tables/yardsticks_bi_bps.csv` | BI and BPS figures (sources in script) |
| Marketplace tax base under four rulers | `tax_base_rulers.py` | `tables/tax_base_rulers.csv` | BPS, BI, Momentum Works, e-Conomy, World Bank FX |
| Policy and growth-debate timeline (2017-2026) | (table) | `tables/src/policy_timeline_web.csv` | news and official pages; `status` column says what is verified |
| 3 Oct numbers recomputed | `claims_ledger_v3.py` | `tables/claims_ledger_v3.csv` | the three tables above |
| Spin-off paper universe (listed platforms reporting V and R) | `publishable_track/universe_scan.py` | `publishable_track/universe_scan.csv` | SEC EDGAR full-text search |
| H1 vs 27 foreign firms; D measure; leave-one-out; market-income pattern (exploratory) | `h1_extended.py` | `tables/h1_extended_*.{csv,json}` | thesis panel + `tables/src/spinoff_g*_extraction.csv` (1,188 quote-checked numbers, 29 firms) |
| Spin-off tests S1-S3 (pre-registered; S1, S2 falsified) | `publishable_track/spinoff_tests.py` | `tables/spinoff_results.json` | same extractions |
| Eleven rulers of the online economy ("both cannot be true") | `consistency_grid.py` | `tables/consistency_grid_*.csv` | `tables/src/digital_rulers_annual.csv` (status per row) |
| World Bank informal and formal surveys, Indonesia 2023 (W1-W3, F1-F3) | `wb_tests.py` (licensed data) | `tables/wb_tests_results.json` | WBES microdata, not committed |
| Cross-country formal surveys, 7 countries (X2, X3) | `wb_crosscountry.py` (licensed data) | `tables/wb_crosscountry.csv` | WBES microdata, not committed |
| BPS e-commerce microdata tests E1-E8, RBI (locked code, run 7 Oct 2026; E5, E7 falsified) | `bps_microdata_tests.py` | `tables/bps_microdata_results.json` | SILASTIK files 2021, 2023, 2024 (licensed, not committed) |
| BPS microdata descriptive numbers (records, marketplace path, apps, incumbents) | `bps_descriptives.py` | `tables/bps_descriptives.json` | same files |
| 3Q26 scoring of P1-P5 and R1-R3 | `score_q3_2026.py` | printed | GoTo 27 Oct; BPS GDP early Nov; Grab and Sea mid-Nov |
| H1 with quarterly pairs (robustness; falsified) | `h1_quarterly.py` | `tables/h1_quarterly_*` | committed quarterly tables |
| Wedge changes split into volume and monetization | `wedge_split.py` | `tables/wedge_split*` | `tables/transitions_master.csv` |
| 7 Oct numbers recomputed | `claims_ledger_v5.py` | `tables/claims_ledger_v5.csv` | BPS aggregates, tables above |
| Draft exhibits, one per layer (plus BPS's own answers) | `exhibits.py` | `exhibits/*.png` | tables above |

## Story spine (updated 8 Oct 2026; thesis question, hypotheses and measures unchanged; chapter order H1, H2, Objective 3, why it matters)
1) **Inside the app (H1).** Platform revenue and transaction value split apart about 3x more in Indonesia than at 27 foreign platforms (firm-level p 0.004; main sample alone p 0.06 under the strictest test). Why: platforms raised their take rate in 2022-24 by cutting incentives and raising fees (Grab mostly repricing; GoTo's cut in 2024), soon after all four listed in 2021-22; specific to Indonesian and regional platforms, not a worldwide wave. In 2023, 5 of 6 Indonesia-only measures of buying grew less than household spending, 3 fell.
2) **The national count (H2 and the additional analyses).** H2 holds on BPS's published numbers, but 2023 was a break year: about half of the +27.4% in sellers (37-56%, depending on how many sellers stopped) was existing chat-and-social sellers counted for the first time, the rest real entry (513 thousand started in 2023; cohorts grew instead of shrinking; at least 306 thousand newly counted); 2024 was normal entry. Most of BPS's 2023 value growth cannot be traced to what respondents reported (existing sellers' mean -4.3%; net down in 2023 after net up in 2022). Who is outside every indicator: about 96% sell through chat or social media; book-keeping falling; Indonesia has the most formal firms without a digital trail of seven countries.
3) **Between the indicators (Objective 3).** Indicators seeing mainly the platforms grow about 5% a year; BPS much faster. Overlapping slices (BPS's marketplace slice, half food and ride merchants) agree on slow growth, so the disagreement sits outside marketplaces. Sizes cannot be reconciled (definitions; BPS thin at the top).
4) **Why it matters (proposal section 6).** The 2026 rules act on how activity is counted or captured: the ride-hailing commission cap (Gojek and Grab rides only), the discount rule, the marketplace tax (collects from at most about 5% of online sellers and about a fifth of online value; identifies every marketplace seller, about 18% of sellers), the data rule and the census. No causal claims.
Scope rule: criticise only platform-economy numbers we tested; GDP and fiscal debates (LPEM, public commentary) are one paragraph of context. Failures are reported (S1, S2, W3, E5, E7, the quarterly test; coding fixes disclosed in PREREGISTRATION.md).

## Data discipline
Every extraction in `tables/src/` passed `check_rows.py` (quote must appear verbatim in the source text; stated number must appear in the quote). Grok drafted the extractions; none is used unchecked. Licensed LSEG data (prices, consensus, market caps) is not committed; scripts that use it are listed in `tables/claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt`.
Known data limits: only four independent high-discount firm-segments disclose incentive amounts (Grab, GoTo, Tokopedia, Blibli 3P); annual counts and value exist together only for Indonesia (BPS); the Shopee Indonesia series is Momentum Works shares times its Indonesia total with an assumed 10% take rate; Perpres 27/2026 and Kepmenhub 667/2022 texts are unverified (GoTo cites Ministerial Decree 532/2026 for the cap; news names Perpres 27/2026 on protection of online transport workers, announced 1 May 2026; it was still not on JDIH Setneg on 7 Oct 2026, when later Perpres were). GoTo's 2Q26 values in `three_rulers.py` are the rounded figures quoted in `PREREGISTRATION.md`.
