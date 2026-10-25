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
# the figures in Times New Roman, as the body (needs the font installed; see the log, 24 Oct)
if fc-list | grep -qi "Times New Roman"; then
  F=$(fc-list : file family | grep -i "^.*Times New Roman" | sed 's/:.*//' | tr '\n' ':' | sed 's/:$//')
  ( cd ../.. && FIG_FONT="Times New Roman" FIG_OUT=papers/thesis_2026-10/figures_yzu FIG_FONT_FILES="$F" python3 papers/thesis_2026-10/figures/make_figures.py && FIG_FONT="Times New Roman" FIG_OUT=papers/thesis_2026-10/figures_yzu FIG_FONT_FILES="$F" python3 papers/thesis_2026-10/figures/make_fig3_1.py )
fi
slot() { printf '\n::: {custom-style="Front Heading"}\n%s\n:::\n\n::: {custom-style="Field Slot"}\n%s\n:::\n' "$1" "$2"; }
{
  printf -- '---\nlang: en\n---\n\n'
  # cover (YZU template A1, Chinese only; not numbered), a section break, then the title page (A2)
  cat <<'COVER'
::: {custom-style="Cover University"}
元　智　大　學
:::

::: {custom-style="Cover Dept"}
管理學院財務金融暨會計碩士班
:::

::: {custom-style="Cover Track"}
財務金融碩士學程
:::

::: {custom-style="Cover Degree"}
碩　士　論　文
:::

::: {custom-style="Cover Title"}
隱形帳簿：量化印尼平台經濟中的隱形缺口
:::

::: {custom-style="Cover Person"}
研究生：王新福
:::

::: {custom-style="Cover Person Next"}
指導教授：孔德蓉
:::

::: {custom-style="Cover Date"}
中華民國 115 年 10 月
:::

::: {custom-style="Field Slot"}
§COVER§
:::

::: {custom-style="TP Title"}
隱形帳簿：量化印尼平台經濟中的隱形缺口
:::

::: {custom-style="TP Title"}
THE INVISIBLE LEDGER: QUANTIFYING THE INVISIBLE WEDGE IN INDONESIA'S PLATFORM ECONOMY
:::

::: {custom-style="TP People"}
研究生：王新福  Student: Christopher Ongko
:::

::: {custom-style="TP Line"}
指導教授：孔德蓉  Advisor: De-Rong Kong
:::

::: {custom-style="TP Gap"}
元智大學
:::

::: {custom-style="TP Line"}
管理學院財務金融暨會計碩士班
:::

::: {custom-style="TP Line"}
碩士論文
:::

::: {custom-style="TP People"}
A Thesis
:::

::: {custom-style="TP Block"}
Submitted to MS Program in Finance and Accounting
:::

::: {custom-style="TP Block"}
College of Management
:::

::: {custom-style="TP Block"}
Yuan Ze University
:::

::: {custom-style="TP Block"}
in Partial Fulfillment of the Requirements
:::

::: {custom-style="TP Block"}
for the Degree of
:::

::: {custom-style="TP Block"}
Master of Science
:::

::: {custom-style="TP Block"}
in
:::

::: {custom-style="TP Block"}
Finance and Accounting
:::

::: {custom-style="TP Block"}
October 2026
:::

::: {custom-style="TP Block"}
Chungli, Taiwan, Republic of China.
:::

::: {custom-style="TP Line"}
中華民國 115 年 10 月
:::

::: {custom-style="Field Slot"}
§TITLE§
:::

COVER
  cat ../abstract.md; printf '\n\n'
  slot "Contents" "§TOC§"; slot "List of Tables" "§LOT§"; slot "List of Figures" "§LOF§"; printf '\n'
  printf '\n\n::: {custom-style="Field Slot"}\n§SECT§\n:::\n\n'
  for f in ch1_introduction.md ch2_literature.md ch3_framework.md ch4_data_methods.md ch5_results.md drafts/ch6_draft_2026-10-14.md drafts/ch7_draft_2026-10-14.md references.md appendix_notes.md; do cat "../$f"; printf '\n\n'; done
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
