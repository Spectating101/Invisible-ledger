# Proposal preemptive review map

**Purpose:** anticipate the next round of small but consequential review comments by applying the logic of the advisor's earlier questions. This document is an internal quality-control instrument, not correspondence and not evidence of advisor approval.

## How to use this map

The earlier comments reveal a consistent review standard:

```text
What exactly is the observation?
        ↓
Is its geography, period, and business scope what the paper says it is?
        ↓
Is the quantity observed or constructed?
        ↓
Is it comparable with the other rows?
        ↓
Does the interpretation follow from the measurement?
```

The proposal should answer those questions before presenting any result. The following comments are therefore predictable even if they have not yet been made explicitly.

## Resolution status

This map is not merely a list of future tasks. The accompanying machine-readable tracker records **29 controls**:

- **19 resolved in the empirical backend**;
- **5 partially resolved** and requiring a bounded methodological completion;
- **3 requiring an advisor sample decision** rather than an agent assumption;
- **1 dependent on future event-study work**; and
- **1 not yet applied to the authoritative proposal document**, although proposal-ready text exists.

Tracker: `data/quality_control/proposal_preemptive_review_resolution_status_2026-09-11.csv`.

“Resolved in the backend” means that the evidence, exclusion, calculation, or claim boundary has been implemented and documented. It does not mean that the corresponding wording has already been inserted into the final proposal file or approved by the advisor.

## Priority 1 — comments likely to affect sample approval

| Likely review question | Why it will arise | Preemptive proposal treatment | Current status |
|---|---|---|---|
| What is the final main sample? | Several candidate boundaries remain possible | State one proposed boundary and show excluded, conditional, and supporting records separately | Unresolved pending advisor decision |
| Are Blibli's activities actually Indonesian? | Its 3P segment includes online travel, which may involve overseas destinations | Describe the issuer/segment perimeter precisely; do not claim every transaction occurred domestically | Scope pending |
| Can Bukalapak Group be called Indonesia-only? | Its reports identify overseas operations | Keep it scope-pending or supporting unless a compatible Indonesia allocation is found | Scope pending |
| Why include Grab and Shopee if their country figures are constructed? | Their Indonesian transaction/revenue pairs are not both directly disclosed | Put them in a labelled conditional sensitivity tier, not among equivalent direct observations | Resolved methodologically; final role pending |
| Why exclude Tokopedia FY2021 and Bukalapak FY2024? | Superficially they look like additional years | State the exact period mismatch: full-year/pro-forma versus partial consolidation, and nine-month TPV versus twelve-month revenue | Hard exclusions established |
| Does the multi-year design still use the same companies every year? | The panel is unbalanced | State that it is an unbalanced evidence panel governed by consistent eligibility rules; do not force a balanced panel through imputation | Proposed treatment established |
| Is this a company panel or an Indonesia market panel? | Some records are country, some segment, some issuer scope | Define the main design as Indonesia-aligned issuer/segment evidence and disclose the evidence tier; do not use the phrase “country panel” without qualification | Wording control required |

## Priority 2 — comments likely to affect measurement credibility

| Likely review question | Preemptive answer/control | Repository evidence |
|---|---|---|
| Are GMV, GTV, and TPV the same thing? | No. Preserve issuer terminology and definition; harmonize only when the economic perimeter is sufficiently comparable | `data/definition_audit/`; issuer source notes |
| Do the transaction measures include cancelled, returned, refunded, or unsettled orders? | Record each issuer/source definition. Do not describe all transaction metrics as completed sales | Definition map and source locators |
| Why use net revenue for one platform and service or gross revenue for another? | Choose the closest consistent concept, show alternatives where available, and treat denominator choice as definition sensitivity | Tokopedia and Blibli component reconciliations |
| Are customer incentives deducted from revenue? | Extract gross/pre-promotion revenue, incentives, and net revenue separately when disclosed | Tokopedia FY2022–FY2023 and Blibli reconciliations |
| Could a principal-versus-agent change explain revenue growth? | Flag business-model/accounting-perimeter changes and use issuer-provided comparable bases when available | Grab and global issuer definition maps |
| Are annual ratios averages of quarterly ratios? | No. Annual ratios must be computed from annual transaction and annual revenue totals | Methodology rule |
| Are fiscal years aligned across issuers? | Store fiscal period start/end and explain material year-end differences; do not equate a March year with a December year silently | Period metadata required in final table |
| Are currencies converted consistently? | Preserve native currency for within-platform changes; use an explicit dated FX source only for cross-platform display | World Bank FX source and source-input files |
| Were rounded values used to manufacture precision? | Report source precision and avoid re-dividing rounded headline values when the issuer directly states the rate | Sea 10.0% rate treatment; Blibli vintage sensitivity |
| Which publication vintage is canonical? | Prefer the latest comparable/restated value for analysis while retaining original vintages and testing whether the choice is load-bearing | Blibli vintage diagnostics |

## Priority 3 — comments likely to affect statistical interpretation

| Likely review question | Preemptive answer/control |
|---|---|
| What is N? | Report firms, segments, period-level observations, usable transitions, and excluded records separately. Never sum source inputs, annual totals, quarters, vintages, and scenarios into one N. |
| Are repeated years independent observations? | No. They are within-platform longitudinal observations. Do not imply 19 independent firms. |
| Why use medians or growth-divergence statistics? | Explain that distributions are small, heterogeneous, and sensitive to extreme early revenue bases; report every platform path alongside summaries. |
| Does the transaction–revenue identity predetermine the result? | Yes, the level difference is positive whenever revenue is below transaction value. The informative tests concern changes over time, sign reversals, revenue components, and sensitivity to definitions. |
| Are sensitivity ranges confidence intervals? | No. Label them scenario or assumption ranges and explain their basis. |
| Why not interpolate missing years? | Missingness reflects non-disclosure and scope incompatibility; interpolation would create unobserved issuer facts. |
| Is missing disclosure itself causing sample selection? | Yes. State that admission favors publicly disclosed and often listed platforms. Treat this as a limitation and potential visibility finding, not proof about excluded firms. |
| Is market-share coverage equivalent to representativeness? | No. Report value coverage separately from merchant, sectoral, regional, and tax-liability representativeness. |
| Are platform-level observations pooled with BPS businesses or provinces? | No. These are complementary levels of evidence and must not enter one regression or one N. |

## Priority 4 — comments likely to affect the BPS module

| Likely review question | Preemptive answer/control |
|---|---|
| Does “2024 survey” describe 2024 economic activity? | Not automatically. State survey wave and economic reference year separately for every indicator. |
| Are the 2023 and 2024 questionnaires identical? | Only compare fields after wording, eligibility, denominator, and skip-pattern concordance. Keep the financial-report trend guarded until this is closed. |
| Are the province correlations business-level evidence? | No. Treat them as ecological diagnostics. Use BPS's published business-level comparisons for participant-side associations. |
| Does marketplace participation cause better recordkeeping? | Not established. More formal businesses may select into marketplaces; say “associated with,” not “caused by.” |
| What does “financial statements” mean? | Use BPS's definition: separable business accounts including income, assets, and liabilities. It is not tax filing, audited quality, or mere sales logging. |
| Were survey weights and design used? | Published BPS estimates may be cited as published. Independent microdata analysis must use the released weights and available design information. |
| Are 40,066 selected businesses equal to usable released records? | No. That is a survey-selection figure, not the final response or complete-case N. |
| Can marketplace and non-marketplace activity be treated as mutually exclusive? | Only for the specific BPS decomposition whose categories are exclusive; other multiple-response sales-media tables answer a different question. |

## Priority 5 — comments likely to affect the tax discussion

| Likely review question | Preemptive answer/control |
|---|---|
| Are merchants already legally required to pay tax? | Yes, subject to the applicable rules. PMK 37/2025 changes the collection/reporting mechanism; it does not create the underlying income-tax obligation. |
| Does the 0.5% apply to all online merchants? | No. State thresholds, declarations, taxpayer treatment, and statutory exclusions from the regulation. |
| Is transaction value the tax base? | Not automatically. PMK uses covered seller gross turnover recorded in transaction documents; issuer GMV/GTV/TPV definitions are not interchangeable with taxable turnover. |
| Does the residual estimate unpaid tax? | No. It contains merchant proceeds and potentially taxes, refunds, incentives, third-party fulfilment, and other amounts depending on the source definition. |
| Does the appointment of marketplaces prove past underpayment? | No. It proves an administrative design and policy concern, not a quantified compliance failure. |
| Has the policy already produced observable effects? | No defensible post-policy effect is available as of 11 September 2026 because implementation was postponed through 31 October 2026. |
| Why are only four marketplaces named? | Report the legal appointments and their estimated market-value coverage. Do not assume the initial list exhausts all marketplaces or digital sales channels. |
| What about TikTok Shop? | Distinguish the consumer-facing brand from the post-combination PT Tokopedia legal/perimeter structure. It was not separately named in the initial four appointments. |
| What about non-marketplace sales? | State that websites, messaging, social media, bank/payment records, and merchant accounts may create other traces; the study has not established their administrative linkage. |
| Is the paper estimating tax evasion? | No. Its tax contribution concerns the informational distinction and potential linkage among transaction, seller, corporate, and administrative records. |

## Priority 6 — comments likely to affect ASEAN and global robustness

| Likely review question | Preemptive answer/control |
|---|---|
| Why include ASEAN after being asked to focus on Indonesia? | Use it only to test recurrence and measurement sensitivity, after the Indonesia analysis. It does not enlarge the main Indonesia N. |
| Can ASEAN countries be pooled? | Not under the current design. Preserve country histories and identify tax, platform, currency, source, and regulatory differences. |
| Are country GMV estimates directly comparable? | Not automatically. Retain source definitions and publication vintages; use revisions as a measurement result rather than hiding them. |
| Does the global issuer module validate Indonesia? | No. It demonstrates that transaction/revenue divergence recurs under different business models. It cannot validate country allocations. |
| Is the global panel representative? | No. It is a disclosure-selected corroboration sample of eight platform businesses. |
| Why exclude Amazon, Alibaba, PDD, or Coupang? | State the source-availability/perimeter reason for every exclusion rather than selecting only favorable results. |

## Priority 7 — comments likely to affect novelty and contribution

| Likely review question | Preemptive answer/control |
|---|---|
| Isn't transaction value simply larger than revenue by definition? | The contribution is not that identity. It is the longitudinal reconciliation showing when activity and revenue tell different growth stories and which incentives, monetization, or perimeter changes explain them. |
| What is new beyond BPS's own marketplace study? | BPS supplies participant-side evidence. The project contributes a cross-ledger reconciliation linking issuer activity/revenue, business records/channels, and the legal reporting architecture. |
| Is this an accounting paper rather than finance/economics? | Frame the economic problem as information comparability: different records change conclusions about scale, growth, monetization, and observability. Accounting mechanisms are explanations, not the entire contribution. |
| Does it show GDP is wrong? | No. It shows that firm revenue and selected platform metrics are incomplete descriptions of digital-commercial activity. National-accounts inclusion requires separate supply-use and value-added evidence. |
| What affirmative result remains after all caveats? | Transaction and revenue growth can diverge materially; participant growth and non-marketplace activity explain dimensions not visible in issuer revenue; public and administrative visibility depends on channel and institutional linkage. |
| What would falsify or weaken the argument? | Stable matched activity/revenue growth, evidence that apparent divergence disappears under compatible definitions, or comprehensive linkage of participant/channel records into official systems would weaken stronger fragmentation claims. |

## Priority 8 — comments likely to affect reproducibility and presentation

| Likely review question | Preemptive answer/control |
|---|---|
| Can each table be reproduced? | Maintain a table/figure map from source file to extract to script to output. Mark any manually transcribed step. |
| Are source documents included? | Archive unchanged issuer filings and official documents where licensing permits; distinguish downloaded originals from generated extracts. |
| Did the script actually generate the workbook shown? | Record script and output version hashes. Do not claim lineage where script/output versions differ. |
| Are source URLs enough? | No. Include file, page/table/line, accessed date, unit, and exact measure. |
| Are formulas hidden in Excel? | Put essential formulas in the methods text and machine-readable scripts; the workbook is an inspection interface, not the sole method record. |
| What is final versus preliminary? | Use explicit statuses in filenames/indexes and keep legacy/not-final results outside the active result layer. |
| Why are there several sample counts? | Present a small count reconciliation showing the eligibility universe, positive-denominator subset, executed analysis set, and sensitivity tiers. |
| Do figures mix scopes? | Put geography, business perimeter, period, currency, and evidence tier in every table/figure note. |

## Minimum proposal table set

The proposal can answer most anticipated comments with five disciplined tables:

1. **Candidate sample and admission table** — platform, years, geography, business scope, direct/derived status, admission status.
2. **Variable-definition table** — issuer terminology, inclusion/exclusion of refunds/returns, revenue basis, incentives, principal/agent treatment.
3. **Source and derivation table** — exact source, locator, formula, unit, vintage.
4. **Empirical-module table** — issuer panel, BPS, ASEAN, global, tax institution; unit and purpose of each.
5. **Claim-boundary table** — what each result establishes and what it does not establish.

These are proposal design tables. They should not be mistaken for five separate analytical samples.

## Short verbal explanation for a meeting

> The earlier problem was not simply that one file had too few rows. The main tables mixed periods, geographies, and disclosure types without a single admission rule. The revised design is longitudinal and Indonesia-centred. It separates directly reported issuer pairs from conditional country reconstructions, excludes period mismatches, and uses BPS, ASEAN, global issuers, and tax rules as separate evidence modules. The tax interpretation is informational rather than accusatory: marketplace records can link sellers and turnover in ways that public platform revenue cannot, but the analysis does not estimate unpaid tax. Every observation retains its source, definition, period, geography, and derivation status so the sample decision can be reviewed before the final analysis.

## Stop conditions before calling the proposal ready

The proposal is not ready for final circulation if any of the following remains hidden:

- the proposed main-sample boundary;
- the status of Blibli travel scope and Bukalapak overseas operations;
- the difference between direct issuer records and conditional country estimates;
- the definition of the selected transaction and revenue measures;
- fiscal-period or restatement differences;
- the distinction between market coverage and representativeness;
- the fact that the tax mechanism was postponed and has no measurable post-period yet;
- the separation of the Indonesia, BPS, ASEAN, and global empirical populations; or
- the distinction between descriptive association and causal effect.
