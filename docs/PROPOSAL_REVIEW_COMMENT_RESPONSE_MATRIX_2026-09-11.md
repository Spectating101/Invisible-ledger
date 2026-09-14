# Proposal review-comment response matrix

**Purpose:** translate the advisor's data and interpretation comments into concrete proposal requirements. This is an internal drafting control, not correspondence and not a claim that the expanded sample has been approved.

## Summary

The comments do not require abandoning the research question. They require the proposal to stop presenting different empirical layers as one interchangeable sample. The proposal should define one proposed longitudinal Indonesian issuer design, disclose the status of every observation, and keep BPS, ASEAN, global issuers, tax institutions, and the FY2023 cross-section in separately labelled roles.

## Comment-by-comment controls

| Review concern | Required proposal response | Evidence already available | Remaining decision |
|---|---|---|---|
| The early tables used different years and geographic samples | Define the proposed main empirical unit once and apply it throughout the main analysis | `data/longitudinal/advisor_empirical_candidate_table_2026-09-10.csv`; `docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md` | Final admission of Blibli and Bukalapak scope requires advisor agreement |
| FY2023 alone is insufficient | State the complete longitudinal coverage and treat FY2023 only as a common market snapshot | 13 direct candidates spanning FY2019–FY2025; six conditional country reconstructions spanning FY2021–FY2024 | Select the final longitudinal boundary after scope review |
| GoTo Group activity may include activity outside Indonesia | Do not use GoTo Group as an Indonesia observation; use the Tokopedia e-commerce segment and describe it as Indonesia-aligned rather than literally country-disclosed | Tokopedia FY2022 and FY2023 GTV and net third-party segment revenue in GoTo FY2023 annual report | Whether an Indonesia-aligned segment satisfies the main-sample rule |
| Verify whether transaction value and revenue are disclosed at country level | Include an evidence-status column: direct country, direct segment, scope-pending issuer, external estimate, or derived | Candidate census and source-input tables preserve these distinctions | Strict direct-country matched pairs remain unavailable |
| Explain Grab's transaction-value derivation | Present the formula, inputs, and assumption separately for each retained year | Grab Indonesia revenue is direct for FY2021–FY2023; Group revenue and Group GMV are source-reported | Whether the Group monetization rate is acceptable only as sensitivity or may appear in the main comparison |
| Clarify why transaction value minus platform revenue could matter for tax reporting when merchants may already be taxed | Recast the measure as an information/accounting boundary; use PMK 37/2025 to show why seller turnover and platform revenue are distinct administrative objects | Official Ministry/DJP regulation, guidance, appointment, and postponement documents | Post-implementation compliance effects are not yet observable |
| Cite every platform source separately | Provide source, locator, period, geography, measure, definition, and direct/derived status at row level | Existing source-input CSVs and source locators | Proposal tables must inherit those fields rather than cite one generic source note |
| Other ASEAN countries may be retained as robustness evidence | Keep six country histories separate; control for country-specific tax rules, platforms, definitions, and source revisions; do not pool them as one treatment sample | `data/asean_corroboration/` and its design rules | Exact robustness specification follows approval of the Indonesia core |
| Establish how much of the market the selected evidence covers | Report market-value coverage separately from analytical paired-measure coverage | 2023 marketplace-share table; 2022–2025 platform snapshots | High GMV coverage does not establish merchant representativeness |

## Proposed main-sample statement

> The proposed main analysis is a longitudinal study of Indonesia-aligned platform or issuer segments for which transaction value and a matching revenue measure can be traced to the same period and business perimeter. Direct issuer observations are separated from conditional country reconstructions. FY2023 remains a common cross-platform illustration, but the longitudinal candidate evidence spans FY2019–FY2025. Observations with unmatched periods are excluded, and observations with unresolved geographic or business scope are presented as pending admission rather than silently treated as Indonesia-only.

This statement should appear once in the research design and govern the first main empirical tables. Subsequent modules must identify themselves as sensitivity, official-statistics evidence, institutional context, or external corroboration.

## Worked Grab derivation requested in the review

Grab reports Indonesia revenue but not Indonesia GMV. For each year `y`, the conditional construction is:

```text
Group monetization rate_y = Group revenue_y / Group GMV_y

Conditional Indonesia GMV_y = Indonesia revenue_y / Group monetization rate_y
```

Equivalent expression:

```text
Conditional Indonesia GMV_y
    = Indonesia revenue_y × Group GMV_y / Group revenue_y
```

| Year | Indonesia revenue | Group revenue | Group GMV | Conditional Indonesia GMV | Status |
|---|---:|---:|---:|---:|---|
| FY2021 | US$79m | US$675m | US$16,061m | US$1,879.732m | Derived using Group rate |
| FY2022 | US$275m | US$1,433m | US$19,937m | US$3,826.012m | Derived using Group rate |
| FY2023 | US$605m | US$2,359m | US$20,983m | US$5,381.397m | Derived using Group rate |

Proposal interpretation:

> This allocation assumes that Grab's Indonesian activity has the same revenue-to-GMV relationship as the Group. The assumption is transparent and testable through sensitivity ranges, but the resulting country GMV is not a direct company disclosure and is not independent evidence of an Indonesia-specific monetization rate.

Sources and locators are stored in `data/longitudinal/indonesia_extension_source_inputs.csv` and `data/indonesia_fy2023/fy2023_indonesia_source_inputs.csv`.

## Country and business-scope disclosure table

The proposal should include, or reproduce the substance of, this table:

| Series | Periods | Transaction measure | Revenue measure | Geographic status | Proposed role |
|---|---|---|---|---|---|
| Tokopedia e-commerce | FY2022–FY2023 | Direct segment GTV | Direct net third-party segment revenue | Indonesia-aligned segment; not literal country line | Strongest direct core candidate |
| Blibli 3P retail | FY2019–FY2025 | Direct segment TPV | Direct segment net revenue | Issuer/segment scope; includes online travel | Core candidate pending scope approval |
| Bukalapak Group | FY2020–FY2023 | Direct Group TPV | Direct Group revenue | Group reports overseas operations | Supporting or core only if geography accepted |
| Grab Indonesia | FY2021–FY2023 | Derived from direct country revenue and Group rate | Direct country revenue | Explicit country revenue; derived country activity | Conditional sensitivity |
| Shopee Indonesia | FY2022–FY2024 | External market estimate | Derived using Group service monetization | Country activity externally estimated | Conditional sensitivity |

This is the proposal's most important safeguard against another sample-scope objection.

## Tax-reporting clarification

The proposal should not say that the transaction–revenue difference is a tax gap. The correct hierarchy is:

```text
platform transaction value
    != platform corporate revenue
    != merchant taxable turnover or profit
    != unpaid tax
```

The tax relevance is informational:

> Marketplace records can contain seller identity and transaction-linked turnover information that is absent from the marketplace operator's public corporate revenue. PMK 37/2025 demonstrates the institutional relevance of that distinction by assigning designated marketplaces a withholding and reporting role. The regulation is officially described as a change in collection mechanism, not proof of prior underpayment. Accordingly, the empirical transaction–revenue difference is interpreted as a measurement boundary, not as tax evasion or a tax-liability estimate.

Primary sources:

- Ministry of Finance, [PMK 37/2025](https://www.jdih.kemenkeu.go.id/dok/pmk-37-tahun-2025/files).
- Directorate General of Taxes, [marketplace withholding guidance](https://pajak.go.id/marketplace).
- Directorate General of Taxes, [appointment of four marketplaces](https://pajak.go.id/id/siaran-pers/pemerintah-implementasi-pmk-372025-melalui-penunjukan-empat-marketplace-sebagai).
- Directorate General of Taxes, [implementation postponement](https://pajak.go.id/index.php/id/pengumuman/penundaan-waktu-pemberlakuan-ketentuan-pemungutan-pph-pasal-22-oleh-marketplace).

## Market-coverage clarification

The 2023 commercial estimate provides a transparent common denominator:

| Coverage definition | Share of estimated 2023 platform GMV | Interpretation |
|---|---:|---|
| Shopee + Tokopedia | 70% | Original marketplace cases; evidence strength differs |
| Shopee + Tokopedia + Blibli | 74% | Platforms with current issuer evidence; Blibli remains scope-pending |
| Four marketplaces designated in July 2026 | 83% | Contextual comparison using a later policy designation |
| Five named 2023 market leaders | 94% | Market-activity coverage, not matched accounting coverage |

Proposal wording:

> The platform evidence covers a substantial share of estimated marketplace transaction value, but market-value coverage and analytical comparability are different properties. The study therefore reports both the share of market activity represented by named platforms and the narrower share for which matching issuer transaction and revenue measures are available.

Do not describe these percentages as the share of merchants, tax liabilities, total digital commerce, or the national economy.

## ASEAN robustness control

The regional section must preserve the advisor's country-heterogeneity concern:

> ASEAN evidence is analyzed as six country-specific histories rather than a pooled regional tax sample. The countries differ in marketplace structure, tax instruments, implementation dates, business models, currencies, and source definitions. The regional evidence tests whether digital-commercial expansion and measurement sensitivity recur across settings; it does not apply an Indonesian transaction–revenue ratio or tax interpretation to the region.

This treatment retains the original regional motivation while avoiding the earlier aggregation error.

## Final proposal checklist

- [ ] Main geography and unit of observation defined before the hypotheses.
- [ ] FY2019–FY2025 longitudinal coverage stated; FY2023 not described as the entire dataset.
- [ ] Same admission rule used in all main-result tables.
- [ ] Every series marked direct, segment, scope-pending, external, or derived.
- [ ] Grab derivation and assumption displayed explicitly.
- [ ] Tokopedia described as Indonesia-aligned segment, not an explicit country line.
- [ ] Blibli travel scope and Bukalapak overseas scope disclosed.
- [ ] Transaction–revenue difference not called GDP, undeclared income, unpaid tax, or tax evasion.
- [ ] PMK 37/2025 presented as institutional motivation, with postponement disclosed.
- [ ] Market share described as value coverage, not representativeness.
- [ ] ASEAN and global evidence placed after the Indonesia main analysis and kept unpooled.
- [ ] Post-policy tax effects identified as future research until operational data exist.

