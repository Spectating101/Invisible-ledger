"""M1-M2 (PREREGISTRATION.md addendum of 8 Oct 2026, written before the market values below were pulled): do markets value revenue growth
from more transactions and revenue growth from a higher take rate alike?
dlnMV = year fixed effects + b1 x dlnV + b2 x dlnm, OLS, standard errors clustered by firm. M1: b1 > b2 (one-sided 5%). M2: b1 > 0.
Market values: LSEG company market capitalisation at calendar year-end, in each firm's reporting currency (licensed, NOT committed;
pass the file path). Only December dates are used (a firm delisted mid-year has no year-end value that year).
Transaction value and revenue (committed, verified): tables/peers_quarterly.csv (US peers, full four-quarter years), the global matched annual file
(Shopify, Zalando, Jumia; Sea, Rakuten and Mercado Libre for robustness), tables/spinoff_panel.csv (rows flagged keep), tables/take_rate_levels.csv
(Bukalapak group; Blibli 3P for robustness), tables/l_panel.csv (GoTo and Grab on-demand, robustness).
Run: python3 m1_market_value.py <mcap_reporting_ccy.csv> -> tables/m1_market_value_results.json (coefficients and counts only)"""
import json, sys
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

HERE = "tables/"
mv = pd.read_csv(sys.argv[1]); mv["date"] = pd.to_datetime(mv.date)
mv = mv[mv.date.dt.month == 12].assign(year=lambda d: d.date.dt.year)[["firm", "year", "mcap"]]

parts = []
q = pd.read_csv(HERE + "peers_quarterly.csv"); q = q[q.status != "FAIL"]; q["year"] = q.quarter.str[:4].astype(int)
a = q.groupby(["firm", "year"]).agg(V=("V", "sum"), R=("R", "sum"), n=("quarter", "count")).reset_index()
parts.append(a[a.n == 4].drop(columns="n").assign(group="main"))
g = pd.read_csv("../../data/global_ecommerce/global_platform_matched_annual.csv").rename(columns={"issuer": "firm", "transaction_value": "V", "revenue_value": "R"})
for f, grp in (("Shopify", "main"), ("Zalando", "main"), ("Jumia", "main"), ("Sea / Shopee", "robust"), ("Rakuten", "robust"), ("Mercado Libre", "robust")):
    parts.append(g[g.firm == f][["firm", "year", "V", "R"]].assign(group=grp))
s = pd.read_csv(HERE + "spinoff_panel.csv"); s = s[s.flag_1p == "keep"]
parts.append(s.rename(columns={"entity": "firm", "revenue": "R"})[["firm", "year", "V", "R"]].assign(group="main"))
t = pd.read_csv(HERE + "take_rate_levels.csv").rename(columns={"transaction_value": "V", "revenue_value": "R"})
parts.append(t[t.firm == "Bukalapak Group"][["firm", "year", "V", "R"]].assign(group="main"))
parts.append(t[t.firm == "Blibli 3P Retail"][["firm", "year", "V", "R"]].assign(firm="Blibli", group="robust"))
lp = pd.read_csv(HERE + "l_panel.csv")
parts.append(lp[(lp.firm == "GoTo") & (lp.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo", group="robust"))
parts.append(lp[lp.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab", group="robust"))
P = pd.concat(parts, ignore_index=True).dropna(subset=["V", "R"])
P = P[(P.V > 0) & (P.R > 0)].drop_duplicates(["firm", "year"]).merge(mv, on=["firm", "year"], how="inner")
P = P.sort_values(["firm", "year"])
for c in ("V", "R", "mcap"):
    P[f"ln{c}"] = np.log(P[c])
prev = P.groupby("firm").shift()
ok = (P.year - prev.year == 1)
D = pd.DataFrame({"firm": P.firm, "year": P.year, "group": P.group, "dlnMV": P.lnmcap - prev.lnmcap, "dlnV": P.lnV - prev.lnV,
                  "dlnm": (P.lnR - prev.lnR) - (P.lnV - prev.lnV)})[ok].dropna()

def run(d, label):
    m = smf.ols("dlnMV ~ dlnV + dlnm + C(year)", data=d).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d.firm)[0]})
    tt = m.t_test("dlnV - dlnm = 0"); diff = float(np.squeeze(tt.effect)); se = float(np.squeeze(tt.sd)); tv = diff / se
    G = d.firm.nunique(); p1 = float(1 - stats.t.cdf(tv, G - 1))
    b1, b2 = float(m.params["dlnV"]), float(m.params["dlnm"])
    p_b1 = float(1 - stats.t.cdf(b1 / float(m.bse["dlnV"]), G - 1))
    return {"label": label, "firms": int(G), "firm_years": int(len(d)), "b1_volume": b1, "se_b1": float(m.bse["dlnV"]),
            "b2_take_rate": b2, "se_b2": float(m.bse["dlnm"]), "b1_minus_b2": diff, "se_diff": se,
            "p_one_sided_b1_gt_b2": p1, "p_one_sided_b1_gt_0": p_b1, "r2": float(m.rsquared),
            "M1_holds": bool(p1 < 0.05 and diff > 0), "M2_holds": bool(p_b1 < 0.05 and b1 > 0)}

def wins(d):
    d = d.copy()
    for c in ("dlnMV", "dlnV", "dlnm"):
        lo, hi = d[c].quantile([0.05, 0.95]); d[c] = d[c].clip(lo, hi)
    return d

main = D[D.group == "main"]
res = {"main": run(main, "main sample (whole-company figures)"),
       "robust_winsorised_5_95": run(wins(main), "main sample, winsorised 5/95"),
       "robust_with_segments": run(D, "main plus segment series and Mercado Libre"),
       "firms_main": sorted(main.firm.unique().tolist()), "firms_robust_added": sorted(set(D.firm) - set(main.firm))}
# descriptive: Indonesian and regional listed platforms, log(MV/R) and log(MV/V) by year (segment figures where that is all there is)
desc = P[P.firm.isin(["GoTo", "Grab", "Bukalapak Group", "Sea / Shopee", "Blibli"])].assign(ln_mv_over_R=lambda d: d.lnmcap - d.lnR, ln_mv_over_V=lambda d: d.lnmcap - d.lnV)
res["descriptive_idn_regional_change_since_first_year"] = {
    f: {"years": [int(desc[desc.firm == f].year.min()), int(desc[desc.firm == f].year.max())],
        "change_ln_mv_over_R": float(desc[desc.firm == f].ln_mv_over_R.iloc[-1] - desc[desc.firm == f].ln_mv_over_R.iloc[0]),
        "change_ln_mv_over_V": float(desc[desc.firm == f].ln_mv_over_V.iloc[-1] - desc[desc.firm == f].ln_mv_over_V.iloc[0])}
    for f in desc.firm.unique() if (desc.firm == f).sum() >= 2}
s_ = json.dumps(res, indent=1); print(s_); open(HERE + "m1_market_value_results.json", "w").write(s_)
