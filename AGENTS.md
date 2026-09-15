# AI assistant instructions

Read these files before changing this repository:

1. `CANONICAL_ARTIFACTS.md`
2. `docs/CURRENT_STATUS.md`
3. `docs/PROJECT_HISTORY.md`
4. `docs/METHODOLOGY.md`
5. `data/README.md`
6. `docs/KNOWN_LIMITATIONS.md`

## Canonical proposal rule

- The only editable canonical proposal is `papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx`.
- The canonical committee render is the same path with `.pdf`.
- For search/review, use `papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md`, which is generated from the FINAL DOCX.
- Never infer current proposal text from `PROPOSAL_*_CANDIDATE*`, `VERSION_*COMPARISON*`, `scripts/surgery/*`, or historical proposal generators.
- Never call a historical snapshot `current` without an explicit commit SHA and path.

## Research boundaries

- Preserve Indonesia as the proposed main geography unless the researcher and advisor explicitly approve a change.
- Do not mix Indonesia, ASEAN, company-wide, segment-level, annual, quarterly, full-year, partial-year, original, revised, and pro-forma observations as though they formed one sample.
- Label every value as direct country disclosure, direct segment disclosure, external estimate, derived value, conversion, scenario, or legacy output.
- Do not call transaction value minus platform revenue missing GDP, undeclared income, unpaid tax, or tax evasion.
- Do not describe the ecosystem ratio as a prior-literature metric. It is an author-constructed transformation equal to `1 / take_rate - 1`.
- Do not count source inputs, scenarios, reporting vintages, quarters and annual totals as independent observations.
- Never silently overwrite a reporting-vintage conflict or restatement.
- Do not promote files in `data/legacy_not_active/` into active analysis without source-level resolution.
- Treat event-study results as exploratory until timing, contamination and raw-price reproduction are closed.
- Keep downloaded documents immutable. New extracts and transformations require explicit provenance.

## Working practice

- Build the chain `source document -> source extract -> analytic row -> result`.
- Prefer primary issuer, regulator, statistical-office or exchange sources.
- Keep original currency and units; convert only through a documented period-specific FX rule.
- Missing data stay missing. No interpolation or annual-total division by four.
- Before manuscript changes, verify that the proposed table can be reproduced from repository data.
- Before proposal comparisons or rewrites, read the canonical searchable text mirror or the FINAL DOCX; do not retrieve a historical candidate by keyword and treat it as current.
- Update `docs/CURRENT_STATUS.md` when a sample decision is actually approved or rejected.
