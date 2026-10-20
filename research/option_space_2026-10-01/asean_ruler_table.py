"""Official e-commerce value vs e-Conomy SEA e-commerce GMV, 2023 and 2024, in US$ bn (World Bank period-average FX, same series as the Indonesia bridge).
Inputs (all quote-verified in tables/src): DOSM ICTEC 2025 (Malaysia), ETDA (Thailand), IDEA White Book / VECOM (Vietnam), BPS and Bank Indonesia (Indonesia), e-Conomy SEA 2024 regional report.
CAUTION: scopes differ.  Official series count online sales across all sectors (Malaysia and Thailand include services; totals include B2B); e-Conomy 'e-commerce' is the
e-commerce vertical only (transport, food, travel, media are separate).  The ratios therefore describe how far apart the rulers are, not which one is wrong.
Vietnam values were stored x10 in the extraction (comma decimals) and are corrected here (20.5, 25.0, 32.0)."""
import json, pandas as pd
fx = json.load(open("tables/src/worldbank_fx_2022_2024.json"))
E = {("Indonesia", 2023): 59, ("Indonesia", 2024): 65, ("Malaysia", 2023): 13, ("Malaysia", 2024): 16, ("Thailand", 2023): 22, ("Thailand", 2024): 26, ("Vietnam", 2023): 19, ("Vietnam", 2024): 22}
rows = []
def add(c, y, label, usd): rows.append(dict(country=c, year=y, series=label, usd_bn=usd, econ_usd_bn=E[(c, y)], ratio_to_econ=usd / E[(c, y)]))
add("Indonesia", 2023, "BPS total (all channels, businesses)", 1100.87e3 / fx["IDN"]["2023"])
add("Indonesia", 2024, "BPS total", 1288.93e3 / fx["IDN"]["2024"])
add("Indonesia", 2024, "Bank Indonesia e-commerce value", 487e3 / fx["IDN"]["2024"])
add("Malaysia", 2023, "DOSM e-commerce income, total", 1184.1 / fx["MYS"]["2023"]); add("Malaysia", 2023, "DOSM B2C", 336.6 / fx["MYS"]["2023"])
add("Malaysia", 2024, "DOSM e-commerce income, total", 1288.1 / fx["MYS"]["2024"]); add("Malaysia", 2024, "DOSM B2C", 374.7 / fx["MYS"]["2024"])
add("Thailand", 2023, "ETDA total ex e-Auction, incl. B2G", 5815362e0 / 1e3 / fx["THA"]["2023"]); add("Thailand", 2023, "ETDA B2C", 2905021 / 1e3 / fx["THA"]["2023"])
add("Thailand", 2024, "ETDA B2C (forecast)", 3108562 / 1e3 / fx["THA"]["2024"])
add("Vietnam", 2023, "IDEA B2C", 20.5); add("Vietnam", 2023, "VECOM total", 25.0); add("Vietnam", 2024, "VECOM total", 32.0)
T = pd.DataFrame(rows); T.round(2).to_csv("tables/asean_ruler_table.csv", index=False)
pd.set_option("display.width", 200); print(T.round(2).to_string())
