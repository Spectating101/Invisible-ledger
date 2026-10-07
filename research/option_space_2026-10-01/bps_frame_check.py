"""EXPLORATORY (7 Oct 2026, designed after the E5 result): does BPS's 2022->2023 growth in the e-commerce business count follow real entry,
or the survey's sample design? BPS estimates the count by listing businesses in sampled census blocks (method note, Statistik E-Commerce),
so a change in the sampled places can move the count. The files identify provinces only. Province totals compared across the two files.
Licensed inputs are not committed; output is province-free summary statistics only.
Run: python3 bps_frame_check.py --f2023 B.dbf --f2024 C.dbf -> tables/bps_frame_check.json"""
import argparse, json
import numpy as np, pandas as pd
from scipy import stats
from bps_microdata_tests import read_dbf, num

a_ = argparse.ArgumentParser(); a_.add_argument("--f2023"); a_.add_argument("--f2024"); x = a_.parse_args()
a, b = read_dbf(x.f2023), read_dbf(x.f2024)
A = pd.DataFrame({"prov": a["prov"], "w": num(a["w_usaha_fi"])})
B = pd.DataFrame({"prov": b["prov"], "w": num(b["w_final"]), "start": num(b["r307"])})
ga = A.groupby("prov").agg(n0=("w", "size"), N0=("w", "sum"))
gb = B.groupby("prov").agg(n1=("w", "size"), N1=("w", "sum"))
gb["entrant_share"] = B.assign(e=B.w * (B.start == 2023)).groupby("prov").e.sum() / gb.N1
c = ga.join(gb, how="inner")
c["count_growth"] = c.N1 / c.N0 - 1; c["sample_growth"] = c.n1 / c.n0 - 1; c["max_from_entry"] = c.entrant_share / (1 - c.entrant_share)
beyond = c.count_growth > c.max_from_entry
r1, r2 = stats.spearmanr(c.count_growth, c.entrant_share), stats.spearmanr(c.count_growth, c.sample_growth)
out = {"provinces_compared": int(len(c)), "provinces_only_in_one_file": int(len(ga.index.symmetric_difference(gb.index))),
       "sample_rows_growth_pct": 100 * (len(B) / len(A) - 1),
       "count_growth_pct_range_across_provinces": [float(100 * c.count_growth.min()), float(100 * c.count_growth.max())],
       "spearman_count_growth_vs_entrant_share": [float(r1.statistic), float(r1.pvalue)],
       "spearman_count_growth_vs_sample_growth": [float(r2.statistic), float(r2.pvalue)],
       "provinces_growing_beyond_entry": int(beyond.sum()),
       "share_of_count_increase_from_those_provinces_pct": float(100 * (c.N1 - c.N0)[beyond].sum() / (c.N1 - c.N0).sum())}
s = json.dumps(out, indent=1); print(s); open("tables/bps_frame_check.json", "w").write(s)
