"""Curated definition map for the transaction-value measure V (2 Oct 2026).  Every row's quote is pulled programmatically from a saved source text and the script FAILS if a snippet
is not found, so nothing here is retyped.  Sources: scratchpad/worktree copies of company filings and BPS OCR (paths in SRC; not committed because of size; the sentences are in the CSV).
Columns: platform, metric, topic (what V includes/excludes, scope, definition change, or disclosure change), source_file, quote."""
import glob, re, sys, pandas as pd
W = "/home/phyrexian/.local/state/grok-muscle/worktrees/"
SCR = "/home/phyrexian/.cache/tmp/claude-1000/-home-phyrexian-Downloads-Invisible-ledger/9307ea4a-56d1-4788-8561-9702a4860971/scratchpad/"
G = "/home/phyrexian/Downloads/Invisible_Ledger_Coverage_Expansion_2026-09-09/broad_archive/text/goto/"
def path(p):
    h = glob.glob(p); assert h, p; return h[0]
ITEMS = [
 ("Shopee (Sea)", "GMV", "includes shipping; group-wide", W + "corpus_bps-*/sea_20f_2024.txt", "calculation of GMV for our e-commerce platform includes shipping"),
 ("GoTo", "GTV", "what GTV sums", W + "corpus_bps-*/goto_fy2023.txt", "GTV means gross transaction value, an operating measure representing"),
 ("GoTo", "GTV", "2024 restatement adds tolls and tips", W + "corpus_bps-*/goto_fy2024.txt", "GTV has been restated to include any additional fees"),
 ("Tokopedia (GoTo)", "GTV", "core GTV excludes digital goods, cars, motorcycles", G + "*4Q23_20Earnings_20Presentation.pdf.txt", "Core GTV: excludes digital goods and sales of cars and motorcycles"),
 ("Tokopedia (GoTo)", "GTV", "digital goods share of GTV, mid-2022", G + "*2022-Aug-30-GOTO.JK-Transcript.pdf.txt", "digital goods is roughly 18% to 20% of GTV"),
 ("Blibli", "TPV", "paid and delivered purchases; 3P includes tiket.com travel", SCR + "corpus_blibli/blibli_fy2022.txt", "Total Processing Value (“TPV”) is total value of paid and delivered purchases"),
 ("Blibli", "Take rate", "GPBD adds back discounts and subsidies", SCR + "corpus_blibli/blibli_fy2022.txt", "after adding back discount and subsidies"),
 ("Bukalapak", "TPV", "paid purchases incl. physical and virtual products", SCR + "corpus_buka/bukalapak_sr2021_mirror.txt", "volume of Rupiah from paid purchases facilitated by the Company"),
 ("Bukalapak", "TPV", "reporting stopped Q4 2024", SCR + "corpus_buka/bukalapak_sr2024_mirror.txt", "no longer reports TPV"),
 ("Bukalapak", "TPV", "strategy: profitability over TPV growth", SCR + "corpus_buka/bukalapak_ar2022_mirror.txt", "focus on profitability instead of TPV growth"),
 ("Grab", "GMV", "financial-services GMV discontinued", SCR + "corpus_grab_ipo/GRAB_20-F_2025-03-14.txt", "discontinued the reporting of GMV for our financial services segment"),
 ("Grab", "GMV", "adds ads and rentals; includes offline-store sales", SCR + "corpus_grab_ipo/GRAB_20-F_2025-03-14.txt", "GMV includes (i) sales made through offline stores"),
 ("BPS", "e-commerce transaction value", "what BPS counts", SCR + "bps_local/bps_2024_ocr_all.txt", "includes all receipts from online"),
 ("BPS", "e-commerce transaction value", "survey scope: marketplace share of value", SCR + "bps_local/bps_2024_ocr_all.txt", "accounted for only 15.79"),
]
rows = []
for plat, metric, topic, p, snip in ITEMS:
    f = path(p); t = open(f, errors="ignore").read(); t = re.sub(r"\s+", " ", t)
    i = t.find(snip); assert i >= 0, (plat, snip)
    a = max(0, i - 60); b = min(len(t), i + len(snip) + 260)
    rows.append(dict(platform=plat, metric=metric, topic=topic, source_file=f.split("/")[-1], quote=t[a:b].strip()))
D = pd.DataFrame(rows); D.to_csv("tables/v_definition_map.csv", index=False); print(len(D), "rows, all quotes found")
for r in D.itertuples(): print("-", r.platform, "|", r.topic, "|", r.quote[:200])
