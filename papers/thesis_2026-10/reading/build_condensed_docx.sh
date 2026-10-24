#!/usr/bin/env bash
# Condensed thesis as a Word file: the same text as the condensed PDF (abstract and Chapters 1 to 7, no notes to the reader, key sentences in bold),
# with real Word equations and three-line tables. A4, Times New Roman 11 pt, 1.15 spacing, page numbers. Run: bash papers/thesis_2026-10/reading/build_condensed_docx.sh
set -euo pipefail
cd "$(dirname "$0")"
D=$(date +%Y-%m-%d)
FILES="abstract.md ch1_introduction.md ch2_literature.md ch3_framework.md ch4_data_methods.md ch5_results.md drafts/ch6_draft_2026-10-14.md drafts/ch7_draft_2026-10-14.md"
{
  printf -- '---\ntitle: "The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia'"'"'s Platform Economy"\nsubtitle: "Master'"'"'s thesis, condensed version"\nauthor:\n  - "Christopher Ongko (王新福)"\n  - "Advisor: Prof. De-Rong Kong (孔德蓉)"\n  - "College of Management, Yuan Ze University"\ndate: "October 2026"\nlang: en\n---\n\n'
  for f in $FILES; do cat "../$f"; printf '\n\n'; done | python3 condense.py | python3 boldkey.py | python3 docx_prep.py
} > condensed_docx.tmp.md
pandoc condensed_docx.tmp.md --from markdown --reference-doc=docx_reference.docx --resource-path=.. -o condensed_docx.tmp.docx
python3 docx_post.py condensed_docx.tmp.docx thesis_condensed_$D.docx
rm -f condensed_docx.tmp.md condensed_docx.tmp.docx
echo "built thesis_condensed_$D.docx"
