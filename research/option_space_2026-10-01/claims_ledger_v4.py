"""Claims ledger v4 (4 Oct 2026): numbers stated in chat on 3-4 Oct after ledger v3, recomputed from committed outputs.
World Bank and BPS-free results come from committed aggregate outputs (the licensed microdata is not committed; see wb_tests.py, wb_crosscountry.py).
Run from this folder: python3 claims_ledger_v4.py -> tables/claims_ledger_v4.csv"""
import json
import pandas as pd
T = "tables/"
h = json.load(open(T + "h1_extended_results.json")); w = json.load(open(T + "wb_tests_results.json")); s = json.load(open(T + "spinoff_results.json"))
x = pd.read_csv(T + "wb_crosscountry.csv").set_index("country"); g = pd.read_csv(T + "consistency_grid_growth.csv", index_col=0)
B = h["B_exploratory_market_income"]
claims = [
 ("H01", "Indonesia+regional median yearly swing in the cut (x100)", 20.1, 100 * h["A_vs_all_foreign"]["median_a"], 0.1),
 ("H02", "All foreign firms median (x100)", 6.2, 100 * h["A_vs_all_foreign"]["median_b"], 0.1),
 ("H03", "Foreign firms counted", 27, h["A_vs_all_foreign"]["firms_b"], 0),
 ("H04", "Firm-level Mann-Whitney p vs all foreign", 0.004, h["A_vs_all_foreign"]["mannwhitney_p"], 0.0005),
 ("H05", "p vs the 19 new firms alone", 0.005, h["A_vs_new"]["mannwhitney_p"], 0.0005),
 ("H06", "D measure: Indonesia median |D| (pp)", 27.0, h["robust_D_measure"]["median_abs_D_indonesia_pp"], 0.1),
 ("H07", "D measure: foreign median |D| (pp)", 6.5, h["robust_D_measure"]["median_abs_D_foreign_pp"], 0.1),
 ("H08", "Leave-one-out: worst Mann-Whitney p", 0.016, max(v["mannwhitney_p"] for v in h["robust_leave_one_out"].values()), 0.001),
 ("M01", "Young emerging-market platforms, median swing (x100)", 16.2, 100 * B["young (<=5y listed)"]["median_emerging"], 0.1),
 ("M02", "Young high-income platforms, median swing (x100)", 4.6, 100 * B["young (<=5y listed)"]["median_high"], 0.1),
 ("M03", "Young emerging ex-Indonesia, median swing (x100)", 14.4, 100 * B["young (<=5y listed) ex-Indonesia"]["median_emerging"], 0.1),
 ("G01", "BI e-commerce 2023 growth (%)", -4.7, g.loc["Bank Indonesia e-commerce", "2023"], 0.05),
 ("G02", "SEA express parcel market 2024 growth (%)", 25.2, g.loc["SEA express parcel market", "2024"], 0.05),
 ("G03", "J&T SEA parcels 2024 growth (%)", 40.8, g.loc["J&T Express SEA parcels", "2024"], 0.05),
 ("W01", "Informal: records, social-media users (%)", 29.9, w["W1_records_social_media"], 0.05),
 ("W02", "Informal: records, others (%)", 12.3, w["W1_records_no_social_media"], 0.05),
 ("W03", "Informal: digital receipt, social-media users (%)", 11.5, w["W2_digital_receipt_social_media"], 0.05),
 ("W04", "Informal: median annual sales, social-media users (Rp m)", 60, w["W3_median_annual_sales_Rp_social_media"] / 1e6, 0.5),
 ("W05", "Informal: share using social media with customers (%)", 27.3, w["share_social_media_weighted"], 0.1),
 ("F01", "Formal: e-pay share of sales, with website (%)", 44.0, w["F1_epay_sales_share_website"], 0.05),
 ("F02", "Formal: e-filing with website (%)", 51.3, w["F2_efile_any_website"], 0.05),
 ("F03", "Formal: neither website nor e-filing, Indonesia (%)", 39.9, w["F3_no_website_no_efile_share"], 0.05),
 ("X01", "Cambodia neither share (%)", 34.8, x.loc["Cambodia", "neither_share"], 0.05),
 ("X02", "Malaysia neither share (%)", 9.1, x.loc["Malaysia", "neither_share"], 0.05),
 ("X03", "Thailand neither share (%)", 8.7, x.loc["Thailand", "neither_share"], 0.05),
 ("X04", "Philippines neither share (%)", 16.0, x.loc["Philippines", "neither_share"], 0.05),
 ("X05", "Countries whose e-filing matches the published figure", 7, int(x.data_check_pass.sum()), 0),
 ("S01", "Spin-off S1 b1-b2 (falsified)", -0.035, s["S1"]["diff"], 0.001),
 ("S02", "Spin-off S2 Spearman (falsified)", -0.016, s["S2_main_2021_2023"]["spearman"], 0.001),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v4.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
