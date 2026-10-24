#!/usr/bin/env bash
# The full thesis as a Word file in YZU's layout (YZU thesis format guidelines): A4, margins 3.5 / 4 / 2 / 2 cm, 1.5 line spacing, Times New Roman 12 pt,
# front matter in Roman numerals and main text in Arabic from Chapter 1, tables and figures numbered 1, 2, 3 through the thesis, contents and lists of tables and
# figures as Word fields. Two passes: the first finds the page of every heading and caption (LibreOffice), the second writes them in.
# Not in the file, because they are the researcher's or the department's: cover, approval sheet, Chinese abstract and keywords, acknowledgements.
# Run: bash papers/thesis_2026-10/reading/build_yzu_docx.sh -> thesis_YZU_layout_<date>.docx
set -euo pipefail
cd "$(dirname "$0")"
D=$(date +%Y-%m-%d)
mkdir -p yzu_tmp
slot() { printf '\n::: {custom-style="Front Heading"}\n%s\n:::\n\n::: {custom-style="Field Slot"}\n%s\n:::\n' "$1" "$2"; }
{
  printf -- '---\ntitle: "The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia'"'"'s Platform Economy"\nsubtitle: "Master'"'"'s thesis"\nauthor:\n  - "Christopher Ongko (王新福)"\n  - "Advisor: Prof. De-Rong Kong (孔德蓉)"\n  - "College of Management, Yuan Ze University"\ndate: "October 2026"\nlang: en\n---\n\n'
  cat ../abstract.md; printf '\n\n'
  slot "Contents" "§TOC§"; slot "List of Tables" "§LOT§"; slot "List of Figures" "§LOF§"; printf '\n'
  cat ../symbols.md; printf '\n\n::: {custom-style="Field Slot"}\n§SECT§\n:::\n\n'
  for f in ch1_introduction.md ch2_literature.md ch3_framework.md ch4_data_methods.md ch5_results.md drafts/ch6_draft_2026-10-14.md drafts/ch7_draft_2026-10-14.md appendix_notes.md references.md; do cat "../$f"; printf '\n\n'; done
} | python3 condense.py | python3 yzu_prep.py | python3 docx_prep.py > yzu_tmp/yzu.md
pandoc yzu_tmp/yzu.md --from markdown --reference-doc=yzu_reference.docx --resource-path=.. -o yzu_tmp/raw.docx
# pass 1: placeholders, convert, read the pages
python3 yzu_post.py yzu_tmp/raw.docx yzu_tmp/p1.docx > /dev/null
python3 - <<'PY'
import docx, json
d = docx.Document("yzu_tmp/p1.docx"); want = []; main = False
for p in d.paragraphs:
    if p.style.name in ("Heading 1", "Heading 2"): want.append(p.text.strip())
    if p.style.name in ("Table Caption", "Figure Caption"): want.append(p.text.strip())
json.dump(want, open("yzu_tmp/pages.json.want", "w"), ensure_ascii=False)
PY
( cd yzu_tmp && timeout 300 soffice --headless --convert-to pdf p1.docx >/dev/null 2>&1 )
python3 yzu_pages.py yzu_tmp/p1.pdf yzu_tmp/pages.json
# pass 2
python3 yzu_post.py yzu_tmp/raw.docx thesis_YZU_layout_$D.docx yzu_tmp/pages.json
echo "built thesis_YZU_layout_$D.docx"
