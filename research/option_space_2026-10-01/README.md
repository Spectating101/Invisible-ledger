# October 2026 research package (index)

Status: research evidence for the frozen proposal (`papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf`). It is not a plan to change the concept. `ATLAS.md` is an older options map; its spine options are superseded and its numbers are checked by `tables/claims_ledger.csv`.
Rebuild everything: `bash research/option_space_2026-10-01/rebuild_all.sh` (about 3 minutes; deterministic; checks `claims_ledger.csv` 55/55 and `claims_ledger_v2.csv` 32/32).
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
| Cap forward test | `cap_prediction.py` (`score_v2`) | printed | Q3 2026 releases (November) |

## Data discipline
Every extraction in `tables/src/` passed `check_rows.py` (quote must appear verbatim in the source text; stated number must appear in the quote). Grok drafted the extractions; none is used unchecked. Licensed LSEG data (prices, consensus, market caps) is not committed; scripts that use it are listed in `tables/claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt`.
Known data limits: only four independent high-discount firm-segments disclose incentive amounts (Grab, GoTo, Tokopedia, Blibli 3P); annual counts and value exist together only for Indonesia (BPS); the Shopee Indonesia series is Momentum Works shares times its Indonesia total with an assumed 10% take rate; Perpres 27/2026 and Kepmenhub 667/2022 texts are unverified (GoTo cites Ministerial Decree 532/2026 for the cap).
