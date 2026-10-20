// Progress update deck: what has changed since the proposal oral (1 Oct 2026). Built 9 Oct 2026.
// Follows NARRATIVE_ARC.md and the voice of GOLDEN_PITCH.md; charts are the slide versions from exhibits.py and
// exhibits_v2.py (IL_DECK=1 -> exhibits/deck/). Visual system carried over from the v4.10 oral deck (paper background,
// Montserrat titles); body text in Calibri. Static chart images keep the thesis figures and the slides identical.
// Run: NODE_PATH=<dir with pptxgenjs> node deck/progress_deck.js <out.pptx>
const path = require("path");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const HERE = __dirname, EX = path.join(HERE, "..", "exhibits", "deck"), AS = path.join(HERE, "assets");
const OUT = process.argv[2] || path.join(HERE, "IL_Progress_Update_2026-10-09.pptx");
const THEME = {
  name: "Invisible Ledger", headFontFace: "Montserrat", bodyFontFace: "Calibri",
  colors: { dk1: "1A1A1A", lt1: "FFFFFF", dk2: "1F4E5F", lt2: "F1EFEA", accent1: "1E88A8", accent2: "BF4B33",
            accent3: "1F4E5F", accent4: "8A8782", accent5: "A33A2C", accent6: "5F5C57", hlink: "1E88A8", folHlink: "5F5C57" },
};
const INK = "1A1A1A", INK2 = "3A3834", MUTED = "5F5C57", FAINT = "8A8782", TEAL = "1F4E5F", BRICK = "A33A2C", CARD = "FAF9F6", LINE = "D9D5CD";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";             // 13.333 x 7.5 in, as the oral deck
pres.title = "The Invisible Ledger: progress since the proposal oral";
pres.author = "Christopher Ongko";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };

pres.defineSlideMaster({
  title: "IL Title", background: { path: path.join(AS, "paper_title.jpeg") },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.0, w: 11.7, h: 0.9, fontFace: "Montserrat", fontSize: 40, bold: true, color: INK, align: "center", valign: "middle", margin: 0 }, text: "" } }],
});
pres.defineSlideMaster({
  title: "IL Content", background: { path: path.join(AS, "paper.jpeg") },
  margin: [0.5, 0.6, 0.6, 0.6],
  objects: [
    { rect: { x: 0.6, y: 0.42, w: 0.38, h: 0.05, fill: { color: INK } } },
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.5, w: 12.1, h: 0.62, fontFace: "Montserrat", fontSize: 26, bold: true, color: INK, align: "left", valign: "middle", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "quote", type: "body", x: 0.6, y: 1.12, w: 12.1, h: 0.45, fontFace: "Calibri", fontSize: 15, italic: true, color: INK2, valign: "top", margin: 0 }, text: "" } },
    { text: { text: "THE INVISIBLE LEDGER   ·   PROGRESS SINCE THE PROPOSAL ORAL", options: { x: 0.6, y: 7.05, w: 8, h: 0.25, fontFace: "Calibri", fontSize: 9, color: FAINT, charSpacing: 1, margin: 0 } } },
  ],
  slideNumber: { x: 12.3, y: 7.05, w: 0.45, h: 0.25, fontFace: "Calibri", fontSize: 9, color: FAINT, align: "right" },
});

let n = 0;
function content(section, title, quote, notes) {
  const s = pres.addSlide({ masterName: "IL Content", sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  if (quote) s.addText(quote, { placeholder: "quote" });
  if (notes) s.addNotes(notes);
  n += 1; return s;
}
function txt(s, runs, o) { s.addText(runs, Object.assign({ isTextBox: true, fontFace: "Calibri", fontSize: 14, color: INK2, valign: "top", margin: 0, paraSpaceAfter: 6 }, o)); }
function label(s, t, o) { txt(s, t, Object.assign({ fontSize: 11, bold: true, color: TEAL, charSpacing: 1 }, o)); }
function b(t) { return { text: t, options: { bold: true, color: INK } }; }
function para(parts, last) { const p = parts.map(x => (typeof x === "string" ? { text: x } : x)); if (!last) p[p.length - 1].options = Object.assign({}, p[p.length - 1].options, { breakLine: true }); return p; }
function bullets(items) { return items.map((it, i) => ({ text: it, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1 } })); }
function img(s, file, x, y, w, ratio) { s.addImage({ path: path.join(EX, file), x, y, w, h: w / ratio, altText: file }); }
function card(s, x, y, w, h, name) { s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: CARD }, line: { color: LINE, width: 0.75 }, objectName: name }); }
function source(s, t) { txt(s, t, { x: 0.6, y: 6.6, w: 12.1, h: 0.35, fontSize: 10, italic: true, color: FAINT }); }

// 1. Title
pres.addSection({ title: "Opening" });
{
  const s = pres.addSlide({ masterName: "IL Title", sectionTitle: "Opening" });
  s.addText("The Invisible Ledger", { placeholder: "title" });
  txt(s, "Quantifying the Invisible Wedge in Indonesia's Platform Economy", { x: 0.8, y: 2.95, w: 11.7, h: 0.45, fontSize: 20, color: INK2, align: "center" });
  txt(s, "隱形帳簿：量化印尼平台經濟中的隱形缺口", { x: 0.8, y: 3.42, w: 11.7, h: 0.35, fontSize: 14, color: MUTED, align: "center" });
  txt(s, "Progress update: what has changed since the proposal oral of 1 October", { x: 0.8, y: 4.2, w: 11.7, h: 0.4, fontSize: 18, bold: true, color: TEAL, align: "center" });
  txt(s, "CHRISTOPHER ONGKO  王新福   ·   ADVISOR: PROF. DE-RONG KONG  孔德蓉", { x: 0.8, y: 5.05, w: 11.7, h: 0.3, fontSize: 12, color: INK2, align: "center", charSpacing: 1 });
  txt(s, "MASTER OF SCIENCE IN FINANCE, YUAN ZE UNIVERSITY   ·   9 OCTOBER 2026", { x: 0.8, y: 5.45, w: 11.7, h: 0.3, fontSize: 10, color: FAINT, align: "center", charSpacing: 1 });
  s.addNotes("Progress update for the advisor. Same thesis as the proposal: same title, question, hypotheses and measures. This deck shows what came back from the work promised at the oral, and what it changed.");
  n += 1;
}

// 2. What stayed, what was added, what changed
{
  const s = content("Opening", "Since 1 October: what stayed, was added, changed",
    "“The question and hypotheses are the ones you approved. The answers are new.”",
    "Three columns. Stayed: nothing the committee approved has moved. Added: the data and tests promised at the oral. Changed: what the results mean, including two places where the meaning shifted from the proposal.");
  const cols = [
    ["STAYED", ["The title, the research question, H1 and H2, word for word", "The measures: the invisible wedge, the ecosystem ratio, growth divergence", "The Tanah Abang opening and the three users of the numbers"]],
    ["ADDED", ["BPS's own survey answers, three rounds (bought through SILASTIK)", "27 foreign platforms in the comparison, up from 8", "A market-value test, and tests written down before the data were opened", "Primary texts of the 2023-26 rules"]],
    ["CHANGED", ["The thesis now answers the oral deck's own question", "The wedge has a job: it helps explain why revenue swings", "H2's meaning: about half the 2023 rise in sellers was not first-time entry", "The market test came back only partly"]],
  ];
  cols.forEach(([h, items], i) => {
    const x = 0.6 + i * 4.1;
    card(s, x, 1.85, 3.85, 3.6, "col" + i);
    label(s, h, { x: x + 0.3, y: 2.1, w: 3.3, h: 0.3, color: i === 2 ? BRICK : TEAL });
    txt(s, bullets(items), { x: x + 0.3, y: 2.55, w: 3.3, h: 2.8, fontSize: 14, paraSpaceAfter: 10 });
  });
  txt(s, "Nothing the committee approved has moved. Everything promised at the oral has a result.", { x: 0.6, y: 5.75, w: 12.1, h: 0.45, fontSize: 16, italic: true, color: TEAL });
}

// 3. The question, answered
{
  const s = content("Opening", "The oral deck's question, now answered",
    "“How much commerce had actually moved online? It depends on which number you read.”  (oral deck, slide 3)",
    "This is the golden pitch, frozen on 8 October. Everything else in the deck backs one of its sentences.");
  card(s, 0.6, 1.85, 12.1, 4.55, "pitch");
  label(s, "THE ANSWER, IN SIX SENTENCES", { x: 0.95, y: 2.1, w: 8, h: 0.3 });
  txt(s, "In 2023 Indonesia argued about whether online selling was growing so fast it was hurting market traders, and the government shut TikTok Shop. The official figures for that year later said online sales rose 41%. I looked inside the survey behind those figures. Most sellers said their sales were flat or down, and their main complaint was a lack of customers. About half the new sellers weren't first-time sellers: the extra count leaned toward older, long-running small businesses selling through WhatsApp and social media. On the big platforms, revenue grew mostly because they charged more, not because people bought more.",
    { x: 0.95, y: 2.55, w: 11.4, h: 3.0, fontSize: 18, color: INK, paraSpaceAfter: 0, lineSpacingMultiple: 1.15 });
  txt(s, [b("Short version: "), { text: "less commerce had moved online in 2023 than the headlines suggested. Platform income followed prices; the official seller count rose by more than first-time entry can explain." }],
    { x: 0.95, y: 5.65, w: 11.4, h: 0.6, fontSize: 14 });
}

// 4. The arc
pres.addSection({ title: "How it reads" });
{
  const s = content("How it reads", "How the thesis now reads",
    "“Start where everyone is, prove it where the numbers break, end with what anyone can check.”",
    "The five parts are the reading order; the chapters stay the proposal's. The wedge and H1 are the foundation, the 2023 seller count is the centre, the rules and other countries are the way back out.");
  const parts = [
    ["A", "The problem everywhere", "Investors, statistics offices and tax offices all read the digital economy through stand-ins", 3.0],
    ["A-B", "Why Indonesia", "Thin platform slices, sellers in chat apps, and a public fight in 2023", 2.2],
    ["B", "The evidence", "The wedge and H1; buying stalled; H2 and the entry test; who the sellers were", 1.6],
    ["B-C", "What travels", "The checks travel; the Indonesian numbers do not", 2.2],
    ["C", "Back to everyone", "One lesson for each of the three users", 3.0],
  ];
  parts.forEach(([k, t, d, hgt], i) => {
    const x = 0.6 + i * 2.46, w = 2.26, cy = 3.65;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy - hgt / 2, w, h: hgt, rectRadius: 0.1, fill: { color: i === 2 ? "E6EEF0" : CARD }, line: { color: i === 2 ? TEAL : LINE, width: i === 2 ? 1.25 : 0.75 }, objectName: "arc" + i });
    txt(s, k, { x, y: cy - 0.55, w, h: 0.4, fontFace: "Montserrat", fontSize: 20, bold: true, color: i === 2 ? TEAL : INK, align: "center" });
    txt(s, t, { x: x + 0.12, y: cy - 0.08, w: w - 0.24, h: 0.35, fontSize: 14, bold: true, color: INK, align: "center" });
  });
  parts.forEach(([k, t, d], i) => txt(s, d, { x: 0.6 + i * 2.46, y: 5.6, w: 2.26, h: 0.9, fontSize: 12, color: MUTED, align: "center" }));
  txt(s, "WIDE", { x: 0.6, y: 1.85, w: 2.26, h: 0.3, fontSize: 10, color: FAINT, align: "center", charSpacing: 2 });
  txt(s, "NARROW: INDONESIA", { x: 5.52, y: 1.85, w: 2.26, h: 0.3, fontSize: 10, color: FAINT, align: "center", charSpacing: 2 });
  txt(s, "WIDE AGAIN", { x: 10.44, y: 1.85, w: 2.26, h: 0.3, fontSize: 10, color: FAINT, align: "center", charSpacing: 2 });
}

// 5. Promises -> results
{
  const s = content("How it reads", "What the oral deck promised, and what came back",
    "“Every promise has a result, including the ones that did not go our way.”",
    "Read across. The quarterly test failed and is reported. The market test answers only half its question. The entry test was not promised by name, but it tests the oral deck's own caveat on H2.");
  const hdr = { bold: true, color: "FFFFFF", fill: { color: TEAL }, fontSize: 12, fontFace: "Calibri", margin: [4, 6, 4, 6] };
  const c = (t, o) => ({ text: t, options: Object.assign({ fontSize: 12, color: INK2, fontFace: "Calibri", margin: [4, 6, 4, 6], fill: { color: CARD } }, o || {}) });
  const rows = [
    [{ text: "Promised at the oral", options: hdr }, { text: "Result", options: hdr }, { text: "Status", options: hdr }],
    [c("Thicken H1 with quarterly pairs"), c("Does not hold: the quarterly data mostly cover the calmer years after the repricing"), c("Failed, reported", { color: BRICK, bold: true })],
    [c("A longer foreign comparison"), c("27 foreign platforms; Indonesia still stands apart (p = 0.004; worst leave-one-out 0.016)"), c("Done", { color: TEAL, bold: true })],
    [c("Diagnose each large divergence"), c("Grab mostly repricing; Blibli partly travel mix; GoTo cut discounts in 2024; Tokopedia 60.6% from fewer discounts"), c("Done", { color: TEAL, bold: true })],
    [c("Reconcile platform and BPS figures"), c("They agree on growth where they cover the same sellers; levels cannot be fully reconciled, and the reasons are named"), c("Done, with limits", { color: TEAL, bold: true })],
    [c("Market test: does the market tell the two kinds of revenue growth apart?"), c("Market value moved with buying (28 firms, p = 0.002); a different price for fee-driven revenue is not shown (p = 0.20)"), c("Half answered", { color: BRICK, bold: true })],
    [c("H2 caveat: “an arithmetic decomposition, not entry dynamics”"), c("Entry test written down before the data: entry was too small; about half the 2023 rise was not first-time entry"), c("Done, new centre", { color: TEAL, bold: true })],
  ];
  s.addTable(rows, { x: 0.6, y: 1.85, w: 12.1, colW: [3.6, 6.6, 1.9], border: { type: "solid", color: LINE, pt: 0.75 }, rowH: 0.62 });
}

// 6. Thin slice
pres.addSection({ title: "Platforms" });
{
  const s = content("Platforms", "The wedge's job: similar price changes, thinner slice",
    "“In rupiah, Indonesian platforms' changes were close to those abroad. Their slice is ten times thinner.”",
    "Answers Thomas's question on the wedge. Exactly, growth divergence D = (1 + gV)(m1 - m0)/m0: the amplifier is 1/m0 = 1 + E0, together with transaction growth. So the size of the wedge next to revenue sets how far a price change moves revenue growth. Exploratory check, h1_points_vs_log.py. It also corrects our own earlier wording.");
  img(s, "1_thin_slice.png", 0.9, 1.75, 11.2, 2.976);
  txt(s, [b("Reading it: "), { text: "a typical platform abroad keeps about 17 rupiah of every 100 sold; Indonesian marketplaces keep under 2. Both change what they keep by about 1 rupiah per 100 a year. On a 2-rupiah slice that is a huge change, so revenue growth swings about three times as much. H1 is still rejected; a thin slice helps explain why." }],
    { x: 0.6, y: 5.6, w: 12.1, h: 0.8, fontSize: 14 });
  source(s, "Issuer filings, 5 Indonesian and regional vs 26 foreign platforms (firm medians); in points p = 0.65, relative p = 0.003. Exploratory, 9 Oct.");
}

// 7. 2023 hinge
pres.addSection({ title: "2023" });
{
  const s = content("2023", "2023: the headline numbers boomed, buying did not",
    "“Where two numbers look at the same place, they agree. They split where only one of them looks.”",
    "Orange bars are the headlines; teal bars are what buying and sellers show. Bank Indonesia and BPS disagree only outside the marketplaces: BPS's own marketplace slice barely grew.");
  img(s, "6_verdict_2023.png", 0.6, 1.8, 8.4, 2.015);
  label(s, "WHAT IT SHOWS", { x: 9.35, y: 1.9, w: 3.3, h: 0.3 });
  txt(s, bullets(["Five of six Indonesia-only measures of buying grew less than household spending", "Existing sellers: 24% up, 44% same, 32% down", "Main complaint: not enough customers (41%, up from 35%)", "Bank Indonesia −5%, BPS +41%: they agree on the marketplaces and split outside them"]),
    { x: 9.35, y: 2.3, w: 3.35, h: 3.9, fontSize: 13, paraSpaceAfter: 9 });
  source(s, "Company filings; Bank Indonesia; Momentum Works; BPS publications and survey microdata. Growth 2023 vs 2022, each in its own unit.");
}

// 8. H2 and the entry test
pres.addSection({ title: "Sellers" });
{
  const s = content("Sellers", "H2 holds on paper; half the rise was not new entry",
    "“If 820,000 people had started selling in 2023, they would say so. About 513,000 did.”",
    "The entry test was written down on 2 October and committed before the survey files were opened on 7 October. It closes the caveat on the oral deck's H2 slide: 'an arithmetic decomposition, not entry dynamics'.");
  img(s, "5_bps_own_answers.png", 0.6, 1.8, 8.6, 2.876);
  label(s, "THE ENTRY TEST", { x: 9.5, y: 1.9, w: 3.2, h: 0.3 });
  txt(s, bullets(["Written down before the data: at least 1 in 5 sellers should say they started in 2023", "Result: about 1 in 7", "37-56% of the rise was sellers already selling before 2023", "Large in the sampling-error scenarios checked; follows where the survey grew; 2024 is normal again"]),
    { x: 9.5, y: 2.3, w: 3.2, h: 3.4, fontSize: 13, paraSpaceAfter: 9 });
  txt(s, [b("H2 on BPS's published numbers: "), { text: "holds (71% of 2022-23 growth from more businesses). The survey's own answers change what “more businesses” means." }],
    { x: 0.6, y: 4.95, w: 8.6, h: 0.9, fontSize: 14 });
  source(s, "BPS e-commerce survey microdata (2022 and 2023 rounds), weighted. Range depends on how many sellers stopped in 2023.");
}

// 9. Who they are
{
  const s = content("Sellers", "Who the extra sellers were",
    "“The larger count was concentrated among older, long-running businesses selling through chat and social media.”",
    "Exploratory: the surveys do not follow individual businesses, so each group's 2023 count is compared with its 2022 count, net of that group's normal yearly change from the 2020-22 surveys. The raw tilt to men disappears under this control.");
  img(s, "3_who_they_are.png", 0.6, 1.75, 7.9, 1.781);
  label(s, "WHAT IT MEANS", { x: 8.9, y: 1.9, w: 3.8, h: 0.3 });
  txt(s, bullets(["Businesses opened before 2010, often going online years later", "Older owners, mostly schooled to high school or less", "More often outside Java; food stalls and small workshops", "Selling only through chat and social media"]),
    { x: 8.9, y: 2.3, w: 3.8, h: 3.0, fontSize: 14, paraSpaceAfter: 9 });
  txt(s, "These are the kind of businesses the original question was about: real, long-running, and easy for the numbers to miss.", { x: 8.9, y: 5.3, w: 3.8, h: 0.8, fontSize: 14, italic: true, color: TEAL });
  source(s, "BPS e-commerce survey microdata (2020, 2022, 2023 rounds), weighted; about 450,000 sellers beyond normal change. Exploratory, 9 Oct.");
}

// 10. Not returners
{
  const s = content("Sellers", "Sellers back from a break: checked, not closed",
    "“Part-year selling fell, even within the same start-year groups.”",
    "The open alternative to wider survey reach is sellers who paused in 2022 and came back. Three checks weigh against it: the month pattern within the same start-year groups, the timing, and who closes and restarts small firms. Without linked histories, returns can be offset by exits or by sellers moving to full-year selling, and January returns are possible, so the alternative stays open.");
  img(s, "4_full_year_sellers.png", 0.6, 1.8, 7.4, 2.099);
  label(s, "THREE CHECKS", { x: 8.4, y: 1.9, w: 4.3, h: 0.3 });
  txt(s, [
    ...para([b("Months: "), "among sellers who started by 2021, part-year selling fell from 472k to 318k; it falls for every start-year group."]),
    ...para([b("Timing: "), "returning happens every year; it would have to spike in 2023 alone, while 2020-22 groups shrank and 2024 is normal."]),
    ...para([b("Who restarts: "), "small firms close most often when young, with young owners (McKenzie and Paffhausen 2019). The extra count leans the other way. Returns stay the open alternative."], true),
  ], { x: 8.4, y: 2.3, w: 4.3, h: 3.9, fontSize: 14, paraSpaceAfter: 12 });
  source(s, "BPS survey microdata; the month question changed format between rounds. If recall errors run forward, as in Neter and Waksberg (1964), the entry shortfall is conservative.");
}

// 11. Why it matters
pres.addSection({ title: "Why it matters" });
{
  const s = content("Why it matters", "Each rule reaches only what its number sees",
    "“A rule built on platform records reaches the sellers on the platforms. In Indonesia that is fewer than one in five.”",
    "No causal claims about any rule: reach is measured, effects are not. The same design is spreading: OECD model rules (2020, goods 2021), EU DAC7 (2023), Philippines withholding (2024), Viet Nam (2025).");
  img(s, "5_tax_reach.png", 0.6, 1.85, 12.1, 4.608);
  const rules = [["Commission cap", "Motorbike rides only (Gojek, Grab); first test 27 October"], ["Discount rule", "Targets discounts the platforms were already cutting"],
                 ["Marketplace tax", "Can collect from about 1 seller in 20; puts every marketplace seller on record"], ["2026 census", "Reaches the same group the 2023 count found: the next jump may be counting again"]];
  rules.forEach(([h, d], i) => {
    const x = 0.6 + i * 3.06;
    card(s, x, 4.75, 2.86, 1.7, "rule" + i);
    txt(s, h, { x: x + 0.2, y: 4.92, w: 2.5, h: 0.32, fontSize: 14, bold: true, color: INK });
    txt(s, d, { x: x + 0.2, y: 5.3, w: 2.5, h: 1.05, fontSize: 12, color: MUTED });
  });
  source(s, "PMK 37/2025; Permendag 19/2026; Perpres 27/2026 as announced; BPS survey microdata. Abroad: OECD (2020), Directive 2021/514, BIR RR 16-2023, Decree 117/2025/ND-CP.");
}

// 12. Answers to the oral questions
pres.addSection({ title: "Answers" });
{
  const s = content("Answers", "Answers to the questions from the oral",
    "“Each question now has an answer in the thesis, not just at the podium.”",
    "Thomas's wedge question is answered by the thin-slice result. Kong's readability point is answered by the new voice and structure; the proposal averaged 25.6 words a sentence, the story draft 15.8.");
  const qa = [
    ["Prof. Thomas: what is the point of the wedge?", "Its size sets how far a price change moves revenue growth. The wedge is why growth divergence is large in Indonesia."],
    ["Prof. Thomas: the ride-hailing commission cap", "Scoped to motorbike rides; its slice of the measure is shown; predictions are scored on 27 October and in mid-November."],
    ["Prof. Thomas: politics and the players", "The rules chapter maps each rule to the number it acts on and how far it reaches. No causal claims."],
    ["Prof. Kong: how transaction value compares across platforms", "A definition map of each platform's transaction value, in the appendix."],
    ["Prof. Kong: hard to read, too cautious", "A plain story with one line from start to end; the centre is a bolder, tested claim about the official count."],
  ];
  qa.forEach(([q, a], i) => {
    const y = 1.85 + i * 0.93;
    card(s, 0.6, y, 12.1, 0.8, "qa" + i);
    txt(s, q, { x: 0.85, y: y + 0.13, w: 4.4, h: 0.55, fontSize: 13, bold: true, color: INK, valign: "middle" });
    txt(s, a, { x: 5.4, y: y + 0.13, w: 7.1, h: 0.55, fontSize: 13, color: INK2, valign: "middle" });
  });
}

// 13. Corrections
{
  const s = content("Answers", "What we corrected along the way",
    "“Each correction made a claim smaller and the thesis harder to knock over.”",
    "These were found by our own checks and by the independent review. None changes a verdict.");
  const fixes = [
    ["“Indonesian platforms changed their prices far more”", "Similar changes in rupiah; a much thinner slice"],
    ["“Mostly newly counted sellers”", "About half not explained by first-time entry (37-56%); returning sellers named"],
    ["“Markets did not pay up for fee-driven growth”", "Market value moved with buying; the multiples comparison is arithmetic, not evidence"],
    ["“Two thirds of revenue growth came from the cut”", "Two thirds of the movement, defined; not a share of net growth"],
    ["“No one has compared platform and national figures”", "UNCTAD (2024) has; our contribution is the connected Indonesian evidence"],
  ];
  label(s, "BEFORE", { x: 0.6, y: 1.85, w: 5, h: 0.3, color: BRICK });
  label(s, "NOW", { x: 6.6, y: 1.85, w: 5, h: 0.3 });
  fixes.forEach(([a, c], i) => {
    const y = 2.25 + i * 0.82;
    txt(s, a, { x: 0.6, y, w: 5.6, h: 0.7, fontSize: 14, color: MUTED, italic: true });
    txt(s, c, { x: 6.6, y, w: 6.1, h: 0.7, fontSize: 14, color: INK });
    s.addShape(pres.shapes.LINE, { x: 0.6, y: y + 0.74, w: 12.1, h: 0, line: { color: LINE, width: 0.75 } });
  });
}

// 14. Next
pres.addSection({ title: "Next" });
{
  const s = content("Next", "Next: writing, and four dates outside our control",
    "“The material is complete. What remains is writing it and scoring the predictions.”",
    "The one decision needed from the advisor: is the H2 framing acceptable, with the entry test presented as closing the proposal's own stated limit?");
  const dates = [["27 Oct", "GoTo 3Q26: commission-cap predictions"], ["1 Nov", "Marketplace tax start (registered: slips again)"], ["Early Nov", "BPS 3Q26 GDP: buying vs household spending"], ["Mid Nov", "Grab and Sea 3Q26: remaining predictions"]];
  s.addShape(pres.shapes.LINE, { x: 0.9, y: 2.55, w: 9.0, h: 0, line: { color: TEAL, width: 1.5 } });
  dates.forEach(([d, t], i) => {
    const x = 0.9 + i * 3.0;
    s.addShape(pres.shapes.OVAL, { x: x - 0.1, y: 2.45, w: 0.2, h: 0.2, fill: { color: TEAL }, line: { color: TEAL } });
    txt(s, d, { x: x - 0.1, y: 1.95, w: 2.8, h: 0.35, fontSize: 14, bold: true, color: INK });
    txt(s, t, { x: x - 0.1, y: 2.8, w: 2.8, h: 0.8, fontSize: 13, color: MUTED });
  });
  card(s, 0.6, 3.9, 5.9, 2.5, "writing");
  label(s, "WRITING", { x: 0.9, y: 4.1, w: 5.3, h: 0.3 });
  txt(s, bullets(["Results chapter first, then the introduction", "Same chapters as the proposal; the story runs through them", "YZU template and reference check before submission"]), { x: 0.9, y: 4.5, w: 5.3, h: 1.8, fontSize: 14, paraSpaceAfter: 8 });
  card(s, 6.8, 3.9, 5.9, 2.5, "ask");
  label(s, "ONE QUESTION FOR YOU", { x: 7.1, y: 4.1, w: 5.3, h: 0.3, color: BRICK });
  txt(s, "H2 still holds on the published numbers, but its 2023 meaning changes: about half the rise in sellers was not new. Is it acceptable to present the entry test as closing the limit the proposal itself named?", { x: 7.1, y: 4.5, w: 5.3, h: 1.8, fontSize: 14, color: INK });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT, n, "slides");
})();
