# Research-direction handoff — 9 September 2026

This note preserves the reasoning and decisions behind the current empirical rebuild so another reviewer or agent can contribute without reconstructing the private conversation. It is not an advisor-facing manuscript, a transcript, or evidence that an expanded design has been approved.

Status labels:

- **Agreed** — explicitly settled by the researcher or directly instructed by the advisor.
- **Established** — supported by executed repository analysis or inspected source evidence.
- **Provisional** — a working interpretation or candidate design.
- **Unresolved** — requires evidence or a researcher/advisor decision.
- **Not investigated** — no adequate review has been completed.

The technical empirical baseline immediately before this handoff is commit 2ced0bf. Authoritative audit outputs are under outputs/empirical_backend_2026-09-09/; the principal narrative audit is reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md.

## 1. Current research question and intended answer

**Agreed enduring question:** How can the depth and movement of Indonesia's rapidly expanding digitally mediated economy be understood when relevant activity is recorded separately by platforms, participating businesses, payment systems, statistical agencies and tax authorities?

**Provisional operational question:** How does the growth of platform-mediated and digitally conducted commerce expose differences in coverage and economic meaning between transaction records, corporate revenue recognition, business financial recordkeeping and official economic measurement in Indonesia?

**Provisional substantive answer:** Indonesia has a large and growing digital commercial ecosystem, but no single public or private ledger describes it completely. Platform accounts show the corporate slice of selected transaction flows; BPS evidence shows that the broader e-commerce population extends well beyond marketplaces and that formal financial recordkeeping remains limited; issuer histories show that the relationship between transaction value and recognized revenue changes with monetization, incentives, business perimeter and accounting definitions. These sources are complementary evidence about visibility and measurement boundaries, not one pooled sample.

**Agreed elements that must remain central:**

1. The economically consequential activity of merchants, drivers and other participants, rather than the platform company alone.
2. The possibility that familiar firm-centred or official summaries do not communicate the full depth and dynamism of digital commercial activity.
3. Indonesia as the proposed main empirical setting, with ASEAN evidence separated as context or robustness.
4. An ambitious measurement question, not a paper whose only finding is the identity that transaction value exceeds platform revenue.

**Agreed claims abandoned:** transaction value minus platform revenue is not itself missing GDP, undeclared income, unpaid tax or tax evasion; the selected platforms do not estimate the entire Indonesian platform economy; the ecosystem-ratio arithmetic is not a prior-literature innovation.

**Unresolved:** whether the final paper's main contribution should be a longitudinal issuer/segment measurement study, a broader multi-ledger Indonesian measurement study incorporating BPS evidence centrally, or another empirical design approved by the advisor. The multi-ledger formulation is the current agent recommendation, not an advisor-approved replacement question.

## 2. Conceptual decisions and turning points missing from the technical audit

**Agreed / advisor-directed turning points:**

1. The earlier ASEAN architecture mixed countries, years, company-wide figures, country estimates and different regulatory environments too closely. The advisor required one consistent main sample.
2. The FY2023 Indonesia reconstruction solved part of the geography and provenance problem, including replacing GoTo Group with the more Indonesia-aligned Tokopedia e-commerce segment. It then created a new problem: a single fiscal year was explicitly judged insufficient for a master's thesis.
3. The advisor asked to review the dataset and derivations before another manuscript rewrite. The current priority is empirical coverage and sample agreement.
4. More years should be collected for Indonesia where possible. ASEAN-wide aggregation is unsafe without country-level comparability because countries differ in tax systems, regulation and platform business models.

**Researcher objections that shaped the rebuild:**

- The researcher rejected repeated attempts to defend a three-row FY2023 file as the complete empirical database.
- The researcher rejected an over-cautious rewrite that reduced the project to gross-versus-net accounting.
- The researcher wants the original ambition preserved: reveal economically important digital activity beneath simplistic descriptions of a relatively poor economy, while replacing the unsupported shortcut previously used to quantify it.
- The researcher strongly prefers empirical depth and robustness, but does not want row counts inflated by incompatible periods, source inputs, scenarios or overlapping totals.

**Agreed meaning of preserving the original ambition:** build a defensible empirical bridge from digital transaction activity to economic visibility and measurement. Do not return to a literal claim that a gross transaction residual can be added to GDP.

**What would count as losing the purpose again:** treating accounting-definition differences as the entire substantive result; making corporate disclosure comparability the only question; replacing the economic puzzle with an unrelated large-N dataset; or restoring national quantities that the evidence cannot identify.

## 3. Strongest findings at the current baseline

### Finding 1 — Digital commerce is large, growing and broader than major marketplaces

- **Status:** Established descriptively.
- **Evidence:** data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv; official BPS publications archived in sources/core_public_documents/; outputs/empirical_backend_2026-09-09/bps_province_panel_2023_2024.csv.
- **Finding:** BPS reports e-commerce transaction value of approximately Rp783 trillion in 2022, Rp1,100.87 trillion in 2023 and Rp1,288.93 trillion in 2024. Instant messaging is used by roughly 95 percent of e-commerce businesses, while exclusive marketplace transaction value is a minority of the broader total.
- **Conclusion supported:** platform issuer accounts cannot by themselves describe Indonesia's broader digital commerce.
- **Alternative explanation / limit:** BPS estimates already represent official attempts to measure this activity; broader digital commerce is not synonymous with unrecorded activity.

### Finding 2 — Formal financial recordkeeping remains limited

- **Status:** Established descriptively.
- **Evidence:** data/bps_official/ and outputs/empirical_backend_2026-09-09/bps_province_associations_by_year.csv.
- **Finding:** published national financial-report ownership among e-commerce businesses is 15.19 percent for 2023 and 17.15 percent for 2024.
- **Conclusion supported:** digital participation does not automatically imply conventional firm-level financial documentation.
- **Alternative explanation / limit:** owning financial statements is not equivalent to tax filing, reporting quality, auditability or authority access.

### Finding 3 — Marketplace use and financial-report ownership do not show one stable provincial relationship

- **Status:** Established from executed repository analysis.
- **Evidence:** scripts/analysis/build_comprehensive_empirical_audit.py; outputs/empirical_backend_2026-09-09/bps_province_associations_by_year.csv and bps_within_province_changes_2023_2024.csv.
- **Finding:** the positive provincial association visible in 2023 is weak or absent in 2024, and within-province changes are not robust.
- **Conclusion supported:** marketplace participation should not be portrayed as automatically formalizing business recordkeeping.
- **Alternative explanation / limit:** this is ecological province-level evidence, with only two waves and possible changes in survey composition; it is not a business-level causal test.

### Finding 4 — Platform transaction/revenue relationships are definition- and business-model-dependent

- **Status:** Established for documented comparisons; not a country-wide conclusion.
- **Evidence:** data/measurement/; data/longitudinal/; data/quarterly/clean_event_panel_accounting.csv; scripts/analysis/build_measurement_reconciliations.py.
- **Finding:** observed ratios and growth rates change with gross versus net revenue, incentives, principal-agent treatment, segment scope, acquisitions and deconsolidation.
- **Conclusion supported:** corporate revenue is a platform-boundary measure, not a stable proxy for the surrounding participant economy.
- **Alternative explanation / limit:** some changes are genuine economic changes in monetization or business model, not mere reporting artefacts.

### Finding 5 — Public evidence is fragmented across sources and scopes

- **Status:** Established as a reproducibility finding.
- **Evidence:** outputs/empirical_backend_2026-09-09/disclosure_matrix.csv, source_chain_status.csv, candidate_research_designs.csv and candidate_observation_census.csv.
- **Finding:** the audit finds no strict explicit-country direct annual transaction/revenue pairs. It identifies 14 Indonesia-aligned direct annual candidate periods across three issuers/segments, nine conditional Indonesia extension observations, and 47 company-quarter accounting records, but these are different evidence families.
- **Conclusion supported:** reconstructing comparable platform measures requires explicit scope and provenance rules.
- **Alternative explanation / limit:** disclosure fragmentation is not by itself proof of economic undermeasurement by BPS, tax authorities or other institutions.

**Connection beyond three obvious facts:** the evidence jointly shows a growing digital economy whose activity spans marketplace and non-marketplace channels; weak formal recordkeeping among many businesses; and corporate disclosures that observe only issuer-specific slices under changing definitions. The proposed substantive insight is the mismatch between economic activity and the institutional partitioning of information about it. Whether that insight is sufficiently original and consequential for the final thesis remains under review.

## 4. What makes the ledgers meaningfully misaligned

Different systems measuring different objects is ordinary and legitimate. Invisible Ledger should claim a consequential misalignment only when the separation obstructs a comparison, linkage or inference that an identified user needs.

| Visibility claim | Visible to whom | Established condition | Still hypothetical |
|---|---|---|---|
| Platform transaction flow | Platform; partly public researchers/investors when disclosed | Selected issuers record transaction value, but definitions and geography differ | Whether authorities receive transaction-level records and can link them to participants |
| Platform recognized revenue | Platform, investors, public researchers | Audited/reported revenue covers the platform's accounting boundary | Whether a selected revenue line is the best economic denominator across business models |
| Merchant activity and records | Merchant; BPS through survey response | BPS estimates channel use and financial-report ownership | Quality, completeness and linkability of each merchant's records |
| Payment flow | Payment provider; possibly regulators under specific rules | Not established as a linked dataset in the current repository | Whether payment records can bridge platform and merchant ledgers without duplication |
| Tax visibility | Taxpayer and tax authority under applicable reporting systems | Rules and selected collection statistics exist in supporting material | Actual taxpayer matching, compliance, liabilities and coverage |
| Official statistical visibility | BPS through surveys and administrative sources | BPS publishes e-commerce estimates by year and province | Exact overlap between BPS estimates and issuer-reported transactions |

**Established:** fragmentation of public disclosure, incomplete marketplace coverage of broader e-commerce, limited conventional business recordkeeping, delayed annual publication and inability in the repository to link issuer records to BPS businesses.

**Unresolved:** whether institutions themselves cannot link records; whether any amount is genuinely absent from official accounts; and the quantitative consequence of fragmentation for national economic measurement. The current data establish boundaries and incomplete public observability, not a quantified unrecorded national amount.

## 5. Relationship between platform and BPS populations

**Agreed:** they are complementary evidence about different populations. They must not be pooled as one sample.

- Issuer data describe selected listed companies or business segments.
- The FY2023 construction describes three selected Indonesia-focused platform cases using mixed directness classes.
- BPS estimates describe the population of Indonesian businesses selling or accepting orders online, including marketplace and non-marketplace channels.
- Province-level BPS tables are aggregate/ecological observations, not individual issuer or merchant records.

**Provisional bridge:** issuer data reveal what the platform corporate ledger contains; BPS data reveal the breadth, channels and recordkeeping characteristics of the business population outside any single issuer boundary. Their connection is conceptual and institutional, not a record-level match.

**Unresolved:** the researcher agrees that broader digital commerce belongs to the original motivation, but has not yet approved a final design in which the BPS module replaces the platform analysis as the main empirical contribution. Any such change also requires advisor agreement.

## 6. Changes since the reviewed baseline and source issues

**Latest reviewed technical baseline:** 2ced0bf.

**Authoritative outputs:**

- reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md
- reports/empirical_backend_audit_2026_09_09.html
- notebooks/empirical_backend_audit_2026_09_09.executed.ipynb
- outputs/empirical_backend_2026-09-09/candidate_observation_census.csv
- outputs/empirical_backend_2026-09-09/candidate_research_designs.csv
- outputs/empirical_backend_2026-09-09/source_chain_status.csv
- outputs/empirical_backend_2026-09-09/data_quality_issues.csv

**Tokopedia FY2021 — unresolved/excluded from a clean net-revenue series:** the previously flagged construction paired full-year pro-forma transaction value with revenue recognized only after the 17 May acquisition. It must remain excluded unless a genuinely period-matched pair under a consistent definition is recovered. Any candidate census row must be interpreted using its admission status rather than counted from its fiscal-year label.

**Blibli vintages — partially resolved:** a legacy 1Q23 column-mapping error was isolated. The official PDF is sources/core_public_documents/blibli_q12023_verified.pdf and the corrected extract is data/longitudinal/blibli_q1_2023_corrected_extract.csv. Other original-versus-comparative publication differences remain preserved in data/longitudinal/blibli_reporting_vintage_conflicts.csv. They are not separate observations and should not be silently overwritten.

**Current candidate counts under explicit rules:**

- strict explicit-country direct annual pairs: 0;
- Indonesia-aligned direct issuer/segment annual candidate periods: 14 across Blibli, Bukalapak and Tokopedia before final geography/scope admission;
- conditional Indonesia reconstruction periods: 9 across Grab, Tokopedia and Shopee;
- company/segment quarterly accounting inventory: 47;
- complete BPS province-years in retained 2023–2024 tables: 74.

These counts are alternatives or separate modules, never one combined N.

**Important non-result:** the YZUC/Refinitiv object advertised as 227 instrument-fiscal-year rows is an FY0 cross-sectional snapshot with missing fiscal-year fields. See outputs/empirical_backend_2026-09-09/yzuc_refinitiv_panel_assessment.csv.

## 7. Participant-side and institutional evidence

**Established public aggregate evidence:** BPS national indicators, province estimates, survey sampling context and questionnaires/publication metadata are preserved under data/bps_official/ and sources/core_public_documents/.

**Established published subgroup evidence:** a BPS analytical publication reports a stronger financial-report-ownership percentage for marketplace users than non-users. This is BPS's published analysis, not a new result from this project, and must be cited as such.

**Not acquired:** licensed business-level BPS microdata. The repository contains public aggregate tables, not respondent records.

**BPS variable meaning:** the retained public indicator measures whether a business has financial statements/reports as defined by the survey instrument. It does not measure tax filing, audited statements, complete bookkeeping, compliance or government access.

**Wave comparability:** national and province values for 2023 and 2024 have been extracted, but questionnaire wording, survey reference years, sampling changes and high-relative-standard-error cells require explicit checks before stronger longitudinal claims. The repository preserves a 2023 national-total inconsistency and a one-business 2024 province-sum discrepancy rather than resolving them silently.

**Administrative reporting:** the current repository has policy/rule and aggregate collection context, not linked evidence demonstrating actual participant-level reporting coverage or matching performance.

## 8. Literature and contribution state

**Established nearby literatures already identified:**

1. OECD/IMF work on digital-economy and digital-intermediation-platform measurement already establishes that digitalisation creates classification, attribution and compilation challenges.
2. National-accounts research already distinguishes conceptual coverage from practical compilation problems and warns against treating gross transaction value as value added.
3. Accounting research on revenue recognition and financial-statement comparability already establishes that economically similar transactions can be reported differently.
4. Third-party-information and platform-reporting literature already motivates why platform records can assist administration.
5. BPS's own publications already establish the scale, channels and recordkeeping characteristics of Indonesian e-commerce, including published marketplace comparisons.

**What is not novel:** that the digital economy is hard to measure; that GMV exceeds platform revenue; that small businesses often lack formal accounts; or that platform information may aid tax administration.

**Provisional contribution that may be distinctive:** a source-auditable Indonesian reconciliation showing how these known issues intersect across selected issuer disclosures, longitudinal reporting changes, marketplace/non-marketplace business channels and official recordkeeping estimates—and identifying exactly which economic conclusions survive or fail when the ledgers are aligned by scope.

**Unresolved:** no exhaustive systematic literature review has yet certified that this exact reconciliation is absent from prior work. Most full-text review completed so far concerns official measurement frameworks, source documents and selected related research; the closest-study map remains a useful independent-review task.

## 9. Agreed completion scope with the researcher and advisor

**Advisor-directed:** Indonesia is the proposed main market; one FY2023 fiscal year is insufficient; sources and Grab's derivation must be explicit; different samples must not be mixed in the main results; other countries may be robustness evidence; the dataset should be reviewed before further manuscript rewriting.

**Not advisor-approved:** the 14-period issuer/segment candidate design, the nine-period conditional reconstruction, a BPS-centred redesign, the multi-ledger research question above, or any advertised final N.

**Researcher preference:** retain the original economic ambition, maximize valid empirical depth, keep Indonesia central if feasible, use ASEAN evidence without aggregating unlike countries, and finish the empirical backend before another wholesale manuscript rewrite.

**Provisional main contribution:** longitudinal Indonesian platform/segment measurement combined with an explicitly separate BPS visibility/recordkeeping module.

**Supporting:** FY2023 conditional cases, company-quarter evidence, ASEAN context and policy evidence.

**Optional/exploratory:** event-study return analysis unless timing, contamination and market-data interpretation are fully closed.

## 10. Most useful non-duplicative contribution from another thread

**Ready for independent review:**

- evidence-to-claim logic in Sections 1–5 of this note;
- closest-literature mapping and novelty assessment;
- alternative explanations for the BPS and issuer findings;
- eligibility decisions in candidate_observation_census.csv;
- whether the 14-period direct issuer/segment candidate set is sufficiently coherent;
- whether the multi-ledger structure produces an affirmative economic conclusion rather than a catalogue of limitations.

**Current work already completed:** broad source recovery, source profiling, candidate census construction, BPS extraction and descriptive analyses, Blibli correction, YZUC/Refinitiv field audit, validation scripts, audit report and reproducible notebook.

**Avoid changing without an explicit decision:**

- docs/CURRENT_STATUS.md sample-approval language;
- source files in sources/core_public_documents/;
- legacy exclusions;
- direct/derived classifications;
- the proposed main geography;
- or the manuscript as though a new main design had already been approved.

**Best complementary contribution:** challenge the evidence-to-claim bridge. Identify the closest prior studies, specify what ordinary division of measurement responsibilities would explain, and determine what additional result would make the observed fragmentation economically consequential. Then help translate only the verified findings into a coherent paper argument after the sample decision.

## Short orientation for a new reviewer

The project did not move from a good ASEAN paper to a small Indonesia paper because the economic motivation disappeared. It moved because the original calculations combined incompatible geography and treated a corporate accounting residual as more economically revealing than the data allowed. The FY2023 reconstruction repaired provenance but became temporally inadequate. The current expansion therefore seeks a multi-year Indonesia evidence base while preserving the wider question: whether a large, rapidly changing digital commercial ecosystem is adequately understood when its activity is partitioned across separate institutional records.

The repository now has materially more evidence than three rows, but it does not yet have an advisor-approved final main sample. The correct next intellectual task is to decide which verified evidence answers the enduring question, not to maximize a headline row count or write another defensive manuscript.
