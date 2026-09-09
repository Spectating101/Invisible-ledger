#!/usr/bin/env python3
"""Archive primary annual filings for the global e-commerce corroboration.

The script uses SEC submissions metadata for SEC-reporting issuers and a small
set of issuer-hosted documents for non-US reporters.  It saves source documents
unchanged and writes a provenance manifest.  It does not extract or harmonise
financial observations.
"""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "sources" / "global_ecommerce"
RAW_ROOT = SOURCE_ROOT / "raw"
MANIFEST = SOURCE_ROOT / "global_issuer_document_manifest.csv"
USER_AGENT = "Invisible Ledger academic research contact: repository owner"


def sec_fallback_user_agent() -> str:
    """Return a SEC-compatible declared agent without hard-coding private contact data."""
    try:
        email = subprocess.run(
            ["git", "config", "user.email"], check=True, capture_output=True, text=True
        ).stdout.strip()
    except subprocess.SubprocessError:
        email = ""
    return f"InvisibleLedgerResearch/1.0 {email}" if "@" in email else USER_AGENT

SEC_ISSUERS = {
    "ebay": {"cik": "0001065088", "forms": {"10-K"}},
    "etsy": {"cik": "0001370637", "forms": {"10-K"}},
    "shopify": {"cik": "0001594805", "forms": {"10-K", "40-F"}},
    "jumia": {"cik": "0001756708", "forms": {"20-F"}},
    "mercadolibre": {"cik": "0001099590", "forms": {"10-K"}},
}

# These stable issuer pages/documents establish additional non-SEC candidates.
# Further annual vintages are discovered from the archived pages rather than
# guessed from URL patterns.
ISSUER_URLS = {
    "shopify_fy2019_results": "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2019-financial-results",
    "ebay_fy2020_results": "https://investors.ebayinc.com/investor-news/press-release-details/2021/eBay-Inc.-Reports-Better-Than-Expected-Fourth-Quarter-and-Full-Year-2020-Results/default.aspx",
    "ebay_fy2021_results": "https://investors.ebayinc.com/investor-news/press-release-details/2022/eBay-Inc.-Reports-Better-Than-Expected-Fourth-Quarter-and-Full-Year-2021-Results/default.aspx",
    "ebay_fy2022_results": "https://investors.ebayinc.com/investor-news/press-release-details/2023/eBay-Inc.-Reports-Better-Than-Expected-Fourth-Quarter-2022-Results/default.aspx",
    "ebay_fy2023_results": "https://investors.ebayinc.com/investor-news/press-release-details/2024/eBay-Inc.-Reports-Fourth-Quarter-and-Full-Year-2023-Results/default.aspx",
    "ebay_fy2024_results": "https://investors.ebayinc.com/investor-news/press-release-details/2025/eBay-Inc.-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx",
    "ebay_fy2025_results": "https://investors.ebayinc.com/investor-news/press-release-details/2026/eBay-Inc--Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx",
    "etsy_fy2020_results": "https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-21-000009/exhibit99112312020.htm",
    "etsy_fy2021_results": "https://investors.etsy.com/news-events/press-releases/detail/64/etsy-inc-reports-fourth-quarter-and-full-year-2021-results",
    "etsy_fy2023_results": "https://investors.etsy.com/news-events/press-releases/detail/29/etsy-inc-reports-fourth-quarter-and-full-year-2023-results",
    "etsy_fy2024_results": "https://investors.etsy.com/news-events/press-releases/detail/13/etsy-inc-reports-fourth-quarter-and-full-year-2024-results",
    "etsy_fy2025_10k": "https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-26-000019/etsy-20251231.htm",
    "shopify_fy2020_results": "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2020-financial-results",
    "shopify_fy2021_results": "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2021-financial-results",
    "shopify_fy2022_results": "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2022-financial-results",
    "shopify_fy2023_results": "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2023-financial-results",
    "shopify_fy2024_annual_report": "https://s27.q4cdn.com/572064924/files/doc_financials/2025/ar/49701a1b-f486-481a-b773-e5d6c2c39068.pdf",
    "shopify_fy2025_results": "https://s27.q4cdn.com/572064924/files/doc_financials/2025/q4/Shopify_Investor_Press_Release_Q4-25_FINAL.pdf",
    "jumia_fy2022_results": "https://s205.q4cdn.com/370993272/files/doc_news/2023/02/1/JMIA-Q4-22-ER-16-02-23-vF.pdf",
    "jumia_fy2024_results": "https://investor.jumia.com/files/doc_financials/2024/q4/Jumia-EX-99-1-Q4-2024_v02192025-v4.pdf",
    "jumia_fy2025_results": "https://investor.jumia.com/news/news-details/2026/Jumia-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx",
    "mercadolibre_fy2023_10k": "https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/meli-20231231.htm",
    "mercadolibre_fy2024_10k": "https://www.sec.gov/Archives/edgar/data/1099590/000109959025000007/meli-20241231.htm",
    "mercadolibre_fy2025_10k": "https://investor.mercadolibre.com/open-file?file=aHR0cHM6Ly9odHRwMi5tbHN0YXRpYy5jb20vc3RvcmFnZS9tbC1jbXMtYmFja2VuZC9jbXMtZG9jdW1lbnRzLXByb2Qvc2VjLzAwMDEwOTk1OTAvMDAwMTA5OTU5MC0yNi0wMDAwMDYvZm9ybTEwLUstMDAwMTA5OTU5MC0yNi0wMDAwMDYucGRm",
    "mercadolibre_fy2021_results": "https://investor.mercadolibre.com/download-uspr?path=%2Fnews-and-events%2Fmercadolibre-inc-reports-fourth-quarter-2021-financial-results",
    "rakuten_fy2025_results_deck": "https://global.rakuten.com/corp/investors/assets/doc/documents/25Q4MAINPPT_E.pdf",
    "rakuten_financial_indicators": "https://global.rakuten.com/corp/investors/financial/indicators.html",
    "zalando_key_figures_2021": "https://corporate.zalando.com/en/investor-relations/key-figures-2021",
    "zalando_key_figures_2022": "https://corporate.zalando.com/en/investor-relations/key-figures-2022",
    "zalando_fy2023_results": "https://corporate.zalando.com/en/financials/zalando-full-year-23-results",
    "zalando_key_figures_2024": "https://corporate.zalando.com/en/investor-relations/key-figures-2024",
    "zalando_key_figures_2025": "https://corporate.zalando.com/en/investor-relations/key-figures-2025",
    "allegro_annual_report_2025": "https://about.allegro.eu/static-files/2014bc8d-1806-47d6-bc34-350f6ba7c72a",
}


def request_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            return response.read()
    except urllib.error.HTTPError as error:
        if error.code != 403:
            raise
        # EDGAR archive endpoints occasionally reject urllib while accepting
        # the same declared research user-agent through curl. Keep this
        # deterministic fallback inside the acquisition script.
        try:
            completed = subprocess.run(
                ["curl", "-L", "--fail", "--silent", "--show-error", "--max-time", "90",
                 "-A", sec_fallback_user_agent(), url],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as curl_error:
            # Do not leak the locally resolved SEC contact string into the
            # public acquisition manifest.
            raise RuntimeError(
                f"curl fallback failed with exit status {curl_error.returncode}"
            ) from curl_error
        return completed.stdout


def safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in value)


def save_document(issuer: str, source_id: str, url: str, data: bytes) -> dict[str, str | int]:
    suffix = Path(urlparse(url).path).suffix.lower()
    if data.startswith(b"%PDF"):
        suffix = ".pdf"
    elif suffix not in {".htm", ".html", ".json", ".pdf"}:
        suffix = ".html"
    relative = Path("raw") / issuer / f"{safe_name(source_id)}{suffix}"
    destination = SOURCE_ROOT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return {
        "issuer": issuer,
        "source_id": source_id,
        "source_type": "primary issuer filing/document",
        "url": url,
        "file": str(Path("sources/global_ecommerce") / relative),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "status": "downloaded",
        "error": "",
    }


def sec_filing_rows(issuer: str, cik: str, allowed_forms: set[str]) -> list[dict[str, str | int]]:
    submissions_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    submission_data = request_bytes(submissions_url)
    rows = [save_document(issuer, f"{issuer}_sec_submissions", submissions_url, submission_data)]
    metadata = json.loads(submission_data)
    recent = metadata["filings"]["recent"]
    chosen: dict[tuple[str, str], tuple[str, str, str, str]] = {}
    for form, report_date, filing_date, accession, primary in zip(
        recent["form"], recent["reportDate"], recent["filingDate"],
        recent["accessionNumber"], recent["primaryDocument"], strict=True,
    ):
        if form not in allowed_forms or not report_date:
            continue
        year = report_date[:4]
        if not ("2015" <= year <= "2025"):
            continue
        key = (form, year)
        candidate = (filing_date, accession, primary, report_date)
        if key not in chosen or candidate[0] > chosen[key][0]:
            chosen[key] = candidate

    cik_plain = str(int(cik))
    for (form, year), (filing_date, accession, primary, report_date) in sorted(chosen.items()):
        accession_plain = accession.replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik_plain}/{accession_plain}/{primary}"
        source_id = f"{issuer}_{year}_{form.lower().replace('-', '')}_{accession_plain}"
        try:
            row = save_document(issuer, source_id, url, request_bytes(url))
            row.update({"form": form, "report_date": report_date, "filing_date": filing_date})
        except Exception as error:  # preserve failed acquisition attempts
            row = {
                "issuer": issuer, "source_id": source_id,
                "source_type": "primary SEC filing", "url": url, "file": "",
                "bytes": 0, "sha256": "", "status": "failed", "error": str(error),
                "form": form, "report_date": report_date, "filing_date": filing_date,
            }
        rows.append(row)
        time.sleep(0.12)
    return rows


def main() -> None:
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str | int]] = []
    for issuer, config in SEC_ISSUERS.items():
        try:
            rows.extend(sec_filing_rows(issuer, config["cik"], config["forms"]))
        except Exception as error:
            rows.append({
                "issuer": issuer, "source_id": f"{issuer}_sec_submissions",
                "source_type": "SEC submissions metadata", "url": "", "file": "",
                "bytes": 0, "sha256": "", "status": "failed", "error": str(error),
            })

    for source_id, url in ISSUER_URLS.items():
        issuer = source_id.split("_", 1)[0]
        try:
            rows.append(save_document(issuer, source_id, url, request_bytes(url)))
        except Exception as error:
            rows.append({
                "issuer": issuer, "source_id": source_id,
                "source_type": "primary issuer document", "url": url, "file": "",
                "bytes": 0, "sha256": "", "status": "failed", "error": str(error),
            })

    fieldnames = [
        "issuer", "source_id", "source_type", "form", "report_date", "filing_date",
        "url", "file", "bytes", "sha256", "status", "error",
    ]
    with MANIFEST.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {MANIFEST.relative_to(ROOT)} with {len(rows)} acquisition records")


if __name__ == "__main__":
    try:
        main()
    except (urllib.error.URLError, TimeoutError) as error:
        raise SystemExit(f"Acquisition failed: {error}") from error
