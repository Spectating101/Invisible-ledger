"""Claims ledger v9 (8 Oct 2026): Part 6 numbers (part6_checks.json, from committed tables).
Run: python3 claims_ledger_v9.py -> tables/claims_ledger_v9.csv"""
import json
import pandas as pd
T = "tables/"; p = json.load(open(T + "part6_checks.json"))
claims = [
 ("T6-01", "Marketplace tax: value reach 2022, low scenario (%)", 17.5, p["tax_value_reach_pct_2022"]["low"], 0.05),
 ("T6-02", "Marketplace tax: value reach 2022, mid scenario (%)", 23.6, p["tax_value_reach_pct_2022"]["mid"], 0.05),
 ("T6-03", "Marketplace tax: seller reach, marketplace and Rp300m+ (%)", 5.4, p["tax_seller_reach_pct"], 0.05),
 ("T6-04", "Marketplace sellers, share of online sellers 2023 (%)", 17.8, p["marketplace_sellers_share_pct"]["2023"], 0.05),
 ("T6-05", "Off-marketplace sellers wanting to join (%)", 13.5, p["off_marketplace_wanting_to_join_pct"], 0.05),
 ("T6-06", "Tax base, smallest ruler (Rp tn)", 203.6, p["tax_base_range_Rp_tn"][0], 0.05),
 ("T6-07", "Tax base, largest ruler (Rp tn)", 983.0, p["tax_base_range_Rp_tn"][1], 0.05),
 ("T6-08", "Grab rides share of on-demand GMV, last 4 quarters (%)", 35.6, p["grab_rides_share_of_ondemand_gmv_pct_last4q"], 0.1),
 ("T6-09", "Grab incentives, % of on-demand GMV, last 4 quarters", 10.4, p["grab_incentives_pct_of_ondemand_gmv_last4q"], 0.1),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v9.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
