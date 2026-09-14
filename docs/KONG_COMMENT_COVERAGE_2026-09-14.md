# Per-comment coverage — 8-page FINAL proposal, 14 September 2026

All 40 tracked comments from Prof. Kong's two marked drafts, checked against the promoted 8-page
proposal **with their anchor context**, since the source documents are not proposals.

## What the source documents actually are

Neither marked draft is a proposal. Both are full thesis manuscripts:

| | Words | Tables | Structure |
|---|---:|---:|---|
| `Invisible_Ledger_Aug1426(1)_Kong.docx` | 6,778 | 11 | Abstract → Results → Policy implications → Conclusion → Appendix A |
| `Invisible_Ledger_Sept0126_Kong.docx` | 8,535 | 17 | 11 numbered sections including §8 investor-response event study, §10 policy implications, §11 conclusion |

Several comments are therefore anchored to material that does not belong in a proposal at all, and
reporting them as "unaddressed" would be a category error. Anchors were recovered by locating each
`commentRangeStart` in `word/document.xml` and reading its containing paragraph.

## Moot — anchored to sections or terms the current design no longer contains (7)

| # | Comment | Anchored to | Why moot |
|---|---|---|---|
| 164 | "A year consists of four quarters. Why do some years contain only one or two quarters?" | *Panel A. Number of firm-quarter observations by year* | The event panel it describes belonged to the investor-response study, which is not part of the current research direction |
| 163 | "What is GMV?" | §The investor-response sample | Same section; the terminology point is separately satisfied, GTV is defined at first use |
| 167 | "Grab has reported since 2021, Sea since Q3 2017 — collect as much data as possible" | GRAB row of the event panel | Aimed at the quarterly event sample; the longitudinal extension it implies is satisfied at annual frequency, FY2019–FY2025 |
| 214 | "Use a consistent currency, USD" | USD cell in the event panel | Table gone; the principle holds — USD throughout, no bare rupiah figures |
| 215 | "Consistent font, size, spacing per YZU" | §Reconciling the Indonesia and company-wide ecosystem ratios | Section gone; the formatting instruction is general and remains open below |
| 161 | "What is take rate? What is the difference between take rate and blended take rate?" | §Sensitivity — the blended take rate parameter | The proposal no longer uses either term, and no longer prints the parameter sweep |
| 109 | "What do you mean by scope-matched?" | "Fourth, I use scope-matched historical Grab and Shopee…" | The term was removed; evidence tiers state scope explicitly instead |

Two more, **177** and **192**, targeted the "Table 3B / Table 3C" numbering and the reason for
reporting them separately. That structure is gone, but both underlying instructions are satisfied:
tables are numbered sequentially 1–3, and where two admission universes are reported side by side the
proposal states why they differ.

## Addressed (29)

**Terminology.** GTV is the single label, GMV and TPV named once as issuer variants (130, 178, 217,
163). BPS-Statistics Indonesia, PMK and DJP expanded at first use (107). Currency USD throughout
(214).

**The proxy.** Claimed as the author's own construction in both abstract and §3 — her twice-asked,
still-unsatisfied question (89, 114, 107). Berg et al. (2020) supports the premise (89).

**Tables.** Three, numbered 1–3, no "3B" construction (177). Each named in prose with purpose and
insight (119, 125, 154). Captions above and self-contained (2, 162, 174). Evidence class and scope
in-table (189, 200, 203). Both universes explained (192).

**Scope and sample.** GoTo appears only as the Tokopedia segment, never Group, stated as not a literal
country line (153 Sept, 170). Platform selection justified (58). FY2019–FY2025 annual (159, 167).
Results current (80).

**Other.** Abstract 148 words (2 Aug). No figure in the title (1). Appendix carries variables and data
sources as she asked, pointing at her own sample draft (153 Aug). Four finance/accounting references,
three in A+ journals on her ranking (88). Economic scale as a share of GDP — her own suggestion (165).
Momentum Works named and justified (146).

## Not verifiable here (2)

**0 and 215 — YZU formatting compliance.** Raised in both rounds. The build is Times New Roman 12pt on
A4 with the Flashpoint title-page structure, but the department's current specification has not been
seen. Needs the template.

## Genuinely open (2)

**160 — "Update the figure using the extended sample."** Anchored to *Figure 1. Indonesia platform
gross transaction value*, a figure in the FY2023 cross-section. That cross-section survives as Table 2,
so the instruction still applies and the proposal contains no figures at all. A time-series of
transaction-value versus revenue growth across the retained series would answer it and would make the
42.02pp divergence visible rather than only tabulated.

**26 and 130 — footnote placement.** She asked for footnotes at the page bottom, and specifically that
the GTV/GMV terminology difference be carried *in a footnote*. It is inline in §3. Substance
addressed, placement not; the build script has no footnote support.

## Summary

29 addressed, 7 moot, 2 blocked on the department template, 2 open. Nothing open blocks submission.
The figure is the one worth adding before the examination: it answers a direct instruction and
strengthens the longitudinal section, currently the most table-dependent part of the argument.
