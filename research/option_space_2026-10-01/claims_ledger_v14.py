"""Claims ledger v14 (25 Oct 2026): the numbers from Prof. Kong's empirical items (kong_results.json, h1_simple_change.json, regression_panel.csv).
Stated values are the ones the thesis prints (Chapter 5 summary statistics and correlations, the growth test of H1, the OLS tables, Chapter 7, the abstract).
All of it is exploratory: designed after the data were seen.
Run: python3 claims_ledger_v14.py -> tables/claims_ledger_v14.csv"""
import json
import pandas as pd
T = "tables/"
k = json.load(open(T + "kong_results.json")); s = json.load(open(T + "h1_simple_change.json")); P = pd.read_csv(T + "regression_panel.csv")
H = k["h1_growth"]; F = H["foreign"]; I = H["Indonesian and regional"]; O = k["ols"]; C = k["checks"]
claims = [
 ("K14-01", "Platform-years in the regression panel", 213, len(P), 0),
 ("K14-02", "Platforms in the panel", 32, P.key.nunique(), 0),
 ("K14-03", "Indonesian and regional platform-years", 20, int((P.grp == "IDN").sum()), 0),
 ("K14-04", "Growth pairs abroad (winsorised 5/95)", 166, F["n"], 0),
 ("K14-05", "Growth pairs, Indonesia and region", 15, I["n"], 0),
 ("K14-06", "H1 growth regression, foreign slope on g(V)", 0.99, F["coef"]["g_V_w"]["b"], 0.005),
 ("K14-07", "H1 growth regression, foreign slope, standard error", 0.07, F["coef"]["g_V_w"]["se"], 0.005),
 ("K14-08", "H1 growth regression, foreign slope equal to 1, p", 0.84, F["slope_eq_1_p"], 0.005),
 ("K14-09", "H1 growth regression, Indonesia and region slope", 0.40, I["coef"]["g_V_w"]["b"], 0.005),
 ("K14-10", "H1 growth regression, Indonesia and region slope, standard error", 0.16, I["coef"]["g_V_w"]["se"], 0.005),
 ("K14-11", "H1 growth regression, Indonesia and region slope equal to 1, p", 0.02, I["slope_eq_1_p"], 0.005),
 ("K14-12", "H1 growth regression, Indonesia and region constant", 0.44, I["coef"]["const"]["b"], 0.005),
 ("K14-13", "H1 growth regression, foreign constant", 0.06, F["coef"]["const"]["b"], 0.005),
 ("K14-14", "Correlation of g(R) and g(V), foreign", 0.90, F["pearson_w"], 0.005),
 ("K14-15", "Correlation of g(R) and g(V), Indonesia and region", 0.31, I["pearson_w"], 0.005),
 ("K14-16", "Correlation of g(R) and g(V), all platforms", 0.84, k["corr"]["g_R_w~g_V_w"]["r"], 0.005),
 ("K14-17", "Equal correlations in the two groups, Fisher p below 0.001", 1, int(H["fisher_z_equal_corr_p"] < 0.001), 0),
 ("K14-18", "Correlation of g(R) and g(V) without winsorising, foreign", 0.54, F["pearson_raw"], 0.005),
 ("K14-19", "OLS (1) ln(wedge): IndonesiaRegion", -0.07, O[0]["coef"]["idn"]["b"], 0.005),
 ("K14-20", "OLS (2) ln(wedge): IndonesiaRegion", -0.30, O[1]["coef"]["idn"]["b"], 0.005),
 ("K14-21", "OLS (3) ln(wedge): IndonesiaRegion", 0.08, O[2]["coef"]["idn"]["b"], 0.005),
 ("K14-22", "OLS (1) ln(wedge): ln(Assets)", 0.90, O[0]["coef"]["ln_assets_usd"]["b"], 0.005),
 ("K14-23", "OLS (3) ln(wedge): ln(Assets)", 0.90, O[2]["coef"]["ln_assets_usd"]["b"], 0.005),
 ("K14-24", "OLS (1) ln(wedge): R-squared", 0.81, O[0]["r2"], 0.005),
 ("K14-25", "OLS (3) ln(wedge): R-squared", 0.87, O[2]["r2"], 0.005),
 ("K14-26", "OLS (4) ecosystem ratio: IndonesiaRegion", 15.2, O[3]["coef"]["idn"]["b"], 0.05),
 ("K14-27", "OLS (5) ecosystem ratio: IndonesiaRegion", 12.9, O[4]["coef"]["idn"]["b"], 0.05),
 ("K14-28", "OLS (6) ecosystem ratio: IndonesiaRegion", 17.1, O[5]["coef"]["idn"]["b"], 0.05),
 ("K14-29", "OLS (4) ecosystem ratio: IndonesiaRegion, wild-bootstrap p", 0.031, O[3]["coef"]["idn"]["p_wild"], 0.012),
 ("K14-30", "OLS (5) ecosystem ratio: IndonesiaRegion, wild-bootstrap p", 0.039, O[4]["coef"]["idn"]["p_wild"], 0.012),
 ("K14-31", "OLS (6) ecosystem ratio: IndonesiaRegion, wild-bootstrap p", 0.005, O[5]["coef"]["idn"]["p_wild"], 0.004),
 ("K14-32", "OLS (6) ecosystem ratio: OnDemand", -19.8, O[5]["coef"]["type_on_demand"]["b"], 0.05),
 ("K14-33", "OLS (6) ecosystem ratio: GDPGrowth", 1.5, O[5]["coef"]["gdp_growth"]["b"], 0.05),
 ("K14-34", "OLS (4) ecosystem ratio: R-squared", 0.44, O[3]["r2"], 0.005),
 ("K14-35", "OLS (6) ecosystem ratio: R-squared", 0.57, O[5]["r2"], 0.005),
 ("K14-36", "Observations in OLS (1)", 202, O[0]["n"], 0),
 ("K14-37", "Observations in OLS (2) and (3)", 178, O[1]["n"], 0),
 ("K14-38", "Leave one Indonesian platform out: smallest ecosystem-ratio coefficient", 15.3, min(v["E_w"] for v in C["leave_one_indonesian_platform_out"].values()), 0.05),
 ("K14-39", "Leave one Indonesian platform out: largest ecosystem-ratio coefficient", 18.3, max(v["E_w"] for v in C["leave_one_indonesian_platform_out"].values()), 0.05),
 ("K14-40", "Ecosystem ratio without winsorising: IndonesiaRegion", 28.5, C["E_unwinsorised"]["ecosystem_ratio"]["b"], 0.06),
 ("K14-41", "ln(ecosystem ratio): IndonesiaRegion", 1.68, C["ln_E_instead_of_E_w"]["ln_E"]["b"], 0.005),
 ("K14-42", "Take-rate move, simple percentage change: Indonesia and region median", 0.224, s["simple_percentage_change"]["median_idn"], 0.0005),
 ("K14-43", "Take-rate move, simple percentage change: foreign median", 0.062, s["simple_percentage_change"]["median_foreign"], 0.0005),
 ("K14-44", "Take-rate move, simple percentage change: ratio of medians", 3.6, s["simple_percentage_change"]["ratio"], 0.05),
 ("K14-45", "Take-rate move, simple percentage change: Mann-Whitney p", 0.003, s["simple_percentage_change"]["mannwhitney_p"], 0.0005),
 ("K14-46", "Take-rate move, log change reproduces the chapter: ratio of medians", 3.3, s["log_change (as in the chapter)"]["ratio"], 0.05),
 ("K14-47", "Take-rate move, log change reproduces the chapter: Mann-Whitney p", 0.004, s["log_change (as in the chapter)"]["mannwhitney_p"], 0.0005),
 ("K14-48", "Share of Indonesian and regional pairs with a rising take rate", 0.87, s["share_take_rate_rose"]["idn"], 0.005),
 ("K14-49", "Share of foreign pairs with a rising take rate", 0.65, s["share_take_rate_rose"]["foreign"], 0.005),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(v), 6), status="PASS" if abs(float(v) - st) <= tol else "CHECK") for c, t, st, v, tol in claims])
L.to_csv(T + "claims_ledger_v14.csv", index=False); print(L[L.status != "PASS"].to_string(index=False)); print(L.status.value_counts().to_dict())
