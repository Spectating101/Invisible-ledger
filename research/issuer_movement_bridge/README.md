# Issuer movement bridge

**Status:** supplementary research analysis; no main-sample or advisor approval implied.

This module asks a narrow economic question that supports the larger *Invisible Ledger* thesis without duplicating the ASEAN/global work:

> When selected platform/segment transaction activity changes, does recognized revenue describe the same direction and magnitude of movement?

The analysis uses only adjacent annual changes within one series. It never pools levels across currencies, countries, issuers, segments, or directness classes.

## Why this matters

The original paper's economic object is the surrounding participant/commercial activity, not the platform company alone. If transaction activity and recognized revenue can grow at very different rates—or move in opposite directions—then the corporate revenue ledger is not a stable one-for-one description of the movement of the wider commercial activity it accompanies.

This does **not** imply that one measure is wrong. The divergence can reflect monetization, incentives, business mix, principal/agent treatment, revenue definition, acquisitions, deconsolidation, or genuine business-model change. The empirical point is that the observer's choice of measure can change the growth story.

## Evidence classes

### Direct candidate series

- **Blibli/GDN 3P Retail, 2020–2025.** Direct issuer/segment TPV and net revenue; business/geographic eligibility remains pending and the segment includes online travel.
- **Bukalapak Group, 2020–2023.** Direct reported TPV and revenue with matched 12-month periods; Group includes overseas activity.
- **Tokopedia e-commerce segment, 2022–2023.** Direct Indonesia-aligned segment measures. FY2021 is explicitly excluded because the known construction paired full-year pro-forma transaction value with post-acquisition revenue.

### Conditional country reconstructions

- **Grab Indonesia, 2021–2023.** Country revenue is direct; transaction value is derived using a Group monetization rate.
- **Shopee Indonesia, 2022–2024.** Country GMV is external and country revenue is derived using a company-wide service rate.

Conditional series are summarized separately and are not treated as independent validation of direct issuer/segment evidence.

## Outputs

Running the script produces:

- `annual_series.csv` — the selected annual inputs and their evidence classes;
- `adjacent_growth_transitions.csv` — within-series activity growth, revenue growth, growth-gap, monetization change, and movement classification;
- `exclusions.csv` — explicit known exclusions;
- `SUMMARY.md` — research-facing interpretation.

## Reproduce

```bash
python3 scripts/analysis/build_issuer_movement_bridge.py \
  --output research/issuer_movement_bridge/results

python3 -m unittest discover -s tests -p 'test_issuer_movement_bridge.py' -v
```

## Promotion rule

Do not copy this module into the thesis as a finalized main result until:

1. the geographic/business-scope rule is approved;
2. the selected annual vintages are accepted;
3. the generated results reproduce from the current repository inputs;
4. the interpretation is positioned against the closest platform-economics and financial-reporting literature.
