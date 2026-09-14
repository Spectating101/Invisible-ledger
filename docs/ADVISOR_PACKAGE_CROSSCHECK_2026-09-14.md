# Cross-check: the 10 September advisor data room vs. the 14 September proposal

Chris confirmed the advisor's 9 September dataset request was answered by sharing an "Empirical Data
Review" folder on Dropbox. The Dropbox link given is a `/home/...` authenticated browser URL, which
resolves only inside Chris's own session, so the upload itself could not be read from here. The local
source is almost certainly
`~/Downloads/Invisible_Ledger_Advisor_Data_Review_2026-09-10/` (62MB, 161 files, 10 sheets), and that
is what was cross-checked.

## The material question: is the advisor holding stale numbers?

**No.** The headline construction in the package is the current one:

    fy2023_indonesia_main_summary.csv
    transaction value 43.232567  revenue 3.162279  wedge 40.070288  wedge/revenue 12.671332

So the GoTo Group removal the advisor directed on 7 September was already applied before the package
was built. She was never shown the obsolete US$66.8 billion wedge. Grep hits on "66.8" inside the
package are incidental digit strings in unrelated fields — Shopify GMV rows, filenames, SEC filings —
not wedge claims.

## What the cross-check did find

**One real defect in the repository, now fixed (386fd3c).** The package's BPS certification file
records BPS's directly published 2024 marketplace amount of Rp203.58 trillion and states that it
supersedes the rounded-share reconstruction. `data/bps_official/` in this repository never carried
that row, so the analysis reconstructed the component as 15.79% x Rp1,288.93T and the proposal
reported 1.42% growth. The direct amount gives 1.45%. Details in the commit message; the 14 September
audit's item 6 has been reopened and reversed in `PROPOSAL_REBUILD_AND_AUDIT_2026-09-14.md`.

## Two claims checked and not supported

**"The advisor's personal name appears in generated package metadata."** Not found. A sweep of every
file in the package, binaries included, returns her name nowhere. The only matches on "Kong" are the
string *Hong Kong* inside the Sea Limited and Grab 20-F filings in `07_SOURCE_DOCUMENTS/`. The
workbook carries no `docProps` part at all, so it has no author metadata to strip.

**"13 direct candidate periods and nine direct transitions."** The transition count is right but the
level count is not. From `indonesia_longitudinal_candidate_levels.csv`: 17 levels total, of which 9
are `direct_issuer_scope_pending` and 2 are `direct_indonesia_aligned_segment` — **11 direct, not
13**. The nine direct transitions are correct and are the certified sensitivity: 8 direct transitions
in the table plus the Blibli FY2020 prospectus extension, median absolute difference 42.94pp, per
`EMPIRICAL_TIER_RECONCILIATION_2026-09-10.md`. The all-tier universe remains 12 transitions across
five series at 42.02pp. The two universes are not nested and neither supersedes the other.

## Genuine hygiene item, not yet fixed

Two shipped CSVs embed absolute build paths exposing the local account name:

- `01_INDONESIA_ISSUER/data/longitudinal/shopee_additional_country_anchors.csv`
- `08_MANIFESTS/repository_manifests/preserved_existing_manifest.csv`

These should be relative paths in any refreshed package. They leak the machine layout, not anything
about the advisor.

## What a refreshed package still needs

The 10 September data room predates two bodies of work that remain unmerged on `main`:

| Branch | Carries |
|---|---|
| `research/research-synthesis-20260910` | Bank Indonesia payment layer, packaging code, global/ASEAN/BPS evidence |
| `research/results-consolidation-20260912` | canonical results consolidation |

The payment layer alone adds roughly 18,954 national monthly, 42,701 regional monthly, 1,460
published annual, 3,616 core monthly and 278 core annual records (counts reported by ChatGPT from the
branch, not independently verified here).

A refresh should therefore fold in the payment layer and the consolidated results, carry the corrected
Rp203.58T BPS figure, keep the US$40.070 billion FY2023 construction, state the 11-direct-level /
9-direct-transition and 17-level / 12-transition universes separately rather than as one pooled N, and
use relative paths throughout. That is a consolidation of existing branches, not a rebuild.
