"""Advisor preview package (12 Oct 2026): the progress deck, the charts and one data workbook, zipped for Dropbox.
Only committed aggregates go in: national weighted totals from the BPS files, firm-level ratios from public filings, regression
coefficients from the market test. Licensed microdata (BPS SILASTIK) and licensed market values (LSEG) are never copied (data-use terms).
Run from this folder: python3 advisor_package.py -> ../../papers/advisor_package_2026-10/"""
import csv, json, pathlib, shutil, zipfile
import pandas as pd

HERE = pathlib.Path(__file__).parent; T = HERE / "tables"
OUT = HERE.parent.parent / "papers" / "advisor_package_2026-10"; OUT.mkdir(parents=True, exist_ok=True)
J = lambda n: json.load(open(T / n))

sheets = {}
sheets["README"] = pd.DataFrame({"Item": [
    "What this is", "Same thesis", "Sheets", "Charts", "Not included", "Built from"], "Note": [
    "Data behind the progress deck of 9 Oct 2026 (what has changed since the proposal oral of 1 Oct). One sheet per slide topic.",
    "Title, research question, H1, H2 and the measures are unchanged from the 27 Sep proposal.",
    "Wedge_2023, H1_firms, Revenue_changes, Tokopedia_2023, Market_test, Verdict_2023, Seller_rise, Seller_profile, Part_year_selling, Seller_answers, Tax_reach, Rules_abroad.",
    "charts/ holds the figures used in the deck and the thesis.",
    "BPS survey microdata and LSEG market values stay on the researcher's machine (data-use agreements). Only national totals and coefficients are shown.",
    "Committed tables in the thesis repository (research/option_space_2026-10-01/tables); every number is rebuilt by rebuild_all.sh (272 ledger checks pass)."]})
sheets["Wedge_2023"] = pd.DataFrame([
    ["Tokopedia", 16.33, 0.41, 15.93, 39.3, "Issuer-reported"], ["Shopee", 21.52, 2.15, 19.37, 9.0, "Constructed (assumed take rate 9-11%)"],
    ["Grab Indonesia", 5.38, 0.61, 4.78, 7.9, "Constructed"], ["Total", 43.23, 3.16, 40.07, 12.7, ""]],
    columns=["Platform", "Transaction value (US$bn)", "Revenue (US$bn)", "Invisible wedge (US$bn)", "Ecosystem ratio (wedge / revenue)", "Evidence"])
f = pd.read_csv(T / "h1_points_vs_log_firms.csv").rename(columns={"firm": "Firm", "group": "Group", "share_kept_pct": "Take rate (% of transaction value, median)",
    "change_points": "Yearly change in take rate (points, median)", "change_log": "Yearly change in take rate (relative, log, median)", "n": "Year pairs"})
sheets["H1_firms"] = f.sort_values(["Group", "Firm"], ascending=[False, True])
g = pd.read_csv(T / "growth_decomposition.csv").rename(columns={"firm": "Firm", "seg": "Segment", "window": "Years", "revenue_growth_pct": "Revenue growth (%)",
    "volume_growth_pct": "Transaction value growth (%)", "take_rate_start_pct": "Take rate start (%)", "take_rate_end_pct": "Take rate end (%)",
    "share_from_volume": "Share from more buying", "share_from_fee": "Share from higher fees", "share_from_discount_cut": "Share from fewer discounts"})
sheets["Revenue_changes"] = g
sheets["Tokopedia_2023"] = pd.DataFrame([["Gross revenue", 8143.239, 8988.909], ["Customer incentives (deducted)", 4112.320, 2813.719], ["Net revenue", 4030.919, 6175.190]],
    columns=["Third-party e-commerce segment (Rp bn)", "2022 (restated)", "2023"]).assign(Note=["", "Lower incentives explain 60.6% of the net revenue rise", "Transaction value fell 8.9%"])
m = J("m1_market_value_results.json")
sheets["Market_test"] = pd.DataFrame([[v["label"], v["firms"], v["firm_years"], v["b1_volume"], v["se_b1"], v["b2_take_rate"], v["se_b2"], v["p_one_sided_b1_gt_0"], v["p_one_sided_b1_gt_b2"]]
    for v in m.values() if isinstance(v, dict) and "b1_volume" in v],
    columns=["Sample", "Firms", "Firm-years", "b1 (transaction value growth)", "SE b1", "b2 (take-rate growth)", "SE b2", "p (b1 > 0)", "p (b1 > b2)"])
v = J("h1_groundwork.json")["verdict_2023"]
rows = [("Tokopedia revenue", v["platform_revenue_growth_pct"]["Tokopedia"], "Headline"), ("BPS e-commerce value (published)", v["BPS_value_growth_pct"], "Headline"),
        ("BPS online sellers (published)", v["BPS_published_seller_growth_pct"], "Headline"), ("Household spending (nominal)", v["household_spending_nominal_growth_pct"], "Reference")]
rows += [(k, x, "Buying through platforms") for k, x in v["buying_growth_pct"].items()]
sheets["Verdict_2023"] = pd.DataFrame(rows, columns=["Measure", "Growth 2023 vs 2022 (%)", "Kind"])
ra = J("bps_rise_accounting.json")
sheets["Seller_rise"] = pd.DataFrame([["Published rise in online sellers, 2022 to 2023", ra["rise_k"]], ["Started selling online in 2023", ra["entrants_k"]],
    ["Selling before 2023, above the whole 2022 count (no exits)", ra["scenarios"]["no_exits"]["newly_counted_k"]],
    ["Same, if sellers stopped at the 2020-22 rate", ra["scenarios"]["reference"]["newly_counted_k"]],
    ["Share of rise not explained by first-time entry, low (%)", ra["scenarios"]["no_exits"]["newly_counted_share_of_rise_pct"]],
    ["Share of rise not explained by first-time entry, high (%)", ra["scenarios"]["reference"]["newly_counted_share_of_rise_pct"]],
    ["Entry test (registered 2 Oct): needed share starting in 2023 (%)", 21.5], ["Entry test: observed share starting in 2023 (%)", 13.45]],
    columns=["Item", "Thousand sellers or %"])
p = J("bps_newly_counted_profile.json")["profile"]
prow = []
for grp, cats in p.items():
    for cat, x in cats.items():
        prow.append([grp, cat, x["share_of_2022_count_pct"], x.get("share_of_beyond_normal_pct"), x["counted_2022_k"], x["pre2023_in_2023_k"]])
sheets["Seller_profile"] = pd.DataFrame(prow, columns=["Trait", "Group", "Share of 2022 count (%)", "Share of extra sellers beyond normal change (%)",
                                                      "2022 count (thousand)", "Pre-2023 sellers in 2023 survey (thousand)"])
r = J("bps_returning_check.json")["same_start_year_groups"]
sheets["Part_year_selling"] = pd.DataFrame([[k, y, x["all_12_months_k"], x["part_year_k"], x["part_year_pct"]] for k, ys in r.items() for y, x in ys.items()],
    columns=["Sellers who", "Survey year", "Sold every month (thousand)", "Sold part of the year (thousand)", "Part-year share (%)"])
d = J("bps_descriptives.json"); gl = J("gel_checks.json")
sheets["Seller_answers"] = pd.DataFrame([["Existing sellers: online sales up (%)", d["incumbents_2023_revenue_direction"]["up"]],
    ["Existing sellers: about the same (%)", d["incumbents_2023_revenue_direction"]["same"]], ["Existing sellers: down (%)", d["incumbents_2023_revenue_direction"]["down"]],
    ["Main complaint 'lack of demand', 2023 (%)", 41], ["Main complaint 'lack of demand', 2022 (%)", 35],
    ["Sellers using a marketplace, 2020 / 2022 / 2023 / 2024 (%)", "21.6 / 19.8 / 17.8 / 17.2"],
    ["Keep complete financial statements, 2020 / 2022 / 2023 (%)", " / ".join(f"{d['books_share'][k]:.1f}" for k in ["2020", "2022", "2023"])]],
    columns=["Item", "Value"])
t = J("part6_checks.json")
sheets["Tax_reach"] = pd.DataFrame([["Online sellers who can be taxed (upper bound, %)", t["tax_seller_reach_pct"]],
    ["Online sales value they hold, 2022 (%)", f"{t['tax_value_reach_pct_2022']['low']:.0f}-{t['tax_value_reach_pct_2022']['mid']:.0f}"],
    ["Marketplace sellers on record, 2023 (% of online sellers)", t["marketplace_sellers_share_pct"]["2023"]],
    ["Sellers outside marketplaces who want to join one (%)", t["off_marketplace_wanting_to_join_pct"]],
    ["Grab: rides as share of on-demand transaction value (%)", t["grab_rides_share_of_ondemand_gmv_pct_last4q"]]], columns=["Item", "Value"])
sheets["Rules_abroad"] = pd.read_csv(T / "src/platform_seller_rules_intl.csv")

xl = OUT / "IL_Data_Package_2026-10.xlsx"
with pd.ExcelWriter(xl, engine="openpyxl") as w:
    for name, df in sheets.items():
        df.round(3).to_excel(w, sheet_name=name, index=False)
        ws = w.sheets[name]
        for col in ws.columns:
            width = max(len(str(c.value)) if c.value is not None else 0 for c in col)
            ws.column_dimensions[col[0].column_letter].width = min(max(12, width + 2), 70)
        ws.freeze_panes = "A2"

(OUT / "charts").mkdir(exist_ok=True)
for src, dst in [("exhibits/v2/1_thin_slice.png", "1_thin_slice.png"), ("exhibits/v2/2_tokopedia_2023.png", "2_tokopedia_2023.png"),
                 ("exhibits/6_verdict_2023.png", "3_verdict_2023.png"), ("exhibits/5_bps_own_answers.png", "4_sellers_own_answers.png"),
                 ("exhibits/v2/3_who_they_are.png", "5_who_they_are.png"), ("exhibits/v2/4_full_year_sellers.png", "6_part_year_selling.png"),
                 ("exhibits/v2/5_tax_reach.png", "7_tax_reach.png")]:
    shutil.copy(HERE / src, OUT / "charts" / dst)
for n in ["IL_Progress_Update_2026-10-09.pptx", "IL_Progress_Update_2026-10-09_preview.pdf"]:
    shutil.copy(HERE / "deck" / n, OUT / n)
(OUT / "README.txt").write_text(
    "The Invisible Ledger: progress since the proposal oral (Christopher Ongko, 12 Oct 2026)\n\n"
    "1. IL_Progress_Update_2026-10-09.pdf (or .pptx): 14 slides on what changed since 1 October.\n"
    "2. IL_Data_Package_2026-10.xlsx: the numbers behind each slide, one sheet per topic (see the README sheet).\n"
    "3. charts/: the figures used in the slides and the thesis.\n\n"
    "Same title, research question, hypotheses and measures as the approved proposal. BPS survey microdata and licensed market data\n"
    "are not included (data-use agreements); only national totals and test results are shown.\n", encoding="utf-8")
z = OUT.parent / "IL_Advisor_Package_2026-10-12.zip"
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for fp in sorted(OUT.rglob("*")):
        if fp.is_file(): zf.write(fp, fp.relative_to(OUT.parent))
print(xl, len(sheets), "sheets"); print(z, round(z.stat().st_size / 1e6, 2), "MB")
