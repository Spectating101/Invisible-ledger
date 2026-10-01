#!/usr/bin/env python3
"""Export a searchable text mirror of the active proposal PDF.

The active proposal is the 27 September 2026 PDF; no editable source has been located.
This script exists so code-search and agents can read current proposal text without
consulting stale drafts. Do not edit the generated Markdown by hand and do not rebuild
the proposal from it. The text follows the PDF's line breaks; table cells may be out of order.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf"
OUTPUT = ROOT / "papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md"
FOOTER = re.compile(r"^Yuan Ze University \| .*\| \d+\s*$")


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"active proposal not found: {SOURCE}")

    source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    raw = subprocess.check_output(["pdftotext", str(SOURCE), "-"], text=True)
    lines = [ln.rstrip() for ln in raw.replace("\f", "\n").splitlines() if not FOOTER.match(ln)]
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()

    header = [
        "<!-- GENERATED FILE: DO NOT EDIT. SOURCE OF TRUTH IS THE ACTIVE PDF. -->",
        "# Invisible Ledger proposal — canonical searchable text",
        "",
        f"Generated from `{SOURCE.relative_to(ROOT)}`.",
        f"Source PDF SHA-256: `{source_sha}`.",
        "",
        "> **Authority rule:** this file mirrors the active PDF for search/review only. "
        "If this file and the PDF ever disagree, the PDF wins and this mirror must be regenerated.",
        "",
    ]
    OUTPUT.write_text("\n".join(header) + body + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"source sha256 {source_sha}")


if __name__ == "__main__":
    main()
