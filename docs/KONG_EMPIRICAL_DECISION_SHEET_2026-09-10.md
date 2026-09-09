# Invisible Ledger — empirical decision sheet for advisor review

**Status:** data/sample review only. No manuscript rewrite and no claim that any candidate sample is approved.

## 1. Certified Indonesia status

The FY2023 three-case construction is auditable but one year is insufficient. After hard exclusions:

- **13 direct annual candidate periods** remain across Blibli 3P, Bukalapak Group and Tokopedia;
- **12** have positive revenue denominators;
- the original Indonesia extension retains **8** observations, not 9;
- **6** of those are conditional Grab/Shopee country reconstructions and **2** are direct Tokopedia segment observations.

Hard exclusions:

- Tokopedia FY2021: period mismatch;
- Bukalapak FY2024: 9-month TPV vs 12-month revenue.

Row-level table: `data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv`.

## 2. Candidate sample boundaries

| Boundary | Levels | Valid adjacent transitions | Reversals | Limitation |
|---|---:|---:|---:|---|
| Strict explicit-country direct | 0 | 0 | 0 | infeasible with current disclosures |
| Tokopedia direct Indonesia-aligned segment | 2 | 1 | 1 | too narrow alone |
| Tokopedia + Blibli 3P | 9 | 6 | 3 | Blibli includes OTA/travel; FY2020 prospectus extension included |
| Tokopedia + Blibli + Bukalapak | 13 | 9 | 3 | Bukalapak Group includes overseas operations |
| Grab/Shopee conditional country reconstructions | 6 | 4 | 0 | model-dependent sensitivity only |

Box's first all-tier hypothesis execution is a separate **coverage diagnostic**: 17 retained levels and 12 transitions across all five series, with 2 sign reversals and median absolute divergence 42.02pp. It starts Blibli at FY2021 and includes conditional Grab/Shopee. The direct-candidate sensitivity above includes Blibli FY2020 from the prospectus and excludes conditional country series. Do not treat these as competing estimates.

## 3. BPS national results

Established/descriptive national evidence:

- total e-commerce value: **Rp1,100.87T (2023) → Rp1,288.93T (2024), +17.08%**;
- estimated businesses: **3,816,750 → 4,400,972, +15.31%**;
- implied nominal value per estimated business: **+1.54%**;
- marketplace component: **Rp200.68T → Rp203.58T, +1.45%**;
- non-marketplace component: **Rp900.19T → Rp1,085.35T, +20.57%**;
- financial-report ownership: **15.19% (2023)** and **17.15% (2024)** as published wave values.

The channel comparison is a national aggregate-estimate result, not a business panel or causal channel-substitution estimate. The financial-report trend remains guarded pending exact questionnaire/population concordance.

Box's broader aggregate decomposition also reports 2022→2023 total value +40.60%, businesses +27.40%, implied nominal value/business +10.36%; this is arithmetic, not causal entry/productivity evidence.

## 4. BPS province result

Province evidence does **not** establish a stable marketplace/financial-recordkeeping relationship. Box's executed results include 2024 Pearson `r≈0.022 (p≈0.897)` and 2023→2024 within-province Pearson `r≈0.309 (p≈0.066)`, Spearman `rho≈0.151 (p≈0.379)`, weighted `r≈0.099`. Business-level microdata or an official joint table is required for the individual-business hypothesis.

## 5. Supporting evidence kept separate

- ASEAN: six separate country histories with tax/platform heterogeneity and revision sensitivity; no pooled treatment effect.
- Global issuers: 48 matched issuer-years, 40 transitions, 29 clean-screened, 4 clean sign reversals; corroboration across business models, not a representative global sample.
- Quarterly company panel: 47 source-reconciled company/segment quarters; not Indonesia-only.
- Investor/event module: exploratory until timing and contamination are closed.

## 6. Decisions requested

1. Is an Indonesia-aligned segment acceptable without a literal country label?
2. May Blibli 3P enter despite OTA/travel, or should it remain supporting evidence?
3. Should Bukalapak Group be excluded from the main Indonesia analysis because of overseas scope?
4. Should Grab/Shopee country reconstructions remain sensitivity only?
5. Should BPS remain an official-statistics module or should business-level microdata be pursued before finalizing the design?

Pending these decisions, do not report one final sample size and do not reconstruct the manuscript.
