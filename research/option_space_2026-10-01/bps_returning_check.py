"""EXPLORATORY (9 Oct 2026; designed after the entry test and the profile, data already seen): do the 2023 survey's established sellers look
like sellers returning from a break? A seller who paused in 2022 and resumed during 2023 would sell online for only part of 2023 (unless it
resumed in January). So compare part-year selling among sellers who started before the reference year: 2022 survey (2023 file, question 3.08,
months of online selling in 2022; sellers who started by 2021) vs 2023 survey (2024 file, R311 month flags for 2023; sellers who started by 2022).
The month question changed format between files (a list of months vs twelve yes/no flags), which is stated.
Licensed inputs are not committed; output is national weighted totals only.
Run: python3 bps_returning_check.py --f2023 B.dbf --f2024 C.dbf -> tables/bps_returning_check.json"""
import argparse, json
import numpy as np
from bps_microdata_tests import read_dbf, num

x_ = argparse.ArgumentParser(); x_.add_argument("--f2023"); x_.add_argument("--f2024"); x = x_.parse_args()
a, b = read_dbf(x.f2023), read_dbf(x.f2024)
wa, sa, wb, sb = num(a["w_usaha_fi"]), num(a["r305"]), num(b["w_final"]), num(b["r307"])
ma = np.array([len([m for m in v.split(",") if m.strip()]) for v in a["r308"]])
mb = sum((num(b["r311_" + m]) == 1).astype(int) for m in ["jan", "feb", "mar", "apr", "mei", "juni", "juli", "agt", "sept", "okt", "nov", "des"])
out = {}
for lab, w, s, m, ref in [("2022 survey (2022 activity)", wa, sa, ma, 2022), ("2023 survey (2023 activity)", wb, sb, mb, 2023)]:
    est = s <= ref - 1
    r = {"established_sellers_k": float(w[est].sum()) / 1e3, "all_12_months_k": float(w[est & (m == 12)].sum()) / 1e3,
         "part_year_k": float(w[est & (m < 12)].sum()) / 1e3}
    r["part_year_pct"] = 100 * r["part_year_k"] / r["established_sellers_k"]
    r["by_months_k"] = {f"{lo}-{hi}": float(w[est & (m >= lo) & (m <= hi)].sum()) / 1e3 for lo, hi in [(1, 3), (4, 6), (7, 9), (10, 11)]}
    out[lab] = r
k = list(out)
out["change_k"] = {"all_12_months": out[k[1]]["all_12_months_k"] - out[k[0]]["all_12_months_k"], "part_year": out[k[1]]["part_year_k"] - out[k[0]]["part_year_k"]}
# Same start-year groups in both rounds (independent review, 9 Oct): sellers who started online by year c, in the 2022 and 2023 activity files.
out["same_start_year_groups"] = {}
for c in (2020, 2021, 2022):
    r = {}
    for lab, w, s_, m in [("2022", wa, sa, ma), ("2023", wb, sb, mb)]:
        g = s_ <= c
        r[lab] = {"all_12_months_k": float(w[g & (m == 12)].sum()) / 1e3, "part_year_k": float(w[g & (m < 12)].sum()) / 1e3}
        r[lab]["part_year_pct"] = 100 * r[lab]["part_year_k"] / (r[lab]["part_year_k"] + r[lab]["all_12_months_k"])
    out["same_start_year_groups"][f"started by {c}"] = r
out["reading"] = ("Part-year selling falls under all three common cutoffs. Diagnostic only: without linked histories, sellers returning during "
                  "the year can be offset by exits of part-year sellers or by incumbents moving to full-year selling; January returns are also possible.")
s = json.dumps(out, indent=1); print(s); open("tables/bps_returning_check.json", "w").write(s)
