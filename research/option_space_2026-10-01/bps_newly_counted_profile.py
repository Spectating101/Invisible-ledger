"""EXPLORATORY (8 Oct 2026; designed after the cohort and rise-accounting checks, data already seen): who are the ~306 thousand
pre-2023 online sellers that the 2023 survey counts above the whole 2022 count?
No business ID links the surveys, so the profile is a difference of weighted counts: for each group g,
  surplus(g) = [2023 survey (2024 file): sellers who started selling online by 2022, in g] - [2022 survey (2023 file): all sellers, in g].
It is net of exits (sellers who stopped in 2023 lower it); if exits are not even across groups, the split shifts with them.
Traits that change with time are aligned: age is compared one year on; business size and online share can change between years.
Codes: 2023 file from its layout and questionnaire; the 2024 file has no layout here, and its education codes (6) are mapped to the
2023 file's four groups by matching shares (1-3 up to high school, 4 diploma, 5 bachelor, 6 postgraduate), so education is labelled inferred.
Licensed inputs are not committed; output is national weighted totals only.
Run: python3 bps_newly_counted_profile.py --f2021 A.dbf --f2023 B.dbf --f2024 C.dbf -> tables/bps_newly_counted_profile.json"""
import argparse, json
import numpy as np
from bps_microdata_tests import read_dbf, num

x_ = argparse.ArgumentParser(); x_.add_argument("--f2021"); x_.add_argument("--f2023"); x_.add_argument("--f2024"); x = x_.parse_args()
a, b = read_dbf(x.f2023), read_dbf(x.f2024)
wa, wb = num(a["w_usaha_fi"]), num(b["w_final"])
sa, sb = num(a["r305"]), num(b["r307"])
pre = sb <= 2022            # 2023 survey, started selling online by 2022
ent = sb == 2023            # 2023 survey, started selling online in 2023
JAVA = {31, 32, 33, 34, 35, 36}


def groups_a():
    age = num(a["r301b"]) + 1                       # one year on, to compare with the 2023 survey
    edu = num(a["r301d"])
    tk = num(a["r303a_1"]) + num(a["r303a_2"]) + num(a["r303b_1"]) + num(a["r303b_2"])
    opened, online = num(a["r304"]), sa
    off = num(a["r310a"])
    chat_only = ((num(a["r307c"]) == 1) | (num(a["r307d"]) == 1)) & (num(a["r307e"]) != 1) & (num(a["r307a"]) != 1)
    return dict(age=age, edu=edu, tk=tk, opened=opened, online=online, off=off, sex=num(a["r301c"]),
                prov=num(a["prov"]), sector=np.array(a["r302a"]), chat_only=chat_only, records=num(a["r306"]) == 1)


def groups_b():
    e = num(b["r301d"]); edu = np.where(e <= 3, 1, e - 2)
    chat_only = ((num(b["r309c"]) == 1) | (num(b["r309d"]) == 1)) & (num(b["r309e"]) != 1) & (num(b["r309a"]) != 1)
    return dict(age=num(b["r301b"]), edu=edu, tk=num(b["total_tk"]), opened=num(b["r306"]), online=sb, off=num(b["r313a"]),
                sex=num(b["r301c"]), prov=num(b["prov"]), sector=np.array(b["r302b"]), chat_only=chat_only, records=num(b["r308"]) == 1)


A, B = groups_a(), groups_b()
SECT = {"G": "trade", "I": "food and lodging", "C": "making goods", "S": "personal services", "H": "transport"}
DEFS = {
    "owner sex": lambda g: {"man": g["sex"] == 1, "woman": g["sex"] == 2},
    "owner age": lambda g: {"under 30": g["age"] < 30, "30-39": (g["age"] >= 30) & (g["age"] < 40),
                            "40-49": (g["age"] >= 40) & (g["age"] < 50), "50 and over": g["age"] >= 50},
    "owner education (2023 survey codes inferred)": lambda g: {"high school or less": g["edu"] == 1, "diploma": g["edu"] == 2,
                                                              "bachelor": g["edu"] == 3, "postgraduate": g["edu"] == 4},
    "sector": lambda g: {**{v: g["sector"] == k for k, v in SECT.items()}, "other": ~np.isin(g["sector"], list(SECT))},
    "island": lambda g: {"Java": np.isin(g["prov"], list(JAVA)), "outside Java": ~np.isin(g["prov"], list(JAVA))},
    "business opened": lambda g: {"before 2010": g["opened"] < 2010, "2010-2017": (g["opened"] >= 2010) & (g["opened"] <= 2017),
                                  "2018-2022": (g["opened"] >= 2018) & (g["opened"] <= 2022)},
    "years between opening and selling online": lambda g: {"same year or 1": (g["online"] - g["opened"]) <= 1,
                                                           "2-5": ((g["online"] - g["opened"]) >= 2) & ((g["online"] - g["opened"]) <= 5),
                                                           "6 or more": (g["online"] - g["opened"]) >= 6},
    "share of sales made online": lambda g: {"under 25%": (100 - g["off"]) < 25, "25-74%": ((100 - g["off"]) >= 25) & ((100 - g["off"]) < 75),
                                             "75% or more": (100 - g["off"]) >= 75},
    "channel": lambda g: {"chat or social only": g["chat_only"], "other": ~g["chat_only"]},
    "keeps financial statements": lambda g: {"yes": g["records"], "no": ~g["records"]},
}

out = {"note": "thousands of sellers, weighted; surplus = 2023-survey pre-2023 sellers minus the whole 2022 count, net of exits",
       "totals_k": {"count_2022": float(wa.sum()) / 1e3, "pre_2023_in_2023_survey": float(wb[pre].sum()) / 1e3,
                    "surplus": float(wb[pre].sum() - wa.sum()) / 1e3, "entrants_2023": float(wb[ent].sum()) / 1e3},
       "size_check": {"2022 survey, share with 1 worker (owner only)": 100 * float(wa[A["tk"] == 1].sum() / wa.sum()),
                      "2023 survey total_tk == 0 share": 100 * float(wb[B["tk"] == 0].sum() / wb.sum()),
                      "2023 survey total_tk == 1 share": 100 * float(wb[B["tk"] == 1].sum() / wb.sum())},
       "profile": {}}
S = out["totals_k"]["surplus"]
for name, f in DEFS.items():
    ga, gb = f(A), f(B); rows = {}
    for k in ga:
        n22 = float(wa[ga[k]].sum()) / 1e3; n23 = float(wb[pre & gb[k]].sum()) / 1e3; ne = float(wb[ent & gb[k]].sum()) / 1e3
        rows[k] = {"counted_2022_k": round(n22, 1), "pre2023_in_2023_k": round(n23, 1), "surplus_k": round(n23 - n22, 1),
                   "change_pct": round(100 * (n23 / n22 - 1), 1) if n22 else None,
                   "share_of_2022_count_pct": round(100 * n22 / out["totals_k"]["count_2022"], 1),
                   "share_of_surplus_pct": round(100 * (n23 - n22) / S, 1),
                   "share_of_2023_entrants_pct": round(100 * ne / out["totals_k"]["entrants_2023"], 1)}
    out["profile"][name] = rows

# Control: the same comparison for the stable period. Sellers who started selling online by 2020, in the 2020 survey (2021 file)
# vs the 2022 survey (2023 file), two years apart (age aligned by two years). Normal survey-to-survey change is exits only, so the
# question is whether the 2022-23 tilt by group also appears when coverage was steady.
if x.f2021:
    c = read_dbf(x.f2021); wc, sc = num(c["w_usaha_fi"]), num(c["r305"])
    C = dict(age=num(c["r301b"]) + 2, edu=num(c["r301d"]), opened=num(c["r304"]), online=sc, sex=num(c["r301c"]),
             prov=num(c["prov"]), sector=np.array([v[:1] for v in c["r302b"]]))
    A2 = {**A, "age": A["age"] - 1}           # 2022 survey ages as reported (no shift) for the two-year comparison
    by20_c, by20_a = sc <= 2020, sa <= 2020
    tot_c, tot_a = float(wc[by20_c].sum()), float(wa[by20_a].sum())
    out["control_2020_to_2022"] = {"all_change_pct": round(100 * (tot_a / tot_c - 1), 1), "groups": {}}
    out["break_2022_to_2023_all_change_pct"] = round(100 * (float(wb[pre].sum()) / float(wa.sum()) - 1), 1)
    for name in ["owner sex", "owner age", "owner education (2023 survey codes inferred)", "sector", "island", "business opened",
                 "years between opening and selling online"]:
        gc, ga = DEFS[name](C), DEFS[name](A2); rows = {}
        for k in gc:
            n0, n1 = float(wc[by20_c & gc[k]].sum()), float(wa[by20_a & ga[k]].sum())
            rows[k] = {"2020_survey_k": round(n0 / 1e3, 1), "2022_survey_k": round(n1 / 1e3, 1),
                       "change_pct": round(100 * (n1 / n0 - 1), 1) if n0 else None}
        out["control_2020_to_2022"]["groups"][name] = rows
        # Beyond normal: expected 2023 count = 2022 count x the group's own yearly change in the stable period (two-year change, annualised)
        ex = {}
        for k in gc:
            r = rows[k]; n22 = out["profile"][name][k]["counted_2022_k"]; n23 = out["profile"][name][k]["pre2023_in_2023_k"]
            yearly = (1 + r["change_pct"] / 100) ** 0.5
            ex[k] = n23 - n22 * yearly
        tot = sum(ex.values())
        for k in gc:
            out["profile"][name][k]["beyond_normal_k"] = round(ex[k], 1)
            out["profile"][name][k]["share_of_beyond_normal_pct"] = round(100 * ex[k] / tot, 1)

s = json.dumps(out, indent=1); print(s); open("tables/bps_newly_counted_profile.json", "w").write(s)
