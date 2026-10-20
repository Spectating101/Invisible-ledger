"""Claims ledger v11 (8 Oct 2026): closing checks (rq_closing_checks.json).
Run: python3 claims_ledger_v11.py -> tables/claims_ledger_v11.csv"""
import json
import pandas as pd
T = "tables/"; c = json.load(open(T + "rq_closing_checks.json")); n = c["noise_vs_2023_surplus"]; s = c["marketplace_channel_share_of_online_value_pct"]
claims = [
 ("C11-01", "Province rows sum to the published 2024 total (businesses)", 4400972, c["province_total_2024"], 2),
 ("C11-02", "Implied national RSE of the business count (%)", 1.37, n["published_rse"]["national_rse_pct"], 0.01),
 ("C11-03", "2023 surplus of pre-2023 sellers, in standard errors", 4.6, n["published_rse"]["surplus_in_se"], 0.05),
 ("C11-04", "Same, with twice the RSE", 2.3, n["twice_rse"]["surplus_in_se"], 0.05),
 ("C11-05", "Revenue as a share of transaction value, 2023, three platforms (%)", 7.3, c["revenue_share_of_transaction_value_2023_pct"], 0.05),
 ("C11-06", "Marketplace channel share of online value, 2022, low scenario (%)", 22.6, s["2022_low"], 0.05),
 ("C11-07", "Marketplace channel share of online value, 2022, mid scenario (%)", 25.6, s["2022_mid"], 0.05),
 ("C11-08", "Marketplace channel share of online value, 2023, published (%)", 18.2, s["2023_published"], 0.05),
 ("C11-09", "Marketplace channel share of online value, 2024, published (%)", 15.8, s["2024_published"], 0.05),
]
L = pd.DataFrame([dict(id=c_, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c_, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v11.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
