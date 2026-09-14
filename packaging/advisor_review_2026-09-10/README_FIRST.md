# Invisible Ledger data review package

## Start here

Open `Invisible_Ledger_Data_Guide_2026-09-10.xlsx` first. It gives a compact
view of the proposed sample boundaries, the longitudinal issuer observations,
the BPS results, and the separate ASEAN, global, and quarterly modules.

The workbook is an inspection aid. The CSV files and original source documents
remain the evidence. The workbook does not replace or silently correct them.

## What this package is for

This package is designed to answer the sample and data questions raised before
the manuscript is rewritten:

1. Which multi-year Indonesia-aligned issuer or segment observations actually
   exist?
2. Which observations are directly reported, conditionally constructed,
   scope-pending, or excluded?
3. How do transaction activity and recognized revenue change within the same
   issuer series?
4. What separate evidence does BPS provide about the broader Indonesian
   e-commerce population?
5. Which ASEAN, global, and quarterly results are corroborating evidence rather
   than additional Indonesia observations?

## Package layout

```text
Invisible_Ledger_Advisor_Data_Review_2026-09-10/
├── 00_READ_FIRST/
│   ├── README_FIRST.md
│   ├── PACKAGE_FLOW.svg
│   ├── PACKAGE_FLOW.png
│   ├── ADVISOR_EMPIRICAL_DECISION_SHEET_2026-09-10.md
│   ├── RESEARCH_SYNTHESIS_AND_MANUSCRIPT_BRIDGE_2026-09-10.md
│   └── HYPOTHESIS_EXTENSION_PARTICIPANT_AND_INSTITUTIONAL_LINKAGE_2026-09-10.md
├── 01_INDONESIA_ISSUER/
│   ├── data/
│   ├── outputs/
│   └── notes/
├── 02_BPS_OFFICIAL/
│   ├── data/
│   ├── outputs/
│   └── source_documents/
├── 03_ASEAN_CORROBORATION/
├── 04_GLOBAL_CORROBORATION/
├── 05_QUARTERLY_SUPPORT/
├── 06_SCRIPTS/
├── 07_SOURCE_DOCUMENTS/
├── 08_MANIFESTS/
├── 09_ANALYTICAL_FIGURES/
├── Invisible_Ledger_Data_Guide_2026-09-10.xlsx
└── PACKAGE_CONTENTS.csv
```

## The evidence chain

```text
original source document
          |
          v
source-preserving CSV extract
          |
          v
module-specific analysis script
          |
          v
reported output and limitation
          |
          v
advisor sample decision
          |
          v
manuscript reconstruction
```

## How the modules relate

The modules are connected but must not be pooled as one dataset.

| Module | Unit | Purpose | Main boundary |
|---|---|---|---|
| Indonesia issuer | issuer/segment-year and within-series transition | Proposed main longitudinal measurement evidence | Geography and business perimeter require advisor decisions |
| BPS official | national year, province-year, or published business-level statistic | Broader business participation, sales channels, and recordkeeping | Not issuer data and not a causal firm panel |
| ASEAN | country-year and publication vintage | Recurrence, heterogeneity, and revision sensitivity | Countries retain separate tax and platform systems |
| Global issuer | issuer-year and within-issuer transition | Corroboration across platform business models | Purposive disclosure sample, not a representative global panel |
| Quarterly | company/segment-quarter | Historical accounting and source coverage | Not Indonesia-only and not part of the annual main sample |

## Current sample facts

- The candidate census has 21 rows because it preserves direct candidates,
  conditional constructions, and explicit exclusions.
- Thirteen direct candidate periods remain after hard exclusions.
- Twelve of those have positive revenue denominators.
- Nine direct-candidate annual transitions are currently usable.
- The older Grab/Shopee Indonesia constructions remain sensitivity evidence.
- Tokopedia FY2021 and Bukalapak FY2024 remain excluded for period mismatch.

These counts answer different questions. They must not be added together as one
sample size.

## Current empirical boundaries

- Transaction value minus platform revenue is not automatically missing GDP,
  merchant income, unpaid tax, or tax evasion.
- BPS business-level marketplace differences are associations, not causal
  marketplace effects.
- PMK 37/2025 establishes a legal reporting architecture. Implementation was
  postponed through 31 October 2026, so operating coverage and effects are not
  yet established.
- The ASEAN and global modules corroborate measurement problems while preserving
  country and business-model differences.
- The investor/CAR result and raw market-price layer are not included because
  they are not part of the currently closed empirical claims.

## Reproduction

Read `06_SCRIPTS/HOW_TO_REPRODUCE.md`. The package includes the scripts used for
the current module outputs and a package validator. Some historical scripts are
preserved for lineage but are not represented as turnkey reproduction code.
