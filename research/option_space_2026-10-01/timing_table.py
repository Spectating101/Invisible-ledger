"""Timing: did funding conditions, company decisions or government policy come first? (2 Oct 2026, descriptive; no causal claim)
Inputs: tables/src/events_extraction.csv (36 dated events, quote-verified), tables/grab_quarterly_verified.csv (incentives % of on-demand GMV), GoTo's own statements (verified
quotes in tables/src/goto_2021_extraction.csv: 1Q22 'reduced ... incentives ... as a percentage of GTV by 90 basis points QoQ'; 2Q22 incentives -3.5% of GTV, -52 bp QoQ),
Blibli 1Q23 release (published 3P rate adjusted from March 2023), and market conditions from LSEG daily closes (Nasdaq composite; licensed, not committed; passed as argument).
Sourced events only: Kepmenhub 667/2022, PP 80/2019, Permendag 50/2020, Grab's SPAC listing and layoffs, Perpres 27/2026 and the PMK 37/2025 deferral instruments could NOT be sourced and are absent."""
import sys, pandas as pd, numpy as np
ev = pd.read_csv("tables/src/events_extraction.csv")
ev = ev.drop_duplicates(subset=["period", "entity", "field"]).sort_values("period")[["period", "entity", "field", "note"]]
ev["kind"] = ev.field.map({"tax_rule": "policy: tax", "regulation": "policy: trade", "incentive_policy": "policy: commission cap (company)", "ipo": "capital markets", "listing": "capital markets",
                           "merger": "company", "deconsolidation": "company", "restructuring": "company"})
g = pd.read_csv("tables/grab_quarterly_verified.csv", index_col=0)
gq = pd.DataFrame({"period": [f"{q[:4]}-{int(q[-1])*3:02d}-28" for q in g.index], "entity": "Grab", "field": "incentive_pct_gmv",
                   "note": [f"incentives {i:.1f}% of on-demand GMV; net take rate {m:.1f}%" for i, m in zip(g.iota_pct, g.m_pct)], "kind": "company: incentives (data)"})
extra = pd.DataFrame([
    dict(period="2022-03-31", entity="GoTo", field="incentive_cut", note="1Q22: incentives cut by 90 bp of GTV QoQ (company statement)", kind="company: incentives (statement)"),
    dict(period="2022-06-30", entity="GoTo", field="incentive_cut", note="2Q22: total incentives -3.5% of GTV, down 52 bp QoQ (company statement)", kind="company: incentives (statement)"),
    dict(period="2023-03-31", entity="Blibli", field="rate_change", note="3P published seller rate adjusted from March 2023 (company release); net take 0.32% -> 2.07%", kind="company: incentives (statement)")])
T = pd.concat([ev, gq[gq.period < "2024-01-01"], extra]).sort_values("period")
if len(sys.argv) > 1:
    n = pd.read_csv(sys.argv[1]); n["date"] = pd.to_datetime(n.date); n = n.set_index("date").close.sort_index()
    pk = n["2021-01-01":"2022-06-30"].idxmax(); print("Nasdaq composite peak in window:", pk.date(), f"{n[pk]:.0f}")
    T["nasdaq_drawdown_pct"] = [round(100 * (n[:pd.Timestamp(p)].iloc[-1] / n[:pk].max() - 1), 1) if pd.Timestamp(p) >= pk else np.nan for p in T.period]
T.to_csv("tables/timing_table.csv", index=False)
pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 105); pd.set_option("display.max_rows", 120)
S = T[(T.period >= "2021-05-01") & (T.period <= "2024-06-30")]
print(S.drop(columns=["field"]).to_string(index=False))
