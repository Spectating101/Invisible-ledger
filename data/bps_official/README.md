# BPS official e-commerce extracts

These CSVs transcribe public tables from BPS–Statistics Indonesia. They are a
separate official-statistics module, not additional rows in the issuer
transaction-value/revenue sample.

The province file joins two tables with the same reference year and province
grain: financial-report ownership (Appendix 6) and sales media (Appendix 14).
The two Papua observations withheld by BPS because relative standard error
exceeded 25% remain missing.

Important distinctions:

- BPS transaction value is business online-sales revenue, not an issuer GMV or
  TPV metric.
- The exclusive marketplace/non-marketplace decomposition (18.23%/81.77%) is
  not the same question as the multiple-response sales-media statistic
  (marketplace 32.74% of attributed transaction value).
- Financial-report ownership is not tax filing, tax payment, audited financial
  quality, or proof that an authority can access the record.
- Province-level associations are ecological and descriptive, not causal.

Primary publication:

https://www.bps.go.id/id/publication/2025/01/30/d52af11843aee401403ecfa6/statistik-e-commerce-2023.htm
# Important 2024 extension

The official BPS *E-Commerce Statistics 2024* publication has also been archived at
`sources/core_public_documents/bps_ecommerce_statistics_2024.pdf`. It is an image-based
PDF and is being extracted separately. Do not assume that a survey wave label is the
same as the economic reference year; preserve both when adding 2024 observations.

# Internal consistency warning

The 2023 publication contains two different counts in its English/OCR-visible text:
3,934,981 in an executive-summary passage and 3,816,750 in the main body/figure. The
latter is used in the current descriptive extract because it is paired with the stated
2022 count and 27.40% growth calculation. Both values must remain documented until the
publisher's table/erratum is checked; neither should be silently overwritten.

In the 2024 appendix, the 38 published province counts sum to 4,400,973 while the
published Indonesia total is 4,400,972. The one-business difference is preserved as
a source-table reconciliation difference; no province value has been adjusted to force
the total.
