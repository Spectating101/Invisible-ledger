#!/usr/bin/env python3
"""Create a transparent file inventory for the Professor Kong data-review package.

The manifest does not alter data or calculations.  It records the files actually
included in the package and, where meaningful, their tabular row counts.
"""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path

from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = ROOT / "00_READ_FIRST" / "FILE_MANIFEST.csv"
OUT_TREE = ROOT / "00_READ_FIRST" / "PACKAGE_TREE.md"
SKIP_PATHS = {
    OUT_CSV.relative_to(ROOT).as_posix(),
    OUT_TREE.relative_to(ROOT).as_posix(),
    "00_READ_FIRST/Invisible_Ledger_Data_Summary.xlsx.inspect.ndjson",
    "build_data_summary.mjs",
    "verify_data_summary.mjs",
}


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    raise AssertionError("unreachable")


def inspect(path: Path) -> tuple[str, str, str, str]:
    """Return file type, row/record count, structural detail, and interpretation."""
    ext = path.suffix.lower()
    if ext == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))
        columns = len(rows[0]) if rows else 0
        return "CSV table", str(max(0, len(rows) - 1)), f"{columns} columns", "data rows exclude header"
    if ext in {".xlsx", ".xlsm"}:
        wb = load_workbook(path, read_only=True, data_only=False)
        counts = []
        total = 0
        for ws in wb.worksheets:
            nonempty_rows = sum(1 for row in ws.iter_rows() if any(cell.value is not None for cell in row))
            data_rows = max(0, nonempty_rows - 1)
            total += data_rows
            counts.append(f"{ws.title}:{data_rows}")
        return "Excel workbook", str(total), "; ".join(counts), "approximate data rows across sheets; headers excluded"
    if ext == ".pdf":
        try:
            output = subprocess.check_output(["pdfinfo", str(path)], text=True, stderr=subprocess.DEVNULL)
            pages = next(line.split(":", 1)[1].strip() for line in output.splitlines() if line.startswith("Pages:"))
        except Exception:
            pages = "unreadable"
        return "PDF source document", "N/A", f"{pages} pages", "source document; rows are not applicable"
    if ext in {".htm", ".html", ".xml"}:
        lines = sum(1 for _ in path.open("r", encoding="utf-8", errors="replace"))
        return "HTML/XML source document", "N/A", f"{lines} lines", "source document; rows are not applicable"
    if ext == ".json":
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(obj, list):
                return "JSON data/source", str(len(obj)), "top-level records", "JSON records"
            return "JSON data/source", "N/A", "structured object", "source/API object; rows are not applicable"
        except Exception:
            return "JSON source", "N/A", "unreadable JSON", "source/API object; rows are not applicable"
    if ext == ".py":
        lines = sum(1 for _ in path.open("r", encoding="utf-8", errors="replace"))
        return "Python script", "N/A", f"{lines} code lines", "code file; rows are not applicable"
    if ext in {".md", ".txt"}:
        lines = sum(1 for _ in path.open("r", encoding="utf-8", errors="replace"))
        return "Documentation", "N/A", f"{lines} lines", "documentation; rows are not applicable"
    return "Other", "N/A", "", "rows are not applicable"


def module_for(relative_path: str) -> str:
    return relative_path.split("/", 1)[0]


def main() -> None:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in SKIP_PATHS or "/__pycache__/" in f"/{rel}" or rel.startswith("00_READ_FIRST/qa_data_summary/"):
            continue
        file_type, rows, structure, note = inspect(path)
        files.append({
            "module": module_for(rel),
            "relative_path": rel,
            "size_bytes": path.stat().st_size,
            "size_human": human_size(path.stat().st_size),
            "file_type": file_type,
            "data_rows_or_records": rows,
            "structure_or_pages": structure,
            "count_interpretation": note,
        })

    fields = list(files[0])
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(files)

    by_module: dict[str, list[dict[str, object]]] = {}
    for row in files:
        by_module.setdefault(str(row["module"]), []).append(row)

    lines = [
        "# Package tree and file inventory",
        "",
        "This is an inventory of the submitted empirical package. `data_rows_or_records` counts CSV rows after the header and approximates workbook data rows across sheets. For original PDFs, HTML filings, scripts, and documentation, a row count is not meaningful; pages or source/code lines are supplied instead.",
        "",
        f"Underlying submitted files inventoried: {len(files)}. Together with this manifest and this package tree, the package contains {len(files) + 2} files.",
        "",
    ]
    for module, rows in sorted(by_module.items()):
        module_bytes = sum(int(row["size_bytes"]) for row in rows)
        lines += [f"## {module} — {len(rows)} files — {human_size(module_bytes)}", ""]
        for row in rows:
            count = row["data_rows_or_records"]
            detail = row["structure_or_pages"]
            suffix = f"; {detail}" if detail else ""
            lines.append(f"- `{row['relative_path']}` — {row['size_human']}; {row['file_type']}; rows/records: {count}{suffix}")
        lines.append("")
    OUT_TREE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_CSV.relative_to(ROOT)} and {OUT_TREE.relative_to(ROOT)} for {len(files)} files.")


if __name__ == "__main__":
    main()
