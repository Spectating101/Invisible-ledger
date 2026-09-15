# The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy

**Christopher Ongko (王新福)** · Yuan Ze University, MS Finance · Advisor: Prof. De-Rong Kong (孔德蓉)

*Sample boundary: **direct_plus_scope_pending**. Regenerate with a different boundary to follow the committee's ruling.*

---

## 1. Introduction

Digital platforms process far more transaction value than they recognise as their own revenue. I call that difference the **invisible wedge**. For a matched platform scope and period, the absolute wedge is *W = V − R*, where *V* is transaction value and *R* is platform-recognised revenue, and the **Ecosystem Ratio** *E = (V − R)/R* expresses the same boundary relative to revenue. The Ecosystem Ratio is constructed for this study rather than adopted from prior work.

Suppose a platform processes 100 units of transaction value and recognises 10 as revenue. The remaining 90 units are recorded inside the platform but are not platform revenue: they are merchant receipts, driver payouts, inventory cost, taxes paid elsewhere and other pass-through payments. The thesis measures that accounting boundary. It does not assume the residual is profit, taxable income, or unpaid tax.

For FY2023, three documented Indonesian platform cases imply a combined wedge of approximately **US$40.07 billion** at an Ecosystem Ratio of **12.671**, about **2.9 percent** of Indonesia's 2023 nominal GDP of US$1.371 trillion. That comparison is a scale reference only: the wedge is transaction value outside platform revenue, not value added, and therefore not a component of GDP.

"Invisible" does not mean concealed. A platform may hold seller- and worker-linked transaction records even where those records do not enter routine third-party income reporting. The wedge measures the transaction–revenue boundary; whether the underlying records are transmitted and usable outside the platform is a separate, institutional question this thesis treats as evidence rather than assumption.

**Research question.** *How large is the invisible wedge in Indonesia, how does it change over time, and what explains those changes?*

### 1.1 Hypotheses

|  | Hypothesis | Status in the evidence assembled here |
|---|---|---|
| H1 | transaction and revenue growth can diverge | supported in candidate inventory not final sample |
| H2 | aggregate growth partly reflects more businesses | supported for 2022 2024 aggregate decomposition |
| H3 | marketplace participation predicts financial recordkeeping | associated in published business level evidence not validated by province aggregates |
| H4 | institutional linkage failure | not yet tested |
| H5 | measurement choices can alter conclusions | supported by existing measurement modules |

H1 to H3 and H5 are addressed by the empirical chapters below. H4 is stated as the thesis's forward question: PMK 37/2025 implementation is scheduled for 1 November 2026, so evidence on actual administrative linkage postdates this draft. None of the five is framed as a causal claim.

## 2. Literature and Conceptual Framework

### 2.1 Platform economics and revenue recognition

Multisided-platform theory explains why platform revenue need not move proportionally with the transaction value a platform coordinates (Rochet and Tirole 2003; Caillaud and Jullien 2003; Parker and Van Alstyne 2005; Armstrong 2006; Hagiu and Wright 2015; Evans and Schmalensee 2016). Accounting then determines how much facilitated commerce becomes recognised revenue: principal–agent treatment under IFRS 15, customer incentives, service mix, acquisitions and reporting perimeter can all move revenue without an equivalent change in underlying commerce. De Franco, Kothari and Verdi (2011) establish why comparability of accounting bases matters when users interpret such differences.

### 2.2 Informality, digital records and third-party information

Platform participants occupy an unusual position: their transactions are priced, recorded and settled through a formal intermediary while the participants themselves may be self-employed, unregistered, below filing thresholds, or outside any automatic reporting channel. The object measured here is therefore not the shadow economy as conventionally defined (La Porta and Shleifer 2014; Ulyssea 2018; Medina and Schneider 2019). Digital records nevertheless carry economic information where conventional records are thin (Berg et al. 2020), and platform-mediated work leaves observable financial and administrative traces (Barrios, Hochberg and Yi 2022; Denes, Lagaras and Tsoutsoura 2025).

A central public-finance result is that third-party information changes compliance and enforcement (Kleven et al. 2011; Pomeranz 2015; Naritomi 2019; Kleven, Kreiner and Saez 2016; Slemrod 2019). The OECD Model Rules and the European Union's DAC7 regime are the closest policy precedents; Indonesia's PMK 37/2025 applies the same logic through seller identification, transaction-linked reporting and marketplace withholding.

### 2.3 Measuring the digital economy

National-accounting frameworks address the same boundary from the measurement side. Official guidance separates the underlying buyer–seller transaction from the intermediation service the platform provides, and rejects treating gross transaction value as value added or as an alternative output measure (Ahmad and Schreyer 2016; International Monetary Fund 2018; OECD 2023; United Nations et al. 2025). This literature establishes what the wedge is **not**, and is why the thesis treats *V − R* as an accounting boundary rather than unmeasured output.

### 2.4 Research gap

The literature explains why transaction value can exceed platform revenue, why accounting moves the two apart, and why third-party records matter for administration. What is missing is a longitudinal, source-auditable account for a single market that measures the wedge, explains why it moves, and then asks where the wider activity and its records appear beyond platform revenue.

### 2.5 Framework and key variables

Let *V* denote transaction value and *R* platform-recognised revenue on a matched scope and period:

> **W = V − R**   ·   **E = (V − R) / R**   ·   **D = g(V) − g(R)**

*W* is the absolute wedge, *E* the Ecosystem Ratio, and *D* the annual growth divergence. A higher *E* means more transaction value sits outside platform revenue per unit of revenue; it does not by itself imply participant profit, taxable income, value added, non-compliance or tax due. Gross transaction value (GTV) is the common label throughout; issuers use GMV or TPV for the same quantity and those source labels are retained in the empirical files rather than treated as interchangeable.

## 3. Data and Empirical Design

### 3.1 Admission rules

A platform-period is eligible only when transaction value and revenue cover the same period; geography and business scope can be evaluated; units and definitions are known; derived inputs trace to source; and structural breaks or revised reporting bases are flagged. Repeated publication vintages of the same underlying period are not counted as independent observations.

### 3.2 Evidence tiers

| Evidence tier | Series | Levels | Transitions | In this sample |
|---|---|---|---|---|
| direct Indonesia-aligned | Tokopedia e-commerce segment | 2 | 1 | yes |
| direct issuer, scope-pending | Blibli 3P Retail; Bukalapak Group | 9 | 7 | yes |
| conditional country reconstruction | Grab; Shopee | 6 | 4 | no |
| **All tiers (diagnostic)** | five series | 17 | 12 | — |

The inventory holds **17 candidate platform-year levels** across five series from FY2019 to FY2025. Under the **direct_plus_scope_pending** boundary used here, **11 levels** enter the main sample. Tokopedia is the strongest Indonesia-aligned segment but is not a literal country line; Blibli 3P Retail includes online travel; Bukalapak reports at Group scope with overseas operations; Grab and Shopee each require a derived or externally estimated country component. Tokopedia FY2021 and Bukalapak FY2024 are excluded because transaction and revenue periods do not match.

Three counts are intentionally different and are never collapsed into one *N*: the all-tier inventory holds 17 retained levels; the executed direct tiers hold 11 levels; and the broader direct-candidate sensitivity holds 13 periods, including a Blibli FY2020 prospectus observation, yielding 9 annual transitions.

### 3.3 Comparability strategy

The primary longitudinal inference is within-series: each platform is compared against its own prior year on a consistent reporting basis, so perimeter differences between issuers cannot drive the result. Cross-platform levels are descriptive and scope-labelled rather than a matched panel. The FY2023 cross-section establishes order of magnitude, not a ranking of platforms.

### 3.4 Conditional country constructions

Grab discloses Indonesia revenue but not Indonesia transaction value, so its conditional country transaction value is derived as **Indonesia GTV = Indonesia revenue × Group GTV / Group revenue**. The construction assumes the Group monetisation rate applies to Indonesia and is treated as sensitivity evidence. Shopee's Indonesia transaction value uses Momentum Works' recurring Southeast Asian e-commerce estimate, because Sea Limited discloses no Indonesian country figure; it is labelled third-party wherever it enters a calculation.

## 4. Issuer Evidence

### 4.1 FY2023 cross-section

| Case | V (US$bn) | R (US$bn) | W (US$bn) | E | Evidence class |
|---|---|---|---|---|---|
| Grab Indonesia | 5.381 | 0.605 | 4.776 | 7.895× | derived V |
| Tokopedia e-commerce | 16.331 | 0.405 | 15.926 | 39.296× | direct pair |
| Shopee Indonesia | 21.520 | 2.152 | 19.368 | 9.000× | derived V and R |
| **Selected platforms** | **43.233** | **3.162** | **40.070** | **12.671×** | sum, not a national total |

The final row sums three documented cases under mixed evidence classes and is not an Indonesia-wide estimate. One-at-a-time parameter variation moves the combined wedge between approximately US$37.65 billion and US$42.49 billion; leave-one-platform-out calculations give approximately US$35.29 billion, US$24.14 billion and US$20.70 billion. The large transaction–revenue gap does not depend on any single case.

### 4.2 Longitudinal divergence

| Admission rule | Transitions | Revenue faster | Transaction faster | Sign reversals | Median abs. divergence |
|---|---|---|---|---|---|
| all candidate tiers | 12 | 10 | 2 | 2 | 42.02 pp |
| conditional country reconstruction | 4 | 4 | 0 | 0 | 50.64 pp |
| direct indonesia aligned segment | 1 | 1 | 0 | 1 | 62.10 pp |
| direct issuer scope pending | 7 | 5 | 2 | 1 | 15.74 pp |

Reported by tier rather than pooled, because the tiers differ in how directly they map to Indonesia. The all-tier inventory gives 12 transitions at a median absolute divergence of 42.02 pp; the certified direct-candidate sensitivity gives 9 transitions at 42.94 pp. These answer different construction questions and neither is a filtered restatement of the other.

## 5. Mechanism and Robustness

### 5.1 Reconciling a divergence: Tokopedia FY2022–FY2023

Tokopedia provides the cleanest mechanism case. Transaction value falls **8.90 percent** while selected third-party net segment revenue rises **53.20 percent**. Of the arithmetic increase in net revenue, **60.56 percent** is associated with lower customer incentives and **39.44 percent** with higher gross revenue. This reconciles the divergence against disclosed components without asserting causality: the decomposition is arithmetic, and incentive policy is itself a managerial choice rather than an exogenous treatment.

### 5.2 Robustness of the longitudinal result

The direct-candidate baseline gives 9 adjacent annual transitions, 3 sign reversals and a median absolute ordinary growth gap of **42.94 pp**. Four checks follow.

- **Growth transformation.** Log changes rather than ordinary percentage growth give a median absolute gap of **36.64 log-points ×100**. Direction rankings and sign-reversal classification are unchanged.
- **Extreme transition.** Dropping the single largest gap (Blibli FY2022→FY2023, a low starting net-revenue base with major monetisation changes) leaves 8 transitions, still 3 reversals, median **29.34 pp**.
- **Leave-one-transition-out.** Across all nine exercises the median ranges **29.34 pp to 52.52 pp**. No single transition is necessary for the qualitative conclusion.
- **Leave-one-series-out.** Excluding Blibli leaves 4 transitions at 38.92 pp; Bukalapak, 6 at 52.52 pp; Tokopedia, 8 at 29.34 pp. Every construction retains at least one sign reversal.

These establish that the descriptive non-equivalence is not an artefact of one observation, one series, or the growth transformation. They do **not** establish a population effect: geographic and business scope quality changes sharply across the scenarios, and the small candidate count means these remain descriptive diagnostics rather than conventional inferential statistics.

## 6. Indonesia's Broader E-Commerce Transformation

### 6.1 National aggregates

| Year | Transaction value (Rp tn) | Estimated businesses | Implied value/business (Rp mn) | Marketplace (Rp tn) | Non-marketplace (Rp tn) |
|---|---|---|---|---|---|
| 2023 | 1100.87 | 3,816,750 | 288.43 | 200.68 | 900.19 |
| 2024 | 1288.93 | 4,400,972 | 292.87 | 203.58 | 1085.35 |

BPS-Statistics Indonesia reports national e-commerce transaction value rising **17.08 percent** from 2023 to 2024, with estimated e-commerce businesses rising **15.31 percent** and implied nominal value per business rising only **1.54 percent**. Both marketplace amounts are directly published; the 2024 figure of Rp203.58 trillion is preferred over reconstructing from the rounded 15.79 percent share, to which it reconciles.

### 6.2 Channel composition

The marketplace component grows **1.45 percent** while the non-marketplace component grows **20.57 percent**. In level terms the marketplace increase is Rp2.90 trillion against a total increase of Rp188.06 trillion, so approximately **98.46 percent** of the nominal increase falls outside the marketplace component that platform accounts observe. This is the single most consequential aggregate result in the thesis: it locates the growth outside exactly the channel the issuer evidence measures.

### 6.3 Extensive versus intensive margin

Decomposing *V = N × A* symmetrically into a business-count term and an implied-value-per-business term allocates the change exactly. The count term is the larger component in every comparison: **70.98 percent** of the 2022→2023 increase, **90.29 percent** of 2023→2024, and **76.95 percent** over 2022→2024. Substituting the conflicting 2023 count of 3,934,981 as a sensitivity still leaves the count term at **70.95 percent**, so the extensive-margin reading does not depend on that choice. The 2023 count is a documented source conflict: the BPS main body reports 3,816,750 and an executive-summary passage reports 3,934,981; the former is used because it reconciles to the displayed 2022 count and BPS's later stated growth rate.

## 7. Payment Traces and Institutional Visibility

### 7.1 Payment-system evidence

| Series, 2023→2024 | Growth |
|---|---|
| BPS e-commerce transaction value | 17.08% |
| Electronic-money shopping value | 30.47% |
| Mobile-banking payment and purchase value | 82.84% |
| Internet-banking payment and purchase value | 41.53% |
| QRIS transaction value | 186.98% |
| QRIS merchants | 18.05% |

Bank Indonesia's payment-system statistics give a view of digital trace activity independent of both issuer accounts and BPS survey estimates. Payments and sales are different economic objects, so these series are not competing estimates of the same quantity and are not reconciled one-for-one to issuer transaction value. Their analytical value is the contrast: digital traces expand on a markedly different trajectory from the commerce they help record. Trace abundance is therefore not evidence of measured activity, which is precisely the asymmetry the invisible wedge formalises.

### 7.2 Business recordkeeping

Financial-report ownership among Indonesian e-commerce businesses is 15.19 percent in 2023 and 17.15 percent in 2024 as separately published wave values. BPS also publishes a business-level analysis reporting higher financial-report ownership among marketplace users than non-users. That is BPS's own result and is cited as such. The within-province change between waves is unstable — Pearson r = 0.309 (p = 0.066), Spearman rho = 0.151 (p = 0.379) across 36 common complete provinces — so H3 is reported as a published association that province aggregates do not independently validate. Province-level evidence is ecological and is not used to infer a business-level relationship.

### 7.3 The reporting architecture

PMK 37/2025 is the institutional bridge. The verified implementation sequence records marketplace designation on 1 July 2026, collection effective 1 August, postponement through 31 October, and scheduled implementation on 1 November 2026. The regulation establishes a legal architecture built on seller identity, transaction-linked turnover, withholding and reporting — not on platform corporate revenue. Because implementation postdates this draft, the thesis can establish the architecture but not operational matching, compliance, or revenue effects. This is H4, and it is the study's principal forward question.

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

The ASEAN panel holds **42 country-years across 6 countries, 2019–2025**, retained by publication vintage with GDP and household-consumption normalisation. It is used to show that Indonesia's e-commerce expansion is neither unique nor uniform in the region. Vintage revisions are material in these estimates and are preserved rather than smoothed; the panel is contextual and is never pooled with issuer observations.

### 8.2 Global platform corroboration

Across **48 matched issuer-years for 8 non-Indonesian platform businesses** — eBay, Etsy, Shopify, Jumia, Zalando, Rakuten, Mercado Libre and Sea — the transaction–revenue boundary appears under distinct business models. Of 40 annual transitions, 29 meet the clean-scope requirement; 4 of those show opposite-direction movement, at a median absolute growth divergence of **7.10 pp**. This is external corroboration that the measured boundary is a general feature of platform accounting. It is not an Indonesia observation, not a representative global panel, and is never pooled with the main sample.

## 9. Discussion

### 9.1 What the evidence establishes

Three findings hold. The transaction–revenue boundary is economically large: for FY2023 the documented Indonesian cases imply a wedge of US$40.07 billion at an Ecosystem Ratio of 12.671. The boundary is not constant: within-series growth in transaction value and revenue diverges materially, with a median absolute divergence of 42.02 pp across the all-tier inventory and sign reversals that survive every robustness construction. And the boundary is explicable: the Tokopedia reconciliation traces a 53.20 percent net-revenue rise against an 8.90 percent transaction decline to disclosed incentive and gross-revenue components.

### 9.2 Why it matters

Different records support different diagnoses of the same transformation. Platform revenue growth implies a different performance story from transaction growth. Marketplace-centred evidence mislocates where national growth occurs — 98.46 percent of the 2023–2024 nominal increase falls outside the marketplace component. Payment growth is not commerce growth, as the QRIS and mobile-banking series show. And abundant private traces still require identity, a reporting rule, transmission and matching before they become administratively usable. The risk is not that these records differ; it is that one is used as a proxy for another without reconciling the boundary between them.

### 9.3 What it does not establish

| The evidence supports | It does not by itself establish |
|---|---|
| *W* and *E* measure the transaction–revenue boundary. | Participant profit, taxable income, unpaid tax, tax evasion or missing GDP. |
| Evidence tiers identify how directly each series maps to Indonesia. | That direct, scope-pending and conditional observations are interchangeable. |
| Issuer components arithmetically reconcile selected divergences. | A causal treatment effect of incentives, monetisation or accounting choices. |
| BPS and PMK document wider activity and reporting architecture. | A firm-level causal effect or a completed compliance or revenue effect. |
| Payment series expand faster than measured commerce. | That payment volume is commerce, or that the difference is unrecorded sales. |

### 9.4 Limitations

Five limitations bound the design. The issuer sample is small and selected by disclosure availability and comparability. BPS business-level relationships are observational and the province-level change is unstable. Bank Indonesia payment measures capture trace activity, not e-commerce sales. PMK 37/2025 establishes legal architecture while postponed implementation prevents inference about operational linkage. And the ASEAN and global modules are purposive corroboration rather than representative samples.

## 10. Conclusion

Indonesian platforms process transaction value far in excess of the revenue they recognise, that gap moves over time in ways disclosed accounting components can partly explain, and the national statistics locate most e-commerce growth outside the marketplace channel that platform accounts observe. Measured carefully, the invisible wedge is an accounting boundary rather than a hidden economy — but it is the boundary at which a platform's own records stop being visible in its revenue line, which is precisely where a reporting architecture like PMK 37/2025 has to operate. Whether those records become administratively usable is the question the next stage of this work takes up.

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
