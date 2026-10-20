# H2 coverage-adjusted scenarios — 16 October 2026

## Why this note exists

The 15 October thesis draft reports that H2 holds on BPS's published figures: 2022–2023 online sales value grew by about 40.6%, while the published number of online sellers grew by about 27.4%. Under the thesis's log decomposition, the extensive margin contributes about 71% of the published value growth.

The same draft's registered entry test then shows that the published rise in the seller count cannot be explained entirely by first-time entry. The threshold required for the published 27.4% rise is 21.5% of 2023 sellers beginning to sell online in 2023; the survey gives about 13.45%. The post-test cohort accounting estimates that 306,000 to 458,000 of the 2023 seller count is not explained by first-time entry, depending on the exit assumption.

This note asks the natural follow-up: **does H2 still hold if that unexplained count is treated as additional survey coverage rather than genuine net entry?**

This is a scenario analysis. It does not overwrite the registered H2 result, and it does not establish that the unexplained sellers are definitely a coverage break. Returning sellers remain an alternative explanation in the survey files.

## Inputs

Use the same published figures and accounting already used by the thesis:

- 2022 BPS online sellers: **2,995,879**.
- 2023 BPS online sellers: **3,816,750**.
- 2022–2023 BPS online-sales-value growth: **40.6%**.
- Unexplained seller count, no-exit scenario: **306,000**.
- Unexplained seller count, 5%-annual-exit scenario: **458,000**.

The thesis defines H2 using the exact log split

`Δln(Y) = Δln(N) + Δln(Y/N)`

and says H2 holds when `Δln(N) / Δln(Y) > 0.5`.

## Published-count result

With the published seller count:

- seller-count growth = `3,816,750 / 2,995,879 - 1` ≈ **27.4%**;
- extensive-margin share = `ln(3,816,750 / 2,995,879) / ln(1.406)` ≈ **71.1%**.

So **H2 holds on the published BPS series**, as the current draft states.

## Coverage-adjusted scenario A: remove 306,000 sellers

Treat the minimum unexplained count as additional survey coverage:

- adjusted 2023 seller count = `3,816,750 - 306,000` = **3,510,750**;
- adjusted seller-count growth = `3,510,750 / 2,995,879 - 1` ≈ **17.19%**;
- extensive-margin share = `ln(3,510,750 / 2,995,879) / ln(1.406)` ≈ **46.54%**.

Under this scenario, **H2 does not meet its >50% criterion**.

## Coverage-adjusted scenario B: remove 458,000 sellers

Treat the larger unexplained count, which allows for about 5% annual seller exit, as additional survey coverage:

- adjusted 2023 seller count = `3,816,750 - 458,000` = **3,358,750**;
- adjusted seller-count growth = `3,358,750 / 2,995,879 - 1` ≈ **12.11%**;
- extensive-margin share = `ln(3,358,750 / 2,995,879) / ln(1.406)` ≈ **33.55%**.

Under this scenario, **H2 again does not meet its >50% criterion**.

## Interpretation

The important result is not that H2 was "wrong." The registered/descriptive result and the coverage-adjusted scenarios answer different questions.

1. **Published-series reading:** using BPS's published counts as printed, more businesses account for about 71% of 2022–2023 online-sales-value growth, so H2 holds.
2. **Entry-test reading:** the seller microdata show that first-time entry cannot produce the whole published increase in the count.
3. **Coverage-adjusted reading:** if the unexplained 306,000–458,000 sellers are treated as additional survey coverage, the extensive-margin share falls to about **47%–34%**, and H2 no longer passes its own >50% threshold.

This strengthens the thesis's measurement argument. A conclusion about the source of national e-commerce growth changes when the link between the survey count and genuine seller entry changes. That is the outer-link analogue of H1: a proxy can look stable until the mechanism connecting it to the activity being represented changes.

## Claim boundary

Do **not** write that the adjusted counts are the true number of sellers or that BPS's published totals are wrong. The files do not identify the same businesses across rounds. They cannot rule out sellers who stopped and later returned, and the 306,000–458,000 accounting is exploratory.

The supportable claim is:

> H2 holds on BPS's published series. But under either scenario that treats the seller count not explained by first-time entry as additional survey coverage, the extensive margin falls below half of 2022–2023 sales-value growth. The conclusion about what drove growth therefore depends on whether the published rise in sellers represents genuine entry or a change in who the survey reached.

## Evidence label and manuscript placement

- Keep the original H2 result labelled as it is in the current thesis.
- Keep the registered entry test separate and report its failure unchanged.
- Label this coverage-adjusted H2 calculation **exploratory**, because it is a follow-up prompted by the failed entry test.
- Add the arithmetic after the entry-test result in Sections 5.6–5.7, not as a retroactive change to the registered hypothesis.
- In Section 7.1, replace any unqualified statement that "H2 holds" with the two-level result: it holds on the published series, but not under either coverage-adjusted scenario.
- Preserve returning sellers as the main competing interpretation.

## Reproducible arithmetic

```python
import math

n_2022 = 2_995_879
n_2023 = 3_816_750
sales_growth = 0.406

for unexplained in (306_000, 458_000):
    n_adjusted = n_2023 - unexplained
    seller_growth = n_adjusted / n_2022 - 1
    extensive_share = math.log(n_adjusted / n_2022) / math.log(1 + sales_growth)
    print(unexplained, n_adjusted, seller_growth, extensive_share)
```

Expected results:

| Scenario | Adjusted 2023 sellers | Seller-count growth | Extensive-margin share | H2 (>50%) |
|---|---:|---:|---:|---|
| Published count | 3,816,750 | 27.4% | 71.1% | Holds |
| Remove 306,000 | 3,510,750 | 17.19% | 46.54% | Does not hold |
| Remove 458,000 | 3,358,750 | 12.11% | 33.55% | Does not hold |

## Source state

This note is based on the 15 October 2026 thesis reading copy and the full thesis audit reviewed on 16 October. It is an analysis note for integration into the next manuscript pass; it is not itself a replacement manuscript or a change to the preregistration record.

## Dated correction, 18 October 2026

The scenarios above remove the unexplained sellers from the **count only**. Their sales stay in the 2023 total. If the extra sellers are wider survey coverage, their sales were added too, so the consistent treatment removes both.

The thesis branch (`claude/happy-pascal-uc2eya`, PR #10; `research/option_space_2026-10-01/h2_coverage_adjusted.py`, `tables/h2_coverage_adjusted.json`) reports both treatments. Recomputed here from its inputs (V22 = Rp783.0tn, V23 = Rp1,100.87tn, the same seller counts):

| Scenario | Count only | Count and sales removed |
|---|---:|---:|
| Remove about 306,000 sellers | 46.6% | 53.3% to 54.5% |
| Remove about 458,000 sellers | 33.6% | 41.5% to 43.0% |

The thesis reports the consistent version: under wider coverage, H2 sits on its 50% threshold. It is no longer a clear "does not hold". The count-only rows above stay valid as arithmetic, but the claim boundary and the suggested wording in this note should not be used. Use the thesis wording (Table 5.1, Sections 5.7 and 7.1, abstract). The calculation stays exploratory.
