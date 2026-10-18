"""Spin-off tests S1-S3 (publishable_track/PREREGISTRATION.md), written 3 Oct 2026 while the new-firm extractions were running.
Before writing this, only the Liquidity Services and Alibaba rows were looked at (quality check of the first batch).

Inputs: quote-checked extraction CSVs (entity,period,field,value,unit,...) for the new firms, in ../tables/src/spinoff_*_extraction.csv.
Run: python3 spinoff_tests.py   -> prints results and writes ../tables/spinoff_panel.csv, ../tables/spinoff_results.json"""
import glob, json, pathlib
import numpy as np, pandas as pd
from scipy import stats

HERE = pathlib.Path(__file__).parent
SRC = sorted(glob.glob(str(HERE.parent / "tables/src/spinoff_*_extraction.csv")))
SCALE = {"thousand": 1e-3, "million": 1.0, "billion": 1e3}


def to_million(v, unit):
    u = str(unit).lower()
    for k, f in SCALE.items():
        if k in u:
            return v * f
    return v * 1e-6 if u.strip() else np.nan        # plain currency units (no scale word)


def build_panel():
    d = pd.concat([pd.read_csv(f, dtype=str) for f in SRC], ignore_index=True)
    d = d[d.value.notna() & (d.value.str.strip() != "") & ~d.field.str.endswith("_restated")]
    d["year"] = d.period.str.extract(r"(\d{4})").astype(int)
    d["val"] = [to_million(float(v), u) for v, u in zip(d.value, d.unit)]
    p = d.pivot_table(index=["entity", "year"], columns="field", values="val", aggfunc="first").reset_index()
    for c in ("V", "revenue", "rev_1p", "ocf", "capex", "capex_sw"):
        if c not in p: p[c] = np.nan
    p["share_1p"] = p.rev_1p / p.revenue
    p["flag_1p"] = np.where(p.share_1p > 0.5, "exclude", np.where(p.share_1p >= 0.2, "flag", "keep"))
    p["fcf"] = p.ocf - p.capex.abs() - p.capex_sw.abs().fillna(0)
    p["fcf_margin"] = p.fcf / p.revenue
    p["m"] = p.revenue / p.V
    p = p.sort_values(["entity", "year"])
    g = p.groupby("entity")
    consecutive = g.year.diff() == 1
    p["g_V"] = np.where(consecutive, np.log(p.V) - np.log(g.V.shift()), np.nan)
    p["g_m"] = np.where(consecutive, np.log(p.m) - np.log(g.m.shift()), np.nan)
    p["g_R"] = p.g_V + p.g_m
    p["g_R_next"] = np.where(g.year.shift(-1) - p.year == 1, g.g_R.shift(-1), np.nan)
    return p


def wild_cluster_t(y, X, cl, j1, j2, B=999, seed=1):
    """t-stat of b[j1]-b[j2] with cluster-robust SE; p-value from a wild cluster bootstrap (Rademacher) imposing the null."""
    rng = np.random.default_rng(seed)
    def fit(yv):
        b, *_ = np.linalg.lstsq(X, yv, rcond=None); e = yv - X @ b
        XtXi = np.linalg.inv(X.T @ X); meat = np.zeros((X.shape[1],) * 2)
        for c in np.unique(cl):
            s = X[cl == c].T @ e[cl == c]; meat += np.outer(s, s)
        V = XtXi @ meat @ XtXi; r = np.zeros(X.shape[1]); r[j1], r[j2] = 1, -1
        return b, r @ b, np.sqrt(r @ V @ r)
    b, diff, se = fit(y); t0 = diff / se
    # restricted fit: impose b[j1] = b[j2]
    Xr = np.delete(X, j2, axis=1).copy(); Xr[:, j1 if j1 < j2 else j1 - 1] += X[:, j2]
    br, *_ = np.linalg.lstsq(Xr, y, rcond=None); yhat = Xr @ br; er = y - yhat
    cls = np.unique(cl); ts = []
    for _ in range(B):
        w = dict(zip(cls, rng.choice([-1.0, 1.0], len(cls))))
        ys = yhat + er * np.array([w[c] for c in cl]); _, d2, s2 = fit(ys); ts.append(d2 / s2)
    p_one_sided = float(np.mean(np.array(ts) >= t0))
    return dict(b=b.tolist(), diff=float(diff), se=float(se), t=float(t0), p_one_sided=p_one_sided, n=int(len(y)), firms=int(len(cls)))


def s1(p, drop_flagged=False, ranks=False):
    q = p[(p.flag_1p != "exclude") & p.year.between(2015, 2025)].dropna(subset=["g_R_next", "g_V", "g_m"])
    if drop_flagged: q = q[q.flag_1p == "keep"]
    cols = ["g_R_next", "g_V", "g_m"]
    q = q.copy()
    for c in cols:
        lo, hi = q[c].quantile([0.01, 0.99]); q[c] = q[c].clip(lo, hi)
        if ranks: q[c] = q[c].rank(pct=True)
    if len(q) < 10 or q.entity.nunique() < 4: return {"n": int(len(q)), "note": "too few observations"}
    X = np.column_stack([np.ones(len(q)), q.g_V, q.g_m])
    return wild_cluster_t(q.g_R_next.values, X, q.entity.values, 1, 2)


def s2(p, y0, y1):
    rows = []
    for e, g in p[p.flag_1p != "exclude"].groupby("entity"):
        g = g.set_index("year")
        if y0 in g.index and y1 in g.index and np.isfinite(g.loc[y0, "fcf_margin"]) and np.isfinite(g.loc[y0, "m"]) and np.isfinite(g.loc[y1, "m"]):
            rows.append((e, g.loc[y0, "fcf_margin"], np.log(g.loc[y1, "m"]) - np.log(g.loc[y0, "m"])))
    t = pd.DataFrame(rows, columns=["entity", "fcf_margin", "dlnm"])
    out = {"firms": len(t), "rows": t.round(4).to_dict("records")}
    if len(t) >= 4:
        neg, pos = t[t.fcf_margin < 0].dlnm, t[t.fcf_margin >= 0].dlnm
        if len(neg) and len(pos):
            out["mannwhitney_p_neg_greater"] = float(stats.mannwhitneyu(neg, pos, alternative="greater").pvalue)
        out["spearman"] = float(stats.spearmanr(t.fcf_margin, t.dlnm).statistic)
    return out


def s3(p):
    res = []
    for e, g in p[p.flag_1p != "exclude"].groupby("entity"):   # sample rule applies here too (fixed after first run, see addendum)
        g = g.sort_values("year"); has = g.V.notna().values
        if has.any() and not has[-1]:                      # V reported earlier but not in the latest year
            last = g[g.V.notna()].year.max(); w = g[g.year.between(last - 2, last)]
            if len(w) == 3 and w.m.notna().all() and w.revenue.notna().all():
                dR = np.log(w.revenue.iloc[-1] / w.revenue.iloc[0]); dm = np.log(w.m.iloc[-1] / w.m.iloc[0])
                res.append({"entity": e, "last_year_with_V": int(last), "share_from_cut": float(dm / dR) if dR != 0 else None})
    hits = [r for r in res if r["share_from_cut"] is not None and r["share_from_cut"] > 0.5]
    return {"firms": res, "share_above_half": f"{len(hits)} of {len(res)}", "prediction_holds": len(res) > 0 and len(hits) >= len(res) / 2}


if __name__ == "__main__":
    p = build_panel()
    p.to_csv(HERE.parent / "tables/spinoff_panel.csv", index=False)
    out = {"S1": s1(p), "S1_ranks": s1(p, ranks=True), "S1_no_flagged": s1(p, drop_flagged=True),
           "S2_main_2021_2023": s2(p, 2021, 2023), "S2_placebo_2017_2019": s2(p, 2017, 2019), "S3": s3(p),
           "firms": sorted(p.entity.unique().tolist()), "excluded_1p_firm_years": int((p.flag_1p == "exclude").sum())}
    json.dump(out, open(HERE.parent / "tables/spinoff_results.json", "w"), indent=1, default=float)
    print(json.dumps({k: v for k, v in out.items() if k != "firms"}, indent=1, default=float)[:4000])
