#!/usr/bin/env python3
"""Print the active-proposal facts as Claude Code SessionStart context.

Run by .claude/settings.json at the start of every Claude Code session in this repository.
It reads only local files and never fails the session: on any problem it says so and continues.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def main() -> None:
    try:
        from validate_current_artifacts import PDF  # the single place that names the active proposal

        check = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_current_artifacts.py")],
            capture_output=True, text=True, timeout=60,
        )
        status = "artifact check passed" if check.returncode == 0 else f"ARTIFACT CHECK FAILED: {(check.stderr or check.stdout).strip().splitlines()[-1:]}"
        name = PDF.name
    except Exception as exc:  # never block a session
        status, name = f"artifact check could not run ({exc})", "papers/current/ (see CANONICAL_ARTIFACTS.md)"

    text = (
        "INVISIBLE LEDGER, read first. "
        f"The active thesis proposal is papers/current/{name} (the version examined and passed on 1 October 2026; {status}). "
        "It has NO editable source here. Files named FINAL are not automatically current: the 24 September files are superseded and archived. "
        "The presented oral deck is v4.10 (papers/current). The thesis executes this proposal: same title, research question and two hypotheses (H1 revenue to platform, H2 platform to national growth). "
        "Do not pivot the concept. Writing must be plain (see AGENTS.md, 'Thesis story and writing standard'). "
        "If the researcher names a version or file, believe the researcher over this repository and update CANONICAL_ARTIFACTS.md. "
        "Before any diagnosis or rewrite, read AGENTS.md and CANONICAL_ARTIFACTS.md."
    )
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}))


if __name__ == "__main__":
    main()
