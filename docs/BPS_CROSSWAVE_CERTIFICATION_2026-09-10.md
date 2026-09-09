# BPS cross-wave source certification — 10 September 2026

## Purpose

This note certifies which 2023–2024 BPS e-commerce comparisons can be treated as source-concordant descriptive comparisons and which still require additional questionnaire-level work. It is an empirical-source note only; it does not alter the hypotheses agenda or imply causal identification.

## 1. Transaction value and sales-media decomposition: certified descriptively

### 2023 source

BPS *Statistik E-Commerce 2023* reports Figure 23 as **“E-Commerce Transaction Value and Percentage of E-Commerce Transaction Value by Sales Media, 2023.”** The retained national values are:

- total e-commerce transaction value: **Rp1,100.87 trillion**;
- marketplace/platform-digital transaction value: **Rp200.68 trillion**;
- non-marketplace/platform-digital transaction value: **Rp900.19 trillion**;
- marketplace share: **18.23%**;
- non-marketplace share: **81.77%**.

Primary publication page:
<https://www.bps.go.id/en/publication/2025/01/30/d52af11843aee401403ecfa6/e-commerce-statistics-2023.html>

The searchable official BPS publication text identifies the same figure and decomposition. Repository transcription:
`data/bps_official/bps_ecommerce_national_indicators_2020_2023.csv`.

### 2024 source

A BPS-Statistics Indonesia presentation, **“Measuring the E-commerce Value in Indonesia”** by Adam Luthfi, Directorate of Services Statistics, reports **“E-Commerce Transactions Value by Sales Media, 2024.”** It gives:

- total e-commerce transaction value: **Rp1,288.93 trillion**;
- marketplace transaction value: **Rp203.58 trillion**;
- marketplace share: **15.79%**;
- non-marketplace share: **84.21%**;
- total transaction-value growth relative to 2023: **17.08%**.

BPS presentation hosted by UN SIAP:
<https://www.unsiap.or.jp/sites/default/files/doc/2026-04/08_Measuring%20E-Commerce%20in%20Indonesia_Webinar%20on%20Digitalization_update1.pdf>

Official BPS 2024 publication page:
<https://www.bps.go.id/en/publication/2025/11/28/647323224ecc656c2933571b/statistik-e->

The BPS publication abstract explicitly states that the publication reports e-commerce transaction value **during 2024** from the perspective of e-commerce businesses.

## 2. Certified descriptive cross-wave calculation

Because both source layers explicitly define the national split as **e-commerce transaction value by sales media**, the marketplace/non-marketplace comparison can be treated as a source-concordant **descriptive cross-wave comparison** at the aggregate national level.

Use the directly reported 2024 marketplace amount, **Rp203.58 trillion**, rather than reconstructing it from the rounded 15.79% share. This avoids a small rounding artifact.

### Marketplace component

- 2023: Rp200.68 trillion
- 2024: Rp203.58 trillion
- growth: **+1.45%**

### Non-marketplace component

- 2023: Rp900.19 trillion
- 2024: Rp1,085.35 trillion (`1,288.93 - 203.58`)
- growth: **+20.57%**

### Total

- 2023: Rp1,100.87 trillion
- 2024: Rp1,288.93 trillion
- growth: **+17.08%**

The arithmetic therefore establishes that, in these BPS national aggregate estimates, the non-marketplace component grew much faster than the marketplace component between 2023 and 2024.

## 3. What this does not establish

The cross-wave certification does **not** make the data a business panel. It does not identify the same enterprises in both years, entry/exit, productivity, tax status, or causality. It also does not make BPS transaction value interchangeable with issuer GMV/TPV; BPS measures business online-sales value under its survey concept.

The two survey waves use annual estimation exercises with different realized samples. Accordingly, the safe empirical statement is about the movement of **published national aggregate estimates**, not incumbent-firm behavior.

## 4. Financial-report ownership: published values established, trend interpretation still guarded

The 2023 publication directly reports that **15.19%** of e-commerce businesses have financial reports (Figure 7; “Percentage of E-Commerce Businesses by Financial Report Ownership, 2023”). The retained 2024 official table reports **17.15%**.

The two wave values themselves are established. However, before treating the +1.96 percentage-point movement as a strong longitudinal behavioral result, retain the questionnaire/population-concordance check. In particular, verify the exact 2024 question wording, skip logic, and estimation universe against the 2023 instrument.

Therefore:

- 2023 value: `established_wave_value`;
- 2024 value: `established_wave_value`;
- 2023→2024 trend: `guarded_cross_wave_interpretation` pending questionnaire-level concordance.

## 5. Research consequence

The BPS channel result is now stronger than the earlier rounded-share reconstruction. The defensible empirical statement is:

> **BPS national estimates show total e-commerce transaction value rising 17.08% from 2023 to 2024, while the directly reported marketplace component rises only about 1.45% and the implied non-marketplace component rises about 20.57%.**

This is a descriptive national-estimate result. It should not be translated into “marketplaces do not matter,” “non-marketplace activity is hidden,” or a tax/GDP claim.
