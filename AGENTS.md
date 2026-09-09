# AI assistant instructions

Read these files before changing this repository:

1. `docs/CURRENT_STATUS.md`
2. `docs/PROJECT_HISTORY.md`
3. `docs/METHODOLOGY.md`
4. `data/README.md`
5. `docs/KNOWN_LIMITATIONS.md`

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
- Update `docs/CURRENT_STATUS.md` when a sample decision is actually approved or rejected.

