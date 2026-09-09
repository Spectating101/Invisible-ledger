# Invisible Ledger

Research repository for **The Invisible Ledger**, a thesis project on the measurement and disclosure boundaries of platform-mediated economic activity in Indonesia, with separate historical and ASEAN evidence.

The project asks how platform transaction flows relate to revenue recognized by the platform, what participant-side activity remains outside that corporate revenue boundary, and what can—and cannot—be inferred for economic statistics and tax administration.

## Current status

This repository is a **working research archive**, not a claim that the empirical design has been approved or that every dataset is mutually comparable.

- Indonesia remains the proposed main geography.
- FY2023 is the cleanest cross-platform comparison, but a one-year main sample has been judged insufficient for the master's thesis.
- The active expansion therefore concentrates on a longitudinal Indonesia design using additional years and issuers where source definitions permit.
- ASEAN material is kept separately as context or robustness evidence. It must not be pooled as though ASEAN were one tax or regulatory system.
- The transaction–revenue difference is not automatically missing GDP, participant income, unpaid tax, or tax evasion.
- Investor-event results remain exploratory while event contamination and information timing are unresolved.

Read [AGENTS.md](AGENTS.md), [docs/CURRENT_STATUS.md](docs/CURRENT_STATUS.md), and [data/README.md](data/README.md) before using the files.

## Repository map

```text
Invisible-ledger/
├── AGENTS.md
├── docs/                       # research history, method, status, limitations
├── papers/
│   ├── current/                # current working manuscript
│   ├── milestones/             # representative historical versions
│   └── proposals/              # proposal versions; not all are current
├── data/
│   ├── indonesia_fy2023/       # the reviewed three-case construction
│   ├── longitudinal/           # multi-year candidates and historical extracts
│   ├── quarterly/              # 47-quarter panel and source reconciliation
│   ├── measurement/            # accounting/scope reconciliation exercises
│   ├── market/                 # preserved price data and exploratory outputs
│   ├── asean_context/          # country-level context kept separate
│   └── legacy_not_active/      # preserved but prohibited as active evidence
├── scripts/
│   ├── acquisition/
│   ├── extraction/
│   └── analysis/
└── sources/
    ├── manifests/              # URLs, checksums, procurement and file lineage
    └── core_public_documents/  # selected load-bearing public filings/releases
```

## Core measurement

For transaction value `V` and selected platform revenue `R`:

```text
difference = V - R
ecosystem ratio = (V - R) / R
take/monetization rate = R / V
ecosystem ratio = 1 / take rate - 1
```

The ratio is an author-constructed descriptive transformation. Where a country value is derived using an assumed take rate, the resulting ratio is mechanically implied by that assumption; it is not an independently estimated structural parameter.

## Reproduction boundary

The repository preserves original project scripts as well as later acquisition and reconciliation scripts. Some historical scripts retain their original directory assumptions and are included for lineage, not as a turnkey pipeline. See [scripts/README.md](scripts/README.md).

Large downloaded source archives, private correspondence, chat histories, administrative forms, credentials, and licensed database exports are intentionally not committed. Their public-source URLs and checksums are retained where appropriate.

