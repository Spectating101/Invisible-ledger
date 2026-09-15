# The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy

**Christopher Ongko (王新福)** · Yuan Ze University, MS Finance · Advisor: Prof. De-Rong Kong (孔德蓉)

*Sample boundary: **direct_plus_scope_pending**. Regenerate with a different boundary to follow the committee's ruling.*

---

## 1. Introduction

Southeast Asia's digital economy grew from US$100 billion in gross transaction value in 2020 to US$263 billion in 2024 (Google, Temasek and Bain 2020, 2024; reported there as gross merchandise value). The figures used to describe that growth come from three kinds of record: platform accounts, which report what platforms earn; e-commerce and marketplace statistics, which report sales through particular channels; and payment statistics, which report the value moving through digital payment systems. They are commonly used as interchangeable measures of the same activity. This thesis argues that they are not interchangeable, and that treating them as such produces systematically wrong measurement of platform economies.

Suppose a platform processes 100 units of transaction value and recognises 10 as revenue. The other 90 units are recorded in the platform's systems as merchant receipts, driver payouts, inventory costs and other pass-through payments, and never appear as platform revenue. An analyst sizing the platform from its accounts sees 10; an analyst sizing it from its transaction data sees 100. I call the difference the **invisible wedge**, and I measure it relative to platform revenue with the **Ecosystem Ratio**, a measure constructed for this study.

In Indonesia the gap is both large and unstable. In FY2023, three documented platform cases processed US$43.23 billion of transaction value against US$3.16 billion of recognised revenue, a ratio of 13.7 to 1 and a wedge of US$40.07 billion, equivalent to 2.9 percent of GDP. Within platform series, revenue grew faster than transaction value in 10 of 12 annual transitions, so platform revenue overstates the growth of the commerce it comes from while understating its level. National statistics place 98.5 percent of Indonesia's 2023-2024 e-commerce growth outside the marketplace channel that platform accounts describe, and digital payment value grew up to 11 times as fast as e-commerce value over the same year.

The wedge is invisible in a specific sense. Platforms hold detailed, seller-linked records of the full transaction value, but only the revenue share reaches their financial statements, and the transaction records themselves do not routinely enter third-party income reporting. Indonesia's Regulation PMK 37/2025 is the first attempt to route those records to the tax authority, and Section 7.3 shows how small a part of the activity its design can reach.

**Research question.** *How large is the gap between the commerce Indonesian platforms carry and the revenue their accounts record, how does it move over time, and what does it imply for how the digital economy is measured?*

### 1.1 Hypotheses

|  | Hypothesis | Status in the evidence assembled here |
|---|---|---|
| H1 | Platform revenue is not a stable proxy for platform commerce: the ratio of transaction value to revenue moves materially within the same platform over time. | Supported. Revenue outgrows transaction value in 10 of 12 within-series transitions; median divergence 42.02 pp. Survives log growth (36.64), removal of the largest transition (29.34 pp) and exclusion of any single series. |
| H2 | Indonesian e-commerce growth is driven by the entry of new businesses rather than by higher value per business. | Supported. The business-count term accounts for 90.29% of the 2023-2024 increase in e-commerce value, and 70.95% under the conflicting BPS business count. |
| H3 | Marketplace participation is associated with financial recordkeeping. | Supported in BPS business-level evidence. The within-province change is weaker (r = 0.309, p = 0.066) and is tested further in this thesis. |
| H4 | Platform revenue, marketplace statistics and payment data are not interchangeable measures of digital commerce, and substituting one for another misstates its scale and location. | Supported. FY2023 transaction value is 13.7 times revenue; 98.46% of 2023-2024 e-commerce growth falls outside the marketplace channel; payment value grew 1.8-11 times as fast as e-commerce value. |

H4 is the central claim of the thesis, and H1 to H3 establish the mechanisms behind it. Whether platform records become administratively usable once PMK 37/2025 takes effect on 1 November 2026 depends on post-implementation evidence; Section 7.3 addresses it through the design of the regime.

## 2. Literature and Conceptual Framework

### 2.1 Platform economics and revenue recognition

Multisided-platform theory explains why a platform's revenue need not track the transaction value it coordinates (Rochet and Tirole 2003; Caillaud and Jullien 2003; Parker and Van Alstyne 2005; Armstrong 2006; Hagiu and Wright 2015; Evans and Schmalensee 2016). Accounting determines how much of that value becomes revenue: principal-agent treatment under IFRS 15 (International Accounting Standards Board 2014), customer incentives, service mix, acquisitions and reporting perimeter all move revenue independently of the underlying commerce. De Franco, Kothari and Verdi (2011) show why comparable accounting bases matter when users interpret such movements. What this literature has not done is measure how large and how unstable the resulting gap is within a single economy over time.

### 2.2 Informality, digital records and third-party information

Platform participants occupy an unusual position: their transactions are priced, recorded and settled through a formal intermediary while the participants themselves may be self-employed, unregistered or below filing thresholds. That places the invisible wedge outside the shadow-economy framework of the informality literature (La Porta and Shleifer 2014; Ulyssea 2018; Medina and Schneider 2019), because the activity is fully recorded; it is simply recorded somewhere other than where it is measured. Such digital records carry economic information even where conventional records are thin (Berg et al. 2020), and platform-mediated work leaves observable financial and administrative traces (Barrios, Hochberg and Yi 2022; Denes, Lagaras and Tsoutsoura 2025).

A central public-finance result is that third-party information materially changes compliance and enforcement (Kleven et al. 2011; Pomeranz 2015; Naritomi 2019; Kleven, Kreiner and Saez 2016; Slemrod 2019). The OECD Model Rules and the European Union's DAC7 regime put that result into practice for platforms, and Indonesia's PMK 37/2025 applies the same logic through seller identification, transaction-linked reporting and marketplace withholding.

### 2.3 Measuring the digital economy

Digital-economy measurement frameworks recognise the same boundary from the national-accounting side. Official guidance separates the buyer-seller transaction from the intermediation service the platform provides, and treats only the service as the platform's output (Ahmad and Schreyer 2016; International Monetary Fund 2018; OECD 2023; United Nations et al. 2025). The frameworks are clear in principle, yet the indicators most often quoted for the digital economy, gross merchandise value, platform revenue and payment volume, each sit on a different side of that line. This thesis takes the frameworks' distinction seriously and measures what happens when those indicators are set against one another.

### 2.4 Research gap

The literature explains why transaction value can exceed platform revenue and why accounting moves the two apart. It has not measured the gap longitudinally for one economy, traced its movements to disclosed components, or tested how far the standard indicators of digital commerce depart from one another, and this thesis does all three for Indonesia.

### 2.5 Framework and key variables

Let *V* denote transaction value and *R* platform-recognised revenue on a matched scope and period:

> **W = V − R**   ·   **E = (V − R) / R**   ·   **D = g(V) − g(R)**

*W* is the absolute wedge; *E*, the Ecosystem Ratio, measures the wedge per unit of platform revenue; and *D* is the annual growth divergence. A negative *D* means platform revenue is growing faster than the commerce behind it. Gross transaction value (GTV) is the common label throughout; issuers use GMV or TPV for the same quantity, and those source labels are retained in the empirical files.

## 3. Data and Empirical Design

### 3.1 Admission rules

A platform-period is eligible only when transaction value and revenue cover the same period; geography and business scope can be evaluated; units and definitions are known; derived inputs trace to source; and structural breaks or revised reporting bases are flagged. Repeated publication vintages of the same underlying period count once.

### 3.2 Evidence tiers

| Evidence tier | Series | Levels | Transitions | In this sample |
|---|---|---|---|---|
| direct Indonesia-aligned | Tokopedia e-commerce segment | 2 | 1 | yes |
| direct issuer, scope-pending | Blibli 3P Retail; Bukalapak Group | 9 | 7 | yes |
| conditional country reconstruction | Grab; Shopee | 6 | 4 | no |
| **All tiers (diagnostic)** | five series | 17 | 12 | — |

The inventory holds **17 candidate platform-year levels** across five series from FY2020 to FY2025. Under the **direct_plus_scope_pending** boundary used here, **11 levels** enter the main sample. The design manages a trade-off: only two levels come from a directly Indonesia-aligned segment, while the larger tiers carry more observations under wider scope. Tokopedia is the strongest Indonesia-aligned series; Blibli 3P Retail includes online travel; Bukalapak reports at Group scope with overseas operations; and Grab and Shopee each require a derived or externally estimated country component. Tokopedia FY2021 and Bukalapak FY2024 are excluded because their transaction and revenue periods do not match.

Three counts are reported separately because they answer different construction questions: the all-tier inventory holds 17 retained levels, the executed direct tiers hold 11, and the broader direct-candidate sensitivity holds 13 periods, including a Blibli FY2020 prospectus observation, yielding 9 annual transitions.

### 3.3 Comparability strategy

The primary longitudinal inference is within-series. Each transition holds the issuer, business perimeter and disclosure convention as constant as the filings allow, so a change in the ratio of transaction value to revenue reflects a change in that platform's economics and accounting. Cross-platform levels establish scale, and the FY2023 cross-section is read that way.

### 3.4 Conditional country constructions

Grab discloses Indonesia revenue but not Indonesia transaction value, so its country transaction value is derived as **Indonesia GTV = Indonesia revenue × Group GTV / Group revenue**, applying the Group monetisation rate to Indonesia. Shopee's Indonesian transaction value comes from Momentum Works' recurring Southeast Asian e-commerce estimates, since Sea Limited discloses no country figure, and its revenue applies Sea's disclosed Group rate of 10.0 percent to that estimate. Both are labelled as reconstructions wherever they are used, and Section 4.1 reports how far the results depend on them.

## 4. Issuer Evidence

### 4.1 The level of the wedge

| Case | V (US$bn) | R (US$bn) | W (US$bn) | E | Evidence class |
|---|---|---|---|---|---|
| Grab Indonesia | 5.381 | 0.605 | 4.776 | 7.895× | derived V |
| Tokopedia e-commerce | 16.331 | 0.405 | 15.926 | 39.296× | direct pair |
| Shopee Indonesia | 21.520 | 2.152 | 19.368 | 9.000× | derived V and R |
| **Selected platforms** | **43.233** | **3.162** | **40.070** | **12.671×** | sum of three cases |

Across the three cases, transaction value is 13.7 times recognised revenue. The ratio differs widely by platform: Tokopedia, the one direct pair, shows an Ecosystem Ratio of 39.296, Shopee 9.000 and Grab 7.895. The spread reflects where each business sits on the gross-versus-net recognition spectrum. A marketplace that books commission and advertising against third-party sales records a far smaller share of each transaction than a delivery and mobility platform, which is why the ratio is compared within a series over time and used across platforms only to establish scale.

The level is robust to the reconstructions it depends on. Tokopedia contributes 39.7 percent of the wedge, Shopee 48.3 percent and Grab 11.9 percent. Shopee's Ecosystem Ratio is fixed at 9.000 by the 10.0 percent monetisation assumption, yet varying that rate between 9 and 11 percent moves the combined wedge only between US$40.29 billion and US$39.86 billion, because a higher assumed rate raises estimated revenue and lowers the residual almost equally. Excluding any single platform leaves a wedge between US$20.70 billion and US$35.29 billion. One-at-a-time variation of every derived input keeps it between US$37.65 billion and US$42.49 billion, and Tokopedia alone, resting on no reconstruction, carries US$15.93 billion.

### 4.2 The growth of the wedge

| Admission rule | Transitions | Revenue faster | Transaction faster | Sign reversals | Median abs. divergence |
|---|---|---|---|---|---|
| all candidate tiers | 12 | 10 | 2 | 2 | 42.02 pp |
| conditional country reconstruction | 4 | 4 | 0 | 0 | 50.64 pp |
| direct indonesia aligned segment | 1 | 1 | 0 | 1 | 62.10 pp |
| direct issuer scope pending | 7 | 5 | 2 | 1 | 15.74 pp |

Platform revenue is a poor guide to the growth of the commerce behind it. Across the all-tier inventory, revenue grew faster than transaction value in 10 of 12 annual transitions, at a median absolute divergence of 42.02 percentage points; under the certified direct-candidate rule revenue grew faster in 6 of 9, at a median of 42.94 points. An indicator built on platform revenue growth would therefore have overstated the growth of Indonesian platform commerce in most of the years observed.

Every series ends the period with a lower Ecosystem Ratio than it began with, as platforms raised the share of each transaction they retain: Blibli from 128.1 to 33.3; Bukalapak from 61.9 to 36.0; Grab from 22.8 to 7.9; Shopee from 10.9 to 8.3; Tokopedia from 66.8 to 39.3.

## 5. Mechanism and Robustness

### 5.1 Reconciling a divergence: Tokopedia FY2022-FY2023

Tokopedia FY2022-FY2023 shows how the divergence arises. It is the only directly Indonesia-aligned segment pair in the inventory, and its divergence runs in the direction the aggregate result predicts: transaction value fell **8.90 percent** while third-party net segment revenue rose **53.20 percent**.

Net revenue is gross revenue less customer incentives. Of the arithmetic increase in Tokopedia's net revenue, **60.56 percent** came from lower incentives and **39.44 percent** from higher gross revenue. Most of the revenue improvement was therefore a change in how much of each transaction the platform retained, and the revenue line recorded a strong year in a year when the commerce it carried contracted.

Incentive spending is a managerial choice made in the same competitive conditions that moved transaction value, and the decomposition allocates a disclosed change across disclosed components. Tokopedia is the clearest disclosed case, and the thesis extends the decomposition to every series whose filings report the components separately.

### 5.2 Robustness of the longitudinal result

The direct-candidate baseline gives 9 adjacent annual transitions, 3 sign reversals and a median absolute growth gap of **42.94 pp**. The result survives each of the following tests.

- **Growth transformation.** Log changes rather than ordinary percentage growth give a median absolute gap of **36.64 log-points ×100**, with direction rankings and sign-reversal classification unchanged.
- **Extreme transition.** Dropping the single largest gap (Blibli FY2022→FY2023, a low starting net-revenue base with major monetisation changes) leaves 8 transitions, still 3 reversals, and a median of **29.34 pp**.
- **Leave-one-transition-out.** Across all nine exercises the median ranges from **29.34 pp to 52.52 pp**.
- **Leave-one-series-out.** Excluding Blibli leaves 4 transitions at 38.92 pp, Bukalapak 6 at 52.52 pp, and Tokopedia 8 at 29.34 pp, and every construction retains at least one sign reversal.

The divergence is a property of the evidence as a whole and survives the removal of any single observation or series. The candidate count is small, so the results are reported as robustness tests on a measured phenomenon, and the thesis extends them as further series enter the sample.

## 6. Where Indonesian E-Commerce Is Growing

### 6.1 National aggregates

| Year | Transaction value (Rp tn) | Estimated businesses | Implied value/business (Rp mn) | Marketplace (Rp tn) | Non-marketplace (Rp tn) |
|---|---|---|---|---|---|
| 2023 | 1100.87 | 3,816,750 | 288.43 | 200.68 | 900.19 |
| 2024 | 1288.93 | 4,400,972 | 292.87 | 203.58 | 1085.35 |

BPS-Statistics Indonesia reports national e-commerce transaction value rising **17.08 percent** from 2023 to 2024, estimated e-commerce businesses rising **15.31 percent**, and implied value per business rising only **1.54 percent**. Both marketplace amounts are directly published; the 2024 figure of Rp203.58 trillion reconciles to the published 15.79 percent share.

### 6.2 The marketplace channel misses the growth

The marketplace component grew **1.45 percent** while the non-marketplace component grew **20.57 percent**. The marketplace increase was Rp2.90 trillion against a total increase of Rp188.06 trillion, so **98.46 percent** of the growth took place outside the marketplace channel, and the marketplace share of e-commerce value fell from 18.2 to 15.8 percent in a single year.

This is the most consequential aggregate result in the thesis. The issuer chapters measure marketplace platforms carefully and find a large, unstable wedge inside them; the national statistics show that marketplace platforms are also where Indonesian e-commerce growth is least concentrated. Platform accounts are becoming a narrower window onto national e-commerce, and measurement anchored on them misses almost all of the recent expansion.

The result holds however the 2024 marketplace amount is derived: the directly published figure gives 98.46 percent and reconstruction from the rounded 15.79 percent share gives 98.49 percent. BPS sales-media value categories and multiple-response channel-use figures are different objects, and only the value decomposition is used here.

### 6.3 Entry drives the growth

Decomposing *V = N × A* symmetrically into a business-count term and a value-per-business term allocates the change exactly. Entry of new businesses dominates: the count term accounts for **70.98 percent** of the 2022→2023 increase, **90.29 percent** of 2023→2024 and **76.95 percent** over 2022→2024. Substituting the conflicting 2023 count of 3,934,981 still leaves the count term at **70.95 percent**. The 2023 count is a documented source conflict: the BPS main body reports 3,816,750 and an executive-summary passage 3,934,981; the former reconciles to the displayed 2022 count and BPS's later stated growth rate and is used throughout.

## 7. Payment Traces and Institutional Visibility

### 7.1 Payment data outrun commerce

| Series, 2023→2024 | Growth |
|---|---|
| BPS e-commerce transaction value | 17.08% |
| Electronic-money shopping value | 30.47% |
| Mobile-banking payment and purchase value | 82.84% |
| Internet-banking payment and purchase value | 41.53% |
| QRIS transaction value | 186.98% |
| QRIS merchants | 18.05% |

Bank Indonesia's payment statistics provide a third record of the same activity, independent of issuer accounts and survey estimates. Payments and sales are different economic objects, and over 2023-2024 the digital payment series grew between 1.8 and 11 times as fast as e-commerce value. A digital-economy indicator built on payment value would have substantially overstated commerce growth over this period, which is the third direction in which the standard records misstate platform-based activity.

### 7.2 Business recordkeeping

Financial-report ownership among Indonesian e-commerce businesses is 15.19 percent in 2023 and 17.15 percent in 2024 as separately published wave values. BPS's own business-level analysis reports higher financial-report ownership among marketplace users than non-users, which supports H3. The within-province change between waves is weaker (Pearson r = 0.309, p = 0.066; Spearman rho = 0.151, p = 0.379; 36 common complete provinces), and the thesis tests the association further at business level, since province aggregates are ecological.

### 7.3 What administrative linkage would require

PMK 37/2025 is the institutional response. The verified implementation sequence records marketplace designation on 1 July 2026, collection effective 1 August, postponement through 31 October, and scheduled implementation on 1 November 2026. The regulation builds on seller identity, transaction-linked turnover, withholding and reporting.

A platform record becomes usable for tax administration only once a seller identity is attached, the record is transmitted to the Directorate General of Taxes, and it is matched to a taxpayer. The regime designates marketplace operators, and the marketplace channel carried 15.8 percent of 2024 e-commerce value and 1.5 percent of its 2023-2024 growth. However well it is implemented, its coverage is bounded by the channel it targets. Matching further depends on seller tax identity, which the largely micro population documented by BPS may not uniformly hold, and the postponement through 31 October 2026 indicates that operational readiness is the binding constraint.

Whether linkage delivers reporting, matching and compliance effects becomes testable once post-implementation data are available from November 2026, and is the natural extension of this thesis.

## 8. Corroboration Outside the Indonesian Sample

### 8.1 ASEAN context

| Country | E-commerce GMV 2023 (US$bn) | 2025 (US$bn) | Growth | Digital economy growth |
|---|---|---|---|---|
| Indonesia | 59 | 71 | 20.3% | 23.8% |
| Malaysia | 13 | 20 | 53.8% | 50.0% |
| Philippines | 17 | 24 | 41.2% | 38.5% |
| Singapore | 8 | 9 | 12.5% | 16.0% |
| Thailand | 22 | 33 | 50.0% | 47.4% |
| Vietnam | 19 | 25 | 31.6% | 30.0% |

The ASEAN panel holds **42 country-years across 6 countries, 2019-2025**, retained by publication vintage with GDP and household-consumption normalisation. Indonesia's e-commerce expansion sits within a region growing at very different rates, and vintage revisions in these estimates are large enough to be preserved rather than smoothed.

### 8.2 Global platform corroboration

Across **48 matched issuer-years for 8 platform businesses outside Indonesia**, including eBay, Etsy, Shopify, Jumia, Zalando, Rakuten, Mercado Libre and Sea, the same boundary appears under distinct business models. Of 40 annual transitions, 29 meet the clean-scope requirement and 4 of those show opposite-direction movement, with a median clean divergence of **7.10 pp** and a maximum of 2734 pp.

The clean-scope filter removes 11 of 40 transitions because acquisitions, perimeter changes or restatements make the pair non-comparable. The comparability problem that the evidence tiers address in Indonesia therefore recurs in mature, well-resourced global issuers, which makes it a feature of platform disclosure generally. The Indonesian median divergence of 42.02 pp is well above the global clean median. The global module corroborates the Indonesian result and is kept separate from it.

## 9. Discussion

### 9.1 What the evidence establishes

The standard records of platform-based commerce diverge in three measurable ways in Indonesia. Platform revenue understates the level of platform commerce: FY2023 transaction value is 13.7 times recognised revenue, a wedge of US$40.07 billion. Platform revenue also misstates growth: revenue outgrew transaction value in 10 of 12 transitions, with a median divergence of 42.02 pp that survives every robustness construction. And national records disagree with both: 98.46 percent of 2023-2024 e-commerce growth fell outside the marketplace channel, while payment value grew up to 11 times as fast as commerce. The Tokopedia reconciliation shows that the revenue-transaction divergence follows identifiable commercial choices.

### 9.2 Why it matters

An investor valuing platforms on revenue growth, a statistical agency sizing e-commerce from marketplace data and a policymaker reading payment growth as commerce growth are each working from a record that departs sharply from the activity they intend to measure, and in a different direction. The same transformation looks like rapidly monetising platforms, a stagnant marketplace sector or an explosion of digital commerce depending on which record is used. Indonesia's new reporting regime inherits the problem, because it is built around the marketplace channel. The thesis identifies proxy substitution between these records as the underlying error, and measures its size.

### 9.3 Claims, evidence and robustness

| Claim | Evidence and robustness test |
|---|---|
| Platform revenue understates platform commerce by more than an order of magnitude. | FY2023 transaction value is 13.7 times revenue (wedge US$40.07bn). Holds across Shopee monetisation of 9-11% (US$39.86-40.29bn), leave-one-platform-out (at least US$20.70bn), one-at-a-time input variation (US$37.65-42.49bn), and on the Tokopedia direct pair alone (US$15.93bn). |
| Platform revenue growth misstates commerce growth. | Revenue outgrows transaction value in 10 of 12 transitions; median divergence 42.02 pp. Holds in log changes (36.64), without the largest transition (29.34 pp), under the direct-candidate rule (42.94 pp) and in every leave-one-series-out construction. |
| Marketplace statistics miss where e-commerce grows. | 98.46% of 2023-2024 growth in e-commerce value falls outside the marketplace component; marketplace share 18.2% to 15.8%. Holds on both the published amount and the rounded-share reconstruction (98.49%). |
| Payment data overstate commerce growth. | Electronic-money, mobile-banking and QRIS payment value grew 1.8 to 11 times as fast as e-commerce value, 2023-2024. |
| Questions the thesis tests further. | Causal effects of incentive choices; business-level validation of the BPS recordkeeping association (province r = 0.309, p = 0.066); operational performance of PMK 37/2025 after 1 November 2026. |

### 9.4 Limits and further tests

The issuer sample is small and selected by disclosure availability, so the results are reported as robustness-tested measurements rather than population estimates. The BPS recordkeeping association is published at business level and weaker at province level. Payment series measure trace activity, which is why they serve as a comparison record. PMK 37/2025 establishes the legal architecture, and its operational effects become testable after 1 November 2026. The ASEAN and global modules are purposive corroboration. Each of these defines a test the thesis extends, and none of them qualifies the central claim.

## 10. Conclusion

This thesis set out to measure the gap between the commerce Indonesian platforms carry and the revenue their accounts record, and to establish what that gap implies for how the digital economy is measured. In FY2023, three documented platform cases processed 13.7 dollars of transaction value for every dollar of recognised revenue, a wedge of US$40.07 billion, and the gap is unstable over time: revenue outgrew the underlying transactions in 10 of 12 annual transitions, and Tokopedia's net revenue rose 53.20 percent in a year when its transaction value fell 8.90 percent, mostly through lower customer incentives.

The wider records point the same way. National statistics place 98.46 percent of Indonesia's 2023-2024 e-commerce growth outside the marketplace channel that platform accounts describe, and digital payment value grew up to 11 times as fast as e-commerce value. Platform revenue, marketplace statistics and payment data each misstate the digital economy in a different direction. Platform revenue understates its level and overstates its growth, marketplace statistics miss where it is growing, and payment data overstate how fast it is growing.

The contribution is a measurement result with direct consequences. The Ecosystem Ratio makes the boundary between processed value and recorded revenue measurable within a platform over time, and the evidence-tier design lets that measurement be reported at the directness each observation supports. Applied to Indonesia, it shows that the choice of record, usually treated as a question of data availability, determines the answer. Investors reading revenue growth, statistical agencies sizing e-commerce from marketplace data and policymakers designing platform reporting around the marketplace channel are each working from a record that departs sharply from the activity they intend to measure.

Indonesia's PMK 37/2025 is the first attempt to route platform-held records into tax administration, and its coverage is bounded by the marketplace channel before implementation begins. Whether it delivers reporting and matching in practice becomes testable from November 2026. The broader finding does not depend on that test: the records used to measure platform economies are not interchangeable, and treating them as if they were gives the wrong answer.

---

## Appendix A — Source lineage by evidence class

| Evidence class | Series | Source of V | Source of R |
|---|---|---|---|
| Direct Indonesia-aligned | Tokopedia e-commerce | GoTo annual report, segment metrics | GoTo annual report, segment note |
| Direct, scope-pending | Blibli 3P Retail | Global Digital Niaga prospectus and results | same issuer filings |
| Direct, scope-pending | Bukalapak Group | Bukalapak annual and sustainability reports | same issuer filings |
| Conditional reconstruction | Grab Indonesia | derived from Indonesia revenue and Group monetisation rate (Form 20-F) | Grab Form 20-F |
| Conditional reconstruction | Shopee Indonesia | Momentum Works SEA estimate (third-party) | derived from Sea Limited Form 20-F |
| National statistics | BPS-Statistics Indonesia | E-Commerce Statistics 2023, 2024; BPS directorate presentation | — |
| Payment system | Bank Indonesia | SPIP monthly and annual series; QRIS reports | — |
| Regulatory | PMK 37/2025; DJP | Ministry of Finance of the Republic of Indonesia | — |

## Appendix B — Reproducibility

Every figure in this manuscript is generated from files in this repository by `scripts/build_thesis_manuscript.py`. The sample boundary is the single parameter: this draft uses **direct_plus_scope_pending**. Re-running with `direct_only` or `all_tiers` regenerates the manuscript under that admission rule. Analytical outputs are produced by `scripts/analysis/build_hypothesis_tests.py` and the payment and robustness modules under `outputs/`.
