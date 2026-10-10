# Balanced 10-page proposal candidate — review packet

## Purpose

This branch exists only to compare a **balanced 10-page presentation** against the current canonical 9-page proposal on `main`.

Do **not** treat the 10-page count as a target in itself. The question is whether the readability gain is worth the extra page.

## Candidate artifacts

The workflow on this branch builds:

- `papers/candidates/Invisible_Ledger_Thesis_Proposal_BALANCED_10PP_CANDIDATE_2026-09-15.docx`
- `papers/candidates/Invisible_Ledger_Thesis_Proposal_BALANCED_10PP_CANDIDATE_2026-09-15.pdf`

## Invariants

The candidate must remain content-identical to the current 9-page release:

- 121 paragraph texts: identical
- 6 tables and every cell: identical
- 31 references: retained
- no comments
- no tracked changes
- 10 A4 pages
- body remains 12 pt Times New Roman
- tables remain 9 pt
- captions remain 9.5 pt

No argument, result, citation, table value, figure, or claim boundary is changed.

## What changes

Only presentation rhythm:

1. Pages 1–5 retain the current compact rhythm, so Table 1 still fits cleanly with its discussion.
2. From Section 5 onward, paragraph leading and paragraph separation are relaxed to reduce visual compression in the evidence / limitations / work-plan sequence.
3. References are restored to 12 pt and given more leading/spacing, so the bibliography occupies two pages instead of being compressed into the tail of the 9-page version.

## Review question for Claude

Compare this candidate against the canonical 9-page proposal on `main` and return one of:

- **APPROVE_BALANCED_10PP** — the extra page materially improves committee readability without creating obvious dead space or weakening visual discipline.
- **KEEP_CANONICAL_9PP** — the 9-page version is already sufficiently readable and the extra page mainly adds slack.
- **REVISION** — identify exact pages/spacing decisions to change; do not rewrite content unless a substantive error is found.

Evaluate specifically:

1. first-read comprehension for Kong / Thomas;
2. body density on pages 3–4 and 7–8;
3. table/caption legibility and post-table breathing room;
4. whether page 10 looks like legitimate bibliography space or avoidable padding;
5. consistency with Kong Comment 21 (font type, font size, line spacing, and text formatting consistency);
6. whether any page now looks under-filled enough to make the 10-page layout worse than the 9-page canonical.

## Review stance

Treat the 9-page version on `main` as canonical until this candidate is explicitly approved. This branch is a presentation experiment, not a content revision.
