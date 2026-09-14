import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const repo = "/tmp/invisible-ledger-synthesis-Y73PTP";
const outputDir = path.join(repo, "outputs", "advisor_review_package_2026-09-10");
const outputFile = path.join(outputDir, "Invisible_Ledger_Data_Guide_2026-09-10.xlsx");

function parseCsv(text) {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') { field += '"'; i++; }
      else if (ch === '"') quoted = false;
      else field += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(field); field = ""; }
    else if (ch === '\n') { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += ch;
  }
  if (field.length || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  return rows.filter(r => r.some(v => v !== ""));
}

function coerceColumns(rows) {
  if (rows.length < 2) return rows;
  const cols = rows[0].length;
  const numeric = Array(cols).fill(true);
  for (let c = 0; c < cols; c++) {
    for (let r = 1; r < rows.length; r++) {
      const v = (rows[r][c] ?? "").trim();
      if (!v) continue;
      if (!/^-?(?:\d+\.?\d*|\.\d+)$/.test(v)) { numeric[c] = false; break; }
    }
  }
  return rows.map((row, r) => row.map((v, c) => {
    if (r > 0 && numeric[c] && v.trim() !== "") return Number(v);
    return v;
  }));
}

function colName(n) {
  let s = "";
  for (let x = n + 1; x > 0; x = Math.floor((x - 1) / 26)) s = String.fromCharCode(65 + ((x - 1) % 26)) + s;
  return s;
}

function styleTable(sheet, rows, tableName) {
  const rowCount = rows.length;
  const colCount = Math.max(...rows.map(r => r.length));
  const last = colName(colCount - 1);
  const used = sheet.getRange(`A1:${last}${rowCount}`);
  used.format.font = { name: "Arial", size: 10, color: "#1F2937" };
  used.format.verticalAlignment = "top";
  const header = sheet.getRange(`A1:${last}1`);
  header.format.fill = "#24364B";
  header.format.font = { name: "Arial", size: 10, bold: true, color: "#FFFFFF" };
  header.format.horizontalAlignment = "center";
  header.format.verticalAlignment = "center";
  header.format.wrapText = true;
  header.format.rowHeight = 36;
  sheet.freezePanes.freezeRows(1);
  sheet.showGridLines = false;
  const table = sheet.tables.add(`A1:${last}${rowCount}`, true, tableName);
  table.style = "TableStyleMedium2";
  table.showBandedRows = true;
  table.showFilterButton = true;
  for (let c = 0; c < colCount; c++) {
    const values = rows.slice(0, Math.min(rows.length, 80)).map(r => String(r[c] ?? ""));
    const maxLen = Math.max(...values.map(v => v.length), 8);
    const width = Math.min(Math.max(maxLen + 2, 11), /url|locator|caveat|limit|status|requirement|warning/i.test(String(rows[0][c])) ? 38 : 24);
    const column = sheet.getRange(`${colName(c)}1:${colName(c)}${rowCount}`);
    column.format.columnWidth = width;
    if (width >= 28) column.format.wrapText = true;
  }
}

async function addCsvSheet(workbook, name, relPath, tableName) {
  const text = await fs.readFile(path.join(repo, relPath), "utf8");
  const rows = coerceColumns(parseCsv(text));
  const sheet = workbook.worksheets.add(name);
  sheet.getRange("A1").write(rows);
  styleTable(sheet, rows, tableName);
  return { name, rows: rows.length - 1, columns: rows[0].length, relPath };
}

const workbook = Workbook.create();
const readme = workbook.worksheets.add("Read Me");
readme.showGridLines = false;
readme.getRange("A1:H1").format.borders = { bottom: { style: "medium", color: "#24364B" } };
readme.getRange("A1").values = [["Invisible Ledger data guide"]];
readme.getRange("A1").format.font = { name: "Arial", size: 16, bold: true, color: "#172033" };
readme.getRange("A2").values = [["Advisor data review · Indonesia main design with separate supporting evidence · 10 September 2026"]];
readme.getRange("A2:H2").format.font = { name: "Arial", size: 10, italic: true, color: "#4B5563" };
readme.getRange("A4:B4").values = [["Purpose", "How to use this workbook"]];
readme.getRange("A4:B4").format.fill = "#DCE6F1";
readme.getRange("A4:B4").format.font = { bold: true, color: "#172033" };
readme.getRange("A5:B8").values = [
  ["What this is", "A convenient inspection view of selected CSV files in the accompanying ZIP. The CSV and source documents remain the record of evidence."],
  ["Main decision", "Confirm which longitudinal Indonesia-aligned issuer or segment observations may enter the main analysis."],
  ["Supporting modules", "BPS, ASEAN, global issuer, and quarterly evidence are separate modules. They are not pooled into one sample N."],
  ["Important boundary", "Transaction value minus platform revenue is not missing GDP, participant income, unpaid tax, or tax evasion."],
];
readme.getRange("A10:C10").values = [["Order", "Sheet", "What it answers"]];
readme.getRange("A10:C10").format.fill = "#24364B";
readme.getRange("A10:C10").format.font = { bold: true, color: "#FFFFFF" };
readme.getRange("A11:C20").values = [
  [1, "Sample Decisions", "What the advisor needs to approve before the manuscript is rebuilt"],
  [2, "Indonesia Candidates", "Which annual source-reported periods exist and why each is admitted or limited"],
  [3, "Issuer Transitions", "How transaction and revenue growth differ within candidate series"],
  [4, "BPS Growth", "How national e-commerce value, business counts, and sales channels changed"],
  [5, "BPS Business", "Published business-level marketplace and recordkeeping evidence"],
  [6, "Institutional", "What Indonesia's marketplace reporting rules establish and do not establish"],
  [7, "ASEAN Countries", "Separate country histories and measurement context; no pooled tax comparison"],
  [8, "Global Issuers", "External within-issuer corroboration across business models"],
  [9, "Quarterly Accounting", "The separate 47-quarter company accounting inventory"],
  [10, "FY2023 Sensitivity", "Model dependence of the earlier one-year reconstruction"],
];
readme.getRange("A22:B22").values = [["Evidence chain", "Source document → extracted row → analysis script → reported output"]];
readme.getRange("A22:B22").format.fill = "#E8F1E8";
readme.getRange("A22:B22").format.font = { bold: true, color: "#1F5132" };
readme.getRange("A24:B28").values = [
  ["Direct issuer/official", "Reported in an issuer filing, results release, or BPS publication."],
  ["Conditional construction", "One quantity is derived from an explicitly stated rate or allocation."],
  ["Supporting evidence", "Answers another part of the research question but does not enlarge the Indonesia issuer sample."],
  ["Hypothesis", "Interpretation requiring further evidence or advisor agreement."],
  ["Excluded", "Preserved in the research archive but not used as current analytical evidence."],
];
readme.getRange("A1:H28").format.font = { name: "Arial", size: 10, color: "#1F2937" };
readme.getRange("A1").format.font = { name: "Arial", size: 16, bold: true, color: "#172033" };
readme.getRange("A2:H2").format.font = { name: "Arial", size: 10, italic: true, color: "#4B5563" };
readme.getRange("A5:B28").format.wrapText = true;
readme.getRange("A:A").format.columnWidth = 25;
readme.getRange("B:B").format.columnWidth = 72;
readme.getRange("C:C").format.columnWidth = 74;

const decisions = workbook.worksheets.add("Sample Decisions");
const decisionRows = [
  ["sample_boundary", "levels", "valid_transitions", "reversals", "current_use", "main_limitation"],
  ["Strict explicit-country direct", 0, 0, 0, "Not feasible", "No current issuer discloses the required country pair directly"],
  ["Tokopedia direct Indonesia-aligned segment", 2, 1, 1, "Strongest direct case", "Too narrow as the complete longitudinal sample"],
  ["Tokopedia + Blibli 3P", 9, 6, 3, "Candidate main boundary", "Blibli 3P includes online travel"],
  ["Tokopedia + Blibli + Bukalapak", 13, 9, 3, "Broader candidate boundary", "Bukalapak Group includes overseas operations"],
  ["Grab and Shopee country constructions", 6, 4, 0, "Sensitivity only", "Country values depend on company-wide rates or external allocation"],
];
decisions.getRange("A1").write(decisionRows);
styleTable(decisions, decisionRows, "TblSampleDecisions");

const specs = [
  ["Indonesia Candidates", "data/longitudinal/advisor_empirical_candidate_table_2026-09-10.csv", "TblIndonesiaCandidates"],
  ["Issuer Transitions", "outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv", "TblIssuerTransitions"],
  ["BPS Growth", "outputs/hypothesis_tests_2026-09-10/bps_national_growth_anatomy.csv", "TblBpsGrowth"],
  ["BPS Business", "data/bps_official/bps_marketplace_business_level_published_evidence_2026-09-10.csv", "TblBpsBusiness"],
  ["Institutional", "data/institutional/indonesia_marketplace_reporting_architecture_2025_2026.csv", "TblInstitutional"],
  ["ASEAN Countries", "data/asean_corroboration/asean_country_year_canonical_2019_2025.csv", "TblAseanCountries"],
  ["Global Issuers", "data/global_ecommerce/global_platform_matched_annual.csv", "TblGlobalIssuers"],
  ["Quarterly Accounting", "data/quarterly/clean_event_panel_accounting.csv", "TblQuarterlyAccounting"],
  ["FY2023 Sensitivity", "data/indonesia_fy2023/fy2023_indonesia_main_sensitivity.csv", "TblFy2023Sensitivity"],
];

const summary = [];
for (const [name, relPath, tableName] of specs) summary.push(await addCsvSheet(workbook, name, relPath, tableName));

await fs.mkdir(outputDir, { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputFile);

const inspect = await workbook.inspect({ kind: "workbook,sheet,table", maxChars: 9000, tableMaxRows: 4, tableMaxCols: 8 });
console.log(inspect.ndjson);
const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log(errors.ndjson);

const previewDir = path.join("/tmp/il-workbook-builder", "previews");
await fs.mkdir(previewDir, { recursive: true });
for (const sheetName of ["Read Me", "Sample Decisions", ...specs.map(s => s[0])]) {
  const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName.replaceAll(" ", "_")}.png`), new Uint8Array(await preview.arrayBuffer()));
}

console.log(JSON.stringify({ outputFile, sheets: 2 + specs.length, imported: summary }, null, 2));
