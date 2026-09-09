# Empirical findings ledger — 10 September 2026

## Purpose and status

This document records what the executed and source-auditable empirical work
currently establishes. It is not a manuscript argument, hypothesis list, or
statement of advisor approval. Each finding below names the data and code that
support it and then states the boundary of the inference.

The evidence layers are complementary but are not one pooled sample:

1. Indonesia issuer and official-statistics evidence;
2. ASEAN country histories and institutional heterogeneity;
3. global issuer transaction/revenue histories;
4. exploratory market-price evidence.

Counts from these layers must not be added into a single `N`.

## 1. Indonesia: the one-year construction is auditable but insufficient alone

The FY2023 construction contains three platform cases supported by eleven
source inputs. Tokopedia supplies the strongest paired disclosure. Grab's
Indonesia revenue is direct but its Indonesia transaction value is derived
using a Group monetization rate. Shopee's Indonesia transaction value is an
external country-market estimate and its country revenue is derived using
Sea's disclosed service-revenue/GMV rate.

This establishes that a transparent FY2023 comparison can be reconstructed.
It does not establish a sufficient longitudinal thesis sample, a national
total, or a directly observed country pair for all three platforms.

Evidence and reproduction:

- `data/indonesia_fy2023/`
- `docs/METHODOLOGY.md`
- `docs/KNOWN_LIMITATIONS.md`

## 2. Indonesia: the broader evidence base is longitudinal and multi-layered

The active repository contains more than the FY2023 three-case table:

- fourteen Indonesia-aligned annual candidate periods across Blibli,
  Bukalapak, and Tokopedia before final geographic and scope admission;
- seven Blibli annual issuer-year candidates from 2019–2025;
- four Bukalapak annual Group candidates from 2020–2023;
- forty-seven company-quarter accounting rows for Grab, GoTo, and Sea;
- seventy-four complete BPS province-years across the 2023 and 2024
  publications;
- national BPS indicators extending across available years from 2020–2024.

These observations do not constitute one homogeneous dataset. Their value is
that they permit separate longitudinal, accounting, and population-level
analyses without pretending that issuer segments and official business
statistics describe the same population.

Evidence and reproduction:

- `data/longitudinal/`
- `data/quarterly/`
- `data/bps_official/`
- `scripts/analysis/build_panel.py`
- `scripts/analysis/build_quarterly_panel_source_coverage.py`
- `scripts/analysis/build_comprehensive_empirical_audit.py`
- `reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md`

## 3. Indonesia: official statistics show economically large digital commerce

The official 2024 BPS publication reports:

- e-commerce transaction value of Rp1,288.93 trillion;
- 4,400,972 estimated e-commerce businesses;
- financial-report ownership of 17.15%.

The executed growth decomposition for 2023–2024 reports:

- total nominal e-commerce transaction value growth of 17.08%;
- marketplace-component growth of 1.42%;
- non-marketplace-component growth of 20.58%;
- estimated e-commerce-business growth of 15.31%;
- implied nominal transaction value per estimated business growth of 1.54%.

The arithmetic indicates that expansion in the estimated business population
is an important part of the observed aggregate growth, and that the published
non-marketplace component grew faster than the marketplace component in this
comparison. It does not identify productivity, firm entry causally, tax
compliance, or business-level marketplace effects.

Evidence and reproduction:

- `data/bps_official/`
- `outputs/hypothesis_tests_2026-09-10/bps_national_growth_anatomy.csv`
- `reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md`
- `reports/HYPOTHESIS_TESTS_2026-09-10.md`
- `scripts/analysis/build_comprehensive_empirical_audit.py`
- `scripts/analysis/build_hypothesis_tests.py`

## 4. Indonesia: the first longitudinal tests show divergence but do not finalize the sample

The first hypothesis execution retains seventeen matched annual candidate
levels across five series and twelve consecutive within-series transitions.
The records are kept in three separate evidence tiers. Ten transitions have
faster revenue growth than transaction growth, two have faster transaction
growth, and two move in opposite directions. The all-candidate median absolute
growth difference is 42.02 percentage points, but that number combines evidence
tiers and is an inventory diagnostic rather than a pooled-sample estimate.

The strongest individual transition is Tokopedia FY2022–FY2023 because it uses
an Indonesia-aligned direct segment pair. Transaction value declines 8.90%
while third-party net segment revenue rises 53.20%. Blibli 3P Retail also has an
opposite-sign FY2024–FY2025 transition, but it remains in the scope-pending tier
because the segment includes online travel.

This establishes that transaction activity and recognized revenue can tell
different longitudinal stories within the available Indonesia-related issuer
evidence. It does not establish an approved multi-platform Indonesia sample.

Evidence and reproduction:

- `outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_levels.csv`
- `outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv`
- `outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_transition_summary.csv`
- `scripts/analysis/build_hypothesis_tests.py`
- `reports/HYPOTHESIS_TESTS_2026-09-10.md`

## 5. BPS province evidence does not establish a stable marketplace-recordkeeping relationship

The 2023 province cross-section shows a modest association between marketplace
use and financial-report ownership, but the result is sensitive to correlation
measure and weighting. The 2024 unweighted Pearson association is approximately
zero (`r=0.022`, `p=0.897`). Across thirty-six common provinces, changes from
2023–2024 have Pearson `r=0.309` (`p=0.066`) and Spearman `rho=0.151`
(`p=0.379`). The business-count-weighted change correlation is `0.099`.

The executed province evidence therefore does not validate a stable
business-level marketplace/recordkeeping relationship. The national marginal
percentages also permit very wide joint-status bounds. Business-level microdata
or an official joint cross-tabulation is required to test that hypothesis.

Evidence and reproduction:

- `outputs/hypothesis_tests_2026-09-10/bps_province_hypothesis_results.csv`
- `outputs/hypothesis_tests_2026-09-10/bps_within_province_changes.csv`
- `outputs/hypothesis_tests_2026-09-10/bps_joint_status_bounds.csv`
- `scripts/analysis/build_hypothesis_tests.py`
- `reports/HYPOTHESIS_TESTS_2026-09-10.md`

## 6. Issuer accounting: transaction activity and recognized revenue are not interchangeable measures

The global corroboration panel contains forty-eight matched issuer-years for
eight platform businesses from 2017–2025. These yield forty consecutive
within-issuer annual transitions. Eleven are conservatively flagged for known
perimeter breaks, leaving twenty-nine clean-screened transitions.

Among those twenty-nine transitions:

- recognized revenue grew faster than the transaction measure in twenty-two;
- the transaction measure grew faster in seven;
- the median signed revenue-minus-transaction growth difference was 6.54
  percentage points;
- the median absolute growth difference was 7.10 percentage points;
- four transitions had opposite growth signs.

The opposite-sign cases are Etsy 2021–2022, Etsy 2023–2024, eBay 2022–2023,
and Zalando 2021–2022. These cases directly demonstrate that a revenue series
can imply a different direction of change from the platform's reported
transaction measure.

This does not mean revenue is erroneous. Revenue and transaction measures
describe different economic objects. It does establish that corporate revenue
is not a stable one-for-one proxy for the commercial activity coordinated by a
platform.

Evidence and reproduction:

- `data/global_ecommerce/global_platform_source_inputs.csv`
- `data/global_ecommerce/global_platform_matched_annual.csv`
- `data/global_ecommerce/global_platform_growth_divergence.csv`
- `data/global_ecommerce/global_platform_summary.csv`
- `scripts/analysis/build_global_ecommerce_corroboration.py`
- `reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md`

## 7. Business-model and definition heterogeneity materially affect comparison

Across the retained global histories, the observed revenue-to-transaction
ratio ranges from approximately 0.22% for launch-stage Shopee in 2017 to
74.63% for Zalando in 2020. The range is not a performance ranking. The
underlying definitions differ because the businesses variously include or
exclude subscriptions, advertising, travel, first-party sales, returns,
shipping, taxes, B2B services, and financial services.

The definition evidence establishes that similarly named transaction metrics
cannot be pooled mechanically across issuers or applied as a common country
monetization rate. Business perimeter is part of the empirical result, not a
minor disclosure footnote.

Evidence and reproduction:

- `data/global_ecommerce/global_platform_definition_map.csv`
- `data/global_ecommerce/global_platform_issuer_summary.csv`
- `reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md`

## 8. ASEAN: digital-commerce expansion recurs, but countries are heterogeneous

The revision-aware ASEAN module retains six separate country histories rather
than pooling the region. Latest-vintage estimates show e-commerce GMV rising
between 2023 and 2025 in Indonesia, Malaysia, the Philippines, Singapore,
Thailand, and Vietnam. The median within-country increase is 36.4%, ranging
from 12.5% in Singapore to 53.8% in Malaysia.

In 2025, the estimated e-commerce share of overall digital-economy GMV ranges
from approximately 31.0% in Singapore to 71.7% in Indonesia. Reported platform
market structures and country tax architectures also differ.

The evidence establishes regional recurrence of digital-commercial expansion
and validates the decision to analyze countries separately. It does not
establish a common ASEAN treatment effect, tax system, monetization rate, or
Indonesia allocation.

Evidence and reproduction:

- `data/asean_corroboration/asean_country_year_canonical_2019_2025.csv`
- `data/asean_corroboration/asean_growth_corroboration_2023_2025.csv`
- `data/asean_corroboration/asean_country_heterogeneity_profile.csv`
- `data/asean_corroboration/platform_structure_2025.csv`
- `data/asean_corroboration/asean_tax_platform_context.csv`
- `scripts/analysis/build_asean_corroboration.py`
- `reports/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md`

## 9. Published estimates revise the measured past

The ASEAN source-vintage table preserves repeated estimates for the same
country-year. Of sixty repeated overall-digital-economy and e-commerce cells,
forty-five change between the earliest and latest publication. Among changed
cells, the median absolute revision is 7.14%. These are revisions to estimates
of the same economic period, not additional observations or economic growth.

Issuer reporting can also revise past transaction metrics. Zalando's FY2024
GMV, for example, changes between its original FY2024 publication and the
FY2025 comparative. The global module therefore selects the latest available
comparative vintage while preserving alternatives.

This establishes that measurement vintage affects the apparent historical
record in both market-estimate and issuer-reporting systems. It does not show
that national accounts are wrong by the revision amount.

Evidence and reproduction:

- `data/asean_corroboration/economy_sea_source_vintages_2019_2025.csv`
- `data/asean_corroboration/economy_sea_revision_diagnostics.csv`
- `data/global_ecommerce/global_platform_vintage_diagnostics.csv`
- `scripts/analysis/build_asean_corroboration.py`
- `scripts/analysis/build_global_ecommerce_corroboration.py`

## 10. What the evidence establishes when read together

The combined evidence establishes a measurement-boundary result:

> Digital commerce is recorded through transaction, corporate-revenue,
> business-recordkeeping, market-estimate, statistical, and tax-administrative
> ledgers that measure different objects. Those measures can evolve
> differently, use incompatible perimeters, and revise the same historical
> period. No single public ledger is therefore a sufficient proxy for every
> dimension of platform-mediated commercial activity.

The digital element is not that gross-versus-net accounting began with online
platforms. It is that platforms coordinate large numbers of third-party
transactions and create granular private records while public corporate
accounts recognize the platform's own revenue under a different perimeter.
Digitalization can therefore increase private traceability at the same time
that public and institutional views remain fragmented.

This result preserves the original *Invisible Ledger* motivation in a form the
current evidence can support: the economically relevant activity is not
necessarily absent from every record; it is distributed across ledgers that
are not automatically comparable or linkable.

## 11. What is not an empirical finding

The current repository does not establish:

- a monetary amount of activity omitted from GDP;
- undeclared participant income;
- unpaid tax or tax evasion;
- an Indonesia-wide transaction-minus-revenue total;
- representative effects for all platforms or countries;
- business-level links between marketplace use and financial recordkeeping;
- institutional inability to link private platform records to tax or
  statistical records;
- causal effects of platform participation or reporting policy;
- final investor-market effects.

Those remain separate hypotheses, data-access questions, or future analyses.
They must not be presented as conclusions from the current evidence.

## 12. Current empirical conclusion

The defensible conclusion is not that transaction value missing from platform
revenue is missing from the economy. It is that the economic story changes
with the ledger observed. Indonesia provides the substantive country setting;
BPS describes the broader business population; ASEAN demonstrates recurrence,
heterogeneity, and revision sensitivity; and the global issuer histories show
that transaction activity and recognized revenue often follow materially
different trajectories.

The paper's strongest established contribution is therefore to identify and
measure where public transaction and revenue views cease to be interchangeable,
while documenting what additional participant-level and institutional linkage
would be required to infer hidden income, tax consequences, or omitted value
added.
