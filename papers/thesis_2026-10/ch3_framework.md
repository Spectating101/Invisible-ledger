# Chapter 3. Framework and Hypotheses

Three numbers sit in a chain. A platform's revenue is the smallest, the commerce the platform carries is larger, and the online commerce of the whole country is larger still. Each number is used as a stand-in for the next one out. Investors read revenue as a sign of the commerce a platform carries. Platform figures are then read as a sign of what is happening in the national total.

[Figure 3.1 to be drawn: three nested circles, with revenue inside platform commerce inside all online commerce, H1 on the inner link and H2 on the outer link.]

A stand-in works only while a condition holds. Revenue follows the commerce a platform carries while the share of each sale that the platform keeps stays steady. A count of online sellers follows the arrival of new sellers while the survey keeps reaching the same kinds of seller. This chapter defines the terms, builds the measures, and states the two hypotheses and the entry test that put each condition to the test.

## 3.1 Terms and measures

Table 3.1 lists the terms used throughout the thesis, each defined once, with the symbol used in the formulas. The first rows describe a single platform, and the last rows describe the national survey.

**Table 3.1. Terms and symbols**

| Term | Symbol | Meaning |
|---|---|---|
| Transaction value | V | Everything bought through a platform in a period. Companies call it GMV, GTV or TPV; the thesis treats these as one measure and notes where a company's scope differs. |
| Revenue | R | What the platform recognizes as its own income, after the discounts and incentives it pays to customers are deducted. |
| Take rate | m | Revenue divided by transaction value: the share of each sale that the platform keeps. |
| Customer incentives | | Discounts, vouchers and other promotions that a platform pays for. Accounting rules deduct them from revenue. |
| Invisible wedge | W | Transaction value minus revenue: what a revenue figure leaves out. It is defined for one platform; no national total is computed. |
| Ecosystem ratio | E | The wedge divided by revenue. It equals one divided by the take rate, minus one. This is the author's own measure, built for this thesis. |
| Growth | g | The percentage change from one year to the next. |
| Growth divergence | D | Growth of revenue minus growth of transaction value in the same year, in percentage points. |
| Online seller | | A business that the national statistics office, BPS, counts as selling online. |
| First-time entry | | A seller that began selling online in the year being measured. |

Three measures describe a platform. The invisible wedge gives the size of what revenue leaves out, in currency. The ecosystem ratio gives the same size relative to revenue, so that large and small platforms can be compared. Growth divergence shows whether revenue still follows the commerce from one year to the next. The wedge and growth divergence are plain arithmetic on reported figures. The ecosystem ratio restates the take rate, as the formulas show.

```
W = V − R
E = W / R = 1/m − 1
D = g(R) − g(V)
```

Revenue equals the take rate times transaction value, so growth divergence can be written with the take rate alone:

```
D = (1 + g(V)) × (m1 − m0) / m0
```

Here m0 and m1 are the take rate in the first and the second year. When the take rate is steady, D is zero and revenue grows exactly as fast as the commerce. When the take rate rises, D is positive and revenue grows faster than the commerce.

Tokopedia shows how this works. Between 2022 and 2023 its take rate rose by about 68 percent while its transaction value fell by about 9 percent. Its revenue grew by about 53 percent even though sales fell, and growth divergence was 62 points.

The wedge and growth divergence do different jobs. The wedge follows the commerce. Transaction value is far larger than revenue, so the wedge is almost all of transaction value and moves with it. Growth divergence follows the take rate and shows whether revenue remains a fair guide. The wedge has a second use. Its size next to revenue decides how far a change in the take rate swings revenue growth. Take a platform that keeps 2 percent of each sale, with an ecosystem ratio of 49. If transaction value is flat, a one-point rise in its take rate lifts revenue growth by about 50 points. A platform that keeps 17 percent has an ecosystem ratio near 5, and the same one-point rise lifts its revenue growth by about 6 points. A large wedge means more than a large gap in level. It also means that ordinary changes in fees or discounts can swing reported growth.

## 3.2 Hypotheses

Two hypotheses put the two links of the chain to the test. H1 concerns the inner link, between revenue and the commerce a platform carries. H2 concerns the outer link, between that commerce and national online commerce.

Revenue depends on the take rate, and the take rate depends on fees, on discounts and on how the platform's accounts treat each sale. A platform that cuts its discounts keeps more of each sale and reports more revenue without any more commerce. Revenue is a fair stand-in for the commerce only while the take rate is steady, which means that growth divergence stays close to zero. The first hypothesis states that case.

> **H1.** Transaction value and revenue recognized by the same platform grow in proportion over time.

H1 is tested by comparing growth divergence among Indonesian platforms with growth divergence among listed platforms abroad, where revenue and transaction value broadly move together. Chapter 4 describes both groups.

National online sales can grow in two ways. Existing businesses can sell more, or more businesses can start selling online. BPS reports both the number of businesses selling online and their total online sales, so national growth can be divided between the two. Growth from new sellers can take place in channels that platform records do not cover, such as messaging and social media, which most sellers use. Platform figures can miss that growth even when every platform reports accurately.

> **H2.** The growth of national e-commerce value comes mainly from more businesses selling online, and less from higher sales per business.

The H2 split is arithmetic. It does not say which channels the new businesses use, or whether they are new.

## 3.3 The entry test

The split in H2 rests on BPS's count of online sellers. A count can rise for two reasons: more businesses start selling, or the survey reaches businesses it did not reach before. The published figures cannot tell these apart. The survey itself can, because it asks every seller in which year it began selling online.

If a rise in the count comes from first-time entry, a large enough share of sellers must have started in the year of the rise. For 2023 the published count rose by 27.4 percent. Even if no seller had stopped, new sellers would then have to make up at least 21.5 percent of all sellers. The test was written down before the survey files were opened, and Chapter 4 gives the rule. It does not test H2 itself. It tests what "more businesses" means.

If the share of new sellers falls short, part of the rise is something other than first-time entry. Two readings are open: the survey reached more of the sellers who were already there, or sellers came back after a pause. Chapter 5 weighs them.

## 3.4 Further analyses

Two further analyses support the hypotheses without forming hypotheses of their own. The first divides national growth by sales channel, to show how much of it took place inside the marketplace channel. The second compares marketplace sellers with other sellers on whether they keep financial statements, which bears on what platform records can add to tax administration. A third analysis, developed in Chapter 6, estimates how many sellers a rule based on platform records can reach.

## 3.5 The tests together

Table 3.2 pairs each test with the result that would count against it.

**Table 3.2. Tests and what would count against them**

| Test | What it asks | What would count against it |
|---|---|---|
| H1: growth divergence | Do revenue and transaction value grow together within a platform? | Growth divergence in Indonesia far larger than among listed platforms abroad |
| H2: split of national growth | Does national e-commerce value grow because of more businesses or because of higher sales per business? | Higher sales per business accounting for most of the growth |
| Entry test | Does a rise in the seller count come from first-time entry? | Fewer new sellers than the rise requires, so that the count reflects more than first-time entry |

The first two rows test the hypotheses. The third row sits beside H2, because it tests what the count of businesses in H2 represents. Chapter 4 describes the data behind each test.
