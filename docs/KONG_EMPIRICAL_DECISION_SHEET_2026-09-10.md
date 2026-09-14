# Invisible Ledger — empirical decision sheet for advisor review

**Status:** data/sample review only. This document does not propose a manuscript rewrite and does not state that any candidate sample has been approved.

## 1. Why this review is different from the earlier FY2023 file

The FY2023 three-case construction is source-auditable but one year is insufficient for the master's thesis. The current repository now contains longitudinal direct issuer/segment candidates, conditional country reconstructions, official BPS business/statistical evidence, ASEAN corroboration, and a separate global issuer panel. These evidence families are not pooled into one `N`.

## 2. Certified Indonesia observation status

The historical 14-period direct-candidate headline included an invalid Tokopedia FY2021 period match. After hard exclusion:

- **13 direct annual candidate periods** remain across Blibli 3P, Bukalapak Group, and Tokopedia;
- **12** have positive revenue denominators;
- the original Indonesia extension retains **8** observations, not 9;
- **6** of those 8 are conditional Grab/Shopee country reconstructions;
- **2** are direct Tokopedia segment observations.

Hard exclusions:

- **Tokopedia FY2021:** full-year pro-forma transaction value paired with non-equivalent-period/post-acquisition revenue.
- **Bukalapak FY2024:** 9-month TPV paired with 12-month revenue.

Full row-level review table: `data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv`.

## 3. Candidate sample boundaries requiring advisor choice

| Candidate boundary | Annual observations | Adjacent valid transitions | Opposite-sign transitions | Main strength | Main limitation |
|---|---:|---:|---:|---|---|
| Strict explicit Indonesia country pair | 0 | 0 | 0 | Highest geographic purity | Infeasible from current direct issuer disclosures |
| Tokopedia e-commerce segment only | 2 | 1 | 1 | Strongest Indonesia-aligned direct pair | Too narrow alone |
| Tokopedia + Blibli 3P | 9 | 6 | 3 | Direct multi-year segment evidence; excludes Bukalapak mixed geography | Blibli 3P includes OTA/travel |
| Tokopedia + Blibli 3P + Bukalapak Group | 13 | 9 | 3 | Broadest direct candidate history | Bukalapak includes overseas operations; Blibli still mixed business perimeter |
| Grab/Shopee country reconstructions | 6 | 4 | 0 | Preserves original country-facing comparison | Model-dependent; should remain sensitivity/supporting evidence unless advisor says otherwise |

No boundary is presented as approved.

## 4. Longitudinal movement result under the broad direct-candidate construction

Across the **9** valid adjacent direct-candidate transitions:

- revenue growth exceeds transaction-activity growth in **6**;
- transaction growth exceeds revenue growth in **3**;
- **3** transitions have opposite signs;
- median absolute growth-rate divergence is **42.94 percentage points**.

The three sign reversals are:

- Blibli 3P FY2020→FY2021: activity +14.86%, net revenue −28.08%;
- Blibli 3P FY2024→FY2025: activity −1.89%, net revenue +12.07%;
- Tokopedia FY2022→FY2023: activity −8.90%, net revenue +53.20%.

This is a descriptive within-series result, not a pooled estimator. Its final thesis role depends on the accepted Blibli/Bukalapak scope boundary.

## 5. BPS national evidence now certified for descriptive channel comparison

Retained official national estimates:

- total e-commerce transaction value: **Rp1,100.87T (2023) → Rp1,288.93T (2024), +17.08%**;
- e-commerce businesses: **3,816,750 → 4,400,972, +15.31%**;
- implied nominal transaction value per estimated business: approximately **+1.54%**;
- financial-report ownership: **15.19% (2023)** and **17.15% (2024)** as separately published wave values.

BPS's transaction-value-by-sales-media sources also support:

- marketplace: **Rp200.68T → Rp203.58T, +1.45%**;
- non-marketplace: **Rp900.19T → Rp1,085.35T, +20.57%**.

These are national aggregate survey-estimate comparisons. They do not identify the same firms, productivity, causal channel substitution, tax compliance, or participant income.

The financial-report figures remain more guarded as a longitudinal behavioral result until exact questionnaire/population concordance is completed.

Source certification: `docs/BPS_CROSSWAVE_CERTIFICATION_2026-09-10.md`.

## 6. Supporting evidence kept separate from the Indonesia sample

- **ASEAN:** six separate country histories, institutional/tax heterogeneity, and publication-vintage revisions. No pooled ASEAN tax effect or common monetization rate.
- **Global issuers:** 48 matched issuer-years, 40 transitions, 29 clean-screened transitions, and 4 clean opposite-sign cases across eight platform business models. This corroborates transaction/revenue non-equivalence but is not a representative global sample.
- **Quarterly company panel:** 47 source-reconciled company/segment quarters; not Indonesia-only.
- **Investor/event evidence:** remains exploratory until event timing and contamination are closed.

## 7. Decisions requested

1. Is an **Indonesia-aligned business segment** acceptable when the issuer does not publish a literal country line?
2. May **Blibli 3P Retail** enter the main longitudinal design despite its OTA/travel component, or should it remain supporting mechanism evidence?
3. Should **Bukalapak Group** be excluded from the main Indonesia analysis because its Group perimeter includes overseas operations?
4. Should **Grab and Shopee country reconstructions** remain sensitivity cases only?
5. Should the BPS module remain independent official-statistics evidence, or should business-level BPS microdata be pursued before finalizing the design?

## 8. Pending the advisor decision

Do not advertise one final sample size. Keep direct, conditional, official-statistical, ASEAN, global, quarterly, and market-event evidence as separate modules. No manuscript reconstruction is proposed until the accepted Indonesia scope boundary is known.
