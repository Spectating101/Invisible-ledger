"""Claims ledger v10 (8 Oct 2026): the 2023 seller-rise accounting (bps_rise_accounting.json).
Run: python3 claims_ledger_v10.py -> tables/claims_ledger_v10.csv"""
import json
import pandas as pd
T = "tables/"; a = json.load(open(T + "bps_rise_accounting.json")); s = a["scenarios"]
claims = [
 ("A10-01", "BPS 2022-23 rise in online sellers (thousand)", 819, a["rise_k"], 1),
 ("A10-02", "Sellers who started selling online in 2023 (thousand)", 513, a["entrants_k"], 1),
 ("A10-03", "Pre-2023 sellers above the 2022 count, net of exits (thousand)", 306, a["pre_2023_above_2022_count_k"], 1),
 ("A10-04", "Newly counted, share of rise, no exits (%)", 37, s["no_exits"]["newly_counted_share_of_rise_pct"], 0.5),
 ("A10-05", "Reference exit rate from 2020-22 cohorts (% a year)", 5.1, a["reference_exit_rate_pct"], 0.05),
 ("A10-06", "Newly counted, share of rise, at the reference exit rate (%)", 56, s["reference"]["newly_counted_share_of_rise_pct"], 0.5),
 ("A10-07", "Newly counted at the reference exit rate (thousand)", 458, s["reference"]["newly_counted_k"], 1),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v10.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
