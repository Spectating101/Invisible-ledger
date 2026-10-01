"""Event study part 2: is a revenue SURPRISE priced differently when the revenue growth is driven by the take rate? (1 Oct 2026, exploratory)
S = actual revenue / consensus mean - 1 (LSEG; consensus is licensed and NOT in the repo). Matched to the announcement within +-6 days; at least 5 estimates.
Specs (firm fixed effects, errors clustered by announcement calendar quarter): A) CAR ~ S ; B) CAR ~ S + S x highdm + highdm, where highdm = |YoY change in log take rate| > 0.05;
C) CAR ~ S + S x share, share = dm / gR clipped to [-1, 2] (the part of revenue growth coming from the take rate).
Run: python3 event_study_surprise.py <consensus_csv>
"""
import pathlib, sys
import numpy as np, pandas as pd, statsmodels.formula.api as smf
H = pathlib.Path(__file__).parent
E = pd.read_csv(H / "tables/event_study_panel.csv", parse_dates=["date"])
CONS = pd.read_csv(sys.argv[1], parse_dates=["date"]).dropna(subset=["date", "mean", "actual"]); CONS = CONS[(CONS.n_est >= 5) & (CONS["mean"] > 0)]
rows = []
for _, r in E.iterrows():
    c = CONS[(CONS.firm == r.firm) & ((CONS.date - r.date).abs() <= pd.Timedelta(days=6))]
    if len(c): c = c.iloc[(c.date - r.date).abs().argsort()].iloc[0]; rows.append(c.actual / c["mean"] - 1)
    else: rows.append(np.nan)
E["S"] = rows; D = E.dropna(subset=["S"]).copy(); D = D[D.S.abs() < 0.3]
D["highdm"] = (D.dm.abs() > 0.05).astype(int); D["share"] = (D.dm / D.gR.replace(0, np.nan)).clip(-1, 2); D["Sx"] = D.S * D.highdm; D["Ss"] = D.S * D.share
print(f"events with a matched revenue surprise: {len(D)} ({D.firm.nunique()} firms); mean S {D.S.mean():+.4f}, sd {D.S.std():.4f}; share of events with high take-rate change: {D.highdm.mean():.2f}")
g = pd.factorize(D.cal_q)[0]
def run(f, label):
    r = smf.ols(f, D).fit(cov_type="cluster", cov_kwds={"groups": g}); print("\n==", label)
    for k in [x for x in r.params.index if not x.startswith("C(")]: print(f"  {k:10s} coef {r.params[k]:+.3f}  se {r.bse[k]:.3f}  p {r.pvalues[k]:.3f}")
    print(f"  n={int(r.nobs)} R2={r.rsquared:.3f}"); return r
run("car ~ S + C(firm)", "A: revenue surprise")
run("car ~ S + Sx + highdm + C(firm)", "B: surprise x high take-rate change (|dm|>0.05)")
Dd = D.dropna(subset=["share"]); D = Dd; run("car ~ S + Ss + share + C(firm)", "C: surprise x share of growth from take rate")
D.round(4).to_csv(H / "tables/event_study_surprise_panel.csv", index=False)
