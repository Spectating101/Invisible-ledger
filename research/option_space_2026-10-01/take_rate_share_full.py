"""Take-rate share of revenue moves and of wedge moves, for the thesis groups (5 Indonesian and regional platforms,
27 foreign platforms), with the definitions of wedge_split.py: in logs, revenue growth = volume + take rate, and
wedge growth = volume + change in ln(1 - m). The take-rate share of a move is |take-rate term| / (|volume| + |take-rate term|).
Same inputs and pair rules as h1_extended.py and h1_direction_count.py. Run from this folder:
python3 take_rate_share_full.py "$PWD"  -> tables/take_rate_share_full.json"""
import sys, json, numpy as np, pandas as pd
base = sys.argv[1]
T = pd.read_csv(base + "/tables/transitions_master.csv"); P = pd.read_csv(base + "/tables/l_panel.csv"); S = pd.read_csv(base + "/tables/spinoff_panel.csv")

def pairs(df):
    df = df.sort_values(["firm", "year"]).copy(); df["m"] = df.R / df.V
    ok = df.groupby("firm").year.diff() == 1
    df["dlnV"] = np.where(ok, np.log(df.V) - np.log(df.groupby("firm").V.shift()), np.nan)
    df["dlnm"] = np.where(ok, np.log(df.m) - np.log(df.groupby("firm").m.shift()), np.nan)
    df["m0"] = df.groupby("firm").m.shift()
    return df.dropna(subset=["dlnm"])

idn = T[T.set == "IDN_main"].assign(dlnV=lambda d: d.lnV, m0=lambda d: d.m0_pct / 100, m=lambda d: d.m1_pct / 100)[["firm", "dlnV", "dlnm", "m0", "m"]]
grab = P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab on-demand")
goto = P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo on-demand")
reg = pairs(pd.concat([grab, goto])[lambda d: d.R > 0])[["firm", "dlnV", "dlnm", "m0", "m"]]
ext = T[T.set == "EXT_clean"].assign(dlnV=lambda d: d.lnV, m0=lambda d: d.m0_pct / 100, m=lambda d: d.m1_pct / 100)[["firm", "dlnV", "dlnm", "m0", "m"]]
s = S.rename(columns={"entity": "firm"}).sort_values(["firm", "year"])
s["m0"] = s.groupby("firm").m.shift()  # previous year's take rate, taken before any row is filtered out
s = s[(s.flag_1p != "exclude") & s.g_m.notna() & s.g_V.notna()]
new = s.rename(columns={"g_V": "dlnV", "g_m": "dlnm"})[["firm", "dlnV", "dlnm", "m0", "m"]].dropna(subset=["m0"])

def shares(d):
    d = d.copy()
    d["share_R"] = d.dlnm.abs() / (d.dlnV.abs() + d.dlnm.abs())
    dw = np.log(1 - d.m) - np.log(1 - d.m0)
    d["share_W"] = dw.abs() / (d.dlnV.abs() + dw.abs())
    return d

groups = {"Indonesian and regional": shares(pd.concat([idn, reg])), "Foreign": shares(pd.concat([ext, new]))}
out = {}
for k, d in groups.items():
    firm = d.groupby("firm")[["share_R", "share_W"]].median()
    out[k] = {"pairs": int(len(d)), "platforms": int(d.firm.nunique()),
              "median_take_rate_share_of_revenue_move_pairs": round(float(d.share_R.median()), 3),
              "median_take_rate_share_of_revenue_move_platforms": round(float(firm.share_R.median()), 3),
              "median_take_rate_share_of_wedge_move_pairs": round(float(d.share_W.median()), 3)}
json.dump(out, open(base + "/tables/take_rate_share_full.json", "w"), indent=1)
print(json.dumps(out, indent=1))
