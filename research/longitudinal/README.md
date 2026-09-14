# Longitudinal empirical development

Working branch: `research/longitudinal-review-20260909`.
Input baseline: `c2bced48df1cd7a968267d75bda0dfd046012c08`.

This branch converts seven existing CSV inventories into a reviewable longitudinal ledger and paper-facing tables. It does not change original data, manuscripts, the proposed Indonesia geography, or the main branch. It is not a declaration that the final thesis sample is adequate or approved.

## Reproduce

From the repository root, using Python 3.10 or later and the standard library:

```sh
python -m unittest discover -s tests -p 'test_*longitudinal*.py' -v
python scripts/analysis/paper_review_tables.py --output build/longitudinal
```

Use `paper_review_tables.py` for the complete reviewed output. It invokes `reviewed_longitudinal.py`, which applies the explicit source-review overlay. `longitudinal_review.py` supplies parsing and normalization helpers; its standalone output is an UNREVIEWED inventory and must not be used as final analytical data.

GitHub Actions runs tests, generates the tables twice and compares their contents, verifies that `data/` and `sources/` were not changed, and publishes the `longitudinal-review` artifact. Computational success does not clear geographic or economic comparability.

## What to read

- `coverage.csv`: distinct periods by issuer, business scope and frequency, with basis variants and conflicts separately counted.
- `paper_blibli_3p_annual.csv`: seven selected annual 3P records, including a negative 2019 denominator; release choices and original record identifiers are explicit.
- `paper_blibli_3p_changes.csv`: three adjacent-year comparisons printed in the same releases, rather than a silently spliced vintage series.
- `empirical_section.md`: generated draft empirical text and tables for the paper.
- `review_changes.csv`: ten period relabelings and five recovered source records.
- `rollup_checks_before.csv` and `rollup_checks_after.csv`: arithmetic checks against half-year, nine-month and annual figures, not independent empirical tests.
- `value_conflicts.csv` and `OPEN_SOURCE_ISSUES.csv`: unresolved reporting-vintage and eligibility issues.
- `input_hashes.csv`: exact input-file lineage; all old records also remain in `source_records_original.csv`.

The four source-vintage conflicts remain in the results by design. Tests assert that the pipeline detects rather than hides them.

## Source error corrected in the review layer

Blibli's Q1 2023 release table starts with FY2022, then Q1 2023, then Q1 2022. The original two-period extractor assigned the first column to Q1 2023 and the second to Q1 2022, omitting the third. `blibli_q123_source_review.csv` records the original labels, corrected labels, exact expected values, source page, and reason.

For 3P retail specifically:

| Period | TPV (IDR billion) | Net revenue (IDR billion) |
|---|---:|---:|
| FY2022 | 37,050 | 199 |
| Q1 2023 | 13,316 | 275 |
| Q1 2022 | 5,632 | 40 |

These are directly reported columns, not quarters inferred by division or interpolation. The corrected 3P quarterly observations reconcile with the available 2022 and 2023 cumulative and annual figures within rounding tolerance. Source: https://asset-about.blibli.com/2023/05/Earnings-Release-1Q23-PT-Global-Digital-Niaga-Tbk.pdf, p.2; Q1 2022 3P TPV and revenue are also repeated in the narrative.

Across all five Blibli scope categories, the tested above-tolerance rollup residuals fall from 90 to two. That count consists of repeated arithmetic checks, not 90 independent errors. The two surviving checks concern FY2023 TPV for Group and Institutions. Four Q4 2024 scope/vintage TPV conflicts also remain unresolved.

## What the coverage now means

Blibli 3P has seven annual years (2019-2025) and fifteen distinct quarterly periods in the selected extracts. Those overlap and must not be added. Q4 2024 has an unresolved competing TPV value; Q4 2021 revenue rounds to zero; 2019 annual revenue is negative. The quarterly records contain a continuous 2022Q1-2023Q4 block but not a complete subsequent quarterly history.

Bukalapak has four period-matched annual Group candidates, 2020-2023; its FY2024 9M/12M pair is excluded. The original FY2021 Tokopedia mismatch is also excluded. Existing Grab/Sea/GoTo company histories remain company-wide; the country allocations remain conditional rather than becoming directly observed through normalization.

The Blibli annual table is a selected-vintage display, not a certification that every original and subsequent filing agrees. In particular, the original FY2023 release's 49,917 3P TPV differs from the 49,912 comparative used in the FY2024-release pair. That original-release variant is not present in the seven reviewed CSV inputs; it is separately flagged rather than declared resolved by the four-conflict count.

## Paper-development sequence

1. Resolve the recorded source issues and recover the missing matched periods without changing geography by default.
2. Establish the strongest consistent longitudinal main series, with a separate inclusion decision for commerce/travel, overseas operations, gross/net revenue, and reporting breaks.
3. Use the generated within-release growth comparisons together with the existing Tokopedia revenue/incentive reconciliation. Explain actual changes in operating scale and recognized revenue; do not treat the ratio identity as a statistical discovery.
4. Update the manuscript from those admitted tables. Do not create another FY2023-only main design or count supporting market/macro rows as platform observations.

This branch supplies a tested empirical-development layer and a draft results section, not a finished replacement thesis. The existing pending decisions on geographic scope, time coverage and substantive sufficiency remain open.
