#!/usr/bin/env python3
"""Archive official sources for the ASEAN tax/platform context table."""

from __future__ import annotations

import csv
import hashlib
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "sources" / "asean_tax_sources"

SOURCES = [
    ("Indonesia", "indonesia_dgt_digital_tax.html", "https://pajak.go.id/en/digitaltax"),
    ("Malaysia", "malaysia_mystods_faq_business.html", "https://mysst.customs.gov.my/faq-business/"),
    ("Singapore", "singapore_iras_overseas_businesses.html", "https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/overseas-businesses"),
    ("Thailand", "thailand_revenue_department_eservice_guide.pdf", "https://www.rd.go.th/fileadmin/download/eService.pdf"),
    ("Philippines", "philippines_bir_rr_3_2025.pdf", "https://bir-cdn.bir.gov.ph/BIR/pdf/RR%203-2025.pdf"),
    ("Vietnam", "vietnam_decree_117_2025.html", "https://vanban.chinhphu.vn/?classid=1&docid=213883&orggroupid=2&pageid=27160"),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for country, filename, url in SOURCES:
        target = OUT / filename
        status = "cached"
        error = ""
        if not target.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Invisible-Ledger academic research"})
            try:
                with urllib.request.urlopen(request, timeout=20) as response:
                    target.write_bytes(response.read())
                status = "downloaded"
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                status = "failed"
                error = str(exc)
        payload = target.read_bytes() if target.exists() else b""
        rows.append({
            "country": country,
            "filename": filename,
            "url": url,
            "status": status,
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest() if payload else "",
            "retrieved_at_utc": (
                datetime.fromtimestamp(target.stat().st_mtime, timezone.utc).isoformat()
                if target.exists() else datetime.now(timezone.utc).isoformat()
            ),
            "error": error,
        })
    with (OUT / "download_manifest.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    failures = [row for row in rows if row["status"] == "failed"]
    print(f"sources_available={len(rows) - len(failures)}")
    print(f"failures={len(failures)}")
    for row in failures:
        print(f"  {row['country']}: {row['error']}")


if __name__ == "__main__":
    main()
