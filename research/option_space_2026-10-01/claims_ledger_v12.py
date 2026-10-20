"""Claims ledger v12 (8 Oct 2026): wedge over time (wedge_over_time.csv) and the market-value test (m1_market_value_results.json; market
values are licensed and not committed, the coefficients are).
Run: python3 claims_ledger_v12.py -> tables/claims_ledger_v12.csv"""
import json
import pandas as pd
T = "tables/"; w = pd.read_csv(T + "wedge_over_time.csv"); m = json.load(open(T + "m1_market_value_results.json"))
iss = w[w.tier == "issuer-reported"]; b = w[(w.firm == "Blibli 3P Retail") & (w.year == 2023)].iloc[0]
d = m["descriptive_idn_regional_change_since_first_year"]
claims = [
 ("W12-01", "Wedge share of transaction value, issuer-reported, minimum (%)", 97.1, iss.wedge_share_of_tv_pct.min(), 0.05),
 ("W12-02", "Wedge share of transaction value, issuer-reported, maximum (%)", 99.5, iss.wedge_share_of_tv_pct.max(), 0.05),
 ("W12-03", "Blibli 2022-23 wedge growth (%)", 32.4, b.g_wedge_pct, 0.05),
 ("W12-04", "Blibli 2022-23 revenue growth (%)", 465.3, b.g_revenue_pct, 0.05),
 ("M12-01", "Main sample firms", 28, m["main"]["firms"], 0),
 ("M12-02", "Main sample firm-years", 138, m["main"]["firm_years"], 0),
 ("M12-03", "b1 volume (main)", 0.60, m["main"]["b1_volume"], 0.005),
 ("M12-04", "b2 take rate (main)", 0.33, m["main"]["b2_take_rate"], 0.005),
 ("M12-05", "M1 one-sided p (main, falsified)", 0.20, m["main"]["p_one_sided_b1_gt_b2"], 0.005),
 ("M12-06", "M2 one-sided p (main, holds)", 0.002, m["main"]["p_one_sided_b1_gt_0"], 0.0005),
 ("M12-07", "M1 one-sided p with segment series", 0.004, m["robust_with_segments"]["p_one_sided_b1_gt_b2"], 0.0005),
 ("M12-08", "GoTo change in log(MV/R), 2022-25", -1.13, d["GoTo"]["change_ln_mv_over_R"], 0.005),
 ("M12-09", "GoTo change in log(MV/V), 2022-25", -0.48, d["GoTo"]["change_ln_mv_over_V"], 0.005),
 ("M12-10", "Blibli change in log(MV/R), 2022-25", -1.88, d["Blibli"]["change_ln_mv_over_R"], 0.005),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v12.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
