# Result authority map - 12 September 2026

## Purpose

The repository accumulated several valid but overlapping result, synthesis, hypothesis, and review documents during the September rebuild. This note defines which document answers which question so proposal/manuscript drafting does not silently mix dated execution snapshots, certification layers, and narrative interpretations.

## Authority order

### 1. Current project decisions

**File:** `docs/CURRENT_STATUS.md`

Use for:
- proposed main geography;
- what has or has not been advisor-approved;
- unresolved sample/revenue-basis decisions;
- live nonclaim boundaries.

Do not use it as the detailed results ledger.

### 2. Canonical current empirical results

**File:** `docs/CANONICAL_EMPIRICAL_RESULTS_2026-09-12.md`

Use for:
- proposal statistics;
- preview/manuscript headline results;
- result hierarchy;
- current interpretation boundaries;
- which findings are core versus supporting.

This is the default human-readable source for current result wording.

### 3. Certification and evidence admission

**File:** `docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md`

Use for:
- 13 vs historical 14 direct candidate counts;
- hard exclusions;
- 9-transition direct-candidate sensitivity;
- evidence-tier definitions;
- source/vintage reconciliation.

If the canonical results ledger and an older report appear to disagree on counts, check certification before drafting.

### 4. Source/admission methodology

**Files:**
- `docs/METHODOLOGY.md`
- `docs/KNOWN_LIMITATIONS.md`
- `data/README.md`

Use for:
- direct/derived/external/scenario classes;
- period/geography/business-scope rules;
- nonindependence of annual/quarter/vintage observations;
- GDP/tax interpretation boundaries.

### 5. Module-specific evidence

Use the module documents for depth and reproduction, not as whole-paper narrative authorities:

- BPS cross-wave: `docs/BPS_CROSSWAVE_CERTIFICATION_2026-09-10.md`
- participant/institutional: `docs/HYPOTHESIS_EXTENSION_PARTICIPANT_AND_INSTITUTIONAL_LINKAGE_2026-09-10.md`
- payments: `docs/BANK_INDONESIA_PAYMENT_LEDGER_EXTENSION_2026-09-11.md`
- ASEAN: `reports/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md`
- global issuers: `reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md`
- mechanism outputs: `data/measurement/results/`

### 6. Dated execution snapshots

**Examples:**
- `reports/HYPOTHESIS_TESTS_2026-09-10.md`
- `reports/HYPOTHESIS_TESTS_VALIDATION_2026-09-10.md`
- `reports/EMPIRICAL_BACKEND_AUDIT_2026-09-09.md`

These record what a script/run established at a point in time. Preserve them as reproducibility/audit artifacts. Do not rewrite them to match later narrative decisions.

### 7. Narrative and review documents

**Examples:**
- `docs/RESEARCH_SYNTHESIS_AND_MANUSCRIPT_BRIDGE_2026-09-10.md`
- `docs/LITERATURE_EMPIRICAL_INTEGRATION_2026-09-11.md`
- `docs/WHY_INVISIBLE_LEDGER_MATTERS_STAKES_AND_DEVELOPMENT_2026-09-11.md`
- `docs/PROPOSAL_PREEMPTIVE_REVIEW_MAP_2026-09-11.md`
- `docs/PROPOSAL_REVIEW_COMMENT_RESPONSE_MATRIX_2026-09-11.md`

These are interpretation, synthesis, or review aids. They may contain valid arguments and literature but should pull empirical headline values from the canonical results ledger rather than become independent result authorities.

### 8. Manuscripts and proposals

Files under `papers/` are outward artifacts. They are downstream of the authorities above.

Rules:
- a proposal/manuscript should never become the source of truth for a result;
- if an outward document contains a number not in the canonical ledger/module evidence, trace it before reuse;
- final sample wording remains provisional until advisor approval is reflected in `docs/CURRENT_STATUS.md`.

## Drafting pipeline

Use the repository in this order:

```text
source document
  -> source extract
  -> analytic row
  -> executed/module result
  -> certification/admission check
  -> CANONICAL_EMPIRICAL_RESULTS
  -> paper preview / thesis narrative
  -> proposal / manuscript / slides
```

Do not draft directly from raw module counts when a canonical current result already exists.

## Known legacy/staleness traps

1. **14 vs 13 direct annual candidates**
   - historical audit count: 14;
   - corrected current direct candidates: 13;
   - Tokopedia FY2021 is a hard exclusion for period mismatch.

2. **12 transitions vs 9 transitions**
   - 12 = all-tier inventory, including conditional country reconstructions;
   - 9 = direct-candidate scope sensitivity;
   - neither is advisor-approved as the final thesis sample.

3. **Province recordkeeping result vs business-level result**
   - province relationship is unstable/ecological;
   - BPS later published a business-level association;
   - do not describe the province result as the final substantive H3 result.

4. **Institutional linkage failure**
   - older hypothesis wording framed linkage as unresolved/failure;
   - current evidence establishes legal architecture but not operational linkage/effects;
   - use `legal bridge established; operational closure untested`.

5. **FY2023 transaction-revenue residual**
   - source-auditable historical construction;
   - not the current thesis core;
   - never call it missing GDP, undeclared income, or unpaid tax.

6. **Payment data**
   - independent payment-system evidence;
   - never treat payment value as e-commerce sales or add payment rows to thesis issuer/BPS N.

## Proposed outward-document hierarchy

### Research preview
Purpose: show the full intellectual/empirical direction before the final sample is frozen.

Should include:
- big economic puzzle;
- Invisible Ledger interpretation;
- literature roots;
- core issuer/BPS results;
- payment/institutional extension;
- corroboration and limitations;
- advisor gates.

### Thesis proposal
Purpose: obtain committee/advisor approval for the question, design, feasibility, and remaining decisions.

Should include only:
- problem and stakes;
- three nested research questions;
- core literature;
- compact conceptual framework;
- design and sample hierarchy;
- 3-4 preliminary evidence blocks;
- contribution, limitations, and work plan.

### Final thesis manuscript
Purpose: execute the approved design and synthesize the findings after the sample boundary is frozen.

The final manuscript should not be reconstructed solely because this authority map exists; it remains downstream of advisor review.
