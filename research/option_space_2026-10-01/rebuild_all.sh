#!/usr/bin/env bash
# Rebuilds every committed table from committed inputs, then checks the claims ledgers.  Run from anywhere: bash research/option_space_2026-10-01/rebuild_all.sh
# Needs pandas, numpy, scipy, statsmodels (set PYTHONPATH if they live outside the system python).  Takes about 3 minutes (bootstrap steps).
# NOT rebuilt here (licensed or scratch inputs, see tables/claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt): analyst_extrapolation.py, multiples_dispersion.py,
# event_study*.py, v_definition_map.py, timing_table.py's market column; wb_tests.py, wb_crosscountry.py, bps_microdata_tests.py, bps_descriptives.py, bps_frame_check.py, bps_cohort_check.py, bps_h2_cheap_checks.py, gel_checks.py and part5_checks.py
# (licensed microdata; their committed aggregate outputs are checked by claims_ledger_v4.py to v10).
# Also not run here: cap_prediction.py and score_q3_2026.py (scoring after the 3Q26 releases), l_rule_preregistration.py (the registered rule, text only),
# peers_quarterly.py, mmyt_incentives.py and tokopedia_segment.py (built once from the local filing corpus; outputs committed), verify_extraction.py and
# check_rows.py (acceptance checks used when each extraction was made).  Extraction CSVs in tables/src are the verified inputs (quote-checked when they were made).
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
step() { echo "== $1"; "$PY" "$1"; }
step build_numbers.py          # proposal numbers, test battery, claims_ledger.csv (49 + payment claims)
step l_panel.py                # discount-leverage panel, pre-registered test, rank tests
step growth_decomposition.py   # revenue growth = volume + fee + discount pull-back
step h1_regional_tier.py       # H1 robustness with the regional tier (bootstrap, about 1 minute)
step blibli_discount_split.py
step shopee_quarterly.py
step bps_bridge.py
step bps_scope_digital_goods.py
step asean_ruler_table.py
step h2_malaysia.py
step repricing_split.py
step grab_quarterly.py
step goto_on_demand.py
step claims_ledger_v2.py       # recomputes the 2 Oct headline numbers; prints any CHECK rows
step three_rulers.py           # official household spending vs platform sales vs revenue, by quarter
step yardsticks.py             # Bank Indonesia vs BPS e-commerce
step tax_base_rulers.py        # marketplace tax base under four rulers
step claims_ledger_v3.py       # recomputes the 3 Oct numbers
step publishable_track/spinoff_tests.py   # 29-firm panel (quote-checked extractions) and the spin-off tests
step h1_extended.py            # H1 vs 27 foreign firms, D measure, leave-one-out, exploratory market-income pattern
step consistency_grid.py       # eleven rulers of the online economy
step exhibits.py               # draft exhibits, one per story layer (exhibits/*.png)
step claims_ledger_v4.py       # recomputes the 3-4 Oct numbers (World Bank results from committed aggregates)
step h1_quarterly.py           # H1 with quarterly pairs (robustness; falsified)
step wedge_split.py            # wedge changes: volume part vs monetization part
step claims_ledger_v5.py       # BPS microdata aggregates, quarterly H1, wedge split
step h1_groundwork.py          # Part 3 groundwork: Grab pricing vs mix, Tokopedia two views, 2023 verdict
step claims_ledger_v6.py       # Part 3 groundwork numbers
step timing_check.py           # exploratory: were 2022-24 swings specific to Indonesian platforms?
step bps_cohort_2024_published.py  # cohort check 2023->2024 from the published 2024 table
step listing_check.py          # exploratory: do take rates swing more in the first years after listing?
step claims_ledger_v7.py       # cheap checks of 8 Oct (timing; BPS cohorts from committed totals; GoTo 2024)
step claims_ledger_v8.py       # linking checks (gel_checks.json, from licensed data)
step part6_checks.py           # Part 6: reach of each 2026 rule (tax by sellers and value; cap within Grab on-demand)
step claims_ledger_v9.py       # Part 6 numbers
step bps_rise_accounting.py    # 2023 seller rise: new entrants vs sellers counted for the first time (exit sensitivity)
step claims_ledger_v10.py      # rise accounting
step rq_closing_checks.py      # sampling noise vs the 2023 surplus (BPS published RSEs); platform channel share of online value
step claims_ledger_v11.py      # closing checks
echo "== ledgers"; "$PY" - <<'PYEOF'
import pandas as pd
for f in ("tables/claims_ledger.csv", "tables/claims_ledger_v2.csv", "tables/claims_ledger_v3.csv", "tables/claims_ledger_v4.csv", "tables/claims_ledger_v5.csv", "tables/claims_ledger_v6.csv", "tables/claims_ledger_v7.csv", "tables/claims_ledger_v8.csv", "tables/claims_ledger_v9.csv", "tables/claims_ledger_v10.csv", "tables/claims_ledger_v11.csv"):
    d = pd.read_csv(f); print(f, d.status.value_counts().to_dict())
PYEOF
