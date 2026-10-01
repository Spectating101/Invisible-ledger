"""Split each platform's revenue growth into a volume effect and a take-rate effect (1 Oct 2026, exploratory).

ln R = ln V + ln m, so growth in revenue = growth in transaction value + change in the take rate m = R / V.
'take-rate share' = change in ln m / change in ln R. It can exceed 100% when transaction value fell.
Inputs are committed repo CSVs. Scope caveats are in the notes column. Not yet source-verified against filings.

Run: PYTHONPATH=/home/phyrexian/.local/lib/python3.13/site-packages python3 repricing_split.py
"""
import pathlib

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parent / "tables"
OUT.mkdir(exist_ok=True)
A = pd.read_csv(ROOT / "data/longitudinal/annual_extension_panel_preliminary.csv")
L = pd.read_csv(ROOT / "outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_levels.csv")
rows = []


def add(name, window, v0, r0, v1, r1, note=""):
    lv, lr = np.log(v1 / v0), np.log(r1 / r0)
    rows.append(dict(platform=name, window=window, V_growth_pct=100 * (v1 / v0 - 1), R_growth_pct=100 * (r1 / r0 - 1),
                     m_start_pct=100 * r0 / v0, m_end_pct=100 * r1 / v1,
                     take_rate_share_of_revenue_growth_pct=100 * (lr - lv) / lr, notes=note))


g = A[A.platform == "Grab"].set_index("year")
for w in ((2022, 2023), (2023, 2025), (2022, 2025)):
    add("Grab (group on-demand)", f"{w[0]}-{w[1]}", g.gmv_or_gtv[w[0]], g.matched_revenue[w[0]], g.gmv_or_gtv[w[1]], g.matched_revenue[w[1]],
        "group scope, not Indonesia-only; 2022-23 on company restatement, 2024-25 on summed quarters")
t = A[(A.platform == "GoTo") & (~A.basis.str.contains("pro-forma"))].set_index("year")
for w in ((2022, 2023), (2022, 2025)):
    add("GoTo (group)", f"{w[0]}-{w[1]}", t.gmv_or_gtv[w[0]], t.matched_revenue[w[0]], t.gmv_or_gtv[w[1]], t.matched_revenue[w[1]],
        "group scope incl. fintech; Tokopedia deconsolidated in 2024 (structural break)")
s = A[A.platform == "Sea"].set_index("year")
add("Sea / Shopee (global)", "2022-2025", s.gmv_or_gtv[2022], s.matched_revenue[2022], s.gmv_or_gtv[2025], s.matched_revenue[2025], "global Shopee, not Indonesia")
for ser, note in (("Tokopedia e-commerce segment", "Indonesia-aligned segment"),
                  ("Blibli 3P Retail", "includes online travel; 2022 may reflect a definition change"),
                  ("Bukalapak Group", "group scope incl. overseas")):
    d = L[L.series == ser].set_index("year").sort_index()
    y0, y1 = d.index.min(), d.index.max()
    add(ser, f"{y0}-{y1}", d.transaction_value[y0], d.revenue_value[y0], d.transaction_value[y1], d.revenue_value[y1], note)
    if ser.startswith("Blibli"):
        add(ser, "2023-2025", d.transaction_value[2023], d.revenue_value[2023], d.transaction_value[2025], d.revenue_value[2025], note)
out = pd.DataFrame(rows).round(2)
out.to_csv(OUT / "repricing_split.csv", index=False)
print(out.drop(columns="notes").to_string(index=False))
bps_share = 100 * 203.58 / 1288.93
print(f"\nBPS 2024: marketplace category = {bps_share:.1f}% of e-commerce value; outside = {100 - bps_share:.1f}%")
