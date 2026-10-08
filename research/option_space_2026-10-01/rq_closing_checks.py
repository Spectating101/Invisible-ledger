"""Two closing checks (8 Oct 2026), from committed tables only.
1. Sampling noise vs the 2023 seller surplus. BPS publishes the relative standard error (RSE) of the number of e-commerce businesses by province
   (Statistik E-Commerce 2024, Lampiran 3; tables/src/bps_2024_rse_by_province.csv). Assuming provinces are sampled independently, the
   national RSE is sqrt(sum (RSE_p x N_p)^2) / sum N_p. Applied to the 2022 and 2023 counts (independent surveys), it gives the standard error of
   the change, compared with the 306 thousand pre-2023 sellers above the whole 2022 count. Sensitivity: twice the RSE (the 2022 round had a
   smaller sample, 31.7k rows vs 39.7k). Exploratory: the RSE comes from a later survey round.
2. How much stays outside platform-based measures, two levels.
   Inside platforms: revenue as a share of transaction value, 2023, three platforms (proposal Table 5).
   Across the online economy: BPS's marketplace channel (shopping marketplaces plus food and ride apps) as a share of online sales value:
   2022 from the microdata (E2, three bracket scenarios), 2023 and 2024 published (bps_recompute.json). Within BPS's own survey.
Run: python3 rq_closing_checks.py -> tables/rq_closing_checks.json"""
import csv, json, math
T = "tables/"
prov = list(csv.DictReader(open(T + "src/bps_2024_rse_by_province.csv")))
N = sum(int(p["ecommerce_businesses_2024"]) for p in prov)
rse = math.sqrt(sum((int(p["ecommerce_businesses_2024"]) * float(p["rse_pct"]) / 100) ** 2 for p in prov)) / N
r = json.load(open(T + "bps_cohort_check.json"))["rise_2022_to_2023"]; n22, n23, extra = r["published_count_2022_k"], r["count_2023_k"], r["pre_2023_sellers_more_than_counted_before_k"]
noise = {}
for k, f in (("published_rse", 1), ("twice_rse", 2)):
    se = math.sqrt((n22 * rse * f) ** 2 + (n23 * rse * f) ** 2)
    noise[k] = {"national_rse_pct": 100 * rse * f, "se_of_change_k": se, "surplus_in_se": extra / se}
b = json.load(open(T + "bps_microdata_results.json"))["file2023"]; rc = json.load(open(T + "bps_recompute.json"))["marketplace"]
out = {"provinces": len(prov), "province_total_2024": N, "published_total_2024": 4400972, "noise_vs_2023_surplus": noise,
       "revenue_share_of_transaction_value_2023_pct": 100 * 3.162 / 43.233,
       "marketplace_channel_share_of_online_value_pct": {"2022_low": b["E2_low"], "2022_mid": b["E2_mid"], "2022_high": b["E2_high"],
                                                         "2023_published": rc["mkt_share_2023"], "2024_published": rc["mkt_share_2024"]}}
s = json.dumps(out, indent=1); print(s); open(T + "rq_closing_checks.json", "w").write(s)
