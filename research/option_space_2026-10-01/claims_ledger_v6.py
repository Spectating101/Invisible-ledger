"""Claims ledger v6 (7 Oct 2026): Part 3 groundwork numbers (Grab pricing vs mix, Tokopedia two views, the 2023 verdict).
Run from this folder after h1_groundwork.py: python3 claims_ledger_v6.py -> tables/claims_ledger_v6.csv"""
import json
import pandas as pd
T = "tables/"
h = json.load(open(T + "h1_groundwork.json")); gm = h["grab_pricing_vs_mix"]["2022-2023"]; tk = h["tokopedia_two_views"]; v = h["verdict_2023"]
claims = [
 ("G01", "Grab on-demand take-rate change 2022-23 (pts)", 3.9, gm["take_rate_change_pts"], 0.05),
 ("G02", "...of which pricing within rides and deliveries (pts)", 3.5, gm["within_pts"], 0.05),
 ("G03", "...of which mix between them (pts)", 0.35, gm["mix_pts"], 0.01),
 ("G04", "Grab deliveries take rate 2022 (%)", 6.8, gm["deliveries_take_rate_pct"][0], 0.05),
 ("G05", "Grab deliveries take rate 2023 (%)", 11.7, gm["deliveries_take_rate_pct"][1], 0.05),
 ("K01", "Tokopedia: share of extra net revenue from lower incentives (%)", 60.5, tk["rupiah_view_share_lower_incentives_pct"], 0.05),
 ("K02", "Tokopedia: gross fees per rupiah of transaction value (%)", 21.2, tk["per_unit_gross_fee_change_pct"], 0.05),
 ("K03", "Tokopedia: incentives per rupiah of transaction value (%)", -25.0, tk["per_unit_incentive_change_pct"], 0.05),
 ("V10", "2023: Indonesia-only buying measures below household spending growth (of 6)", 5, v["measures_below_household_spending"], 0),
 ("V11", "2023: Indonesia-only buying measures that fell (of 6)", 3, v["measures_falling"], 0),
 ("V12", "2023: GoTo on-demand transaction value growth (%)", -10.5, v["buying_growth_pct"]["GoTo on-demand transaction value"], 0.05),
 ("V13", "2023: Bank Indonesia e-commerce growth (%)", -4.7, v["buying_growth_pct"]["Bank Indonesia e-commerce"], 0.05),
 ("V14", "2023: household spending nominal growth (%)", 9.4, v["household_spending_nominal_growth_pct"], 0.05),
 ("V15", "2023: upper bound on growth in online sellers from entry (%)", 15.5, v["seller_growth_upper_bound_from_entry_pct"], 0.05),
]
L = pd.DataFrame([dict(id=c, claim=t, stated=st, recomputed=round(float(x), 6), status="PASS" if abs(float(x) - st) <= tol else "CHECK") for c, t, st, x, tol in claims])
L.to_csv(T + "claims_ledger_v6.csv", index=False); print(L.to_string(index=False)); print(L.status.value_counts().to_dict())
