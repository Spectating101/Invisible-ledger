# Audit of the balanced/Flashpoint-format version — 15 September 2026

Reviewed `Invisible_Ledger_Thesis_Proposal_FLASHPOINT_FORMAT_2026-09-14.docx`. The judgement behind
it is right and it is now the FINAL, after two corrections.

## The argument for 9–10 pages is correct

Treating 8 pages as an objective function rather than a sanity benchmark was a real error, and it was
mine. The evidence supports the middle range: Flashpoint carried **3,365 words at 420 words per page**
across 8 pages, so it was *denser in prose* than the 8-page compact version (2,866 words, 358 w/page)
despite far less empirical complexity. The 8-page version was lean partly because the layout was loose,
not only because the content was tight.

## Content verified

All five claimed additions are present and do real work: §1.3 contribution positioning, §4.2
comparability strategy, Figure 1, §5.4 interpretive synthesis, and the four-row inference-boundary
table. Every empirical figure survives — 40.07 / 12.671, 42.02 / 42.94, the BPS split, the Tokopedia
mechanism, 13/11/9, 48 issuer-years, the PMK sequence. All advisor themes still pass; abstract 148
words.

**Figure 1 was checked against source data, point by point.** It plots *E = V/R − 1* from
`indonesia_longitudinal_candidate_levels.csv`, all 17 retained levels, none invented:

| Series | Source V/R | Implied E | Plotted |
|---|---:|---:|---:|
| Blibli FY2022 | 186.181 | 185.18 | ~185 |
| Bukalapak FY2020 | 62.946 | 61.95 | ~62 |
| Tokopedia FY2023 | 40.296 | 39.296 | matches Table 2 |
| Grab FY2023 | 8.895 | 7.895 | matches Table 2 |

The caption states that levels are shown by series and not pooled across evidence tiers, which keeps
the tier discipline intact. This closes advisor comment 160, one of the two genuinely open items.

## Two defects found and corrected

**1. Page size was US Letter, not A4.** 216 × 279mm. Flashpoint is A4 and so is every other version
here; a Taiwanese university expects A4. Converted to 210 × 297mm.

**2. A forced page break produced a completely blank page 8.** An explicit `w:br type="page"` sat
after §7's closing paragraph. Since §7 already ended near the foot of page 7, the break emitted a page
carrying nothing but the footer, then Appendix A began on page 9. Removed.

## Result

| | Letter, as received | A4, corrected |
|---|---:|---:|
| Pages | 10 | **9** |
| Blank pages | 1 | 0 |
| Words per page | 353 | **391** |

Nothing was cut to reach 9 pages. The page came off a blank sheet, and the density gain came from
removing dead space — which is precisely the Flashpoint discipline the rebuild was aiming at.
Remaining gap to Flashpoint's 420 w/page is heading and equation leading, worth perhaps a further half
page; not pursued, since 9 pages sits inside the stated 9–11 target.

## Standing open item

Footnote placement (comments 26 and 130). The GTV/GMV terminology note is inline rather than in a
Word footnote. The decision not to ship a LibreOffice-rendered footnote with a dropped body was the
right call — a renderer-dependent defect is worse than a placement mismatch.
