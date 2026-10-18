"""Sizing ONE scope item of the BPS-platform bridge: digital goods, cars and motorcycles inside Tokopedia's GTV (2 Oct 2026).
Verified inputs: GoTo 4Q23 deck: e-commerce GTV 4Q22 Rp70.8tn, 4Q23 Rp65.3tn; core GTV (excludes digital goods and sales of cars and motorcycles) fell 26% YoY (call: 'core GTV ... down 26%').
GoTo Q2-2022 call (30 Aug 2022): 'the contribution of digital goods is roughly 18% to 20% of GTV'.  Annual Tokopedia GTV 2023 Rp248.8tn (GoTo FY2023 release); BPS marketplace 2023 Rp200.68tn; modelled Shopee Indonesia Rp327.9tn.
Derivation (assumption-labelled): non-core share of 4Q22 GTV >= 18-20% (digital goods alone; cars/motorcycles add more), so core 4Q22 <= 82% x 70.8 = 58.1; core 4Q23 = 0.74 x core 4Q22 <= 43.0;
non-core 4Q23 >= 65.3 - 43.0 = 22.3  (>= 34% of 4Q23 GTV).  Annual 2023 non-core share is not published; the 4Q23 bound is applied as a LOWER bound only for illustration."""
import numpy as np
g22, g23, core_drop = 70.8, 65.3, 0.26
for s in (0.18, 0.20):
    core22 = (1 - s) * g22; core23 = (1 - core_drop) * core22; non23 = g23 - core23
    print(f"non-core share 4Q22 >= {s:.0%}: core 4Q23 <= {core23:.1f}; non-core 4Q23 >= {non23:.1f} = {non23/g23:.0%} of GTV")
toko23, bps_mkt, shopee = 248.8, 200.68, 327.9
for label, share in [("2022-level share 18%", 0.18), ("4Q23 lower bound ~34%", 0.34)]:
    phys = toko23 * (1 - share)
    tot = phys + shopee
    print(f"{label}: Tokopedia physical-goods GTV 2023 ~ Rp{phys:.0f}tn (BPS marketplace Rp{bps_mkt}tn); + modelled Shopee Rp{shopee:.0f}tn = Rp{tot:.0f}tn; BPS shows {bps_mkt/tot:.0%}; gap factor {tot/bps_mkt:.1f}x")
