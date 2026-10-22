// Renders the reading-copy HTML to PDF with page numbers. Usage: node print_pdf.js in.html out.pdf
// PDF_MARGIN=top,bottom,left,right (e.g. 14mm,14mm,15mm,15mm) overrides the margins; the compact copy uses it.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const m = process.env.PDF_MARGIN ? process.env.PDF_MARGIN.split(',') : ['22mm', '20mm', '21mm', '21mm'];
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;text-align:center;font-family:DejaVu Serif,serif;font-size:8pt;color:#333;"><span class="pageNumber"></span></div>',
    margin: { top: m[0], bottom: m[1], left: m[2], right: m[3] } });
  await browser.close();
})();
