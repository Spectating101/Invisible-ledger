# Scripts

## First hypothesis tests

- `analysis/build_hypothesis_tests.py` executes the first longitudinal
  Indonesia candidate analysis and BPS growth/recordkeeping tests. It writes
  only derived outputs under `outputs/hypothesis_tests_2026-09-10/`, figures
  under `reports/figures/`, and the technical readout
  `reports/HYPOTHESIS_TESTS_2026-09-10.md`.

Run from the repository root:

```bash
python3 scripts/analysis/build_hypothesis_tests.py
```

## Global e-commerce corroboration

- `acquisition/acquire_global_ecommerce_sources.py` archives issuer-hosted
  results materials and SEC filing metadata, then writes a URL/hash/status
  manifest. Raw downloads are intentionally ignored by Git.
- `analysis/build_global_ecommerce_corroboration.py` validates 48 reviewed
  matched issuer-year transcriptions, calculates within-issuer measures and
  growth transitions, preserves scope and publication-vintage flags, and
  produces the global corroboration figures.

Run the analytical build from the repository root:

```bash
python3 scripts/analysis/build_global_ecommerce_corroboration.py
```

## Bank Indonesia payment-ledger extension

- `acquisition/acquire_bank_indonesia_payments.py` downloads the selected
  official SPIP archive and BI reports without overwriting existing files by
  default.
- `extraction/extract_bank_indonesia_spip.py` reshapes the official workbook
  into source-row-addressable national, regional and core CSV layers.
- `analysis/build_payment_ledger_extension.py` builds the BPS/payment growth
  comparison and BI definition cross-check.
- `analysis/validate_payment_ledger_extension.py` validates row identities,
  time coverage and source hashes.

Run from the repository root:

```bash
python3 scripts/acquisition/acquire_bank_indonesia_payments.py
python3 scripts/extraction/extract_bank_indonesia_spip.py
python3 scripts/analysis/build_payment_ledger_extension.py
python3 scripts/analysis/validate_payment_ledger_extension.py
```

## `acquisition/`

Later code used to download public issuer, market, World Bank and market-research materials and produce retrieval manifests. Re-running it may produce new publication vintages or encounter changed URLs.

## `extraction/`

Code used to extract selected issuer metrics and reconcile quarterly disclosures. OCR-assisted outputs always require visual source checks.

## `analysis/`

Original project scripts and later reconstruction/validation code. Several original scripts retain their historical directory assumptions. They are preserved for lineage and should not be described as a clean end-to-end pipeline without adaptation.

Primary Python dependencies are listed in `requirements.txt`. Some extraction tasks also require Poppler's `pdftotext` command.

Run `python scripts/validate_repo.py` for repository-level structural and CSV checks.
