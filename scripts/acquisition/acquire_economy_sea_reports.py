#!/usr/bin/env python3
"""Download the official Google–Temasek–Bain e-Conomy SEA report archive.

Downloads are stored unchanged. A manifest records retrieval status, size and
SHA-256. Country reports are evidence inputs, not automatically comparable
observations.
"""

from __future__ import annotations

import csv
import hashlib
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "sources" / "asean_economy_reports"
MANIFEST = OUT / "download_manifest.csv"

FULL_REPORTS = {
    2016: "https://storage.googleapis.com/gweb-economy-sea.appspot.com/assets/pdf/e-Conomy_SEA_2016_report.pdf",
    2017: "https://storage.googleapis.com/gweb-economy-sea.appspot.com/assets/pdf/e-Conomy_SEA_2017_report.pdf",
    2018: "https://storage.googleapis.com/gweb-economy-sea.appspot.com/assets/pdf/e-Conomy_SEA_2018_report.pdf",
    2019: "https://storage.googleapis.com/gweb-economy-sea.appspot.com/assets/pdf/e-Conomy_SEA_2019_report.pdf",
    2020: "https://storage.googleapis.com/gweb-economy-sea.appspot.com/assets/pdf/e-Conomy_SEA_2020_Report.pdf",
    2021: "https://services.google.com/fh/files/misc/e_conomy_sea_2021_report.pdf",
    2022: "https://services.google.com/fh/files/misc/e_conomy_sea_2022_report.pdf",
}

COUNTRIES = {
    "indonesia": "Indonesia",
    "malaysia": "Malaysia",
    "philippines": "Philippines",
    "singapore": "Singapore",
    "thailand": "Thailand",
    "vietnam": "Vietnam",
}


def report_queue() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for year, url in FULL_REPORTS.items():
        rows.append(
            {
                "year": year,
                "geography": "SEA-6",
                "report_scope": "regional_full_report",
                "url": url,
                "filename": f"economy_sea_{year}_regional.pdf",
            }
        )
    for year in (2023, 2024, 2025):
        for slug, country in COUNTRIES.items():
            rows.append(
                {
                    "year": year,
                    "geography": country,
                    "report_scope": "country_report",
                    "url": f"https://services.google.com/fh/files/misc/{slug}_e_conomy_sea_{year}_report.pdf",
                    "filename": f"economy_sea_{year}_{slug}.pdf",
                }
            )
    return rows


def download(row: dict[str, object]) -> dict[str, object]:
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / str(row["filename"])
    status = "cached"
    error = ""
    if not target.exists():
        request = urllib.request.Request(
            str(row["url"]),
            headers={"User-Agent": "Invisible-Ledger academic research; source archival"},
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = response.read()
            if not payload.startswith(b"%PDF"):
                raise ValueError("response is not a PDF")
            target.write_bytes(payload)
            status = "downloaded"
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            status = "failed"
            error = str(exc)
    payload = target.read_bytes() if target.exists() else b""
    return {
        **row,
        "status": status,
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest() if payload else "",
        "retrieved_at_utc": (
            datetime.fromtimestamp(target.stat().st_mtime, timezone.utc).isoformat()
            if target.exists() else datetime.now(timezone.utc).isoformat()
        ),
        "error": error,
    }


def main() -> None:
    results = [download(row) for row in report_queue()]
    fields = [
        "year",
        "geography",
        "report_scope",
        "url",
        "filename",
        "status",
        "bytes",
        "sha256",
        "retrieved_at_utc",
        "error",
    ]
    with MANIFEST.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)
    failures = [row for row in results if row["status"] == "failed"]
    print(f"Reports queued: {len(results)}")
    print(f"Reports available: {len(results) - len(failures)}")
    print(f"Failures: {len(failures)}")
    for row in failures:
        print(f"  {row['year']} {row['geography']}: {row['error']}")


if __name__ == "__main__":
    main()
