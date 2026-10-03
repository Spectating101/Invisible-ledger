"""'Both cannot be true', done systematically for Indonesia's online economy (3 Oct 2026).
Same logic as LPEM FEB UI's check on BPS manufacturing vs electricity (quoted in public debate on the Q1 2026 GDP figure), applied to every
ruler of the online economy: yearly growth of each ruler, then for each pair whether they agree in direction and how far apart they are.
Inputs: tables/src/digital_rulers_annual.csv (sources and verification status per row) + official household consumption (BPS via OECD).
Some rulers count adjacent things (parcels are regional; QRIS is mostly in-person payment; PMSE VAT is foreign digital services); the
'what_it_counts' column says so. Growth only, in each ruler's own unit; no levels are compared across rulers.
Run: python3 consistency_grid.py -> tables/consistency_grid_growth.csv, tables/consistency_grid_pairs.csv"""
import itertools
import numpy as np, pandas as pd
d = pd.read_csv("tables/src/digital_rulers_annual.csv")
o = pd.read_csv("tables/src/oecd_qna_idn_2021_2026.csv")
o = o[(o.SECTOR == "S1M") & (o.TRANSACTION == "P3") & (o.ADJUSTMENT == "N") & (o.UNIT_MEASURE == "XDC") & (o.TRANSFORMATION == "N") & (o.PRICE_BASE == "V")]
o["year"] = o.TIME_PERIOD.str[:4].astype(int)
hc = o.groupby("year").OBS_VALUE.agg(["sum", "size"]); hc = hc[hc["size"] == 4]["sum"] / 1e6
d = pd.concat([d, pd.DataFrame({"ruler": "Official household spending (nominal)", "year": hc.index, "value": hc.values,
                                "what_it_counts": "BPS national accounts, households + NPISH"})], ignore_index=True)
w = d.pivot_table(index="year", columns="ruler", values="value")
g = (100 * (w / w.shift() - 1)).loc[2023:].round(1)
g.T.to_csv("tables/consistency_grid_growth.csv")
rows = []
for y in g.index:
    for a, b in itertools.combinations(g.columns, 2):
        x1, x2 = g.loc[y, a], g.loc[y, b]
        if np.isfinite(x1) and np.isfinite(x2):
            rows.append({"year": y, "ruler_a": a, "ruler_b": b, "growth_a": x1, "growth_b": x2,
                         "same_direction": bool(np.sign(x1) == np.sign(x2)), "gap_pts": round(abs(x1 - x2), 1)})
p = pd.DataFrame(rows); p.to_csv("tables/consistency_grid_pairs.csv", index=False)
pd.set_option("display.width", 220)
print(g.T.to_string())
print("\nPairs moving in opposite directions:"); print(p[~p.same_direction].to_string(index=False))
print("\nPairs more than 20 points apart:", int((p.gap_pts > 20).sum()), "of", len(p))
