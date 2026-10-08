# Independent review and contribution — 8 October 2026

Prepared for the researcher and for Claude's next session. This is a review package, not an adopted sample decision or a manuscript revision. It preserves the approved title, question, hypotheses and Indonesia geography. The baseline examined is commit `b517f8e3b9416493ca1b77295d92b26748900f23`; the proposal is `papers/current/Invisible_Ledger_Proposal_FINAL_2026-09-27.pdf` and the October groundwork is `research/option_space_2026-10-01/`. Nothing in the frozen groundwork or preregistration was edited.

**Assessment.** The repository contains enough completed work to begin the full manuscript. Its strongest contribution is showing when an economic conclusion changes because the measure changes, and explaining the change where the source permits. The remaining work is largely synthesis and qualification. A few interpretations still depend on assumptions the available data cannot settle. Those are boundaries to state, not reasons to rebuild the thesis concept.

**Review standard.** Absence from the manuscript does not establish absence from the research. Check source documents, extracts, scripts, generated tables, local licensed inputs and historical notes before calling work missing. Distinguish completed and incorporated, completed but not incorporated, present but unverified, unresolved, and not located. A historical note may contain a useful qualification without becoming the authority for a current sample or result.

**What was verified.** The October `rebuild_all.sh` completed in an isolated copy. All 272 rows across its twelve claims ledgers passed. Rebuilt committed tables and exhibits matched the repository files byte for byte. The current-artifact and repository-structure validators passed. Then seven BPS scripts and the market-value script were rerun from the local licensed inputs. All eight JSON results matched their saved outputs. Script and input hashes are in [raw_verification.json](raw_verification.json). The verification used the original analytical code; it does not independently validate questionnaire interpretation, survey design, or economic attribution. World Bank and event-return analyses were not rerun from raw inputs in this pass.

**The work already present.** Scope tiers, firm summaries, permutation tests, bootstrap checks, alternative BPS counts, bracket scenarios, cohort checks, channel checks, province checks, exit sensitivity, sampling-error sensitivity, market regressions, and failed tests are already implemented. The earlier [contribution-bridge methods note](../contribution_bridge/METHODS_AND_LITERATURE.md) also explicitly distinguishes financial-statement ownership from absence of tax or other records. Some concerns are about carrying this existing work into the final wording.

## 1. A completed new check strengthens H1

The expanded H1 script treats Tokopedia and GoTo on-demand as separate firm labels. Their shared issuer prompted a sensitivity check, not a conclusion that the reported result was invalid. I repeated the comparison after giving their issuer one summary value.

Two summaries are reported. One takes the median across the issuer's observed segment transitions. The other averages its segment medians, giving each segment equal weight. Neither adds transaction values across scopes. Both retain the 27 foreign reference firms and the existing absolute annual change in log take rate.

| Summary rule | Target units | Reference units | Mann–Whitney, one-sided p | Exact permutation, median-difference p |
|---|---:|---:|---:|---:|
| Existing five segment labels | 5 | 27 | 0.00382 | 0.02138 |
| Four issuer summaries; pooled transition median | 4 | 27 | 0.00299 | 0.00699 |
| Four issuer summaries; equal segment weight | 4 | 27 | 0.00299 | 0.00699 |
| Three main series; expanded foreign benchmark | 3 | 27 | 0.00764 | 0.01330 |

Source: [results.json](results.json), `h1_issuer_sensitivity`. Full-precision inputs reproduce the original five-label Mann–Whitney result before any grouping. Exact enumeration replaces the original expanded script's Monte Carlo permutation calculation; its small difference from the saved permutation p is expected.

**Interpretation.** Shared-issuer grouping does not remove the expanded result under either declared summary. My earlier independence concern is now partly answered by a completed check. The wider evidence remains supportive. It still includes regional scope, estimated GoTo 2022 GTV, heterogeneous businesses and unequal time coverage. Grouping is a robustness summary, not a fitted dependence model or proof of population representativeness.

**A useful additional distinction.** The main sample's reported p of about 0.06 concerns absolute growth divergence against the original eight-firm benchmark, using the mean of firm medians as the permutation statistic. The new table uses absolute log take-rate changes against 27 reference firms. These are different metrics, reference sets and statistics. They should not be narrated as conflicting verdicts on the same test. Both mean-difference and median-difference exact permutations are saved; neither is universally the "strictest" test.

Recommendation: keep the approved H1 and its case evidence. Use benchmark tests to substantiate relative divergence. Do not interpret them as an Indonesia treatment effect. The new sensitivities are post-result review checks and belong in the robustness record if adopted.

## 2. BPS entry and coverage need a returning-seller term

The existing accounting finds an increase of about 819 thousand estimated sellers, about 513 thousand first-time entrants, and a residual of about 306 thousand. These quantities were reproduced from the licensed inputs. The existing exit scenarios are also reproducible.

One possible process is not represented in the existing exit-only accounting: a seller who first sold online before 2023, was inactive in 2022, and returned in 2023. The seller retains an old start year. That can increase a past-start-year cohort without a change in survey coverage. This is an identification possibility, not evidence that it happened at any particular rate.

The accounting can be written:

`change in estimated active sellers = first-time entrants − exits + returning sellers + residual`

The residual absorbs coverage, weighting, classification, recall and sampling differences. Attributing all of it to coverage requires assumptions about the other terms.

| Existing exit assumption | Returning sellers needed to remove the residual | As a share of the estimated 2022 active count |
|---|---:|---:|
| No exits | About 306 thousand | 10.20% |
| Half the reference exit rate | About 382 thousand | 12.74% |
| Reference exit rate | About 458 thousand | 15.29% |

Source: [results.json](results.json), `bps_returning_seller_sensitivity`. These are scenarios. They are not observations, confidence intervals, or estimates of the dormant seller stock. A fuller assumption grid is saved, including negative residuals rather than silently clipping them.

**Interpretation.** This calculation makes the alternative explanation testable in scale: erasing the coverage residual requires a substantial returning-seller flow under these assumptions. The repository does not establish whether that flow is plausible or implausible. The lack of linked business histories prevents direct separation. The channel and province checks continue to support investigating a coverage change; this sensitivity does not erase them.

Recommendation: lead with the observed finding that first-time entry alone does not account for estimated count growth. Present the 37–56% coverage attribution as conditional on the existing exit assumptions and no returning-seller contribution, alongside the other survey boundaries. The later-wave RSE calculation remains a sensitivity, not a directly estimated design-based standard error for the earlier residual. Keep H2's published arithmetic result separate from causal entry.

## 3. A worse typical seller and growing total sales can coexist

The repository already acknowledges that the reported growth of existing sellers is seller-weighted, while revenue amounts needed for value weighting are unavailable in the 2024 file. This is an existing limitation. My contribution is a reproducible demonstration of its implication.

A synthetic example has nine small sellers and one large seller. Four small sellers decline, five remain unchanged, and the large seller grows. It is constructed to reproduce the observed negative seller-weighted mean and flat median while total sales grow by 40.6%. The inputs are invented; this is not a reconstruction of BPS businesses or its published total.

The example passes checks on the mean, median, aggregate growth and positive sales levels. Its complete values and classification are in [results.json](results.json), `synthetic_seller_growth_example`.

**Interpretation.** A negative seller-weighted mean and flat median do not logically contradict positive aggregate sales growth. They answer different economic questions. This does not establish that concentration explains the actual increase. It establishes that the reported seller distribution alone cannot reject that increase.

Recommendation: describe the typical seller's experience and aggregate sales as separate results. Say the available microdata do not reconcile the aggregate increase, not that the aggregate is disproved by the typical seller's report. A claim that the remaining value increase is unexplained should keep its bracket and size-proxy assumptions attached.

## 4. Market evidence has two different jobs

The market-value regression is implemented, its local raw-input reproduction matched, and the unsuccessful main coefficient-difference test is openly reported. That is completed work.

The descriptive comparison of multiples has an exact identity:

`change log(MV/R) − change log(MV/V) = −change log(R/V)`

Market value cancels. A larger fall in the revenue multiple than in the transaction-value multiple follows from a rising take rate, regardless of the market-value path. This comparison illustrates denominator sensitivity; it is not independent evidence that investors prefer transaction growth.

The regression provides the separate association evidence. Its main coefficient-difference p is about 0.20. The positive volume association does not establish predictive superiority over revenue, a causal valuation response, or that investors ignored take-rate growth. The registered operational prediction failed; that is not proof the underlying coefficients are equal.

There is another measurement boundary: market-capitalization change includes share-count change. It is not stock return. Existing event-return scripts address a separate exploratory question; no claim is made that stock-return work is absent. Do not describe the market-capitalization regression as completion of precisely the same stock-return estimand promised in the proposal's later extension.

Recommendation: keep the association result and its unsuccessful comparison. Use the multiples illustration to explain denominator choice. Preserve the distinction between market value, stock return and causal response.

## 5. My perspective on the thesis story

The two main layers are connected by the question, but their mechanisms differ. A take-rate change is a real change in the platform's retained revenue share. A survey-coverage change alters which activity enters an estimate. Both can change the growth story, but the first is not merely a counting error. Revenue can accurately describe the platform's own income while answering a different question from transaction value.

The most useful contribution is to state the substitution assumption and then show when it fails. Revenue can stand in for transaction growth while the take rate is stable. Platform commerce can describe broader online commerce only while the covered channels and their shares support that use. Counts from repeated surveys can describe entry only after other changes in participation and estimation are addressed. Each link has its own evidence; no single omnibus test validates the whole chain.

The thesis can be written around three substantive results: the transaction–revenue separation with source-backed mechanisms; the wider national participation and channel evidence; and the limits of reconciling those views. Policy reach and market evidence explain relevance. They do not need to become additional competing thesis claims.

A smaller statistical result is not automatically a failed thesis contribution. Even without a country-wide effect, a source-auditable case in which revenue and sales imply opposite growth directions matters. The external benchmark strengthens the scale comparison. The accounting reconciliation makes the case intelligible.

Similarly, H2 remains informative when its interpretation becomes more careful. Published growth attributed to the estimated number of businesses is not equivalent to demonstrated growth through first-time entry. Explaining that distinction extends the promised reconciliation work without changing the approved hypothesis.

## For Claude's next session

Read this note, [results.json](results.json), and [raw_verification.json](raw_verification.json). Reproduce the new exploratory calculations with:

```bash
python3 research/independent_review_2026-10-08/review_checks.py
```

Carry the existing financial-statement/tax-record distinction into the current wording. Consider the issuer sensitivity for the appendix. Decide how to qualify the coverage attribution and the market interpretation. Preserve the frozen preregistration; any adoption of these checks should be recorded as a dated post-result addition. No final sample choice has been approved or rejected by this review, so `docs/CURRENT_STATUS.md` was not changed.
