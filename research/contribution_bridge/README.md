# Economic contribution bridge

Independent contribution, 10 September 2026. Based on main commit `69f8e3d6ca1af9bef310098d36f5cd0511454acb`. This directory complements Box's empirical exploration. It is not a replacement manuscript, an approved sample, or a claim that the original research ambition is now completely established.

## Purpose

The original ambition is to make the breadth and movement of Indonesia's digitally mediated commercial economy economically intelligible beyond a narrow company-centred view. This contribution asks what concrete interpretation changes when existing measurements are read together. It does not turn the project into a general accounting essay or an unrelated BPS study.

The attached Box explanation already proposes studying separate transaction, corporate, and statistical/administrative ledgers. That is the research framing. The calculations here are additional analysis of the versioned repository extracts, not further facts asserted by that explanation.

## Completed work

1. Channel-specific nominal growth: compare the exclusive BPS marketplace component with total e-commerce, without equating nonmarketplace commerce with informal commerce.
2. Breadth versus average activity: decompose total-value growth into estimated business-count and average nominal value terms, with the known competing 2023 count retained as a sensitivity scenario.
3. Financial-report coverage: separate changes in ownership rates from changes in implied numbers of businesses with and without statements.
4. Joint coverage bounds: use compatible published marginals to bound the share reporting neither marketplace use nor financial-report ownership. No independence or enterprise-level correlation is assumed. Endpoint tables prove the bounds are attainable.
5. Research positioning: compare the actual addition with the nearest literature and identify remaining promotion conditions.

## Reproduce

Python 3.10 or later; standard library only:

```sh
python -m unittest discover -s tests -p 'test_contribution_bridge.py' -v
python scripts/analysis/build_contribution_bridge.py --output build/contribution_bridge
```

The exact input CSV is pinned by Git blob hash. If Box updates that file, execution stops rather than silently treating changed definitions or observations as the same experiment. Reassess the update, then deliberately revise the pin. The default command writes only to `build/contribution_bridge`.

`results/RESULTS.md` is a committed readable output. The CI run reconstructs it with its CSVs and manifest, verifies byte-identical regeneration, and checks that the source directories are unchanged. Local execution passed 31 tests, including a 441-marginal-pair grid for feasible and sharp endpoint tables. Test coverage is evidence of arithmetic and reproducibility, not statistical-source validation.

## What the results add

With the repository's current BPS inputs, total 2023-2024 nominal transaction value rises about 17.08%, while the exclusive marketplace component rises about 1.42%. About 98.49% of the arithmetic increase is in the nonmarketplace component. The new point is a growth comparison, not the already published observation that marketplaces are a minority of total value.

The selected business counts imply 15.31% growth in businesses and 1.54% growth in average nominal transaction value per estimated business. The alternative 2023 count gives 11.84% and 4.69%, respectively. Both differ markedly from a reading of 17.08% aggregate growth as growth within a typical continuing firm.

For 2024, the point marginals imply that the share with neither reported marketplace use nor financial-report ownership lies in [65.62%, 82.77%]. This is a standard method-of-bounds result applied to the two source marginals. It does not identify the exact joint share or the amount of sales produced by this group, and it is not a survey confidence interval.

## Relationship to the idealized original paper

- **Original purpose preserved:** commercial participation and economic activity outside any single corporate view remain the subject.
- **Additional information produced:** the choice of channel changes the measured growth story; an aggregate growth headline differs from the implied per-business movement; two limited coverage channels jointly leave a bounded portion of the reported business population outside them.
- **Not yet established:** an independently valuable empirical novelty relative to all closest studies; actual inability of authorities to see or link records; participant earnings, productivity, wealth or creditworthiness.
- **Not a restored shortcut:** no business-count percentage is multiplied by total sales to estimate unreported income, and no company residual is treated as a national missing quantity.

An affirmative working interpretation is: the published evidence suggests broadening nominal commercial participation and substantially different growth across channels, while conventional financial-statement ownership remains limited. The paper can investigate what a marketplace- or company-only reading fails to communicate about that transformation. This remains a proposed contribution, not a claim that government statisticians actually make that mistake.

## Scope and evidence limits

All numerical calculations use the existing BPS national extract. The 2023 alternate business count comes from the conflict already documented in `data/bps_official/README.md`. This pass independently verified the copied CSV against GitHub's exact blob hash. It did not acquire enterprise microdata or re-audit the entire issuer backend.

Official BPS publication pages were accessed; PDF downloads failed. Consequently, original-cell verification and exact wave/denominator concordance remain prerequisites for manuscript inclusion. Within-year bounds do not require identical businesses across years, but each year's two margins must describe the same target population and compatible item-response denominators. Cross-year growth additionally requires compatible measurement definitions and populations.

The bound intervals address unknown overlap, not sampling error. Rounding sensitivity covers the last displayed digit only. No monotonicity, model-based imputation or p-value search is used. If BPS supplies a valid joint table for the same year and population, use it rather than these broader bounds.

Company periods, BPS businesses, province-years, source rows and sensitivity variants remain distinct. These outputs add analysis, not more observations to the issuer main sample.

## Concrete handoff to Box

1. Confirm the BPS 2023/2024 exclusive channel definitions and total-value populations; do not replace them with multiple-response channel attributions.
2. Check financial-report and sales-channel item definitions, denominators and weights within each year. Direct same-year cross-tabulations take precedence over bounds.
3. Resolve or retain the 2023 count discrepancy explicitly. Do not suppress its sensitivity because the preferred estimate looks more coherent.
4. Keep the outstanding Tokopedia FY2021 exclusion in the canonical census and derive candidate counts from rules. This separate branch does not repair the incumbent code or endorse its advertised 14/9 counts.
5. Check these particular additional comparisons against the nearest Indonesian studies. Novelty is not inferred from calling the framework 'three ledgers'.
6. Bring only the accepted comparisons into the agreed main/supporting architecture. Do not revise the whole manuscript before that decision.

No changes in this branch are made to `data/`, `sources/`, existing `outputs/`, `papers/`, the advisor-approval language, or the original engineering PR.
