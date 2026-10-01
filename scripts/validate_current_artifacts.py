#!/usr/bin/env python3
"""Check that the active proposal (27 Sep 2026 PDF) and the presented oral deck (v4.10) have their declared companions."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "papers/current"
PDF = CURRENT / "Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf"
MIRROR = CURRENT / "Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md"
DECK = CURRENT / "IL_Proposal_Oral_Deck_v4.10_Christopher_Ongko.pptx"
DECK_PDF = CURRENT / "IL_Proposal_Oral_Deck_v4.10_Christopher_Ongko_preview.pdf"


def pages(path: Path) -> int:
    result = subprocess.run(["pdfinfo", str(path)], check=True, text=True, capture_output=True)
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, re.MULTILINE)
    if not match:
        raise AssertionError(f"PDF page count missing: {path}")
    return int(match.group(1))


def main() -> None:
    for path in (PDF, MIRROR, DECK, DECK_PDF):
        assert path.is_file() and path.stat().st_size > 0, f"missing active artifact: {path}"

    source_hash = hashlib.sha256(PDF.read_bytes()).hexdigest()
    mirror = MIRROR.read_text(encoding="utf-8")
    assert f"Generated from `papers/current/{PDF.name}`." in mirror
    assert f"Source PDF SHA-256: `{source_hash}`." in mirror, "searchable text is stale"
    assert "How much economic activity remains invisible when digital platforms are measured" in " ".join(mirror.split())

    with ZipFile(DECK) as archive:
        assert archive.testzip() is None
        slide_count = sum(bool(re.fullmatch(r"ppt/slides/slide\d+\.xml", name)) for name in archive.namelist())

    assert pages(PDF) > 0
    pdf_text = " ".join(subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).split())
    assert "How much economic activity remains invisible when digital platforms are measured" in pdf_text, "proposal PDF does not match the active research question"
    assert pages(DECK_PDF) == slide_count, "deck preview has a different slide count"
    for old in ("Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14", "Invisible_Ledger_Proposal_KONG_MASTER_FINAL_2026-09-24"):
        for suffix in (".docx", ".pdf"):
            assert not (CURRENT / f"{old}{suffix}").exists(), f"superseded proposal still in papers/current: {old}{suffix}"

    # Rule files must name the active proposal, and may mention the archived 24 September files only as superseded.
    for rel in ("AGENTS.md", "CANONICAL_ARTIFACTS.md", "README.md", "docs/CURRENT_STATUS.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert PDF.name in text, f"{rel} does not name the active proposal {PDF.name}"
        assert "v4.10" in text, f"{rel} does not name the presented deck v4.10"
        for line in text.splitlines():
            if "IL_Oral_Deck_v1" in line:
                assert any(w in line.lower() for w in ("not", "archive", "superseded")), f"{rel} names the old v1 deck without saying it is not the presented deck: {line[:90]}"
        for line in text.splitlines():
            if "KONG_MASTER_FINAL_2026-09-24" in line:
                assert any(w in line.lower() for w in ("superseded", "archive")), f"{rel} names the 24 September file without saying it is superseded: {line[:90]}"

    # Exactly one proposal file may sit in papers/current (older proposals live in archive/).
    proposals = sorted(p.name for p in CURRENT.glob("Invisible_Ledger*Proposal*") if p.suffix in (".docx", ".pdf"))
    assert proposals == [PDF.name], f"unexpected proposal files in papers/current: {proposals}"

    print(f"Active proposal: {PDF.name}, SHA-256 {source_hash}, {pages(PDF)} PDF pages")
    print(f"Presented deck: {DECK.name}, {slide_count} slides, {pages(DECK_PDF)} preview pages")


if __name__ == "__main__":
    main()
