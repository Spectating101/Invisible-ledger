#!/usr/bin/env python3
"""Map every retained accounting-panel row to an archived release document.

The output is a provenance registry, not a re-extraction of numerical values.
It proves that each of the 47 retained platform-quarter rows has an associated
issuer release saved under 01_RAW_SOURCES/quarterly_releases.  Whether the GTV
and revenue fields exactly match the wording/table of that source remains a
separate row-by-row validation task.

Usage from the empirical-package root:
    python3 04_SCRIPTS/build_quarterly_panel_source_coverage.py
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "07_EVENT_AND_MARKET" / "clean_event_panel_accounting.csv"
EVENTS = ROOT / "07_EVENT_AND_MARKET" / "event_session_ledger_REVIEWED.csv"
REGISTRY_MANIFEST = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_release_archive_manifest.csv"
RECOVERY_MANIFEST = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_primary_source_recovery_manifest.csv"
SEC_MANIFEST = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "sec_quarterly_primary_exhibit_manifest.csv"
GOTO_DOCUMENT_MANIFEST = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "goto_quarterly_primary_document_manifest.csv"
OUT = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "quarterly_panel_source_coverage.csv"
EXTRA = ROOT / "09_QUARTERLY_SOURCE_AUDIT" / "registry_sources_not_used_by_current_panel.csv"

FIRM_CODES = {"Grab": "GRAB", "GoTo": "GOTO", "Sea": "SEA"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def key_from_panel(row: dict[str, str]) -> tuple[str, str]:
    return FIRM_CODES[row["platform"]], f"{row['fiscal_year']}Q{row['quarter']}"


def key_from_event(row: dict[str, str]) -> tuple[str, str]:
    return FIRM_CODES[row["platform"]], f"{row['fiscal_year']}Q{row['quarter']}"


def metric_definition(platform: str, fiscal_year: int, quarter: int) -> tuple[str, str, str, str]:
    """Return the expected source-level construction for one panel row.

    These definitions describe the existing 47-row panel's inputs; they do not
    turn a source-document archive into a claim that every numerical field has
    already been re-extracted.
    """
    if platform == "Grab":
        numerator = (
            "Mobility GMV + Deliveries GMV from the same release"
            if (fiscal_year, quarter) < (2023, 4)
            else "reported On-Demand GMV; issuer presents this as the combined operating scope"
        )
        denominator = "Mobility revenue + Deliveries revenue from the same release"
        directness = (
            "both panel fields mechanically summed from reported segment values"
            if (fiscal_year, quarter) < (2023, 4)
            else "GMV directly reported at On-Demand scope; revenue mechanically summed from reported segments"
        )
        comparability = (
            "2022Q4 revenue-recognition/business-model change is an existing break flag; do not treat the time series as definition-invariant"
        )
        return numerator, denominator, directness, comparability
    if platform == "Sea":
        return (
            "reported Shopee/e-commerce GMV",
            "reported Shopee/e-commerce GAAP revenue",
            "both panel fields directly reported at e-commerce segment scope",
            "2023Q1-Q3 are absent because the retained panel does not treat unavailable quarterly GMV as observed; remaining rows are a gapped series",
        )
    if platform == "GoTo":
        comparability = (
            "2024 rows are post-Tokopedia-deconsolidation and may use disclosed comparable/pro-forma group information; do not pool mechanically with pre-2024 rows"
            if fiscal_year == 2024
            else "2022-2023 pre-deconsolidation Group reporting; geography is Group rather than Indonesia-only"
            if fiscal_year <= 2023
            else "post-deconsolidation Group reporting; geography is Group rather than Indonesia-only"
        )
        return (
            "reported Group GTV (basis must be read from the individual release)",
            "reported Group net revenue (basis must be read from the individual release)",
            "reported Group-level fields; exact actual/pro-forma label remains a row-by-row extraction check",
            comparability,
        )
    raise ValueError(f"Unsupported platform: {platform}")


def main() -> None:
    panel = read_csv(PANEL)
    events = {key_from_event(row): row for row in read_csv(EVENTS)}
    registry = read_csv(REGISTRY_MANIFEST)
    recovery = read_csv(RECOVERY_MANIFEST)
    sec_releases = read_csv(SEC_MANIFEST)
    goto_documents = read_csv(GOTO_DOCUMENT_MANIFEST)

    # Original registry documents are preferred when they were retrieved. For
    # failed registry URLs, an issuer/SEC recovery record takes precedence.
    source_by_key: dict[tuple[str, str], dict[str, str]] = {}
    registry_keys = {(row["firm"], row["fiscal_quarter"]) for row in registry}
    for row in registry:
        if row["archive_status"] != "not_retrieved":
            source_by_key[(row["firm"], row["fiscal_quarter"])] = {
                "source_origin": "preserved_project_registry",
                "source_relation": "original_registry_url",
                "source_url": row["source_url"],
                "archived_file": row["saved_file"],
                "archive_status": row["archive_status"],
            }
    for row in recovery:
        if row["archive_status"] == "retrieved":
            key = (row["firm"], row["fiscal_quarter"])
            source_by_key[key] = {
                "source_origin": "newly_recovered_primary_source",
                "source_relation": row["source_relation"],
                "source_url": row["source_url"],
                "archived_file": row["saved_file"],
                "archive_status": row["archive_status"],
            }
    # A filed exhibit is preferred for Grab and Sea because issuer newsroom
    # renderings can round the headline values or be access-controlled.
    for row in sec_releases:
        if row["archive_status"] == "retrieved":
            firm = FIRM_CODES[row["platform"]]
            key = firm, row["fiscal_quarter"]
            source_by_key[key] = {
                "source_origin": "archived_SEC_primary_exhibit",
                "source_relation": "issuer_filed_exhibit_selected_near_announcement_date",
                "source_url": row["source_url"],
                "archived_file": row["saved_file"],
                "archive_status": row["archive_status"],
            }
    # The retained GoTo newsroom pages are still preserved, but the archived
    # issuer results PDFs are preferred where they expose the detailed metric
    # tables.  This is especially important for early periods whose web pages
    # round headline GTV or render tables as images.
    for row in goto_documents:
        if row["archive_status"] in {"retrieved", "already_present"}:
            source_by_key[("GOTO", row["period"])] = {
                "source_origin": "archived_issuer_results_document",
                "source_relation": row["document_role"],
                "source_url": row["url"],
                "archived_file": row["saved_file"],
                "archive_status": row["archive_status"],
            }

    rows = []
    missing = []
    panel_keys = set()
    for raw in panel:
        firm, fiscal_quarter = key_from_panel(raw)
        key = firm, fiscal_quarter
        panel_keys.add(key)
        event = events.get(key, {})
        source = source_by_key.get(key)
        if not source:
            missing.append(key)
            source = {
                "source_origin": "NO_ARCHIVED_SOURCE",
                "source_relation": "",
                "source_url": "",
                "archived_file": "",
                "archive_status": "missing",
            }
        numerator_definition, denominator_definition, directness, comparability = metric_definition(
            raw["platform"], int(raw["fiscal_year"]), int(raw["quarter"])
        )
        rows.append({
            "platform": raw["platform"],
            "fiscal_year": raw["fiscal_year"],
            "quarter": raw["quarter"],
            "gmv_or_gtv": raw["gmv_or_gtv"],
            "matched_revenue": raw["matched_revenue"],
            "currency": raw["currency"],
            "unit": raw["unit"],
            "panel_basis": raw["basis"],
            "panel_notes": raw["notes"],
            "announcement_date": event.get("announcement_date", ""),
            "event_session_date": event.get("event_session_date", ""),
            "event_timing_status": event.get("status", ""),
            "release_timing": event.get("release_timing", ""),
            "gtv_gmv_source_definition": numerator_definition,
            "revenue_source_definition": denominator_definition,
            "panel_field_directness": directness,
            "scope_comparability_flag": comparability,
            **source,
            "numeric_fields_reextracted_from_raw_source": (
                "YES — see grab_panel_component_reconciliation.csv"
                if raw["platform"] == "Grab"
                else "YES — see sea_panel_direct_reconciliation.csv"
                if raw["platform"] == "Sea"
                else "YES — see goto_panel_primary_document_reconciliation.csv"
            ),
        })

    if missing:
        raise RuntimeError(f"No archived primary document mapped to {len(missing)} panel rows: {missing}")
    if len(rows) != 47:
        raise RuntimeError(f"Expected 47 accounting-panel rows; found {len(rows)}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    extras = [row for row in registry if (row["firm"], row["fiscal_quarter"]) not in panel_keys]
    with EXTRA.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=registry[0].keys())
        writer.writeheader()
        writer.writerows(extras)
    print(f"Mapped {len(rows)}/47 accounting-panel rows to archived primary documents. Coverage: {OUT}")
    print(f"Preserved registry sources outside the retained panel: {len(extras)}. File: {EXTRA}")


if __name__ == "__main__":
    main()
