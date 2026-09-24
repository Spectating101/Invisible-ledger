# Current thesis artifacts

Updated 25 September 2026. This map identifies the files currently in use. Check both this map and file timestamps when new work arrives; update the map when a newer version is adopted.

## Proposal

- Editable source: `papers/current/Invisible_Ledger_Proposal_KONG_MASTER_FINAL_2026-09-24.docx`
- Render of that source: `papers/current/Invisible_Ledger_Proposal_KONG_MASTER_FINAL_2026-09-24.pdf`
- Generated search text: `papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md`

The September 24 DOCX is the active proposal. The PDF was rendered from that exact DOCX on 25 September; the text mirror records its SHA-256. Edit the DOCX directly, then regenerate the PDF and mirror. Never rebuild it from historical Markdown or proposal surgery scripts.

The file `papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.*` was the former proposal path. It is historical and recoverable from Git commit `b8f35576f30f6ab9518409c8f7510d1ad019ddf6`. The September 17 and September 23 DOCXs in Downloads or other folders are earlier drafts. Identical copies outside the repository are not separate authorities.

## Oral presentation

- Editable deck: `papers/current/IL_Oral_Deck_v1.pptx`
- Matching preview: `papers/current/IL_Oral_Deck_v1_preview.pdf`

The deck was last saved on 25 September and follows the September 24 proposal. Update its preview after deck changes. The deck is a presentation of the proposal, not a source for research data or result values.

## Manuscript

The manuscript is a separate, earlier work stream:

- generator: `scripts/build_thesis_manuscript.py`
- searchable manuscript: `papers/current/Invisible_Ledger_Thesis_Manuscript.md`
- rendered manuscript: `papers/current/Invisible_Ledger_Thesis_Manuscript.docx` and `.pdf`

Do not infer proposal wording from the manuscript or from historical candidate, comparison, or surgery files.

## Authority and update rule

1. For the current proposal, use the September 24 DOCX. The PDF and searchable text are derived from it.
2. For empirical results, use `docs/RESULT_AUTHORITY_MAP_2026-09-12.md` and the underlying source chain. A proposal or slide is not the authority for a data value.
3. A filename containing `FINAL` does not establish current status. Compare timestamps, content, and provenance; record a successor here when one is adopted.
4. For historical comparisons, identify each artifact by date, path, and commit SHA where available. Do not label an old snapshot simply `current`.
5. Preserve research boundaries in `AGENTS.md`, `docs/METHODOLOGY.md`, and `docs/KNOWN_LIMITATIONS.md`.
