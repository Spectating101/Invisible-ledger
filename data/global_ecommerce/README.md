# Global e-commerce corroboration

This directory tests whether the transaction-versus-recognized-revenue
measurement boundary seen in *Invisible Ledger* also appears in other platform
businesses. It is a separate supporting module. It does not enlarge the
proposed Indonesia main sample, pool countries, or estimate missing GDP,
undeclared income, unpaid tax, or tax evasion.

## Files

| File | Rows | Grain and role |
|---|---:|---|
| `global_platform_source_inputs.csv` | 48 | One issuer × segment × fiscal year matched transaction/revenue pair transcribed from issuer materials. |
| `global_platform_matched_annual.csv` | 48 | The same pairs plus mechanically calculated take rate, difference, and ecosystem ratio. |
| `global_platform_growth_divergence.csv` | 40 | One consecutive within-issuer annual transition, with perimeter-break flags. |
| `global_platform_definition_map.csv` | 8 | One issuer/segment definition record explaining the transaction and revenue perimeter. |
| `global_platform_issuer_summary.csv` | 8 | Within-issuer time coverage and take-rate trajectory; not a pooled estimate. |
| `global_platform_coverage.csv` | 13 | Admission, candidate, and exclusion decisions for reviewed issuers. |
| `global_platform_vintage_diagnostics.csv` | 8 | Zalando publication-vintage revisions; repeated vintages are not extra observations. |
| `global_platform_summary.csv` | 8 | Mechanical module counts and diagnostics. |

## Coverage

The 48 matched issuer-years cover eight businesses and fiscal years 2017–2025:

- Sea/Shopee: 9;
- Etsy and Shopify: 7 each;
- eBay and Zalando: 6 each;
- Jumia and Mercado Libre: 5 each;
- Rakuten Domestic EC: 3.

They span Southeast Asia and other Shopee markets, global platform businesses,
Africa, Europe, Japan, and Latin America. This is purposive issuer coverage,
not a representative sample of global e-commerce.

## Reproduction

Run:

```bash
python3 scripts/analysis/build_global_ecommerce_corroboration.py
```

To refresh the raw issuer archive and acquisition manifest, run:

```bash
python3 scripts/acquisition/acquire_global_ecommerce_sources.py
```

The analysis script contains reviewed manual transcriptions with source URLs,
local file paths, and locators. It validates row count, positive paired values,
unit consistency, and issuer-year uniqueness before producing outputs.

## Interpretation rules

1. Compare growth primarily within the same issuer and revenue definition.
2. Exclude flagged perimeter breaks from the clean-transition summary.
3. Do not add annual transitions, matched levels, publication vintages, or
   source documents into one sample count.
4. Do not convert or add issuer values across currencies. The chart indexes
   each issuer to its own first retained year.
5. The ecosystem ratio is exactly `1 / take_rate - 1`; it is a descriptive
   transformation, not an independent outcome or prior-literature metric.
6. Cross-issuer differences can reflect returns, taxes, shipping, first-party
   sales, subscriptions, advertising, travel, B2B services, and principal-agent
   accounting. The definition map is therefore part of the result.

## Source boundary

Raw downloaded files under `sources/global_ecommerce/raw/` are ignored by Git
because of their size, while
`sources/global_ecommerce/global_issuer_document_manifest.csv` records URLs,
status, byte counts, and hashes. Selected public documents can later be promoted
to the tracked core-source layer if needed for the advisor package.

