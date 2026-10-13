# Chapter 3. Framework and Hypotheses

A measure of the digital economy is a stand-in. Revenue stands in for the commerce a platform carries, and the figures of platforms stand in for the online economy of a country. A stand-in is only as good as its link to the thing it represents, so this thesis builds its framework around the links. It treats each link as a claim that can fail, measures how far each claim holds, and states in advance what result would show that it does not.

Figure 3.1 shows the structure. Three circles sit inside one another. The smallest is a platform's revenue, the part of each sale that it keeps. Around it is platform commerce, the full value of the sales the platform handles. The largest is all online commerce in a country, which also includes sellers who never use a platform. The inner link joins revenue to platform commerce, and the outer link joins platform commerce to all online commerce.

[Figure 3.1 to be drawn: three nested circles, with revenue inside platform commerce inside all online commerce, H1 on the inner link and H2 on the outer link.]

Each link holds only under a condition. The inner link holds while the share of each sale that the platform keeps stays steady, because then revenue rises and falls with the commerce. The outer link holds while national growth comes from the sellers that platforms record, because then platform figures show what the whole economy is doing. When a condition fails, the stand-in misleads. Revenue can rise while commerce falls, and platform growth can miss growth that happens elsewhere.

The two links answer the research question together. The inner link measures how much revenue leaves out and whether the share it keeps stays steady. The outer link asks whether the commerce that platforms carry is where the growth of the whole online economy happens. A third question sits beside them, because governments now write rules on platform records, and a rule can reach only what the records cover. So the framework asks three questions, and each becomes a measure, a test or both.

1. **How far does revenue follow commerce?** The invisible wedge, the part of transaction value that revenue leaves out, measures how much is missing. Growth divergence, the difference between the growth of revenue and the growth of transaction value, measures whether revenue still follows commerce from year to year. Hypothesis H1 states the expected case (Sections 3.1 and 3.2).
2. **Do platform figures follow national growth?** Hypothesis H2 asks whether national growth comes mainly from more businesses selling online or from higher sales per business. An entry test checks what a rise in the count of businesses contains (Sections 3.2 and 3.3).
3. **How far do rules built on platform records reach?** A separate analysis counts the sellers that such a rule can reach (Section 3.4 and Chapter 6).

## 3.1 Terms and measures

Table 3.1 lists the terms used throughout the thesis, each defined once, with the symbol used in the formulas. The first rows describe a single platform, and the last rows describe the national survey.

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

The framework builds three measures from a platform's revenue (R) and transaction value (V). Each is a formula:

```
W = V − R
E = W / R = 1/m − 1
D = g(R) − g(V)
```

The invisible wedge W is the part of transaction value that revenue leaves out, in currency. The ecosystem ratio E is the same part relative to revenue, so that large and small platforms can be compared. It restates the take rate. Growth divergence D shows whether revenue still follows the commerce from one year to the next. The wedge and growth divergence are plain arithmetic on reported figures.

Growth divergence can also be written with the take rate alone. Let m0 be a platform's take rate in the first year and m1 its take rate in the second year. Revenue is the take rate times transaction value in each year, so revenue in the second year equals (1 + g(V)) × m1 / m0 times revenue in the first year. Subtracting the growth of transaction value gives:

```
D = (1 + g(V)) × (m1 − m0) / m0
```

When the take rate is steady, m1 equals m0, D is zero, and revenue grows exactly as fast as the commerce. When the take rate rises, D is positive, and revenue grows faster than the commerce.

Tokopedia between 2022 and 2023 shows the formula at work. Its take rate rose by about 68 percent, so that it kept about two thirds more of each sale. Its transaction value fell by about 9 percent, yet its revenue grew by about 53 percent. Growth divergence was 62 points, which is (1 − 0.09) × 0.68 = 0.62.

Tokopedia's case also shows what each measure records. Its wedge was about 98 percent of its transaction value in both years, so the wedge moved with the commerce and fell by about 10 percent along with it. Its growth divergence was 62 points, because revenue followed the take rate and not the commerce. The two measures answer different halves of the research question. The wedge answers the question of size, and at the marketplaces studied in Indonesia it is almost all of transaction value. Growth divergence answers the question of growth, because it follows the take rate and shows whether revenue remains a fair guide.

The size of the wedge next to revenue also decides how far a change in the take rate swings revenue growth. Take a platform that keeps 2 percent of each sale, with an ecosystem ratio of 49. If transaction value is flat, a rise in its take rate from 2 to 3 percent lifts revenue growth by about 50 points. A platform that keeps 17 percent has an ecosystem ratio near 5, and a rise from 17 to 18 percent lifts its revenue growth by about 6 points. A wedge that is large next to revenue means more than a big number. It also means that ordinary changes in fees or discounts can swing reported growth.

## 3.2 Hypotheses

The framework tests the two links with two hypotheses. H1 asks whether revenue follows commerce within a platform. H2 asks where the growth of national online commerce comes from, which decides whether platform figures can speak for the whole economy.

The take rate depends on fees, on discounts and on how the platform's accounts treat each sale. Revenue stays a fair stand-in for the commerce only while the take rate is steady, which means that growth divergence stays close to zero. H1 states that case.

> **H1.** Transaction value and revenue recognized by the same platform grow in proportion over time.

Growth rates never match exactly, so H1 is tested by asking whether growth divergence among Indonesian and regional platforms, measured in logs, is unusually large. The yardstick is growth divergence among listed platforms abroad, where revenue and transaction value broadly move together. Chapter 4 describes both groups.

National online sales can grow because existing sellers sell more or because more businesses sell online. BPS publishes both the number of businesses selling online and their total online sales, so the split can be made from published figures. The split matters for platform figures because new businesses often start in channels that platform records do not cover, such as messaging and social media, which most sellers use. If growth comes mainly from more businesses, platform figures can miss it even when every platform reports accurately. H2 states that case.

> **H2.** The growth of national e-commerce value comes mainly from more businesses selling online, and less from higher sales per business.

The H2 split is arithmetic. It does not say which channels the new businesses use, or whether they are new.

## 3.3 The entry test

H2 rests on a count: the number of businesses selling online. A rise in that count can mean two different things, so the thesis checks what it contains before relying on it. Either more businesses started selling, or the survey reached businesses that were already selling. The published figures cannot tell the two apart. The survey can, because it asks every seller in which year it began selling online.

> **Entry test.** In the survey file for 2023, at least 21.5 percent of online sellers must report that they began selling online in 2023.

The threshold is arithmetic. The published count of online sellers rose by 27.4 percent in 2023. Suppose every extra seller was new and no seller stopped. Then for every 100 sellers a year earlier there were 127.4, and 27.4 of those were new. New sellers would make up 21.5 percent of all sellers, which is 27.4 divided by 127.4. A smaller share means that part of the rise came from somewhere else. The test was written down before the survey files were opened, as Chapter 4 describes. It does not test H2 itself. It tests what "more businesses" means.

If the share of new sellers falls short, part of the rise is something other than first-time entry. Two readings are open: the survey reached more of the sellers who were already there, or sellers came back after a pause. Chapter 5 weighs them.

## 3.4 Further analyses

Four further questions use the same measures but carry no hypothesis. Where did large movements in revenue come from: more commerce, higher fees or smaller discounts? Do platform, national and payment figures tell the same story where they cover the same sellers? Which channels do online sellers use, and do they keep financial statements? And do investors value a platform's growth in transaction value differently from growth in its take rate? Chapter 4 describes how each is answered. Chapter 6 uses the answers to ask how many sellers a rule built on platform records can reach.

## 3.5 The tests together

Table 3.2 pairs each test with the result that would count against it.

**Table 3.2. Tests and what would count against them**

| Test | What it asks | What would count against it |
|---|---|---|
| H1: growth divergence | Do revenue and transaction value grow together within a platform? | Growth divergence in Indonesia far larger than among listed platforms abroad |
| H2: split of national growth | Does national e-commerce value grow because of more businesses or because of higher sales per business? | Higher sales per business accounting for most of the growth |
| Entry test | Does a rise in the count of online sellers come from first-time entry? | Fewer new sellers than the rise requires, so that the count reflects more than first-time entry |

The first two rows test the hypotheses. The third row sits beside H2, because it tests what the count of online sellers behind H2 represents. Chapter 4 describes the data behind each test.
