# AI assistant instructions

Read these files before changing this repository:

1. `CANONICAL_ARTIFACTS.md`
2. `docs/CURRENT_STATUS.md`
3. `docs/PROJECT_HISTORY.md`
4. `docs/METHODOLOGY.md`
5. `data/README.md`
6. `docs/KNOWN_LIMITATIONS.md`

## Canonical proposal rule

- The active proposal is `papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf` (the version examined on 1 October 2026). It has no editable source in this repository.
- Its generated searchable text is `papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md`; the artifact map is `CANONICAL_ARTIFACTS.md`.
- The 24 September DOCX and PDF are superseded (`papers/current/archive/`), even though their names say `FINAL`.
- The presented oral deck is the latest `IL_Proposal_Oral_Deck_v4.x` in the repository root, not `papers/current/IL_Oral_Deck_v1.pptx`. Confirm with the researcher before relying on it.
- This map has been wrong before. **Before any diagnosis, comparison or rewrite, ask which file is final if the researcher has mentioned a version, and believe the researcher over this file.** A newer draft does not silently become active, and an older map does not silently stay active.
- Never infer current proposal text from `PROPOSAL_*_CANDIDATE*`, `VERSION_*COMPARISON*`, `scripts/surgery/*`, or historical proposal generators.
- Never call a historical snapshot `current` without an explicit commit SHA and path.

## Thesis story and writing standard

The thesis executes the 27 September proposal. It is not a new concept. Do not change the title, research question or hypotheses without the researcher's approval.

**The story.** A platform's revenue can tell a different growth story from the sales it carries, and in Indonesia it often does. Two numbers describe a platform: transaction value V (everything sold through it) and revenue R (what it keeps). The proposal's Figure 1 shows three nested circles: revenue sits inside platform commerce, which sits inside all online commerce. H1 tests the inner link (do V and R grow in proportion?). H2 tests the outer link (does national e-commerce growth come mainly from more businesses?). W = V - R is the size of what revenue leaves out, and D = g(R) - g(V) shows whether the share R/V (m) changed. The channel split and recordkeeping evidence are additional analyses, not hypotheses.

**Where improvements go.** Through what the proposal already promised: Objective 2 (reconcile large movements with incentives, monetization, recognition and scope), the Section 8 next steps (reconcile BPS and platform levels, divide wedge changes into volume and monetization effects, quarterly pairs, a stock-return extension) and Section 7 (limitations).

**Writing standard (the committee's main complaint is readability).**
- Plain words that would survive translation into junior-high Chinese and Vietnamese. The languages are filters only; never produce translations.
- Aim for sentences of about 13 to 18 words. Point first, active voice, one claim per sentence, no stacked nouns. Avoid "indicator", "Overall,", "therefore", "rather than".
- No hedging inside the story. Put caveats once, in the limitations chapter. Each number has one home chapter; the abstract and conclusion may repeat the headline.
- Define each technical term once, at first use, in plain words (transaction value, revenue, take rate, GDP, BPS, wedge, D).
- The researcher's own wording leads. Do not veto everyday phrasing. Flag a sentence only when it makes a different claim (for example, calling the wedge hidden GDP), say so once, and offer the closest supportable version.
- Every drafted sentence with a number is checked against the source before it is kept, whoever wrote it. Plain prose can still carry an invented claim.

**Advisor feedback pattern (Prof. Kong).** Define every term at first use. Use one term and one currency (GTV, USD). Explain every table in the text. State the geographic and business scope of every sample. Say whether a measure is the author's own. Explain unusual sources. Cite finance work. Give findings at economic scale. Her comments were written on whole thesis drafts: apply the concern behind a comment, not its literal wording, and treat "make it easier to read" as the main request.

**Open items.** The reference list has not been checked against the 27 September text (eight references were once supplied from general knowledge). The YZU thesis template has never been seen. Which oral deck was presented is unconfirmed (the latest `IL_Proposal_Oral_Deck_v4.x` in the repository root is the best candidate).

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
- Before proposal comparisons or rewrites, read the active searchable text mirror or September 24 DOCX; do not retrieve a historical candidate by keyword and treat it as current.
- Update `docs/CURRENT_STATUS.md` when a sample decision is actually approved or rejected.
