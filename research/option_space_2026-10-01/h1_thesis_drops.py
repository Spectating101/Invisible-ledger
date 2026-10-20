"""Two checks added for the thesis (13 Oct 2026, exploratory; formed after the main H1 result, in answer to the second audit).
Does the 5-against-27 test survive without Ozon (its only pair starts in a year where own goods exceed half of revenue) and without Zalando
(a retailer that also sells goods itself)? Same statistic as h1_extended.py: one median size of yearly change in log take rate per platform,
one-sided Mann-Whitney and a 9,999-label shuffle of platform medians.
Run from this folder: python3 h1_thesis_drops.py -> tables/h1_thesis_drops.json"""
import json
import numpy as np, pandas as pd
from scipy import stats

rng = np.random.default_rng(20261013)
f = pd.read_csv("tables/h1_extended_firms.csv")
idn = f[f.group == "Indonesia"].median_abs.values
out = {}
for label, drop in [("all 27", []), ("without Ozon", ["Ozon"]), ("without Zalando", ["Zalando"]), ("without Ozon and Zalando", ["Ozon", "Zalando"])]:
    fo = f[(f.group != "Indonesia") & (~f.firm.isin(drop))].median_abs.values
    obs = np.median(idn) - np.median(fo); pool = np.concatenate([idn, fo]); hits = 0
    for _ in range(9999):
        rng.shuffle(pool); hits += (np.median(pool[:5]) - np.median(pool[5:])) >= obs
    out[label] = {"foreign_platforms": len(fo), "median_indonesia": round(float(np.median(idn)), 4), "median_foreign": round(float(np.median(fo)), 4),
                  "mannwhitney_p": round(float(stats.mannwhitneyu(idn, fo, alternative="greater").pvalue), 4), "shuffle_p": round((hits + 1) / 10000, 4)}
json.dump(out, open("tables/h1_thesis_drops.json", "w"), indent=1)
print(json.dumps(out, indent=1))
