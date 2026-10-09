# Complementary contribution for Claude — 8 October 2026

This is the next contribution after [REVIEW.md](REVIEW.md) and [NEXT_STEPS.md](NEXT_STEPS.md). The earlier review has already been incorporated through dated groundwork revisions. This pass preserves the approved proposal, sample-decision boundaries and preregistration. It writes only new files in this review folder.

## Read first

- [RESULTS_INSERTS.md](RESULTS_INSERTS.md): six draft passages for the existing framework, methods, results, literature and discussion. They include checked numerical wording and scope/source notes. They are working inserts, not a newly designated manuscript.
- [CONCEPT_AND_LITERATURE_AUDIT.md](CONCEPT_AND_LITERATURE_AUDIT.md): support for those passages, exact identities, original-report reconciliation, and a primary-source literature map.
- [measurement_checks.json](measurement_checks.json): full precision, input hashes and check results; [growth_bridge.csv](growth_bridge.csv) gives the transition-level bridge.

## Material findings to carry into drafting

| Item | Completed check | Suggested action |
|---|---|---|
| Tokopedia incentive contribution | Full annual-report values give 60.5614%, rounding to the proposal's 60.6%. The later 60.5% comes from rounded inputs. | Use 60.6% in final prose; preserve both existing input vintages and record the source-precision reconciliation. |
| Growth decomposition | Exact ordinary growth includes an interaction; exact log growth adds. Existing numerical code is correct. | Keep the framework's additive statement in logs, or state the ordinary-growth interaction in the appendix. |
| Main growth-gap summary | 38.9 versus 7.1 is the median absolute gap. | Retain “absolute” in the sentence and caption. Do not attach the expanded test's p-value. |
| Two-thirds movement statement | The existing statistic uses absolute component magnitudes, then a transition median. | Define its denominator. Avoid interpreting it as a causal fraction or a share of net growth. |
| Closest literature | UNCTAD already compares business e-commerce statistics and platform transaction values. Givoly's public notes exclude technology KPIs. De Franco concerns comparability; Hummels–Klenow concerns export varieties. | Position the contribution around the connected Indonesian evidence and source reconciliation. Match each reference to the claim it actually supports. |
| Connection between the circles | Retained share and covered commerce share are distinct conditions. Offsetting changes can produce matching headlines. | Use the plain discussion insert. Do not multiply constructed issuer and BPS ratios into a national estimate. |
| Incentive accounting | IFRS customer-payment treatment has a distinct-good/service exception; issuer-specific treatment matters. | Lead with the disclosed deductions and cite the standard as accounting background. |

## Reproduce

```bash
python3 research/independent_review_2026-10-08/measurement_checks.py
```

The script uses Python's standard library plus Poppler's `pdftotext`. It checked all 52 existing transition rows and both saved movement-share summaries. This count covers separate tiers; it is not a new sample N. It also asserts the source values on the annual-report pages and the reconciliation to the existing Tokopedia transition. No hypothesis-test verdict changes.

## Integration boundary

Use the frozen groundwork's dated-note process for adopted changes. Leave the proposal's title, question and hypotheses intact. This pass does not claim that the entire bibliography has been checked, global novelty established, or formal expanded-sample approval received. The literature audit identifies what was actually read and what still requires full-paper comparison.
