"""Claims ledger v13 (22 Oct 2026): the coverage-adjusted H2 scenarios (h2_coverage_adjusted.json) and the exact-inference checks on H1 (h1_exact_inference.json).
Stated values are the ones the thesis prints (Table 5.1, Sections 5.2, 5.7, 7.1, 7.4, Appendix B and the abstract).
Run: python3 claims_ledger_v13.py -> tables/claims_ledger_v13.csv"""
import json
import pandas as pd
T = "tables/"; h = json.load(open(T + "h2_coverage_adjusted.json")); x = json.load(open(T + "h1_exact_inference.json")); ev = json.load(open(T + "event_study_panel_check.json")); m1 = json.load(open(T + "m1_market_value_results.json"))["main"]
s = h["scenarios"]; A = x["A_exact"]; B = x["B_size"]; C = x["C_sea_regional"]; D = x["D_drop_two"]; E = x["E_young_only"]
claims = [
 ("H13-01", "H2 extensive share, published count (%)", 71.1, h["published"]["extensive_share_pct"], 0.05),
 ("H13-02", "Extra sellers removed, no exits (thousand)", 306, s["no_exits"]["extra_sellers_removed_k"], 0.5),
 ("H13-03", "Extra sellers removed, 5% exits (thousand)", 458, s["reference"]["extra_sellers_removed_k"], 0.5),
 ("H13-04", "Count-only share, no exits (%)", 46.6, s["no_exits"]["count_only_extensive_share_pct"], 0.05),
 ("H13-05", "Count-only share, 5% exits (%)", 33.6, s["reference"]["count_only_extensive_share_pct"], 0.05),
 ("H13-06", "Count and value removed, no exits, low (%)", 54.5, s["no_exits"]["count_and_value"]["low"]["extensive_share_pct"], 0.05),
 ("H13-07", "Count and value removed, no exits, high (%)", 53.3, s["no_exits"]["count_and_value"]["high"]["extensive_share_pct"], 0.05),
 ("H13-08", "Count and value removed, 5% exits, low (%)", 43.0, s["reference"]["count_and_value"]["low"]["extensive_share_pct"], 0.05),
 ("H13-09", "Count and value removed, 5% exits, high (%)", 41.5, s["reference"]["count_and_value"]["high"]["extensive_share_pct"], 0.05),
 ("H13-10", "H1 exact Mann-Whitney p, 5 against 27", 0.0038, A["exact_mannwhitney_p"], 0.00005),
 ("H13-11", "H1 exact permutation p over all 201,376 splits", 0.021, A["exact_permutation_p"], 0.0005),
 ("H13-12", "Splits enumerated", 201376, A["splits_enumerated"], 0),
 ("H13-13", "Hodges-Lehmann shift in |change in log take rate| per year", 0.117, B["hodges_lehmann_shift"], 0.0005),
 ("H13-14", "Exact 95% interval for the shift, low", 0.039, B["ci95_low"], 0.0005),
 ("H13-15", "Exact 95% interval for the shift, high", 0.223, B["ci95_high"], 0.0005),
 ("H13-16", "Ratio of group medians", 3.3, B["ratio_of_medians"], 0.05),
 ("H13-17", "Bootstrap interval for the ratio, low", 1.4, B["ratio_bootstrap_ci95"][0], 0.05),
 ("H13-18", "Bootstrap interval for the ratio, high", 8.5, B["ratio_bootstrap_ci95"][1], 0.05),
 ("H13-19", "Sea in the regional group: median, regional group", 0.225, C["median_idn"], 0.0005),
 ("H13-20", "Sea in the regional group: median, foreign group", 0.060, C["median_foreign"], 0.0005),
 ("H13-21", "Sea in the regional group: exact Mann-Whitney p", 0.0004, C["exact_mannwhitney_p"], 0.00005),
 ("H13-22", "Dropping any two of five: best exact p", 0.003, D["best_p"], 0.0005),
 ("H13-23", "Dropping any two of five: worst exact p", 0.058, D["worst_p"], 0.0005),
 ("H13-24", "Dropping any two of five: cases above 0.05 (of 10)", 1, sum(c["exact_mannwhitney_p"] > 0.05 for c in D["cases"]), 0),
 ("H13-25", "Young platforms only: Indonesian and regional platforms", 4, E["firms_idn"], 0),
 ("H13-26", "Young platforms only: foreign platforms", 18, E["firms_foreign"], 0),
 ("H13-27", "Young platforms only: median, regional group", 0.169, E["median_idn"], 0.0005),
 ("H13-28", "Young platforms only: median, foreign group", 0.069, E["median_foreign"], 0.0006),
 ("H13-30", "Announcements in the event-study panel", 191, ev["announcements"], 0),
 ("H13-31", "Event study: volume growth coefficient", 0.014, ev["A_volume_and_take_rate"]["gV"]["coef"], 0.0005),
 ("H13-32", "Event study: volume growth p", 0.24, ev["A_volume_and_take_rate"]["gV"]["p_two_sided"], 0.005),
 ("H13-33", "Event study: take-rate change coefficient", 0.026, ev["A_volume_and_take_rate"]["dm"]["coef"], 0.0005),
 ("H13-34", "Event study: take-rate change p", 0.63, ev["A_volume_and_take_rate"]["dm"]["p_two_sided"], 0.005),
 ("H13-35", "Event study: gap between the two, p", 0.80, ev["A_volume_and_take_rate"]["gV_minus_dm"]["p_two_sided"], 0.005),
 ("H13-36", "Announcements with a revenue surprise", 117, ev["surprise_announcements"], 0),
 ("H13-37", "Revenue surprise coefficient", 0.23, ev["B_surprise"]["S"]["coef"], 0.005),
 ("H13-38", "Revenue surprise p", 0.20, ev["B_surprise"]["S"]["p_two_sided"], 0.005),
 ("H13-39", "Surprise x large take-rate change coefficient", -0.28, ev["C_surprise_x_high_take_rate_change"]["Sx"]["coef"], 0.005),
 ("H13-40", "Surprise x large take-rate change p", 0.42, ev["C_surprise_x_high_take_rate_change"]["Sx"]["p_two_sided"], 0.005),
 ("H13-41", "Registered market-value test: standard error of b1 - b2", 0.31, m1["se_diff"], 0.005),
 ("H13-42", "Smallest gap flagged with 80% power, 5% one-sided (about)", 0.8, 2.4865 * m1["se_diff"], 0.03),
 ("H13-29", "Young platforms only: exact Mann-Whitney p", 0.059, E["exact_mannwhitney_p"], 0.0005),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v13.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
