# Tax context and market-coverage integration

**Status:** proposal/manuscript structure note based on sources verified through 11 September 2026. This note does not change the main-sample admission decision and does not treat a tax rule as evidence of past underpayment.

## Bottom line

The tax material strengthens the institutional motivation for *Invisible Ledger*: Indonesia has created a mechanism that uses marketplace transaction records and seller identities to collect and report merchant income tax. This demonstrates that merchant turnover and platform corporate revenue are different information objects and that marketplace records can serve an administrative role.

It does **not** demonstrate that e-commerce merchants previously failed to pay enough tax. The government explicitly describes PMK 37/2025 as a change in collection mechanism rather than a new tax. The defensible inference is that the government considers platform-mediated withholding and reporting useful for simpler administration, compliance, legal certainty, and parity between online and offline sellers.

The market-share evidence also adds a useful denominator. In the 2023 Momentum Works estimates reported by Katadata:

- Shopee and Tokopedia together account for **70%** of Indonesian platform e-commerce GMV;
- adding Blibli raises the share associated with current issuer evidence to **74%**, although Blibli remains scope-pending and Shopee remains a conditional country reconstruction;
- the four marketplaces designated by DJP in July 2026—Blibli, Shopee, Tokopedia, and Lazada—account for **83%** of the same 2023 market estimate;
- the five named leaders account for **94%**, leaving a rounded residual of 6%.

These percentages are market-coverage descriptions, not sampling probabilities or proof that the analytical dataset captures the same percentage of issuer revenue, merchants, tax liabilities, or total Indonesian digital commerce.

## Where this fits in the research design

```text
INDONESIAN DIGITAL COMMERCE
          |
          +----------------------+----------------------+---------------------+
          |                      |                      |
          v                      v                      v
 platform market/activity   issuer accounting     merchant tax obligation
 GMV, shares, transactions  revenue, incentives   seller turnover and identity
          |                      |                      |
          |                      |                      v
          |                      |             PMK 37/2025 mechanism
          |                      |             marketplace withholds/reports
          |                      |                      |
          +----------------------+----------------------+
                                 |
                                 v
                    INVISIBLE LEDGER QUESTION
       What can each record reveal, and what cannot be inferred
          until transaction, seller, accounting, and tax records
                       are actually linked?
```

The tax section is therefore not a separate tax-gap analysis. It supplies the institutional reason that the difference between a platform's transaction ledger and its corporate accounts matters: the seller-side record can contain information useful to tax administration even though it is not the platform's own revenue.

## Verified Indonesian tax architecture

### Existing obligation versus new mechanism

PMK 37/2025 provides for designated electronic marketplaces to withhold, deposit, and report Article 22 income tax on income received by domestic merchants through electronic commerce. The rate is 0.5% of gross turnover shown in the transaction document, excluding VAT and luxury-goods sales tax.

The official DJP explanation makes two boundaries explicit:

1. this is **not a new category of tax**; merchants were already subject to applicable income-tax obligations;
2. the policy changes the collection route from merchant self-payment to withholding through a designated marketplace.

Individual taxpayers with annual gross turnover up to Rp500 million are excluded from marketplace withholding when the required declaration is provided. Other exclusions and credit/final-tax treatment must be described from the regulation rather than inferred from the platform dataset.

### Implementation chronology

| Date | Event | What it establishes |
|---|---|---|
| 11 June 2025 | PMK 37/2025 issued | Legal framework for marketplace withholding and reporting |
| 1 July 2026 | DJP designated Blibli, Shopee Indonesia, Tokopedia, and Lazada | Named marketplaces received a formal administrative role |
| 5 August 2026 | DJP announced postponement through 31 October 2026 | As of this note, the framework cannot be treated as a completed post-policy intervention |

This chronology supports an institutional-design discussion. It does not currently support a before/after compliance estimate.

### Visibility created by the rule

The official marketplace guidance requires domestic sellers to provide an NPWP or NIK and correspondence address. The 0.5% withholding base is seller gross turnover recorded in invoices, not the marketplace operator's corporate revenue. This is direct institutional support for the paper's ledger distinction:

```text
platform corporate revenue != merchant gross turnover != merchant taxable profit
```

The first inequality is observable from the rule and issuer accounts. The second follows from ordinary tax/accounting structure because taxable income may require costs, exemptions, credits, and taxpayer status. None of these quantities should be inferred from `transaction value - platform revenue`.

## What the market-share calculation actually says

### 2023 marketplace structure

| Platform | Estimated 2023 share | Estimated GMV | Role in the research |
|---|---:|---:|---|
| Shopee | 40% | US$21.52bn | Conditional Indonesia construction; tax-designated in 2026 |
| Tokopedia | 30% | US$16.14bn | Direct issuer segment evidence; tax-designated in 2026 |
| TikTok Shop | 11% | US$5.92bn | Market context only; separate platform in 2023 |
| Lazada | 9% | US$4.84bn | Market/tax context; no matched issuer series in the current module |
| Blibli | 4% | US$2.15bn | Direct but scope-pending issuer evidence; tax-designated in 2026 |
| Other | 6% | US$3.23bn | Rounded residual |

The estimated total market is US$53.8 billion. Shares are rounded and originate in a commercial market estimate reported by Katadata, not an official census.

### Coverage statements that are safe to use

**Original FY2023 e-commerce cases:**

> Shopee and Tokopedia represented an estimated 70% of Indonesian platform e-commerce GMV in 2023 according to Momentum Works data reported by Katadata. This indicates substantial marketplace coverage, but the two observations have different evidence strength: Tokopedia's analytical pair is issuer-reported at segment level, whereas Shopee's Indonesia quantities remain partly constructed.

**Expanded issuer evidence:**

> The platforms for which the project currently holds 2023 e-commerce issuer evidence—Shopee, Tokopedia, and Blibli—correspond to approximately 74% of the same market estimate. This is a coverage diagnostic, not a claim that all three series are equally direct or already admitted to one main sample.

**Tax-policy reach:**

> The four marketplaces designated by DJP in July 2026 correspond to approximately 83% of estimated 2023 platform e-commerce GMV. This comparison suggests that the initial administrative design targeted large marketplaces, but it combines a 2026 designation with a 2023 market-share benchmark and should be labelled as contextual rather than contemporaneous coverage.

### Coverage statements that must not be used

- “The thesis covers 83% or 90% of Indonesia's digital economy.”
- “Grab, Shopee, and Tokopedia cover 70% of e-commerce.” Grab is not included in the referenced marketplace-share denominator.
- “The sample is representative because it covers most GMV.” High value coverage does not establish representativeness of merchants, sectors, regions, or tax behavior.
- “DJP selected the platforms because their merchants were underpaying.” The official rationale is administration, compliance, certainty, and parity; the designation is not a finding of merchant underpayment.
- “The remaining 6% is unrecorded.” It is merely the rounded market share outside the five named platforms.

## Proposal integration

The proposal should add the tax and coverage material in four small, deliberate locations.

### 1. Motivation

Use the policy development to explain why platform records matter:

> Indonesia's marketplace-withholding architecture illustrates the institutional importance of distinguishing platform revenue from seller-side transaction records. PMK 37/2025 assigns designated marketplaces a role in identifying domestic sellers and withholding and reporting tax on merchant turnover. The regulation does not create a new tax or prove prior non-compliance; it demonstrates that platform transaction records can serve an administrative function not performed by public issuer revenue.

### 2. Institutional setting

Explain the tax base, seller identifiers, threshold, designated platforms, and implementation chronology. Keep the August 2026 postponement visible so the proposal does not imply that an effect has already been measured.

### 3. Data and sample coverage

Add one table containing the 2023 platform shares and mark each platform as included, conditional, scope-pending, or unavailable. State the 70%, 74%, and 83% figures only beside their exact definitions.

### 4. Limitations and future test

State that the current evidence establishes a legal reporting bridge but not its operating quality or compliance effect. A future post-implementation design could examine collections, filing, or reporting outcomes once implementation dates and outcome data support it.

## Literature bridge

Three literature layers are sufficient; the proposal does not need a long generic tax review.

1. **Third-party information and enforcement.** Kleven et al. (2011), Pomeranz (2015), and Slemrod (2019) explain why verifiable third-party records can affect compliance and enforcement.
2. **Digital-platform seller reporting.** The OECD (2020) Model Rules provide an international reference for platform collection of seller identity and consideration information and reporting to tax authorities.
3. **Indonesia's institutional application.** PMK 37/2025 and DJP's 2026 designation/postponement documents show the domestic mechanism and its current status.

The literature supports the proposition that third-party information can be administratively useful. It does not convert the present descriptive dataset into evidence of Indonesian merchant underpayment.

## Recommended contribution language

> This study does not estimate unpaid tax. It documents why platform transaction records, issuer revenue, merchant turnover, and public statistics must be treated as separate ledgers. Indonesia's marketplace-withholding framework provides institutional evidence that seller-level platform records can be used for reporting and collection even though those records are not visible in platform corporate revenue. The empirical analysis then measures how conclusions about digital-commercial scale and growth change across the available ledgers.

## Source map

- Directorate General of Taxes, PMK 37/2025 implementation and four designated marketplaces: <https://pajak.go.id/id/siaran-pers/pemerintah-implementasi-pmk-372025-melalui-penunjukan-empat-marketplace-sebagai>
- Directorate General of Taxes, marketplace withholding guidance, seller identifiers, threshold, base, and rate: <https://pajak.go.id/marketplace>
- Directorate General of Taxes, postponement announcement: <https://www.pajak.go.id/id/pengumuman/penundaan-waktu-pemberlakuan-ketentuan-pemungutan-pph-pasal-22-oleh-marketplace>
- Ministry of Finance, PMK 37/2025: <https://jdih.kemenkeu.go.id/dok/pmk-37-tahun-2025/files>
- OECD, Model Rules for Reporting by Platform Operators: <https://doi.org/10.1787/d7973047-en>
- Katadata report of Momentum Works 2023 Indonesian platform GMV estimates: <https://databoks.katadata.co.id/teknologi-telekomunikasi/statistik/678272b342544/tak-ada-bukalapak-ini-5-e-commerce-ri-dengan-gmv-terbesar>

The machine-readable market-share rows are stored in `data/institutional/indonesia_marketplace_gmv_coverage_2023.csv`. The existing tax chronology is stored in `data/institutional/indonesia_marketplace_reporting_architecture_2025_2026.csv`.
