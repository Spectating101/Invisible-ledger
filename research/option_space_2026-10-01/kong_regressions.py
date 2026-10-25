"""Prof. Kong's empirical items (24 Oct 2026): summary statistics, pairwise correlations and OLS, all EXPLORATORY (designed after the data were seen).

Input: tables/regression_panel.csv (build_regression_panel.py). Nothing here needs the network or a licensed file.
What is run, and why (the reasoning behind each of her instructions is in papers/thesis_2026-10/KONG_COMMENTS_TRACE.md):
  A. Summary statistics (N, mean, median, standard deviation) for the Indonesian and regional platforms and for the foreign platforms.
  B. Pairwise correlations of the main variables, with stars at 1, 5 and 10 percent.
  C. H1 in growth: revenue growth on transaction value growth, with the simple percentage change g(Y) = (Y_t - Y_t-1) / Y_t-1. If revenue grows in
     proportion to transaction value, the slope is 1 and the group does not matter. Run for all platforms (with a group interaction), abroad
     and in Indonesia and the region; the test of slope = 1 is reported.
  D. OLS of ln(wedge in US$) and of the ecosystem ratio on platform features (Indonesia/region dummy, years since listing, size by total assets,
     platform type), home-market macro variables (GDP growth, inflation, household-consumption growth, policy rate) and year effects. The take rate and
     its components are NOT regressors (E = 1/m - 1 links them mechanically). Standard errors are clustered by platform, with the small-sample
     correction and t(G-1) critical values; with 32 clusters, a wild cluster bootstrap p-value (Rademacher weights, null imposed) is added for the
     Indonesia/region coefficient.
Growth rates and the ecosystem ratio are winsorised at the 5th and 95th percentiles of the pooled sample, the rule used for the market-value test
(m1_market_value.py). Unwinsorised, rank and log versions are reported as checks.
Run from this folder: python3 kong_regressions.py -> tables/kong_*.csv, tables/kong_results.json, tables/kong_table_*.md"""
import json
import numpy as np, pandas as pd
from scipy import stats

rng = np.random.default_rng(20261025)
L = pd.read_csv("tables/regression_panel.csv")

def wins(s, lo=0.05, hi=0.95):
    a, b = s.quantile([lo, hi]); return s.clip(a, b)

L["g_V_w"], L["g_R_w"], L["E_w"] = wins(L.g_V), wins(L.g_R), wins(L.ecosystem_ratio)
L["ln_E"] = np.log(L.ecosystem_ratio)
L["wedge_usd_bn"] = L.wedge_usd / 1000
for t in ("on-demand", "travel", "freelance", "resale"): L["type_" + t.replace("-", "_")] = (L.type == t).astype(int)
L["idn"] = L.indonesia_region
res = {"n_platform_years": int(len(L)), "n_platforms": int(L.key.nunique()), "n_idn_platforms": int(L[L.idn == 1].key.nunique())}

# ---------------------------------------------------------------- A. summary statistics
VARS = [("wedge_usd", "Wedge, US$ million"), ("E_w", "Ecosystem ratio"), ("g_R_w", "Revenue growth, g(R)"), ("g_V_w", "Transaction value growth, g(V)"),
        ("assets_usd", "Total assets, US$ million"), ("years_listed", "Years since listing"), ("gdp_growth", "GDP growth, percent"),
        ("inflation", "Inflation, percent"), ("household_growth", "Household spending growth, percent"), ("policy_rate", "Policy rate, percent")]
rows = []
for c, lab in VARS:
    r = {"variable": lab}
    for g, name in ((1, "Indonesian and regional"), (0, "Foreign")):
        x = L.loc[L.idn == g, c].dropna()
        r.update({f"{name}|N": len(x), f"{name}|Mean": x.mean(), f"{name}|P50": x.median(), f"{name}|SD": x.std()})
    rows.append(r)
S = pd.DataFrame(rows); S.to_csv("tables/kong_summary_stats.csv", index=False)

# ---------------------------------------------------------------- B. correlations
CV = [("ln_wedge_usd", "ln(Wedge)"), ("E_w", "Ecosystem ratio"), ("g_R_w", "g(R)"), ("g_V_w", "g(V)"), ("ln_assets_usd", "ln(Assets)"),
      ("ln1_years_listed", "ln(1+YearsListed)"), ("idn", "IndonesiaRegion"), ("gdp_growth", "GDPGrowth"), ("policy_rate", "PolicyRate")]
# inflation and household-spending growth are left out of the printed matrix to keep it within the page: they correlate 0.80 with the policy rate and 0.92 with GDP growth (all pairs are in kong_correlations_all.csv)
k = len(CV); C = np.full((k, k), np.nan); P = np.full((k, k), np.nan); NN = np.zeros((k, k), int)
for i in range(k):
    for j in range(i + 1):
        d = L[[CV[i][0], CV[j][0]]].dropna(); NN[i, j] = len(d)
        if i == j: C[i, j] = 1.0; continue
        r, p = stats.pearsonr(d.iloc[:, 0], d.iloc[:, 1]); C[i, j], P[i, j] = r, p
_all = L[["ln_wedge_usd", "E_w", "g_R_w", "g_V_w", "ln_assets_usd", "ln1_years_listed", "idn", "gdp_growth", "inflation", "household_growth", "policy_rate"]]
_all.corr().round(3).to_csv("tables/kong_correlations_all.csv")
pd.DataFrame(C, index=[c[1] for c in CV], columns=range(1, k + 1)).to_csv("tables/kong_correlations.csv")
pd.DataFrame(P, index=[c[1] for c in CV], columns=range(1, k + 1)).to_csv("tables/kong_correlations_p.csv")
res["corr"] = {"g_R_w~g_V_w": {"r": float(C[3, 2]), "p": float(P[3, 2]), "n": int(NN[3, 2])},
               "ln_wedge~E_w": {"r": float(C[1, 0]), "p": float(P[1, 0])}}

# ---------------------------------------------------------------- cluster-robust OLS (CR1, t with G-1 df), own implementation
def ols(y, X, g):
    """y (n,), X (n,k) with constant, g cluster labels -> beta, se, t, p, resid, df, r2"""
    n, kk = X.shape; XtXi = np.linalg.pinv(X.T @ X); b = XtXi @ X.T @ y; e = y - X @ b
    labs, inv = np.unique(g, return_inverse=True); G = len(labs)
    meat = np.zeros((kk, kk))
    for gi in range(G):
        s = X[inv == gi].T @ e[inv == gi]; meat += np.outer(s, s)
    c = G / (G - 1) * (n - 1) / (n - kk); V = c * XtXi @ meat @ XtXi
    se = np.sqrt(np.diag(V)); t = b / se; p = 2 * stats.t.sf(np.abs(t), G - 1)
    r2 = 1 - (e @ e) / ((y - y.mean()) @ (y - y.mean()))
    return b, se, t, p, e, G, r2

def design(d, cols, year_fe):
    X = d[cols].astype(float).copy()
    if year_fe:
        yd = pd.get_dummies(d.year, prefix="yr", drop_first=True).astype(float); X = pd.concat([X, yd], axis=1)
    X.insert(0, "const", 1.0); return X

def wild_p(d, ycol, cols, year_fe, target, B=2999):
    """wild cluster bootstrap p-value for coefficient `target` (null imposed)."""
    X = design(d, cols, year_fe); y = d[ycol].values; g = d.key.values; j = list(X.columns).index(target)
    b, se, t, p, e, G, r2 = ols(y, X.values, g); t_obs = t[j]
    Xr = X.drop(columns=target).values; br = np.linalg.pinv(Xr.T @ Xr) @ Xr.T @ y; er = y - Xr @ br; fr = Xr @ br
    labs, inv = np.unique(g, return_inverse=True); cnt = 0
    for _ in range(B):
        w = rng.choice([-1.0, 1.0], size=len(labs))[inv]
        ys = fr + w * er; bb, ss, tt, pp, *_ = ols(ys, X.values, g); cnt += abs(tt[j]) >= abs(t_obs)
    return (cnt + 1) / (B + 1)

TYPES = ["type_on_demand", "type_travel", "type_freelance", "type_resale"]
FEAT = ["idn", "ln1_years_listed", "ln_assets_usd"] + TYPES
MACRO = ["gdp_growth", "inflation", "household_growth", "policy_rate"]
NAMES = {"idn": "IndonesiaRegion", "ln1_years_listed": "ln(1+YearsListed)", "ln_assets_usd": "ln(Assets)", "type_on_demand": "OnDemand", "type_travel": "Travel",
         "type_freelance": "Freelance", "type_resale": "Resale", "gdp_growth": "GDPGrowth", "inflation": "Inflation", "household_growth": "HouseholdGrowth",
         "policy_rate": "PolicyRate", "const": "Constant", "emerging_market": "EmergingMarket"}
SPECS = [  # (label, dependent, regressors, year fixed effects)
    ("ln_wedge_usd", FEAT, False), ("ln_wedge_usd", FEAT + MACRO, False), ("ln_wedge_usd", FEAT + MACRO, True),
    ("E_w", FEAT, False), ("E_w", FEAT + MACRO, False), ("E_w", FEAT + MACRO, True)]

def run(specs, data=L, bootstrap=True):
    out = []
    for dep, cols, fe in specs:
        d = data.dropna(subset=[dep] + cols).copy()
        X = design(d, cols, fe); b, se, t, p, e, G, r2 = ols(d[dep].values, X.values, d.key.values)
        o = {"dep": dep, "n": int(len(d)), "clusters": int(G), "r2": float(r2), "year_fe": fe, "coef": {}}
        for nm, bb, ss, pp in zip(X.columns, b, se, p):
            if not nm.startswith("yr_"): o["coef"][nm] = {"b": float(bb), "se": float(ss), "p": float(pp)}
        if bootstrap and "idn" in cols: o["coef"]["idn"]["p_wild"] = float(wild_p(d, dep, cols, fe, "idn"))
        out.append(o)
    return out

main = run(SPECS)
res["ols"] = main

# self-check against statsmodels' cluster-robust estimator (CR1) for column (2)
try:
    import statsmodels.api as sm
    d = L.dropna(subset=["ln_wedge_usd"] + FEAT + MACRO); X = design(d, FEAT + MACRO, False)
    m = sm.OLS(d.ln_wedge_usd.values, X.values).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d.key)[0], "use_correction": True}, use_t=True)
    res["selfcheck_se_max_abs_diff_vs_statsmodels"] = float(np.max(np.abs(m.bse - np.array([main[1]["coef"][c]["se"] for c in X.columns]))))
except Exception as ex: res["selfcheck_se_max_abs_diff_vs_statsmodels"] = str(ex)

# ---------------------------------------------------------------- C. H1 in growth
g = L.dropna(subset=["g_R_w", "g_V_w"]).copy(); g["gv_idn"] = g.g_V_w * g.idn
H = {}
for lab, d, cols in (("all, with group interaction", g, ["g_V_w", "idn", "gv_idn"]), ("foreign", g[g.idn == 0], ["g_V_w"]), ("Indonesian and regional", g[g.idn == 1], ["g_V_w"])):
    X = design(d, cols, False); b, se, t, p, e, G, r2 = ols(d.g_R_w.values, X.values, d.key.values)
    o = {"n": int(len(d)), "clusters": int(G), "r2": float(r2), "coef": {n: {"b": float(bb), "se": float(s), "p": float(pp)} for n, bb, s, pp in zip(X.columns, b, se, p)}}
    j = list(X.columns).index("g_V_w"); o["slope_eq_1_p"] = float(2 * stats.t.sf(abs((b[j] - 1) / se[j]), G - 1))
    r, pr = stats.pearsonr(d.g_V_w, d.g_R_w); rs, ps = stats.spearmanr(d.g_V, d.g_R, nan_policy="omit")
    o.update({"pearson_w": float(r), "pearson_w_p": float(pr), "spearman": float(rs), "spearman_p": float(ps)})
    rr, pp_ = stats.pearsonr(d.dropna(subset=["g_V", "g_R"]).g_V, d.dropna(subset=["g_V", "g_R"]).g_R); o.update({"pearson_raw": float(rr), "pearson_raw_p": float(pp_)})
    H[lab] = o
res["h1_growth"] = H
fi = g[g.idn == 0]; ii = g[g.idn == 1]
zf = lambda r, n: np.arctanh(r) * np.sqrt(n - 3)
rf, ri = H["foreign"]["pearson_w"], H["Indonesian and regional"]["pearson_w"]
z = (np.arctanh(rf) - np.arctanh(ri)) / np.sqrt(1 / (len(fi) - 3) + 1 / (len(ii) - 3)); res["h1_growth"]["fisher_z_equal_corr_p"] = float(2 * stats.norm.sf(abs(z)))

# ---------------------------------------------------------------- D2. checks on the Indonesia/region coefficient
chk = {}
base = [("ln_wedge_usd", FEAT + MACRO, True), ("E_w", FEAT + MACRO, True)]
chk["leave_one_indonesian_platform_out"] = {}
for kname in L[L.idn == 1].key.unique():
    r_ = run(base, L[L.key != kname], bootstrap=False)
    chk["leave_one_indonesian_platform_out"][kname] = {o["dep"]: round(o["coef"]["idn"]["b"], 3) for o in r_}
chk["no_year_effects"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3)} for o in run([("ln_wedge_usd", FEAT + MACRO, False), ("E_w", FEAT + MACRO, False)], bootstrap=False)}
chk["ln_E_instead_of_E_w"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3), "p_wild": round(o["coef"]["idn"]["p_wild"], 3)} for o in run([("ln_E", FEAT + MACRO, True)])}
chk["E_unwinsorised"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3)} for o in run([("ecosystem_ratio", FEAT + MACRO, True)], bootstrap=False)}
chk["without_total_assets"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3), "n": o["n"]} for o in run([("ln_wedge_usd", [c for c in FEAT if c != "ln_assets_usd"] + MACRO, True), ("E_w", [c for c in FEAT if c != "ln_assets_usd"] + MACRO, True)], bootstrap=False)}
chk["excluding_pre_listing_years"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3), "n": o["n"]} for o in run(base, L[L.pre_listing == 0], bootstrap=False)}
chk["excluding_alibaba_rakuten_pinduoduo_shopify"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3)} for o in run(base, L[~L.platform.isin(["Alibaba", "Rakuten", "Pinduoduo", "Shopify"])], bootstrap=False)}
chk["with_emerging_market_dummy"] = {o["dep"]: {"b": round(o["coef"]["idn"]["b"], 3), "p": round(o["coef"]["idn"]["p"], 3), "p_wild": round(o["coef"]["idn"]["p_wild"], 3), "emerging_b": round(o["coef"]["emerging_market"]["b"], 3), "emerging_p": round(o["coef"]["emerging_market"]["p"], 3)} for o in run([("ln_wedge_usd", FEAT + ["emerging_market"] + MACRO, True), ("E_w", FEAT + ["emerging_market"] + MACRO, True)])}
res["checks"] = chk
json.dump(res, open("tables/kong_results.json", "w"), indent=1)

# ---------------------------------------------------------------- tables as markdown (Prof. Kong's format: caption block above, panels, stars, SE below)
star = lambda p: "∗∗∗" if p < 0.01 else "∗∗" if p < 0.05 else "∗" if p < 0.10 else ""
f2 = lambda x, dd=2: "" if pd.isna(x) else f"{x:,.{dd}f}"
def fmt_stat(v, c):
    big = c in ("wedge_usd", "assets_usd")
    return f2(v, 0) if big else f2(v, 2)
md = ["| Variable | N | Mean | P50 | SD | N | Mean | P50 | SD |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for (c, lab), (_, r) in zip(VARS, S.iterrows()):
    cells = []
    for name in ("Indonesian and regional", "Foreign"):
        cells += [f"{int(r[name + '|N']):,}", fmt_stat(r[name + "|Mean"], c), fmt_stat(r[name + "|P50"], c), fmt_stat(r[name + "|SD"], c)]
    md.append(f"| {lab} | " + " | ".join(cells) + " |")
open("tables/kong_table_summary.md", "w").write("\n".join(md) + "\n")

cm = ["| Variables | " + " | ".join(f"({i})" for i in range(1, k + 1)) + " |", "|---|" + "---:|" * k]
for i in range(k):
    cells = []
    for j in range(k):
        if j > i: cells.append("")
        elif i == j: cells.append("1")
        else: cells.append(f"{C[i, j]:.2f}{star(P[i, j])}")
    cm.append(f"| ({i + 1}) {CV[i][1]} | " + " | ".join(cells) + " |")
open("tables/kong_table_corr.md", "w").write("\n".join(cm) + "\n")

def coef_rows(models, order, labels):
    rws = []
    for nm in order:
        a, b2 = [f"{labels[nm]}"], [""]
        for m in models:
            c = m["coef"].get(nm)
            if c is None: a.append(""); b2.append("")
            else:
                a.append(f"{c['b']:.3f}{star(c['p'])}"); b2.append(f"({c['se']:.3f})")
        rws.append("| " + " | ".join(a) + " |"); rws.append("| " + " | ".join(b2) + " |")
    return rws
ncol = len(main)
head = ["| *Dependent variable* | ln(Wedge) | ln(Wedge) | ln(Wedge) | Ecosystem ratio | Ecosystem ratio | Ecosystem ratio |", "|---|" + "---:|" * ncol,
        "| | (1) | (2) | (3) | (4) | (5) | (6) |"]
order = ["idn", "ln1_years_listed", "ln_assets_usd"] + TYPES + MACRO + ["const"]
tail = ["| Observations | " + " | ".join(f"{m['n']:,}" for m in main) + " |", "| Platforms (clusters) | " + " | ".join(str(m["clusters"]) for m in main) + " |",
        "| *R*^2^ | " + " | ".join(f"{m['r2']:.3f}" for m in main) + " |", "| Year dummies | " + " | ".join("Yes" if m["year_fe"] else "No" for m in main) + " |",
        "| Wild-bootstrap *p*, IndonesiaRegion | " + " | ".join(f"{m['coef']['idn']['p_wild']:.3f}" for m in main) + " |"]
open("tables/kong_table_ols.md", "w").write("\n".join(head + coef_rows(main, order, NAMES) + tail) + "\n")

gm = ["| *Dependent variable* | g(R) | g(R) | g(R) |", "|---|---:|---:|---:|", "| Sample | All platforms | Foreign | Indonesian and regional |", "| | (1) | (2) | (3) |"]
Hm = [H["all, with group interaction"], H["foreign"], H["Indonesian and regional"]]
def hrow(nm, lab):
    a, b2 = [lab], [""]
    for m in Hm:
        c = m["coef"].get(nm)
        a.append("" if c is None else f"{c['b']:.3f}{star(c['p'])}"); b2.append("" if c is None else f"({c['se']:.3f})")
    return ["| " + " | ".join(a) + " |", "| " + " | ".join(b2) + " |"]
gm += hrow("g_V_w", "g(V)") + hrow("idn", "IndonesiaRegion") + hrow("gv_idn", "IndonesiaRegion × g(V)") + hrow("const", "Constant")
gm += ["| Observations | " + " | ".join(str(m["n"]) for m in Hm) + " |", "| Platforms (clusters) | " + " | ".join(str(m["clusters"]) for m in Hm) + " |",
       "| *R*^2^ | " + " | ".join(f"{m['r2']:.3f}" for m in Hm) + " |", "| *p*-value, slope on g(V) equal to 1 | " + " | ".join(f"{m['slope_eq_1_p']:.3f}" for m in Hm) + " |",
       "| Pearson correlation, g(R) and g(V) | " + " | ".join(f"{m['pearson_w']:.3f}" for m in Hm[:1] + Hm[1:]) + " |"]
open("tables/kong_table_h1_growth.md", "w").write("\n".join(gm) + "\n")
print(json.dumps({k: res[k] for k in ("n_platform_years", "n_platforms", "n_idn_platforms", "corr", "selfcheck_se_max_abs_diff_vs_statsmodels")}, indent=1))
