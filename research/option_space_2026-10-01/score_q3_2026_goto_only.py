"""Score the GoTo-only predictions (P1, P3, P5, R1; R2 once BPS publishes) as soon as GoTo's 3Q26 release is out (27 Oct 2026),
without waiting for Grab and Sea (mid-November). Written 15 Oct 2026, before any 3Q26 number exists.
It copies the formulas and thresholds of cap_prediction.score_v2 and score_q3_2026.r_scores unchanged; those registered files are not edited.
Usage: python3 score_q3_2026_goto_only.py GTV_TN NET_REVENUE_TN [BPS_NOMINAL_HH_YOY_PCT]   (GoTo on-demand, IDR trillion)"""
import sys
from cap_prediction import BASE2
from score_q3_2026 import GOTO_3Q25

def score(gtv, net, hh=None):
    take = 100 * net / gtv; d1 = take - BASE2["goto_net_take_2q26_pct"]
    yoy = 100 * (gtv / GOTO_3Q25[0] - 1); rev = 100 * (net / GOTO_3Q25[1] - 1)
    out = {
        "P1 GoTo net take change vs 2Q26 (pt) in [-2.5, -0.3]": (round(d1, 2), -2.5 <= d1 <= -0.3),
        "P3 GoTo GTV YoY (%) in [0, 12]": (round(yoy, 1), 0 <= yoy <= 12),
        "P5 GoTo GTV YoY (%) >= 5; falsified only if < 2": (round(yoy, 1), True if yoy >= 5 else (False if yoy < 2 else None)),
        "R1 GoTo revenue minus GTV growth (pt) in [-0.5, +12.5]": (round(rev - yoy, 1), -0.5 <= rev - yoy <= 12.5),
    }
    if hh is not None:
        out["R2 GoTo GTV growth below nominal household spending growth"] = ((round(yoy, 1), hh), yoy < hh)
    for k, (v, ok) in out.items():
        print(f"{k}: {v} -> {'CONFIRMED' if ok else ('NEITHER' if ok is None else 'FALSIFIED')}")
    print(f"(3Q26 net take {take:.2f}% against 2Q26 {BASE2['goto_net_take_2q26_pct']}%; revenue YoY {rev:.1f}%)")
    return out

if __name__ == "__main__":
    a = [float(v) for v in sys.argv[1:]]
    score(*a) if len(a) >= 2 else print(__doc__)
