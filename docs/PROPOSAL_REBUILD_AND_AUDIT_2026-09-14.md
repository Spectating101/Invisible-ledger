# Proposal rebuild and verification audit — 14 September 2026

**Status:** working record of a Claude session. Nothing here has been sent to the advisor.
Deliverables are in `papers/current/` and `papers/advisor_tracked/`.

## 1. Deliverables

| File | What it is |
|---|---|
| `papers/current/Invisible_Ledger_Thesis_Proposal_2026-09-14.docx/.pdf` | **10-page proposal.** Proposal register, Flashpoint format, Kong's Sept-01 section numbering |
| `papers/advisor_tracked/..._Sept01_Surgery_2026-09-14.docx/.pdf` | 20pp markup: Kong's Sept-01 file with her edits accepted and this session's revisions as tracked changes, 7 live comment anchors |
| `papers/advisor_tracked/..._Sept01_ACCEPTED_PREVIEW_2026-09-14.docx/.pdf` | 17pp thesis-register evidence record (the Surgery file with all changes accepted) |

## 2. The 9-vs-12 transitions question is NOT a conflict

`docs/EMPIRICAL_TIER_RECONCILIATION_2026-09-10.md` (on `research/research-synthesis-20260910`)
already settled this. Both summaries are valid; they admit different evidence.

| Universe | Series | Transitions | Rev faster | Txn faster | Reversals | Median abs |
|---|---|---:|---:|---:|---:|---:|
| All-tier inventory | Blibli FY2021–25, Bukalapak, Tokopedia, Grab, Shopee | 12 | 10 | 2 | 2 | 42.02 pp |
| Direct-candidate sensitivity | Blibli FY2020–25, Bukalapak, Tokopedia | 9 | 6 | 3 | 3 | 42.94 pp |

The proposal reports **both**, side by side. The extra reversal is Blibli FY2020→FY2021.
Prior drafts quoted one set without saying which universe it came from; that was the only defect.

Count reconciliation: the advisor candidate table holds **15 direct rows** (Blibli 7, Bukalapak 5,
Tokopedia 3). Removing Bukalapak FY2024 and Tokopedia FY2021 for period mismatch gives **13
period-matched**; removing Blibli FY2019 for negative segment revenue gives **12 with positive
denominators**. The executed hypothesis run admitted **17 levels / 12 transitions**.

## 3. Errors found and corrected this session

| # | Error | Correction |
|---|---|---|
| 1 | Leave-one-out cited **transaction values** (37.85 / 26.90 / 21.71) in a sentence about the wedge | Wedges are **35.29 / 24.14 / 20.70** |
| 2 | "22 platform-year snapshots" for marketplace structure | Unsupported — no file has 22 rows (`platform_structure_2025.csv` has 6). Replaced with a description |
| 3 | "74 complete province-years" | Does not reproduce: 36 (2023) + 39 (2024) fully populated. Replaced with "39 provinces observed in 2023 and 2024" |
| 4 | SEA 2020 GMV "$98 billion" | Not a published figure. e-Conomy SEA 2020 reports **$100 billion** |
| 5 | PMK timeline jumped designation → postponement | Collection **took effect 1 August 2026** after a month for system adjustment, which is why refunds were ordered |
| 6 | BPS marketplace growth 1.45% / 98.46% outside | Executed output is **1.4162%** and **98.49%** |

## 4. Verified against primary sources

- **Indonesia 2023 nominal GDP = US$1.371T** — World Bank $1,371,169,301,563.62; FRED $1,371,166,925,749.88.
  40.070288 / 1371.169 = **2.922%**. This closes advisor comment 165.
- **Tokopedia mechanism reproduces exactly** from `data/measurement/source_extracts/tokopedia_fy2022_2023_revenue_components.csv`:
  FY2022 8,143,239 − 4,112,320 = 4,030,919; FY2023 8,988,909 − 2,813,719 = 6,175,190.
  Net change +2,144,271 (+53.20%): **60.56%** lower incentives, **39.44%** higher gross.
- **FY2023 cross-section**, **Grab derivation**, **tier counts**, **global module** (48/8/40/29/4/7.10pp/0.22–74.63%),
  **four sensitivity dimensions**, **ASEAN 42 from 450**, **quarterly 47** — all exact against committed outputs.
- **PMK 37/2025**: 0.5% of invoice gross turnover; Blibli, Shopee, Tokopedia, Lazada designated 1 July 2026;
  effective 1 August 2026; postponed through 31 October; scheduled 1 November 2026; DJP describes it as a
  change in collection mechanism, **not a new tax** — so it cannot be cited as evidence of prior underpayment.
- **Kleven et al. (2011)** 0.3% vs 37%, Econometrica 79(3).

## 5. Conceptual correction: the wedge is V − R

Earlier drafts defined the invisible wedge two ways — an *administrative information gap* in §1 and
*W = V − R* in the framework. These are different objects. The proposal now defines it once, as the
accounting boundary, and treats third-party reporting as a separate downstream question:

> "The wedge does not measure that reporting gap, and this paper does not claim it does. It measures the
> accounting boundary; whether the activity behind that boundary is separately recorded and transmitted to
> public institutions is a further question the study then examines."

Consequent changes: research questions reduced 4 → 3, with the 48-issuer-year global module demoted to
**external corroboration** reported in Section 5; "admitted platform-years" → "retained candidate
platform-years" so the front of the document does not sound more settled than Section 6 admits; and the
framework's closing sentence no longer claims to quantify what is "not directly captured by the existing
tax system."

## 6. Continuity with the advisor's reviewed draft

Share of substantive sentences (references excluded) carried verbatim or near-verbatim from Kong's
Aug-14 / Sept-01 reviewed drafts:

| Version | Continuity |
|---|---:|
| Sep-12 Committee Rebuild | 0% |
| Sep-13 Flashpoint | 7% |
| First 9pp proposal (rewritten) | 11% |
| **Current 10pp proposal (grafted)** | **26%** |
| 17pp Surgery file (tracked on her file) | 47% |

Fifteen of eighteen load-bearing passages are word-for-word identical to Sept-01, including the
100/10/90 schematic, the ratio definition, the GTV/GMV definition, the "higher ratio" boundary
sentence, the take-rate definition, and four literature sentences.

## 7. Advisor format requirements now satisfied

Abstract 137 words (comment 2) · every table captioned, numbered and referenced in text (119, 125, 154) ·
Appendix A variable definitions (153) · GTV/GMV footnote (130) · USD equivalents for IDR and Rp (214) ·
consistent captions above tables (162) · section numbering per her Sep-12 chat (1.1/1.2, Literature §2,
Framework §3, Data §4) · GDP share (165) · finance-journal references (88).

YZU format spec located: A4, top 3.5cm / left 4.0cm / right 2.0cm / bottom 2.0cm, Chinese 標楷體,
English Times New Roman, body 12pt, 1.15 line spacing. The proposal uses Flashpoint's margins
(2.30/2.00/2.20/2.20) rather than the thesis binding margins; fonts and line spacing comply.

## 8. Open

- Never opened in Microsoft Word (built and rendered in LibreOffice only).
- RQ3-as-corroboration is a structural decision the advisor has not seen.
- The advisor's Sep-9 request to review the dataset was answered out of band: Chris reports showing
  her an Empirical Data review via Dropbox. Not verified here (no Dropbox access from the build
  environment), and not reconciled against `Invisible_Ledger_Data_Package_2026-09-14.xlsx` — so it is
  unknown whether the figures she saw match the ones the proposal now states.
- Blibli and Bukalapak scope admission remains the open question the proposal puts to the committee.
