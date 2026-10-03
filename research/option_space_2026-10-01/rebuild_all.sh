#!/usr/bin/env bash
# Rebuilds every committed table from committed inputs, then checks the claims ledgers.  Run from anywhere: bash research/option_space_2026-10-01/rebuild_all.sh
# Needs pandas, numpy, scipy, statsmodels (set PYTHONPATH if they live outside the system python).  Takes about 3 minutes (bootstrap steps).
# NOT rebuilt here (licensed or scratch inputs, see tables/claims_ledger_v2_NOT_REPRODUCIBLE_FROM_REPO.txt): analyst_extrapolation.py, multiples_dispersion.py,
# event_study*.py, v_definition_map.py, timing_table.py's market column.  Extraction CSVs in tables/src are the verified inputs (quote-checked when they were made).
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
echo "== ledgers"; "$PY" - <<'PYEOF'
import pandas as pd
for f in ("tables/claims_ledger.csv", "tables/claims_ledger_v2.csv", "tables/claims_ledger_v3.csv"):
    d = pd.read_csv(f); print(f, d.status.value_counts().to_dict())
PYEOF
