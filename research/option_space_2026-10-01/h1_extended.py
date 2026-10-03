"""H1 with the bigger foreign comparison, plus an EXPLORATORY look at market income (3 Oct 2026).

Part A (H1, as promised in the proposal, bigger benchmark): does the platform's cut (m = R/V) move more in Indonesia than abroad?
  Indonesia = IDN_main (as examined) + regional tier (Grab and GoTo on-demand, verified); foreign = the proposal's 8 clean firms (EXT_clean)
  + the 29 new firms extracted for the spin-off (excluding firm-years where own-goods sales are over half of revenue).
  Metric: |change in log m| per year. Unit of inference: the firm (median per firm). One-sided Mann-Whitney and a firm-label permutation test.
Part B (EXPLORATORY, formed after seeing part of the data, so not evidence in the pre-registered sense): are cuts more volatile, and discounts
  larger relative to revenue, in emerging markets than in high-income markets, holding stage roughly fixed (years since listing)?
  Market group = the firm's main market (emerging: low and middle income; high: high income). Listing years are approximate, from public record.
Run from this folder: python3 h1_extended.py -> tables/h1_extended_firms.csv, tables/h1_extended_results.json"""
import json
import numpy as np, pandas as pd
from scipy import stats

rng = np.random.default_rng(20261003)
T = pd.read_csv("tables/transitions_master.csv")
P = pd.read_csv("tables/l_panel.csv")
S = pd.read_csv("tables/spinoff_panel.csv")

def trans(df, firm_col="firm"):
    df = df.sort_values([firm_col, "year"]).copy(); df["m"] = df.R / df.V
    df["dlnm"] = np.where(df.groupby(firm_col).year.diff() == 1, np.log(df.m) - np.log(df.groupby(firm_col).m.shift()), np.nan)
    return df.dropna(subset=["dlnm"])[[firm_col, "year", "dlnm"]].rename(columns={firm_col: "firm"})

idn = T[T.set == "IDN_main"].rename(columns={"y1": "year"})[["firm", "year", "dlnm"]].assign(group="Indonesia")
grab = P[P.firm == "Grab"].groupby("year")[["V", "R"]].sum().reset_index().assign(firm="Grab on-demand")
goto = P[(P.firm == "GoTo") & (P.seg == "On-demand")][["year", "V", "R"]].assign(firm="GoTo on-demand")
reg = trans(pd.concat([grab, goto])[lambda d: d.R > 0]).assign(group="Indonesia")
ext = T[T.set == "EXT_clean"].rename(columns={"y1": "year"})[["firm", "year", "dlnm"]].assign(group="Foreign (proposal 8)")
new = S[(S.flag_1p != "exclude") & S.g_m.notna()].rename(columns={"entity": "firm", "g_m": "dlnm"})[["firm", "year", "dlnm"]].assign(group="Foreign (new)")
allt = pd.concat([idn, reg, ext, new], ignore_index=True); allt["abs"] = allt.dlnm.abs()

firm = allt.groupby(["firm", "group"]).agg(median_abs=("abs", "median"), n=("abs", "size"), share_within_010=("abs", lambda x: (x <= 0.10).mean())).reset_index()

def compare(a, b, label):
    xa, xb = firm[firm.firm.isin(a)].median_abs.values, firm[firm.firm.isin(b)].median_abs.values
    obs = np.median(xa) - np.median(xb); pool = np.concatenate([xa, xb]); k = len(xa); hits = 0
    for _ in range(9999):
        rng.shuffle(pool); hits += (np.median(pool[:k]) - np.median(pool[k:])) >= obs
    return {"label": label, "firms_a": len(xa), "firms_b": len(xb), "median_a": float(np.median(xa)), "median_b": float(np.median(xb)),
            "mannwhitney_p": float(stats.mannwhitneyu(xa, xb, alternative="greater").pvalue), "permutation_p": (hits + 1) / 10000}

IDN = firm[firm.group == "Indonesia"].firm.tolist()
OLD = firm[firm.group == "Foreign (proposal 8)"].firm.tolist(); NEW = firm[firm.group == "Foreign (new)"].firm.tolist()
res = {"A_vs_proposal8": compare(IDN, OLD, "Indonesia+regional vs proposal's 8"),
       "A_vs_new": compare(IDN, NEW, "Indonesia+regional vs new foreign firms"),
       "A_vs_all_foreign": compare(IDN, OLD + NEW, "Indonesia+regional vs all foreign"),
       "share_within_010": allt.assign(w=allt["abs"] <= 0.10).groupby("group").w.mean().round(3).to_dict()}

# ---- Part B (exploratory) ----
EMERGING = {"Blibli 3P Retail", "Bukalapak Group", "Tokopedia e-commerce segment", "Grab on-demand", "GoTo on-demand", "Jumia", "Mercado Libre",
            "Sea / Shopee", "YTRA", "DESP", "KSPI", "HEPS", "MOGU", "BABA", "PDD", "Ozon", "TOUR", "TCOM", "UXIN"}
LISTED = {"eBay": 1998, "Etsy": 2015, "Jumia": 2019, "Mercado Libre": 2007, "Rakuten": 2000, "Sea / Shopee": 2017, "Shopify": 2015, "Zalando": 2014,
          "Blibli 3P Retail": 2022, "Bukalapak Group": 2021, "Tokopedia e-commerce segment": 2022, "Grab on-demand": 2021, "GoTo on-demand": 2022,
          "EXPE": 2005, "TCOM": 2003, "YTRA": 2016, "DESP": 2017, "TOUR": 2014, "VCSA": 2021, "FVRR": 2019, "UPWK": 2018, "SEAT": 2021, "RBA": 1998,
          "ACVA": 2021, "REAL": 2019, "DIBS": 2021, "KSPI": 2020, "HEPS": 2021, "MOGU": 2018, "BABA": 2014, "PDD": 2018, "GrubHub": 2014,
          "ASAPQ": 2018, "Ozon": 2020, "LQDT": 2006, "UXIN": 2018, "Jumei": 2014, "VIPS": 2012, "JD": 2014, "DDL": 2021, "NEGG": 2021}
allt["market"] = np.where(allt.firm.isin(EMERGING), "emerging", "high-income")
allt["years_listed"] = allt.year - allt.firm.map(LISTED)
allt["stage"] = np.where(allt.years_listed <= 5, "young (<=5y listed)", "older")
fb = allt.groupby(["firm", "market", "stage"])["abs"].median().reset_index()
B = {}
for st in ("young (<=5y listed)", "older", "all"):
    q = fb if st == "all" else fb[fb.stage == st]
    e, h = q[q.market == "emerging"]["abs"], q[q.market == "high-income"]["abs"]
    if len(e) >= 3 and len(h) >= 3:
        B[st] = {"firm_stage_cells_emerging": len(e), "high": len(h), "median_emerging": float(e.median()), "median_high": float(h.median()),
                 "mannwhitney_p": float(stats.mannwhitneyu(e, h, alternative="greater").pvalue)}
# robustness: the same without the Indonesian and regional firms (is it only Indonesia?)
fbx = allt[~allt.firm.isin(IDN)].groupby(["firm", "market", "stage"])["abs"].median().reset_index()
for st in ("young (<=5y listed)", "older"):
    q = fbx[fbx.stage == st]; e, h = q[q.market == "emerging"]["abs"], q[q.market == "high-income"]["abs"]
    B[st + " ex-Indonesia"] = {"emerging": len(e), "high": len(h), "median_emerging": float(e.median()), "median_high": float(h.median()),
                               "mannwhitney_p": float(stats.mannwhitneyu(e, h, alternative="greater").pvalue)}
# discount size relative to revenue kept (L), where disclosed
LM = {"Grab": "emerging", "GoTo": "emerging", "Tokopedia": "emerging", "MakeMyTrip": "emerging", "Blibli": "emerging", "Shopee": "emerging",
      "GoTo Group": "emerging", "Meituan": "emerging", "DoorDash": "high-income", "Lyft": "high-income", "Talabat": "high-income", "Delivery Hero": "mixed"}
Lf = P.dropna(subset=["L"]).assign(market=lambda d: d.firm.map(LM)).groupby(["firm", "market"]).L.median().reset_index()
B["discount_to_revenue_L_firm_medians"] = Lf.round(3).to_dict("records")
res["B_exploratory_market_income"] = B
firm.round(4).to_csv("tables/h1_extended_firms.csv", index=False)
json.dump(res, open("tables/h1_extended_results.json", "w"), indent=1)
print(json.dumps(res, indent=1))
