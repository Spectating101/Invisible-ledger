# Blibli publication-vintage sensitivity — 10 September 2026

## Purpose

This note tests whether the known FY2023 Blibli 3P TPV publication-vintage difference changes the longitudinal result used in the empirical certification layer.

## Known source-vintage issue

The reviewed source-issue register records two FY2023 3P TPV values:

- original FY2023 release: **Rp49,917 billion**;
- FY2024 comparative: **Rp49,912 billion**.

The current canonical annual table uses the later FY2024 comparative, while the earlier value remains preserved as source lineage. The difference is **Rp5 billion**, approximately 0.01% of the annual TPV level.

Source issue register: `research/longitudinal/OPEN_SOURCE_ISSUES.csv` on the earlier longitudinal-review branch, issue `BLI-FY23-V`.

## Sensitivity result

Holding the surrounding canonical FY2022 and FY2024 annual observations fixed:

| Comparison | Canonical FY2023 TPV = 49,912 | Alternative FY2023 TPV = 49,917 | Difference |
|---|---:|---:|---:|
| FY2022→FY2023 TPV growth | 34.7153% | 34.7287% | +0.0135 pp |
| FY2023→FY2024 TPV growth | 8.6112% | 8.6003% | −0.0109 pp |

The activity-growth sign remains positive under both vintages in both transitions.

At the broader direct-candidate result level, the alternative FY2023 TPV does **not** change:

- the **9** valid adjacent direct-candidate transitions;
- the **3** opposite-sign activity/revenue cases;
- the **42.94pp** median absolute activity/revenue growth divergence.

Machine-readable sensitivity table: `data/longitudinal/blibli_vintage_sensitivity_2026-09-10.csv`.

## Interpretation

The FY2023 Blibli annual TPV vintage issue should remain documented, but it is **not load-bearing for the current longitudinal headline result**. The later comparative remains the preferred canonical value because it is the later issuer-provided comparative and supports consistent vintage handling.

This conclusion does not resolve separate Blibli issues involving:

- the 3P segment's OTA/travel business perimeter;
- competing **quarterly** Q4 2024 TPV vintages;
- annual-versus-quarterly roll-up residuals in Group/Institutions;
- the negative FY2019 3P net-revenue denominator.

Those issues should stay separate rather than being treated as one generic “Blibli data problem.”
