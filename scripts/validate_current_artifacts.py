#!/usr/bin/env python3
"""Check that the active proposal and oral deck have their declared companions."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "papers/current"
STEM = "Invisible_Ledger_Proposal_KONG_MASTER_FINAL_2026-09-24"
DOCX = CURRENT / f"{STEM}.docx"
PDF = CURRENT / f"{STEM}.pdf"
MIRROR = CURRENT / "Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md"
DECK = CURRENT / "IL_Oral_Deck_v1.pptx"
DECK_PDF = CURRENT / "IL_Oral_Deck_v1_preview.pdf"


def pages(path: Path) -> int:
    result = subprocess.run(["pdfinfo", str(path)], check=True, text=True, capture_output=True)
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, re.MULTILINE)
    if not match:
        raise AssertionError(f"PDF page count missing: {path}")
    return int(match.group(1))


def main() -> None:
    for path in (DOCX, PDF, MIRROR, DECK, DECK_PDF):
        assert path.is_file() and path.stat().st_size > 0, f"missing active artifact: {path}"

    source_hash = hashlib.sha256(DOCX.read_bytes()).hexdigest()
    mirror = MIRROR.read_text(encoding="utf-8")
    assert f"Generated from `papers/current/{DOCX.name}`." in mirror
    assert f"Source DOCX SHA-256: `{source_hash}`." in mirror, "searchable text is stale"
    assert "When can platform revenue serve as a useful proxy" in mirror

    with ZipFile(DOCX) as archive:
        assert archive.testzip() is None
        assert "word/document.xml" in archive.namelist()
    with ZipFile(DECK) as archive:
        assert archive.testzip() is None
        slide_count = sum(bool(re.fullmatch(r"ppt/slides/slide\d+\.xml", name)) for name in archive.namelist())

    assert pages(PDF) > 0
    pdf_text = " ".join(subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).split())
    assert "When can platform revenue serve as a useful proxy" in pdf_text, "proposal PDF does not match the active research question"
    assert pages(DECK_PDF) == slide_count, "deck preview has a different slide count"
    for suffix in (".docx", ".pdf"):
        assert not (CURRENT / f"Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14{suffix}").exists(), "former proposal still in papers/current"

    print(f"Active proposal: {DOCX.name}, SHA-256 {source_hash}, {pages(PDF)} PDF pages")
    print(f"Active deck: {slide_count} slides, {pages(DECK_PDF)} preview pages")


if __name__ == "__main__":
    main()
