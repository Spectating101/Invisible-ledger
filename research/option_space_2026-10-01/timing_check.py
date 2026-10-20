"""EXPLORATORY (8 Oct 2026; the data were already seen, so this is not evidence in the pre-registered sense).
Were take-rate swings concentrated in 2022-23 (and, as a second window, 2022-24, since GoTo's incentive cut came in 2024) (the end of cheap funding) for platforms in lower-income markets abroad too, or only in Indonesia?
Unit: the firm. For each firm with transitions both in 2022-23 and in other years, compare the median |change in log take rate| in
transitions ending in 2022 or 2023 with its median in other years (paired, within firm). Groups as in h1_extended.py: Indonesia and region;
foreign platforms whose main market is lower or middle income ("emerging"); foreign platforms in high-income markets.
Run: python3 timing_check.py -> tables/timing_check.json"""
import json
import numpy as np, pandas as pd
from scipy import stats

T = pd.read_csv("tables/transitions_master.csv"); P = pd.read_csv("tables/l_panel.csv"); S = pd.read_csv("tables/spinoff_panel.csv")

def trans(df):
    df = df.sort_values(["firm", "year"]).copy(); df["m"] = df.R / df.V
    df["dlnm"] = np.where(df.groupby("firm").year.diff() == 1, np.log(df.m) - np.log(df.groupby("firm").m.shift()), np.nan)
    return df.dropna(subset=["dlnm"])[["firm", "year", "dlnm"]]

idn = T[T.set == "IDN_main"].rename(columns={"y1": "year"})[["firm", "year", "dlnm"]]
grab = P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab on-demand")
goto = P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo on-demand")
reg = trans(pd.concat([grab, goto])[lambda d: d.R > 0])
ext = T[T.set == "EXT_clean"].rename(columns={"y1": "year"})[["firm", "year", "dlnm"]]
new = S[(S.flag_1p != "exclude") & S.g_m.notna()].rename(columns={"entity": "firm", "g_m": "dlnm"})[["firm", "year", "dlnm"]]
IDN = set(idn.firm) | set(reg.firm)
EMERGING = {"Jumia", "Mercado Libre", "Sea / Shopee", "YTRA", "DESP", "KSPI", "HEPS", "MOGU", "BABA", "PDD", "Ozon", "TOUR", "TCOM", "UXIN"}
A = pd.concat([idn, reg, ext, new], ignore_index=True); A["abs"] = A.dlnm.abs()
A["group"] = np.where(A.firm.isin(IDN), "Indonesia and region", np.where(A.firm.isin(EMERGING), "Foreign, lower-income markets", "Foreign, high-income markets"))
out = {}
for wname, yrs in (("2022-23", [2022, 2023]), ("2022-24", [2022, 2023, 2024])):
  A["window"] = np.where(A.year.isin(yrs), "2022-23", "other years")
  out[wname] = {}
  for grp, d in A.groupby("group"):
    f = d.groupby(["firm", "window"])["abs"].median().unstack()
    f = f.dropna()
    diff = f["2022-23"] - f["other years"]
    res = {"firms_with_both": int(len(f)), "median_in_window": float(f["2022-23"].median()), "median_other_years": float(f["other years"].median()),
           "firms_larger_in_window": int((diff > 0).sum())}
    if len(f) >= 5:
        res["wilcoxon_one_sided_p"] = float(stats.wilcoxon(f["2022-23"], f["other years"], alternative="greater").pvalue)
    res["firms"] = {k: [round(float(v["2022-23"]), 3), round(float(v["other years"]), 3)] for k, v in f.iterrows()}
    out[wname][grp] = res
s = json.dumps(out, indent=1); print(s); open("tables/timing_check.json", "w").write(s)
