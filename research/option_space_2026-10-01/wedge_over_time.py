"""Objective 1 over time (8 Oct 2026, descriptive): the invisible wedge (transaction value minus revenue) by platform-year, in each platform's own
reporting unit, with its growth next to revenue growth. Issuer-reported pairs only (Tokopedia, Blibli 3P, Bukalapak); constructed or estimated
series (Grab Indonesia, Shopee) shown separately. No exchange-rate conversion: growth rates are within one currency.
Run: python3 wedge_over_time.py -> tables/wedge_over_time.csv"""
import numpy as np, pandas as pd
t = pd.read_csv("tables/take_rate_levels.csv")
keep = {"Tokopedia e-commerce segment": "issuer-reported", "Blibli 3P Retail": "issuer-reported", "Bukalapak Group": "issuer-reported",
        "Grab": "constructed (group ratio)", "Shopee": "estimated (third party, assumed take rate)"}
t = t[t.firm.isin(keep)].sort_values(["firm", "year"]).copy()
t["tier"] = t.firm.map(keep); t["W"] = t.transaction_value - t.revenue_value
for c, s in (("W", "wedge"), ("revenue_value", "revenue"), ("transaction_value", "tv")):
    t[f"g_{s}_pct"] = 100 * (t.groupby("firm")[c].pct_change())
t["wedge_share_of_tv_pct"] = 100 * t.W / t.transaction_value
out = t[["firm", "tier", "year", "transaction_value", "revenue_value", "W", "wedge_share_of_tv_pct", "g_tv_pct", "g_wedge_pct", "g_revenue_pct"]]
out.round(3).to_csv("tables/wedge_over_time.csv", index=False); print(out.round(1).to_string(index=False))
