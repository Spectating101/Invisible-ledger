# Invisible Ledger research synthesis and manuscript bridge

**Status:** integration note based on the certified empirical branch and Box's
executed hypothesis tests. It does not select a final sample, claim advisor
approval, or revise the manuscript.

## The paper in one sentence

*Invisible Ledger* asks how the interpretation of Indonesia's digital
commercial transformation changes when platform transaction records, issuer
accounts, business participation, official statistics, and institutional
reporting systems are examined together rather than treating company revenue as
a sufficient view of the underlying activity.

The strongest current answer is:

> Transaction activity, recognized revenue, participating businesses, sales
> channels, and successive market estimates can evolve differently because
> they measure different economic objects. The resulting problem is not a
> proven stock of activity missing from GDP or tax records; it is a documented
> boundary and comparability problem whose institutional linkages remain only
> partly observed.

## Empirical architecture

```text
digital commercial event
  |
  +-- platform transaction record ------ issuer transaction disclosures
  |                                         |
  +-- company accounting record -------- issuer revenue/incentive disclosures
  |                                         |
  |                                         +--> within-issuer growth comparison
  |                                         +--> revenue-component reconciliation
  |
  +-- participating business ---------- BPS national/province publications
  |                                         |
  |                                         +--> business-count growth anatomy
  |                                         +--> sales-media composition
  |                                         +--> recordkeeping marginals
  |
  +-- regional market estimate --------- successive e-Conomy SEA vintages
  |                                         |
  |                                         +--> six separate country histories
  |                                         +--> revision sensitivity
  |
  +-- other platform business models --- global issuer filings/results
                                            |
                                            +--> external divergence check
```

These are complementary evidence families, not one pooled sample.

### Indonesia issuer layer

The all-tier inventory contains 17 matched annual candidate levels and 12
within-series transitions across five series. It includes direct
Indonesia-aligned, direct-but-scope-pending, and conditional country evidence.
Across the inventory, revenue grows faster in 10 transitions and transaction
value grows faster in two; two transitions have opposite signs. The 42.02
percentage-point median absolute divergence is an inventory diagnostic, not a
population effect.

The independent certification view uses 13 direct candidate periods, 12 with a
positive revenue denominator, and nine direct-candidate transitions. It adds
Blibli FY2020 prospectus evidence and excludes the conditional Grab and Shopee
constructions. It produces three sign reversals and a 42.94 percentage-point
median absolute divergence. The two summaries differ because they answer
different admission questions.

The evidence hierarchy is:

1. Tokopedia FY2022--FY2023: direct Indonesia-aligned segment evidence.
2. Blibli 3P: direct issuer evidence, but the segment includes online travel.
3. Bukalapak Group: direct issuer evidence, but overseas scope remains.
4. Grab: Indonesia revenue is direct; transaction value is constructed from a
   Group monetization rate.
5. Shopee: country transaction value is externally estimated and country
   revenue is constructed from a company-wide service rate.

Sources and outputs:

- `outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_levels.csv`
- `outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv`
- `docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md`
- `data/longitudinal/kong_empirical_candidate_table_2026-09-10.csv`

### Official Indonesia layer

BPS national evidence shows:

- total estimated e-commerce value rose from Rp1,100.87 trillion in 2023 to
  Rp1,288.93 trillion in 2024, or 17.08%;
- estimated e-commerce businesses rose from 3,816,750 to 4,400,972, or 15.31%;
- implied nominal value per estimated business rose 1.54%;
- the marketplace component rose from Rp200.68 trillion to Rp203.58 trillion,
  or 1.45%; and
- the non-marketplace component rose from Rp900.19 trillion to Rp1,085.35
  trillion, or 20.57%.

The marketplace amount for 2024 is directly reported in a BPS-authored source,
not reconstructed from the rounded share. These are national aggregate
estimates, not firm-panel outcomes or causal estimates of channel substitution.

The province layer contains 74 complete province-years across the 2023 and 2024
publications. It does not establish a stable association between marketplace
participation and financial-report ownership. The 2024 Pearson correlation is
approximately 0.022, and the within-province 2023--2024 Pearson correlation is
approximately 0.309. Province marginals cannot show whether the same businesses
both use marketplaces and maintain financial reports.

Sources and outputs:

- `data/bps_official/bps_crosswave_source_certification_2026-09-10.csv`
- `outputs/hypothesis_tests_2026-09-10/bps_national_growth_anatomy.csv`
- `outputs/hypothesis_tests_2026-09-10/bps_province_hypothesis_results.csv`
- `docs/BPS_CROSSWAVE_CERTIFICATION_2026-09-10.md`

### ASEAN corroboration layer

The ASEAN module contains 450 source-vintage rows that yield 42 latest-vintage
country-years across six countries. Its purpose is to establish recurrence,
country heterogeneity, and revision sensitivity. It does not pool different tax
systems or use an ASEAN aggregate to validate Indonesia allocations.

Successive reports revise earlier country-year estimates. Those revisions show
that the measured history of digital commerce depends partly on information,
scope, and publication vintage. They are not economic growth and are preserved
separately from canonical latest-vintage histories.

Sources and outputs:

- `data/asean_corroboration/`
- `reports/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md`

### Global issuer layer

The global corroboration module contains 48 matched issuer-years across eight
platform businesses, producing 40 within-issuer transitions. Eleven transitions
are conservatively scope-break flagged, leaving 29 clean-screened comparisons.
Revenue grows faster in 22 of those 29 and transaction value grows faster in
seven; four move in opposite directions.

This purposive disclosure sample is not representative of all global platforms.
It establishes that transaction/revenue divergence is not unique to one
Indonesian company, while leaving the cause to be diagnosed within each issuer.

Sources and outputs:

- `data/global_ecommerce/`
- `reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md`

## What explains the divergences

The analysis should not stop at observing different growth rates. Five distinct
mechanisms can cause transaction activity and recognized revenue to separate:

1. **Monetization:** commission, advertising, logistics, and financial-service
   revenue can change without an equivalent change in transaction value.
2. **Customer incentives:** incentives deducted from revenue can change net
   revenue even when gross commercial activity falls or grows slowly.
3. **Principal-versus-agent presentation:** a change in contractual
   responsibility can alter which gross or net amount is recognized.
4. **Business mix and perimeter:** marketplace, travel, payments, physical
   retail, overseas operations, and acquisitions can change the entity being
   measured.
5. **Publication basis:** restatements and later comparative vintages can change
   a historical value without representing new economic activity.

Tokopedia FY2022--FY2023 is the clearest mechanism example. Transaction value
fell approximately 8.90% while third-party net segment revenue rose about
53.20%. The reported revenue reconciliation attributes approximately 39.4% of
the net-revenue increase arithmetically to higher gross revenue and 60.6% to
lower customer incentives. This is a component reconciliation, not a causal
estimate, but it shows why company revenue and coordinated activity can give
opposite impressions.

The Blibli and global histories show that such divergence recurs, but each case
requires its own mechanism check. An early low or negative revenue base can
create a very large growth-rate difference without implying a comparably large
economic disconnection. This is why the evidence-tier medians are diagnostics,
not headline treatment effects.

## What makes this specifically a digital-economy question

Gross-versus-net accounting is not new. The digital feature is the scale and
distribution of third-party activity coordinated through platforms. A platform
can retain detailed private transaction records covering many independent
merchants, drivers, travellers, and customers while its public accounts report
only the revenue within the issuer's accounting perimeter.

Digitalization can therefore create two developments simultaneously:

- greater private traceability of transactions; and
- a public economic picture fragmented across firms, participants, channels,
  statistical estimates, and administrative systems.

BPS evidence is essential here because it shows that the phenomenon is broader
than listed marketplace companies. In 2023--2024, non-marketplace e-commerce
value grew far faster than the marketplace component, while business-count
growth accounted arithmetically for much of aggregate growth. Platform-company
accounts cannot reveal that participation and channel structure.

## What is established about institutional linkage

The repository establishes the following observation boundaries:

| Record | Directly visible in current evidence | Link not established in current evidence |
|---|---|---|
| Platform transaction flow | issuer/platform; partly public when disclosed | participant-level transfer to BPS or tax authorities |
| Recognized platform revenue | issuer, investor, public researcher | consistent denominator across business models |
| Merchant records | merchant; BPS through survey response | completeness, quality, and record-level linkage |
| Official statistics | BPS aggregate estimates | exact overlap with issuer-reported transactions |
| Tax information | existence of selected rules and collection statistics | taxpayer matching, liability, compliance, and transaction coverage |
| Payment records | potentially payment provider/regulator | a verified linked dataset bridging platform and merchant records |

The current finding is that linkage is **not established in the available
evidence**. It is not yet an empirical finding that the institutions themselves
are unable to link these records.

To strengthen this layer, the next evidence search should prioritize:

1. exact platform-reporting fields, taxpayer identifiers, coverage thresholds,
   effective dates, and implementation evidence;
2. BPS documentation describing use of administrative versus survey sources;
3. an official marketplace-by-financial-report cross-tabulation or approved
   business-level microdata; and
4. evidence showing whether payment, marketplace, merchant, and tax records can
   be matched without double counting.

## How the September manuscript maps to the rebuilt evidence

The September 9 manuscript is not discarded, but it cannot remain structurally
unchanged. Its conceptual discipline survives; its FY2023-only empirical centre
must be replaced.

| Existing manuscript element | Decision | Rebuilt role |
|---|---|---|
| Platform theory and revenue-recognition discussion | keep and deepen | conceptual foundation for why transaction and revenue differ |
| Information-reporting literature | keep, but stop before compliance claims | motivates the institutional-linkage question |
| Measurement identities and direct/derived labels | keep | definitions and evidence admission rules |
| FY2023 Grab/Tokopedia/Shopee source construction | retain, demote | conditional cross-sectional illustration and sensitivity |
| US$40.070bn combined residual | demote heavily | conditional historical illustration, not the main finding |
| FY2023 sensitivity tables | retain selectively | assumption-dependence evidence, not independent observations |
| Tokopedia gross/net comparison | retain and expand | first mechanism reconciliation in the main results |
| historical issuer ratios | replace with longitudinal growth analysis | test whether activity and revenue tell the same story |
| 47-quarter panel | supporting or optional | separate company-level evidence, never Indonesia country N |
| investor/event study | optional | include only if timing, contamination, and raw-price pipeline close |
| old ASEAN calibration | remove | replace with six separate country histories and vintage analysis |
| existing conclusion | rewrite | synthesize issuer, BPS, ASEAN, and global evidence |

The required change is therefore a **structural upgrade**, not a topic reset.
Sections on definitions, source discipline, Tokopedia accounting, and claim
boundaries remain valuable. The abstract, introduction, central results,
figures, ASEAN discussion, and conclusion must be rebuilt around longitudinal
evidence.

## Proposed result hierarchy for the rebuilt paper

1. **Core longitudinal result:** transaction activity and recognized revenue can
   provide materially different accounts of platform growth.
2. **Indonesia mechanism result:** Tokopedia's opposite-sign movement is partly
   reconciled through gross revenue and incentives.
3. **Indonesia economy result:** recent e-commerce growth is strongly associated
   arithmetically with expansion in estimated businesses, while non-marketplace
   channels account for most of the 2023--2024 value increase.
4. **Negative result:** province-level marketplace use does not establish a
   stable financial-recordkeeping relationship.
5. **ASEAN corroboration:** digital expansion recurs, but country institutions,
   market structures, and measurement vintages differ.
6. **Global corroboration:** transaction/revenue divergence recurs across
   platform business models, without validating Indonesia allocations.
7. **Synthesis:** the economic interpretation changes with the ledger observed;
   no single public ledger is a sufficient proxy for every dimension of digital
   commercial transformation.

## Claims that remain outside the evidence

The rebuilt paper must not claim that it has estimated:

- missing GDP or value added;
- undeclared participant income;
- unpaid tax or tax evasion;
- the complete Indonesian platform economy;
- a representative ASEAN or global effect;
- a business-level marketplace effect from province aggregates; or
- institutional inability to link records.

## Immediate research gates

Before manuscript reconstruction, the project should close or explicitly bound:

1. the advisor-approved Indonesia sample and treatment of Blibli, Bukalapak,
   Grab, and Shopee;
2. systematic revenue-component and comparable-basis reconciliations beyond
   Tokopedia;
3. the BPS financial-report question's cross-wave population and wording;
4. participant-level or official joint evidence for marketplace use and
   recordkeeping; and
5. implementation evidence for the proposed institutional visibility matrix.

The new evidence moves the project well beyond the one-year problem identified
by Professor Kong. It does not remove the need for her sample decision. The
research backend now supports a coherent longitudinal measurement study; the
current manuscript still describes the earlier FY2023-only implementation.
