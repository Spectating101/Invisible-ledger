# Bank Indonesia payment-system source layer

This directory preserves the official source material used for the payment-ledger extension.

## Files

- `raw/SPIP-Desember-2025.zip` is the unchanged archive downloaded from Bank Indonesia's December 2025 SPIP page.
- `raw/SPIP-Desember-2025.xlsx` is the unchanged workbook member extracted from that ZIP.
- `raw/reports/Monetary-Policy-Report-Quarter-IV-2023.pdf` supports the 2023 headline payment observations.
- `raw/reports/LKTBI-2024.pdf` supports the 2024 QRIS observations.
- `raw/reports/LPI-2025_05_Bab-3.pdf` supports the 2025 QRIS observations.
- `source_manifest_2026-09-11.csv` records URLs, sizes, hashes and source roles.

Bank Indonesia describes SPIP as official payment-system and financial-market-infrastructure statistics compiled from Bank Indonesia data and cooperating authorities. The workbook contains multiple payment objects. It is not an e-commerce dataset, and transaction values from different tables must not be added together without checking overlap and definitions.

The December 2025 workbook's monthly blocks end at November 2025. No December 2025 value is manufactured. The published annual columns are preserved separately from the monthly columns.

## Transformations

Run:

```bash
python3 scripts/extraction/extract_bank_indonesia_spip.py
python3 scripts/analysis/build_payment_ledger_extension.py
```

The first script mechanically reshapes the source workbook into long-form CSV files while preserving the source sheet, row, label, unit and published value. The second script creates descriptive comparisons. Neither script interpolates missing periods or treats payments as platform sales.

Primary source page: [Bank Indonesia SPIP December 2025](https://www.bi.go.id/id/statistik/ekonomi-keuangan/spip/Pages/SPIP-Desember-2025.aspx).
