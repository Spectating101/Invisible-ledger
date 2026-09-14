# Visual audit — proposal DOCX, 14 September 2026

Method: every page rendered to PNG at 100 dpi and inspected as an image, not as extracted text.
Twelve pages. Artifact: `papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.pdf`.

## Defect found and fixed

**Table 6 — the FY2023 cross-section — split across pages 8 and 9, stranding its TOTAL row alone
at the top of page 9.** This is the most consequential table in the proposal and the row that carries
the headline figure. Text extraction did not surface it: the caption and the header row were on the
same page, so the caption/table check passed. Only the rendered image showed the break.

Fix: tables of seven rows or fewer now carry `keepNext` on every row but the last, so they move to the
next page as a block rather than splitting. Table 6 is now whole on page 9 with its caption, and
Table 7 follows on the same page.

Cost: page 8 drops to 35 lines against a 40–43 line norm. Page count unchanged at 12.

## Checked and clean

- **Cover** — Chinese and English title blocks render correctly, proportions correct, footer present.
- **Tables 1, 2, 3, 5, 7, 8, A1** — captions with their tables, no stranded headers, no clipped cells.
- **Table 4** (eight rows) splits pages 7–8 with its header correctly repeating. Acceptable.
- **Equations** — `W = V − R`, `E = (V − R)/R`, `D = g(V) − g(R)` render centred and italic; the minus
  signs are true minus glyphs, not hyphens.
- **Page density** — 40–43 lines on body pages; page 1 is the cover, page 8 is 35 after the table fix,
  page 12 is 34 where the references end. No widow pages.
- **Typography** — Times New Roman throughout at 9.5 / 11 / 12 / 13 pt; no colour; no markdown
  artefacts (`**`, backticks, `~~`, annotation arrows) leaked into the document.
- **Terminology** — GTV 4 uses, GMV 5 (all inside issuer-specific labels or the definition sentence),
  "Ecosystem Ratio" 10, "invisible wedge" 5, zero lowercase "ecosystem ratio". US$ used throughout,
  with Rp retained only for the two BPS figures and their USD equivalents given alongside.

## False positives from the earlier text-only checks

- "the the" — matched "The thesis".
- "US$ absent" — a grep escaping error; US$ appears ten times.
- "IDR absent" — correct and intended: the Blibli IDR figures left with the Blibli mechanism case.

## Still outstanding

The document has never been opened in Microsoft Word. Every render in this session has been
LibreOffice. Track-changes and comment behaviour is where the two diverge most, and the proposal
carries neither, which reduces but does not remove the risk.
