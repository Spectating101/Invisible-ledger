"""Shopee quarterly take rate (marketplace revenue / GMV) from Sea earnings releases (quote-verified extraction).
Unit fix: releases up to 2020Q2 print revenue in US$ thousands although the extraction tags them USD_m; values above 50,000 in a
revenue field are therefore divided by 1,000. GMV is in US$ bn. 2023Q1 and 2023Q2 releases were not available."""
import numpy as np, pandas as pd
d = pd.read_csv("tables/src/shopee_quarterly_extraction.csv")
d = d[d.value.notna() & (d.field != "note_text")].copy()
d["x"] = np.where(d.unit.str.contains("_bn"), d.value * 1000, d.value)
rev = d.field.isin(["gaap_revenue", "marketplace_revenue", "product_revenue"])
d.loc[rev & (d.x > 50000), "x"] /= 1000
w = d.pivot_table(index="period", columns="field", values="x", aggfunc="first").sort_index()
w["mkt_take_pct"] = 100 * w.marketplace_revenue / w.gmv
w["gaap_take_pct"] = 100 * w.gaap_revenue / w.gmv
w["dln_mkt_take"] = np.log(w.mkt_take_pct).diff()
w.round(3).to_csv("tables/shopee_quarterly_take_rate.csv")
if __name__ == "__main__":
    pd.set_option("display.width", 200)
    print(w[["gmv", "marketplace_revenue", "mkt_take_pct", "dln_mkt_take"]].round(3).to_string())
    print("\nlargest quarterly |dln| :", w.dln_mkt_take.abs().nlargest(3).round(3).to_dict())
    print("median |dln| per quarter :", round(w.dln_mkt_take.abs().median(), 3))
