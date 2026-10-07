"""H1 with quarterly pairs (PREREGISTRATION.md addendum Q1, 7 Oct 2026; robustness, specified after the annual result).
Year-over-year |change in log m| (same quarter one year earlier); one median per firm; one-sided Mann-Whitney and a firm-label permutation.
Inputs: committed quarterly tables (grab_quarterly_verified, goto_ondemand_quarterly_net, blibli_3p_quarterly, shopee_quarterly_take_rate, peers_quarterly).
Run: python3 h1_quarterly.py -> tables/h1_quarterly_firms.csv, tables/h1_quarterly_results.json"""
import json
import numpy as np, pandas as pd
from scipy import stats

T = "tables/"
def q_index(q): return int(q[:4]) * 4 + int(q[-1]) - 1

def yoy(df, firm, ttm=False):
    d = df[["quarter", "V", "R"]].dropna().copy(); d = d[(d.V > 0) & (d.R > 0)]
    d["qi"] = d.quarter.map(q_index); d = d.sort_values("qi").set_index("qi")
    if ttm:   # trailing four quarters, only where all four are present
        full = d.index.to_series().rolling(4).apply(lambda s: s.iloc[-1] - s.iloc[0] == 3, raw=False) == 1
        d[["V", "R"]] = d[["V", "R"]].rolling(4).sum(); d = d[full]
    m = np.log(d.R / d.V); prev = m.reindex(m.index - 4).values
    out = pd.DataFrame({"firm": firm, "quarter": d.quarter.values, "abs_dlnm": np.abs(m.values - prev)}).dropna()
    return out

g = pd.read_csv(T + "grab_quarterly_verified.csv", index_col=0).rename_axis("quarter").reset_index().rename(columns={"od_gmv": "V", "od_rev": "R"})
go = pd.read_csv(T + "goto_ondemand_quarterly_net.csv", index_col=0).rename_axis("quarter").reset_index().rename(columns={"gtv": "V", "net": "R"})
bl = pd.read_csv(T + "blibli_3p_quarterly.csv").rename(columns={"period": "quarter", "tpv": "V", "net_revenue": "R"})
se = pd.read_csv(T + "shopee_quarterly_take_rate.csv").rename(columns={"period": "quarter", "gmv": "V", "marketplace_revenue": "R"})
pq = pd.read_csv(T + "peers_quarterly.csv"); pq = pq[pq.status != "FAIL"]
pq = pq[~((pq.firm == "DASH") & (pq.quarter.map(q_index) >= q_index("2025Q4")))]

rows = [yoy(g, "Grab on-demand"), yoy(go, "GoTo on-demand"), yoy(bl, "Blibli 3P"), yoy(se, "Sea / Shopee")]
rows += [yoy(pq[pq.firm == f], f, ttm=f in ("ABNB", "BKNG")) for f in sorted(pq.firm.unique())]
A = pd.concat(rows, ignore_index=True)
IDN = ["Grab on-demand", "GoTo on-demand", "Blibli 3P"]
A["group"] = np.where(A.firm.isin(IDN), "Indonesia and region", "Benchmark")
F = A.groupby(["firm", "group"]).abs_dlnm.agg(median_abs="median", pairs="size").reset_index()
a, b = F[F.group != "Benchmark"].median_abs.values, F[F.group == "Benchmark"].median_abs.values
rng = np.random.default_rng(20261007); pool = np.concatenate([a, b]); obs = np.median(a) - np.median(b); hits = 0
for _ in range(9999):
    rng.shuffle(pool); hits += (np.median(pool[:len(a)]) - np.median(pool[len(a):])) >= obs
mw = float(stats.mannwhitneyu(a, b, alternative="greater").pvalue)
res = {"firms": [len(a), len(b)], "median_indonesia_region": float(np.median(a)), "median_benchmark": float(np.median(b)),
       "mannwhitney_p": mw, "permutation_p": (hits + 1) / 10000, "Q1_holds": bool(np.median(a) > np.median(b) and mw < 0.05),
       "pairs_by_firm": F.set_index("firm").pairs.to_dict()}
F.round(4).to_csv(T + "h1_quarterly_firms.csv", index=False); json.dump(res, open(T + "h1_quarterly_results.json", "w"), indent=1)
print(F.round(4).to_string(index=False)); print(json.dumps(res, indent=1))
