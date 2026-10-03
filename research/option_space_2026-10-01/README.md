# October 2026 research package (index)

Status: research evidence for the frozen proposal (`papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`). It is not a plan to change the concept. `ATLAS.md` is an older options map; its spine options are superseded and its numbers are checked by `tables/claims_ledger.csv`.
Rebuild everything: `bash research/option_space_2026-10-01/rebuild_all.sh` (about 3 minutes; deterministic; checks `claims_ledger.csv` 55/55, `claims_ledger_v2.csv` 32/32 and `claims_ledger_v3.csv` 20/20).
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

## Story spine (3 Oct 2026; thesis question, hypotheses and measures unchanged)
Four layers, small to large. 1) Inside one platform (H1): revenue and sales drift apart, mostly because discounts are given and withdrawn; revenue can show a boom that did not happen. 2) Platforms vs the nation (objective 3): platform sales, platform revenue, BPS, Bank Indonesia and official household spending tell different stories; BI says e-commerce fell 4.7% in 2023 while BPS says it rose 40.6%. 3) Outside the platforms (H2, channel and record-keeping analyses): most growth comes from new sellers outside the apps, many without books; the BPS microdata (2020, 2022, 2023) tests this business by business. 4) The state acting (why it matters, proposal section 6): the 8% cap, the June 2026 discount rule, the marketplace tax, the data-handover rule and the 2026 census act on numbers from layers 1-3. Scope rule: criticise only platform-economy numbers we tested; GDP, fiscal and manufacturing debates (LPEM, public commentary) are one paragraph of context. No causal claims about policy.

## Data discipline
Every extraction in `tables/src/` passed `check_rows.py` (quote must appear verbatim in the source text; stated number must appear in the quote). Grok drafted the extractions; none is used unchecked. Licensed LSEG data (prices, consensus, market caps) is not committed; scripts that use it are listed in `tables/claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt`.
Known data limits: only four independent high-discount firm-segments disclose incentive amounts (Grab, GoTo, Tokopedia, Blibli 3P); annual counts and value exist together only for Indonesia (BPS); the Shopee Indonesia series is Momentum Works shares times its Indonesia total with an assumed 10% take rate; Perpres 27/2026 and Kepmenhub 667/2022 texts are unverified (GoTo cites Ministerial Decree 532/2026 for the cap; news names Perpres 27/2026 on protection of online transport workers, signed 1 May 2026; a 21 May 2026 petition said its text was not public). GoTo's 2Q26 values in `three_rulers.py` are the rounded figures quoted in `PREREGISTRATION.md`.
