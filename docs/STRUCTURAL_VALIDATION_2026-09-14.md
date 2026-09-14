# Structural validation — OOXML integrity, 14 September 2026

Rendering checks catch layout differences. This catches the different and more damaging class of
problem: a file that opens but makes Word report "unreadable content" and silently repair it, or one
where accepting a single tracked change silently accepts several.

Tool: `scripts/validate_docx.py`. Checks XML well-formedness across all parts, Content-Types
overrides resolving to real parts, relationship targets resolving, style references defined, table
grid columns matching cell counts per row, revision-id uniqueness, comment range balance and
definition/anchor correspondence, footnote reference resolution, and presence of the final `sectPr`.

## Findings

**Two real defects, both found and fixed.**

**1. 303 duplicate revision ids in the tracked Surgery file** (478 marks, 175 unique). Cause: the
surgery pipeline runs as several stage scripts, each re-importing the helper library, so the
revision-id counter restarted at 9001 in every stage. Word tolerates duplicate `w:id` values but uses
them to group revisions — accepting one change could have accepted several unrelated ones. Since this
is the document the advisor would click through change by change, that is a functional defect, not a
cosmetic one. All 478 marks renumbered uniquely; the 6 comment anchors survive.

**2. One orphaned comment definition in the accepted preview.** Comment id 109 remained in
`word/comments.xml` after its anchor was removed during change acceptance. Pruned; 5 defined, 5
anchored, 0 orphans.

## Result

| File | Parts | Revisions | Comments | Tables | Verdict |
|---|---:|---:|---:|---:|---|
| `Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx` | 23 | 0 | 0 | 9 | CLEAN |
| `Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx` | 34 | 478 | 6 | 10 | CLEAN |
| `Invisible_Ledger_Proposal_Sept01_ACCEPTED_PREVIEW_2026-09-14.docx` | 34 | 0 | 5 | 9 | CLEAN |
| `Invisible_Ledger_Thesis_Proposal_2026-09-14.docx` (earlier build) | — | 0 | 0 | — | CLEAN |

## On installing a different editor

Considered and not done. The risk surface says why:

| | Tracked changes | Comments | Text boxes | Fields | Footnotes |
|---|---:|---:|---:|---:|---:|
| Proposal (the submission) | 0 | 0 | 0 | 0 | 0 |
| Surgery file (supporting) | 478 | 6 | 0 | 18 | 1 |

The proposal is plain paragraphs and tables in one font, which is where LibreOffice and Word agree
most closely; the remaining difference is column-width rounding and line-break position. The features
where renderers actually diverge are all in the Surgery file, which is supporting evidence rather than
the submission.

OnlyOffice, WPS and FreeOffice are all absent from the system's apt repositories, with no flatpak or
snap available, so a local install would mean a third-party repository or an AppImage — to obtain a
second approximation of Word rather than Word itself. **Word Online is free, needs no install, and
uses the actual Microsoft engine**; that is the only check that settles the question, and it remains
outstanding.
