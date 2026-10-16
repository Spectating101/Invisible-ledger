"""H2 after the entry test (exploratory, 16 Oct 2026, designed after all results were known). Built only from committed tables.
Question: if the 2023 seller count not explained by first-time entry is treated as wider survey coverage, how much of BPS's
2022-23 value growth would more businesses account for (the split of equation (7), H2's threshold 50 percent)?
Two treatments: (a) remove the extra sellers from the count only (their sales stay in the total, which raises sales per business);
(b) remove them from the count and remove their sales, using the chat-and-social seller size from gel_checks.json (consistent
treatment: coverage adds both count and value). The value of the 458k scenario scales the 306k value in proportion (assumption)."""
import json, math, pathlib
T = pathlib.Path(__file__).parent / "tables"
acc = json.load(open(T / "bps_rise_accounting.json"))
gel = json.load(open(T / "gel_checks.json"))
V22, V23 = 783.0, 1100.87                  # BPS published online sales value, Rp trillion (Statistik E-Commerce 2023)
C22, C23 = 2_995_879, 3_816_750            # BPS published counts of businesses (C22 implied by the published 27.40 percent growth)
share = lambda c, v: 100 * math.log(c / C22) / math.log(v / V22)
out = {"published": {"count_growth_pct": 100 * (C23 / C22 - 1), "value_growth_pct": 100 * (V23 / V22 - 1), "extensive_share_pct": share(C23, V23)},
       "scenarios": {}}
base_k = acc["scenarios"]["no_exits"]["newly_counted_k"]
for name in ("no_exits", "reference"):
    k = acc["scenarios"][name]["newly_counted_k"]
    c = C23 - k * 1e3
    row = {"extra_sellers_removed_k": k, "adjusted_count_growth_pct": 100 * (c / C22 - 1),
           "count_only_extensive_share_pct": share(c, V23), "count_and_value": {}}
    for s, v in gel["newly_counted_value_scenarios"].items():
        val = v["value_added_tn"] * k / base_k
        row["count_and_value"][s] = {"value_removed_tn": val, "adjusted_value_growth_pct": 100 * ((V23 - val) / V22 - 1),
                                     "extensive_share_pct": share(c, V23 - val)}
    out["scenarios"][name] = row
json.dump(out, open(T / "h2_coverage_adjusted.json", "w"), indent=1)
for n, r in out["scenarios"].items():
    cv = [x["extensive_share_pct"] for x in r["count_and_value"].values()]
    print(f"{n}: remove {r['extra_sellers_removed_k']:.0f}k -> count-only {r['count_only_extensive_share_pct']:.1f}%, count and value {min(cv):.1f}-{max(cv):.1f}% (published {out['published']['extensive_share_pct']:.1f}%)")
