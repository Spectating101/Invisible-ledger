"""EXPLORATORY (8 Oct 2026; data already seen): is the take rate less stable in the first years after a platform lists on an exchange?
The Indonesian and regional platforms all listed in 2021-22 and repriced in 2022-24. This checks the same idea on the foreign firms:
for each firm with transitions both within 3 years of listing and later, compare its median |change in log take rate| in the two windows (paired).
Listing years as in h1_extended.py (approximate, from public record). Also reports years from listing to each Indonesian platform's largest move.
Run: python3 listing_check.py -> tables/listing_check.json"""
import json
import numpy as np, pandas as pd
from scipy import stats

T = pd.read_csv("tables/transitions_master.csv"); P = pd.read_csv("tables/l_panel.csv"); S = pd.read_csv("tables/spinoff_panel.csv")
LISTED = {"eBay": 1998, "Etsy": 2015, "Jumia": 2019, "Mercado Libre": 2007, "Rakuten": 2000, "Sea / Shopee": 2017, "Shopify": 2015, "Zalando": 2014,
          "Blibli 3P Retail": 2022, "Bukalapak Group": 2021, "Tokopedia e-commerce segment": 2022, "Grab on-demand": 2021, "GoTo on-demand": 2022,
          "EXPE": 2005, "TCOM": 2003, "YTRA": 2016, "DESP": 2017, "TOUR": 2014, "VCSA": 2021, "FVRR": 2019, "UPWK": 2018, "SEAT": 2021, "RBA": 1998,
          "ACVA": 2021, "REAL": 2019, "DIBS": 2021, "KSPI": 2020, "HEPS": 2021, "MOGU": 2018, "BABA": 2014, "PDD": 2018, "GrubHub": 2014,
          "ASAPQ": 2018, "Ozon": 2020, "LQDT": 2006, "UXIN": 2018, "Jumei": 2014, "VIPS": 2012, "JD": 2014, "DDL": 2021, "NEGG": 2021}

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
A = pd.concat([idn, reg, ext, new], ignore_index=True); A["abs"] = A.dlnm.abs(); A["since_listing"] = A.year - A.firm.map(LISTED)
A = A.dropna(subset=["since_listing"])
A["window"] = np.where(A.since_listing <= 3, "within 3 years", "later")
f = A[~A.firm.isin(IDN)].groupby(["firm", "window"])["abs"].median().unstack().dropna()
out = {"foreign_firms_with_both_windows": int(len(f)), "median_within_3_years": float(f["within 3 years"].median()),
       "median_later": float(f["later"].median()), "firms_larger_within_3_years": int((f["within 3 years"] > f["later"]).sum()),
       "wilcoxon_one_sided_p": float(stats.wilcoxon(f["within 3 years"], f["later"], alternative="greater").pvalue),
       "firms": {k: [round(float(v["within 3 years"]), 3), round(float(v["later"]), 3)] for k, v in f.iterrows()}}
big = A[A.firm.isin(IDN)].sort_values("abs").groupby("firm").tail(1)
out["indonesia_largest_move"] = {r.firm: {"year": int(r.year), "years_after_listing": int(r.since_listing), "abs_dlnm": round(float(r.abs), 3)} for r in big.itertuples()}
s = json.dumps(out, indent=1); print(s); open("tables/listing_check.json", "w").write(s)
