# Advisor feedback-pattern audit — 14 September 2026

Not a check against individual comments but against the **pattern** in them: what Prof. Kong asks for
repeatedly, what she escalates when unsatisfied, and what she is therefore likely to ask next.

Source: all 40 tracked comments across her two marked drafts — 21 on `Invisible_Ledger_Aug1426(1)`
and 19 on `Invisible_Ledger_Sept0126`, extracted from `word/comments.xml` in each.

## The ten recurring themes

| # | Theme | Comments | Signal |
|---|---|---|---|
| A | Define every term and abbreviation at first use | 107, 161, 163, 130, 178, 217, 109 | Raised in **both** rounds — her most repeated request of any kind |
| B | Pick one term and one currency, then stay consistent | 130, 178, 217, 214 | Repeated after being asked once; she named the winner (GTV, USD) |
| C | Tables: explain in text, informative captions, consistent placement and numbering | 2, 119, 125, 154, 162, 174, 177, 192 | Eight comments — her largest single cluster |
| D | State geographic and business scope for every sample | 109, 153, 170, 189, 200, 203 | **Absent in August, six comments in September** — sharply escalating |
| E | Provenance: is this proxy yours or from the literature? | 89, 114 | "I *still* do not know" — explicitly unsatisfied on re-ask |
| F | Justify non-standard sources | 146 | Written with six question marks |
| G | Cite finance, not only economics | 88 | She attached a finance journal ranking file |
| H | Use all available data; explain gaps | 159, 160, 164, 167 | Drove the longitudinal rebuild |
| I | Express findings at economic scale | 165 | **Her own suggestion**, with a figure for us to verify |
| J | Comply with YZU formatting | 0, 2, 26, 215 | Bracketing both rounds |

The escalation pattern matters more than any single item. Themes A, B and E were raised in August and
raised **again** in September in sharper language. Anything she has asked for twice and not received
should be treated as the highest risk in the examination.

## Audit result against the current proposal

**Passing before this audit.** Theme E is answered directly and prominently — "The measure is my own
construction for this paper rather than one adopted from a prior study" — which closes her most
pointed repeated question. Theme D is answered structurally: the evidence-tier design exists precisely
to keep geographic scope visible, and tiers are never pooled into one monetary total. Theme F is
answered — Momentum Works is named, explained and justified in §4.4. Captions are consistently placed
above every table, numbering is sequential 1–8 with no "Table 3B" construction, and USD is used
throughout with the single Rp figure carrying a USD conversion.

**Eight failures found and fixed.**

| Theme | Failure | Fix |
|---|---|---|
| C | Tables 1, 2, 3, 6, 7 and 8 were never named in the prose — six of eight tables, against the cluster she has commented on eight times | Each table now introduced by name with its purpose and main insight |
| B | GTV and GMV both used, including "GTV/GMV" in Appendix A, after she twice said to choose GTV | GTV throughout; a terminology note records each issuer's own label |
| A | "take rate" used undefined, after she asked what it means and supplied the definition herself | Defined at first use, with the Ecosystem Ratio given as its complement, *E = 1/(take rate) − 1* |
| A | BPS and PMK never expanded anywhere in the document | Both expanded at first occurrence |
| I | The GDP-share framing she proposed herself was absent entirely | §5.1 now reports ~2.9% of 2023 GDP, with World Bank and FRED figures agreeing to 0.0002%, and states plainly that the wedge is not value added |
| J | ~~No references section at all~~ **Retracted — this finding was wrong.** The audit grepped the markdown source, but the references section is emitted by the build script, so it was present in the built document all along. A duplicate was briefly added and has been removed. | Berg et al. (2020), *Review of Financial Studies*, added to the existing list |
| J | Abstract 171 words against her stated 100–150 | 149 words |
| A/J | Appendix A gave variable definitions but not data sources, which she asked for in August | Data-source table added by evidence tier |

## What she is likely to ask next

Extrapolating the same pattern rather than the same comments:

1. **"Which one number is the answer?"** The tier design deliberately refuses a single pooled total.
   That is defensible, but Theme C shows she wants results stated, not just structured. Have the
   one-sentence answer ready: the FY2023 selected-platform wedge is US$40.07bn at an Ecosystem Ratio
   of 12.671, and it is a sum of three documented cases, not a national estimate.
2. **Theme G is still only partly met.** Of roughly seventeen cited works, three are finance or
   accounting (De Franco et al.; Barrios et al.; the IFRS material) against a clear majority from
   economics. She raised this once and supplied a ranking file; on her pattern, the second ask will be
   sharper.
3. **Theme D will extend to the corroboration module.** The 48 matched issuer-years across eight
   non-Indonesian platforms is exactly the kind of sample she asked scope questions about six times in
   September. It is labelled corroboration, but expect "what is the geographic coverage of this table?"
4. **Theme H on the remaining gaps.** She asked why some years had only one or two quarters. The
   equivalent question here is why Blibli enters at FY2021 in one universe and FY2020 in the other.
   The answer is documented in the prospectus-extension rule; it should be sayable out loud.
5. **Theme J on YZU formatting.** She has raised it in both rounds and it remains the one item that
   cannot be verified from here — it needs the department's current template.

## Outstanding

- **Eight references could not be sourced from this repository** and were supplied from general
  knowledge: Barrios et al.; Caillaud and Jullien; Evans and Schmalensee; Kleven, Kreiner and Saez
  (2016); Medina and Schneider; Naritomi; Parker and Van Alstyne; and Momentum Works. These must be
  checked against the actual sources before submission. **Denes, Lagaras and Tsoutsoura (2025) could
  not be verified at all** and is marked in the reference list as requiring completion — complete it
  from the source copy or remove the citation.
- The document is now 14 pages, up from 12, of which the references and appendix account for roughly
  two. The argument itself has not lengthened.

---

# Addendum — Theme G, the finance-citation balance

Her August comment 88 read: *"I checked the references you have cited, most of them are econ papers.
Please include some finance papers. I uploaded a file (i.e., Journal Ranking in Finance)."*

That attachment was located at
`Molina-Optiplex/Sharpe-Renaissance/drive/dropbox_snapshot/Chris/Journal Ranking in Finance.pdf`. It is
an image-only PDF, so it was rendered and read as pages. It is the Taiwanese general-finance journal
grading table (表 4, 一般財務領域期刊分級結果):

| Grade | Count | Journals |
|---|---|---|
| **A+** | 4 | Journal of Finance; Journal of Financial Economics; Review of Financial Studies; Journal of Financial and Quantitative Analysis |
| **A Tier-1** | 16 | Review of Finance; Journal of Banking and Finance; Journal of Money, Credit and Banking; Review of Corporate Finance Studies; Journal of Financial Intermediation; Journal of Corporate Finance; Review of Asset Pricing Studies; Journal of Financial Markets; Financial Management; Journal of Empirical Finance; Mathematical Finance; Journal of International Money and Finance; Journal of Financial Econometrics; Critical Finance Review; Financial Analysts Journal; Journal of Business, Finance & Accounting |
| **A Tier-2** | 14 | Journal of Financial Stability; Pacific-Basin Finance Journal; European Financial Management; Journal of Futures Markets; Journal of Accounting, Auditing & Finance; Journal of Financial Services Research; and others |

This is a grading table, not a reading list — it tells us which outlets count, not which papers to cite.

## What changed

**Berg, Burg, Gombović and Puri (2020),** *Review of Financial Studies* — **A+** — was already in this
repository's reference list and used in the integrated manuscript, but had never reached the proposal.
It is now cited in §2.3, where it does real work rather than decorating the list: their result that a
digital footprint predicts default as well as a bureau score establishes that intermediary-held
transaction traces are economically informative even when conventional records are thin, which is
exactly the asymmetry the invisible wedge measures.

**Barrios, Hochberg and Yi (2022),** *Journal of Financial Economics* — **A+** — was already cited;
the sentence now names the journal and states what the paper contributes.

**Denes, Lagaras and Tsoutsoura (2025) is retained.** It was briefly removed as unverifiable, which
was a mistake with the same root cause: the reference list lives in the build script's content module,
not the markdown, and it carries the entry in full — *Entrepreneurship and the gig economy: Evidence
from U.S. tax returns*, Journal of Financial Economics, 173, 104156. JFE is A+ on the advisor's own
ranking, so this is a finance citation that was already in place.

The built list carries 20 entries, of which five are finance or accounting — **three of them in A+
journals** (Barrios et al. and Denes et al. in JFE, Berg et al. in RFS). That is a real improvement on the balance she objected to, but it is still a minority.

## What remains, and why it is not done here

Closing Theme G properly needs two or three more citations from the graded outlets. Those are not
added here because no further verifiable candidates exist in this repository, and inventing
publication details for a submitted thesis proposal is not an acceptable trade. The gap is therefore
stated rather than filled.

The three most promising directions, each mapped to a section that already needs support:

1. **§2.2, accounting and revenue recognition** — gross-versus-net presentation and non-GAAP metric
   disclosure. *Journal of Business, Finance & Accounting* (A Tier-1) and *Journal of Accounting,
   Auditing & Finance* (A Tier-2) publish directly on this, and the topic is the analytical core of
   the wedge: whether facilitated commerce is booked gross or net is what creates the gap being
   measured.
2. **§2.1, platform economics** — platform and marketplace business models in *Journal of Financial
   Intermediation* or *Journal of Corporate Finance* (both A Tier-1). This would replace or supplement
   the current reliance on Rochet–Tirole and Armstrong, which are economics rather than finance.
3. **§5, the Indonesian and Southeast Asian setting** — *Pacific-Basin Finance Journal* (A Tier-2) is
   the natural venue for regional work and would additionally signal awareness of where this paper
   could itself be submitted.

A search of those outlets on "platform", "marketplace", "gross merchandise value", "revenue
recognition" and "digital intermediary" should produce candidates quickly. Each new citation should
earn its place in an argument, since Theme C shows the advisor reads for whether material is used, not
merely present.
