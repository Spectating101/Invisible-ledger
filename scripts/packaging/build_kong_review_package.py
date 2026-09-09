#!/usr/bin/env python3
"""Build the compact advisor data-review package from the research repository."""

from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DEST = Path.home() / "Downloads" / "Invisible_Ledger_Kong_Review_2026-09-10"


FILE_MAP = {
    "00_READ_FIRST/README_FIRST.md": "packaging/kong_review_2026-09-10/README_FIRST.md",
    "00_READ_FIRST/HOW_TO_REPRODUCE.md": "packaging/kong_review_2026-09-10/HOW_TO_REPRODUCE.md",
    "00_READ_FIRST/PACKAGE_FLOW.svg": "packaging/kong_review_2026-09-10/PACKAGE_FLOW.svg",
    "00_READ_FIRST/PACKAGE_FLOW.png": "packaging/kong_review_2026-09-10/PACKAGE_FLOW.png",
    "00_READ_FIRST/KONG_EMPIRICAL_DECISION_SHEET_2026-09-10.md": "docs/KONG_EMPIRICAL_DECISION_SHEET_2026-09-10.md",
    "00_READ_FIRST/RESEARCH_SYNTHESIS_AND_MANUSCRIPT_BRIDGE_2026-09-10.md": "docs/RESEARCH_SYNTHESIS_AND_MANUSCRIPT_BRIDGE_2026-09-10.md",
    "00_READ_FIRST/HYPOTHESIS_EXTENSION_PARTICIPANT_AND_INSTITUTIONAL_LINKAGE_2026-09-10.md": "docs/HYPOTHESIS_EXTENSION_PARTICIPANT_AND_INSTITUTIONAL_LINKAGE_2026-09-10.md",
    "00_READ_FIRST/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md": "docs/EMPIRICAL_CERTIFICATION_RECONCILIATION_2026-09-10.md",
    "Invisible_Ledger_Data_Guide_2026-09-10.xlsx": "outputs/kong_review_package_2026-09-10/Invisible_Ledger_Data_Guide_2026-09-10.xlsx",
}


TREE_MAP = {
    "01_INDONESIA_ISSUER/data/indonesia_fy2023": "data/indonesia_fy2023",
    "01_INDONESIA_ISSUER/data/longitudinal": "data/longitudinal",
    "01_INDONESIA_ISSUER/data/measurement": "data/measurement",
    "01_INDONESIA_ISSUER/outputs/hypothesis_tests": "outputs/hypothesis_tests_2026-09-10",
    "02_BPS_OFFICIAL/data": "data/bps_official",
    "02_BPS_OFFICIAL/institutional": "data/institutional",
    "03_ASEAN_CORROBORATION/data": "data/asean_corroboration",
    "04_GLOBAL_CORROBORATION/data": "data/global_ecommerce",
    "05_QUARTERLY_SUPPORT/data": "data/quarterly",
    "06_SCRIPTS": "scripts",
    "08_MANIFESTS/repository_manifests": "sources/manifests",
    "09_ANALYTICAL_FIGURES": "reports/figures",
}


REPORT_MAP = {
    "01_INDONESIA_ISSUER/HYPOTHESIS_TESTS_2026-09-10.md": "reports/HYPOTHESIS_TESTS_2026-09-10.md",
    "01_INDONESIA_ISSUER/HYPOTHESIS_TESTS_VALIDATION_2026-09-10.md": "reports/HYPOTHESIS_TESTS_VALIDATION_2026-09-10.md",
    "03_ASEAN_CORROBORATION/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md": "reports/ASEAN_CORROBORATION_EXTENSION_2026-09-10.md",
    "04_GLOBAL_CORROBORATION/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md": "reports/GLOBAL_ECOMMERCE_CORROBORATION_2026-09-10.md",
}


SOURCE_FILES = [
    "bps_ecommerce_statistics_2024.pdf",
    "bps_marketplace_benefits_risks_2025.pdf",
    "blibli_prospectus.pdf",
    "blibli_fy2022_linked_0.pdf",
    "blibli_fy2023_linked_0.pdf",
    "blibli_fy2024_linked_0.pdf",
    "blibli_fy2025_linked_0.pdf",
    "bukalapak_ar2021_mirror.pdf",
    "bukalapak_ar2022_mirror.pdf",
    "bukalapak_ar2023_mirror.pdf",
    "goto_fy2022_annual_report.pdf",
    "goto_annual_report_2023.pdf",
    "grab_2023_20f.htm",
    "grab_2023_results.htm",
    "sea_2023_20f.htm",
    "katadata_momentumworks_indonesia_2023.htm",
]


def copy_file(source: Path, target: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def csv_rows(path: Path) -> int | None:
    if path.suffix.lower() != ".csv":
        return None
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        return sum(1 for _ in reader)


def build_index(dest: Path) -> None:
    records = []
    for path in sorted(p for p in dest.rglob("*") if p.is_file()):
        rel = path.relative_to(dest).as_posix()
        if rel == "PACKAGE_CONTENTS.csv":
            continue
        records.append({
            "relative_path": rel,
            "module": rel.split("/", 1)[0] if "/" in rel else "ROOT",
            "extension": path.suffix.lower(),
            "bytes": path.stat().st_size,
            "data_rows_or_records": csv_rows(path) if path.suffix.lower() == ".csv" else "",
            "sha256": digest(path),
        })
    with (dest / "PACKAGE_CONTENTS.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def make_zip(dest: Path) -> Path:
    zip_path = dest.with_suffix(".zip")
    if zip_path.exists():
        raise FileExistsError(f"Refusing to overwrite {zip_path}")
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(p for p in dest.rglob("*") if p.is_file()):
            archive.write(path, arcname=f"{dest.name}/{path.relative_to(dest).as_posix()}")
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    args = parser.parse_args()
    dest = args.dest.resolve()
    if dest.exists():
        raise FileExistsError(f"Refusing to overwrite existing package directory: {dest}")
    dest.mkdir(parents=True)

    for target, source in {**FILE_MAP, **REPORT_MAP}.items():
        copy_file(ROOT / source, dest / target)
    for target, source in TREE_MAP.items():
        shutil.copytree(ROOT / source, dest / target)
    for filename in SOURCE_FILES:
        copy_file(ROOT / "sources" / "core_public_documents" / filename, dest / "07_SOURCE_DOCUMENTS" / filename)

    build_index(dest)
    zip_path = make_zip(dest)
    print(dest)
    print(zip_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
