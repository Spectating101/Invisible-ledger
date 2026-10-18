"""Part 6 cheap checks (8 Oct 2026): how far each 2026 rule reaches into what the thesis measures. Built only from committed tables.
- Marketplace tax (PMK 37/2025): seller reach (from gel_checks.json) and value reach = marketplace share of online value (E2) x share of
  marketplace value held by sellers with Rp300m+ a year (E8), 2022, three bracket scenarios. Upper bounds: the tax exempts individuals up
  to Rp500m and BPS's brackets split at Rp300m. Identification reach: PMK 37 Art. 6 requires every domestic marketplace seller, exempt or
  not, to give the marketplace a tax number or NIK; marketplace sellers' share of online sellers (bps_descriptives.json).
- Commission cap (two-wheel rides only): rides' share of Grab on-demand GMV and the take rate by segment (group-wide), latest quarters.
Run: python3 part6_checks.py -> tables/part6_checks.json"""
import json
import pandas as pd
T = "tables/"
b = json.load(open(T + "bps_microdata_results.json"))["file2023"]; g = json.load(open(T + "gel_checks.json"))
d = json.load(open(T + "bps_descriptives.json")); tb = pd.read_csv(T + "tax_base_rulers.csv", index_col=0)
q = pd.read_csv(T + "grab_quarterly_verified.csv", index_col=0).tail(4)
out = {
 "tax_value_reach_pct_2022": {s: b[f"E2_{s}"] * b[f"E8_{s}"] / 100 for s in ("low", "mid", "high")},
 "tax_seller_reach_pct": g["share_of_all_online_sellers_marketplace_and_300m_plus_pct"],
 "marketplace_sellers_share_pct": {"2022": d["marketplace_share"]["2022"], "2023": d["marketplace_share"]["2023"], "2024_published": d["marketplace_share"]["2024_published"]},
 "off_marketplace_wanting_to_join_pct": g["non_marketplace_sellers_wanting_to_join_pct"],
 "tax_base_range_Rp_tn": [float(tb.base_Rp_tn.min()), float(tb.base_Rp_tn.max())],
 "tax_at_half_pct_share_of_2026_target_pct": [float(tb["pct_of_2026_tax_target"].min()), float(tb["pct_of_2026_tax_target"].max())],
 "grab_rides_share_of_ondemand_gmv_pct_last4q": float((100 * q.mob_gmv / q.od_gmv).mean()),
 "grab_take_rate_rides_pct_last4q": float((100 * q.rev_mob / q.mob_gmv).mean()),
 "grab_take_rate_deliveries_pct_last4q": float((100 * q.rev_del / q.del_gmv).mean()),
 "grab_incentives_pct_of_ondemand_gmv_last4q": float(q.iota_pct.mean()),
}
s = json.dumps(out, indent=1); print(s); open(T + "part6_checks.json", "w").write(s)
