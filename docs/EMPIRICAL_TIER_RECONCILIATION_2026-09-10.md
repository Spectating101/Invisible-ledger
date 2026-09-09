# Indonesia transition-universe reconciliation — 10 September 2026

## Why two valid headline counts exist

Two executed Indonesia longitudinal summaries now coexist because they answer different questions and use different evidence universes.

### Box hypothesis inventory

`outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv` contains **12 transitions across five series**:

- Blibli 3P Retail FY2021→FY2025: 4 transitions;
- Bukalapak Group FY2020→FY2023: 3;
- Tokopedia FY2022→FY2023: 1;
- Grab conditional Indonesia FY2021→FY2023: 2;
- Shopee conditional Indonesia FY2022→FY2024: 2.

Across all evidence tiers it reports:

- revenue growth faster in 10;
- transaction growth faster in 2;
- 2 opposite-sign transitions;
- median absolute growth difference 42.02pp.

This is an **all-candidate-tier inventory diagnostic**, not a direct-sample estimate. It intentionally combines direct scope-pending, direct Indonesia-aligned, and conditional reconstruction tiers only for coverage diagnostics while continuing to label the tiers separately.

### Certified direct-candidate universe

The empirical-certification layer asks a narrower question: what happens if the conditional Grab/Shopee country reconstructions are removed and all currently transcribed direct issuer/segment annual candidates with usable positive transition bases are considered?

That layer contains **9 valid direct transitions**:

- Blibli 3P FY2020→FY2025: 5;
- Bukalapak Group FY2020→FY2023: 3;
- Tokopedia FY2022→FY2023: 1.

It reports:

- revenue growth faster in 6;
- transaction growth faster in 3;
- 3 opposite-sign transitions;
- median absolute growth difference 42.94pp.

The additional opposite-sign case is **Blibli 3P FY2020→FY2021**. FY2020 comes from the issuer prospectus transcription in `data/longitudinal/blibli_prospectus_2019_2020_candidates.csv`; Box's first hypothesis script starts the Blibli series from the later `blibli_reported_pairs_all_vintages.csv`, which begins at FY2021.

## What should be shown to Kong

Do not collapse these into one headline.

Use the following hierarchy:

1. **Direct Indonesia-aligned tier:** Tokopedia FY2022→FY2023 (1 transition; direct segment; strongest geographic fit).
2. **Direct issuer scope-pending tier:** Blibli and Bukalapak, with the Blibli prospectus extension shown as a source/vintage sensitivity rather than silently mixed into the first hypothesis execution.
3. **Conditional country-reconstruction tier:** Grab and Shopee, explicitly sensitivity/supporting evidence only.
4. **All-tier inventory diagnostic:** Box's 12-transition summary, useful for coverage but not an approved pooled sample.

The broad direct-candidate 9-transition result remains useful as a **scope sensitivity**, not as a final-sample estimate.

## Research consequence

Both executions support the bounded proposition that transaction activity and recognized revenue can move materially differently. The exact count of sign reversals depends on evidence admission, which is itself part of the empirical sample-design problem. That sensitivity should be shown rather than hidden.
