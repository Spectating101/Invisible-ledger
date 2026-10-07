"""EXPLORATORY (8 Oct 2026; data already seen): three cheap checks for H2, using the licensed BPS files (national weighted totals only).
1. Where the extra pre-2023 sellers were counted: sellers who started selling online by 2022, by channel, in the 2022 vs 2023 surveys.
   (The channel question is worded "promotion and/or sales" in the 2023 file and "sales" in the 2024 file; cohort totals do not depend on it.)
2. Size of new vs older sellers: annual revenue bracket by start cohort (2023 file, year 2022).
3. Financial statements by start cohort in both surveys (same cohort compared across surveys).
Run: python3 bps_h2_cheap_checks.py --f2023 B.dbf --f2024 C.dbf -> tables/bps_h2_cheap_checks.json"""
import argparse, json
from bps_microdata_tests import read_dbf, num

x_ = argparse.ArgumentParser(); x_.add_argument("--f2023"); x_.add_argument("--f2024"); x = x_.parse_args()
a, b = read_dbf(x.f2023), read_dbf(x.f2024)
wa, sa = num(a["w_usaha_fi"]), num(a["r305"]); wb, sb = num(b["w_final"]), num(b["r307"])
mka, mkb = num(a["r307e"]) == 1, num(b["r309e"]) == 1
only_chat_a = ((num(a["r307c"]) == 1) | (num(a["r307d"]) == 1)) & ~mka & (num(a["r307a"]) != 1)
only_chat_b = ((num(b["r309c"]) == 1) | (num(b["r309d"]) == 1)) & ~mkb & (num(b["r309a"]) != 1)
out = {"cohort_started_by_2022_by_channel_k": {}}
for lab, ma, mb in [("marketplace users", mka, mkb), ("no marketplace", ~mka, ~mkb), ("chat or social only", only_chat_a, only_chat_b)]:
    p, q = float(wa[ma & (sa <= 2022)].sum()) / 1e3, float(wb[mb & (sb <= 2022)].sum()) / 1e3
    out["cohort_started_by_2022_by_channel_k"][lab] = {"2022_survey": p, "2023_survey": q, "change_pct": 100 * (q / p - 1)}
cat = num(a["kategori_p"]); out["revenue_bracket_by_cohort_2022_pct"] = {}
for lab, m in [("started 2022", sa == 2022), ("started 2020-21", (sa >= 2020) & (sa <= 2021)), ("started before 2020", sa < 2020)]:
    tot = float(wa[m].sum())
    out["revenue_bracket_by_cohort_2022_pct"][lab] = {k: 100 * float(wa[m & (cat == i)].sum()) / tot for i, k in enumerate(["<300m", "300m-2.5bn", "2.5-50bn", ">50bn"], 1)}
ra, rb = num(a["r306"]), num(b["r308"]); out["financial_statements_by_cohort_pct"] = {}
for lab, w, s, r, m in [("2022 survey, started 2022", wa, sa, ra, sa == 2022), ("2022 survey, started before 2020", wa, sa, ra, sa < 2020),
                        ("2023 survey, started 2023", wb, sb, rb, sb == 2023), ("2023 survey, started 2020-22", wb, sb, rb, (sb >= 2020) & (sb <= 2022)),
                        ("2023 survey, started before 2020", wb, sb, rb, sb < 2020)]:
    out["financial_statements_by_cohort_pct"][lab] = 100 * float(w[m & (r == 1)].sum()) / float(w[m].sum())
s = json.dumps(out, indent=1); print(s); open("tables/bps_h2_cheap_checks.json", "w").write(s)
