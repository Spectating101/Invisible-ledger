# The Invisible Ledger: empirical package

Replication materials for the master's thesis *The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy*
(Christopher Ongko, Yuan Ze University, College of Management; advisor Prof. De-Rong Kong). Built on {DATE}.

The package holds the code, every table the thesis reports, the inputs that come from public company filings and official statistics,
the dated registration of the tests, and the checks that tie each number in the thesis to a table. **It holds no licensed data.**

## 1. What you can rerun without any licensed file

```
bash research/option_space_2026-10-01/rebuild_all.sh
```

Needs Python 3.13 with `pandas`, `numpy`, `scipy`, `statsmodels` and `matplotlib` (tested with pandas 3.0, numpy 2.5, scipy 1.18, statsmodels 0.15,
matplotlib 3.11). It takes about three minutes. It rebuilds every table that depends only on the files in this package, then checks the claims
ledgers (`tables/claims_ledger*.csv`): every number the thesis quotes from these tables is recomputed and compared, one row per claim, with status PASS or
CHECK. On the build of {DATE} the run ended with {LEDGER_SUMMARY}.

The six thesis figures are drawn from the committed tables by `papers/thesis_2026-10/figures/make_figures.py` and `make_fig3_1.py`
(run from the package root).

## 2. What is in the package

| Folder | Content |
|---|---|
| `research/option_space_2026-10-01/*.py` | the analysis scripts, one per result or check (the header of each says what it reads and writes) |
| `research/option_space_2026-10-01/tables/` | every output table, as CSV or JSON, and the claims ledgers |
| `research/option_space_2026-10-01/tables/src/` | the extractions from public company filings and official statistics: each value with its source file and the quoted passage, and a `*_NOTES.txt` per source |
| `research/option_space_2026-10-01/tables/src/wdi_extraction.csv`, `bis_policy_extraction.csv`, `total_assets_extraction.csv`, `total_assets_manual.csv` | public inputs of the regressions (added 25 Oct 2026): World Bank WDI (CC BY 4.0), BIS central-bank policy rates, total assets from SEC filings, and total assets typed from published statements for six platforms that do not file with the SEC (each row names its source) |
| `data/`, `outputs/` | the thirteen input tables the rebuild reads (company-reported revenue and transaction value, published BPS national totals, World Bank context series), as they were when the tests were run |
| `research/option_space_2026-10-01/PREREGISTRATION.md` | the tests written down before the data were opened, with dates |
| `research/option_space_2026-10-01/LICENSED_DATA.md` | the three licensed sources, what each file is, its size and SHA-256, and which script reads it |
| `papers/thesis_2026-10/figures/` | the figure scripts and the six figures |
| `MANIFEST.csv` | every file in this package with its size and SHA-256 |

## 3. What is not in the package, and why

Three sources are used under data-use terms and are **not included and must not be shared**:

1. BPS e-commerce survey microdata (SILASTIK, rounds 2021, 2023 and 2024), under a signed data-use statement;
2. LSEG year-end market values and prices, under the university licence;
3. World Bank Enterprise Surveys files, under the World Bank's access terms (no redistribution).

The scripts that read them are in the package, so the method can be inspected, but they cannot be rerun here. Their outputs are in `tables/`: national totals,
shares and test results only, with no business-level record. `LICENSED_DATA.md` gives the file names, sizes and SHA-256 of the originals, so a reader
who obtains the same files from the source (SILASTIK, LSEG, enterprisesurveys.org) can check them and pass the paths to the scripts as their headers
show. The thesis cites BPS as the source of every survey figure, as the data-use agreement requires.

Also left out:

- **Firm-level announcement-return panels** (`event_study_panel.csv`, `event_study_surprise_panel.csv`). They are derived from licensed prices and
  consensus estimates. The announcement-return analysis is exploratory and not in the thesis text; its regression output is kept
  (`tables/event_study_panel_check.json`), and `rebuild_all.sh` skips the step that would re-estimate it when the panels are absent.
- **The market-value upgrade** (`m1_upgrade.py`, written 22 October). It needs the licensed LSEG files; its reading rules are fixed in `PREREGISTRATION.md`,
  and its results (`tables/m1_upgrade_results.json`) are not yet in this package.
- **The market-value regression in simple percentage changes.** The thesis keeps the registered log definition of that test; a version with simple changes needs the licensed LSEG values and has not been run.
- **The scoring of the registered predictions on the 2026 rules** (`score_q3_2026.py`, `score_q3_2026_goto_only.py`). The results they need
  (GoTo on 27 October 2026, BPS in early November, Grab and Sea in mid-November) were not published when this package was built.

## 4. Where each result of the thesis comes from

| Thesis result | Scripts | Main outputs |
|---|---|---|
| Wedge and ecosystem ratio, 2023 (Section 5.1, Table 5.1; Appendix B) | `build_numbers.py`, `wedge_over_time.py` | `tables/wedge_over_time.csv`, `tables/take_rate_levels.csv` |
| H1: size of take-rate changes, Indonesia against abroad (5.2; Appendix C) | `h1_extended.py`, `h1_thesis_drops.py`, `h1_points_vs_log.py`, `h1_quarterly.py`, `h1_regional_tier.py`, `h1_exact_inference.py` | `tables/h1_extended_results.json`, `h1_extended_firms.csv`, `h1_thesis_drops.json`, `h1_points_vs_log.json`, `h1_quarterly_results.json`, `h1_exact_inference.json` |
| What explains the wedge and the ecosystem ratio; H1 in growth rates (5.2, 5.3; Appendix C.3) | `build_regression_panel.py`, `kong_regressions.py`, `h1_simple_change.py`; public inputs fetched once by `fetch_wdi.py` and `fetch_total_assets.py` | `tables/regression_panel.csv`, `kong_results.json`, `kong_table_*.md`, `h1_simple_change.json` |
| The seven windows traced (5.3; Appendix B.3) | `growth_decomposition.py`, `h1_groundwork.py`, `blibli_discount_split.py`, `tokopedia_segment.py` | `tables/growth_decomposition.csv`, `tokopedia_segment.csv`, `h1_groundwork.json` |
| What markets valued (5.4) | `m1_market_value.py` (licensed LSEG) | `tables/m1_market_value_results.json` |
| Platforms against household spending (5.5); national figures (5.10) | `consistency_grid.py`, `three_rulers.py`, `yardsticks.py`, `bps_bridge.py` | `tables/consistency_grid_growth.csv`, `yardsticks_bi_bps.csv`, `bps_bridge.csv` |
| H2 and the entry test (5.6); the rise in the count and who the extra sellers were (5.7, 5.8) | `bps_microdata_tests.py`, `bps_rise_accounting.py`, `bps_cohort_check.py`, `bps_newly_counted_profile.py`, `bps_frame_check.py`, `bps_returning_check.py` (licensed BPS); `h2_coverage_adjusted.py`, `bps_cohort_2024_published.py` (rebuild here) | `tables/bps_microdata_results.json`, `bps_rise_accounting.json`, `bps_cohort_check.json`, `bps_newly_counted_profile.json`, `h2_coverage_adjusted.json` |
| Channels and records (5.9) | `bps_descriptives.py`, `part5_checks.py`, `wb_tests.py` (licensed) | `tables/bps_descriptives.json`, `part5_checks.json`, `wb_tests_results.json` |
| The 2026 rules and how far they reach (Chapter 6) | `part6_checks.py`, `tax_base_rulers.py`, `cap_prediction.py` | `tables/part6_checks.json`, `tax_base_rulers.csv` |
| Every number quoted in the thesis | `claims_ledger*.py` | `tables/claims_ledger*.csv` |

## 5. Notes

- The `Run:` lines in some script headers show the author's own environment; they do not matter here.
- `fetch_wdi.py` and `fetch_total_assets.py` need network access and were run once; `rebuild_all.sh` does not run them, and everything after them reads the committed files in `tables/src/`. Refetching can change the last values (the World Bank and the SEC revise series).
- The regressions of Sections 5.2 and 5.3 are exploratory. They use the same 32 platforms as the H1 test; `build_regression_panel.py` records every classification (type, main market, listing year) in `tables/platform_attributes.csv`.
- Some extraction tables in `tables/src/` were built once from a local corpus of filing text (`tokopedia_segment.py`, `mmyt_incentives.py`, `peers_quarterly.py`); their outputs are included, and each row carries its quoted source passage.
- Labels used in the thesis: a result is **registered** (written down and dated in `PREREGISTRATION.md` before the data were opened), **exploratory**
  (designed after some results were known) or **descriptive** (numbers without a test).
- Section 6.5 of the thesis and the scoring scripts are pending the 2026 releases named above.

Author: Christopher Ongko (王新福), College of Management, Yuan Ze University.
