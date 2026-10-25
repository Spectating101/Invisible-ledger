#!/usr/bin/env bash
# Full redline of the thesis against an earlier version: bash papers/thesis_2026-10/reading/build_redline.sh [BASE_COMMIT_OR_TAG]
# Writes papers/thesis_2026-10/REDLINE_FULL.md, REDLINE_FULL_INDEX.csv and reading/REDLINE_FULL_<date>.pdf
set -euo pipefail
cd "$(dirname "$0")/../../.."
BASE="${1:-a1f1af2}"; D=$(date +%Y-%m-%d)
python3 papers/thesis_2026-10/reading/build_redline.py "$BASE"
pandoc papers/thesis_2026-10/REDLINE_FULL.md --from markdown-tex_math_dollars+fenced_divs+raw_html+strikeout --to html5 --standalone \
  --css papers/thesis_2026-10/reading/style.css --css papers/thesis_2026-10/reading/style_redline.css --embed-resources \
  --resource-path=papers/thesis_2026-10 --metadata pagetitle="Full redline" -o papers/thesis_2026-10/reading/redline.tmp.html
( cd papers/thesis_2026-10/reading && node print_pdf.js redline.tmp.html REDLINE_FULL_$D.pdf && rm -f redline.tmp.html )
echo "built REDLINE_FULL_$D.pdf: $(pdfinfo papers/thesis_2026-10/reading/REDLINE_FULL_$D.pdf | grep Pages)"
