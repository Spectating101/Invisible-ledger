> **SUPERSEDED — do not rebuild the proposal from this file.** Since 2026-09-15 the canonical proposal is `papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx`, edited directly. This markdown holds an earlier abstract and framing.

# Invisible Ledger — merged proposal candidate

**Date:** 2026-09-14
**Base:** `docs/PROPOSAL_CONSOLIDATION_CANDIDATE_2026-09-14.md` (commit 3feec50)
**Changes against that base:** 1 correction, 8 restorations. Change log at the end of this file.
**Status:** not advisor-approved; not yet merged into the DOCX/PDF.

This file supersedes the consolidation candidate as the leading *content* candidate. It does not
supersede `papers/current/Invisible_Ledger_Thesis_Proposal_2026-09-14.docx` until the diff has been
inspected and the numbers re-verified against committed sources.

---

## Abstract

This study measures the difference between the transaction value digital platforms process in Indonesia and the revenue those platforms recognize. I call that difference the **invisible wedge**. The absolute wedge is *W = V − R*, where *V* is transaction value and *R* is platform revenue; the **Ecosystem Ratio**, *E = (V − R)/R*, expresses the same boundary relative to revenue and is constructed for this study rather than adopted from prior work. Because no Indonesian platform discloses a strictly country-labelled matched pair across the study period, observations are retained under named evidence tiers rather than pooled as if equal in scope. The inventory spans seventeen candidate platform-year levels across five issuer series from FY2019 to FY2025. Transaction value and revenue move differently, and disclosed revenue components explain important divergences. Official statistics and Indonesia's marketplace reporting rules then evidence wider activity and how platform-held records can enter third-party reporting.

---

## 1. Introduction

Southeast Asia's digital economy grew from **$100 billion in gross merchandise value in 2020 to $263 billion in 2024** (Google, Temasek and Bain 2020, 2024). Much of that activity is coordinated through digital platforms, but the value of transactions a platform processes can be far larger than the revenue it recognizes for itself. These platforms record transactions, determine participant payouts, and book their own revenue. I call the difference between the transaction value processed through a platform and the revenue that platform books the **"invisible wedge."**

The term invisible does not imply criminal concealment. Suppose a platform processes **100 units of transaction value** but recognizes only **10 units as revenue**. The remaining **90 units** are still recorded within the platform's system but do not constitute platform revenue. Instead, they may represent merchant receipts, driver payouts, inventory costs, taxes paid elsewhere, and other pass-through payments. The paper measures this accounting gap without assuming that the residual represents profit, taxable income, or unpaid tax. The 90-unit difference in this example is the **absolute wedge**, *W = V − R*.

I measure the wedge relative to platform revenue with the **Ecosystem Ratio**, defined as gross transaction value (GTV) not recognized as platform revenue divided by the revenue the platform does recognize. Inputs differ in directness and scope. Grab and Shopee country constructions require derived or external components, while Blibli and Bukalapak report both transaction and revenue inputs directly but at business or Group scopes that require explicit eligibility decisions. For fiscal year 2023 the selected platform cases place transaction value not booked as platform revenue at approximately **US$40.07 billion**, equivalent to roughly **2.9 percent of Indonesia's 2023 nominal GDP**. This comparison is a scale reference only: the wedge is gross transaction value outside platform revenue, not participant profit, unpaid tax, or GDP value-added.

Digital platform scale is also not the same as the information automatically reported about merchants, drivers, and other participants. Their gross receipts may remain outside routine third-party income reporting even when the platform holds a record of the transaction that produced them. **The wedge does not measure that reporting gap, and this paper does not claim it does.** The wedge measures the accounting boundary between processed transaction value and platform-booked revenue. Whether the activity behind that boundary is separately recorded and transmitted to public institutions is a further question the study then examines.

### 1.1 Research question and objectives

One question drives the proposal:

> **How large is the invisible wedge in Indonesia, how does it change over time, and what explains those changes?**

**Table 1. Research objectives and principal evidence.** *Objectives 1 and 2 concern the measurement and its movement within Indonesia; objective 3 follows the activity and the underlying records beyond platform accounts. Global issuer evidence is reported as external corroboration in Section 5.*

| | Objective | Principal evidence |
|---|---|---|
| 1 | Measure the wedge longitudinally while keeping evidence tiers visible | 17 retained candidate platform-year levels, three tiers, FY2019–FY2025 |
| 2 | Explain why the wedge moves | Disclosed monetization, customer incentives, gross-versus-net revenue, accounting, business scope |
| 3 | Locate the wider activity and the underlying records beyond platform revenue | National statistical evidence from BPS-Statistics Indonesia (*Badan Pusat Statistik*); Regulation PMK 37/2025 (*Peraturan Menteri Keuangan*) and Directorate General of Taxes (DJP) materials |

Table 1 shows that the three objectives rest on different evidence bases rather than on one dataset. The measurement, the explanation of its movement, and the wider-activity evidence each stand or fall on their own sources, so a weakness in one objective does not propagate to the others.

A separate module of **48 matched issuer-years across eight non-Indonesian platform businesses** is retained as external corroboration. It tests whether the transaction–revenue boundary also appears across other platform business models; it is not an Indonesia observation, not a representative global panel, and not a separate main research question.

### 1.2 Contributions

**First, longitudinal measurement.** Earlier evidence for Indonesia rested heavily on a single fiscal year. The current inventory spans seventeen retained candidate platform-year levels from FY2019 to FY2025 across five issuer series, with direct Indonesia-aligned, direct scope-pending, and conditional tiers kept separate. The study therefore reports both the scale of the wedge and its direction of travel. External issuer evidence provides corroboration that a transaction–revenue boundary is not peculiar to one Indonesian disclosure setting, while remaining outside the Indonesia sample.

**Second, mechanism.** The thesis explains why transaction value and platform revenue can move differently by reconciling material divergences against the revenue components issuers themselves disclose: monetization, customer incentives, gross-versus-net recognition, and reporting perimeter. These reconciliations are arithmetic against disclosed components, not causal decompositions.

**Third, wider economic and institutional interpretation.** The thesis connects the issuer-level accounting boundary to BPS evidence on e-commerce value, business participation, channels, payment practices, and recordkeeping. Indonesia's PMK 37/2025 and related Directorate General of Taxes materials then provide a concrete institutional example of how platform-held seller and transaction records can be used for reporting and withholding. This does not establish a completed compliance or tax-revenue effect.

### 1.3 What the proposal supports — and does not support

**Table 2. Claims supported and not supported by the evidence assembled for this proposal.**

| The evidence supports | The evidence does **not** by itself establish |
|---|---|
| Transaction value processed through selected platform scopes can substantially exceed platform-booked revenue. | That *V − R* is profit, taxable income, unpaid tax, tax evasion, or missing GDP. |
| The wedge and Ecosystem Ratio can be followed through time when period and scope are matched. | That all candidate tiers are equally direct or belong in one final advisor-approved sample. |
| Transaction-value growth and revenue growth can diverge, including opposite-sign transitions. | A causal mechanism unless a separate design identifies one. |
| Issuer revenue components can arithmetically reconcile selected divergences. | That accounting components are causal treatment effects. |
| BPS aggregates show wider e-commerce activity, channels, participation, and recordkeeping beyond issuer accounts. | A firm-level causal relationship or a reconciliation of BPS totals to issuer transaction value. |
| PMK/DJP documents establish a legal/reporting architecture using seller-linked transaction information. | That the policy has already raised compliance or tax revenue. |

Table 2 states the claim boundary row by row. The pattern is consistent across all six: what the assembled evidence supports is descriptive and measurement-focused, while every causal, fiscal or welfare reading sits in the right-hand column. The table is included so that the boundary is fixed before the examination rather than negotiated during it.

---

## 2. Literature Review and Research Gap

### 2.1 Platform economics and the location of value

The economics of multisided platforms begins with the interaction of distinct user groups whose participation affects the value received by the other side. Rochet and Tirole (2003), Caillaud and Jullien (2003), Parker and Van Alstyne (2005), and Armstrong (2006) show why platform pricing cannot be read as a simple markup over cost: prices and commissions are chosen to balance cross-group network effects, participation, and competition. Hagiu and Wright (2015) further distinguish a multisided platform from a vertically integrated firm by locating decision rights and entrepreneurial effort with affiliated participants rather than inside the platform. **Evans and Schmalensee (2016) translate the same point into the business-model literature.** These results explain why low retained shares can coexist with large ecosystems and why platform revenue is a poor proxy for the transaction value coordinated through the platform.

### 2.2 Accounting and revenue recognition

Accounting determines how much facilitated commerce becomes revenue. Under IFRS 15, principal–agent treatment governs gross-versus-net presentation, while customer incentives, advertising and service income, acquisitions, and reporting perimeter can move revenue without an equivalent change in commerce. De Franco, Kothari and Verdi (2011) show why comparability matters to users of financial statements. The accounting boundary therefore provides a mechanism for transaction value and recognized revenue to diverge even when both measures are correctly reported.

### 2.3 Informality, platform work, and measurement

Traditional informal-economy estimates rely on household surveys, firm surveys, or indirect macroeconomic indicators. Medina and Schneider (2019) estimate a large global shadow economy; La Porta and Shleifer (2014) emphasise the small scale and low productivity of informal firms; and Ulyssea (2018) shows that registration and off-the-books employment are distinct margins whose welfare effects cannot be inferred from formal status alone. **The International Labour Organization (2021, 2023) likewise treats platform work and informality as overlapping but non-identical categories.**

The finance literature supplies the complementary result that these digital records carry economic value in their own right. Berg, Burg, Gombović and Puri (2020) show that a simple digital footprint predicts borrower default as well as a credit bureau score, establishing that transaction-level traces held by an intermediary constitute usable financial information even where conventional records are thin. That is precisely the asymmetry this proposal measures: the record exists and is economically informative, but it is not necessarily visible in either the platform's revenue or the participant's reported income.

Platform participants occupy an unusual position in this literature. Their transactions are priced, recorded, and settled through a formal intermediary, but the participant may remain self-employed, unregistered, below filing thresholds, or simply outside an automatic reporting channel. The object measured here is therefore not the shadow economy as conventionally defined. It is a digitally recorded flow whose administrative treatment may resemble self-reported income even though an intermediary already possesses the transaction record.

### 2.4 Third-party reporting

A central result in public finance is that tax compliance depends strongly on third-party information and remittance structure. Kleven et al. (2011) find an evasion rate of 0.3 percent on income subject to third-party reporting versus 37 percent on self-reported income in Denmark. Pomeranz (2015) shows that the VAT paper trail creates self-enforcement across firms, while Naritomi (2019) demonstrates that consumer-held records can raise reported sales. Kleven, Kreiner and Saez (2016) formalise firms as fiscal intermediaries, and Slemrod (2019) places information reporting and remittance regimes among the core instruments of modern enforcement.

Platform work creates a new configuration: a large intermediary may hold detailed transaction records even where there is no comprehensive obligation to report seller or worker income. The administrative problem is therefore not necessarily a lack of data generation; it can be the absence, incompleteness, or fragmentation of the reporting rule. Barrios, Hochberg and Yi (2022) and Denes, Lagaras and Tsoutsoura (2025), both in the *Journal of Financial Economics*, further show that platform-mediated work leaves economically meaningful financial and administrative traces; the latter observes gig activity directly in U.S. tax returns.

### 2.5 Digital taxation and platform-reporting rules

Corporate digital-tax reforms and platform-participant reporting address different bases. The OECD Pillar One blueprint concerns the allocation of taxing rights over large multinational enterprises (OECD 2020b). By contrast, the OECD's Forum on Tax Administration report and Model Rules require platforms to collect and report information on income realised by sellers and service providers (OECD 2019, 2020a). The European Union's DAC7 regime similarly imposes due-diligence and reporting duties on platform operators (European Union 2021). These instruments provide the closest policy precedent for the mechanism studied here: using the platform's existing transaction record to improve participant-level visibility without treating platform revenue as the participant tax base. **Indonesia's PMK 37/2025 applies the same logic through seller identification, transaction-linked reporting, and marketplace withholding.**

### 2.6 Research gap

These literatures explain why transaction value can exceed platform revenue, why accounting can move the two apart, why participant records vary, and why third-party information matters. What is missing is a longitudinal, source-auditable account for one market that **measures the wedge, explains why it moves, locates the wider digital activity beyond issuer accounts, and then asks how the existing transaction records enter institutional reporting**. External issuer evidence can then test whether the underlying transaction–revenue boundary also appears across other platform business models without turning that corroboration into a second main sample.

---

## 3. Theoretical Framework: the Ecosystem Ratio

To capture the invisible wedge in Indonesia, I propose and construct the **Ecosystem Ratio**. The measure is my own construction for this paper rather than one adopted from a prior study.

Let *V* denote transaction value and *R* denote platform-recognized revenue. The **absolute invisible wedge** is:

> **W = V − R**

The **Ecosystem Ratio** expresses that wedge relative to platform revenue:

> **E = (V − R) / R**

For example, if a platform processes 100 units of transaction value and books 10 units as revenue, then *W = 90* and *E = 9*.

Gross transaction value (GTV) is the total value of transactions processed through a platform, regardless of who ultimately receives the proceeds. **Terminology note.** Issuers label this quantity inconsistently: Sea Limited and Blibli report *gross merchandise value* (GMV), Grab reports *gross merchandise value* for deliveries and *total payment volume* (TPV) for financial services, and GoTo reports *gross transaction value*. Where the underlying measure is the same, this proposal uses GTV throughout and records the issuer's own label in the source extracts. This construction is consistent with the platform-economics literature showing that booked platform revenue need not track the total transaction value coordinated through a multisided platform (Rochet and Tirole 2003; Evans and Schmalensee 2016).

The Ecosystem Ratio describes the scale of participant-facing transaction value relative to the platform's auditable revenue base. A higher ratio indicates a larger unbooked transaction flow relative to the platform's own revenue; it does **not** by itself imply greater participant profit, taxable income, value-added, non-compliance, or tax due.

This distinction is essential. Platform filings and investor disclosures can make the accounting gap measurable, but the tax treatment of the residual varies according to participant type, deductible expenses, tax thresholds, registration status, and taxes already remitted through other channels. The empirical contribution of this paper is therefore to quantify the recorded transaction flow that platforms process but do not book as their own revenue, and to establish how that quantity moves and why — **not** to infer the amount outside the tax system directly from *V − R*.

Because the transaction–revenue relationship also changes through time, the analysis compares transaction-value growth with platform-revenue growth for each within-series annual transition:

> **D = g(V) − g(R)**

Opposite signs identify periods in which activity and revenue move in different directions. Material divergences are then reconciled against disclosed revenue components rather than treated as self-explanatory changes in the wedge.

---

## 4. Data and Methodology

### 4.1 Admission rules and evidence tiers

Platform revenue and transaction value are taken from primary company disclosures whenever possible. A platform-period is **eligible for consideration** only when transaction and revenue measures cover the same period; geography and business scope can be evaluated; currency and units are known; original, revised and pro-forma bases are labelled; transaction and revenue definitions are recorded; derived inputs trace transparently to source inputs; structural breaks, acquisitions and reporting-perimeter changes are flagged; and repeated publication vintages of the same underlying period are not counted as independent observations.

Eligibility is not equivalent to final main-sample admission. The current analysis therefore keeps three evidence tiers visible. No expanded sample is represented as advisor-approved.

**Table 3. Evidence tiers for Indonesian platform observations.** *Tokopedia is a business segment rather than an explicit country line; Blibli 3P Retail also contains tiket.com travel and Bukalapak reports at Group level with overseas operations; Grab and Shopee each require one side to be derived. Tiers are never pooled into a single monetary total.*

| Evidence tier | Series | Levels | Transitions |
|---|---|---:|---:|
| Direct Indonesia-aligned segment | Tokopedia e-commerce | 2 | 1 |
| Direct issuer, scope-pending | Blibli 3P Retail; Bukalapak Group | 9 | 7 |
| Conditional country reconstruction | Grab Indonesia; Shopee Indonesia | 6 | 4 |
| All tiers (inventory diagnostic) | 5 series | 17 | 12 |

Table 3 reports how the seventeen candidate levels distribute across the tiers. The decisive figure is that only two levels — Tokopedia's — are directly Indonesia-aligned; nine are direct issuer disclosures whose geographic scope is still pending, and six require a country reconstruction. Sample size and evidence quality therefore move in opposite directions, which is why the tiers are reported separately and never summed into one monetary total.

### 4.2 Current candidate structure

No Indonesian platform provides a strictly country-labelled matched transaction-value / revenue pair across the full study period. Tokopedia supplies the strongest Indonesia-aligned issuer segment currently available. Blibli and Bukalapak provide direct issuer pairs but remain scope-pending because Blibli 3P Retail includes online travel and Bukalapak Group includes overseas operations. Grab and Shopee country constructions remain conditional because matching country transaction value and revenue are not both directly disclosed.

Tokopedia FY2021 is excluded for period mismatch. Bukalapak FY2024 is excluded because transaction value and revenue cover different durations. Candidate evidence is reported under its tier rather than silently promoted into one pooled sample.

The executed all-tier inventory currently contains **17 matched annual candidate levels and 12 within-series transitions across five series**. A **direct-candidate sensitivity excludes the conditional Grab and Shopee reconstructions and instead extends Blibli with its directly transcribed FY2020 prospectus observation**, giving **9 transitions**. These are different admissible evidence universes, **not a filtered subset of one another**, and are reported separately.

### 4.3 Retained evidence modules

The study is not a single-fiscal-year design. Table 4 lists the seven retained modules, each with its own unit of observation. They are never summed into one sample size, because their geographic, regulatory and business-model definitions differ.

**Table 4. Retained evidence modules and their role.** *Counts are not additive across rows.*

| Module | Coverage | Retained scale | Role |
|---|---|---|---|
| Direct Indonesian issuer candidates | FY2019–FY2025 | 13 period-matched; 12 with positive denominators | Candidate longitudinal core |
| Conditional country reconstructions | FY2021–FY2024 | 6 Grab/Shopee platform-years | Sensitivity only |
| Indonesia marketplace structure | 2022–2025 | Market-share and platform-structure evidence | Coverage and structural breaks |
| BPS official e-commerce evidence | 2020–2024 | National indicators; province evidence for 2023–2024, with 36 common complete provinces in the change analysis | Activity, channels, recordkeeping |
| ASEAN corroboration | 2019–2025 | 42 country-years from 450 source-vintage rows | Separate-country robustness |
| Global issuer corroboration | Multi-year | 48 matched issuer-years, 8 businesses | Business-model corroboration |
| Historical quarterly accounting | 2017–2022 | 47 company/segment-quarters | Historical disclosure evidence |

### 4.4 Conditional country constructions

Grab's Indonesia transaction value is derived from disclosed Indonesia revenue using the company's Group monetization rate (Group revenue / Group GTV); Table 5 sets out the derivation year by year. The assumption is transparent and testable but is not a direct country transaction-value disclosure. Shopee's Indonesia transaction value uses an external market estimate from **Momentum Works, whose annual Southeast Asian e-commerce report is the only recurring public source disaggregating regional marketplace transaction value by country and platform. It is used because Sea Limited discloses no Indonesian figure, is labelled a third-party estimate wherever it enters a calculation, and is tested in the Section 5.1 sensitivity.** These constructions are supporting / conditional evidence rather than proof that the same monetization rate holds identically at country level.

**Table 5. Worked derivation of conditional Indonesia transaction value for Grab.** *Indonesia revenue is directly disclosed and Group figures are source-reported; the final column is derived, not disclosed.*

| Year | Indonesia revenue | Group revenue | Group GTV | Conditional Indonesia GTV (derived) |
|---|---|---|---|---|
| FY2021 | US$79m | US$675m | US$16,061m | US$1,879.7m |
| FY2022 | US$275m | US$1,433m | US$19,937m | US$3,826.0m |
| FY2023 | US$605m | US$2,359m | US$20,983m | US$5,381.4m |

---

## 5. Preliminary Evidence and Feasibility

The current evidence is sufficient to establish feasibility while leaving final sample admission to advisor / committee judgment.

### 5.1 FY2023 cross-section and sensitivity

**Table 6. Indonesia-focused FY2023 cross-section, US$ billions.** *V is transaction value, R is platform revenue, E the Ecosystem Ratio. The final row sums three documented cases under mixed evidence classes and is not an Indonesia-wide total.*

| Case | V | R | Wedge | E | Evidence class |
|---|---|---|---|---|---|
| Grab Indonesia | 5.381 | 0.605 | 4.776 | 7.895× | Derived V |
| Tokopedia e-commerce | 16.331 | 0.405 | 15.926 | 39.296× | Direct pair |
| Shopee Indonesia | 21.520 | 2.152 | 19.368 | 9.000× | Derived V and R |
| Selected platforms | 43.233 | 3.162 | 40.070 | 12.671× | Sum, not a total |

Table 6 reports the FY2023 cross-section. The combined wedge is approximately **US$40.07 billion** at an Ecosystem Ratio of **12.671**. One-at-a-time parameter variation moves the wedge between approximately **US$37.65 billion and US$42.49 billion**. Leave-one-platform-out calculations give approximately **US$35.29 billion, US$24.14 billion, and US$20.70 billion**. These are composition and sensitivity checks, not estimates of one national total.

**Economic scale.** Against Indonesia's 2023 nominal GDP of approximately **US$1.371 trillion**, the combined wedge is equivalent to about **2.9 percent of GDP**. The GDP figure is taken from the World Bank (US$1,371,169,301,564) and cross-checked against the Federal Reserve Economic Data series (US$1,371,166,925,750), which agree to within 0.0002 percent. This comparison is a scale reference only. The wedge is transaction value not booked as platform revenue; it is not value added, and it is therefore not a component of GDP and not a claim about GDP mismeasurement.

### 5.2 Two valid longitudinal evidence universes

**Table 7. Within-series annual growth divergence under two admission rules.** *Counts differ because evidence admission differs; both are reported rather than resolved into a single headline.*

| | All-tier inventory | Direct-candidate sensitivity |
|---|---|---|
| Series admitted | Blibli FY2021–25, Bukalapak, Tokopedia, Grab, Shopee | Blibli FY2020–25, Bukalapak, Tokopedia |
| Transitions | 12 | 9 |
| Revenue grows faster | 10 | 6 |
| Transaction grows faster | 2 | 3 |
| Opposite-sign transitions | 2 | 3 |
| Median absolute divergence | 42.02 pp | 42.94 pp |

Table 7 compares the two admission rules side by side. The difference between these summaries comes from admission rules, not from an arithmetic contradiction. **The additional opposite-sign transition in the direct-candidate universe is Blibli FY2020→FY2021, which enters only when the prospectus observation is admitted.** The sample hierarchy is therefore shown rather than collapsed.

### 5.3 Mechanism: Tokopedia

Tokopedia FY2022–FY2023 provides the cleanest mechanism case currently reproduced from committed source extracts. Transaction value falls **8.90 percent** while selected third-party net segment revenue rises **53.20 percent**. Reconciling disclosed revenue components, approximately **60.56 percent** of the arithmetic increase in net revenue is associated with lower customer incentives and **39.44 percent** with higher gross revenue. The disclosed components sum to reported net revenue in both years. This is an arithmetic reconciliation, not a causal decomposition.

### 5.4 External corroboration

The **take rate** is platform revenue divided by gross transaction value — the share of processed commerce the platform books as its own revenue. The Ecosystem Ratio is its complement: *E = 1/(take rate) − 1*. Across **48 matched issuer-years for eight non-Indonesian platform businesses** — eBay, Etsy, Shopify, Jumia, Zalando, Rakuten, Mercado Libre and Sea — the transaction–revenue boundary appears across distinct business models while its magnitude varies substantially: **take rates range from 0.22 to 74.63 percent**. Of **40 annual transitions, 29 are clean-scope**, with a **median absolute growth divergence of 7.10 percentage points** and four transitions in which transaction value and revenue move in opposite directions. This module is purposively selected on disclosure availability, its definitions differ by issuer, its levels are not pooled, and it does not validate Indonesia country allocations. Its role is external corroboration only.

### 5.5 BPS and wider Indonesian e-commerce activity

BPS reports national e-commerce transaction value rising from **Rp1,100.87 trillion in 2023 to Rp1,288.93 trillion in 2024 (+17.08%)**, approximately US$72.2 billion to US$81.4 billion, while estimated e-commerce businesses rise from **3,816,750 to 4,400,972 (+15.31%)**. The 2023 business count is taken from the BPS main body/figure, which reconciles to the displayed 2022 count and its stated growth rate; an executive-summary passage in the same publication reports 3,934,981. The conflict is unresolved at source, is recorded in `data/bps_official/README.md` and in the repository's data-quality findings, and business-count growth is therefore reported as descriptive context rather than as a load-bearing result. In the current channel decomposition, the marketplace component grows approximately **1.45 percent** while the non-marketplace component grows approximately **20.57 percent**, so roughly **98.46 percent** of the nominal increase falls outside the marketplace component. These aggregates provide a wider view of Indonesian e-commerce activity; they are not reconciled one-for-one to issuer transaction value and do not establish a firm-level causal effect.

### 5.6 PMK 37/2025 and reporting architecture

PMK 37/2025 provides a current institutional application of platform-held seller and transaction records. The current verified timeline records marketplace designation on **1 July 2026**, collection effective on **1 August 2026**, postponement through **31 October 2026**, and a scheduled **1 November 2026** implementation date. DJP describes the mechanism as a change in collection / reporting architecture rather than evidence of a newly identified tax base. The proposal therefore uses PMK as evidence of institutional design, not as proof that compliance or tax revenue has already increased.

---

## 6. Limitations and decisions for the proposal examination

The wedge measures transaction value not booked as platform revenue. It does not establish that all residual GTV is profit, taxable income, unpaid tax, tax evasion, or GDP value-added. No Indonesian platform publishes a strictly country-labelled matched pair across the full longitudinal design, so every observation carries an explicit evidence tier and the tiers differ in what they support. Mechanism reconciliations are arithmetic against disclosed issuer categories, not causal decompositions. BPS evidence is aggregate / ecological relative to issuer observations. PMK 37/2025 does not yet provide a completed post-implementation period from which to estimate a compliance effect. The global issuer panel is purposively selected and is not a representative global population.

Two sample decisions should remain explicit rather than silently settled in prose:

1. whether **Blibli 3P Retail and Bukalapak Group** enter the final longitudinal main sample, remain a labelled direct scope-pending tier, or are excluded;
2. whether **Grab and Shopee conditional country reconstructions** may appear in the main comparison or should remain sensitivity evidence only.

Both decisions change the reported transition counts, and neither should be described as advisor-approved before the advisor / committee decides.

---

## 7. Work plan

**Table 8. Planned work to the final defence.** *The empirical backend is assembled and source-linked; the remaining work is sample admission, requested analysis, and manuscript construction.*

| Period | Planned work |
|---|---|
| September 2026 | Advisor review of the data package; proposal oral examination; freeze the sample-admission rule and the checks the committee requests. |
| October–November 2026 | Complete requested reconciliations and source concordance; extend sensitivity to the approved tier boundary; freeze thesis tables and figures. |
| Before final defence | Rebuild the manuscript under the approved sample; retain supporting modules only where they advance the final argument. |

Table 8 sets out the remaining work. The empirical backend is already assembled and source-linked; what remains is the sample-admission decision, any analysis the committee requests, and manuscript construction. The schedule therefore depends on the examination outcome rather than on further data collection.

---

## Appendix A — key variables

| Symbol | Definition | Status |
|---|---|---|
| *V* | platform transaction value (GTV or the issuer-equivalent metric, scope labelled) | observed or explicitly derived / external by tier |
| *R* | platform-recognized revenue on the matched scope and period | observed or explicitly derived by tier |
| *W* | *V − R*, absolute invisible wedge | derived |
| *E* | *(V − R)/R*, Ecosystem Ratio | author-constructed derived measure |
| *g(V)* | within-series transaction-value growth | derived from unrounded inputs |
| *g(R)* | within-series platform-revenue growth | derived from unrounded inputs |
| *D* | *g(V) − g(R)*, growth divergence | derived |

**Data sources by evidence tier.**

| Tier | Series | Source of *V* | Source of *R* |
|---|---|---|---|
| Direct Indonesia-aligned segment | Tokopedia e-commerce | GoTo Gojek Tokopedia annual report, e-commerce segment operating metrics | GoTo annual report, segment note |
| Direct issuer, scope-pending | Blibli 3P Retail | Global Digital Niaga prospectus and annual results releases | Same issuer filings |
| Direct issuer, scope-pending | Bukalapak Group | Bukalapak annual and sustainability reports | Same issuer filings |
| Conditional country reconstruction | Grab Indonesia | Derived: disclosed Indonesia revenue ÷ Group monetization rate (Grab Form 20-F) | Grab Form 20-F, disclosed Indonesia revenue |
| Conditional country reconstruction | Shopee Indonesia | Momentum Works Southeast Asia e-commerce report, third-party market estimate | Derived from Sea Limited Form 20-F at the estimated country take rate |
| National statistical evidence | BPS-Statistics Indonesia | *E-Commerce Statistics 2023* and *2024*; BPS directorate presentation for the 2024 sales-media split | — |
| Regulatory architecture | PMK 37/2025; DJP materials | Ministry of Finance of the Republic of Indonesia | — |

Every figure used in this proposal is traced to a named file and locator in the accompanying data package.

---

## Change log against `3feec50`

### Correction (1)

**§4.2 — the 9-transition universe was described as "a stricter direct-candidate sensitivity … after the relevant period/scope filters."** That implies a filtered subset of the 12-transition universe. It is not. Per `docs/EMPIRICAL_TIER_RECONCILIATION_2026-09-10.md` (branch `research/research-synthesis-20260910`), it removes the conditional Grab/Shopee reconstructions **and adds Blibli FY2020 from the prospectus transcription**, which is why transitions fall from 12 to 9 while opposite-sign transitions rise from 2 to 3 — impossible under filtering. Replaced with the explicit two-universe wording.

### Restorations from the Sept-14 10-page proposal (8)

1. **§7 Work plan + Table 8** — absent from the candidate; a proposal oral needs a timeline.
2. **Table 4, seven retained evidence modules** — absent; this is the answer to "one fiscal year is not sufficient." Recovers the ASEAN module (42 country-years from 450 source-vintage rows) and the historical quarterly module (47 company/segment-quarters), both otherwise dropped entirely.
3. **Global corroboration figures** — take rates **0.22–74.63 percent**, **40** annual transitions of which **29** clean-scope, median absolute divergence **7.10 pp**. The candidate said only "varies substantially"; the 340× spread is the finding.
4. **Momentum Works named and justified** — answers advisor comment 146 ("This is not a standard or commonly used company report. Please explain what the report is and why you use it").
5. **Tables 1, 5 and 6 restored as tables** — research objectives, Grab derivation, FY2023 cross-section. The candidate carried these as prose only.
6. **§5.2 Blibli FY2020→FY2021 explanation** — states which transition the extra reversal is, so the 9-vs-12 counts read as coherent.
7. **BPS USD equivalents** — approximately US$72.2 billion to US$81.4 billion alongside the rupiah figures (advisor comment 214, consistent currency).
8. **Table captions** — all eight tables captioned and numbered (advisor comments 119, 125, 154, 162).

### Not restored, deliberately (1)

**The Blibli mechanism case** (transaction value +34.72 percent against segment net revenue +465.33 percent). Arithmetically correct but a low-base artefact — segment net revenue moves from IDR 199 billion to IDR 1,125 billion — and the 3P Retail perimeter also contains travel. The candidate was right to leave Tokopedia as the single clean mechanism case.

---

## Verification status

Every load-bearing figure in **this file** was re-verified against committed repository outputs on
2026-09-14. The per-claim result is committed as
`outputs/verification_2026-09-14/merged_candidate_claim_ledger.csv`:
**46 claims checked, 46 PASS**, each row naming the claim, the value stated in the proposal, the value
reproduced from source, and the source file.

This supersedes the earlier note that the check still needed re-running; the audit in
`docs/PROPOSAL_REBUILD_AND_AUDIT_2026-09-14.md` was performed against the 10-page proposal, and the
ledger above was produced against this file specifically.

Two source-level caveats survive verification and are disclosed in the text rather than resolved:

- **BPS 2023 business count.** 3,816,750 (main body/figure) versus 3,934,981 (executive summary) in the
  same publication. The former is used because it reconciles to the displayed 2022 count and stated
  growth rate. Reproducing 15.31% confirms the arithmetic, not the source conflict.
- **Province coverage.** The change analysis uses 36 common complete provinces, not a full 39-province
  panel in both years.

Known gaps that remain open regardless of this file:

- never opened in Microsoft Word;
- the advisor's 9 September request to review the dataset was answered out of band via a Dropbox
  Empirical Data review, per Chris; that material has not been seen or reconciled against the data
  package built here;
- `main` now carries `docs/EMPIRICAL_TIER_RECONCILIATION_2026-09-10.md`, so the 9-vs-12 authority no
  longer depends on a branch, but the other five `research/*` branches remain unmerged.
