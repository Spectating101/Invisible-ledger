# Licensed data: what is kept off the repository, and what the repository holds in its place (12 Oct 2026)

Three sources are used under data-use terms and are **never committed**: BPS survey microdata, LSEG market values and World Bank Enterprise Surveys. They sit on the researcher's machine in `_local/licensed_data/` (git-ignored). This note records what each file is, how to check a copy against the one used (size and SHA-256), which scripts read it, and which committed files carry its results. With it, the thesis can be understood and its numbers traced without the raw files, and the raw files can be re-obtained and verified.

## 1. BPS e-commerce survey microdata (SILASTIK)

Bought from BPS-Statistics Indonesia through SILASTIK in October 2026 under a signed data-use statement (SPPD). Duties: no sharing of copies; cite BPS as the source; give BPS a copy of the thesis; non-commercial use; a new request before any use outside the thesis.

| File (as delivered) | Survey round | Activity year | Rows | Variables | Bytes | SHA-256 |
|---|---|---|---|---|---|---|
| `716 Survei E-commerce 2021/survei_ecommerce_2021.dbf` | Survei E-Commerce 2021 | 2020 | 11,848 | 64 | 4,528,017 | 80a7145fe0a5d24b5ed9cf80d7eb41dd2d2d96a71a6a53ab04d82bcb0352f355 |
| `Data/ecom2023.dbf` | Survei E-Commerce 2023 | 2022 | 31,724 | 54 | 13,706,530 | ed9ec5243deeff75121d08811c1c1ee610b85304c0633099f652170f4d43222c |
| `e_commerce2024.dbf` | Survei Usaha/Perusahaan E-Commerce 2024 | 2023 | 39,736 | 172 | 9,343,498 | b58ed340fcb39d04b4d0aa145ac3e433fc38853227d092402ac3801a37cea43f |

Delivered with them: the 2021 questionnaire and metadata sheet, the 2023 questionnaire and layout sheet. The 2024 file came without a layout; its variable meanings were matched to the 2023 layout by position and value patterns (documented in the scripts).

**What the files contain.** One row per surveyed business that sold online in the activity year, with a survey weight (`w_usaha_fi` in the 2021 and 2023 files, `w_final` in the 2024 file). Weighted totals reproduce BPS's published counts (2,361,423 for 2020; 2,995,986 against 2,995,879 for 2022; 3,814,799 against 3,816,750 for 2023). Variables used in the thesis:

| What | 2023 file (2022 activity) | 2024 file (2023 activity) |
|---|---|---|
| Province | `prov` | `prov` |
| Owner's age, sex, education | `r301b`, `r301c`, `r301d` | `r301b`, `r301c`, `r301d` (education on a six-level code) |
| Sector | `r302a` | `r302b` |
| Workers | `r303a_*`, `r303b_*` | `total_tk` |
| Year the business opened | `r304` | `r306` |
| Year it started selling online | `r305` | `r307` |
| Keeps financial statements | `r306` | `r308` |
| Channels (website, email, chat, social media, marketplace) | `r307a` to `r307e` | `r309a` to `r309e` |
| Months of online selling | `r308` (list of months) | `r311_jan` to `r311_des` |
| Revenue bracket | `kategori_p` | not released |
| Share of sales offline / marketplace / other online | `r310a`, `r310b`, `r310c` | `r313a`, `r313b`, `r313c` |
| Online sales vs previous year | `r312` | `r315`, `r315b` |
| Main obstacle | `r325` | `r325` |

No business identifier links the rounds, and the files carry no area or sample-design variables below province.

**Scripts that read these files and the committed results.**

| Script | Committed output (national totals only) | Used for |
|---|---|---|
| `bps_microdata_tests.py` | `tables/bps_microdata_results.json` | Data checks; registered tests E1-E8 (entry test = E5) |
| `bps_descriptives.py` | `tables/bps_descriptives.json` | Marketplace use, records, sellers' reported change |
| `bps_cohort_check.py`, `bps_rise_accounting.py` | `tables/bps_cohort_check.json`, `tables/bps_rise_accounting.json` | The 2023 rise: first-time entry vs sellers already selling |
| `bps_frame_check.py` | `tables/bps_frame_check.json` | Count growth vs survey size by province |
| `bps_h2_cheap_checks.py`, `gel_checks.py` | `tables/bps_h2_cheap_checks.json`, `tables/gel_checks.json` | Channel, cohort and value checks |
| `bps_newly_counted_profile.py` | `tables/bps_newly_counted_profile.json` | Who the extra sellers were |
| `bps_returning_check.py` | `tables/bps_returning_check.json` | Part-year selling (returning-seller check) |
| `part5_checks.py`, `part6_checks.py`, `rq_closing_checks.py` | `tables/part5_checks.json`, `tables/part6_checks.json`, `tables/rq_closing_checks.json` | Channel shares, tax reach, sampling-error check |

Narrative and limits: `PART4_H2_GROUNDWORK.md`, `PART5_OBJ3_GROUNDWORK.md`, `PART6_WHY_IT_MATTERS_GROUNDWORK.md`; tests registered in `PREREGISTRATION.md` before the files were opened (commit `26ab2cf`, 2 Oct; results commit `365ef96`, 7 Oct).

## 2. LSEG market values

Pulled from LSEG (Refinitiv) under the university licence on 8 Oct 2026, after the market test was registered (commit `ab24063`).

| File | Content | Bytes | SHA-256 |
|---|---|---|---|
| `lseg/mcap_reporting_ccy.csv` | Year-end market value in reporting currency by firm (firm, RIC, currency, date, value), 334 rows | 14,616 | dff6ad347f227407704fa16ca207e2fb3fd0fa7206e668824c8234487a21de87 |
| `lseg/mcap_annual_2019_2025.csv` | Annual market values 2019-2025, 126 rows | 8,529 | 149fcfedf5b2e9181816391944b93fc924fa3f7e017e48d53da3e40c42cb3986 |

Read by `m1_market_value.py` (path passed as an argument). Committed result: `tables/m1_market_value_results.json` (coefficients and test statistics only, 28 firms and 138 firm-years in the main sample). Narrative: Part 3 dated note; `PREREGISTRATION.md` M1-M2. The event-study scripts (`event_study*.py`) use licensed prices and stay exploratory.

## 3. World Bank Enterprise Surveys

Downloaded from enterprisesurveys.org under the World Bank's access terms (registration; no redistribution). Used: the Indonesia 2023 enterprise survey and informal-sector survey (`WBES_Indonesia2023_Data/Indonesia-2023-full-data.dta`, `WBES-IS_Indonesia2023_Data/Indonesia-2023-ISES-full-data.dta`), and a cross-country custom query for the seven-country comparison. Local copies in `_local/licensed_data/wbes/` hold the custom query (`CustomQuery-FormalSectorWBES-Oct-2-2026.xlsx`, 3,612,785 bytes, SHA-256 c8c5a6a90dde5e88f673f13264b3a0bd5a899271c9f5b2083be6b78de3d59328) and country downloads for Viet Nam, Thailand, the Philippines, Malaysia and Cambodia.

Read by `wb_tests.py` and `wb_crosscountry.py`. Committed results: `tables/wb_tests_results.json` and `tables/wb_crosscountry.csv`, used for the "formal firms with neither a website nor online tax filing" comparison. Registered tests W1-W3 and F1-F3 in `PREREGISTRATION.md`.

## What a reader without the raw files can and cannot do

- **Can:** read every result, see the test that produced it and when it was registered, rebuild all tables that depend only on committed inputs (`rebuild_all.sh`, 272 ledger checks), and inspect the national totals each licensed script produced.
- **Cannot:** rerun the scripts listed above. To do so, obtain the files from the source (SILASTIK for BPS, LSEG for market values, enterprisesurveys.org for the World Bank files), check the size and SHA-256 against this note, and pass the paths to the scripts as shown in their headers.
- **Backup:** the raw files exist only on the researcher's machine. A private offline copy is advisable; they must not go to shared or public storage.
