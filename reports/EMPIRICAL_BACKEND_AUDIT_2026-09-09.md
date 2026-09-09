# Invisible Ledger empirical backend audit

**Status:** Working research backend; no expanded main sample is yet advisor-approved.  
**Date:** 9 September 2026  
**Purpose:** Establish what evidence actually exists, what it can support, and what must remain separate before the next manuscript revision.

## Executive conclusion

The project is no longer accurately described as a three-row empirical exercise. It now contains several source-auditable empirical modules: 9 proposed Indonesia platform-years, 14 direct Indonesia-aligned annual issuer/segment pairs (one has a negative revenue denominator), 47 source-reconciled company/segment quarters, 74 usable BPS province-years for 2023–2024, official national e-commerce indicators through 2024, and 22,393 security-day records in the market layer.

Those counts **cannot be added into one N**. They have different units, scopes, periods, and purposes. The academically defensible advance is therefore not a giant pooled dataset. It is a deeper, modular Indonesia measurement design with separate longitudinal, issuer-accounting, official-statistics, and exploratory market evidence.

The strongest affirmative finding is broader than the original platform residual. Official BPS estimates show Indonesia e-commerce transaction value rising from Rp783 trillion in 2022 to Rp1,100.87 trillion in 2023 and Rp1,288.93 trillion in 2024, while estimated e-commerce businesses rose from 2.996 million to 3.817 million and then 4.401 million. Yet only 15.19% of e-commerce businesses reported owning financial reports in 2023 and 17.15% in 2024. This is evidence of a rapidly expanding digital transaction environment with uneven formal recordkeeping. It is **not** proof that the activity is absent from GDP, unreported for tax, or untaxed.

## What is actually available

| Empirical module | Usable coverage | Unit of observation | Proper role |
|---|---:|---|---|
| Conditional Indonesia reconstruction | 9 records, FY2021–FY2024, unbalanced | platform-year | Preserves Grab/Tokopedia/Shopee design; Grab and Shopee remain model-dependent |
| Indonesia-aligned direct annual issuer/segment evidence | 14 matched periods, FY2019–FY2025, unbalanced | platform/segment-year | Candidate longitudinal core if Kong accepts Indonesia-aligned rather than strict country-labelled scope |
| Quarterly issuer accounting panel | 47 quarters: Grab 17, GoTo 16, Sea 14 | company/segment-quarter | Longitudinal accounting and disclosure evidence; not Indonesia-only |
| BPS province evidence | 74 complete province-years across 2023–2024 | province-year | Official repeated cross-sections on channels and financial-report ownership |
| BPS national indicators | available observations from 2020–2024 | national indicator-year | Scale, channel composition, and formal-recordkeeping context |
| Market data | 22,393 security-days across 9 symbols | security-day | Event-study input; results remain exploratory while contamination classifications are unresolved |
| ASEAN/World Bank context | 2,860 country-year-indicator slots, 2,617 numeric | country-year-indicator | Context and robustness only; not platform-accounting observations |

The repository profiles 78 data/source files and 35,972 CSV rows. That is a source-layer inventory, not the analytical sample size.

## Candidate main-design choices

1. **Strict explicit-country direct pairs:** currently zero complete issuer-disclosed Indonesia transaction/revenue pairs. This standard is clean but infeasible with present public issuer reporting.
2. **Indonesia-aligned direct issuer/segment annual panel:** 14 matched annual periods across Blibli, Bukalapak, and Tokopedia. This is the strongest route for direct reported pairs, but Blibli 3P includes online travel, Bukalapak reports group activity with overseas operations, and Tokopedia ends with deconsolidation.
3. **Conditional Indonesia reconstruction:** 9 platform-years across Grab, Tokopedia, and Shopee. It preserves the existing thesis architecture, but Grab and Shopee country quantities remain constructed.
4. **Quarterly company/segment panel:** 47 source-reconciled quarters. This is substantially deeper longitudinal evidence, but it changes the geographic unit to listed platforms serving Indonesia.
5. **Official BPS business-statistics module:** 74 complete province-years plus national indicators. This directly observes business channel use and financial-report ownership, but province analysis is ecological and microdata would be required for business-level inference.

Kong must approve which boundary defines the main sample. The evidence can inform that choice; packaging cannot make the choice on her behalf.

## Empirical findings that survive the audit

### 1. Digital transaction scale is rising faster than formal-recordkeeping prevalence

BPS reports transaction value growth of about 40.6% from 2022 to 2023 and 17.1% from 2023 to 2024. Estimated e-commerce business counts rose about 27.4% and 15.3% over the same intervals. Financial-report ownership fell from 23.45% in 2020 and 22.06% in 2021 to 15.19% in 2023, then recovered only partly to 17.15% in 2024.

This supports a measurement-and-information problem: large and growing digital commerce coexists with limited business-level financial records. It does not establish the size of GDP omission or a tax gap.

### 2. Marketplace activity is only one part of the digital transaction environment

In 2023, the exclusive BPS decomposition attributes Rp200.68 trillion (18.23%) of e-commerce transaction value to marketplaces and Rp900.19 trillion (81.77%) to non-marketplace channels. In 2024, BPS reports marketplaces at about 15.79% of total value. Separately, multiple-response channel measures show very high instant-messaging use. These definitions must not be mixed, but both show why issuer/platform accounts alone cannot represent all digital commerce.

### 3. The province association is not stable enough to become a causal headline

Across reported provinces, marketplace use and financial-report ownership have Pearson correlation 0.263 in 2023 (p=0.121) and 0.022 in 2024 (p=0.897). Weighting provinces by estimated e-commerce business counts yields correlations of 0.490 and 0.314, respectively. Within 36 matched provinces, the association between the 2023–2024 changes is 0.309 (p=0.066) unweighted and 0.099 weighted.

Therefore, the data do not justify a stable causal claim that marketplace use formalizes businesses. They do justify further business-level investigation and show that conclusions depend on year and weighting.

### 4. Platform monetization and reporting scope vary materially over time

The 47-quarter accounting panel contains 17 Grab, 16 GoTo, and 14 Sea observations. Median gap-to-revenue ratios are approximately 6.39, 36.99, and 7.25, respectively. These are descriptive company/segment results, not 47 independent firms and not Indonesia-only estimates. Structural breaks—especially revenue-model changes and Tokopedia deconsolidation—must remain explicit.

### 5. The platform residual remains a measurement construct

For any matched transaction value \(V\) and platform-recognized revenue \(R\), the gap ratio is \((V-R)/R=V/R-1\). When a country transaction value is derived from an assumed monetization rate, the ratio is mechanically implied by that assumption. Its role is to make the accounting boundary visible; it is not an independently estimated tax or GDP parameter.

## Corrections and rejected false expansions

- The legacy Blibli 1Q23 extraction shifted the FY22, 1Q23, and 1Q22 columns. The official issuer PDF was recovered and a corrected extract created. Legacy rows remain preserved but excluded.
- The YZUC/Refinitiv object registered as a 227-row annual panel is an FY0 cross-sectional snapshot with all `fiscal_year` values missing. It contributes zero longitudinal observations.
- Bukalapak FY2024 is excluded because its TPV covers nine months while the revenue denominator covers twelve.
- Report vintages, annual totals, component segments, cumulative periods, quarters, sensitivity scenarios, and source input rows are never added as independent observations.
- BPS 2023 contains an internal count discrepancy: an executive-summary passage reports 3,934,981 while the body/figure reports 3,816,750. The latter is currently used because it reconciles to the displayed 2022 count and 27.40% growth; both values remain flagged.
- The market layer is not a closed investor-result module while event contamination classifications remain unresolved.

## Source and reproducibility chain

The intended chain is:

> original issuer or BPS document → exact source extract → observation census → module-specific calculation → table/figure.

The complete observation census is `outputs/empirical_backend_2026-09-09/candidate_observation_census.csv`. It preserves directness, geography, period matching, accounting scope, reporting vintage, admission status, and source location. The audit script is `scripts/analysis/build_comprehensive_empirical_audit.py`; the executed notebook is `notebooks/empirical_backend_audit_2026_09_09.executed.ipynb`.

## Recommended research architecture

The evidence best supports an Indonesia-first, multi-layer measurement thesis:

1. Use a multi-year Indonesia-aligned issuer/segment series as the longitudinal platform layer, conditional on Kong accepting its geographic rule.
2. Retain Grab and Shopee country reconstructions as explicitly conditional cases or sensitivity evidence, not as equivalent to direct disclosures.
3. Add BPS national and province evidence as an independent official-statistics layer showing scale, channel composition, and financial-recordkeeping coverage.
4. Use the 47-quarter company panel to analyze reporting definitions and structural breaks, without relabelling it Indonesia-only.
5. Keep ASEAN comparisons and the market/event study separate unless their own source and design problems are fully resolved.

This preserves the original ambition—modern digital activity can outrun familiar company-based measurement interfaces—while replacing the unsupported leap that the transaction/revenue residual directly measures missing GDP or unpaid tax.

## Remaining work before manuscript revision

- Obtain Kong's approval of the main geographic and business-scope rule.
- Decide whether the direct Indonesia-aligned annual panel or the conditional Grab/Tokopedia/Shopee series is the main longitudinal object.
- If business-level inference is required, obtain licensed BPS microdata under its data-use agreement; do not infer enterprise behavior from province correlations.
- Complete accounting-definition reconciliations for the admitted platform series.
- Close event contamination and timing decisions before presenting investor-response results as established.
- Rebuild paper tables only after the sample rule is approved.

## Primary sources added in this audit

- [BPS E-Commerce Statistics 2023](https://www.bps.go.id/en/publication/2025/01/30/d52af11843aee401403ecfa6/statistik-e-commerce-2023.html)
- [BPS E-Commerce Statistics 2024](https://www.bps.go.id/en/publication/2025/11/28/647323224ecc656c2933571b/ecommerce-statistics-2024.html)
- [BPS marketplace analytical publication](https://www.bps.go.id/en/publication/2025/09/30/3bc481a585782813cc894636/cerita-data-statistik-untuk-indonesia---menimbang-manfaat-dan-risiko-penggunaan-marketplace-dalam-e-commerce-di-indonesia.html)
- [BPS 2024 microdata catalogue](https://silastik.bps.go.id/v3/index.php/mikrodata/detail/ODdXeUNNcW5vcVVGVWhTUERuTGNTQT09)
- [Blibli 1Q23 issuer release](https://asset-about.blibli.com/2023/05/Earnings-Release-1Q23-PT-Global-Digital-Niaga-Tbk.pdf)

