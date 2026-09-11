# BPS growth-anatomy robustness — 10 September 2026

**Status:** exact arithmetic robustness note using published BPS national estimates. It does not estimate causal entry, survival, incumbent-firm growth, inflation-adjusted output, or productivity.

## Why this check matters

The rebuilt *Invisible Ledger* interpretation increasingly relies on the proposition that recent Indonesian e-commerce growth reflects broadening participation as well as transaction intensity. The ordinary growth rates support that reading, but an exact arithmetic decomposition provides a cleaner statement of how the observed aggregate increase maps into business-count and implied value-per-business terms.

## Exact symmetric decomposition

For aggregate e-commerce transaction value `V = N × A`, where `N` is the estimated number of e-commerce businesses and `A` is implied nominal value per estimated business, the symmetric two-factor decomposition exactly allocates the change in `V`.

| Period | Aggregate value increase | Business-count term | Implied value/business term |
|---|---:|---:|---:|
| 2022→2023 | Rp317.87T | **70.98%** | 29.02% |
| 2023→2024 | Rp188.06T | **90.29%** | 9.71% |
| 2022→2024 | Rp505.93T | **76.95%** | 23.05% |

The business-count term is therefore the larger arithmetic component in each comparison. The strongest recent case is 2023→2024, where the count term accounts for about **90.29%** of the nominal increase under this exact decomposition.

## Source-conflict sensitivity

The BPS source audit preserves a conflicting 2023 business-count figure of 3,934,981, while 3,816,750 is the certified cross-year series value because it matches BPS's later official 15.30% growth statement.

If 3,934,981 is substituted only as a sensitivity scenario, the 2023→2024 business-count term still accounts for about **70.95%** of the nominal value increase. Thus the broad participation interpretation does not depend on the disputed 2023 count choice, although the certified series should continue to use 3,816,750.

## Sales-media decomposition of the 2023→2024 increase

Using the certified direct BPS sales-media amounts:

- total national e-commerce value increases by **Rp188.06T**;
- marketplace value increases by **Rp2.90T**, only **1.54%** of the total arithmetic increase;
- non-marketplace value increases by **Rp185.16T**, or **98.46%** of the increase.

This is stronger than merely comparing growth rates. It shows where the arithmetic increase in the published national estimate resides.

It does **not** imply that non-marketplace commerce is hidden, informal, untaxed, or omitted from official statistics. BPS is precisely the source observing this activity. The result instead establishes that a marketplace-company view would miss most of the change captured in the broader BPS national sales-media estimates for this period.

## Research consequence

The evidence supports the bounded statement:

> Recent Indonesian e-commerce expansion is associated arithmetically with broadening estimated business participation, and the 2023→2024 increase in published national transaction value is overwhelmingly concentrated in non-marketplace sales media.

This strengthens the original "economic depth beneath the surface" intuition without requiring a missing-GDP, hidden-income, or tax-gap claim.

Reproduction:

- `scripts/analysis/build_bps_growth_robustness.py`
- `outputs/empirical_robustness_2026-09-10/bps_growth_exact_decomposition.csv`
- `outputs/empirical_robustness_2026-09-10/bps_business_count_conflict_sensitivity.csv`
- `outputs/empirical_robustness_2026-09-10/bps_channel_increment_decomposition.csv`
