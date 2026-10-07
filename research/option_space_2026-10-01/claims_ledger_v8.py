"""Claims ledger v8 (8 Oct 2026): linking checks (gel_checks.py, licensed data; national totals committed in tables/gel_checks.json).
Run: python3 claims_ledger_v8.py -> tables/claims_ledger_v8.csv"""
import json
import pandas as pd
T = "tables/"; g = json.load(open(T + "gel_checks.json")); lc = json.load(open(T + "listing_check.json"))
v = g["value_increase_split_pct"]; e = g["existing_sellers_reported_change_2023"]; m = g["bps_marketplace_value_tn"]["growth_2022_2023_pct_by_scenario"]
claims = [
 ("L01", "Main obstacle 2023: lack of demand (% of sellers)", 41.3, g["main_obstacle_2023_pct"]["lack of demand"], 0.05),
 ("L02", "Main obstacle 2023 among existing sellers whose revenue fell: lack of demand (%)", 58.2, g["main_obstacle_2023_existing_sellers_revenue_down_pct"]["lack of demand"], 0.05),
 ("L03", "Off-marketplace sellers wanting to join a marketplace (%)", 13.5, g["non_marketplace_sellers_wanting_to_join_pct"], 0.05),
 ("L04", "BPS marketplace value growth 2022-23, mid scenario (%)", 0.2, m["mid"], 0.05),
 ("L05", "BPS marketplace value growth 2022-23, low scenario (%)", 13.2, m["low"], 0.05),
 ("L06", "Online sellers on marketplaces with Rp300m+ revenue (% of all online sellers)", 5.4, g["share_of_all_online_sellers_marketplace_and_300m_plus_pct"], 0.05),
 ("L07", "BPS 2023 value increase from newly counted sellers, mid (%)", 15.4, v["mid"]["newly_counted"], 0.05),
 ("L08", "BPS 2023 value increase from entrants, mid (%)", 25.5, v["mid"]["entrants"], 0.05),
 ("L09", "BPS 2023 value increase left for existing sellers, mid (%)", 59.1, v["mid"]["rest (existing sellers and other)"], 0.05),
 ("L10", "Existing sellers' reported change in online revenue 2023, mean (%)", -4.3, e["all"]["mean_pct"], 0.05),
 ("L11", "Existing sellers with 20+ workers, mean reported change (%)", 1.4, e["20+ workers"]["mean_pct"], 0.05),
 ("L12", "Existing sellers with 1 worker, mean reported change (%)", -6.3, e["1 worker"]["mean_pct"], 0.05),
 ("L13", "Existing sellers 2022 vs 2021: online revenue up (%)", 36.9, g["existing_sellers_direction_2022_vs_2021_pct"]["up"], 0.05),
 ("L14", "Existing sellers 2022 vs 2021: online revenue down (%)", 24.4, g["existing_sellers_direction_2022_vs_2021_pct"]["down"], 0.05),
 ("L15", "Main obstacle 2022: lack of demand (%)", 35.3, g["main_obstacle_2022_pct"]["lack of demand"], 0.05),
 ("L16", "Main obstacle 2022: lack of capital (%)", 36.8, g["main_obstacle_2022_pct"]["lack of capital"], 0.05),
 ("L17", "Foreign firms: median take-rate swing within 3 years of listing", 0.070, lc["median_within_3_years"], 0.0005),
 ("L18", "Foreign firms: median take-rate swing later", 0.084, lc["median_later"], 0.0005),
 ("L19", "Foreign firms: within-3-years vs later, Wilcoxon p", 0.24, lc["wilcoxon_one_sided_p"], 0.005),
 ("L20", "Indonesian platforms whose largest move came 1 year after listing (of 5)", 4, sum(v["years_after_listing"] == 1 for v in lc["indonesia_largest_move"].values()), 0),
]
L = pd.DataFrame([dict(id=i, claim=x, stated=s, recomputed=round(float(val), 6), status="PASS" if abs(float(val) - s) <= tol else "CHECK") for i, x, s, val, tol in claims])
L.to_csv(T + "claims_ledger_v8.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
