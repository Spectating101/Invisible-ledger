# Bank Indonesia payment-ledger extension

## Bottom line

The payment data are available, source-auditable, and materially expand the empirical backend. The official Bank Indonesia archive yields:

| Extract | Rows | Coverage | Role |
|---|---:|---|---|
| National monthly SPIP | 18,954 | January 2009-November 2025 | Broad national payment-system inventory |
| Regional monthly SPIP | 42,701 | January 2009-November 2025 | Regional payment-system inventory |
| National published annual SPIP | 1,460 | 2009-2024 | Issuer-published annual columns, not recomputed totals |
| Core national monthly subset | 3,616 | January 2009-November 2025 | Cards, electronic money, merchants, transfers and digital-banking channels |
| Core national published annual subset | 278 | 2009-2024 | Compact annual research layer |
| Official report observations | 14 | 2023-2025 | QRIS and headline payment measures from separate BI reports |

These counts are observations across many metrics, dates and geographies. They are not an e-commerce sample N and must not be added to the issuer, BPS or ASEAN sample counts.

Bank Indonesia describes SPIP as official statistics covering payment systems and financial-market infrastructure. Its tables include cash and noncash instruments, infrastructure and payment channels. The December 2025 release and its original workbook are preserved under `sources/bank_indonesia_payments/`. See the [SPIP overview](https://www.bi.go.id/id/statistik/ekonomi-keuangan/spip/pengantar.aspx), [December 2025 release](https://www.bi.go.id/id/statistik/ekonomi-keuangan/spip/Pages/SPIP-Desember-2025.aspx), and [SPIP metadata](https://www.bi.go.id/id/statistik/Metadata/metadata-SPIP/Default.aspx).

## What was recovered

The national extraction preserves six official tables:

- ATM and debit cards (`5a`);
- credit cards (`5c`);
- electronic money (`5e`);
- card/electronic-money merchant infrastructure (`5g`);
- non-bank fund transfers (`6`);
- proprietary channels, including mobile and internet banking (`7`).

The regional extraction preserves the corresponding regional tables `5b`, `5d`, `5f` and `5h`. Each CSV row retains the source sheet, workbook row, original indicator label, unit, period and value.

The source workbook provides complete published annual columns through 2024. Its 2025 monthly block runs from January through November. The extraction therefore does not call 2025 a completed fiscal year and does not synthesize a December observation.

QRIS is not a named table in this SPIP workbook. It is kept in a separate 14-row official-report file rather than being forced into the SPIP table structure. Bank Indonesia directly reports:

- 2023 QRIS value of Rp229.96 trillion, 45.78 million users and 30.41 million merchants in its [Q4 2023 Monetary Policy Report](https://www.bi.go.id/en/publikasi/laporan/Documents/Monetary-Policy-Report-Quarter-IV-2023.pdf);
- 2024 QRIS volume of 6.24 billion transactions, value of Rp659.94 trillion, 55.4 million users and 35.9 million merchants in its [2024 institutional report](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Documents/LKTBI-2024.pdf);
- Q4 2025 users of 59.53 million, merchants of 42.75 million, volume growth of 139.99% year on year and nominal growth of 107.22% year on year in its [2025 Indonesia Economy Report, chapter 3](https://www.bi.go.id/id/publikasi/laporan/Documents/LPI-2025_05_Bab-3.pdf).

## What the first comparison shows

The executed 2023-2024 comparison keeps BPS e-commerce, SPIP payments and QRIS as separate evidence layers.

| Observation | 2023-2024 growth |
|---|---:|
| BPS total e-commerce value | 17.08% |
| BPS marketplace component | 1.45% |
| BPS non-marketplace component | 20.57% |
| SPIP electronic-money shopping value | 30.47% |
| SPIP mobile-banking payment/purchase value | 82.84% |
| QRIS transaction value | 186.98% |

This is not evidence that one series validates or explains another. It is evidence that the payment trace, the sales-media estimate and the platform-company view are different observational objects with different growth dynamics.

The comparison is economically useful because a statement such as "digital commerce grew 17%" does not imply that every payment rail, sales channel or platform-accounting measure grew at 17%. A rapidly expanding payment trace can coexist with much slower growth in one marketplace component. Reconciliation asks what each series covers before drawing a conclusion.

## A useful definition result inside Bank Indonesia's own publications

The extension also exposes why source labels cannot be treated as interchangeable.

For 2023:

| Comparison | Report headline | Candidate SPIP quantity | Difference |
|---|---:|---:|---:|
| Digital banking vs proprietary-channel total | Rp58,478.24T | Rp58,324.90T | -0.26% |
| Electronic money vs all table-5e transaction components | Rp835.84T | Rp1,859.95T | +122.52% |
| Electronic money vs table-5e shopping only | Rp835.84T | Rp457.73T | -45.24% |
| Card headline vs ATM/debit plus credit-card totals | Rp8,178.69T | Rp8,210.95T | +0.39% |

These are definition cross-checks, not completed reconciliations. In particular, the SPIP electronic-money total includes shopping, transfers, top-ups and other components, while its shopping line is narrower. The BI report headline sits between those quantities. That does not show an error; it shows that a label such as "electronic-money transaction value" is insufficient without the underlying metadata.

This is directly relevant to the paper's method: even within one authoritative institution, differently presented payment quantities can describe different scopes. The research contribution is to preserve and reconcile those definitions before substituting one ledger for another.

## What this adds to Invisible Ledger

The payment layer provides a genuinely independent observation system:

```text
commercial activity
    |-- issuer ledger: transaction value, revenue, incentives
    |-- BPS ledger: estimated sales, channels, businesses
    `-- payment ledger: instruments, payment volume/value, merchants
```

It improves the thesis in three ways.

1. It supplies long-run monthly and annual evidence that digital transaction traces have expanded substantially; the backend is no longer confined to issuer disclosures or a one-year comparison.
2. It creates a direct empirical example of ledger dependence: payment growth and e-commerce-channel growth can differ sharply because they observe different actions and populations.
3. It makes the institutional stakes more concrete. Digital activity may leave detailed payment traces even when those traces are not equivalent to merchant accounts, corporate revenue, BPS sales estimates or tax records.

## What it does not establish

The payment layer cannot be used to claim any of the following:

- that all payment transactions are e-commerce sales;
- that a payment value equals platform GMV or BPS e-commerce value;
- that one commercial sale produces exactly one payment-system record;
- that payment traces are linked to merchant financial statements or tax filings;
- that fast payment growth measures missing GDP, undeclared income, unpaid tax or tax evasion;
- that the regional rows form a merchant-level panel.

Transfers, top-ups, cash withdrawals, person-to-person transactions, refunds, repeated flows and differences in reporting scope can all separate payment values from underlying sales. The payment data therefore belong as an independent corroboration and measurement layer, not as extra rows in the Indonesia issuer sample.

## Recommended paper role

The best immediate use is a compact supporting section or figure showing that the observable digital trace depends on the measurement system:

1. issuer evidence shows transaction and recognized-revenue divergence;
2. BPS evidence shows marketplace and non-marketplace sales-media divergence;
3. Bank Indonesia evidence shows payment-instrument and channel growth with its own definitions;
4. the discussion then asks which linkages among these records are established, regulated, or still unknown.

This strengthens the original economic-measurement ambition without reviving the invalid claim that transaction value minus platform revenue is itself a hidden economy or tax gap.

## Reproduction

```bash
python3 scripts/extraction/extract_bank_indonesia_spip.py
python3 scripts/analysis/build_payment_ledger_extension.py
```

Outputs:

- `data/payments/bank_indonesia_spip_national_monthly_2009_2025.csv`
- `data/payments/bank_indonesia_spip_regional_monthly_2009_2025.csv`
- `data/payments/bank_indonesia_spip_national_published_annual_2009_2024.csv`
- `data/payments/bank_indonesia_payments_core_monthly_2009_2025.csv`
- `data/payments/bank_indonesia_payments_core_published_annual_2009_2024.csv`
- `data/payments/bank_indonesia_payment_report_observations_2023_2025.csv`
- `outputs/payment_ledger_2026-09-11/bps_payment_growth_comparison_2023_2024.csv`
- `outputs/payment_ledger_2026-09-11/bank_indonesia_definition_crosscheck_2023.csv`

The raw archive and workbook hashes are recorded in `sources/bank_indonesia_payments/source_manifest_2026-09-11.csv` and propagated into the extract inventory.
