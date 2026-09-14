# Tracked-changes surgery pipeline

Builds `papers/advisor_tracked/Invisible_Ledger_Proposal_Sept01_Surgery_2026-09-14.docx` — the
1 September proposal edited *in place* with Word tracked changes, so the advisor sees what changed
against the draft she already marked up rather than a fresh document she has to read from scratch.
That is the whole point of the surgery approach: familiarity comes from retaining her wording, and
tracked changes are what make the retention visible.

## Run order

`surgery.py`, then `stage2.py`, `stage2b.py`, `stage3.py`, `stage3b.py`, `stage4.py` … `stage9.py`,
then `accept.py` to produce the accepted preview. Each stage is a separate process; `content.py`
holds the replacement prose, `cont.py` the continuity metric, `make.py` the driver.

## surg_lib.py

Custom OOXML helpers, because python-docx has no tracked-changes API.

- `rebuild(p, segs)` — rewrites a paragraph from `[('keep'|'del'|'ins', text)]` segments, preserving
  per-run formatting through an offset map and stashing/restoring comment anchors so the advisor's
  existing comments stay attached.
- `del_paragraph(p)` — marks a whole paragraph deleted, including its paragraph mark.
- `new_paragraph(body, style, segs, after)` — inserts a new paragraph.
- `accept_existing(body)` — resolves the advisor's own edits into the baseline before new marks go on
  top, so the diff shown is ours and not hers replayed.

**Revision ids are file-backed** (`.revision_counter`, gitignored). They must be unique across the
whole document, but the stages run as separate processes, so an in-memory counter restarts each stage
and emits duplicates. Word groups revisions by id, so duplicates mean accepting one change can accept
several unrelated ones — the 14 September validation found 303 such duplicates across 478 marks. Delete
`.revision_counter` before a clean rebuild.

## Always validate the output

    python scripts/validate_docx.py <file.docx>

See `docs/STRUCTURAL_VALIDATION_2026-09-14.md`.
