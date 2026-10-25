#!/usr/bin/env bash
# The YZU Word file with the differences against an earlier version as real Word tracked changes.
# Run: bash papers/thesis_2026-10/reading/build_tracked_changes.sh [BASE_COMMIT] [AUTHOR_LABEL]
# Builds the BASE version (default a1f1af2: the 24 Oct thesis with Prof. Kong's Chapter 1 edits) from its own commit in a temporary git worktree, then compares
# the current thesis_YZU_layout_<today>.docx against it with LibreOffice (compare_docx.py). Build the current YZU file first (build_yzu_docx.sh).
# Writes reading/thesis_YZU_TRACKED_CHANGES_24Oct_to_25Oct.docx. Stops, and writes nothing, if the base build is missing or the comparison finds no change.
set -euo pipefail
cd "$(dirname "$0")"
BASE="${1:-a1f1af2}"; AUTHOR="${2:-Changes 24 to 25 Oct}"; D=$(date +%Y-%m-%d)
OUT=thesis_YZU_TRACKED_CHANGES_24Oct_to_25Oct.docx
[ -f "thesis_YZU_layout_$D.docx" ] || { echo "build thesis_YZU_layout_$D.docx first (build_yzu_docx.sh)"; exit 1; }
T=$(mktemp -d); W="$T/wt"
trap 'git worktree remove --force "$W" >/dev/null 2>&1 || true; git worktree prune; rm -rf "$T"' EXIT
git worktree add --detach "$W" "$BASE" >/dev/null 2>&1
( cd "$W/papers/thesis_2026-10/reading" && bash build_yzu_docx.sh >/dev/null 2>&1 ) || true
BEFORE="$W/papers/thesis_2026-10/reading/thesis_YZU_layout_$D.docx"
[ -f "$BEFORE" ] || { echo "the build of $BASE failed (no $BEFORE)"; exit 1; }
python3 compare_docx.py "thesis_YZU_layout_$D.docx" "$BEFORE" "$T/raw.docx"
python3 -I - "$T/raw.docx" "$OUT" "$AUTHOR" <<'PY'
import sys, zipfile, re
src, out, author = sys.argv[1:4]
zin = zipfile.ZipFile(src); parts = {}; ins = dele = 0
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename.startswith("word/") and it.filename.endswith(".xml"):
        s = data.decode("utf8").replace('w:author="Unknown Author"', 'w:author="%s"' % author)
        if it.filename == "word/document.xml": ins = len(re.findall(r"<w:ins ", s)); dele = len(re.findall(r"<w:del ", s))
        data = s.encode("utf8")
    parts[it.filename] = (it, data)
if ins + dele == 0: sys.exit("the comparison found no changes; nothing written")
zout = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
for it, data in parts.values(): zout.writestr(it, data)
zout.close(); print("wrote %s: %d insertions, %d deletions" % (out, ins, dele))
PY
