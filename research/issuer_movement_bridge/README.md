# Issuer movement and mechanism bridge

**Status:** supplementary research analysis; no main-sample or advisor approval implied.

This branch owns an inward analytical lane that supports the larger *Invisible Ledger* thesis without duplicating Box's ASEAN/global work.

It asks two linked questions:

1. **Movement:** when selected platform/segment transaction activity changes, does recognized revenue describe the same direction and magnitude of movement?
2. **Mechanism:** where those measures diverge, which cases can be explained with source-supported incentives, promotion, monetization or business-mix evidence—and which remain unresolved?

The analysis uses adjacent annual changes only within one series. It never pools levels across currencies, countries, issuers, segments, or directness classes.

## Why this matters

The original paper's economic object is the surrounding participant/commercial activity, not the platform company alone. If transaction activity and recognized revenue can grow at very different rates—or move in opposite directions—then the corporate revenue ledger is not a stable one-for-one description of the movement of the wider commercial activity it accompanies.

This does **not** imply that one measure is wrong. Divergence can reflect monetization, incentives, business mix, principal/agent treatment, revenue definition, acquisitions, deconsolidation or genuine business-model change. The empirical point is that the observer's choice of measure can change the growth story.

## Evidence classes

### Direct candidate series

- **Blibli/GDN 3P Retail, 2020–2025.** Direct issuer/segment TPV and net revenue; business/geographic eligibility remains pending and the segment includes online travel.
- **Bukalapak Group, 2020–2023.** Direct reported TPV and revenue with matched 12-month periods; Group includes overseas activity.
- **Tokopedia e-commerce segment, 2022–2023.** Direct Indonesia-aligned segment measures. FY2021 is explicitly excluded because the known construction paired full-year pro-forma transaction value with post-acquisition revenue.

### Conditional country reconstructions

- **Grab Indonesia, 2021–2023.** Country revenue is direct; transaction value is derived using a Group monetization rate.
- **Shopee Indonesia, 2022–2024.** Country GMV is external and country revenue is derived using a company-wide service rate.

Conditional series are summarized separately and are not treated as independent validation of direct issuer/segment evidence.

## Mechanism evidence added on this branch

- **Tokopedia FY2022→FY2023:** existing source reconciliation separates the arithmetic net-revenue increase into higher gross revenue and lower customer incentives.
- **Blibli 3P FY2022→FY2023:** source extract from the FY2023 annual report separates segment revenue before discount/direct promotion from the direct-promotion deduction and net revenue.
- **Blibli 3P FY2024→FY2025:** FY2025 issuer evidence documents TPV decline alongside net-revenue/GPBD growth and attributes improved GPBD mainly to a shift in OTA toward higher-margin accommodation/experiences plus operating-efficiency measures.
- **Blibli 3P FY2020→FY2021:** retained as an opposite-sign movement with **unresolved mechanism** rather than receiving an invented explanation.

## Research-design artifacts

- `INDONESIA_VISIBILITY_MATRIX.md` — makes “visibility” observer-specific across platform, merchant, public researcher, BPS and DGT; distinguishes current evidence, survey estimates, legally specified reporting and unknown linkages.
- `THESIS_SPINE.md` — evidence-to-claim architecture and promotion gates for a future manuscript rebuild.
- `mechanism_source_extract.csv` — source-located values used by the mechanism calculations.

## Outputs

`build_issuer_movement_bridge.py` produces:

- `annual_series.csv`;
- `adjacent_growth_transitions.csv`;
- `exclusions.csv`;
- `SUMMARY.md`.

`build_mechanism_bridge.py` produces:

- `mechanism_cases.csv`;
- `MECHANISMS.md`.

## Reproduce

```bash
python3 scripts/analysis/build_issuer_movement_bridge.py --output build/issuer_movement_bridge
python3 scripts/analysis/build_mechanism_bridge.py --output build/mechanism_bridge

python3 -m unittest discover -s tests -p 'test_issuer_movement_bridge.py' -v
python3 -m unittest discover -s tests -p 'test_mechanism_bridge.py' -v
```

## Promotion rule

Do not copy these modules into the thesis as finalized main results until:

1. the geographic/business-scope rule is approved;
2. selected annual vintages are accepted;
3. generated results reproduce from the current repository inputs;
4. BPS/channel definitions used in complementary claims are verified;
5. interpretation is positioned against the closest platform-economics, digital-measurement and financial-reporting literature.
