"""H2-style split for Malaysia (DOSM Economic Census, reference years 2015 and 2022; quote-verified in tables/src/asean_my_extraction.csv):
e-commerce income = (establishments engaged in e-commerce) x (income per establishment).  Counts exist for these two census years only.
Compare with Indonesia (BPS 2023-24: count share about 90%; 2022-23 about 71%).  Caveats: 'e-commerce establishments' = registered establishments reporting e-commerce
transactions (includes B2B, the largest part of income); census frame, not the sample survey; 7-year gap, not annual."""
import numpy as np
n15, n22, v15, v22 = 47556, 78236, 398.2, 1126.9
g = np.log(v22 / v15); c = np.log(n22 / n15); p = np.log((v22 / n22) / (v15 / n15))
print(f"income x{v22/v15:.2f}; establishments x{n22/n15:.2f}; income per establishment x{(v22/n22)/(v15/n15):.2f} (RM m: {v15*1000/n15:.2f} -> {v22*1000/n22:.2f})")
print(f"log-share of growth from more establishments {c/g:.0%}; from higher income per establishment {p/g:.0%}")
