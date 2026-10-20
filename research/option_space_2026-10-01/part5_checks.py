"""EXPLORATORY (8 Oct 2026; data already seen): why BPS's marketplace slice is so much smaller than platform GMV (about 4.4x in 2024).
Licensed BPS files; national weighted totals only.
1. Size: BPS marketplace sellers (2022) by annual revenue bracket, their share of marketplace value (scenarios), and the number of sample rows behind each.
2. Composition: which apps BPS's "marketplace" sellers use (2023): shopping marketplaces vs food and ride apps vs travel apps.
Definitions (shipping, digital goods, travel, offline sales inside platform GMV) are in tables/v_definition_map.csv; foreign sellers and platform
merchant counts are from company statements (recorded in PART5 groundwork).
Run: python3 part5_checks.py --f2023 B.dbf --f2024 C.dbf -> tables/part5_checks.json"""
import argparse, json
import numpy as np
from bps_microdata_tests import read_dbf, num, bracket_value, SCEN

x_ = argparse.ArgumentParser(); x_.add_argument("--f2023"); x_.add_argument("--f2024"); x = x_.parse_args()
a, b = read_dbf(x.f2023), read_dbf(x.f2024)
out = {}
w = num(a["w_usaha_fi"]); mk = num(a["r310b"]); cat = num(a["kategori_p"]); user = num(a["r307e"]) == 1
out["bps_marketplace_sellers_2022_k"] = float(w[user].sum()) / 1e3
size = {}
for i, lab in enumerate(["<300m", "300m-2.5bn", "2.5-50bn", ">50bn"], 1):
    m = user & (cat == i)
    size[lab] = {"share_of_marketplace_sellers_pct": 100 * float(w[m].sum() / w[user].sum()), "sample_rows": int(m.sum()),
                 "share_of_marketplace_value_pct": {s: 100 * float(np.nansum((bracket_value(cat, s) * mk / 100 * w)[cat == i]) / np.nansum(bracket_value(cat, s) * mk / 100 * w)) for s in SCEN}}
out["bps_marketplace_by_size_2022"] = size
wb = num(b["w_final"]); mkb = num(b["r309e"]) == 1
y = lambda i: num(b["r309e_y_%02d" % i]) == 1
shop = y(1) | y(2) | y(3) | y(6); food = y(4) | y(5); travel = y(7) | y(8) | y(9)
W = wb[mkb].sum()
out["bps_marketplace_sellers_by_app_2023_pct"] = {
    "shopping marketplaces (Tokopedia, Shopee, Bukalapak, Lazada)": 100 * float(wb[mkb & shop].sum() / W),
    "food and ride apps (Gojek, Grab)": 100 * float(wb[mkb & food].sum() / W),
    "only food and ride apps": 100 * float(wb[mkb & food & ~shop].sum() / W),
    "travel apps": 100 * float(wb[mkb & travel].sum() / W)}
s = json.dumps(out, indent=1); print(s); open("tables/part5_checks.json", "w").write(s)
