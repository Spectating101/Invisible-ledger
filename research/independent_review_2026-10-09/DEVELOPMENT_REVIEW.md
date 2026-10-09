# Review of recent development — 9 October 2026

Reviewed baseline: `914bb3b`, full SHA recorded in [recent_checks.json](recent_checks.json). Comparison begins at `fec5a46`, the first handoff integration on 8 October. The working tree was clean before this review. The September 27 proposal remains active; the new story draft is a working narrative layer. This review adds separate files and changes no frozen groundwork, narrative arc, pitch, sample decision or preregistration.

## Assessment

The project has advanced in substance as well as presentation. A complete story draft now connects the issuer evidence, national seller evidence and relevance to readers. New analyses explain the scale of H1's relative divergence and examine the returning-seller alternative. The reference work has also incorporated the earlier audit's limits.

The strongest new contribution is the distinction between an absolute change in the retained share and its relative effect on revenue. This gives the thin retained share an economic role in explaining growth divergence. The story is now easier to defend as a connected measurement study. It still needs claim-level repairs before its strongest sentences can be used in the full thesis.

## What changed

| Development | Evidence now present | Assessment |
|---|---|---|
| Full narrative | [DRAFT_STORY_v1.md](../option_space_2026-10-01/DRAFT_STORY_v1.md), [NARRATIVE_ARC.md](../option_space_2026-10-01/NARRATIVE_ARC.md), [GOLDEN_PITCH.md](../option_space_2026-10-01/GOLDEN_PITCH.md) | The move from public growth claims to underlying accounts and seller answers works. The story draft and evidence map are concrete progress; chapter writing can draw on them. |
| Thin-share explanation | `h1_points_vs_log.py`, its saved output and dated notes | A useful exploratory result. Comparable median changes in percentage points can produce different relative changes when retained shares differ. |
| Seller profile | `bps_newly_counted_profile.py`, saved aggregate profile and stable-period comparison | Supplies evidence on which groups account for the larger estimated count. It is a difference of weighted counts, not identified people newly found by the survey. |
| Returning-seller diagnostic | `bps_returning_check.py`, saved month-of-selling totals | A reasonable follow-up to the open alternative. Month questions and cohort definitions differ; the check remains diagnostic. |
| Earlier independent contribution | Commit `f0ed92e`, working reference list, draft evidence map | Both contribution packages are committed. The exact Tokopedia incentive percentage, movement-share definition, absolute divergence distinction and citation-use limits have been carried into the drafting materials. |
| Reference follow-up | [REFERENCES_WORKING.md](../option_space_2026-10-01/REFERENCES_WORKING.md), latest commit `914bb3b` | A usable working list now exists. It is not yet a complete formatted and claim-verified submission bibliography. |

## Independent verification

- Ran the full public-input rebuild in an isolated Git archive. All **272 rows across twelve claims ledgers pass**.
- Compared **163 tracked table/exhibit files** in the rebuilt copy against baseline `914bb3b`: **no byte differences**. The count includes preserved inputs and licensed aggregates; it does not mean every file was regenerated from raw data.
- Reran both new BPS scripts from the local licensed files. Both JSON outputs match the saved results exactly. Input and script hashes are recorded in [verification.json](verification.json).
- Independently reconstructed the point/log comparison under both foreign-sample selections and checked the exact growth identity on the eight core transitions.
- Added common-start-year checks to the returning-seller diagnostic using the licensed inputs. National aggregates only are saved in [recent_checks.json](recent_checks.json).
- The active proposal/deck validator passes: the proposal hash and presented deck remain unchanged.

Reproduction validates the execution and saved outputs. It does not itself validate survey identification, source-definition equivalence, or causal interpretation.

## 1. The thin-share explanation survives a sample check

The new point/log script uses **26 foreign firms**, while the existing expanded H1 comparison uses **27**. The difference is Ozon. Its 2022 endpoint passes the existing current-year screen, but its 2021 endpoint is excluded for a high own-goods revenue share. The new script reconstructs transitions after filtering levels, so Ozon contributes no qualifying pair. This is a change in transition eligibility, not a missing calendar year.

I recomputed both metrics using the same rows within each selection:

| Selection | Target/reference firms | Median absolute retained-share change, points: target/reference | Median absolute log change: target/reference | One-sided point/log p |
|---|---|---|---|---|
| Original current-endpoint rule | 5 / 27 | 1.006 / 0.991 | 0.201 / 0.062 | 0.693 / 0.00382 |
| Both endpoints screened, as in the new check | 5 / 26 | 1.006 / 0.978 | 0.201 / 0.060 | 0.652 / 0.00300 |

Source: [recent_checks.json](recent_checks.json). The original row reproduces the expanded H1 log p-value. The second reproduces the new script. Shared-issuer grouping remains an existing separate sensitivity, not performed by this table.

The descriptive reading survives: the median point changes are very close, while relative changes differ. Label the two samples, or present the comparison on a common selection. A non-significant point-change test does not establish statistical equivalence. Similar pooled medians also do not quantify how much of the relative gap is caused by starting shares; business model, scope, mix and period remain relevant.

The plain contribution can be: **“A small retained share helps explain why modest changes in that share move revenue so much.”** The observed changes are changes in `R/V`. Issuer reconciliations establish when those changes arise from incentives, fees or business mix. The comparison alone does not turn every take-rate change into an identified fee change.

## 2. Repair the exact identity in the new explanation

The new script's documentation, the narrative arc and the cut-list note state `D = change in m / m`. For the proposal's ordinary growth definition, the exact relation is:

`D = (1 + gV) × (m1 − m0) / m0`

Here gV and D are fractions; multiply D by 100 for percentage points. The version without the transaction-growth factor is exact when transaction value is unchanged. The exact additive decomposition remains `Δln R = Δln V + Δln m`.

For Tokopedia, take-rate growth is 68.16%, but D is 62.10 percentage points because transaction value fell. All eight core transitions satisfy the correct formula. This is an explanatory repair: the existing numerical calculations are correct.

The amplifier is the inverse starting take rate, `1/m0 = 1 + E0`, together with the transaction-growth factor. The wedge in currency units alone does not determine the amplification. This preserves the proposal's measures and the new intuition.

## 3. The month check survives common start-year cutoffs

The new script compares sellers who started by 2021 in the 2022 activity file with sellers who started by 2022 in the 2023 activity file. Those are different groups. This explains why its established-seller totals rise by more than the previously reported residual.

Using the same start-year cutoff in both files gives:

| Sellers started online by | Part-year sellers in 2022, thousands | Part-year sellers in 2023, thousands | Weighted share in 2022 / 2023 |
|---|---:|---:|---|
| 2020 | 378.1 | 252.3 | 17.8% / 11.2% |
| 2021 | 472.0 | 318.1 | 18.4% / 11.8% |
| 2022 | 737.5 | 402.7 | 24.6% / 12.2% |

Source: [recent_checks.json](recent_checks.json). No zero-month cases or missing start years occur in these files under the current parser. The source question still changes from a month list to twelve flags. The final row also includes businesses newly entering in 2022, so maturation into full-year selling is relevant there.

The decline survives alignment and is useful supporting evidence. It does not identify returning flows. Returning sellers who resume during the year could be offset by exits of earlier part-year sellers or by incumbents moving into full-year selling. January returns are another possibility. Without linked histories, the net change cannot exclude these gross flows.

Closest supported wording: **“Part-year selling fell even when we compared the same start-year groups.”** Keep the explanation as a diagnostic and retain the returning-seller sensitivity. It improves the response to that alternative; it does not close it.

## 4. Repair the fresh story's certainty without losing its voice

The earlier backend qualification is present. These are places where the new prose makes a different claim; they are not missing research modules.

| Draft location and wording | Difference in claim | Closest supportable wording |
|---|---|---|
| B2: “The rest goes to the sellers, drivers and shops.” | `V−R` does not identify participant payouts. Definitions include other components, and incentives affect net revenue. | “The rest sits outside the platform's reported revenue.” |
| B7: “The gap is far too large to be sampling chance.” | The later-wave RSE exercise is a sensitivity with assumptions; it does not directly estimate the earlier seller residual's design variance. | “The gap remains large in the sampling-error scenarios we checked.” |
| B7–B8: “about half a count that reached further”; “They had been there all along.” | The data establish a non-first-entry residual and its group profile. They do not identify the same businesses across rounds or settle returns, weighting and coverage separately. | “About half the rise is not explained by first-time entry.” Then: “The larger count was concentrated among older, long-running chat and social businesses.” |
| B9: “Neither is [wrong].” | Different scopes can explain disagreement; neither complete levels nor every measurement error has been reconciled. | “The offices measure different parts of online selling.” |
| B-C: one start-year question is “enough to test it.” | It can test whether first-time entry alone accounts for the count increase, not identify survey coverage stability. | “The start-year question tests whether first-time entry explains the increase.” |
| Closing line: “every number read [2023] as a boom” | The draft itself reports several declining buying measures. | “the headline growth figures described a boom” |

The required limitations can remain in their designated chapter. These sentence changes state the result itself correctly; they do not require caveats in every paragraph.

The profile also needs its existing coding note: the 2023 education-code mapping is inferred in the script. Net-surplus shares can exceed 100% when another group declines. Such shares describe contributions to a net difference, not the distribution of a directly observed group of newly found individuals. The stable-period control adds a conditional adjustment, not individual identification.

## 5. Reference progress is real, with one interpretation limit

The new Bowen, Davis and Rajgopal citation is verified in the [publisher record](https://onlinelibrary.wiley.com/doi/abs/10.1506/9728-4YG8-GC3L-FPFA): *Determinants of Revenue-Reporting Practices for Internet Firms*, Contemporary Accounting Research 19(4), 523–562 (2002). It is relevant background on grossed-up and barter revenue reporting. Its historical setting does not establish the current platforms' accounting choices.

Neter and Waksberg is verified in the [publisher record](https://www.tandfonline.com/doi/abs/10.1080/01621459.1964.10480699): *A Study of Response Errors in Expenditures Data from Household Interviews*, JASA 59(305), 18–55 (1964). Its experiment finds net forward telescoping in recalled household expenditures. That is support for a recall mechanism, not direct evidence of the direction of error in recalled online-selling start years. State the claim that the BPS entry shortfall is conservative as conditional on that direction of recall error.

The working bibliography is meaningful progress. Full claim checks, complete citation fields and final style still follow from the actual chapter text. The root status and artifact-routing documents lag the October narrative work; use dated file roles, not those old summaries alone, to assess completion. No new expanded-sample approval was located in the decision record reviewed here.

## Next useful step

Keep the narrative arc and the new explanatory insight. Repair the exact identity, align the point/log comparison's sample label, and adopt the common-start-year month check as an appendix sensitivity. Carry the claim repairs into the story before turning it into chapters. Then draft the empirical chapter in the proposal's structure, with the same evidence map and source notes.

The thesis now has a clearer answer to why its measures matter. Its remaining work is concentrated: preserve the exact meaning of the findings as the prose becomes more compelling, document sample decisions, and produce the full chapter artifact. Publication potential benefits from the more transferable explanation; the new analysis remains exploratory and does not create a country-wide causal result.
