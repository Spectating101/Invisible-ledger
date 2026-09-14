# Empirical push status — 10 September 2026

This note records the stopping point of the current non-Box lane. It is dataset-first work only; no manuscript reconstruction has been performed.

## Completed in this lane

- Hard-enforced Tokopedia FY2021 and Bukalapak FY2024 exclusions.
- Non-pooled adjacent-year transaction-activity vs recognized-revenue analysis.
- Mechanism reconciliations for Tokopedia and Blibli, with unresolved cases left unresolved.
- Alternative sample-boundary sensitivity table.
- Certified candidate census overlay preserving historical audit fields.
- Corrected advisor-facing headline counts (13 direct candidates; 12 positive-denominator; 8 retained Indonesia-extension periods).
- BPS province geography cleanup (38 actual provinces; 36 complete matched provinces).
- BPS 2023 business-count series resolution using later official 15.30% growth consistency while preserving the conflicting source passage.
- BPS wave/microdata timing review: located 2024 survey is economic-reference-year 2023.
- Indonesia visibility matrix with observer-specific evidence states.
- Sample-scope certification for Tokopedia, Blibli, Bukalapak, Grab and Shopee.
- Kong-facing empirical review and decision-sheet generator.
- Advisor package index.

## Empirical findings currently reproducible

- 9 adjacent direct-candidate transitions; 3 opposite-sign activity/revenue movements; median absolute growth-rate gap 42.94pp.
- Tokopedia FY2022→FY2023: activity -8.90%, net revenue +53.20%; existing reconciliation assigns 60.56% of the arithmetic net-revenue increase to lower customer incentives.
- Blibli 3P FY2024→FY2025: TPV -1.89%, net revenue +12.07%, GPBD +13.93%; issuer documents margin/mix and efficiency explanation.
- BPS total nominal e-commerce transaction value 2023→2024: +17.08% from retained published totals.
- Marketplace-component growth ~+1.42% remains conditional pending exact cross-wave source-definition certification.
- E-commerce business count 2023→2024: +15.31% using 3,816,750→4,400,972, consistent with later official 15.30% statement.

## Remaining gates that cannot be settled unilaterally

1. Advisor acceptance of the Indonesia-aligned business-scope boundary:
   - Tokopedia only;
   - Tokopedia + Blibli 3P;
   - or Tokopedia + Blibli 3P + Bukalapak Group.
2. Exact 2023/2024 BPS marketplace-decomposition wording/denominator concordance.
3. Exact cross-wave financial-report item/population concordance before promoting a trend.
4. Whether to acquire the licensed reference-year-2023 BPS business microdata.
5. Box-owned ASEAN/global external-validity work and its later integration into the empirical review.

## Current branch/CI

Branch: `research/issuer-movement-bridge-20260910`  
Draft PR: #3  
The final workflow merges this branch against current main, runs all movement/mechanism/review tests, regenerates outputs twice, diffs them, and uploads the computed empirical bundle.
