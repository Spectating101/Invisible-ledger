#!/usr/bin/env bash
# Compact reading copy: Chapters 1 to 7 only, small type and tight margins (about 25 to 30 pages). Same text and pipeline as the full copy.
# The key sentences listed in keypoints.txt are bold (boldkey.py), so the bold alone summarises the thesis; the full copy and the thesis text are not changed.
# Run: bash papers/thesis_2026-10/reading/build_compact.sh -> thesis_compact_<date>.pdf
set -euo pipefail
cd "$(dirname "$0")"
D=$(date +%Y-%m-%d)
FILES="abstract.md ch1_introduction.md ch2_literature.md ch3_framework.md ch4_data_methods.md ch5_results.md drafts/ch6_draft_2026-10-14.md drafts/ch7_draft_2026-10-14.md"
{
  printf -- '---\ntitle: "The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia'"'"'s Platform Economy"\nsubtitle: "Master'"'"'s thesis, condensed version"\nauthor:\n  - "Christopher Ongko (王新福)"\n  - "Advisor: Prof. De-Rong Kong (孔德蓉)"\n  - "College of Management, Yuan Ze University"\ndate: "October 2026"\nlang: en\n---\n\n'
  python3 prep.py $(for f in $FILES; do printf '../%s ' "$f"; done) | python3 condense.py | python3 boldkey.py
} > compact.tmp.md
pandoc compact.tmp.md --from markdown --to html5 --standalone --section-divs --css style.css --css style_compact.css --embed-resources \
  --resource-path=.. --metadata title-prefix="" -o compact.tmp.html
python3 post.py compact.tmp.html
PDF_MARGIN=14mm,15mm,15mm,15mm node print_pdf.js compact.tmp.html thesis_compact_$D.pdf
rm -f compact.tmp.md
echo "built thesis_compact_$D.pdf: $(pdfinfo thesis_compact_$D.pdf | grep Pages)"
