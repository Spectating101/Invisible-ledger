// Renders the reading-copy HTML to PDF with page numbers. Usage: node print_pdf.js in.html out.pdf
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;text-align:center;font-family:DejaVu Serif,serif;font-size:8pt;color:#333;"><span class="pageNumber"></span></div>',
    margin: { top: '22mm', bottom: '20mm', left: '21mm', right: '21mm' } });
  await browser.close();
})();
