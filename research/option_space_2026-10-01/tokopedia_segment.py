"""Tokopedia (GoTo e-commerce segment) gross revenue, incentives and net revenue, FY2022-FY2023, from the audited segment note (1 Oct 2026).
Cross-checks the proposal's Tokopedia bridge (net revenue +53.2%, 60.6% from lower incentives) against a SECOND source: the audited
consolidated financial statements. Identity: gross - incentives = net. Run: python3 tokopedia_segment.py <broad_archive/text/goto>
"""
import pathlib, re, sys
import pandas as pd
# IDR million, 'E-commerce' column, third parties (FY2023 statements: first table = FY2023, second = FY2022)
seg = pd.DataFrame({"gross": [8_143_239, 8_988_909], "incentives": [4_112_320, 2_813_719], "net": [4_030_919, 6_175_190]}, index=[2022, 2023])
assert ((seg.gross - seg.incentives - seg.net).abs() <= 1).all()
if len(sys.argv) > 1:
    t = "".join(p.read_text(errors="ignore") for p in pathlib.Path(sys.argv[1]).glob("*LK_20GOTO_31_20Des_202023*.txt"))
    for y, row in seg.iterrows():
        print(f"FY{y}: all three numbers found in audited statements:", all(f"{v:,}" in t for v in row))
g = seg.loc[2023] - seg.loc[2022]
print(seg.to_string()); print(f"\nnet revenue change {g.net:,} = gross change {g.gross:,} + incentive reduction {-g.incentives:,}")
print(f"net +{100*g.net/seg.loc[2022].net:.1f}%  | incentive reduction = {100*(-g.incentives)/g.net:.1f}% of the net change; gross = {100*g.gross/g.net:.1f}%   (proposal: +53.2%, 60.6% / 39.4%)")
gtv = pd.Series({2022: 273_146_000, 2023: 248_829_000})  # IDR million; repo FY2022 value; FY2023 = USD 16.331bn x 15,236.88
for y in (2022, 2023): print(f"{y}: gross take {100*seg.loc[y].gross/gtv[y]:.2f}%  incentives {100*seg.loc[y].incentives/gtv[y]:.2f}%  net take {100*seg.loc[y].net/gtv[y]:.2f}%")
seg.to_csv(pathlib.Path(__file__).parent / "tables/tokopedia_segment.csv")
