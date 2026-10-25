"""H1 take-rate test re-expressed with the simple percentage change g(m) = (m_t - m_t-1) / m_t-1 (25 Oct 2026). EXPLORATORY.

Prof. Kong asked that changes be measured as simple percentage changes and not as changes in logs. The main H1 test (h1_extended.py) uses |change in
log take rate| per platform-year, one median per platform, Indonesia and region (5) against abroad (27), one-sided Mann-Whitney. The same pairs
are used here (same sample, same exclusions); only the measure changes: g(m) = exp(dlnm) - 1 exactly. Reports the group medians, the ratio, the
Mann-Whitney and permutation p-values, and the version with the symmetric measure |m_t - m_t-1| / mean(m_t, m_t-1) as a check, because a fall in the
take rate can be at most -100 percent while a rise has no limit.
Run from this folder: python3 h1_simple_change.py -> tables/h1_simple_change.json"""
import json
import numpy as np, pandas as pd
from scipy import stats
rng = np.random.default_rng(20261025)
T = pd.read_csv("tables/transitions_master.csv"); P = pd.read_csv("tables/l_panel.csv"); S = pd.read_csv("tables/spinoff_panel.csv")
def trans(df, firm_col="firm"):
    df = df.sort_values([firm_col, "year"]).copy(); df["m"] = df.R / df.V
    df["m0"] = df.groupby(firm_col).m.shift(); df["gap"] = df.groupby(firm_col).year.diff()
    df = df[df.gap == 1]; df["dlnm"] = np.log(df.m) - np.log(df.m0)
    return df[[firm_col, "year", "dlnm", "m0", "m"]].rename(columns={firm_col: "firm"})
idn = T[T.set == "IDN_main"].rename(columns={"y1": "year"}).assign(m0=lambda d: d.m0_pct / 100, m=lambda d: d.m1_pct / 100)[["firm", "year", "dlnm", "m0", "m"]].assign(group="Indonesia")
grab = P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab on-demand")
goto = P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo on-demand")
reg = trans(pd.concat([grab, goto])[lambda d: d.R > 0]).assign(group="Indonesia")
ext = T[T.set == "EXT_clean"].rename(columns={"y1": "year"}).assign(m0=lambda d: d.m0_pct / 100, m=lambda d: d.m1_pct / 100)[["firm", "year", "dlnm", "m0", "m"]].assign(group="Foreign (proposal 8)")
nw = S[(S.flag_1p != "exclude") & S.g_m.notna()].rename(columns={"entity": "firm", "g_m": "dlnm"}).assign(m0=lambda d: d.m / np.exp(d.dlnm))[["firm", "year", "dlnm", "m0", "m"]].assign(group="Foreign (new)")
A = pd.concat([idn, reg, ext, nw], ignore_index=True)
A["abs_log"] = A.dlnm.abs(); A["abs_simple"] = (np.exp(A.dlnm) - 1).abs(); A["abs_sym"] = (A.m - A.m0).abs() / ((A.m + A.m0) / 2)
A["is_idn"] = A.group == "Indonesia"
out = {"pairs": int(len(A)), "platforms_idn": int(A[A.is_idn].firm.nunique()), "platforms_foreign": int(A[~A.is_idn].firm.nunique())}
def compare(col):
    f = A.groupby(["firm", "is_idn"])[col].median().reset_index(); a = f[f.is_idn][col].values; b = f[~f.is_idn][col].values
    obs = np.median(a) - np.median(b); pool = np.concatenate([a, b]); k = len(a); hits = 0
    for _ in range(9999):
        rng.shuffle(pool); hits += (np.median(pool[:k]) - np.median(pool[k:])) >= obs
    return {"median_idn": float(np.median(a)), "median_foreign": float(np.median(b)), "ratio": float(np.median(a) / np.median(b)), "mannwhitney_p": float(stats.mannwhitneyu(a, b, alternative="greater").pvalue), "permutation_p": (hits + 1) / 10000}
out["log_change (as in the chapter)"] = compare("abs_log"); out["simple_percentage_change"] = compare("abs_simple"); out["symmetric_change"] = compare("abs_sym")
# direction: share of pairs in which revenue grew faster than transaction value (take rate rose)
out["share_take_rate_rose"] = {"idn": float((A[A.is_idn].dlnm > 0).mean()), "foreign": float((A[~A.is_idn].dlnm > 0).mean())}
s = json.dumps(out, indent=1); print(s); open("tables/h1_simple_change.json", "w").write(s)
