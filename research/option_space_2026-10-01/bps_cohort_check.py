"""EXPLORATORY (8 Oct 2026; designed after E5, data already seen): do the same start-year cohorts of online sellers shrink between BPS surveys,
as they must if each survey counts the same population (sellers can stop, but nobody can join a past start year)?
Weighted counts by year the business started selling online: 2021 file (r305, year 2020), 2023 file (r305, year 2022), 2024 file (r307, year 2023).
A cohort that grows between surveys means the later survey counted sellers that the earlier one did not: found, not new (net of exits, so a lower bound).
Licensed inputs are not committed; output is national weighted totals only.
Run: python3 bps_cohort_check.py --f2021 A.dbf --f2023 B.dbf --f2024 C.dbf -> tables/bps_cohort_check.json"""
import argparse, json
import numpy as np
from bps_microdata_tests import read_dbf, num

a_ = argparse.ArgumentParser(); a_.add_argument("--f2021"); a_.add_argument("--f2023"); a_.add_argument("--f2024"); x = a_.parse_args()
files = {"2020": (read_dbf(x.f2021), "w_usaha_fi", "r305"), "2022": (read_dbf(x.f2023), "w_usaha_fi", "r305"), "2023": (read_dbf(x.f2024), "w_final", "r307")}
W = {k: (num(c[w]), num(c[s])) for k, (c, w, s) in files.items()}
def count(k, lo, hi):
    w, s = W[k]; return float(w[(s >= lo) & (s <= hi)].sum())
out = {"cohort_counts_thousands": {}, "started_by": {}}
for lo, hi, lab in [(1900, 2015, "up to 2015"), (2016, 2017, "2016-17"), (2018, 2019, "2018-19"), (2020, 2020, "2020"), (2021, 2021, "2021"), (2022, 2022, "2022"), (2023, 2023, "2023")]:
    out["cohort_counts_thousands"][lab] = {k: count(k, lo, hi) / 1e3 for k in W}
for cut in (2019, 2020, 2021):
    v = {k: count(k, 1900, cut) / 1e3 for k in W}
    out["started_by"][str(cut)] = {**v, "change_2020_to_2022_pct": 100 * (v["2022"] / v["2020"] - 1) if v["2020"] else None,
                                   "change_2022_to_2023_pct": 100 * (v["2023"] / v["2022"] - 1)}
total22 = float(W["2022"][0].sum()); total23 = float(W["2023"][0].sum()); pre23_in_23 = count("2023", 1900, 2022)
out["rise_2022_to_2023"] = {"published_count_2022_k": total22 / 1e3, "count_2023_k": total23 / 1e3, "rise_k": (total23 - total22) / 1e3,
                            "entrants_2023_k": count("2023", 2023, 2023) / 1e3,
                            "pre_2023_sellers_more_than_counted_before_k": (pre23_in_23 - total22) / 1e3,
                            "share_of_rise_from_pre_2023_sellers_pct": 100 * (pre23_in_23 - total22) / (total23 - total22)}
s = json.dumps(out, indent=1); print(s); open("tables/bps_cohort_check.json", "w").write(s)
