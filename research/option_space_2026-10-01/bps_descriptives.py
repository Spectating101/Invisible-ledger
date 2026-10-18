"""BPS e-commerce microdata: DESCRIPTIVE numbers reported next to the pre-registered tests (7 Oct 2026, written after the locked run).
Not tests. Weighted shares only; licensed files are never committed.
Run: python3 bps_descriptives.py --f2021 A.dbf --f2023 B.dbf --f2024 C.dbf -> tables/bps_descriptives.json"""
import argparse, json
import numpy as np
from bps_microdata_tests import read_dbf, num, wshare

a = argparse.ArgumentParser(); a.add_argument("--f2021"); a.add_argument("--f2023"); a.add_argument("--f2024")
x = a.parse_args()
c21, c23, c24 = read_dbf(x.f2021), read_dbf(x.f2023), read_dbf(x.f2024)
w21, w23, w24 = num(c21["w_usaha_fi"]), num(c23["w_usaha_fi"]), num(c24["w_final"])
out = {}

# records: share of businesses with financial statements (2023 value rebuilt from the file's marketplace / other split)
mk24 = num(c24["r309e"]) == 1; books24 = num(c24["r308"]) == 1
out["books_share"] = {"2020": wshare(num(c21["r306"]) == 1, w21), "2022": wshare(num(c23["r306"]) == 1, w23), "2023": wshare(books24, w24)}
# marketplace participation path (2024 is BPS's published 17.23%)
out["marketplace_share"] = {"2020": wshare(num(c21["r307e"]) == 1, w21), "2022": wshare(num(c23["r307e"]) == 1, w23),
                            "2023": wshare(mk24, w24), "2024_published": 17.23}
# revenue brackets (annual business revenue), 2022
cat = num(c23["kategori_p"])
out["bracket_share_2022"] = {k: wshare(cat == i, w23) for i, k in enumerate(["<300m", "300m-2.5bn", "2.5-50bn", ">50bn"], 1)}
# which apps BPS's "marketplace" sellers use, 2023 (share of marketplace users)
apps = ["Tokopedia", "Shopee", "Bukalapak", "Gojek", "Grab", "Lazada", "Agoda", "Traveloka", "Pegipegi", "Other"]
out["apps_among_marketplace_users_2023"] = {n: wshare(mk24 & (num(c24[f"r309e_y_{i:02d}"]) == 1), w24 * mk24) for i, n in enumerate(apps, 1)}
# sellers already online before 2023: online revenue up / same / down versus 2022
st = num(c24["r307"]); inc = (st < 2023) & (st > 1900); d = num(c24["r315"])
out["incumbents_2023_revenue_direction"] = {k: wshare(inc & (d == v), w24 * inc) for k, v in (("up", 1), ("same", 2), ("down", 3))}
# entry arithmetic: with zero exits, the entrant share caps count growth at e / (1 - e)
e = wshare(st == 2023, w24) / 100
out["max_count_growth_from_entry_pct"] = 100 * e / (1 - e); out["published_count_growth_pct"] = 27.40
out["chat_or_social_sellers_2023"] = wshare((num(c24["r309c"]) == 1) | (num(c24["r309d"]) == 1), w24)
s = json.dumps(out, indent=1); print(s)
open("tables/bps_descriptives.json", "w").write(s)
