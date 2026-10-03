"""Score every prediction registered for 3Q26 in one place (written 3 Oct 2026, before any 3Q26 number exists).
Cap predictions P1-P5: cap_prediction.score_v2. Three-rulers predictions R1-R3: below. Fill in the published numbers and run:
  python3 score_q3_2026.py
GoTo releases 27 Oct 2026; BPS 3Q26 GDP early November; Grab and Sea mid-November. Leave a value as None until it is published."""
import pathlib, pandas as pd
from cap_prediction import score_v2
here = pathlib.Path(__file__).parent
IN = dict(   # --- fill these from the releases (units as noted) ---
    goto_gtv_3q26_tn=None, goto_net_3q26_tn=None,             # GoTo on-demand, IDR trillion
    grab_mob_gmv=None, grab_mob_rev=None, grab_del_gmv=None, grab_del_rev=None,   # Grab, US$ m, 3Q26
    official_nominal_yoy_3q26=None,                           # BPS household (+NPISH) consumption, nominal YoY %, 3Q26
    shopee_gmv_3q26=None, shopee_mkt_rev_3q26=None,          # Sea e-commerce, US$ m, 3Q26
)
GOTO_3Q25 = (16.743, 3.205)                                   # GTV, net revenue, IDR tn (three_rulers.py)
SHOPEE_3Q25 = pd.read_csv(here / "tables/shopee_quarterly_take_rate.csv", index_col="period").loc["2025Q3", ["gmv", "marketplace_revenue"]]

def r_scores(x):
    out = {}
    if x["goto_gtv_3q26_tn"] and x["goto_net_3q26_tn"]:
        gs = 100 * (x["goto_gtv_3q26_tn"] / GOTO_3Q25[0] - 1); gr = 100 * (x["goto_net_3q26_tn"] / GOTO_3Q25[1] - 1)
        out["R1 GoTo revenue minus sales growth (pts) in [-0.5, +12.5]"] = (round(gr - gs, 1), -0.5 <= gr - gs <= 12.5)
        if x["official_nominal_yoy_3q26"] is not None:
            out["R2 GoTo sales growth below official nominal spending growth"] = ((round(gs, 1), x["official_nominal_yoy_3q26"]), gs < x["official_nominal_yoy_3q26"])
    if x["shopee_gmv_3q26"] and x["shopee_mkt_rev_3q26"]:
        ss = 100 * (x["shopee_gmv_3q26"] / SHOPEE_3Q25.gmv - 1); sr = 100 * (x["shopee_mkt_rev_3q26"] / SHOPEE_3Q25.marketplace_revenue - 1)
        out["R3 Shopee revenue minus GMV growth (pts) >= +10"] = (round(sr - ss, 1), sr - ss >= 10)
    for k, (v, ok) in out.items(): print(f"{k}: {v} -> {'CONFIRMED' if ok else 'FALSIFIED'}")
    return out

if __name__ == "__main__":
    x = IN
    if None not in (x["goto_gtv_3q26_tn"], x["goto_net_3q26_tn"], x["grab_mob_gmv"], x["grab_mob_rev"], x["grab_del_gmv"], x["grab_del_rev"]):
        score_v2(x["goto_gtv_3q26_tn"], x["goto_net_3q26_tn"], GOTO_3Q25[0], x["grab_mob_gmv"], x["grab_mob_rev"], x["grab_del_gmv"], x["grab_del_rev"])
    else:
        print("P1-P5: waiting for GoTo and Grab 3Q26 numbers")
    if not r_scores(x): print("R1-R3: waiting for 3Q26 numbers")
