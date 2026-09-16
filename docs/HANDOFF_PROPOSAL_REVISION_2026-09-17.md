# Handoff: Invisible Ledger proposal revision (16–17 September 2026)

Written by Claude (supervisor role) for Codex (editing role). Read fully before touching any file.

---

## 1. What we are doing

Revising the thesis **proposal** (not the thesis) for Christopher Ongko (王新福), YZU MS Finance, advisor Prof. De-Rong Kong (孔德蓉), oral examination 1 October 2026.

The goal now is **readability for any reader, including one with no finance/accounting background, without weakening the claim or introducing unsupported statements.** Structure and evidence are largely settled; the remaining work is line-level language quality ("taste") plus a small set of first-use explanations.

---

## 2. Where everything is

| Item | Location | Status |
|---|---|---|
| Repo | `/home/phyrexian/Downloads/Invisible-ledger` | branch `proposal/integrated-2026-09-16` |
| `main` | origin/main `1983584` | **stale — an earlier unapproved rewrite. Do not use or edit.** |
| Your "original" (Chris's download of `1ff9dfa`) | `~/Downloads/Inviledger Proposal Sept16.docx` | 13 pp, reference point |
| Claude R1 (whole-paper restructure) | commit `d34dfcf` on the branch | 15 pp, committed |
| **Current working tree** = R2 + previewed revisions 1–8 | uncommitted edits in `scripts/surgery/restructure_proposal_2026-09-16.py` | **This is the base. 14 pp, verified.** Built copy: scratchpad `…/scratchpad/integ/R3.docx` (Claude's local name; not Codex's "R3") |
| Figure 1 generator | `scripts/figures/figure1_ecosystem_ratio.py` (committed) | constructed series dashed/grey |
| Formatting | `scripts/finalize_proposal_format.py` | run after every build |
| Validator | `scripts/validate_docx.py` | |
| Astra/Sol outputs (audit inputs only) | `~/Downloads/Invisible_Ledger_Independent_Iteration_2026-09-16/`, `~/Downloads/Invisible_Ledger_Original_Based_Consolidation_2026-09-16/`, `~/Downloads/build_invisible_ledger_full_comparison.py` | **Do not use as a base** (see §7) |

**First action for Codex:** commit the current working tree as a checkpoint (e.g. `Checkpoint: R2 plus previewed revisions 1-8`) before editing.

### Build and verify

```bash
cd ~/Downloads/Invisible-ledger
export PYTHONPATH=/home/phyrexian/.local/lib/python3.13/site-packages   # HOME is overridden; required
S=<your scratch dir>
python3 scripts/surgery/restructure_proposal_2026-09-16.py <approved_f51331d.docx> $S/out.docx papers/current/figures/figure1_ecosystem_ratio_timeseries.png
python3 scripts/finalize_proposal_format.py $S/out.docx
python3 scripts/validate_docx.py $S/out.docx
cd $S && soffice --headless --convert-to pdf out.docx
```

The approved input DOCX is `f51331d:papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx`. Extract it with `git cat-file blob` through Python (a shell output filter corrupts binary `git show` output).

The script rebuilds everything from the Abstract to References using a `Writer` helper, then applies a **"previewed revisions 1–8" block** (whole-paragraph matches on the built document) just before the references/footnote section. For further line edits, the cleanest route is to extend that block with `revise_sub` / `revise_whole` / `delete_para`: each asserts exactly one match.

**Verification required before any commit:**
- page count (target 14)
- every table whole on one page (match caption and **last** row using a distinctive full-row string; single words like "Tokopedia" give false splits)
- no heading or caption stranded as the last line of a page
- figure aspect equals the image's pixel ratio
- every reference cited, and every citation resolving to a reference
- footnote present in the PDF
- visual check of changed pages
- CI gates in `.github/workflows/finalize-proposal-format.yml`, currently pages=15, tables=10, refs=32 — update the page gate to the real count

---

## 3. Chris's standing decisions (non-negotiable unless he changes them)

1. **Bold, not defensive.** He explicitly rejected a hedged "defensive" paper. Overclaim-and-defend-with-robustness is preferred over pre-emptive disclaimers. Don't hedge findings the data proves (e.g. Tokopedia's opposite movements happened; don't write "can").
2. **Research question verbatim:** "How much economic activity remains invisible when digital platforms are measured through their reported revenue?"
3. **Abstract opens** "Digital economy is measured through…" (no article, deliberate).
4. **Keep first person "I".** Kong's own reviewed draft used "I" and she never flagged it. His friend queried it; he decided to keep it.
5. **Proposal, not compressed thesis.** No results chapter; robustness stays proportionate.
6. **Previews before applying.** Show before/after for wording changes. He does not trust edits he hasn't read.
7. **Layout matters:** tables whole, no orphans, 12 pt body, Flashpoint-derived margins.
8. **No bridging to his separate digital-tax paper.** The practical contribution is not "calculate tax more accurately". PMK stays a brief institutional note.
9. **Kong's comments came from thesis iterations, not the proposal.** Apply the concern behind each one, not the literal instruction.

---

## 4. Kong's feedback: items that must stay satisfied

These are 40 comments across `Invisible_Ledger_Aug1426(1)_Kong.docx` (21) and `Invisible_Ledger_Sept0126_Kong.docx` (19). Current status: essentially all applicable ones are met. **Don't regress these:**

| Concern | What must remain |
|---|---|
| #107 abbreviations at first use | GTV, GMV, TPV, DJP expanded; BPS and Bank Indonesia described. **Still missing:** IFRS and QRIS expansions (approved to add) |
| #89, #114 is the proxy yours, and supported? | §3.1: Ecosystem Ratio constructed for this study, with its literature basis cited |
| #119, #125, #154 tables explained | every table and Figure 1 named and explained in prose (**keep "Table 4 gives each record a single role…"**) |
| #130, #178, #217 one term | GTV as the common label plus a footnote giving each issuer's actual label (GoTo GTV, Sea GMV, Blibli/Bukalapak TPV, Grab GMV/TPV) |
| #26 footnotes at page bottom | real footnote part exists; keep |
| #146 Momentum Works | **keep the justification** (Singapore-based research firm; used because no issuer discloses Shopee Indonesia) |
| #165 GDP share | 2.9% of US$1.371tn, in §5.1 only, as a magnitude comparison |
| #214 USD | no bare rupiah except the BPS Rp figure with its USD conversion |
| #88 finance references | De Franco (JAR), Berg (RFS), Barrios (JFE), Denes (JFE) |
| #2 abstract 100–150 words | currently ~207 — Chris accepted the overage |
| #153 Aug appendix with variables and sources | Appendix A: Table A1 variables, Table A2 sources |
| #153/#170 Sept GoTo | only the Tokopedia segment is used, never GoTo Group; scope stated |
| #0, #215 YZU template | unverified: template not available |

Kong's recurring pattern: define every term; stay consistent; state geographic/business scope (escalated sharply in September); explain non-standard sources; express findings at economic scale; avoid tax-gap framing.

---

## 5. His friend's assessment (Mei Fani): the confusions we are fixing

A careful reader with an accounting background, not a finance specialist. Her questions, in order, with roots and status:

| Her question | Root cause in the text | Status in current base |
|---|---|---|
| Why use "I"? Usually "this study / the author". | Style convention | **Kept by Chris's decision** |
| Isn't a gap obvious? Companies record service fees/commission. | Paper asserted substitution without showing it; E is just the inverse take rate | Fixed: E = 1/t − 1 stated; four records of 2023 shown on page 2; Tokopedia's opposite readings shown |
| Tokopedia was private before joining TikTok; does pulling data back years matter? Shopee reports at group level, not per country. | Tokopedia's 2-year window unexplained; construction under-explained | Fixed: window explained (2021 pair mismatched; combined under PT Tokopedia 31 Jan 2024; parent then reports a contractual fee); construction in §4.3 |
| Title sounds broad — "digital platform" could mean travel etc. | Scope named only on page 7; Grab isn't e-commerce; Blibli includes travel | Fixed: five platforms and roles named in Ch1; scope in §4.1 |
| We surface Tokopedia much more than Blibli, though data is small. | Tokopedia labelled "main anchor" with 1 transition; Blibli supplies the most data | Fixed: main sample = issuer-reported Tokopedia + Blibli + Bukalapak (11 platform-years, 8 transitions); Blibli 2024–25 added as a second reversal |
| Besides W = V − R, what else do you calculate? | W, E, D are all transformations of one (V, R) pair | Stated honestly; hierarchy to be sharpened (Codex rewrite 7 approved) |
| Are the formulas cited from prior articles? | Self-constructed | §3.1: constructed for this study; basis cited; not a new underlying quantity |
| After finding W, what is it used for? What's the contribution? | Purpose sat in §6 on page 11 and pulled toward tax | Fixed: Ch1 ends on measurement ("a statement about size is a statement about a record"); tax thread reduced |
| The company already has financial statements and tax reports — what's the difference? | The paper implied something was missing | Fixed: "Neither number is wrong: revenue records what the platform earned; transaction value what it carried" |

**Chris's own verbal misstatements to her** (context only; the document must never say these):
- "not recorded" — wrong; it is recorded, just outside the revenue line
- "BPS and company reports combined to get the gap" — wrong; W uses company filings only, and BPS is never an input
- "outside the company report" — wrong; both V and R appear in the same filing for the main sample
- "to calculate tax more accurately" — wrong for this paper
- "Indonesia is richer than recorded" — wrong; national accounts attribute merchant sales to merchants (SNA), and the paper's own §2.2 says so

---

## 6. How we got here

1. **Frozen ChatGPT version** (Ch1–2 approved by Chris, Ch3–8 frozen) → integrated with Kong fixes → spacing and orphan fixes → variable appendix (`1ff9dfa`, 13 pp).
2. **Whole-paper read** (Claude) found three structural problems that explained almost all of the friend's confusions:
   - the substitution error was asserted, never shown;
   - measurement and tax stories ran in parallel, with tax looking like the destination;
   - the sample and platforms appeared out of order, with two different headline numbers.

   Plus two examiner risks nobody had flagged:
   - **Grab's and Shopee's Indonesian ratios equal group ratios by construction.** Grab: group GMV 20,983 / revenue 2,359 − 1 = 7.895, identical to Table 5. Shopee's is 1/10% − 1 = 9.000.
   - **BPS and platform levels disagree ~3×** and the paper was silent about it.
3. **Claude R1** (`d34dfcf`): restructured the whole paper around those findings. It also introduced overreaches (see §7).
4. **Astra/Sol**: audited R1, built alternative candidates and a 72-page diff.
5. **Claude R2**: R1 plus astra's valid corrections plus a testable H4. **Then previewed revisions 1–8 applied** (precision fixes and compression) → 14 pp. That is the current base.

---

## 7. Astra/Sol: what to take, what not to

**Valid catches (all incorporated into the current base):**
- R1 converted BPS's multiple-response 32.74% marketplace share into "US$23.7bn". Wrong: that measure is not additive.
- R1 located non-marketplace growth in social media/messaging from 2023 shares. Shares don't allocate the 2023→24 increase.
- R1 claimed PMK's reach = BPS marketplace channel (1.5% of growth). Unverified: designated operators have not been mapped to BPS categories.
- "The share entering revenue is a reporting choice" — wrong under IFRS 15 (principal/agent follows control).
- "A platform keeping 2.5 percent" — revenue isn't money kept.
- "Activity outside revenue is still recorded" — overclaim.
- "Five platforms that publish usable figures" — false for Grab and Shopee.
- Blibli's reversal is not explained by Tokopedia's incentive reconciliation.
- R1's H4 ("different records give different accounts") couldn't fail.
- Payment growth also reflects adoption and substitution.
- Blibli's FY2020 prospectus pair belongs only to a separate sensitivity.

**Regressions (do not reintroduce):**
- H4 narrowed to a within-BPS channel comparison. That guts the central claim.
- The page-2 four-records demonstration removed; Ch1 made abstract again.
- Heavy hedging ("selected", "conditional", "not like-for-like", §6 "does not need to show all records are defective").
- Momentum Works justification cut (Kong #146).
- Table 4 explanation deleted (Kong #119/#125).
- "I" cut from 7 to 3 (against Chris's decision).
- "Systematically wrong conclusions" and "largest digital market in Southeast Asia" removed.
- Claimed the PMK 1 November 2026 date was unverified. **It is verified:** `docs/PROPOSAL_REBUILD_AND_AUDIT_2026-09-14.md`.

**Its genuine strength:** prose economy. The concise version fit the structure in 13 pp.

---

## 8. Pending work: rulings already made

### 8a. Codex's 13 "taste" rewrites: supervisor rulings

Standard adopted: *concrete before abstract; one sentence, one job; technical precision without bureaucratic prose; limitations stated once.* Added rule: **don't hedge findings the data proves.**

| # | Ruling |
|---|---|
| 1 Opening | **Revise:** "Substituting one for another changes the measured scale, growth and even the direction of digital activity." Keep the bold claim; drop "can"; "systematically" may go. |
| 2 100/10/90 | **Accept**, but keep "I call the difference the invisible wedge." |
| 3 Central distinction | **Accept**; "elementary" → "familiar". |
| 4 2023 comparison | **Reject.** Keep "processed" (not "were associated with"); no disclaimer list in Ch1. |
| 5 Constructed figures | **Accept** (named construction for Grab and Shopee). |
| 6 Opposite growth | **Accept** (contradiction first, 62.1-point gap later). |
| 7 W/E/D hierarchy | **Accept** (D carries the central test). |
| 8 Take-rate | **Accept.** |
| 9 H4 | **Split:** take the headline "Conclusions about the growth of Indonesian digital commerce change with the record used to measure it." Reject "economically consequential" (undefined threshold). Keep R2's falsification clause: *fails if revenue grows in step with transaction value within platforms and the marketplace channel grows in step with all e-commerce.* |
| 10 BPS levels | **Accept**; drop "or incomplete". |
| 11 Non-marketplace | **Accept**; use numbers (95.33% of businesses sell via instant messaging; social media 44.04% of value) instead of "important". |
| 12 Payments | **Accept** ("an independent view of digitalization"). |
| 13 Conclusion | **Revise:** don't open on a negation; start "Indonesia's digital economy is observed through…"; "disagree", not "can disagree". |

### 8b. Claude's novice-reader list: status after Codex review

Approved in substance (wording may follow the taste rulings):
- explain "recognizes as revenue" (commissions and fees)
- explain construction (see 8a #5)
- "neither record is in error; the error is treating either as the size of the digital economy"
- define g ("g is the percentage growth of a measure from one year to the next")
- explain BPS's two marketplace shares (18.2% exclusive split that sums to the total, vs 32.74% multiple-response measure)
- "moved in the opposite direction" (replacing "moved against it")
- expand IFRS 15 and QRIS
- gloss "Group level" (whole company) and "prospectus"
- plain statement that Shopee's and Grab's Indonesian ratios come from company-wide rates
- in the abstract: "the same transaction–revenue distinction" (not "same gap"; magnitudes differ)

Rejected or modified:
- **Rejected:** "98.5% of the increase … through social media, messaging apps and websites". Use: outside the marketplace category; BPS identifies those channels, but the comparison doesn't show which generated the increase.
- **BPS vs platform levels:** "not yet reconciled" is fine; don't cite "populations covered" as a cause.
- **H3:** financial statements indicate conventional business-level recordkeeping; don't say they determine what other records capture.
- **Blibli 2022 peak** ("low revenue base"): allowed, traceable to `outputs/empirical_robustness_2026-09-10/SUMMARY.md`.
- **62.1-point example:** a short standalone sentence in §5.1, not a long parenthesis.

Optional:
- a Years column in Table 2 (would shorten §4.1)
- a clause explaining the "Ecosystem" name
- standardize "marketplace channel" (the text currently mixes "component" and "channel")

**Output expected from Codex:** a compact editorial before/after for Chris, then apply, rebuild, verify, and commit to the branch. Target: stay at 14 pages.

---

## 9. Verified facts: use only these (with sources)

**Platform sample** (`outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_{levels,transitions}.csv`)
- Main sample (Tokopedia, Blibli, Bukalapak): 11 platform-years, 8 transitions; revenue faster in 6; opposite direction in 2 (Tokopedia 2022–23, Blibli 2024–25); median absolute gap **38.92 pp**; median signed gap 15.07 pp.
- Drop largest (Blibli 2022–23, +430.61 pp): 5 of 7, median 15.74. Leave one out: without Tokopedia 5/7; without Blibli 3/4; without Bukalapak 4/5 — at least one reversal each.
- All five (with Grab and Shopee): 17 / 12, revenue faster in 10, median absolute 42.02 pp.
- Growth rates are computed in native currency (recomputed and matched for all 12).
- Windows: Tokopedia 2022–23 (FY2021 period-mismatched); Blibli 2021–25 (FY2020 prospectus pair used only in the sensitivity; 3P includes tiket.com travel); Bukalapak 2020–23 Group, overseas activity, FY2024 excluded (9M vs 12M); Grab 2021–23 (GMV basis changed after FY2023); Shopee 2022–24.
- Tokopedia 2022–23: transaction value −8.90%, third-party net revenue +53.20%; 60.56% incentives / 39.44% gross revenue. Gap 62.10 pp.
- Blibli 2024–25: TPV −1.89%, net revenue +12.07% (components not reconciled).
- Blibli 2022 E peak (185) reflects a low net-revenue base (`outputs/empirical_robustness_2026-09-10/SUMMARY.md`).

**2023 cross-section** (`data/indonesia_fy2023/`)
- Grab V 5.381 / R 0.605 / W 4.776 / E 7.895.
- Tokopedia V 16.331 / R 0.405 / W 15.926 / E 39.296.
- Shopee V 21.520 / R 2.152 / W 19.368 / E 9.000.
- Total V 43.233 / R 3.162 / W 40.070 / ratio 13.7.
- Shopee rate 9–11% → wedge US$39.86–40.29bn. Excluding any one platform → at least US$20.70bn.
- Blibli 2023 at the same FX: W US$3.20bn, E 43.4. Bukalapak: W US$10.50bn, E 36.0.
- Tokopedia + Shopee V = US$37.85bn.
- Shopee 40% + Tokopedia 30% of 2023 marketplace GMV; Momentum market US$53.8bn (2023), 56.5 (2024).
- FX 15,236.88 IDR/USD and GDP US$1,371.17bn: World Bank WDI (PA.NUS.FCRF, NY.GDP.MKTP.CD) in `data/asean_context/asean_worldbank_context_2000_2025.csv`. 40.07/1,371.17 = 2.92%.

**BPS** (`data/bps_official/`, `docs/BPS_CROSSWAVE_CERTIFICATION_2026-09-10.md`)
- 2023 total Rp1,100.87T (US$72.25bn). Exclusive marketplace component Rp200.68T = 18.23% (US$13.17bn).
- 2024 total Rp1,288.93T; marketplace Rp203.58T = 15.79%.
- Growth 2023→24: total +17.08%, marketplace +1.45%, non-marketplace +20.57%; 98.46% of the increase outside marketplace.
- Businesses +15.31%; value per business +1.54%; count term 90.29% (70.95% under the alternative 2023 count 3,934,981 vs 3,816,750).
- Multiple-response (2023, **not additive; don't convert to USD**): marketplace 32.74% of value, social media 44.04% of value; businesses using instant messaging 95.33%, social media 33.29%, marketplace 17.80%.
- Recordkeeping: complete financial statements 28.63% (marketplace users) vs 12.25% (non-users).
- BPS value = online sales revenue of surveyed e-commerce businesses; differs from issuer GMV/TPV.

**Payments** (`outputs/payment_ledger_2026-09-11/`)
- 2023→24: e-money shopping +30.47%, mobile-banking payments/purchases +82.84%, QRIS +186.98% → 1.78×, 4.85×, 10.95× e-commerce.
- Economy-wide, not e-commerce-only.

**External panel** (`data/global_ecommerce/`)
- 48 matched observations, 8 firms (eBay, Etsy, Jumia, Mercado Libre, Rakuten, Sea, Shopify, Zalando), 2017–2025.
- 40 transitions, 29 clean-scope; revenue faster in 22 of 29; opposite direction in 4; median absolute 7.10 pp.
- Take rates: Shopify 2.4–3.1%, eBay 10.3–13.9, Mercado Libre 16.3–25.1, Zalando 69–75.

**Institutional**
- PMK 37/2025 implementation 1 Nov 2026 (`docs/PROPOSAL_REBUILD_AND_AUDIT_2026-09-14.md`).
- Tokopedia and TikTok Shop combined under PT Tokopedia 31 Jan 2024; GoTo then reports contractual revenue from Tokopedia (`docs/LAZADA_TIKTOK_ADMISSION_FEASIBILITY_2026-09-11.md`).
- Lazada and TikTok Shop: no matched Indonesian revenue series located.

## 10. Do NOT claim (unverified or wrong)

- Who BPS's survey frame covers (individuals, households, informal sellers). The 2023 methodology isn't archived; the 2024 PDF is image-only.
- Which channels generated the 2023–24 non-marketplace growth.
- PMK's coverage share, or any mapping of designated operators to BPS categories.
- GoTo's IPO date.
- Any USD value derived from BPS multiple-response shares.
- That the wedge is income, profit, a tax base, missing GDP or hidden activity; that either record is "wrong".
- That payment growth measures e-commerce growth.
- Causal statements (entry, formalization, incentive effects).

## 10a. Writing priorities and style (Chris's chosen standard — governs every edit)

Priorities, in order. When two conflict, the higher one wins.

1. **The argument survives.** Never cut or soften a sentence that carries the claim, the research question, or the explanation a reader needs to avoid misreading (e.g. "using its own definitions"). Word limits and page counts rank below this.
2. **True to the evidence.** Every statement traceable to a repo file; nothing explained before the evidence exists. Precision fixes are always accepted.
3. **Understood on first read.** A reader with no finance background should know after page 2 what the paper claims and why it matters. Define terms at first use, in the sentence where they appear.
4. **Confident voice.** State what the data shows plainly. No "can", "may" or "appears to" on findings the data proves. Limitations are stated once, in §7, not scattered as disclaimers.
5. **Economy.** Cut repetition and throat-clearing, but only after 1–4 are satisfied.

Style:
- Concrete before abstract: show the number or the contradiction, then name the idea.
- One sentence, one job. Split sentences that define, qualify and conclude at once.
- Affirmative framing. Say what something is before what it is not; avoid opening or closing paragraphs on a negation.
- Consistent terms: one name per concept (wedge; transaction value; marketplace channel; issuer-reported), used the same way throughout.
- First person "I" for the author's decisions (defining, measuring, reconciling); impersonal voice for results.
- No committee-facing hedging, no bureaucratic phrasing ("it should be noted", "in terms of"), no rhetorical flourishes.
- When shortening, remove words, not meaning. Before cutting a clause, ask what misreading it prevents.

## 11. Remaining open items (not for this pass)

- Title breadth ("Platform Economy") is mitigated by the scope paragraph; a title change would cascade to the Chinese title and department records. Chris's call.
- The References page-break rule leaves the appendix page short. Chris's call.
- YZU template compliance is unverifiable without the template.
- Thesis-stage analyses listed in §8/Table 8: BPS–platform definition reconciliation; decomposition of wedge changes into volume and monetization (verified feasible: e.g. Tokopedia 2022–23 ≈ 90% volume / 10% monetization); PMK mapping.
