"""Does the market price revenue growth that comes from the take rate differently from growth that comes from volume? (1 Oct 2026, exploratory)

Unit: one firm-quarter earnings announcement. Outcome: CAR[0,+1] = market-model abnormal return over the announcement day and the next trading day
(market model estimated on trading days -270..-20; benchmark .SPX, or .JKSE for GOTO.JK). Regressors: YoY log growth in transaction value V (gV) and the YoY change
in log take rate (dm = gR - gV), so that revenue growth gR = gV + dm. Firm fixed effects; standard errors clustered by calendar quarter of the announcement.
Second spec uses the CHANGE in those YoY numbers vs the previous quarter (acceleration), a crude proxy for surprise.
Prices come from LSEG (licensed) and are NOT in the repo; only the derived panel is saved. Needs: peers_quarterly.csv, grab/goto/mmyt tables, corpus_peers, prices dir.
Run: PYTHONPATH=... python3 event_study.py <corpus_peers_dir> <prices_dir>
"""
import datetime as dt, pathlib, re, sys
import numpy as np, pandas as pd, statsmodels.formula.api as smf

HERE = pathlib.Path(__file__).parent; ROOT = HERE.parents[1]
corpus, prices = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
# ---------- quarterly V, R panel
p = pd.read_csv(HERE / "tables/peers_quarterly.csv")[["firm", "quarter", "V", "R"]]
S = re.search(r'S = """(.*?)"""', (HERE / "mmyt_incentives.py").read_text(), re.S).group(1)
m = pd.DataFrame([x.split("|") for x in S.split()], columns=["quarter", "V", "R", "ind"])[["quarter", "V", "R"]].astype({"V": float, "R": float}); m["firm"] = "MMYT"
g = pd.read_csv(HERE / "tables/grab_quarterly_verified.csv", index_col=0).reset_index().rename(columns={"index": "quarter", "od_gmv": "V", "od_rev": "R"})[["quarter", "V", "R"]]; g["firm"] = "GRAB"
q = pd.read_csv(HERE / "tables/goto_ondemand_quarterly_net.csv", index_col=0).reset_index().rename(columns={"index": "quarter", "gtv": "V", "net": "R"})[["quarter", "V", "R"]]; q["firm"] = "GOTO"
P = pd.concat([p, m, g, q], ignore_index=True)
P["y"] = P.quarter.str[:4].astype(int); P["n"] = P.quarter.str[5].astype(int); P["t"] = P.y * 4 + P.n
P = P.sort_values(["firm", "t"]); out = []
for f, d in P.groupby("firm"):
    d = d.set_index("t"); d["gV"] = np.log(d.V / d.V.shift(4, freq=None)) if False else np.nan
    d = d.reindex(range(d.index.min(), d.index.max() + 1)); d["firm"] = f; d["quarter"] = d.quarter.fillna(""); 
    d["gV"] = np.log(d.V / d.V.shift(4)); d["gR"] = np.log(d.R / d.R.shift(4)); d["dm"] = d.gR - d.gV
    d["accV"] = d.gV - d.gV.shift(1); d["accm"] = d.dm - d.dm.shift(1); d["accR"] = d.gR - d.gR.shift(1)
    out.append(d.dropna(subset=["V", "R"]))
P = pd.concat(out).reset_index().rename(columns={"index": "t"})
# ---------- announcement dates
def qend(qs): y, n = int(qs[:4]), int(qs[5]); return dt.date(y, 3 * n, [31, 30, 30, 31][n - 1])
cov = pd.read_csv(ROOT / "data/quarterly/quarterly_panel_source_coverage.csv")
ann = {}
for _, r in cov[cov.platform.isin(["Grab", "GoTo"])].iterrows():
    ann[("GRAB" if r.platform == "Grab" else "GOTO", f"{int(r.fiscal_year)}Q{int(r.quarter)}")] = dt.date.fromisoformat(r.announcement_date)
for f in P.firm.unique():
    if f in ("GRAB", "GOTO"): continue
    docs = sorted((dt.date.fromisoformat(x.name[:10]), x.read_text(errors="ignore")) for x in (corpus / f).glob("*.txt"))
    for _, r in P[P.firm == f].iterrows():
        e = qend(r.quarter); tok = [f"{r.R:,.0f}", f"{r.R:.1f}", f"{int(r.R):,}"]
        for d, t in docs:
            if 10 <= (d - e).days <= 130 and any(re.search(r"(?<![\d.,])" + re.escape(k) + r"(?![\d])", t) for k in tok):
                ann[(f, r.quarter)] = d; break
P["date"] = [ann.get((f, qq)) for f, qq in zip(P.firm, P.quarter)]
# ---------- CARs
def load(name): d = pd.read_csv(prices / f"{name}.csv", parse_dates=["date"]).set_index("date").close.sort_index(); return d[~d.index.duplicated()]
bm = {"SPX": load("_SPX"), "JKSE": load("_JKSE")}; px = {f: load(f.replace("GRAB", "GRAB_OQ").replace("GOTO", "GOTO_JK").replace("UBER", "UBER_N").replace("LYFT", "LYFT_OQ").replace("DASH", "DASH_O").replace("ABNB", "ABNB_O").replace("BKNG", "BKNG_O").replace("EBAY", "EBAY_O").replace("ETSY", "ETSY_O").replace("MMYT", "MMYT_OQ")) for f in P.firm.unique()}
cars = []
for _, r in P.iterrows():
    if r.date is None or pd.isna(r.date): cars.append(np.nan); continue
    s = px[r.firm]; b = bm["JKSE" if r.firm == "GOTO" else "SPX"]; ret = pd.concat([s.pct_change(), b.pct_change()], axis=1, keys=["r", "m"]).dropna()
    ev = ret.index.searchsorted(pd.Timestamp(r.date))
    if ev < 140 or ev + 1 >= len(ret): cars.append(np.nan); continue
    est = ret.iloc[ev - 270: ev - 20]; est = est[(est.r.abs() < 0.5)]
    if len(est) < 120: cars.append(np.nan); continue
    beta, alpha = np.polyfit(est.m, est.r, 1); w = ret.iloc[ev: ev + 2]
    cars.append(float((w.r - (alpha + beta * w.m)).sum()))
P["car"] = cars; P["cal_q"] = [f"{d.year}Q{(d.month-1)//3+1}" if d else None for d in P.date]
D = P.dropna(subset=["car", "gV", "dm"]).copy(); D = D[D.car.abs() < 0.6]
D.drop(columns=["V", "R"]).round(4).to_csv(HERE / "tables/event_study_panel.csv", index=False)
print(f"events with CAR and YoY growth: {len(D)} across {D.firm.nunique()} firms; mean CAR {D.car.mean():+.4f}; by firm:"); print(D.groupby("firm").agg(n=("car", "size"), mean_car=("car", "mean")).round(4).to_string())
def run(form, label):
    r = smf.ols(form, D).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(D.cal_q)[0]})
    print(f"\n== {label}\n" + r.summary().tables[1].as_text().split("\n")[0:1][0]); 
    for k in [x for x in r.params.index if not x.startswith("C(")]:
        print(f"  {k:10s} coef {r.params[k]:+.4f}   se {r.bse[k]:.4f}   p {r.pvalues[k]:.3f}")
    if "gV" in r.params and "dm" in r.params:
        t = r.t_test("gV - dm = 0"); print(f"  test gV = dm: diff {float(t.effect[0]):+.4f}, p {float(t.pvalue):.3f}")
    print(f"  n={int(r.nobs)}  R2={r.rsquared:.3f}"); return r
run("car ~ gV + dm + C(firm)", "Spec A: YoY volume growth vs take-rate change, firm fixed effects")
run("car ~ gR + C(firm)", "Spec A0: total revenue growth only")
Dacc = D.dropna(subset=["accV", "accm"]); D_all = D; D = Dacc
run("car ~ accV + accm + C(firm)", "Spec B: acceleration (change in YoY volume growth vs change in YoY take-rate change)")
D = D_all[D_all.firm.isin(["GRAB", "GOTO", "MMYT"])]
run("car ~ gV + dm", "Spec C: incentive-disclosing firms only (Grab, GoTo, MakeMyTrip), no FE")
