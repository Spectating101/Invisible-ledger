#!/usr/bin/env python3
"""Acquire the public Bank Indonesia source files used by the payment extension.

Existing files are never overwritten unless --force is supplied.  The script is
new research infrastructure created on 11 September 2026; it is not represented
as code used for earlier manuscript results.
"""

from __future__ import annotations

import argparse
import hashlib
import time
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "sources/bank_indonesia_payments/raw"
FILES = {
    SOURCE_DIR / "SPIP-Desember-2025.zip": "https://www.bi.go.id/id/statistik/ekonomi-keuangan/spip/Documents/SPIP-Desember-2025.zip",
    SOURCE_DIR / "reports/Monetary-Policy-Report-Quarter-IV-2023.pdf": "https://www.bi.go.id/en/publikasi/laporan/Documents/Monetary-Policy-Report-Quarter-IV-2023.pdf",
    SOURCE_DIR / "reports/LKTBI-2024.pdf": "https://www.bi.go.id/id/publikasi/ruang-media/news-release/Documents/LKTBI-2024.pdf",
    SOURCE_DIR / "reports/LPI-2025_05_Bab-3.pdf": "https://www.bi.go.id/id/publikasi/laporan/Documents/LPI-2025_05_Bab-3.pdf",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def download(url: str, destination: Path, force: bool) -> None:
    if destination.exists() and not force:
        print(f"preserved {destination.relative_to(ROOT)} sha256={sha256(destination)}")
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; academic-source-archiver/1.0)",
            "Referer": "https://www.bi.go.id/",
        },
    )
    temporary = destination.with_suffix(destination.suffix + ".part")
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                temporary.write_bytes(response.read())
            temporary.replace(destination)
            print(f"downloaded {destination.relative_to(ROOT)} sha256={sha256(destination)}")
            return
        except Exception:
            if temporary.exists():
                temporary.unlink()
            if attempt == 5:
                raise
            time.sleep(attempt)


def extract_workbook(force: bool) -> None:
    archive = SOURCE_DIR / "SPIP-Desember-2025.zip"
    destination = SOURCE_DIR / "SPIP-Desember-2025.xlsx"
    if destination.exists() and not force:
        print(f"preserved {destination.relative_to(ROOT)} sha256={sha256(destination)}")
        return
    with zipfile.ZipFile(archive) as package:
        members = [name for name in package.namelist() if name.endswith("SPIP-Desember-2025.xlsx")]
        if len(members) != 1:
            raise ValueError(f"Expected one SPIP workbook, found {members}")
        destination.write_bytes(package.read(members[0]))
    print(f"extracted {destination.relative_to(ROOT)} sha256={sha256(destination)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="replace existing public source files")
    args = parser.parse_args()
    for destination, url in FILES.items():
        download(url, destination, args.force)
    extract_workbook(args.force)


if __name__ == "__main__":
    main()
