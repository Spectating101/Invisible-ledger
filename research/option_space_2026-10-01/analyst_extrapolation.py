"""EXPLORATORY angle 1 (2 Oct 2026): do analysts treat take-rate-driven revenue growth as repeatable?
Panel: tables/event_study_surprise_panel.csv (S = actual revenue / LSEG consensus - 1, YoY growth gR split into volume gV and take rate dm).
share = dm / gR (part of YoY revenue growth from the take rate), clipped to [-1, 2]. If forecasters extrapolate repricing, surprises should be
NEGATIVE after quarters with high share (growth fades), i.e. S_t ~ share_{t-1} < 0.  Firm fixed effects, errors clustered by calendar quarter.
Unit of inference caveat: few firms; 'cal_q' clusters share the 2022-23 shock.  Not pre-registered; exploratory."""
import numpy as np, pandas as pd, statsmodels.formula.api as smf
D = pd.read_csv("tables/event_study_surprise_panel.csv", parse_dates=["date"]).sort_values(["firm", "date"])
D["share"] = D["share"].astype(float)
D["share_lag"] = D.groupby("firm").share.shift(1); D["dm_lag"] = D.groupby("firm").dm.shift(1); D["gR_lag"] = D.groupby("firm").gR.shift(1)
D["high_lag"] = (D.dm_lag.abs() > 0.05).astype(float).where(D.dm_lag.notna())
print("events", len(D), "firms", D.firm.nunique(), D.groupby("firm").size().to_dict())
def run(f, d, label):
    d = d.dropna(subset=[v for v in ["S","share_lag","dm_lag","high_lag","share"] if v in f]); g = pd.factorize(d.cal_q)[0]
    r = smf.ols(f, d).fit(cov_type="cluster", cov_kwds={"groups": g}); print("\n==", label, f"(n={int(r.nobs)})")
    for k in [x for x in r.params.index if not x.startswith("C(")]: print(f"  {k:10s} coef {r.params[k]:+.4f}  se {r.bse[k]:.4f}  p {r.pvalues[k]:.3f}")
run("S ~ share_lag + C(firm)", D, "A: surprise vs prior-quarter take-rate share of growth")
run("S ~ dm_lag + C(firm)", D, "B: surprise vs prior-quarter YoY change in log take rate")
run("S ~ high_lag + C(firm)", D, "C: surprise after a high-take-rate-change quarter (|dm|>0.05)")
run("S ~ share + C(firm)", D, "D: contemporaneous share (consensus already knows the quarter's mix?)")
g = D.dropna(subset=["high_lag"]).groupby("high_lag").S.agg(["mean", "std", "count"]); print("\nmean surprise by prior-quarter high take-rate change:\n", g.round(4))
by = D.dropna(subset=["share_lag"]).assign(top=lambda x: x.share_lag > x.share_lag.median()).groupby("top").S.agg(["mean", "count"]); print("\nmean surprise, prior share above vs below median:\n", by.round(4))
