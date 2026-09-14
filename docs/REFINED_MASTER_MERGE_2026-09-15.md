# Merge of the refined master — 15 September 2026

Reviewed `Invisible_Ledger_Thesis_Proposal_FLASHPOINT_REFINED_MASTER_2026-09-15.docx`. It carries three
genuine editorial improvements, but it was refined from the 9-page base **before** the completeness
pass, so it does not contain the four sections added there. The two lines of work had forked. This
merges them.

## What the refined master got right, and was adopted

1. **The 13/11/9 reconciliation is rephrased more clearly.** "Three counts are intentionally
   different. The all-tier inventory contains 17 retained levels; the executed direct tiers contain 11
   levels (2 Indonesia-aligned and 9 scope-pending); and the broader direct-candidate sensitivity
   contains 13 periods … yielding 9 annual transitions." This is easier to follow than the previous
   phrasing and is accurate against Table 1. Adopted verbatim.
2. **Appendix A renamed to "data sources by evidence class" with a numbered Table A1 caption.**
   Correct: it was the only table in the document without a number, against the advisor's table rules.
   Adopted.
3. **"Primary and Institutional Sources" removed.** This was a real duplication — it repeated BPS, the
   Ministry of Finance, the issuers and Momentum Works, all already in References or Appendix A. It had
   been flagged during the 15-to-13 page work and never acted on. Adopted, with one correction below.

## What it lost, and was not adopted

It predates the completeness pass, so it lacks all four additions: the measurement literature
(§2.3), payment traces (§5.4), why the problem matters (§6), and the planned-work table. **Bank
Indonesia appears zero times anywhere in it** — dropping the sources section removed the payment layer's
only remaining trace.

It is also **US Letter**, 612 × 792pt. Flashpoint and every other version here are A4, which is what a
Taiwanese university expects.

## Corrections made while merging

Removing the sources block orphaned the Bank Indonesia citation, which §5.4 now relies on. Added
`Bank Indonesia. (2025). Payment System Statistics (SPIP) and QRIS reports.` to References.

**Figure 1 was regenerated** rather than scaled. At the original 1.96:1 aspect it could not fit on its
page and forced roughly 190 words of dead space; shrinking it to fit would have cost legibility. It was
rebuilt from `indonesia_longitudinal_candidate_levels.csv` at 2.81:1 — full text width, shorter, with
the legend on a single row — so it is both more readable and fits in place. Same 17 points, same
E = V/R − 1 construction.

## Result

| | 10pp (mine) | Refined master | **Merged** |
|---|---:|---:|---:|
| Pages | 10 | 9 | **9** |
| Paper | A4 | Letter | **A4** |
| Words | 3,877 | 3,460 | 3,737 |
| Words per page | 375 | 384 | **415** |
| Completeness sections | 4 | 0 | **4** |
| Bank Indonesia | cited | absent | **cited + referenced** |

415 words per page against Flashpoint's 420 — the density target is effectively met, and the page came
off dead space rather than content. Validates clean; abstract 148 words; all empirical figures intact.
