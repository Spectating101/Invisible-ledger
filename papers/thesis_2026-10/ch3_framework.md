# Chapter 3. Framework and Hypotheses

Platform activity can be observed through several figures, and these figures do not measure the same economic object. Transaction value measures the commerce a platform carries. Revenue measures the part of that commerce the platform keeps. National statistics measure online sales across all sellers, whether or not they use a platform. The framework starts from the difference between the value a platform processes and the revenue it recognizes. It then asks whether that relationship stays stable over time, and whether figures from other sources give the same account of online activity. Figure 3.1 shows the structure.

Figure 3.1 places the three quantities inside one another. Revenue sits inside platform commerce, because a platform keeps only part of each sale. Platform commerce sits inside all online commerce, because many sellers trade outside platforms. The first hypothesis, H1, tests the inner link between revenue and platform commerce. The second, H2, tests the outer link between platform commerce and national online commerce. The figure is illustrative, and the sizes are not to scale. The platform circle also differs from the marketplace channel in the survey of online sellers run by BPS, the national statistics office.

[Figure 3.1 to be drawn: three nested circles, with revenue inside platform commerce inside all online commerce, H1 on the inner link and H2 on the outer link.]

The research question asks how much activity remains invisible when platforms are measured through revenue, and when that choice changes the conclusion about growth. The two links answer it. The inner link measures how much commerce revenue leaves out and whether the share that revenue captures stays stable (Sections 3.1 and 3.2). The outer link tests whether the commerce on platforms tells the same story of growth as national figures (Section 3.2). A further test checks the count of sellers behind national growth (Section 3.3). The reach of rules built on platform records is examined separately, in Chapter 6.

## 3.1 Measurement framework

Table 3.1 defines the terms used throughout the thesis, each once, with the symbol used in the formulas.

**Table 3.1. Terms and symbols**

| Term | Symbol | Meaning |
|---|---|---|
| Transaction value | V | Everything bought through a platform in a period, also called the commerce the platform carries. Companies call it gross merchandise value (GMV), gross transaction value (GTV) or total payment volume (TPV); the thesis treats these as one measure and notes where a company's scope differs. |
| Revenue | R | What the platform recognizes as its own income in its accounts. |
| Take rate | m | Revenue divided by transaction value: the share of each sale that the platform keeps. |
| Customer incentives | | Discounts, vouchers and other promotions that a platform pays for. Accounting rules normally deduct them from revenue, and Tokopedia reports the deduction as a separate line. |
| Invisible wedge | W | Transaction value minus revenue: what a revenue figure leaves out. It is defined for one platform. The thesis sums it over three platforms in Indonesia for 2023 and computes no national total. |
| Ecosystem ratio | E | The wedge divided by revenue. It equals one divided by the take rate, minus one. This is the author's own measure, built for this thesis. |
| Growth | g | The change from one year to the next as a share of the first year: 0.09 means 9 percent. |
| Growth divergence | D | Growth of revenue minus growth of transaction value in the same year: 0.62 means 62 percentage points. |
| Online seller | | A business that the national statistics office, BPS, counts as selling online; the text also calls it a seller or a business. The count of online sellers is BPS's estimate of how many there are in a year. |
| First-time entry | | A seller that began selling online in the year being measured. |

Transaction value and revenue are paired only when they refer to the same period and the same business. Figures that companies report are kept apart from figures that the thesis constructs, and both are kept apart from national statistics and payment figures (Chapter 4).

The invisible wedge measures, in currency, the part of transaction value that lies outside a platform's revenue:

```
W_it = V_it − R_it                                   (1)
```

where V_it is the transaction value of platform i in year t and R_it is the revenue it recognizes for the same year and business. The wedge is not an accounting error, because both amounts may appear in the same company report. It is a measure of transaction value, not of income or value added, so it does not measure missing output.

To compare platforms of different size, the thesis also expresses the wedge relative to revenue, as the ecosystem ratio:

```
E_it = W_it / R_it = 1 / m_it − 1                     (2)
```

where m_it = R_it / V_it is the take rate, the share of each sale that the platform keeps. The ecosystem ratio is the author's own measure, and it restates the take rate. Its interpretation draws on two established results. Platform pricing means that revenue need not follow the commerce a platform carries, and revenue recognition means that the share recorded as revenue depends on whether the platform acts as principal or agent (Rochet and Tirole 2003; Hagiu and Wright 2015; International Accounting Standards Board 2014). An ecosystem ratio of 9 means that 9 units of transaction value lie outside revenue for every unit recorded as revenue. Equivalently, the platform keeps 10 percent of each sale.

A single ratio does not show whether the relationship holds over time, so the thesis defines growth divergence:

```
D_it = g(R_it) − g(V_it)                              (3)
```

where g(X) is the growth of X from one year to the next, as a share of the first year. A positive D means that revenue grew faster than transaction value, so the take rate rose. A negative D means the reverse. Revenue equals the take rate times transaction value, so D can also be written with the take rate alone:

```
D_it = (1 + g(V_it)) × (m_it − m_i,t−1) / m_i,t−1      (4)
```

where m_i,t−1 is the take rate in the earlier year and m_it the take rate in the later year. If the take rate is steady, D is zero and revenue grows exactly as fast as transaction value. If revenue were a stable proxy for transaction value, D would stay close to zero.

Tokopedia between 2022 and 2023 illustrates the three measures. Its take rate rose from about 1.5 to about 2.5 percent, so it kept about two thirds more of each sale. Its transaction value fell by about 9 percent and its revenue rose by about 53 percent, so D was 0.91 × 0.68 = 0.62, or 62 percentage points. Its wedge stayed at about 98 percent of transaction value and fell with it, by about 10 percent.

The wedge, the ecosystem ratio and growth divergence do different jobs. The wedge gives the size of what revenue leaves out. At a marketplace that keeps a few percent of each sale, the wedge is almost all of transaction value, so it moves with the commerce. The ecosystem ratio expresses that size relative to revenue. Growth divergence carries the central test: whether revenue and transaction value keep the same relationship from year to year.

The ecosystem ratio also governs how far a change in the take rate moves revenue growth. Equation (4) shows that D is the change in the take rate divided by its starting level. A platform that keeps 2 percent of each sale has an ecosystem ratio of 49. If its transaction value is flat, a rise in its take rate to 3 percent raises its revenue by 50 percent. A platform that keeps 17 percent has an ecosystem ratio near 5, and a rise to 18 percent raises its revenue by about 6 percent. So a large ecosystem ratio means that ordinary changes in fees or discounts can produce large swings in reported revenue growth.

## 3.2 Hypothesis development

Two hypotheses follow from the research question. H1 asks whether revenue follows the commerce carried within a platform. H2 asks where national online growth comes from, which decides whether the commerce on platforms can stand for national online commerce. Together they test the two links in Figure 3.1. Table 3.2 pairs each hypothesis, and the entry test of Section 3.3, with its main test and with the result that would count against it.

**Table 3.2. Hypotheses, tests and what would count against them**

| Test | What it asks | Main test | What would count against it |
|---|---|---|---|
| H1 | Do revenue and transaction value grow together within a platform? | Size of yearly changes in the take rate, Indonesian and regional platforms against listed platforms abroad | Changes in Indonesia far larger than abroad |
| H2 | Does national e-commerce value grow because of more businesses or because of higher sales per business? | BPS's national e-commerce value split into the number of businesses and sales per business | Higher sales per business accounting for most of the growth |
| Entry test | Does a rise in the count of online sellers come from first-time entry? | Share of 2023 sellers in BPS's survey files who began selling online in 2023 | Fewer new sellers than the rise requires |

Platform economics and accounting both suggest that the share of transaction value a platform records as revenue is not fixed. The share depends on fees, on customer incentives and on whether the platform acts as principal or agent, and each of these can change with the platform's pricing, business model and scope (Rochet and Tirole 2003; Hagiu and Wright 2015; International Accounting Standards Board 2014). Research on disclosed operating measures adds that a measure becomes less informative when the way it is computed changes (Givoly, Li, Lourie and Nekrasov 2019). Revenue follows transaction value only while the take rate stays constant, that is, while D stays close to zero. If the relationship were stable, revenue would be a workable proxy for the commerce a platform carries, D would stay near zero and the ecosystem ratio would be constant. The first hypothesis states this case.

> **H1.** Transaction value and revenue recognized by the same platform grow in proportion over time.

Growth rates never match exactly, so H1 is tested by comparison. The test compares the size of yearly changes in the take rate, measured in logs, between two groups. One is the Indonesian and regional platforms, and the other is listed platforms abroad, where revenue and transaction value broadly move together. Chapter 4 describes the two groups and the test.

National e-commerce value can grow because existing businesses sell more, the intensive margin, or because more businesses sell online, the extensive margin (Hummels and Klenow 2005). The distinction matters for measurement. Growth driven by new sellers can take place in channels that platform accounts do not cover, such as social media and instant messaging, which BPS reports are widely used (BPS 2025). Platform figures can then miss that growth even when every platform reports accurately. BPS publishes both the number of businesses selling online and their total online sales, so national growth can be split into the two margins from published figures. The second hypothesis states the case in which more businesses drive growth.

> **H2.** The growth of national e-commerce value comes mainly from more businesses selling online, and less from higher sales per business.

The H2 split is arithmetic. It does not assign new businesses to channels, and it does not show whether the businesses in the count are new.

## 3.3 The entry test

H2 rests on BPS's count of businesses selling online, and a rise in that count can mean two different things. Either more businesses started selling, or the survey reached businesses that were already selling. The published figures cannot tell the two apart. The survey can, because it asks every seller in which year it began selling online. The thesis checks what the count contains with a test written down before the survey files were opened.

> **Entry test.** In the survey file for 2023, at least 21.5 percent of online sellers must report that they began selling online in 2023.

The 21.5 percent threshold comes from arithmetic. The published count of online sellers rose by 27.4 percent in 2023. Suppose every extra seller was new and no seller stopped. Then for every 100 sellers a year earlier there were 127.4, and 27.4 of those were new. New sellers would make up 21.5 percent of all sellers, which is 27.4 divided by 127.4. A smaller share means that part of the rise came from somewhere else. The test does not test H2 itself. It tests what "more businesses" means.

If the share of new sellers falls short, part of the rise is something other than first-time entry. Two readings are open: the survey reached more of the sellers who were already there, or sellers came back after a pause. Chapter 5 weighs them.

The split of national sales by channel and the comparison of record keeping between marketplace sellers and other sellers support the hypotheses without forming hypotheses of their own. The first shows whether national growth took place inside or outside the marketplace channel. The second shows whether marketplace sellers keep financial statements more often than other sellers, which bears on the information that platform records can supply to tax administration. Chapter 4 describes the data and methods behind each test and analysis.
