# September 16 proposal comparison audit

This directory preserves a **non-canonical review artifact**. It does not replace or modify the canonical proposal identified in [`CANONICAL_ARTIFACTS.md`](../../../CANONICAL_ARTIFACTS.md).

## Main report

- `Invisible_Ledger_Full_Line_by_Line_Comparison_2026-09-16.docx`
- SHA256: `dd5976449d473e7cae817af0a4c2760c9b57bf44c830c5133382d50a1fdebf0c`
- Scope: exhaustive text-unit comparisons in three directions:
  1. September 16 local original to Claude R1;
  2. Claude R1 to the readable consolidation candidate;
  3. September 16 local original to the readable consolidation candidate.
- Extraction unit: text-bearing heading, paragraph, equation-like paragraph, caption, table row, header, footer, footnote, or endnote. Blank layout-only paragraphs and non-text image pixels are excluded.
- Status: audit/reference only. It is not an approved proposal rewrite and must not be treated as current proposal text.

## Frozen source snapshots

| File | Role | SHA256 |
|---|---|---|
| `source_snapshots/01_September_16_local_original.docx` | Local September 16 source supplied for the comparison; not labelled as repository-canonical | `b33ec0076ae9122a48874780e4ecb3dbd18bfbe809d62772e1ae285fa965e7a8` |
| `source_snapshots/02_Claude_R1.docx` | Exact R1 document recovered from Claude's session scratchpad | `bddd67543f8a8068b912a5ce70bd07f4578dc78b39266ef252ee0c1b569e5e0a` |
| `source_snapshots/03_Readable_consolidation_candidate.docx` | Separate readable consolidation candidate; not canonical | `e341fcad352836ad571792bb555803c628caadf5b18a53bdf14baa3c834dc415` |

Claude provenance for the R1 snapshot:

- transcript session ID: `494fb109-6c6b-442f-9643-1b568b599504`
- slug: `witty-zooming-pearl`
- internal API session: `a4a4a90c-ff2e-47be-8b36-68ca39926dec`

## Interpretation boundary

The comparison is intentionally mechanical and exhaustive. It establishes exactly what wording differs among the three snapshots; it does not decide which unfinished Claude edits should become canonical. Any later proposal revision must still begin from the canonical artifact and follow the repository's proposal rules.
