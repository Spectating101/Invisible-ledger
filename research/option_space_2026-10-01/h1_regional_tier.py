"""H1 robustness with the REGIONAL TIER added (2 Oct 2026).  Same metric definitions as build_numbers.py (abs_dlnm, abs_D; identical firm-level permutation and
cluster bootstrap), same foreign benchmark (EXT_clean, 29 comparisons, 8 firms; and ex-Sea).  New transitions come from verified Grab 20-F and GoTo filings
(tables/l_panel.csv): Grab on-demand = Mobility + Deliveries summed (reported, no construction; regional scope), GoTo on-demand (Indonesia + Vietnam to 2024; 2022 GTV estimated).
Transitions with non-positive revenue are skipped (log undefined).  Sets: IDN_main (as examined), REGIONAL (Grab OD, GoTo OD), IDN_main+REGIONAL.
The proposal's headline test is NOT changed; this reports how the result behaves when the tier is added."""
import itertools, numpy as np, pandas as pd
from scipy import stats
rng = np.random.default_rng(20261002)
T = pd.read_csv("tables/transitions_master.csv")
P = pd.read_csv("tables/l_panel.csv")
g = P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab on-demand")
go = P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo on-demand")
rows = []
for d in (g, go):
    d = d.sort_values("year").set_index("year")
    for y in d.index:
        if y + 1 in d.index and d.loc[y, "R"] > 0 and d.loc[y + 1, "R"] > 0:
            a, b = d.loc[y], d.loc[y + 1]
            gV, gR = 100 * (b.V / a.V - 1), 100 * (b.R / a.R - 1)
            rows.append(dict(set="REGIONAL", firm=d.firm.iloc[0], y0=y, y1=y + 1, gV=gV, gR=gR, D_pp=gR - gV,
                             dlnm=np.log1p(gR / 100) - np.log1p(gV / 100)))
RG = pd.DataFrame(rows); RG["abs_dlnm"] = RG.dlnm.abs(); RG["abs_D"] = RG.D_pp.abs()
RG.round(3).to_csv("tables/h1_regional_transitions.csv", index=False)
IDN = T[T.set == "IDN_main"]; EXT = T[T.set == "EXT_clean"]; EXTX = EXT[EXT.firm != "Sea / Shopee"]
cols = ["firm", "abs_dlnm", "abs_D", "dlnm"]
IDNR = pd.concat([IDN[cols], RG[cols]]); REG = RG[cols]; IDN = IDN[cols]; EXT = EXT[cols]; EXTX = EXTX[cols]
def mw(a, b, c): return stats.mannwhitneyu(a[c], b[c], alternative="greater").pvalue
def perm(a, b, c):
    fm = pd.concat([a.groupby("firm")[c].median(), b.groupby("firm")[c].median()]).values; k = a.firm.nunique(); obs = a.groupby("firm")[c].median().mean()
    dist = np.array([fm[list(i)].mean() for i in itertools.combinations(range(len(fm)), k)]); return (dist >= obs - 1e-12).mean(), len(dist)
def boot(a, b, c, reps=400):
    fa, fb = a.firm.unique(), b.firm.unique(); out = []
    for _ in range(reps):
        sa, sb = rng.choice(fa, len(fa)), rng.choice(fb, len(fb))
        out.append(np.median(np.concatenate([a.loc[a.firm == f, c].values for f in sa])) - np.median(np.concatenate([b.loc[b.firm == f, c].values for f in sb])))
    return np.percentile(out, [2.5, 97.5])
res = []
for c in ("abs_dlnm", "abs_D"):
    for la, a in [("IDN_main (3 firms, as examined)", IDN), ("REGIONAL only (Grab OD, GoTo OD)", REG), ("IDN_main + REGIONAL (5 firms)", IDNR)]:
        for lb, b in [("EXT_clean (8 firms)", EXT), ("EXT_clean ex-Sea (7 firms)", EXTX)]:
            p, n = perm(a, b, c); lo, hi = boot(a, b, c)
            res.append(dict(metric=c, test_set=la, benchmark=lb, n_a=len(a), firms_a=a.firm.nunique(), median_a=a[c].median(), median_b=b[c].median(),
                            mw_obs_p=mw(a, b, c), firm_perm_p=p, combos=n, boot95=f"[{lo:.3f},{hi:.3f}]"))
R = pd.DataFrame(res); R.round(4).to_csv("tables/h1_regional_tier.csv", index=False)
tol = []
for la, a in [("IDN_main", IDN), ("REGIONAL", REG), ("IDN_main+REGIONAL", IDNR), ("EXT_clean", EXT), ("EXT_clean ex-Sea", EXTX)]:
    tol.append(dict(set=la, n=len(a), **{f"share_within_{e}": (a.abs_dlnm <= e).mean() for e in (0.05, 0.10, 0.20)}))
TL = pd.DataFrame(tol); TL.round(3).to_csv("tables/h1_tolerance_shares.csv", index=False)
if __name__ == "__main__":
    pd.set_option("display.width", 220); pd.set_option("display.max_colwidth", 40)
    print(RG.round(3).to_string()); print(); print(R[R.metric == "abs_dlnm"].round(4).to_string()); print(); print(TL.round(3).to_string())
