# Reproduction guide

Run commands from the extracted package root.

## Check the package first

```bash
python3 06_SCRIPTS/packaging/validate_kong_review_package.py
```

This verifies required files, recorded hashes, and CSV row counts. Row counts
describe each file in its own grain and are not added into one analytical N.

## Rebuild the hypothesis outputs

The analysis scripts retain their repository-relative paths. The package keeps
the same data and output directory names inside each empirical module, but the
advisor-facing folders are reorganized for readability. Therefore, the scripts
are included as auditable code and should be run in the full GitHub repository
unless a script explicitly states that it is portable.

Full repository checks:

```bash
python3 scripts/analysis/build_hypothesis_tests.py
python3 scripts/analysis/validate_empirical_certification.py
python3 scripts/analysis/build_asean_corroboration.py
python3 scripts/analysis/build_global_ecommerce_corroboration.py
python3 scripts/validate_repo.py
```

The package preserves the exact input CSVs and reported outputs needed to
inspect those results. It does not rewrite historical scripts merely to make
the reorganized advisor folder look executable.

## What can be reproduced directly

| Result family | Input | Code | Output |
|---|---|---|---|
| Indonesia issuer transitions | `01_INDONESIA_ISSUER/data` | `06_SCRIPTS/analysis/build_hypothesis_tests.py` | `01_INDONESIA_ISSUER/outputs` |
| BPS national decomposition | `02_BPS_OFFICIAL/data` | `06_SCRIPTS/analysis/build_hypothesis_tests.py` | `02_BPS_OFFICIAL/outputs` |
| ASEAN country histories | `03_ASEAN_CORROBORATION/data` | `06_SCRIPTS/analysis/build_asean_corroboration.py` | `03_ASEAN_CORROBORATION/reports` |
| Global issuer comparison | `04_GLOBAL_CORROBORATION/data` | `06_SCRIPTS/analysis/build_global_ecommerce_corroboration.py` | `04_GLOBAL_CORROBORATION/reports` |
| Sample count certification | Indonesia/BPS/global files above | `06_SCRIPTS/analysis/validate_empirical_certification.py` | Console checks and certification notes |

## Source audit

`08_MANIFESTS/PACKAGE_CONTENTS.csv` records the size, SHA-256 hash, and CSV row
count of every submitted file. Source-document manifests preserve original URLs
and retrieval status. Files in `07_SOURCE_DOCUMENTS` are unchanged copies of
the archived public documents.

