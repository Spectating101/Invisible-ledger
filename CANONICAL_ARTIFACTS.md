# Current thesis artifacts

Updated 1 October 2026. This map identifies the files currently in use. The map can lag behind the real work: it named the wrong proposal from 27 September to 1 October 2026. When the researcher names a version ("the finalised one", "the Sept 27 one"), believe the researcher over this map, find that file, and then fix this map.

## Proposal

- Active proposal (examined 1 October 2026, passed): `papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf` (21 pages).
- Generated search text: `papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md`. It records the SHA-256 of the PDF.
- **No editable source for the 27 September proposal has been located.** Do not rebuild it from Markdown, candidate files or generators. If the researcher supplies the editable file, add it here and regenerate the search text.

The September 24 DOCX and PDF (`papers/current/archive/Invisible_Ledger_Proposal_KONG_MASTER_FINAL_2026-09-24.*`) are superseded. Their file names say `FINAL`, but they are not the proposal that was examined. The reference list in the 24 September DOCX has not been checked against the 27 September PDF. The September 14 proposal is also historical and is recoverable from Git commit `b8f35576f30f6ab9518409c8f7510d1ad019ddf6`. Other copies in Downloads are not separate authorities.

### What the 27 September proposal fixes (frozen)

These were seen by the advisor and the committee. The thesis builds on them and does not contradict them.

- Title: *The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy*.
- Research question: "How much economic activity remains invisible when digital platforms are measured through their reported revenue, and when does that choice change the conclusion about growth?"
- Two hypotheses on two links: H1 (revenue to platform commerce) and H2 (platform commerce to national e-commerce growth). Channel and recordkeeping evidence are additional analyses, not hypotheses.
- Measures: W = V - R, E = W/R = 1/m - 1, D = g(R) - g(V), with m = R/V.
- Main sample: Tokopedia, Blibli, Bukalapak (11 platform-years, 8 comparisons). Grab and Shopee are constructed and support the 2023 scale comparison only. Eight listed platforms outside Indonesia are the benchmark.

## Oral presentation

The presented deck is **not** `papers/current/IL_Oral_Deck_v1.pptx` (a 25 September file with 23 slides). The presented deck is the latest `IL_Proposal_Oral_Deck_v4.x` in the repository root (`v4.10`, 18 slides, as of 1 October 2026; these files are untracked). Confirm with the researcher before relying on it. The deck is a presentation of the proposal, not a source for research data or result values.

## Manuscript

The manuscript is a separate, earlier work stream:

- generator: `scripts/build_thesis_manuscript.py`
- searchable manuscript: `papers/current/Invisible_Ledger_Thesis_Manuscript.md`
- rendered manuscript: `papers/current/Invisible_Ledger_Thesis_Manuscript.docx` and `.pdf`

Do not infer proposal wording from the manuscript or from historical candidate, comparison, or surgery files.

## Authority and update rule

1. For the current proposal, use the 27 September PDF. The search text is derived from it.
2. For empirical results, use `docs/RESULT_AUTHORITY_MAP_2026-09-12.md` and the underlying source chain. A proposal or slide is not the authority for a data value.
3. A filename containing `FINAL` does not establish current status. Compare dates, content and provenance, and ask the researcher.
4. For historical comparisons, identify each artifact by date, path and commit SHA where available. Do not label an old snapshot simply `current`.
5. When a new version is adopted, update this map, `AGENTS.md`, `README.md`, `docs/CURRENT_STATUS.md` and `scripts/validate_current_artifacts.py` together.
6. Preserve research boundaries in `AGENTS.md`, `docs/METHODOLOGY.md`, and `docs/KNOWN_LIMITATIONS.md`.
