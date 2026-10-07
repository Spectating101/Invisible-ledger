"""EXPLORATORY (8 Oct 2026; data already seen): cheap checks that link H1, H2 and the indicator comparison. National weighted totals only.
1. Sellers' own view of 2023: main obstacle to selling online (R325) and, for sellers not on marketplaces, wish to join one (R309E_GBNG).
2. Do indicators agree where they measure the same slice? BPS marketplace value 2022->2023 (2022 share from E2, all three scenarios,
   times the published Rp783tn; 2023 = published 18.23% of Rp1,100.87tn) vs Bank Indonesia and Momentum Works; 2023->2024 published (+1.45%).
3. Reach of the marketplace tax: share of ALL online sellers (2022) that sell on marketplaces AND have annual revenue of Rp300m or more
   (upper bound for the Rp500m exemption).
4. Scenario: value that the newly counted pre-2023 sellers (306 thousand, net) could add, using the 2022 average online value of
   chat-or-social-only sellers relative to all sellers (bracket scenarios), scaled to BPS's published 2022 average per business.
5. Existing sellers' own reported change in online revenue, by number of workers (seller-weighted; the 2024 file has no revenue amounts, so no value weights).
Run: python3 gel_checks.py --f2023 B.dbf --f2024 C.dbf -> tables/gel_checks.json"""
import argparse, json
import numpy as np
from bps_microdata_tests import read_dbf, num, bracket_value, SCEN, wmedian

x_ = argparse.ArgumentParser(); x_.add_argument("--f2023"); x_.add_argument("--f2024"); x = x_.parse_args()
a, b = read_dbf(x.f2023), read_dbf(x.f2024)
wa, wb = num(a["w_usaha_fi"]), num(b["w_final"])
out = {}
# 1. obstacles and wish to join
obst = {1: "lack of capital", 2: "lack of skilled workers", 3: "limited internet", 4: "fraud", 5: "lack of demand", 6: "limited delivery", 7: "other"}
r325 = num(b["r325"]); ok = ~np.isnan(r325)
out["main_obstacle_2023_pct"] = {v: 100 * float(wb[ok & (r325 == k)].sum() / wb[ok].sum()) for k, v in obst.items()}
st = num(b["r307"]); d = num(b["r315"]); inc = (st < 2023) & ok
out["main_obstacle_2023_existing_sellers_revenue_down_pct"] = {v: 100 * float(wb[inc & (d == 3) & (r325 == k)].sum() / wb[inc & (d == 3)].sum()) for k, v in obst.items()}
mk = num(b["r309e"]) == 1; g = num(b["r309e_gbng"]); okg = ~mk & ~np.isnan(g)
out["non_marketplace_sellers_wanting_to_join_pct"] = 100 * float(wb[okg & (g == 1)].sum() / wb[okg].sum())
out["non_marketplace_share_answered_pct"] = 100 * float(wb[okg].sum() / wb[~mk].sum())
# 2. the marketplace slice
r = json.load(open("tables/bps_microdata_results.json"))["file2023"]
mk22 = {s: r[f"E2_{s}"] / 100 * 783.0 for s in ("low", "mid", "high")}
mk23 = 0.1823 * 1100.87
out["bps_marketplace_value_tn"] = {"2022_by_scenario": mk22, "2023_published": mk23,
                                   "growth_2022_2023_pct_by_scenario": {s: 100 * (mk23 / v - 1) for s, v in mk22.items()},
                                   "growth_2023_2024_pct_published": 1.45}
out["platform_indicators_growth_pct"] = {"Bank Indonesia 2023": -4.7, "Momentum Works 2023": 3.5, "Bank Indonesia 2024": 7.3, "Momentum Works 2024": 5.2, "e-Conomy 2024": 5.1}
out["bps_total_growth_pct"] = {"2023": 40.6, "2024": 17.1}
# 3. tax reach among all sellers
cat = num(a["kategori_p"]); mka = num(a["r307e"]) == 1
out["share_of_all_online_sellers_marketplace_and_300m_plus_pct"] = 100 * float(wa[mka & (cat >= 2)].sum() / wa.sum())
out["share_of_all_online_sellers_on_marketplaces_pct"] = 100 * float(wa[mka].sum() / wa.sum())
# 4. scenario value of newly counted sellers
off = num(a["r310a"]); only_chat = ((num(a["r307c"]) == 1) | (num(a["r307d"]) == 1)) & ~mka & (num(a["r307a"]) != 1)
avg_all_2022 = 783e12 / 2_995_879
newly = json.load(open("tables/bps_cohort_check.json"))["rise_2022_to_2023"]["pre_2023_sellers_more_than_counted_before_k"] * 1e3
sc = {}
for s in SCEN:
    online = bracket_value(cat, s) * (100 - off) / 100
    rel = float(np.nansum(online[only_chat] * wa[only_chat]) / wa[only_chat].sum() / (np.nansum(online * wa) / wa.sum()))
    sc[s] = {"chat_only_avg_relative_to_all": rel, "value_added_tn": newly * avg_all_2022 * rel / 1e12}
out["newly_counted_value_scenarios"] = sc
# entrants (513 thousand in 2023), using 2022 starters in the 2022 file as the size proxy
st22 = num(a["r305"]); entrants = json.load(open("tables/bps_cohort_check.json"))["rise_2022_to_2023"]["entrants_2023_k"] * 1e3
se = {}
for s in SCEN:
    online = bracket_value(cat, s) * (100 - off) / 100
    rel = float(np.nansum(online[st22 == 2022] * wa[st22 == 2022]) / wa[st22 == 2022].sum() / (np.nansum(online * wa) / wa.sum()))
    se[s] = {"new_seller_avg_relative_to_all": rel, "value_added_tn": entrants * avg_all_2022 * rel / 1e12}
out["entrants_value_scenarios"] = se
inc = out["published_value_increase_2022_2023_tn"] = 1100.87 - 783.0
out["value_increase_split_pct"] = {s: {"newly_counted": 100 * sc[s]["value_added_tn"] / inc, "entrants": 100 * se[s]["value_added_tn"] / inc,
                                       "rest (existing sellers and other)": 100 - 100 * (sc[s]["value_added_tn"] + se[s]["value_added_tn"]) / inc} for s in SCEN}
# 5. existing sellers' own reported change in online revenue (2023 vs 2022), seller-weighted, by number of workers
p_ = num(b["r315b"]); sig = np.where(d == 1, p_, np.where(d == 2, 0.0, np.where(d == 3, -p_, np.nan))); incs = (st < 2023) & ~np.isnan(sig); tk = num(b["total_tk"])
ex = {"all": {"mean_pct": float(np.nansum(sig[incs] * wb[incs]) / wb[incs].sum()), "median_pct": wmedian(np.where(incs, sig, np.nan), wb)}}
for lab, m in [("1 worker", tk <= 1), ("2-4 workers", (tk >= 2) & (tk <= 4)), ("5-19 workers", (tk >= 5) & (tk <= 19)), ("20+ workers", tk >= 20)]:
    mm = incs & m
    ex[lab] = {"share_pct": 100 * float(wb[mm].sum() / wb[incs].sum()), "mean_pct": float(np.nansum(sig[mm] * wb[mm]) / wb[mm].sum()),
               "up_pct": 100 * float(wb[mm & (d == 1)].sum() / wb[mm].sum()), "down_pct": 100 * float(wb[mm & (d == 3)].sum() / wb[mm].sum())}
out["existing_sellers_reported_change_2023"] = ex
s = json.dumps(out, indent=1); print(s); open("tables/gel_checks.json", "w").write(s)
