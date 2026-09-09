# Methods, interpretation and closest-literature check

10 September 2026. Targeted research note, not a systematic review or a novelty certification. Sources below are external literature; numerical inputs remain the repository's BPS extracts. All proposed additions are labelled as our calculations or research judgments.

## The economic question

What changes in our account of Indonesian digital commerce when we distinguish commercial breadth, transaction scale, marketplace channels, and conventional financial-statement ownership rather than use a single platform-company measure?

This operationalizes part of the original commercial-depth ambition. It does not redefine its object as corporate accounting. Company/segment reconciliations remain useful for understanding recorded monetization, while BPS describes a different broader business population. They are not linkable microdata in the current repository.

## M1. Conditional growth decomposition

For each year let V be the published nominal BPS e-commerce value and N the estimated business count. Define A=V/N. Then V=N*A and:

Delta V = Delta N * (A1+A0)/2 + Delta A * (N1+N0)/2.

The symmetric allocation avoids assigning the interaction term entirely to either factor. It is exact arithmetic, not a causal decomposition or identification of entry and continuing-firm growth. It does not control for prices, compositional change or sampling-frame changes. The competing 2023 N is a separate labelled source-conflict scenario.

The report computes V/N in IDR million per estimated business. It must not be called productivity, profitability, household welfare or average income.

## M2. Channel-specific movement

Use only BPS's exclusive value decomposition. The 2024 marketplace amount is V2024 multiplied by the reported 15.79% share; it is a derived value using a rounded source percentage. Subtract from V2024 to obtain the corresponding nonmarketplace component. Compare with the published 2023 component amounts.

This does not use the percentage of businesses selecting a marketplace sales channel or the multiple-response attribution of transaction value. A seller can use several media. Nonmarketplace activity includes other online channels and is not synonymous with a group of informal WhatsApp sellers. The 98.49% allocation of the nominal increase is not a causal share and inherits all source-definition uncertainties.

## M3. Coverage from marginal information

Let M=1 mean marketplace use and F=1 financial-report ownership for a business in the same target population and reference year. Write m=P(M=1), f=P(F=1), and q=P(M=0,F=0). Nonnegativity of the four table cells implies:

max(0,1-m-f) <= q <= min(1-m,1-f).

For any q in that interval, the cells are:

- P(M=1,F=1) = q-1+m+f;
- P(M=1,F=0) = 1-f-q;
- P(M=0,F=1) = 1-m-q;
- P(M=0,F=0) = q.

They are nonnegative and sum to one, proving sharpness conditional on the marginals. The program generates both endpoint tables and tests feasibility on a grid. The same algebra applies to messaging use paired with absence of reports after complementing the channel event.

These are classical Frechet/Duncan-Davis-style bounds. Neither the formula nor the partial-identification idea is new. Applying this logic does not entail fitting an ecological regression or treating an aggregate correlation as an individual association. It makes the unknown overlap explicit instead of inventing an independent joint distribution.

The empirical intervals use survey-estimated marginals as fixed inputs. Rounding-only outer intervals add +/-0.005 percentage points to each displayed percentage. They do not account for sampling error or nonresponse bias. Before promoting a population assertion, review the common population/denominators and survey uncertainty. The implied business counts are products of estimates, not an enumeration of identified enterprises.

A business without a financial statement may still keep receipts, transaction histories, bank records or tax records. The target is the stated survey item, not 'no records' or absence from official statistics. BPS already attempts to observe this population. Likewise the bounds do not identify the group's share of sales: marginal business-count proportions contain no joint revenue information.

## Closest literature and the actual addition

### 1. OECD (2023), OECD Handbook on Compiling Digital Supply and Use Tables

Official full-text Chapter 3 was inspected, particularly digital ordering, intermediation and differing e-commerce definitions. The framework already distinguishes platform intermediation from the underlying transactions. The three-ledger narrative must not claim to invent those boundaries.

Our proposed addition: specific later Indonesian comparisons that change an interpretation of nominal growth or population coverage. Such an application remains to be assessed for value, not assumed novel because the sources differ.

https://www.oecd.org/en/publications/oecd-handbook-on-compiling-digital-supply-and-use-tables_11a0db02-en/full-report/component-5.html
DOI: 10.1787/11a0db02-en

### 2. DFS Lab and RISE Indonesia (2022), The Contribution of Platform Livelihoods to an Inclusive Digital Economy in Indonesia

The original publisher's description was checked. It explicitly investigates scale, scope and quality of platform livelihoods across digital marketplaces and social media, using interviews and more than 100 papers/reports. This is close prior work for the broader participant-economy motivation. Full source-by-source replication was not performed in this pass.

Our proposed addition: a reproducible later-year growth/channel comparison and explicitly bounded joint recordkeeping/channel coverage. Before a novelty claim, check whether the report or its successors already address these particular quantities. Wider participation is not evidence of improved livelihood quality.

https://caribou.global/publications/contribution-of-platform-livelihoods-to-an-inclusive-digital-economy-in-indonesia/

### 3. BPS (2025), Menimbang Manfaat dan Risiko Penggunaan Marketplace dalam E-Commerce di Indonesia

The official catalogue was checked: release 30 September 2025, revised 26 November 2025. It already analyses marketplace use, revenue, literacy and risks. Prior project review also identified financial-statement subgroup comparisons; those numeric cells have not been imported here. The official revised PDF download failed in this pass.

Our proposed addition: a matched 2024 extension and a comparison of channel-specific versus aggregate growth; a bounds calculation only where an appropriate joint table is unavailable. This is not a discovery that BPS statistics exist. Provincial non-significance does not overturn BPS's enterprise-level comparison.

https://www.bps.go.id/id/publication/2025/09/30/3bc481a585782813cc894636/cerita-data-statistik-untuk-indonesia-menimbang-manfaat-dan-risiko-penggunaan-marketplace-dalam-e-commerce-di-indonesia.html

### 4. Imai, Lu and Strauss (2011), eco: R Package for Ecological Inference in 2 x 2 Tables

The author-hosted abstract and citation were checked. This paper describes both model-based EI and Duncan-Davis bounds. It establishes the existing methodological lineage; this branch implements only elementary no-dependence bounds with a self-contained algebraic proof, not the package's Bayesian or likelihood procedures.

https://imai.fas.harvard.edu/research/ecojss/
Journal of Statistical Software 42(5), 1-23.

### 5. Elzayn, Goldin, Guage, Ho and Morton (2026), Monotone Ecological Inference

Publisher full-text introduction and bounds discussion inspected. Online publication 10 July 2026; the NBER predecessor is Working Paper 34285 (2025). The article studies how explicit conditional-association assumptions can tighten bounds. No such monotonicity assumption is adopted here, and no claim is made to reproduce its model or results.

https://www.cambridge.org/core/journals/political-analysis/article/monotone-ecological-inference/4090B0DA4A8B2ACF493795EDD60AF093
https://www.nber.org/papers/w34285

## Evidence-to-conclusion discipline

1. Scope finding: a marketplace-only BPS component and the whole BPS e-commerce estimate show different nominal growth. Not established: actual error by an investor, statistical office or policymaker.
2. Participation finding: an increase in estimated business numbers is the larger arithmetic component under both recorded count alternatives. Not established: causally identified entry, real productivity or income gains.
3. Coverage finding: conditional marginal bounds establish a large possible/necessary group outside two defined channels. Not established: sales-value concentration, complete absence of records, or absence from tax/statistical systems.
4. Original ambition: the work can reveal economic breadth obscured by a chosen narrow lens. Completion requires a clear benchmark, a substantive interpretation and a check against the nearest studies; it does not require reviving the original national residual estimate.

The contribution is still conditional but now includes explicit calculations and falsifiable source requirements. Do not advertise it as a breakthrough, a guaranteed thesis grade or an exhaustive account of Indonesian commercial potential.
