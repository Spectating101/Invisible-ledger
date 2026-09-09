#!/usr/bin/env python3
"""Archive public ASEAN platform-market figures used for corroboration."""

from __future__ import annotations

import csv
import hashlib
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "sources" / "asean_market_sources" / "momentum_public_materials"

URLS = {
    "momentum_2025_figure_1.jpg": "https://thelowdown.momentum.asia/wp-content/uploads/2025/06/Ecommerce-in-Southeast-Asia-3.0_MW_June-2025-1.jpg",
    "momentum_2025_figure_2.jpg": "https://thelowdown.momentum.asia/wp-content/uploads/2025/06/Ecommerce-in-Southeast-Asia-3.0_MW_June-2025-2.jpg",
    "momentum_2025_figure_5.jpg": "https://thelowdown.momentum.asia/wp-content/uploads/2025/06/Ecommerce-in-Southeast-Asia-3.0_MW_June-2025-5.jpg",
    "momentum_2026_press_release.pdf": "https://thelowdown.momentum.asia/wp-content/uploads/2026/04/Embargoed-Press-release-Momentum-Works-Ecommerce-in-SEA-2026.pdf",
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for filename, url in URLS.items():
        target = OUT / filename
        status = "cached"
        if not target.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "Invisible-Ledger academic research; source archival"})
            with urllib.request.urlopen(request, timeout=90) as response:
                target.write_bytes(response.read())
            status = "downloaded"
        payload = target.read_bytes()
        rows.append({
            "filename": filename,
            "url": url,
            "landing_page": "https://thelowdown.momentum.asia/new-report-southeast-asias-platform-ecommerce-gmv-reaches-us128-4b/",
            "status": status,
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "retrieved_at_utc": datetime.fromtimestamp(target.stat().st_mtime, timezone.utc).isoformat(),
        })
    with (OUT / "download_manifest.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"figures_available={len(rows)}")


if __name__ == "__main__":
    main()
