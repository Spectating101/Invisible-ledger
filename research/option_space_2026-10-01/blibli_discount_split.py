"""Blibli 3P Retail (marketplace + tiket.com): net revenue take rate vs Blibli's own before-discount take rate, quarterly.
GPBD = gross profit from direct sales after ADDING BACK discounts and subsidies (company definition, every release).
Proxy only: GPBD - net revenue = discounts and subsidies plus direct costs of 3P revenue. Source: tables/src/blibli_extraction.csv (quote-verified).
Writes tables/blibli_3p_quarterly.csv; prints the 4Q22 -> 1Q23 split of the rise in net take rate."""
import numpy as np, pandas as pd
d = pd.read_csv("tables/src/blibli_extraction.csv")
d = d[d.value.notna() & (d.field != "note_text") & (d.entity == "3P Retail") & (d.unit == "IDR_bn") & d.period.str.match(r"^20\d\dQ\d$")]
order = ["fy2022", "q12023", "q32023", "fy2023", "q22024", "q32024", "fy2024", "q12025", "q22025", "fy2025"]
d = d.assign(v=d.source_file.str.extract(r"blibli_(\w+?)(?:_linked_0)?\.txt")[0].map({k: i for i, k in enumerate(order)}))
w = d.sort_values("v").groupby(["period", "field"]).value.last().unstack()[["tpv", "net_revenue", "gpbd"]]
w["m_pct"] = 100 * w.net_revenue / w.tpv
w["gpbd_take_pct"] = 100 * w.gpbd / w.tpv
w["discount_proxy_over_net"] = (w.gpbd - w.net_revenue) / w.net_revenue
w.round(3).to_csv("tables/blibli_3p_quarterly.csv")
a, b = w.loc["2022Q4"], w.loc["2023Q1"]
dm = b.m_pct - a.m_pct; dg = b.gpbd_take_pct - a.gpbd_take_pct
print(w.round(2).to_string())
print(f"\n4Q22 -> 1Q23: net take {a.m_pct:.2f}% -> {b.m_pct:.2f}% (+{dm:.2f}pp); before-discount take {a.gpbd_take_pct:.2f}% -> {b.gpbd_take_pct:.2f}% (+{dg:.2f}pp)")
print(f"share of the rise from lower discounts and costs (proxy) = {(dm-dg)/dm:.0%}; from the before-discount rate = {dg/dm:.0%}")
print(f"net revenue x{b.net_revenue/a.net_revenue:.1f}, GPBD x{b.gpbd/a.gpbd:.2f}, TPV x{b.tpv/a.tpv:.2f}")
