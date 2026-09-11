# Indonesia longitudinal robustness — 10 September 2026

**Status:** robustness diagnostic for the certified direct-candidate inventory. It does not choose the final thesis sample and does not turn scope-pending observations into Indonesia-only observations.

## Question

Is the observed transaction-versus-revenue divergence being driven entirely by one extreme transition, one platform series, or the ordinary percentage-growth transformation?

## Baseline direct-candidate result

The retained positive-base direct candidates yield **9 adjacent annual transitions**, **3 sign reversals**, and a median absolute ordinary growth-rate gap of **42.94 percentage points**.
Using log changes instead of ordinary percentage growth gives a median absolute log-growth gap of **36.64 log-points ×100**. The direction rankings and sign-reversal classification are unchanged by the monotone growth transformation.

## Extreme-transition sensitivity

Dropping the single largest ordinary growth-gap transition leaves **8 transitions**, still **3 sign reversals**, and a median absolute gap of **29.34 percentage points**.

The largest raw gap is Blibli FY2022→FY2023, where a low starting net-revenue base and major monetization/promotion changes generate an unusually large percentage-growth difference. The descriptive divergence therefore does not disappear when that observation is removed.

## Leave-one-transition-out sensitivity

Across all nine leave-one-transition-out exercises, the median absolute ordinary growth gap ranges from **29.34pp to 52.52pp**. No single transition is necessary for the qualitative conclusion that transaction and revenue growth can differ materially.

## Leave-one-series-out sensitivity

| Excluded series | Remaining transitions | Reversals | Median abs. ordinary gap | Median abs. log gap |
|---|---:|---:|---:|---:|
| Blibli | 4 | 1 | 38.92pp | 28.58 |
| Bukalapak | 6 | 3 | 52.52pp | 41.73 |
| Tokopedia | 8 | 2 | 29.34pp | 25.19 |

Every leave-one-series-out construction retains at least one sign reversal and a non-trivial median growth gap. This means the descriptive non-equivalence is not mechanically dependent on one platform series. However, the **geographic/business-scope quality changes sharply across these scenarios**, so this is robustness of the measurement phenomenon—not evidence of a representative Indonesia population effect.

## What this strengthens

> The direct-candidate result is not solely an artifact of the single largest percentage-growth observation, a single issuer series, or the use of ordinary percentage growth rather than log change.

## What it does not strengthen

- It does not resolve whether Blibli 3P belongs in the final Indonesia sample.
- It does not resolve Bukalapak's overseas Group scope.
- It does not make Tokopedia a literal country geographic line.
- It does not establish a population mean effect, statistical treatment effect, missing GDP, hidden income, or tax gap.
- The small candidate count means these summaries should remain descriptive robustness diagnostics rather than conventional inferential statistics.

## Decision consequence

The empirical question for Professor Kong is now less about whether the divergence disappears under obvious robustness checks and more about **which business/geographic boundary is acceptable for the thesis's Indonesia longitudinal design**.
