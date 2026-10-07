"""Claims ledger v5 (7 Oct 2026): BPS microdata results, quarterly H1, and the wedge split, recomputed from committed outputs.
The BPS microdata is licensed and not committed; its aggregates (bps_microdata_results.json, bps_descriptives.json) are.
Run from this folder: python3 claims_ledger_v5.py -> tables/claims_ledger_v5.csv"""
import json
import pandas as pd
T = "tables/"
b = json.load(open(T + "bps_microdata_results.json")); d = json.load(open(T + "bps_descriptives.json"))
q = json.load(open(T + "h1_quarterly_results.json")); w = json.load(open(T + "wedge_split_summary.json"))
r23, r24, r21 = b["file2023"], b["file2024"], b["file2021"]
claims = [
 ("B01", "Entrants: share of 2023 sellers who began online in 2023 (%)", 13.45, r24["E5_entrants_2023"], 0.01),
 ("B02", "Most count growth entry can explain, no exits (%)", 15.5, d["max_count_growth_from_entry_pct"], 0.05),
 ("B03", "Existing sellers, online revenue median change (%)", 0.0, r24["E6_incumbent_median_change"], 0),
 ("B04", "Existing sellers with online revenue up (%)", 24.5, d["incumbents_2023_revenue_direction"]["up"], 0.05),
 ("B05", "Existing sellers with online revenue down (%)", 31.9, d["incumbents_2023_revenue_direction"]["down"], 0.05),
 ("B06", "Share with financial statements, 2020 (%)", 23.5, d["books_share"]["2020"], 0.05),
 ("B07", "Share with financial statements, 2022 (%)", 20.7, d["books_share"]["2022"], 0.05),
 ("B08", "Share with financial statements, 2023 (%)", 15.2, d["books_share"]["2023"], 0.05),
 ("B09", "Marketplace use, 2020 (%)", 21.6, d["marketplace_share"]["2020"], 0.05),
 ("B10", "Marketplace use, 2022 (%)", 19.75, r23["E2b_marketplace_users_2022"], 0.01),
 ("B11", "Marketplace use, 2023 (%)", 17.8, d["marketplace_share"]["2023"], 0.05),
 ("B12", "Online value without financial statements, 2022, low scenario (%)", 40.4, r23["E1_low"], 0.05),
 ("B13", "Online value without financial statements, 2022, mid scenario (%)", 30.2, r23["E1_mid"], 0.05),
 ("B14", "Marketplace value from sellers >= Rp300m, mid (%)", 92.2, r23["E8_mid"], 0.05),
 ("B15", "Marketplace value from sellers >= Rp300m, low (%)", 77.4, r23["E8_low"], 0.05),
 ("B16", "Marketplace sellers >= Rp300m, count share (%)", 27.6, r23["E8_count_share_marketplace_sellers_above_300m"], 0.05),
 ("B17", "Marketplace-to-consumer slice / BI 2022, mid", 0.68, r23["recon_mid"]["marketplace_b2c_over_BI"], 0.005),
 ("B18", "Marketplace-to-consumer slice / BI 2022, low", 0.16, r23["recon_low"]["marketplace_b2c_over_BI"], 0.005),
 ("B19", "Mid scenario total / BPS Rp783tn", 1.95, r23["bracket_period"]["mid_total_over_783tn"]["annual"], 0.005),
 ("B20", "Gojek users among BPS marketplace sellers, 2023 (%)", 44.7, d["apps_among_marketplace_users_2023"]["Gojek"], 0.05),
 ("B21", "Shopee users among BPS marketplace sellers, 2023 (%)", 42.2, d["apps_among_marketplace_users_2023"]["Shopee"], 0.05),
 ("B22", "Tokopedia users among BPS marketplace sellers, 2023 (%)", 12.6, d["apps_among_marketplace_users_2023"]["Tokopedia"], 0.05),
 ("B23", "2020 E1, online-revenue bracket version (%)", 36.1, r21["E7_E1_2020_online_bracket"], 0.05),
 ("Q01", "Quarterly H1: Indonesia and region median (x100)", 7.1, 100 * q["median_indonesia_region"], 0.05),
 ("Q02", "Quarterly H1: benchmark median (x100)", 4.9, 100 * q["median_benchmark"], 0.05),
 ("Q03", "Quarterly H1: Mann-Whitney p (falsified)", 0.19, q["mannwhitney_p"], 0.005),
 ("V01", "Wedge changes from the cut, Indonesia median (%)", 4.3, 100 * w["IDN_main"]["median_monetization_share_of_W_change"], 0.05),
 ("V02", "Revenue changes from the cut, Indonesia median (%)", 66.5, 100 * w["IDN_main"]["median_monetization_share_of_R_change"], 0.05),
 ("V03", "Revenue changes from the cut, benchmark median (%)", 26.7, 100 * w["EXT_clean"]["median_monetization_share_of_R_change"], 0.05),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v5.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
