"""PRE-REGISTERED PREDICTIONS for Indonesia's 8% commission cap (written 1 Oct 2026, before any post-cap result is public).

Event: Presidential Regulation 27/2026 (two-wheel ride-hailing only; commission cap 20% -> 8%), in force 1 July 2026. Source grades: C (news/transcripts) unless noted;
verify against primary documents when the Q3 2026 releases appear (GoTo and Grab, expected about Nov 2026).

Baselines (2Q26, the last pre-cap quarter):
  GoTo on-demand: net take = net revenue / GTV. Transcript summary: GTV ~Rp16.7tn (+2% YoY), net revenue ~Rp3.6tn (+20% YoY) -> ~21.6%. Consistent with 2Q25 (GTV 16,371bn, net 2,987bn). GRADE C.
  Grab On-Demand: net take = (Mobility rev + Deliveries rev) / (Mobility GMV + Deliveries GMV) = (331+531)/(2214+4249) = 13.3%. Source: Grab 2Q26 6-K via summary. GRADE B-.
Management's own estimate (GoTo, 2Q26 results): net impact on on-demand adjusted EBITDA in 2H26 ~Rp300bn; GoRide ~7% of group net revenue. Grab: two-wheel < 6% of Mobility (grade C).

Derivation of the GoTo range. Mechanical, no offsets: 7% of group net revenue (~Rp5.7tn/quarter) = ~Rp0.40tn/quarter on two-wheel; commission falls by 60% (20% -> 8%) -> -Rp0.24tn/quarter
 = -1.4 points of GTV (Rp16.7tn). Management estimate: Rp300bn over two quarters = Rp150bn/quarter = -0.9 points. Offsets (fees, fares, lower incentives) can shrink the drop.
 => P1: GoTo on-demand net take in 3Q26 is LOWER than in 2Q26 by 0.3 to 1.5 points (central estimate 0.9).
For Grab: 6% of Mobility GMV (~$133m/quarter) x 12 points = ~$16m/quarter = -0.25 points of On-Demand GMV.
 => P2: Grab On-Demand net take in 3Q26 is within -0.6 to +0.4 points of 2Q26 (13.3%), i.e. no visible cap effect beyond ordinary noise.
 => P3 (mechanism): GoTo's drop is NOT matched by an equal rise in the other component: i.e. total on-demand GTV growth stays within 0 to +8% YoY (cap did not collapse volume; management says volumes stable).
Falsification: P1 fails if the 3Q26 net take rises vs 2Q26 or falls by more than 1.5 points; P2 fails outside the range; P3 fails if on-demand GTV falls YoY or grows more than 8%.
Run score(...) with the actual 3Q26 numbers once published.
"""
BASE = {"goto_net_take_2q26_pct": 21.6, "grab_net_take_2q26_pct": 100 * (331 + 531) / (2214 + 4249), "goto_gtv_2q25_bn": 16371}

def score(goto_gtv_bn, goto_net_bn, grab_mob_gmv, grab_mob_rev, grab_del_gmv, grab_del_rev, goto_gtv_3q25_bn=16743):
    g = 100 * goto_net_bn / goto_gtv_bn; b = 100 * (grab_mob_rev + grab_del_rev) / (grab_mob_gmv + grab_del_gmv)
    d1 = g - BASE["goto_net_take_2q26_pct"]; d2 = b - BASE["grab_net_take_2q26_pct"]; yoy = 100 * (goto_gtv_bn / goto_gtv_3q25_bn - 1)
    res = {"P1 GoTo net take change vs 2Q26 (pt)": (round(d1, 2), -1.5 <= d1 <= -0.3), "P2 Grab net take change vs 2Q26 (pt)": (round(d2, 2), -0.6 <= d2 <= 0.4),
           "P3 GoTo on-demand GTV YoY (%)": (round(yoy, 1), 0 <= yoy <= 8)}
    for k, (v, ok) in res.items(): print(f"{k}: {v}  -> {'CONFIRMED' if ok else 'FALSIFIED'}")
    return res

if __name__ == "__main__":
    print("Pre-registered 1 Oct 2026. Baselines:", {k: round(v, 2) for k, v in BASE.items()})
    print("P1 GoTo on-demand net take 3Q26: 2Q26 level minus 0.3 to 1.5 pt (central 0.9)")
    print("P2 Grab On-Demand net take 3Q26: within -0.6 to +0.4 pt of 2Q26 (13.3%)")
    print("P3 GoTo on-demand GTV 3Q26 YoY: between 0% and +8%")
