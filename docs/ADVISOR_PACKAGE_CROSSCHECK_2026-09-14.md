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

## Branch consolidation — done 14 September

All nine `research/*` branches are now merged into `main`; none remain unmerged.

`results-consolidation-20260912` fully contained `research-synthesis-20260910`, so those two were one
merge, and `empirical-certification-v2-20260910` arrived transitively with them. Six of the remaining
merges were clean. Two needed resolution:

- **`results-consolidation`** conflicted on three files in the BPS layer. The branch had
  *independently* made the same Rp203.58T correction fixed on `main` in 386fd3c — convergent
  confirmation that 1.45% is right. Both sides had also added the same data row, which git auto-merged
  into a duplicate; deduplicated.
- **`empirical-certification-integration-20260910`** produced eleven add/add conflicts and is a
  superseded lane: its successor v2 was already in, and `main`'s files are strict supersets
  throughout. Resolved to `main` and merged anyway, so the branch stops reading as outstanding work.

The payment-layer record counts were verified against the merged files and all six match what was
reported: 18,954 national monthly, 42,701 regional monthly, 1,460 published annual, 3,616 core
monthly, 278 core annual, 14 report observations.

`docs/CANONICAL_EMPIRICAL_RESULTS_2026-09-12.md`, now on `main`, agrees with the proposal on every
headline figure — 42.02pp all-tier, 42.94pp direct-candidate, 9 direct transitions, 1.45%, 98.46%. The
analysis was re-run after every resolution and the proposal rebuilt: unchanged at 12 pages and 9
tables, all three advisor documents validating clean.

A `pre-consolidation-backup` tag marks `main` at 07e85a6, immediately before the first merge.

## What a refreshed package still needs

The 10 September data room predates the payment layer and consolidated results, both of which are now
on `main` per the section above. Rebuilding the package from `main` therefore picks them up.

A refresh should therefore fold in the payment layer and the consolidated results, carry the corrected
Rp203.58T BPS figure, keep the US$40.070 billion FY2023 construction, state the 11-direct-level /
9-direct-transition and 17-level / 12-transition universes separately rather than as one pooled N, and
use relative paths throughout. That is a consolidation of existing branches, not a rebuild.
