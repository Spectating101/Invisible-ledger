"""Part 3 groundwork (7 Oct 2026): checks added while preparing the H1 chapter, all from committed tables.
1. Grab on-demand take-rate change split into pricing within rides and deliveries vs mix between them (annual sums of verified quarters; group scope).
2. Tokopedia 2022-23 in two views: rupiah of extra net revenue (the proposal's 60.6%) and per rupiah of transaction value.
3. The 2023 verdict: Indonesia-only measures of buying through platforms vs platform revenue, BPS and household spending;
   the upper bound on growth in the number of online sellers implied by entry (E5); the direction of existing sellers' online revenue (E6).
Run: python3 h1_groundwork.py -> tables/h1_groundwork.json"""
import json
import pandas as pd

T = "tables/"
out = {}

# 1. Grab: pricing within segments vs mix (midpoint weights; the two parts add up to the total change)
q = pd.read_csv(T + "grab_quarterly_verified.csv", index_col=0)
q["yr"] = q.index.str[:4]
full = q.groupby("yr").size() == 4
a = q.groupby("yr")[["mob_gmv", "del_gmv", "rev_mob", "rev_del"]].sum()[full]
a["m_mob"], a["m_del"] = a.rev_mob / a.mob_gmv, a.rev_del / a.del_gmv
a["w_mob"] = a.mob_gmv / (a.mob_gmv + a.del_gmv)
a["m"] = (a.rev_mob + a.rev_del) / (a.mob_gmv + a.del_gmv)
grab = {}
for y0, y1 in [("2022", "2023"), ("2023", "2024"), ("2024", "2025")]:
    r0, r1 = a.loc[y0], a.loc[y1]
    within = (r0.w_mob + r1.w_mob) / 2 * (r1.m_mob - r0.m_mob) + ((1 - r0.w_mob) + (1 - r1.w_mob)) / 2 * (r1.m_del - r0.m_del)
    mix = ((r0.m_mob + r1.m_mob) / 2 - (r0.m_del + r1.m_del) / 2) * (r1.w_mob - r0.w_mob)
    grab[f"{y0}-{y1}"] = {"take_rate_change_pts": 100 * (r1.m - r0.m), "within_pts": 100 * within, "mix_pts": 100 * mix,
                         "rides_take_rate_pct": [100 * r0.m_mob, 100 * r1.m_mob], "deliveries_take_rate_pct": [100 * r0.m_del, 100 * r1.m_del]}
out["grab_pricing_vs_mix"] = grab

# 2. Tokopedia: two views of the same 2022-23 change
t = json.load(open(T + "incentive_leverage.json"))["tokopedia"]
tm = pd.read_csv(T + "transitions_master.csv")
gV = float(tm[(tm.set == "IDN_main") & (tm.firm == "Tokopedia e-commerce segment") & (tm.y1 == 2023)].gV.iloc[0]) / 100
dn = t["net23"] - t["net22"]
out["tokopedia_two_views"] = {
    "net_revenue_change_IDR_tn": dn,
    "rupiah_view_share_lower_incentives_pct": 100 * (t["incent22"] - t["incent23"]) / dn,
    "rupiah_view_share_higher_gross_fees_pct": 100 * (t["gross23"] - t["gross22"]) / dn,
    "transaction_value_growth_pct": 100 * gV,
    "per_unit_gross_fee_change_pct": 100 * ((t["gross23"] / t["gross22"]) / (1 + gV) - 1),
    "per_unit_incentive_change_pct": 100 * ((t["incent23"] / t["incent22"]) / (1 + gV) - 1)}

# 3. The 2023 verdict
g = pd.read_csv(T + "consistency_grid_growth.csv", index_col=0)
idn = tm[tm.set == "IDN_main"].set_index(["firm", "y1"])
buying_2023 = {"Tokopedia transaction value": float(idn.loc[("Tokopedia e-commerce segment", 2023), "gV"]),
               "GoTo on-demand transaction value": float(g.loc["GoTo on-demand GTV", "2023"]),
               "Bank Indonesia e-commerce": float(g.loc["Bank Indonesia e-commerce", "2023"]),
               "Momentum Works Indonesia GMV": float(g.loc["Momentum Works Indonesia GMV", "2023"]),
               "Bukalapak transaction value": float(idn.loc[("Bukalapak Group", 2023), "gV"]),
               "Blibli 3P transaction value": float(idn.loc[("Blibli 3P Retail", 2023), "gV"])}
revenue_2023 = {"Tokopedia": float(idn.loc[("Tokopedia e-commerce segment", 2023), "gR"]),
                "Bukalapak": float(idn.loc[("Bukalapak Group", 2023), "gR"]),
                "Blibli 3P": float(idn.loc[("Blibli 3P Retail", 2023), "gR"])}
hh = float(g.loc["Official household spending (nominal)", "2023"])
d = json.load(open(T + "bps_descriptives.json"))
out["verdict_2023"] = {
    "buying_growth_pct": buying_2023,
    "measures_below_household_spending": sum(v < hh for v in buying_2023.values()),
    "measures_falling": sum(v < 0 for v in buying_2023.values()),
    "measures_counted": len(buying_2023),
    "household_spending_nominal_growth_pct": hh,
    "platform_revenue_growth_pct": revenue_2023,
    "BPS_value_growth_pct": float(g.loc["BPS e-commerce", "2023"]),
    "BPS_published_seller_growth_pct": d["published_count_growth_pct"],
    "seller_growth_upper_bound_from_entry_pct": d["max_count_growth_from_entry_pct"],
    "existing_sellers_online_revenue_direction_pct": d["incumbents_2023_revenue_direction"]}
s = json.dumps(out, indent=1); print(s); open(T + "h1_groundwork.json", "w").write(s)
