# Canonical thesis artifacts

This file is the source-of-truth map for the Invisible Ledger repository. If any older candidate, comparison file, build script, or local duplicate disagrees with this map, this map wins.

## Proposal

**Authoritative content source**

`papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx`

The FINAL DOCX is the only editable canonical proposal. Since 2026-09-15 the proposal has been edited directly in DOCX form. Do not reconstruct current proposal content from historical Markdown candidates, surgery scripts, comparison files, or `scripts/proposal_content/`.

**Authoritative render**

`papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.pdf`

The PDF is the committee/render artifact. It must be regenerated from the canonical DOCX after content or layout changes.

**Authoritative searchable text mirror**

`papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md`

This file is generated automatically from the canonical DOCX by `scripts/export_canonical_proposal_text.py`. It exists so GitHub/code-search agents can retrieve the current proposal without falling back to stale Markdown. Never hand-edit it and never build the proposal from it.

## Manuscript

The current manuscript pipeline remains generated/reproducible rather than DOCX-first:

- generator: `scripts/build_thesis_manuscript.py`
- searchable manuscript: `papers/current/Invisible_Ledger_Thesis_Manuscript.md`
- rendered manuscript: `papers/current/Invisible_Ledger_Thesis_Manuscript.docx` and `.pdf`

Do not use the older `Invisible_Ledger_Integrated_Manuscript_2026-09-11.*` as the current manuscript.

## Historical proposal material

Files named `PROPOSAL_*_CANDIDATE*`, `VERSION_*COMPARISON*`, `scripts/surgery/*`, and the old `scripts/proposal_content/content.py` are historical development artifacts. They are not current proposal sources. Historical full text remains recoverable from Git history; the live tree should contain only stubs/pointers where practical so obsolete prose cannot win code-search retrieval.

## Build rules

1. Never overwrite the FINAL proposal from Markdown or a historical generator.
2. Any proposal content edit must modify the canonical FINAL DOCX.
3. Any proposal format-only pass must preserve paragraph/table text and figure aspect ratio, then regenerate the PDF.
4. After any canonical proposal DOCX change, regenerate `Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md` from that DOCX.
5. For comparisons, always identify both artifacts by commit SHA and path. Never label a historical snapshot simply `current`.
6. If a local file outside this repository has the same filename, it is not authoritative unless its hash matches the repository canonical artifact.

## Current lineage note

The claim-first proposal rewrite entered the canonical proposal at commit `92f166114067fa71c00bbbe744ad2d0c0eb28849`. Subsequent commits repaired tooling and typography without intentionally reverting to the earlier Markdown proposal. Use Git history for provenance; use the canonical paths above for current content.
