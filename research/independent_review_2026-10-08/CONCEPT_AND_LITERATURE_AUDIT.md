# Concept and literature audit — 8 October 2026

Complementary work for the researcher and Claude. This is a source-check and drafting package, not a new thesis concept or an adopted sample decision. The active proposal remains the September 27 PDF. The original question, title and hypotheses stay fixed.

## What this pass adds

1. Exact growth identities checked against existing rows, with ordinary rates kept separate from log changes.
2. A precise explanation of the existing absolute-component movement statistic.
3. Tokopedia's incentive contribution checked against the original annual report at full precision.
4. A primary-source map for the closest literature and the limits of its support.
5. A clear link between the proposal's inner and outer circles, without combining incompatible levels.

See [measurement_checks.py](measurement_checks.py), [measurement_checks.json](measurement_checks.json), [growth_bridge.csv](growth_bridge.csv), and [draft inserts](RESULTS_INSERTS.md). Run the script from any directory. It checks the arithmetic, the saved component-share summaries, and the annual-report text. Relevant report pages were also rendered and inspected. The outputs record input hashes and the repository HEAD at execution. Inputs changing during execution cause an assertion failure.

## 1. Ordinary growth needs its interaction term

Let gV, gR and gm be ordinary growth expressed as fractions. With positive, consistently defined transaction value and revenue:

`1 + gR = (1 + gV)(1 + gm)`

`gR = gV + gm + gV × gm`

`D = gR − gV = (1 + gV) × gm`

The exact additive decomposition uses logs:

`Δln R = Δln V + Δln m`

The proposal already qualifies the ordinary-growth approximation. The October numerical code also correctly uses logs. The framework's plain statement that revenue growth equals transaction growth plus take-rate growth should retain this distinction when drafted. This is a wording repair, not a discovered numerical-code failure.

All 52 rows in the existing transition table pass the exact identities. That count includes separate analytical tiers; it is not the thesis sample N. The source-matched Tokopedia case makes the distinction visible: transaction growth is −8.9%, net revenue growth is +53.2%, and take-rate growth is +68.2%. Adding the ordinary percentages without the interaction term misses revenue growth by 6.1 percentage points. These values are derived from the existing source-linked levels in [measurement_checks.json](measurement_checks.json).

The growth-direction conclusion remains unchanged. For Tokopedia, a take-rate increase of about 9.8% would have kept revenue flat despite the decline in transaction value. The observed increase was larger. This threshold is an accounting condition, not a new statistical test or pricing estimate.

## 2. Two thirds describes absolute component movement

The existing `wedge_split.py` computes:

`|Δln m| / (|Δln V| + |Δln m|)`

It then takes the median across transitions. The main series yield 66.5%; the original clean foreign benchmark yields 26.7%. The inputs cover three main series with eight transitions and eight foreign series with 29 clean transitions. They are not the expanded five-versus-27 comparison. These summaries independently reproduce the saved values.

This statistic describes the relative sizes of the two accounting components before they offset. It is not the share of net revenue growth, the fraction of explained variance, or a causal contribution. At Tokopedia, the take-rate component exceeds the net log revenue increase because the transaction component is negative. That is why a signed share can exceed the whole increase while the absolute-component share remains bounded.

The existing 38.9 versus 7.1 percentage-point comparison is the median **absolute** growth divergence across transitions. The signed medians are 15.1 and 6.5. Keep “absolute” in the result and table caption. No existing p-value is recalculated or relabelled by this check.

## 3. Full-precision Tokopedia inputs support the proposal

The source is [GoTo's 2023 annual report](../../sources/core_public_documents/goto_annual_report_2023.pdf): operating metrics at PDF page 144, printed page 142; and Note 29 at PDF pages 475–476. The financial-statement pages are marked 5/111 and 12. Units are IDR million. The 2022 comparison is restated. The e-commerce column is an Indonesia-aligned segment, not an explicit geographic line.

| Third-party segment component | 2022 | 2023 | Accounting contribution to net revenue increase |
|---|---:|---:|---:|
| Gross revenue | 8,143,239 | 8,988,909 | +845,670 |
| Customer incentive deduction, magnitude | 4,112,320 | 2,813,719 | +1,298,601 through a smaller deduction |
| Net revenue | 4,030,919 | 6,175,190 | +2,144,271 |

The lower deduction accounts for 60.5614% of the net revenue increase, rounding to **60.6%**, as in the proposal. Higher third-party gross revenue accounts for the remaining 39.4%. The October `h1_groundwork.json` uses rounded component inputs and produces 60.4651%, rounding to 60.5%. Both calculations are understandable; the source-precision calculation is preferable for final prose. This package does not overwrite either vintage.

Do not substitute the separate operating presentation's total gross segment revenue for third-party gross revenue here. Note 29 also shows inter-segment revenue. Gross revenue in this accounting table is also distinct from transaction value. The log growth decomposition and this level change explain different denominators; their contribution percentages need not match.

## 4. Primary-source literature map

Checked online on 8 October 2026. For papers, verification here generally covers publisher metadata, abstracts and selected public notes, not complete subscription texts. Institutional reports were checked through official summaries or relevant HTML sections. This is a targeted audit, not a certification of the proposal's entire reference list.

| Work and verified reference | What it supports here | Limit on its use |
|---|---|---|
| Rochet and Tirole (2003), *Platform competition in two-sided markets*, JEEA 1(4), 990–1029. [Publisher](https://academic.oup.com/jeea/article-abstract/1/4/990/2280902), DOI 10.1162/154247603322493212. | Pricing across platform sides and the need to attract both groups. | Background theory; does not establish the Indonesia growth episode or a wedge statistic. |
| Hagiu and Wright (2015), *Multi-sided platforms*, IJIO 43, 162–174. [Publisher](https://www.sciencedirect.com/science/article/pii/S0167718715000363), DOI 10.1016/j.ijindorg.2015.03.003. | The distinction between platform, reseller and vertically integrated business models. | Economic organisation is not the IFRS principal/agent test. Gross/net accounting needs its own source. |
| Givoly, Li, Lourie and Nekrasov (2019), *Key performance indicators as supplements to earnings: Incremental informativeness, demand factors, measurement issues, and properties of their forecasts*, RAST 24, 1147–1183. [Publisher](https://link.springer.com/article/10.1007/s11142-019-09514-y). | KPI information content declines when computation details are missing or change. | The public note says technology KPIs are excluded for insufficient observations. It supplies a general principle, not prior evidence on platform GTV. |
| De Franco, Kothari and Verdi (2011), *The benefits of financial statement comparability*, JAR 49(4), 895–931. [Publisher](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1475-679X.2011.00415.x), DOI 10.1111/j.1475-679X.2011.00415.x. | Comparability and analyst information benefits. | Use for why comparability matters. The verified abstract does not substantiate principal/agent revenue recognition. |
| Hummels and Klenow (2005), *The variety and quality of a nation's exports*, AER 95(3), 704–723. [Publisher](https://www.aeaweb.org/articles?id=10.1257/0002828054201396). | Intensive/extensive margin terminology in trade. | Its extensive margin concerns export varieties. It is an analogy for seller participation, not validation of the BPS business-count decomposition. |
| Trueman, Wong and Zhang (2001), *Back to basics: Forecasting the revenues of Internet firms*, RAST 6, 305–329. [Publisher](https://link.springer.com/article/10.1023/A:1011623111051). | Historical finance research connecting web activity, revenue forecasts and analyst information. | Web traffic in that period is not modern platform transaction value. The thesis's valuation evidence remains its own result. |
| Ahmad and Schreyer (2016), *Measuring GDP in a Digitalised Economy*, OECD Statistics Working Papers 2016/07. [OECD](https://www.oecd.org/en/publications/measuring-gdp-in-a-digitalised-economy_5jlwqd81d09r-en.html), DOI 10.1787/5jlwqd81d09r-en. | Distinguishing national-accounting concepts from practical compilation problems. | Its conclusion supports the ability of the GDP framework to address digitalisation. It does not support claiming that GDP counts only platform revenue or omits all participant activity. |
| OECD (2023), *OECD Handbook on Compiling Digital Supply and Use Tables*. [Official report](https://www.oecd.org/en/publications/2023/11/oecd-handbook-on-compiling-digital-supply-and-use-tables_b127cb7a.html), DOI 10.1787/11a0db02-en. | Separate ordering method, product and industry dimensions; distinguish intermediated sales from intermediation services. | A conceptual recording framework does not establish how much of Indonesian activity is actually captured. |
| UNCTAD (2023), *Measuring the value of e-commerce*, UNCTAD/DTL/ECDE/2023/3. [Official report page](https://unctad.org/publication/measuring-value-e-commerce). | Existing efforts to improve e-commerce value statistics and comparable methods. | The measurement problem is already recognised. Novelty should rest on this study's specific reconciliation and evidence. |
| UNCTAD (2024), *Business e-commerce sales and the role of online platforms*, UNCTAD/DTL/ECDE/2024/3. [Official report page](https://unctad.org/publication/business-e-commerce-sales-and-role-online-platforms). | Already presents business e-commerce sales, online retail sales and transaction values through major platforms. | Comparing these kinds of numbers alone is not an uncontested novelty claim. The public summary does not establish whether its full report already covers every proposed reconciliation. |
| van den Brakel, Zhang and Tam (2020), *Measuring discontinuities in time series obtained with repeated sample surveys*, ISR 88(1), 155–175. [Publisher indexed summary](https://onlinelibrary.wiley.com/doi/pdf/10.1111/insr.12347), DOI 10.1111/insr.12347. | Established methods for discontinuities caused by survey redesign. | The general problem does not prove BPS redesigned its frame or identify the seller residual. Direct access returned a restriction in this pass; full methodological comparison remains pending. |

### Accounting qualifications

IFRS 15's customer-payment rule includes an exception for payments purchasing a distinct good or service. The paragraph-70 wording was checked through an indexed [official standard excerpt](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ifrs-15-revenue-from-contracts-with-customers.pdf?bypass=on); direct access subsequently redirected to the subscription page. An [IASB staff paper on the post-implementation review](https://www.ifrs.org/content/dam/ifrs/meetings/2024/april/iasb/ap6f-ifrs15-pir-determining-transaction-price-cpc-sfc.pdf) also identifies application questions involving agent incentives to end customers. That staff paper is context, not an amendment to the standard.

For the thesis, identify the issuer's actual deduction. Tokopedia's Note 29 directly supplies it. A universal statement that all discounts, promotions and subsidies reduce revenue would go beyond this evidence.

The IFRS principal/agent assessment turns on control of the specified good or service before transfer. [The Foundation's explanation of the applicable requirements](https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-november-2021/) provides this framework in a tentative software-reseller decision. Use the cited requirements as accounting background, not the tentative fact-pattern conclusion as a ruling about the sampled platforms.

## 5. The connection between the circles needs a separate share condition

This is an explanatory identity, not a new metric or hypothesis. Let C denote a consistently defined total of online commerce, and let s = V/C describe the share carried by the relevant platforms. With genuinely compatible scopes:

`R = m × s × C`

`Δln R − Δln C = Δln m + Δln s`

This separates two questions already in the proposal. H1 examines the retained share inside platforms. Channel evidence examines how much commerce platform measures cover. H2 examines the published growth decomposition and its interpretation through participation evidence. H2 alone does not establish a stable platform share of national commerce.

Stable m and s are sufficient for revenue and national commerce growth to match. Opposite changes in the two shares can also offset; agreement between headlines alone does not establish that either share was stable. [measurement_checks.json](measurement_checks.json) contains a synthetic cancellation check, clearly labelled as invented.

Do not calibrate this identity by multiplying the constructed issuer revenue share by BPS's marketplace share. The numerator and denominator definitions have not been harmonised. The existing definition map and cross-source size-gap work are already the basis for explaining that limit.

## Contribution wording to consider

The most defensible positioning is a documented application and reconciliation: establish when matched platform revenue and transaction values change the apparent growth conclusion; explain retained-share movements using issuer disclosures; and test how far the national participation and channel evidence supports the wider story. Report the boundary where the records cannot complete the reconciliation.

This extends established pricing, accounting and statistical work through a connected empirical case. This targeted search does not establish global priority. Avoid a claim that no earlier work has compared platform transaction values with wider e-commerce statistics. Preserve the distinction between the national-accounting framework and the particular public measures examined here.

## For Claude

The actionable drafting changes are small: restore the exact proposal-consistent incentive percentage, specify absolute growth divergence, define the movement-share denominator, keep additive growth decomposition in logs, and match each literature citation to the claim it supports. The draft inserts supply usable wording. The current groundwork can adopt these through its dated-note process; this package does not edit its frozen text or preregistration.
