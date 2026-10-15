#!/usr/bin/env bash
# Rebuilds the reading copies from the chapter files. Run from anywhere: bash papers/thesis_2026-10/reading/build_reading.sh
# Needs pandoc; LibreOffice (soffice) for the PDF. Figure alt text is dropped in the copies so captions are not printed twice.
set -euo pipefail
cd "$(dirname "$0")"
CH="ch1_introduction.md ch2_literature.md ch3_framework.md ch4_data_methods.md ch5_results.md drafts/ch6_draft_2026-10-14.md drafts/ch7_draft_2026-10-14.md"
D=$(date +%Y-%m-%d)
cat_md() { printf -- '---\ntitle: "%s"\nsubtitle: "%s"\n---\n\n' "$1" "$2"; shift 2; for f in "$@"; do sed -E 's/^!\[[^]]*\]\(/![](/' "../$f"; printf '\n\n'; done; }
cat_md "Invisible Ledger: Chapters 1 to 7 (compact reading copy)" "$D. Main text only; appendices and references are in the full copy." $CH > compact.tmp.md
pandoc compact.tmp.md --resource-path=.. --reference-doc=reference_compact.docx -o thesis_compact_$D.docx
cat_md "Invisible Ledger: thesis draft, Chapters 1 to 7" "Reading copy, $D. Chapters 6 and 7 are drafts; Section 6.5 has a slot for results due from 27 October." $CH appendix_notes.md references.md > thesis_reading_copy_$D.md
pandoc thesis_reading_copy_$D.md --resource-path=.. -o thesis_reading_copy_$D.docx --toc --toc-depth=2
rm compact.tmp.md
if command -v soffice >/dev/null; then soffice --headless --convert-to pdf thesis_compact_$D.docx >/dev/null 2>&1; fi
