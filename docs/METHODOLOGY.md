# Methodology

## Conceptual layers

The project distinguishes:

1. gross platform transaction value;
2. platform-recognized gross or net revenue;
3. participant gross receipts or payouts;
4. intermediate inputs, incentives, refunds and transfers;
5. participant and platform value added;
6. amounts captured in statistical and tax systems.

Only the first two layers are commonly available from public platform disclosures. Their difference cannot identify layers three through six without additional data.

## Admission logic for platform-period observations

An observation is eligible for consideration only when:

- geography and business scope are explicit enough to evaluate;
- transaction and revenue measures cover the same period;
- currency and unit are known;
- original, revised and pro-forma bases are labelled;
- transaction and revenue definitions are recorded;
- any derived component has a transparent formula and source inputs;
- structural breaks and acquisitions are flagged.

Eligibility for consideration is not the same as final admission to the main sample.

## Directness classes

- `direct_country`: issuer explicitly reports the country quantity.
- `direct_segment`: issuer reports a business segment aligned with, but not necessarily identical to, the geographic target.
- `external_country_estimate`: country quantity comes from a third-party market source.
- `derived`: quantity is mechanically calculated from sourced inputs.
- `converted`: only currency/unit conversion is performed.
- `scenario`: chosen parameter variation, not an observation.
- `legacy`: preserved output not approved for current analysis.

## Frequency and observation counts

Annual totals, quarters within the same year, half-year/nine-month cumulative amounts, alternative publication vintages and overlapping segment/group totals are not independent observations. Report firms, segments, matched periods and missing pairs separately rather than one inflated N.

## GDP and tax interpretation

GDP measures value added, not gross platform transaction value. The transaction–revenue difference is therefore not an estimate of missing GDP. It may identify a set of participant-facing transactions for which platforms possess useful records, but participant income, costs, value added, filing status and tax liability require separate evidence.

