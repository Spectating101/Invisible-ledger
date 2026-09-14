# Proposal integration: longitudinal design and Indonesian e-commerce tax context

**Status:** proposal-ready source and wording note. It does not alter the empirical admission rules or claim that the legal tax mechanism has produced measurable effects.

## 1. The study is not an FY2023-only design

FY2023 remains useful as the cleanest common cross-platform snapshot and as the year for which a detailed Indonesian marketplace-share denominator is available. It is not the full empirical period.

The retained research base contains the following distinct longitudinal modules:

| Module | Coverage | Retained scale | Intended role |
|---|---|---:|---|
| Direct Indonesian issuer candidates | FY2019–FY2025 | 13 period-matched platform/segment-years; 12 have positive revenue denominators | Candidate longitudinal core, subject to geography and business-scope admission |
| Conditional Indonesian country reconstructions | FY2021–FY2024 | 6 Grab/Shopee platform-years | Sensitivity evidence, not equivalent to direct issuer observations |
| Indonesia marketplace structure | 2022–2025 | 22 platform-year snapshot rows | Market coverage, competition, and structural-break context |
| BPS official e-commerce evidence | 2020–2024 | National indicators plus 74 complete province-years for 2023–2024 | Activity, business participation, sales channels, and recordkeeping |
| ASEAN corroboration | 2019–2025 | 42 latest-vintage country-years across six countries, from 450 source-vintage metric rows | Separate-country robustness and measurement-revision analysis |
| Global issuer corroboration | Multi-year issuer histories | 48 matched issuer-years across eight businesses and 40 annual transitions | Business-model corroboration outside the Indonesian sample |
| Historical quarterly accounting | 2017–2022 coverage varies by issuer | 47 company/segment-quarter observations | Historical accounting and disclosure evidence, not an Indonesia panel |

The current candidate census therefore does not consist of three rows. The earlier three-case FY2023 file is one historical cross-sectional construction. The longitudinal design starts with Blibli/GDN FY2019–FY2025, Bukalapak FY2020–FY2023, Tokopedia FY2022–FY2023, conditional Grab Indonesia FY2021–FY2023, and conditional Shopee Indonesia FY2022–FY2024. Tokopedia FY2021 and Bukalapak FY2024 remain excluded because their transaction and revenue periods do not match.

These counts describe different empirical universes and must not be summed into one artificial sample size. The proposal should identify the unit of observation separately for every module.

## 2. Proposal-ready data wording

> The study adopts a longitudinal, multi-layer design rather than relying on a single fiscal-year cross-section. The candidate issuer evidence spans FY2019–FY2025 and includes directly reported transaction and revenue pairs, together with separately labelled country reconstructions used only for sensitivity analysis. Official BPS evidence provides national e-commerce indicators through 2024 and repeated province observations for 2023–2024. ASEAN country histories and global issuer histories are retained as distinct corroborating modules; they are not pooled with the Indonesian observations because geographic, regulatory, and business-model definitions differ. FY2023 is used only where it provides the cleanest common market-structure benchmark, not as the sole period of analysis.

## 3. Indonesian e-commerce tax context

### What the official material establishes

Indonesia's Ministry of Finance issued PMK 37/2025 to provide a framework under which designated electronic marketplaces withhold, deposit, and report Article 22 income tax relating to income received by domestic marketplace sellers.^1 The Directorate General of Taxes explains that covered sellers provide identifiers such as an NPWP or NIK and that the withholding base is transaction-linked merchant gross turnover recorded in invoices, rather than the marketplace operator's corporate revenue.^2

The rate is 0.5% of invoice gross turnover excluding VAT and luxury-goods sales tax, subject to the regulation's taxpayer treatment and exclusions.^2 Individual taxpayers can declare that their annual gross turnover has not exceeded Rp500 million and thereby remain outside marketplace withholding under the specified conditions.^2

DJP designated Blibli, Shopee Indonesia, Tokopedia, and Lazada on 1 July 2026.^3 DJP subsequently postponed application through 31 October 2026, cancelled the initial appointment decisions pending reappointment, and directed that amounts already withheld be returned.^4 The policy therefore establishes a legal reporting architecture but, as of 11 September 2026, does not provide a completed post-implementation period from which to estimate a compliance effect.

### What it does not establish

The official DJP description expressly characterizes PMK 37/2025 as a change in collection mechanism rather than the creation of a new tax.^3 Consequently, the regulation cannot be cited as proof that online merchants previously evaded tax or systematically paid too little.

Statements attributed to Finance Minister Purbaya Yudhi Sadewa should be treated as political and implementation context, not empirical evidence. A January 2026 report records him saying that Article 22 marketplace collection would depend on economic conditions; a separate June report discussed VAT obligations and should not be conflated with the Article 22 mechanism in PMK 37/2025. The official August announcement then postponed the Article 22 mechanism to protect purchasing power.^5 These statements document policy timing and concern. They are not an empirical estimate of merchant underpayment.

## 4. Proposal-ready tax wording

> Indonesia's marketplace-tax architecture illustrates why platform transaction records have an administrative function distinct from public company revenue. PMK 37/2025 provides for designated marketplaces to identify covered domestic sellers and withhold and report Article 22 income tax using transaction-linked merchant turnover. The measure is officially described as a change in collection mechanism rather than a new tax, and its implementation was postponed through 31 October 2026. The policy therefore motivates the study's distinction between platform transaction records, corporate revenue, merchant turnover, and tax administration; it does not by itself establish past underpayment or permit the transaction–revenue difference to be interpreted as unpaid tax.

## 5. Literature bridge

The tax discussion should connect the Indonesian institution to established research on verifiable transaction records rather than claim that the thesis measures tax evasion.

- Kleven et al. (2011) find far lower evasion for income subject to third-party reporting than for self-reported income in Danish audit data.^6 This supports the general importance of third-party information; it does not establish the magnitude of Indonesian marketplace compliance.
- Pomeranz (2015) shows through randomized enforcement experiments involving more than 400,000 Chilean firms that VAT paper trails can create preventive deterrence and enforcement spillovers.^7 This supports the importance of transaction-linked information chains.
- Slemrod (2019) reviews information reporting and remittance regimes as major tax-enforcement instruments.^8
- The OECD's 2020 Model Rules require covered platform operators to collect seller and consideration information and report it to tax authorities. The framework explicitly treats seller information as distinct from platform corporate accounts.^9

Together, these sources justify the proposition that platform records can improve administrative observability. They do not transform the present issuer and BPS datasets into a causal tax-compliance study.

## 6. Appropriate research inference

The defensible chain is:

```text
platforms record transactions and seller identities
                  |
                  v
public issuer revenue captures a different accounting perimeter
                  |
                  v
PMK 37/2025 creates a legal seller-turnover reporting bridge
                  |
                  v
therefore transaction, corporate-revenue, merchant, and tax records
must be distinguished and their linkages investigated
```

It is not:

```text
transaction value - platform revenue = merchant tax evasion
```

## Sources

1. Ministry of Finance of Indonesia. [PMK 37 Tahun 2025](https://www.jdih.kemenkeu.go.id/dok/pmk-37-tahun-2025/files). Issued 11 June 2025.
2. Directorate General of Taxes. [Pemungutan PPh oleh Marketplace](https://pajak.go.id/marketplace). Accessed 11 September 2026.
3. Directorate General of Taxes. [Pemerintah Implementasi PMK 37/2025 Melalui Penunjukan Empat Marketplace Sebagai Pemungut PPh](https://pajak.go.id/id/siaran-pers/pemerintah-implementasi-pmk-372025-melalui-penunjukan-empat-marketplace-sebagai). 1 July 2026.
4. Directorate General of Taxes. [Penundaan Waktu Pemberlakuan Ketentuan Pemungutan PPh Pasal 22 oleh Marketplace](https://pajak.go.id/index.php/id/pengumuman/penundaan-waktu-pemberlakuan-ketentuan-pemungutan-pph-pasal-22-oleh-marketplace). 5 August 2026.
5. ANTARA. [Purbaya belum berencana terapkan pajak marketplace](https://www.antaranews.com/berita/5380386/purbaya-belum-berencana-terapkan-pajak-marketplace). 27 January 2026; ANTARA. [Purbaya beri sinyal pedagang marketplace bakal bayar PPN mulai Juli](https://m.antaranews.com/amp/berita/5628029/purbaya-beri-sinyal-pedagang-marketplace-bakal-bayar-ppn-mulai-juli). 29 June 2026; Directorate General of Taxes. [Penundaan Waktu Pemberlakuan Ketentuan Pemungutan PPh Pasal 22 oleh Marketplace](https://pajak.go.id/index.php/id/pengumuman/penundaan-waktu-pemberlakuan-ketentuan-pemungutan-pph-pasal-22-oleh-marketplace). 5 August 2026.
6. Kleven, H. J., Knudsen, M. B., Kreiner, C. T., Pedersen, S., and Saez, E. [“Unwilling or Unable to Cheat? Evidence from a Tax Audit Experiment in Denmark.”](https://doi.org/10.3982/ECTA9113) *Econometrica* 79(3), 2011, 651–692.
7. Pomeranz, D. [“No Taxation without Information: Deterrence and Self-Enforcement in the Value Added Tax.”](https://doi.org/10.1257/aer.20130393) *American Economic Review* 105(8), 2015, 2539–2569.
8. Slemrod, J. [“Tax Compliance and Enforcement.”](https://doi.org/10.1257/jel.20181437) *Journal of Economic Literature* 57(4), 2019, 904–954.
9. OECD. [*Model Rules for Reporting by Platform Operators with respect to Sellers in the Sharing and Gig Economy*](https://doi.org/10.1787/d7973047-en). OECD Publishing, 2020.
