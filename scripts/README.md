# Scripts

## `acquisition/`

Later code used to download public issuer, market, World Bank and market-research materials and produce retrieval manifests. Re-running it may produce new publication vintages or encounter changed URLs.

## `extraction/`

Code used to extract selected issuer metrics and reconcile quarterly disclosures. OCR-assisted outputs always require visual source checks.

## `analysis/`

Original project scripts and later reconstruction/validation code. Several original scripts retain their historical directory assumptions. They are preserved for lineage and should not be described as a clean end-to-end pipeline without adaptation.

Primary Python dependencies are listed in `requirements.txt`. Some extraction tasks also require Poppler's `pdftotext` command.

Run `python scripts/validate_repo.py` for repository-level structural and CSV checks.

