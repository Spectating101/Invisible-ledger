# Empirical findings ledger — 10 September 2026

## Purpose and status

This document records what the executed and source-auditable empirical work currently establishes. It is not a manuscript argument, hypothesis list, or statement of advisor approval. Each finding below names the data and code that support it and states the boundary of the inference.

The evidence layers are complementary but are not one pooled sample:

1. Indonesia issuer and official-statistics evidence;
2. ASEAN country histories and institutional heterogeneity;
3. global issuer transaction/revenue histories;
4. exploratory market-price evidence.

Counts from these layers must not be added into a single `N`.

For count corrections, source-certification status, and the direct/conditional sample hierarchy, also read [`EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md`](EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md).

## 1. Indonesia: the one-year construction is auditable but insufficient alone

The FY2023 construction contains three platform cases supported by eleven source inputs. Tokopedia supplies the strongest paired disclosure. Grab's Indonesia revenue is direct but its Indonesia transaction value is derived using a Group monetization rate. Shopee's Indonesia transaction value is an external country-market estimate and its country revenue is derived using Sea's disclosed service-revenue/GMV rate.

This establishes that a transparent FY2023 comparison can be reconstructed. It does not establish a sufficient longitudinal thesis sample, a national total, or a directly observed country pair for all three platforms.

Evidence and reproduction:

- `data/indonesia_fy2023/`
- `docs/METHODOLOGY.md`
- `docs/KNOWN_LIMITATIONS.md`

## 2. Indonesia: the broader evidence base is longitudinal and multi-layered

After enforcing the known Tokopedia FY2021 period mismatch, the advisor-facing direct annual candidate set contains **13** economic periods rather than the historical audit headline of 14:

- seven Blibli 3P annual issuer-year candidates from FY2019–FY2025;
- four Bukalapak Group annual candidates from FY2020–FY2023;
- two valid Tokopedia e-commerce segment periods, FY2022–FY2023.

Twelve of the thirteen have positive revenue denominators; Blibli 3P FY2019 has negative net revenue and is not ratio-eligible.

The original Indonesia longitudinal extension retains **8** observations rather than nine after excluding Tokopedia FY2021:

- Grab FY2021–FY2023: 3 conditional country reconstructions;
- Shopee FY2022–FY2024: 3 conditional country reconstructions;
- Tokopedia FY2022–FY2023: 2 direct Indonesia-aligned segment observations.

The repository also contains:

- forty-seven company-quarter accounting rows for Grab, GoTo, and Sea;
- seventy-four BPS province-years across the retained 2023 and 2024 publications, with the national `Indonesia` total row kept separate from province counts;
- national BPS indicators extending across available years from 2020–2024.

These observations do not constitute one homogeneous dataset. Their value is that they permit separate longitudinal, accounting, and population-level analyses without pretending that issuer segments and official business statistics describe the same population.

Evidence and reproduction:

- `data/longitudinal/`
- `data/quarterly/`
- `data/bps_official/`
- `scripts/analysis/build_panel.py`
- `scripts/analysis/build_quarterly_panel_source_coverage.py`
- `scripts/analysis/build_comprehensive_empirical_audit.py`
- `docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md`

## 3. Indonesia: candidate-series longitudinal movement already differs across ledgers

For the currently reviewed direct candidate histories, adjacent annual changes are computed only within the same issuer/segment. Levels are never pooled across currencies or firms.

The current direct-candidate transition set contains **9 adjacent annual transitions**:

- 5 Blibli 3P transitions, FY2020→FY2021 through FY2024→FY2025;
- 3 Bukalapak Group transitions, FY2020→FY2021 through FY2022→FY2023;
- 1 Tokopedia e-commerce transition, FY2022→FY2023.

Within those 9 transitions:

- recognized-revenue growth exceeds transaction-activity growth in **6**;
- transaction-activity growth exceeds revenue growth in **3**;
- **3 transitions have opposite growth signs**;
- the median absolute revenue-minus-transaction growth difference is **42.94 percentage points**.

The three opposite-sign cases are:

- Blibli 3P FY2020→FY2021: transaction activity +14.86%, net revenue −28.08%;
- Blibli 3P FY2024→FY2025: transaction activity −1.89%, net revenue +12.07%;
- Tokopedia FY2022→FY2023: transaction activity −8.90%, net revenue +53.20%.

This establishes descriptively that recognized platform/segment revenue is not a stable one-for-one proxy for the movement of the transaction activity it accompanies. It does **not** establish a final thesis-sample estimate because Blibli and Bukalapak business/geographic admission remains for the advisor to decide.

## 4. Indonesia: official statistics show economically large and channel-heterogeneous digital commerce

The official retained BPS values report:

- 2023 e-commerce transaction value of **Rp1,100.87 trillion**;
- 2024 e-commerce transaction value of **Rp1,288.93 trillion**;
- nominal transaction-value growth of **17.08%** from 2023 to 2024;
- 2023 selected cross-year e-commerce-business count of **3,816,750**;
- 2024 estimated e-commerce businesses of **4,400,972**;
- business-count growth of **15.31%**;
- financial-report ownership of **15.19%** in 2023 and **17.15%** in 2024 as separately published wave values.

The 3,816,750 count is retained for the cross-year series because a later official BPS 2024 statement reports approximately 15.30% year-on-year growth in the number of e-commerce businesses. Growth from 3,816,750 to 4,400,972 is 15.31%; the conflicting 3,934,981 passage implies only 11.84%. The conflicting source passage remains documented rather than being erased.

Using the selected aggregate totals, implied nominal transaction value per estimated e-commerce business rises approximately **1.54%** from 2023 to 2024. This is an arithmetic ratio of repeated aggregate survey estimates, not growth of the same incumbent businesses and not a productivity estimate.

### Certified descriptive sales-media comparison

The 2023 BPS publication reports national e-commerce transaction value **by sales media**, with **Rp200.68 trillion** through marketplace/platform digital and **Rp900.19 trillion** through non-marketplace/platform-digital media.

A BPS-Statistics Indonesia presentation reports the corresponding 2024 national sales-media split directly as **Rp203.58 trillion / 15.79% marketplace** and **84.21% non-marketplace**, against total e-commerce transaction value of Rp1,288.93 trillion. Using the directly reported 2024 marketplace amount rather than reconstructing it from the rounded share gives:

- marketplace component: **Rp200.68T → Rp203.58T, +1.45%**;
- non-marketplace component: **Rp900.19T → Rp1,085.35T, +20.57%**;
- total e-commerce transaction value: **+17.08%**.

This establishes a descriptive national-estimate result: the published non-marketplace component grew much faster than the marketplace component between 2023 and 2024. It does **not** identify incumbent-firm behavior, causal channel substitution, productivity, hidden activity, tax status, or a linkage to issuer GMV/TPV.

The stronger cross-wave interpretation of financial-report ownership remains guarded. The two published wave values, 15.19% and 17.15%, are established, but questionnaire/population concordance should still be checked before treating the +1.96 percentage-point movement as a strong behavioral trend.

Evidence and reproduction:

- `data/bps_official/`
- `reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md`
- `docs/BPS_CROSSWAVE_CERTIFICATION_2026-09-10.md`
- `docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md`

## 5. BPS province evidence is repeated aggregate evidence, not a business panel

After excluding the national `Indonesia` total row from province counting:

- **38** actual provinces are common across the retained 2023 and 2024 files;
- **36** have complete focal marketplace-use / financial-report fields in both waves;
- the 38 published 2024 province business counts sum to **4,400,973**;
- the published Indonesia total is **4,400,972**.

The one-business source residual is preserved. No province value is adjusted to force reconciliation.

Province-level associations and changes are ecological/descriptive. They do not identify enterprise-level relationships or causal marketplace effects.

## 6. Global issuer accounting: transaction activity and recognized revenue are not interchangeable measures

The global corroboration panel contains **48 matched issuer-years** for eight platform businesses from 2017–2025. These yield **40** consecutive within-issuer annual transitions. Eleven are conservatively flagged for known perimeter breaks, leaving **29 clean-screened transitions**.

Among those 29 transitions:

- recognized revenue grew faster than the transaction measure in **22**;
- the transaction measure grew faster in **7**;
- the median signed revenue-minus-transaction growth difference was **6.54 percentage points**;
- the median absolute growth difference was **7.10 percentage points**;
- **4 transitions had opposite growth signs**.

The clean opposite-sign cases are Etsy 2021–2022, Etsy 2023–2024, eBay 2022–2023, and Zalando 2021–2022.

These cases directly demonstrate that a revenue series can imply a different direction of change from the platform's reported transaction measure. They do not mean revenue is erroneous; the measures describe different economic objects.

Evidence and reproduction:

- `data/global_ecommerce/global_platform_source_inputs.csv`
- `data/global_ecommerce/global_platform_matched_annual.csv`
- `data/global_ecommerce/global_platform_growth_divergence.csv`
- `data/global_ecommerce/global_platform_summary.csv`
- `scripts/analysis/build_global_ecommerce_corroboration.py`
- `reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md`

## 7. Business-model and definition heterogeneity materially affect comparison

Across the retained global histories, the observed revenue-to-transaction ratio ranges from approximately 0.22% for launch-stage Shopee in 2017 to 74.63% for Zalando in 2020. The range is not a performance ranking. The underlying definitions differ because the businesses variously include or exclude subscriptions, advertising, travel, first-party sales, returns, shipping, taxes, B2B services, and financial services.

The definition evidence establishes that similarly named transaction metrics cannot be pooled mechanically across issuers or applied as a common country monetization rate. Business perimeter is part of the empirical result, not a minor disclosure footnote.

Evidence and reproduction:

- `data/global_ecommerce/global_platform_definition_map.csv`
- `data/global_ecommerce/global_platform_issuer_summary.csv`
- `reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md`

## 8. ASEAN: digital-commerce expansion recurs, but countries are heterogeneous

The revision-aware ASEAN module retains six separate country histories rather than pooling the region. Latest-vintage estimates show e-commerce GMV rising between 2023 and 2025 in Indonesia, Malaysia, the Philippines, Singapore, Thailand, and Vietnam. The median within-country increase is 36.4%, ranging from 12.5% in Singapore to 53.8% in Malaysia.

In 2025, the estimated e-commerce share of overall digital-economy GMV ranges from approximately 31.0% in Singapore to 71.7% in Indonesia. Reported platform market structures and country tax architectures also differ.

The evidence establishes regional recurrence of digital-commercial expansion and validates the decision to analyze countries separately. It does not establish a common ASEAN treatment effect, tax system, monetization rate, or Indonesia allocation.

Evidence and reproduction:

- `data/asean_corroboration/asean_country_year_canonical_2019_2025.csv`
- `data/asean_corroboration/asean_growth_corroboration_2023_2025.csv`
- `data/asean_corroboration/asean_country_heterogeneity_profile.csv`
- `data/asean_corroboration/platform_structure_2025.csv`
- `data/asean_corroboration/asean_tax_platform_context.csv`
- `scripts/analysis/build_asean_corroboration.py`
- `reports/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md`

## 9. Published estimates revise the measured past

The ASEAN source-vintage table preserves repeated estimates for the same country-year. Of sixty repeated overall-digital-economy and e-commerce cells, forty-five change between the earliest and latest publication. Among changed cells, the median absolute revision is 7.14%. These are revisions to estimates of the same economic period, not additional observations or economic growth.

Issuer reporting can also revise past transaction metrics. Zalando's FY2024 GMV, for example, changes between its original FY2024 publication and the FY2025 comparative. The global module therefore selects the latest available comparative vintage while preserving alternatives.

This establishes that measurement vintage affects the apparent historical record in both market-estimate and issuer-reporting systems. It does not show that national accounts are wrong by the revision amount.

Evidence and reproduction:

- `data/asean_corroboration/economy_sea_source_vintages_2019_2025.csv`
- `data/asean_corroboration/economy_sea_revision_diagnostics.csv`
- `data/global_ecommerce/global_platform_vintage_diagnostics.csv`
- `scripts/analysis/build_asean_corroboration.py`
- `scripts/analysis/build_global_ecommerce_corroboration.py`

## 10. What the evidence establishes when read together

The combined evidence establishes a measurement-boundary result:

> Digital commerce is recorded through transaction, corporate-revenue, business-recordkeeping, market-estimate, statistical, and tax-administrative ledgers that measure different objects. Those measures can evolve differently, use incompatible perimeters, and revise the same historical period. No single public ledger is therefore a sufficient proxy for every dimension of platform-mediated commercial activity.

The digital element is not that gross-versus-net accounting began with online platforms. It is that platforms coordinate large numbers of third-party transactions and create granular private records while public corporate accounts recognize the platform's own revenue under a different perimeter. Digitalization can therefore increase private traceability at the same time that public and institutional views remain fragmented.

This result preserves the original *Invisible Ledger* motivation in a form the current evidence can support: the economically relevant activity is not necessarily absent from every record; it is distributed across ledgers that are not automatically comparable or linkable.

## 11. What is not an empirical finding

The current repository does not establish:

- a monetary amount of activity omitted from GDP;
- undeclared participant income;
- unpaid tax or tax evasion;
- an Indonesia-wide transaction-minus-revenue total;
- representative effects for all platforms or countries;
- business-level links between marketplace use and financial recordkeeping;
- institutional inability to link private platform records to tax or statistical records;
- causal effects of platform participation or reporting policy;
- final investor-market effects.

Those remain separate hypotheses, data-access questions, or future analyses. They must not be presented as conclusions from the current evidence.

## 12. Current empirical conclusion

The defensible conclusion is not that transaction value missing from platform revenue is missing from the economy. It is that the economic story changes with the ledger observed.

Indonesia provides the substantive country setting and already shows large within-series divergence under the current candidate construction; BPS describes the broader business population and now provides a certified aggregate sales-media comparison; ASEAN demonstrates recurrence, heterogeneity, and revision sensitivity; and the global issuer histories show that transaction activity and recognized revenue can follow materially different trajectories across very different platform business models.

The strongest established contribution is therefore to identify and measure where public transaction and revenue views cease to be interchangeable, while documenting what participant-level and institutional linkage would still be required before stronger hidden-income, tax, or value-added claims could be tested.
