# Indonesia longitudinal robustness — 10 September 2026

**Status:** empirical robustness addendum to the certified evidence and research synthesis. It does not choose the final sample, claim advisor approval, or reconstruct the manuscript.

## Why this check matters

The direct-candidate Indonesia-related issuer result contains large transaction-versus-revenue growth gaps, including an extreme Blibli FY2022→FY2023 revenue-growth observation. Before treating divergence as a meaningful measurement result, the project should establish that the pattern is not purely an artifact of one extreme percentage change, one issuer series, or the choice of ordinary percentage growth.

## Baseline

The positive-base direct-candidate inventory contains **9 adjacent annual transitions** across Blibli 3P, Bukalapak Group, and Tokopedia. It has **3 opposite-sign movements**, and the median absolute ordinary transaction/revenue growth gap is **42.94 percentage points**.

## Alternative growth transformation

Using log changes rather than ordinary percentage growth reduces sensitivity to very large percentage changes from low bases. The median absolute log-growth difference is **36.64 log-points ×100**. The classification of which measure grows faster and the three sign reversals are unchanged.

This supports the qualitative result that the two ledgers can tell materially different growth stories without relying on a single arithmetic growth convention.

## Largest-gap deletion

The largest ordinary growth gap is Blibli FY2022→FY2023, at roughly **430.61 percentage points**, reflecting a low starting net-revenue base plus large monetization/promotion changes.

Deleting that one observation leaves:

- **8 transitions**;
- **3 sign reversals**;
- median absolute ordinary growth gap **29.34pp**;
- median absolute log-growth gap **25.19**.

The phenomenon therefore does not disappear when the most extreme raw percentage-growth observation is removed.

## Leave-one-transition-out

Across all nine leave-one-transition-out exercises, the median absolute ordinary growth gap ranges from **29.34pp to 52.52pp**. No individual transition is necessary to obtain a non-trivial median divergence.

## Leave-one-series-out

| Excluded series | Remaining transitions | Sign reversals | Median absolute ordinary gap | Median absolute log gap |
|---|---:|---:|---:|---:|
| Blibli | 4 | 1 | **38.92pp** | **28.58** |
| Bukalapak | 6 | 3 | **52.52pp** | **41.73** |
| Tokopedia | 8 | 2 | **29.34pp** | **25.19** |

Every leave-one-series-out construction retains at least one sign reversal and material divergence. Thus no one platform series mechanically creates the descriptive non-equivalence.

## What this establishes

> Within the current direct-candidate construction, transaction/revenue growth divergence survives obvious extreme-observation, transformation, and leave-one-series-out checks.

This makes the measurement phenomenon harder to dismiss as a single anomalous growth calculation.

## What remains unresolved

This robustness result does **not** solve the principal admission problem:

- Blibli 3P still includes OTA/travel;
- Bukalapak Group still includes overseas operations;
- Tokopedia remains Indonesia-aligned rather than a literal geographic line;
- the direct candidates are purposive disclosures, not a representative platform sample.

Accordingly, robustness strengthens the descriptive finding but does not convert it into a final Indonesia population estimate.

## Advisor implication

The main unresolved question for Professor Kong is increasingly **sample boundary**, not whether the transaction/revenue divergence vanishes under elementary robustness checks.

Reproduction:

- `scripts/analysis/build_indonesia_longitudinal_robustness.py`
- `outputs/empirical_robustness_2026-09-10/direct_transition_metrics.csv`
- `outputs/empirical_robustness_2026-09-10/robustness_scenarios.csv`
- `outputs/empirical_robustness_2026-09-10/leave_one_transition_out.csv`
