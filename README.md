# Invisible Ledger

Research repository for **The Invisible Ledger**, a thesis project on the measurement and disclosure boundaries of platform-mediated economic activity in Indonesia, with separate historical and ASEAN evidence.

The project asks how platform transaction flows relate to revenue recognized by the platform, what participant-side activity remains outside that corporate revenue boundary, and what can—and cannot be inferred for economic statistics and tax administration.

For the reasoning behind the current rebuild—including agreed decisions, provisional interpretation, strongest findings, unresolved questions, and the handoff to independent reviewers—read [the research-direction handoff](docs/RESEARCH_DIRECTION_HANDOFF_2026-09-09.md).

For a claim-bounded ledger of the results already established by the executed empirical modules, read [the empirical findings ledger](docs/EMPIRICAL_FINDINGS_2026-09-10.md).

For the certified count corrections, evidence-tier reconciliation, BPS cross-wave source checks, and advisor-facing sample decisions, read [the empirical certification reconciliation](docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md) and [the Kong empirical decision sheet](docs/KONG_EMPIRICAL_DECISION_SHEET_2026-09-10.md).

For the integrated explanation of how the issuer, BPS, ASEAN, and global evidence fit together—and exactly what survives or changes in the September manuscript—read [the research synthesis and manuscript bridge](docs/RESEARCH_SYNTHESIS_AND_MANUSCRIPT_BRIDGE_2026-09-10.md).

Potential interpretations, falsification tests, additional data requirements, and manuscript decision gates are kept separately in [the hypotheses and empirical agenda](docs/HYPOTHESES_AND_EMPIRICAL_AGENDA_2026-09-10.md).

## Current status

This repository is a **working research archive**, not a claim that the empirical design has been approved or that every dataset is mutually comparable.

- Indonesia remains the proposed main geography.
- FY2023 is the cleanest cross-platform comparison, but a one-year main sample has been judged insufficient for the master's thesis.
- The active expansion therefore concentrates on a longitudinal Indonesia design using additional years and issuers where source definitions permit.
- ASEAN material is kept separately as context or robustness evidence. It must not be pooled as though ASEAN were one tax or regulatory system.
- The current ASEAN corroboration extension treats six countries separately and preserves publication-vintage revisions; see [the technical readout](reports/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md).
- The first executed hypothesis tests compare 12 within-series Indonesia candidate transitions and evaluate the BPS growth and province-recordkeeping evidence; see [the technical readout](reports/HYPOTHESIS_TESTS_2026-09-10.md) and [validation report](reports/HYPOTHESIS_TESTS_VALIDATION_2026-09-10.md).
- The certification layer separately records the corrected 13-period direct candidate inventory, the 9-transition direct-scope sensitivity, and the distinction between directly reported and derived BPS cross-wave quantities.
- The transaction–revenue difference is not automatically missing GDP, participant income, unpaid tax, or tax evasion.
- Investor-event results remain exploratory while event contamination and information timing are unresolved.

Read [AGENTS.md](AGENTS.md), [docs/CURRENT_STATUS.md](docs/CURRENT_STATUS.md), [docs/PROJECT_HISTORY.md](docs/PROJECT_HISTORY.md), [docs/METHODOLOGY.md](docs/METHODOLOGY.md), [data/README.md](data/README.md), and [docs/KNOWN_LIMITATIONS.md](docs/KNOWN_LIMITATIONS.md) before interpreting repository outputs.

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
│   ├── bps_official/           # Indonesia official-statistics extracts, 2020–2024
│   ├── asean_context/          # country-level context kept separate
│   ├── asean_corroboration/    # six-country, revision-aware supporting evidence
│   └── legacy_not_active/      # preserved but prohibited as active evidence
├── scripts/
│   ├── acquisition/
│   ├── extraction/
│   └── analysis/
├── notebooks/                  # executable empirical audit notebooks
├── reports/                    # durable audit/readout artifacts
├── outputs/                    # generated censuses, diagnostics, and charts
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

## Current empirical audit

The comprehensive backend census is generated by [`scripts/analysis/build_comprehensive_empirical_audit.py`](scripts/analysis/build_comprehensive_empirical_audit.py). Read [`reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md`](reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md) or open the executed notebook in `notebooks/` before interpreting row counts.
