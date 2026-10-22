"""M1-M2 upgrade (22 Oct 2026, EXPLORATORY; specification fixed in PREREGISTRATION.md addendum of 22 Oct BEFORE this script is run on the licensed market values).

The registered market-value test (m1_market_value.py, 8 Oct) rests on 28 firm clusters, uses changes in market capitalisation (which also move when a company
issues shares) and drops Grab, GoTo and Sea from the main sample. This script keeps the registered specification and adds, on the same panel:
  U1  Wild cluster bootstrap-t p-values (Rademacher weights, null imposed, clusters = firms, 9,999 draws) for M2 (b1 = 0) and M1 (b1 = b2), alongside the
      analytic cluster-robust ones. With 28 clusters the analytic p-values are approximate; this is the small-sample check.
  U2  Leave-one-firm-out: range of b1, b1 - b2 and both p-values when any one firm is dropped.
  U3  Outcome net of share issuance: the annual log price change from year-end closing prices (--prices), instead of the change in log market value.
  U4  Levels with firm and year fixed effects: ln(market value) on ln(transaction value) and ln(take rate). More variation than changes; same clustering.
  U5  Grab, GoTo and Sea treated by size of the segment: if --group-revenue is given (firm, year, group_revenue in the same units as R), firm-years where the
      segment is at least 70 percent of group revenue are added to the main sample; the rest stay out.
  U6  Power: the smallest b1 - b2 the registered design could detect with 80 percent power at 5 percent one-sided, from its standard error.
Run (researcher's machine, licensed files in _local/licensed_data/):
  python3 m1_upgrade.py <mcap_reporting_ccy.csv> [--prices <year_end_close.csv: firm,date,close>] [--group-revenue <firm,year,group_revenue>] [--out <path>] -> tables/m1_upgrade_results.json
Self-test (no licensed data; synthetic panel with known coefficients): python3 m1_upgrade.py --selftest
Output holds coefficients, counts and p-values only. No market values are written."""
import json, sys
import numpy as np, pandas as pd
from scipy import stats

def design(d, with_year=True):
    X = d[["dlnV", "dlnm"]].copy()
    if with_year:
        Y = pd.get_dummies(d.year, prefix="y", dtype=float)
        X = pd.concat([X, Y], axis=1)
    return X

def cr_fit(X, y, g):
    """OLS with CR1 cluster-robust variance. X, y numpy; g integer cluster codes. Returns beta, V."""
    N, k = X.shape
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    u = y - X @ beta
    order = np.argsort(g, kind="stable"); gs = g[order]
    S = X[order] * u[order, None]
    idx = np.r_[0, np.flatnonzero(np.diff(gs)) + 1]
    Sg = np.add.reduceat(S, idx, axis=0)
    G = len(idx)
    meat = Sg.T @ Sg
    V = (G / (G - 1)) * ((N - 1) / (N - k)) * XtX_inv @ meat @ XtX_inv
    return beta, V, G

def t_contrast(beta, V, c):
    est = float(c @ beta); se = float(np.sqrt(c @ V @ c)); return est, se, est / se

def wild_p(y, X, g, c, restricted_cols, B=9999, seed=20261022):
    """Wild cluster bootstrap-t, null imposed. restricted_cols: column indices of X kept in the restricted model (those that do not
    contain the tested contrast). For H0: b1 = b2 pass the model with dlnR; for H0: b1 = 0 drop dlnV. Returns the one-sided p (t* >= t)."""
    beta, V, G = cr_fit(X, y, g); est, se, t = t_contrast(beta, V, c)
    Xr = restricted_cols
    br = np.linalg.pinv(Xr.T @ Xr) @ Xr.T @ y
    fit_r = Xr @ br; res_r = y - fit_r
    rng = np.random.default_rng(seed)
    ng = len(np.unique(g)); gi = pd.factorize(g)[0]
    hits = 0; valid = 0
    for _ in range(B):
        w = rng.choice([-1.0, 1.0], size=ng)
        ys = fit_r + w[gi] * res_r
        bb, VV, _ = cr_fit(X, ys, g)
        e2, s2, t2 = t_contrast(bb, VV, c)
        if np.isfinite(t2):
            valid += 1; hits += (t2 >= t)
    return {"estimate": est, "se_cluster": se, "t": t, "p_analytic_one_sided": float(1 - stats.t.cdf(t, G - 1)),
            "p_wild_bootstrap_one_sided": (hits + 1) / (valid + 1), "clusters": int(G), "draws": int(valid)}

def mk_both(D, dep, B):
    """M2 (b1 > 0) and M1 (b1 > b2) on a changes panel D with columns firm, year, dlnV, dlnm and the outcome dep."""
    D = D.dropna(subset=[dep, "dlnV", "dlnm"]).copy()
    g = pd.factorize(D.firm)[0]; y = D[dep].values.astype(float)
    Xdf = design(D); X = Xdf.values.astype(float); cols = list(Xdf.columns)
    years = Xdf[[c for c in cols if c.startswith("y_")]].values.astype(float)
    dlnR = (D.dlnV + D.dlnm).values[:, None]
    c2 = np.zeros(X.shape[1]); c2[cols.index("dlnV")] = 1
    c1 = np.zeros(X.shape[1]); c1[cols.index("dlnV")] = 1; c1[cols.index("dlnm")] = -1
    Xr2 = np.column_stack([D.dlnm.values, years])      # H0: b1 = 0
    Xr1 = np.column_stack([dlnR, years])               # H0: b1 = b2 (so b1 dlnV + b2 dlnm = b dlnR)
    m2 = wild_p(y, X, g, c2, Xr2, B); m1 = wild_p(y, X, g, c1, Xr1, B)
    beta, V, G = cr_fit(X, y, g)
    return {"firms": int(D.firm.nunique()), "firm_years": int(len(D)), "b1_volume": float(beta[cols.index("dlnV")]),
            "b2_take_rate": float(beta[cols.index("dlnm")]), "M2_b1_gt_0": m2, "M1_b1_gt_b2": m1}

def leave_one_out(D, dep):
    rows = []
    for f in sorted(D.firm.unique()):
        d = D[D.firm != f].dropna(subset=[dep, "dlnV", "dlnm"])
        g = pd.factorize(d.firm)[0]; Xdf = design(d); X = Xdf.values.astype(float); cols = list(Xdf.columns); y = d[dep].values.astype(float)
        beta, V, G = cr_fit(X, y, g)
        c2 = np.zeros(X.shape[1]); c2[cols.index("dlnV")] = 1; c1 = c2.copy(); c1[cols.index("dlnm")] = -1
        e2, s2, t2 = t_contrast(beta, V, c2); e1, s1, t1 = t_contrast(beta, V, c1)
        rows.append({"dropped": f, "b1": e2, "p_b1": float(1 - stats.t.cdf(t2, G - 1)), "b1_minus_b2": e1, "p_b1_minus_b2": float(1 - stats.t.cdf(t1, G - 1))})
    r = pd.DataFrame(rows)
    return {"cases": rows, "b1_range": [float(r.b1.min()), float(r.b1.max())], "b1_minus_b2_range": [float(r.b1_minus_b2.min()), float(r.b1_minus_b2.max())],
            "worst_p_b1": float(r.p_b1.max()), "worst_p_b1_minus_b2": float(r.p_b1_minus_b2.max()),
            "firms_dropped_that_flip_M2": r[r.p_b1 >= 0.05].dropped.tolist()}

def levels(P, B):
    """ln MV on ln V and ln m with firm and year fixed effects (firm effects removed by demeaning; they are nested in the clusters)."""
    d = P.dropna(subset=["lnmcap", "lnV", "lnR"]).copy(); d["lnm"] = d.lnR - d.lnV
    d = d[d.groupby("firm").year.transform("size") >= 3]
    Yd = pd.get_dummies(d.year, prefix="y", dtype=float)
    Z = pd.concat([d[["lnV", "lnm"]], Yd], axis=1).values.astype(float); y = d.lnmcap.values.astype(float)
    firm = pd.factorize(d.firm)[0]
    def dm(A):
        A = A.copy()
        for f in np.unique(firm): A[firm == f] -= A[firm == f].mean(axis=0)
        return A
    Zd = dm(Z); yd = dm(y[:, None])[:, 0]
    keep = np.abs(Zd).sum(axis=0) > 1e-12
    Zd = Zd[:, keep]; names = np.array(["lnV", "lnm"] + list(Yd.columns))[keep]
    beta, V, G = cr_fit(Zd, yd, firm)
    out = {}
    for nm, c in (("elasticity_volume_lnV", np.eye(len(names))[list(names).index("lnV")]), ("elasticity_take_rate_lnm", np.eye(len(names))[list(names).index("lnm")])):
        e, s, t = t_contrast(beta, V, c); out[nm] = {"estimate": e, "se_cluster": s, "p_two_sided": float(2 * (1 - stats.t.cdf(abs(t), G - 1)))}
    out.update({"firms": int(G), "firm_years": int(len(d)), "note": "levels with firm and year fixed effects; cluster-robust analytic p-values (CR1, t with G-1 df)"})
    return out

def power_note(se_diff, alpha=0.05, power=0.80):
    z = stats.norm.ppf(1 - alpha) + stats.norm.ppf(power)
    return {"se_of_b1_minus_b2": se_diff, "minimum_detectable_b1_minus_b2": float(z * se_diff),
            "reading": "the smallest gap between the volume and take-rate coefficients that the registered design would flag with 80 percent power at 5 percent one-sided"}

# ------------------------------------------------------------------ synthetic self-test
def synth(G=28, T=6, b1=0.6, b2=0.3, sd=0.35, seed=1):
    rng = np.random.default_rng(seed); rows = []
    for f in range(G):
        for t in range(T):
            dV = rng.normal(0.15, 0.3); dm = rng.normal(0.02, 0.2); rows.append({"firm": f"F{f}", "year": 2019 + t, "dlnV": dV, "dlnm": dm,
                         "dlnMV": b1 * dV + b2 * dm + rng.normal(0, sd) + 0.05 * (t - 2)})
    return pd.DataFrame(rows)

def selftest():
    D = synth()
    r = mk_both(D, "dlnMV", 999)
    print("alternative true (b1=0.6, b2=0.3):", json.dumps({k: r[k] for k in ("b1_volume", "b2_take_rate")}), "M2 p", round(r["M2_b1_gt_0"]["p_wild_bootstrap_one_sided"], 4),
          "M1 p", round(r["M1_b1_gt_b2"]["p_wild_bootstrap_one_sided"], 4))
    # size under the null: b1 = b2 = 0.4 (M1 null) and b1 = 0 (M2 null); share of rejections at 5 percent across simulations
    rej1 = rej2 = 0; S = 300
    for s in range(S):
        a = mk_both(synth(b1=0.4, b2=0.4, seed=100 + s), "dlnMV", 199); rej1 += a["M1_b1_gt_b2"]["p_wild_bootstrap_one_sided"] < 0.05
        b = mk_both(synth(b1=0.0, b2=0.3, seed=500 + s), "dlnMV", 199); rej2 += b["M2_b1_gt_0"]["p_wild_bootstrap_one_sided"] < 0.05
    print(f"size at 5% over {S} simulated panels: M1 null {rej1 / S:.3f}, M2 null {rej2 / S:.3f} (should be near 0.05)")
    lo = leave_one_out(D, "dlnMV"); print("leave-one-out b1 range", [round(v, 3) for v in lo["b1_range"]])
    print(json.dumps(power_note(0.31)))

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--selftest":
        selftest(); sys.exit(0)
    mcap_path = args[0]; opt = {a: args[i + 1] for i, a in enumerate(args) if a in ("--prices", "--group-revenue", "--out")}
    out_path = opt.get("--out", "tables/m1_upgrade_results.json")
    src = open("m1_market_value.py").read(); head = src[: src.index("def run(d, label):")]
    sys.argv = ["m1_market_value.py", mcap_path]       # the head reads sys.argv[1]
    ns = {}; exec(compile(head, "m1_market_value_head", "exec"), ns)
    D, P = ns["D"], ns["P"]; main = D[D.group == "main"]
    res = {"registered_spec_main": mk_both(main, "dlnMV", 9999), "all_with_segments": mk_both(D, "dlnMV", 9999),
           "leave_one_firm_out_main": leave_one_out(main, "dlnMV"), "levels_main": levels(P[P.group == "main"], 9999)}
    reg = json.load(open("tables/m1_market_value_results.json"))["main"]
    res["power_registered_design"] = power_note(reg["se_diff"])
    if "--prices" in opt:
        px = pd.read_csv(opt["--prices"], parse_dates=["date"]); px = px[px.date.dt.month == 12].assign(year=lambda d: d.date.dt.year)[["firm", "year", "close"]]
        Q = P.merge(px, on=["firm", "year"], how="inner").sort_values(["firm", "year"]); Q["lnP"] = np.log(Q.close)
        prev = Q.groupby("firm").shift(); ok = Q.year - prev.year == 1
        E = pd.DataFrame({"firm": Q.firm, "year": Q.year, "group": Q.group, "dlnP": Q.lnP - prev.lnP, "dlnV": Q.lnV - prev.lnV,
                          "dlnm": (Q.lnR - prev.lnR) - (Q.lnV - prev.lnV)})[ok].dropna()
        res["net_of_issuance_price_change_main"] = mk_both(E[E.group == "main"], "dlnP", 9999)
        res["net_of_issuance_note"] = "outcome = annual log change in the year-end closing price (adjusted for splits); dividends ignored"
    if "--group-revenue" in opt:
        gr = pd.read_csv(opt["--group-revenue"]); S_ = P.merge(gr, on=["firm", "year"], how="inner"); S_["share"] = S_.R / S_.group_revenue
        keep = S_[(S_.share >= 0.7) & (S_.group != "main")][["firm", "year"]]
        add = D.merge(keep, on=["firm", "year"], how="inner")
        res["segments_at_least_70pct_of_group_added"] = mk_both(pd.concat([main, add]), "dlnMV", 9999)
        res["segment_share_by_firm_year"] = S_[["firm", "year", "share"]].round(3).to_dict("records")
    s = json.dumps(res, indent=1, default=float); print(s); open(out_path, "w").write(s)
