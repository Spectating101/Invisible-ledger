"""Where did reported revenue growth come from?  Over a window [t0, t1] for one firm or segment group:
   ln(R1/R0) = ln(V1/V0)  [more commerce]  +  ln(m1/m0)  [higher take rate].
   m = tau - iota (tau = fee before incentives, iota = incentives, both per unit of V), so the take-rate part splits into
   fee change  (dtau / m)  and  discount pull-back  (-diota / m), using the endpoint average of m (log-mean) to make it add up.
Reads tables/l_panel.csv (quote-verified inputs).  Grab on-demand = Mobility + Deliveries summed.  Writes tables/growth_decomposition.csv."""
import numpy as np, pandas as pd
P = pd.read_csv("tables/l_panel.csv")
g = P[P.firm == "Grab"].groupby("year")[["V", "R", "I"]].sum().reset_index()
g["firm"], g["seg"], g["sample"] = "Grab", "On-demand (Mobility+Deliveries)", "in"
P2 = pd.concat([P[P.firm != "Grab"], g], ignore_index=True)
P2 = P2.dropna(subset=["V", "R", "I"])
W = [("Grab", "On-demand (Mobility+Deliveries)", 2021, 2024), ("Grab", "On-demand (Mobility+Deliveries)", 2022, 2024),
     ("GoTo", "On-demand", 2023, 2025), ("GoTo", "On-demand", 2022, 2025), ("Tokopedia", "E-commerce", 2022, 2023),
     ("Blibli", "3P Retail", 2022, 2025), ("Blibli", "3P Retail", 2022, 2023), ("MakeMyTrip", "Group", 2019, 2025),
     ("Delivery Hero", "Group", 2020, 2025), ("DoorDash", "Marketplace", 2018, 2019)]
out = []
for f, s, a, b in W:
    d = P2[(P2.firm == f) & (P2.seg == s)].set_index("year")
    if a not in d.index or b not in d.index:
        continue
    x0, x1 = d.loc[a], d.loc[b]
    m0, m1, i0, i1 = x0.R / x0.V, x1.R / x1.V, x0.I / x0.V, x1.I / x1.V
    if m0 <= 0 or m1 <= 0:
        continue
    gR, gV = np.log(x1.R / x0.R), np.log(x1.V / x0.V)
    dm = m1 - m0
    mbar = dm / np.log(m1 / m0) if abs(dm) > 1e-12 else m0           # log-mean of m
    d_iota_part = -(i1 - i0) / mbar                                   # contribution to ln m from discount change
    d_tau_part = ((m1 + i1) - (m0 + i0)) / mbar                       # contribution from fee-before-incentives change
    out.append(dict(firm=f, seg=s, window=f"{a}-{b}", revenue_growth_pct=100 * (np.exp(gR) - 1), volume_growth_pct=100 * (np.exp(gV) - 1),
                    take_rate_start_pct=100 * m0, take_rate_end_pct=100 * m1,
                    share_from_volume=gV / gR, share_from_fee=d_tau_part / gR, share_from_discount_cut=d_iota_part / gR))
D = pd.DataFrame(out)
D.round(3).to_csv("tables/growth_decomposition.csv", index=False)
if __name__ == "__main__":
    pd.set_option("display.width", 220)
    print(D.round(2).to_string())
