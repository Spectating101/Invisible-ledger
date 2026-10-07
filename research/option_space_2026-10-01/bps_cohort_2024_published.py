"""EXPLORATORY (8 Oct 2026): the cohort check for 2023 -> 2024, from published figures (no new microdata).
2024 side: BPS Statistik E-Commerce 2024, Appendix 12 (share of e-commerce businesses by year they started e-commerce, Indonesia row:
<2020 33.66%, 2020-2022 37.55%, >=2023 28.79%; read from the page image, OCR of the table body matched), times the published 2024 count 4,400,972.
2023 side: the same cohorts in the 2024 survey file (year 2023), national weighted totals from tables/bps_cohort_check.json.
A cohort that shrinks is consistent with a stable survey population (sellers stop); one that grows means newly counted existing sellers.
Run: python3 bps_cohort_2024_published.py -> tables/bps_cohort_2024_published.json"""
import json

N_2024 = 4_400_972
SHARE_2024 = {"before 2020": 33.66, "2020-2022": 37.55, "2023 or later": 28.79}
c = json.load(open("tables/bps_cohort_check.json"))["cohort_counts_thousands"]
y23 = {k: v["2023"] for k, v in c.items()}       # thousands, 2024 survey file (year 2023)
in_2023 = {"before 2020": y23["up to 2015"] + y23["2016-17"] + y23["2018-19"],
           "2020-2022": y23["2020"] + y23["2021"] + y23["2022"],
           "2023": y23["2023"]}
in_2024 = {k: N_2024 * s / 100 / 1e3 for k, s in SHARE_2024.items()}
out = {"cohorts_2023_survey_k": in_2023, "cohorts_2024_published_k": in_2024,
       "change_before_2020_pct": 100 * (in_2024["before 2020"] / in_2023["before 2020"] - 1),
       "change_2020_2022_pct": 100 * (in_2024["2020-2022"] / in_2023["2020-2022"] - 1),
       "published_rise_2023_2024_k": (N_2024 - 3_816_750) / 1e3,
       "min_entrants_2024_k": in_2024["2023 or later"] - in_2023["2023"],
       "note": "min_entrants_2024 assumes every 2023 starter was still selling in 2024; any exits among them raise it."}
s = json.dumps(out, indent=1); print(s); open("tables/bps_cohort_2024_published.json", "w").write(s)
