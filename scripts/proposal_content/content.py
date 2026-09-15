# -*- coding: utf-8 -*-
"""Legacy candidate-builder support without a second proposal text source.

The canonical proposal is edited directly at:
  papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx

Historically this module duplicated the complete proposal body and abstract. That made
obsolete prose searchable and caused agents/builders to treat an old iteration as current.
The body copy is deliberately removed. Candidate builds may reuse the reference list from
the canonical DOCX, but no current proposal prose lives here.
"""

from pathlib import Path
from docx import Document

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx"

# Explicitly empty: current proposal prose must come from the canonical DOCX, never here.
ABSTRACT = None
BODY = []

if not CANONICAL.exists():
    raise RuntimeError(f"canonical proposal missing: {CANONICAL}")

_doc = Document(CANONICAL)
_paras = [p.text.strip() for p in _doc.paragraphs]
try:
    _ref_idx = _paras.index("References")
except ValueError as exc:
    raise RuntimeError("canonical proposal has no References heading") from exc

# References are the final prose section in the canonical proposal. Pull them directly
# from the DOCX so the legacy candidate builder cannot carry a stale bibliography either.
REFS = [t for t in _paras[_ref_idx + 1 :] if t]

PRIM_HEAD = "Canonical proposal source"
PRIM_NOTE = (
    "This candidate was built from historical Markdown. Current proposal content and "
    "reference authority remain the FINAL DOCX; see CANONICAL_ARTIFACTS.md."
)
PRIM = []

# Historical full module is preserved at snapshot commit
# 72d49ef50af8f9b60d4d8bbefe99b29c85b548b9.
