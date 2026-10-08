"""EXPLORATORY (9 Oct 2026; formed after seeing the H1 results, prompted by the oral question "why the wedge, not just D?").
Is Indonesia's larger take-rate movement a larger PRICE change, or the same price change on a thinner slice?
Same firms and firm-years as h1_extended.py part A (Indonesia main + Grab and GoTo on-demand; foreign = proposal's 8 + spin-off firms, 1P-heavy
years excluded). For each yearly transition: change in the share kept, m = R/V, in percentage points of transaction value (absolute) and in logs
(relative, what growth divergence D measures). Firm medians; one-sided Mann-Whitney (Indonesia greater).
Identity behind it: D = g(R) - g(V) = (change in m) / m, so a one-point change in m moves revenue growth by about 100/m percent (1 + E).
Run from this folder: python3 h1_points_vs_log.py -> tables/h1_points_vs_log.json"""
import json
import numpy as np, pandas as pd
from scipy import stats

T = pd.read_csv("tables/transitions_master.csv"); P = pd.read_csv("tables/l_panel.csv"); S = pd.read_csv("tables/spinoff_panel.csv")
rows = [dict(firm=r.firm, group="Indonesia" if r.set == "IDN_main" else "Foreign", m0=r.m0_pct / 100, m1=r.m1_pct / 100)
        for r in T[T.set.isin(["IDN_main", "EXT_clean"])].itertuples()]

def levels(df, name, group):
    df = df.sort_values("year")
    for a, b in zip(df.itertuples(), df.iloc[1:].itertuples()):
        if b.year - a.year == 1 and a.m > 0 and b.m > 0:
            rows.append(dict(firm=name, group=group, m0=a.m, m1=b.m))

for name, df in [("Grab on-demand", P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index()),
                 ("GoTo on-demand", P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].copy())]:
    df = df[df.R > 0].copy(); df["m"] = df.R / df.V; levels(df, name, "Indonesia")
for e, g in S[S.flag_1p != "exclude"].dropna(subset=["m"]).groupby("entity"):
    levels(g, e, "Foreign")

d = pd.DataFrame(rows)
d["change_points"] = (d.m1 - d.m0).abs() * 100; d["change_log"] = np.log(d.m1 / d.m0).abs(); d["share_kept_pct"] = d.m0 * 100
f = d.groupby(["firm", "group"]).agg(share_kept_pct=("share_kept_pct", "median"), change_points=("change_points", "median"),
                                     change_log=("change_log", "median"), n=("change_log", "size")).reset_index()
I, F = f[f.group == "Indonesia"], f[f.group == "Foreign"]
out = {"firms": {"Indonesia": len(I), "Foreign": len(F)},
       "median_share_kept_pct": {"Indonesia": float(I.share_kept_pct.median()), "Foreign": float(F.share_kept_pct.median())},
       "median_yearly_change_points": {"Indonesia": float(I.change_points.median()), "Foreign": float(F.change_points.median())},
       "median_yearly_change_log": {"Indonesia": float(I.change_log.median()), "Foreign": float(F.change_log.median())},
       "mannwhitney_p_points": float(stats.mannwhitneyu(I.change_points, F.change_points, alternative="greater").pvalue),
       "mannwhitney_p_log": float(stats.mannwhitneyu(I.change_log, F.change_log, alternative="greater").pvalue),
       "indonesian_firms": I.drop(columns="group").round(4).to_dict(orient="records")}
s = json.dumps(out, indent=1); print(s); open("tables/h1_points_vs_log.json", "w").write(s)
