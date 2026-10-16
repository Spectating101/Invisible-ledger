#!/usr/bin/env bash
# Rebuilds the reading copy from the chapter files: a typeset PDF (HTML + print CSS, rendered by Chromium) and a Word file
# for editing. Run from anywhere: bash papers/thesis_2026-10/reading/build_reading.sh
# Needs pandoc, python3, node with Playwright (preinstalled Chromium).
set -euo pipefail
cd "$(dirname "$0")"
D=$(date +%Y-%m-%d)
FILES="abstract.md symbols.md ch1_introduction.md ch2_literature.md ch3_framework.md ch4_data_methods.md ch5_results.md drafts/ch6_draft_2026-10-14.md drafts/ch7_draft_2026-10-14.md appendix_notes.md references.md"
{
  printf -- '---\ntitle: "The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia'"'"'s Platform Economy"\nsubtitle: "Master'"'"'s thesis, reading copy. Chapters 6 and 7 are drafts, and Section 6.5 waits for results due from 27 October 2026."\nauthor:\n  - "Christopher Ongko (王新福)"\n  - "Advisor: Prof. De-Rong Kong (孔德蓉)"\n  - "College of Management, Yuan Ze University"\ndate: "Draft of %s"\nlang: en\n---\n\n' "$D"
  python3 prep.py $(for f in $FILES; do printf '../%s ' "$f"; done)
} > reading.tmp.md
pandoc reading.tmp.md --from markdown --to html5 --standalone --toc --toc-depth=2 --section-divs --css style.css --embed-resources \
  --resource-path=.. --metadata title-prefix="" -o reading.tmp.html
python3 post.py reading.tmp.html
node print_pdf.js reading.tmp.html first_pass.tmp.pdf
python3 toc_pages.py first_pass.tmp.pdf reading.tmp.html
rm -f first_pass.tmp.pdf
node print_pdf.js reading.tmp.html thesis_reading_copy_$D.pdf
{ printf -- '---\ntitle: "The Invisible Ledger (editing copy)"\nsubtitle: "Draft of %s"\n---\n\n' "$D"; for f in $FILES; do sed -E 's/^!\[[^]]*\]\(/![](/' "../$f"; printf '\n\n'; done; } > edit.tmp.md
pandoc edit.tmp.md --resource-path=.. -o thesis_editing_copy_$D.docx --toc --toc-depth=2
rm -f reading.tmp.md edit.tmp.md
echo "built thesis_reading_copy_$D.pdf, thesis_editing_copy_$D.docx (HTML kept as reading.tmp.html for checking)"
