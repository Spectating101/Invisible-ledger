"""How BPS's 2022->2023 rise in online sellers splits into new entrants and sellers counted for the first time (8 Oct 2026, exploratory).
Direct accounting from committed cohort totals (bps_cohort_check.json; licensed microdata not needed):
  rise = entrants (started selling online in 2023) + (pre-2023 sellers in the 2023 survey - all sellers in the 2022 survey).
The second term is net of sellers who stopped. Adding back stopped sellers at a given yearly rate gives sellers counted for the first time.
The reference rate is the yearly shrink of sellers who started by 2020, between the 2020 and 2022 surveys (-9.9% over two years).
Run: python3 bps_rise_accounting.py -> tables/bps_rise_accounting.json"""
import json
c = json.load(open("tables/bps_cohort_check.json")); r = c["rise_2022_to_2023"]
rise, ent, extra, n22 = r["rise_k"], r["entrants_2023_k"], r["pre_2023_sellers_more_than_counted_before_k"], r["published_count_2022_k"]
ref = 1 - (1 + c["started_by"]["2020"]["change_2020_to_2022_pct"] / 100) ** 0.5
out = {"rise_k": rise, "entrants_k": ent, "pre_2023_above_2022_count_k": extra, "reference_exit_rate_pct": 100 * ref, "scenarios": {}}
for name, x in (("no_exits", 0.0), ("half_reference", ref / 2), ("reference", ref)):
    stopped = x * n22
    out["scenarios"][name] = {"exit_rate_pct": 100 * x, "stopped_k": stopped, "newly_counted_k": extra + stopped,
                              "newly_counted_share_of_rise_pct": 100 * (extra + stopped) / rise,
                              "net_entry_share_of_rise_pct": 100 * (ent - stopped) / rise}
s = json.dumps(out, indent=1); print(s); open("tables/bps_rise_accounting.json", "w").write(s)
