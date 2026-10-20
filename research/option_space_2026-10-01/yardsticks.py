"""Two state agencies, one economy: BI vs BPS e-commerce value, Rp trillion (3 Oct 2026).
BI: 2022 Rp476.3tn (LPI 2022, verified in tables/src/indo_policy_extraction.csv), 2023 Rp453.75tn (BI press conference 17 Jan 2024,
news), 2024 Rp487.01tn (+7.3%; Kontan data infographic; about Rp487tn in BI 2025 UMKM story, verified). BI builds its series mainly from data that platforms hand to BI (BI's own
descriptions; method not fully public). BPS: survey of e-commerce businesses incl. social media and chat sellers; 2022 Rp783tn,
2023 Rp1,100.87tn, 2024 Rp1,288.93tn; marketplace slice 2024 Rp203.58tn (BPS presentation, 31 Mar 2025)."""
import pathlib
import pandas as pd
d = pd.DataFrame({"BI": [476.3, 453.75, 487.01], "BPS": [783.0, 1100.87, 1288.93]}, index=[2022, 2023, 2024])
d["BPS_div_BI"] = (d.BPS / d.BI).round(2)
d["BI_growth_pct"] = (100 * d.BI.pct_change()).round(1)
d["BPS_growth_pct"] = (100 * d.BPS.pct_change()).round(1)
d.loc[2024, "BPS_marketplace"] = 203.58
d.loc[2024, "BPS_marketplace_div_BI"] = round(203.58 / 487.01, 2)
d.to_csv(pathlib.Path(__file__).parent / "tables/yardsticks_bi_bps.csv")
print(d.to_string())
