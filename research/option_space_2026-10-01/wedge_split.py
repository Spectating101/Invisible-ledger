"""Divide each change in the wedge W = V - R into a volume part and a monetization part (proposal section 8; 7 Oct 2026; descriptive).
ln W = ln V + ln(1 - m), so  d ln W = d ln V [volume]  +  d ln(1 - m) [monetization].   Revenue, for contrast: d ln R = d ln V + d ln m.
The same change in m is large for revenue (m is small) and small for the wedge (1 - m is near one).
Inputs: tables/transitions_master.csv (main sample and clean benchmark). Run: python3 wedge_split.py -> tables/wedge_split.csv, tables/wedge_split_summary.json"""
import json
import numpy as np, pandas as pd

T = pd.read_csv("tables/transitions_master.csv")
T = T[T.set.isin(["IDN_main", "EXT_clean"])].copy()
m0, m1 = T.m0_pct / 100, T.m1_pct / 100
T["dlnV"] = np.log(1 + T.gV / 100); T["dlnR"] = np.log(1 + T.gR / 100)
T["dlnW_volume"] = T.dlnV; T["dlnW_monetization"] = np.log((1 - m1) / (1 - m0)); T["dlnW"] = T.dlnW_volume + T.dlnW_monetization
T["dlnR_monetization"] = np.log(m1 / m0)
T["mon_share_W"] = T.dlnW_monetization.abs() / (T.dlnW_volume.abs() + T.dlnW_monetization.abs())
T["mon_share_R"] = T.dlnR_monetization.abs() / (T.dlnV.abs() + T.dlnR_monetization.abs())
cols = ["set", "firm", "y0", "y1", "m0_pct", "m1_pct", "dlnV", "dlnW_monetization", "dlnW", "dlnR", "dlnR_monetization", "mon_share_W", "mon_share_R"]
T[cols].round(4).to_csv("tables/wedge_split.csv", index=False)
S = {s: {"comparisons": int(len(d)), "median_monetization_share_of_W_change": float(d.mon_share_W.median()),
         "median_monetization_share_of_R_change": float(d.mon_share_R.median()), "max_abs_dlnW_monetization": float(d.dlnW_monetization.abs().max())}
     for s, d in T.groupby("set")}
json.dump(S, open("tables/wedge_split_summary.json", "w"), indent=1)
print(T[T.set == "IDN_main"][cols].round(3).to_string(index=False)); print(json.dumps(S, indent=1))
