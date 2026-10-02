"""EXPLORATORY angle 4 (2 Oct 2026): which scaling is steadier across platforms, market value / transaction value or market value / revenue?
V, R: annual sums of VERIFIED quarterly pairs (tables/peers_quarterly.csv; only full 4-quarter years), plus Delivery Hero (annual, EUR m) and Grab/GoTo are excluded
(group market cap includes financial services; segment V,R do not match it).  Market cap (USD, year-end, LSEG, licensed, NOT committed): mcap_annual.csv.
Because currency and scope differ, V and R are used in USD only for US-dollar reporters (UBER LYFT DASH ABNB BKNG ETSY EBAY) so no FX is needed.
Statistic: cross-sectional sd of log(mcap/V) vs log(mcap/R) per year; and R2 of log mcap on log V vs on log R.  n is 6-7 firms per year: DESCRIPTIVE only."""
import sys, numpy as np, pandas as pd
M = pd.read_csv(sys.argv[1]); M["year"] = pd.to_datetime(M.Date).dt.year; M = M.rename(columns={"Company Market Cap": "mcap"})[["ric", "year", "mcap"]]
rmap = {"UBER.N": "UBER", "LYFT.OQ": "LYFT", "DASH.O": "DASH", "ABNB.O": "ABNB", "BKNG.O": "BKNG", "ETSY.O": "ETSY", "EBAY.O": "EBAY"}
M["firm"] = M.ric.map(rmap); M = M.dropna(subset=["firm", "mcap"])
Q = pd.read_csv("tables/peers_quarterly.csv"); Q["year"] = Q.quarter.str[:4].astype(int)
A = Q.groupby(["firm", "year"]).agg(V=("V", "sum"), R=("R", "sum"), n=("quarter", "count")).reset_index(); A = A[A.n == 4]
D = A.merge(M, on=["firm", "year"]); D["mV"] = D.mcap / 1e6 / D.V; D["mR"] = D.mcap / 1e6 / D.R   # V,R in USD m
rows = []
for y, g in D.groupby("year"):
    if len(g) < 5: continue
    sV, sR = np.log(g.mV).std(), np.log(g.mR).std()
    r2 = lambda x: np.corrcoef(np.log(g.mcap), np.log(x))[0, 1] ** 2
    rows.append(dict(year=y, n=len(g), sd_log_mcap_over_V=sV, sd_log_mcap_over_R=sR, R2_mcap_on_V=r2(g.V), R2_mcap_on_R=r2(g.R)))
T = pd.DataFrame(rows); T.round(3).to_csv("tables/multiples_dispersion.csv", index=False); print(T.round(3).to_string())
print("\nfirms by year:", D.groupby("year").firm.apply(lambda s: ",".join(sorted(s))).to_dict())
