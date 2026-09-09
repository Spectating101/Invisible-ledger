# Validation report: first hypothesis tests

## Overall assessment: share with caveats

The analysis is reproducible and the headline calculations reconcile to the
source-layer CSVs. It is suitable for internal review and for discussing sample
design with Professor Kong. It is not ready to be presented as a finalized
Indonesia main sample because most longitudinal transitions are either
scope-pending issuer records or conditional country reconstructions.

## Methodology review

- The issuer calculation uses one consecutive annual transition within the
  same named series. It does not convert currencies or add monetary values.
- Three evidence tiers remain explicit in every level and transition row.
- Tokopedia FY2021 is excluded for period mismatch.
- Bukalapak FY2024 is excluded because TPV covers nine months and revenue covers
  twelve months.
- Blibli selects the latest available comparative publication vintage for each
  year and retains its travel-scope warning.
- BPS national decomposition uses the official transaction-value and estimated-
  business levels. The 2024 marketplace component is labelled as derived from
  the official total and percentage share.
- Province tests exclude the Indonesia total and use 36 common complete
  provinces for the change analysis.
- Pearson, Spearman, and weighted correlations are labelled descriptive and
  ecological. No causal or business-level claim is made.

## Issues found

1. **High — final sample unresolved.** Only one of the twelve transitions is in
   the direct Indonesia-aligned tier. This blocks treating the combined
   transition summary as the final main-sample estimate.
2. **High — scope differences remain.** Blibli includes online travel;
   Bukalapak has overseas operations; Grab and Shopee contain allocation
   assumptions. These records are useful for testing the phenomenon but not
   interchangeable Indonesia observations.
3. **High — province evidence is ecological.** The province analysis cannot
   identify whether marketplace-using businesses themselves maintain financial
   reports.
4. **Medium — 2023 BPS business count has a source conflict.** The current
   calculation uses 3,816,750 because it appears in the main body and matches
   the stated growth rate; 3,934,981 appears elsewhere in the publication.
5. **Medium — the all-candidate 42.02 percentage-point median is sensitive to
   early revenue-base effects.** It is retained as an inventory diagnostic and
   not presented as a population estimate.

## Calculation spot-checks

- **Tokopedia FY2022–FY2023 transaction growth: verified.** Independent
  recomputation from the source extension gives -8.9000%.
- **Tokopedia FY2022–FY2023 net-revenue growth: verified.** Independent
  recomputation gives +53.1956%.
- **BPS 2023–2024 total transaction growth: verified.** Independent
  recomputation gives +17.0829%.
- **BPS 2023–2024 estimated-business growth: verified.** Independent
  recomputation gives +15.3068%.
- **Province-change sample and Pearson association: verified.** The direct
  source merge produces 36 common complete provinces and `r=0.309453`,
  `p=0.066274`.
- **Repository structural validation: passed.** `scripts/validate_repo.py`
  validates 91 CSV files and 38,305 file-layer rows. That count is not the
  analytical sample size.
- **Notebook execution: passed.** The companion notebook executes from top to
  bottom and rebuilds the derived outputs.

## Visualization review

- The Indonesia chart uses horizontal signed bars because the analytical
  quantity is growth divergence. It labels evidence tiers and opposite-sign
  transitions and retains a visible zero line.
- The BPS national chart uses grouped bars for two discrete annual comparisons;
  it does not imply a long continuous time-series trend.
- The province chart shows three alternative correlation measures across the
  two cross-sections and the first-difference specification. Its purpose is to
  display instability, not statistical significance.
- All three figures were inspected after rendering. Labels, units, legends,
  signs, and footnotes are legible at the exported size.

## Required caveats for stakeholders

- The 17 levels and 12 transitions are a candidate inventory, not an approved
  pooled Indonesia sample.
- Transaction/revenue divergence does not measure missing GDP, undeclared
  income, unpaid tax, or tax evasion.
- Aggregate business-count growth does not identify causal entry or
  productivity.
- Province correlations do not identify business-level behavior.
- Institutional linkage failure remains untested.

## Suggested improvements

1. Resolve issuer/segment admission with Kong before manuscript restructuring.
2. Seek a BPS business-level cross-tabulation or licensed microdata.
3. Expand the revenue-component reconciliation for admitted issuer transitions.
4. Retain tier-specific summaries and avoid making the all-candidate median a
   headline result.
