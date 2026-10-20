"""BPS e-commerce microdata: the pre-registered checks and tests (PREREGISTRATION.md section D and addenda), written 3 Oct 2026
BEFORE any purchased file was opened. Only the free 5-10 row sample files were used to test that the code runs.

Files (licensed, never committed): pass their paths as arguments.
  --f2021  Survei E-Commerce 2021 (questions refer to 2020)
  --f2023  Survei E-commerce 2023 (refers to 2022)
  --f2024  Survei Usaha/Perusahaan E-Commerce 2024 (refers to 2023)
Answer codes from the questionnaires: yes = 1, no = 2; revenue brackets 1..4 = <300m | 300m-2.5bn | 2.5-50bn | >50bn;
2024 R315 (online revenue vs previous year): 1 up, 2 same, 3 down, with R315B the percent.
Run: python3 bps_microdata_tests.py --f2021 A.dbf --f2023 B.dbf --f2024 C.dbf [--out tables/bps_microdata_results.json]"""
import argparse, json, struct
import numpy as np

SCEN = {"low": [100e6, 300e6, 2.5e9, 50e9], "mid": [150e6, 1.4e9, 26.25e9, 100e9], "high": [290e6, 2.4e9, 49e9, 500e9]}
BPS_2022_TOTAL = 783e12           # published e-commerce value, 2022 (Rp)
BI_2022 = 476.3e12                # Bank Indonesia e-commerce value, 2022 (Rp)
N_2020, N_2022, N_2023, N_2023_ALT = 2_361_423, 2_995_879, 3_816_750, 3_934_981


def read_dbf(path):
    b = open(path, "rb").read()
    n, hl, rl = struct.unpack("<I", b[4:8])[0], struct.unpack("<H", b[8:10])[0], struct.unpack("<H", b[10:12])[0]
    fields, o = [], 32
    while b[o] != 0x0D:
        fields.append((b[o:o + 11].split(b"\0")[0].decode().lower(), b[o + 16])); o += 32
    cols = {f: [] for f, _ in fields}
    for i in range(n):
        r, pos = b[hl + i * rl: hl + (i + 1) * rl], 1
        if r[:1] == b"*":      # deleted record
            continue
        for f, ln in fields:
            cols[f].append(r[pos:pos + ln].decode("latin1").strip()); pos += ln
    return cols


def num(col):
    out = []
    for v in col:
        try: out.append(float(v.replace(",", ".")))
        except ValueError: out.append(np.nan)
    return np.array(out)


def wshare(mask, w):
    ok = ~np.isnan(w)
    return float(100 * w[mask & ok].sum() / w[ok].sum())


def wmedian(x, w):
    ok = ~np.isnan(x) & ~np.isnan(w)
    x, w = x[ok], w[ok]
    if len(x) == 0: return float("nan")
    o = np.argsort(x); cw = np.cumsum(w[o])
    return float(x[o][np.searchsorted(cw, cw[-1] / 2)])


def bracket_value(cat, scen, monthly=False):
    v = np.array([SCEN[scen][int(c) - 1] if c in (1, 2, 3, 4) else np.nan for c in cat])
    return v * 12 if monthly else v


def check_weights(w, target, alt=None):
    s = float(np.nansum(w)); r = {"sum": s, "target": target, "within_1pct": abs(s / target - 1) <= 0.01}
    if alt: r.update(alt_target=alt, within_1pct_alt=abs(s / alt - 1) <= 0.01)
    return r


def file2023(c):
    w = num(c["w_usaha_fi"]); cat = num(c["kategori_p"]); off = num(c["r310a"]); mkt = num(c["r310b"])
    res = {"weights": check_weights(w, N_2022)}
    # bracket period: pick the reading whose mid total lies within 0.5x-2.0x of Rp783tn
    totals = {}
    for monthly in (False, True):
        for s in SCEN:
            v = bracket_value(cat, s, monthly) * (100 - off) / 100
            totals[("monthly" if monthly else "annual", s)] = float(np.nansum(v * w))
    ok = {p: 0.5 <= totals[(p, "mid")] / BPS_2022_TOTAL <= 2.0 for p in ("annual", "monthly")}
    period = "annual" if ok["annual"] else ("monthly" if ok["monthly"] else None)
    res["bracket_period"] = {"mid_total_over_783tn": {p: totals[(p, "mid")] / BPS_2022_TOTAL for p in ("annual", "monthly")}, "used": period}
    res["validation_passed"] = period is not None
    p_ = period or "annual"
    nobooks = num(c["r306"]) == 2
    for s in SCEN:
        online = bracket_value(cat, s, p_ == "monthly") * (100 - off) / 100 * w
        mval = bracket_value(cat, s, p_ == "monthly") * mkt / 100 * w
        res[f"E1_{s}"] = float(100 * np.nansum(online[nobooks]) / np.nansum(online))
        res[f"E2_{s}"] = float(100 * np.nansum(mval) / np.nansum(online))
    res["E1_count_share_nobooks"] = wshare(nobooks, w)
    # E8 (tax reach): share of marketplace online value from sellers with annual revenue of Rp300m or more (bracket 2-4); the marketplace tax
    # exempts individuals up to Rp500m, so this is an upper bound on the share the tax can reach (brackets do not split at Rp500m)
    above = cat >= 2
    for s in SCEN:
        mval_s = bracket_value(cat, s, p_ == "monthly") * mkt / 100 * w
        res[f"E8_{s}"] = float(100 * np.nansum(mval_s[above]) / np.nansum(mval_s))
    res["E8_count_share_marketplace_sellers_above_300m"] = wshare(above & (mkt > 0), w * (mkt > 0))
    # Reconciliation with Bank Indonesia (2022): how much of BPS's online value is marketplace, and marketplace sold to final consumers
    b2c = num(c["r314a"])
    for s in SCEN:
        rv = bracket_value(cat, s, p_ == "monthly") * w
        online = float(np.nansum(rv * (100 - off) / 100)); mk = float(np.nansum(rv * mkt / 100)); mk_b2c = float(np.nansum(rv * mkt / 100 * b2c / 100))
        res[f"recon_{s}"] = {"online_tn": online / 1e12, "marketplace_tn": mk / 1e12, "marketplace_b2c_tn": mk_b2c / 1e12,
                             "marketplace_over_BI": mk / BI_2022, "marketplace_b2c_over_BI": mk_b2c / BI_2022, "online_over_BI": online / BI_2022}
    # top-bracket calibration (sensitivity): top value X such that the mid total equals Rp783tn
    lo = bracket_value(cat, "mid", p_ == "monthly"); top = cat == 4
    rest = float(np.nansum((lo * (100 - off) / 100 * w)[~top])); top_mass = float(np.nansum(((100 - off) / 100 * w)[top]))
    X = (BPS_2022_TOTAL - rest) / top_mass if top_mass > 0 else float("nan")
    if p_ == "monthly": X = X / 12
    res["top_bracket_calibrated_value"] = X
    res["top_bracket_below_floor"] = bool(X < 50e9 * (1 / 12 if p_ == "monthly" else 1))
    res["E2b_marketplace_users_2022"] = wshare(num(c["r307e"]) == 1, w)
    start = num(c["r305"]); social = (num(c["r307c"]) == 1) | (num(c["r307d"]) == 1)
    res["E4_2022_social_or_chat_entrants_since2020"] = wshare(social & (start >= 2020), w * (start >= 2020))
    res["E4_2022_social_or_chat_before2020"] = wshare(social & (start < 2020), w * (start < 2020))
    res["_period"] = p_
    return res


def file2024(c):
    w = num(c["w_final"]); res = {"weights": check_weights(w, N_2023, N_2023_ALT)}
    mk = num(c["r309e"]) == 1; books = num(c["r308"]) == 1
    res["books_share_marketplace_users"] = wshare(books & mk, w * mk)
    res["books_share_others"] = wshare(books & ~mk, w * ~mk)
    res["records_check_passed"] = abs(res["books_share_marketplace_users"] - 28.63) <= 1 and abs(res["books_share_others"] - 12.25) <= 1
    res["E3_shopee"] = wshare(num(c["r309e_y_02"]) == 1, w); res["E3_tokopedia"] = wshare(num(c["r309e_y_01"]) == 1, w)
    start = num(c["r307"])
    res["E5_entrants_2023"] = wshare(start == 2023, w)
    alt = res["weights"].get("within_1pct_alt") and not res["weights"]["within_1pct"]
    res["E5_threshold"] = 23.9 if alt else 21.5
    d = num(c["r315"]); p = num(c["r315b"])
    signed = np.where(d == 1, p, np.where(d == 2, 0.0, np.where(d == 3, -p, np.nan)))
    inc = (start < 2023) & (start > 1900)
    res["E6_incumbent_median_change"] = wmedian(np.where(inc, signed, np.nan), w)
    res["E2b_marketplace_users_2023"] = wshare(mk, w)
    social = (num(c["r309c"]) == 1) | (num(c["r309d"]) == 1)
    res["E4_2023_social_or_chat_entrants_since2020"] = wshare(social & (start >= 2020), w * (start >= 2020))
    res["E4_2023_social_or_chat_before2020"] = wshare(social & (start < 2020), w * (start < 2020))
    return res


def file2021(c, period):
    w = num(c["w_usaha_fi"]); res = {"weights": check_weights(w, N_2020)}
    res["E2c_marketplace_users_2020"] = wshare(num(c["r307e"]) == 1, w)
    nobooks = num(c["r306"]) == 2; monthly = period == "monthly"
    online_a = bracket_value(num(c["rev_ol_set"]), "mid", False) * w        # online-revenue bracket is labelled yearly
    online_b = bracket_value(num(c["kategori_p"]), "mid", False) * (100 - num(c["sum_of_r36"])) / 100 * w
    res["E7_E1_2020_online_bracket"] = float(100 * np.nansum(online_a[nobooks]) / np.nansum(online_a))
    res["E7_E1_2020_revenue_x_share"] = float(100 * np.nansum(online_b[nobooks]) / np.nansum(online_b))
    return res


def _ge(a, b):
    return "n/a" if (a != a or b != b) else a >= b      # NaN-safe comparison


def verdicts(r21, r23, r24):
    v = {}
    if r23:
        v["E1 (mid share < 84.81%)"] = r23["E1_mid"] < 84.81 if r23["validation_passed"] else "range only"
        v["E2 (mid share > 18.23%)"] = r23["E2_mid"] > 18.23 if r23["validation_passed"] else "range only"
        v["E8 (>=Rp300m sellers hold > half of marketplace value, mid)"] = r23["E8_mid"] > 50 if r23["validation_passed"] else "range only"
        v["RBI (marketplace B2C slice below BI 2022)"] = r23["recon_mid"]["marketplace_b2c_over_BI"] < 1
        v["E2b (2022 users >= 17.23%)"] = _ge(r23["E2b_marketplace_users_2022"], 17.23)
        v["E4 2022 (entrants >= earlier)"] = _ge(r23["E4_2022_social_or_chat_entrants_since2020"], r23["E4_2022_social_or_chat_before2020"])
    if r24:
        v["E3 (Shopee >= Tokopedia)"] = _ge(r24["E3_shopee"], r24["E3_tokopedia"])
        v["E5 (entrants >= threshold)"] = _ge(r24["E5_entrants_2023"], r24["E5_threshold"])
        v["E6 (median <= +10.36%)"] = _ge(10.36, r24["E6_incumbent_median_change"])
        v["E4 2023 (entrants >= earlier)"] = _ge(r24["E4_2023_social_or_chat_entrants_since2020"], r24["E4_2023_social_or_chat_before2020"])
    if r21 and r23:
        v["E2c (2020 users >= 2022 users)"] = _ge(r21["E2c_marketplace_users_2020"], r23["E2b_marketplace_users_2022"])
        v["E7 (2022 E1 >= 2020 E1 - 5)"] = _ge(r23["E1_mid"], r21["E7_E1_2020_online_bracket"] - 5) if r23["validation_passed"] else "range only"
    return v


if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("--f2021"); a.add_argument("--f2023"); a.add_argument("--f2024"); a.add_argument("--out")
    x = a.parse_args()
    r23 = file2023(read_dbf(x.f2023)) if x.f2023 else None
    r24 = file2024(read_dbf(x.f2024)) if x.f2024 else None
    r21 = file2021(read_dbf(x.f2021), r23["_period"] if r23 else "annual") if x.f2021 else None
    out = {"file2021": r21, "file2023": r23, "file2024": r24, "verdicts": verdicts(r21, r23, r24)}
    s = json.dumps(out, indent=1, default=str); print(s)
    if x.out: open(x.out, "w").write(s)
