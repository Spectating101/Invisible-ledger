# October 2026 research package (index)

Status: research evidence for the frozen proposal (`papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`). It is not a plan to change the concept. `ATLAS.md` is an older options map; its spine options are superseded and its numbers are checked by `tables/claims_ledger.csv`.
Rebuild everything: `bash research/option_space_2026-10-01/rebuild_all.sh` (about 3 minutes; deterministic; checks `claims_ledger.csv` 55/55, `claims_ledger_v2.csv` 32/32, `claims_ledger_v3.csv` 20/20, `claims_ledger_v4.csv` 29/29 and `claims_ledger_v5.csv` 29/29).
**All results in one place, in the proposal's order: `FINDINGS.md` (7 Oct 2026).**
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

## Story spine (4 Oct 2026; thesis question, hypotheses and measures unchanged)
1) **Inside the app (H1).** Platform revenue and sales split apart about 3x more in Indonesia than in 27 foreign firms (firm-level p 0.004; holds on the proposal's D measure and dropping any one Indonesian firm). Why: young platforms in price-sensitive markets buy growth with discounts (exploratory pattern, holds ex-Indonesia); not a worldwide law (spin-off tests S1, S2 falsified).
2) **Apps vs the nation (objective 3).** Rulers that see mainly the apps grow about 5% a year; rulers that see all sellers, parcels or tax receipts grow 17-40%; the two state offices moved in opposite directions in 2023 (BI -4.7%, BPS +40.6%).
3) **Outside the apps (H2 and the extra analyses).** Unregistered sellers who use social media are many and tiny (median Rp60m a year), 70% keep no books; 39.9% of Indonesia's formal firms have neither a website nor online tax filing, the highest of seven countries. BPS microdata (2020-2023, 7 Oct): the share of sellers keeping financial statements fell from 23% to 15%, marketplace use fell from 22% to 18%, and the typical existing seller's online revenue was flat in 2023; entry was too small to explain BPS's published +27% seller count (E5 falsified), so part of BPS's 2023 jump is a change in who is counted.
4) **The state (why it matters, proposal section 6).** The 8% cap, the June 2026 discount rule, the marketplace tax, the data-handover rule and the 2026 census act on numbers from layers 1-3; the tax base differs about 5x by ruler; sellers with Rp300m+ a year are 28% of marketplace sellers but hold 77-92% of marketplace value (E8), so the tax can reach most of the money but few of the sellers, and the money is small (0.04-0.21% of the 2026 target).
Scope rule: criticise only platform-economy numbers we tested; GDP and fiscal debates (LPEM, public commentary) are one paragraph of context. No causal claims about policy. Failures are reported (S1, S2, W3; coding fixes disclosed in PREREGISTRATION.md).

## Data discipline
Every extraction in `tables/src/` passed `check_rows.py` (quote must appear verbatim in the source text; stated number must appear in the quote). Grok drafted the extractions; none is used unchecked. Licensed LSEG data (prices, consensus, market caps) is not committed; scripts that use it are listed in `tables/claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt`.
Known data limits: only four independent high-discount firm-segments disclose incentive amounts (Grab, GoTo, Tokopedia, Blibli 3P); annual counts and value exist together only for Indonesia (BPS); the Shopee Indonesia series is Momentum Works shares times its Indonesia total with an assumed 10% take rate; Perpres 27/2026 and Kepmenhub 667/2022 texts are unverified (GoTo cites Ministerial Decree 532/2026 for the cap; news names Perpres 27/2026 on protection of online transport workers, signed 1 May 2026; a 21 May 2026 petition said its text was not public). GoTo's 2Q26 values in `three_rulers.py` are the rounded figures quoted in `PREREGISTRATION.md`.
