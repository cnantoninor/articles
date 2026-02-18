#!/usr/bin/env node
/**
 * High-quality Markdown-to-PDF exporter with proper footnote support.
 * Uses markdown-it + markdown-it-footnote for rendering,
 * and Puppeteer for PDF generation.
 */

const fs = require('fs');
const path = require('path');
const markdownIt = require('markdown-it');
const markdownItFootnote = require('markdown-it-footnote');
const puppeteer = require('puppeteer');

const md = markdownIt({
  html: true,
  typographer: true,
  linkify: true,
}).use(markdownItFootnote);

// Customize footnote rendering for better PDF output
md.renderer.rules.footnote_block_open = () =>
  '<section class="footnotes">\n<hr>\n<ol>\n';

md.renderer.rules.footnote_block_close = () =>
  '</ol>\n</section>\n';

async function exportPdf(inputFile, outputFile) {
  let content = fs.readFileSync(inputFile, 'utf8');

  // Strip YAML front matter
  content = content.replace(/^---\n[\s\S]*?\n---\n/, '');

  // Render markdown to HTML
  const htmlBody = md.render(content);

  // Read CSS
  const cssPath = path.join(__dirname, 'pdf-export-styles.css');
  const css = fs.readFileSync(cssPath, 'utf8');

  // Build full HTML document
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>${css}</style>
</head>
<body>
${htmlBody}
</body>
</html>`;

  // Launch Puppeteer and generate PDF
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'networkidle0' });

  await page.pdf({
    path: outputFile,
    format: 'A4',
    margin: {
      top: '2.2cm',
      right: '2cm',
      bottom: '2.5cm',
      left: '2cm',
    },
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="font-size: 8pt; color: #999; text-align: center; width: 100%; margin: 0 2cm;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  });

  await browser.close();
  const stats = fs.statSync(outputFile);
  console.log(`  ✓ ${outputFile} (${(stats.size / 1024).toFixed(0)} KB)`);
}

async function main() {
  const topic = process.argv[2];
  if (!topic) {
    console.error('Usage: node export-pdf.js <topic-directory>');
    console.error('Example: node scripts/styles/export-pdf.js epistemic_debt');
    process.exit(1);
  }

  const repoRoot = path.resolve(__dirname, '../..');
  const topicDir = path.join(repoRoot, 'topics', topic);
  const outDir = path.join(topicDir, 'exports');

  if (!fs.existsSync(topicDir)) {
    console.error(`Error: Topic directory not found: ${topicDir}`);
    process.exit(1);
  }
  fs.mkdirSync(outDir, { recursive: true });

  const candidates = ['article.md', 'cursor-article.md'];
  const tasks = [];
  for (const name of candidates) {
    const inputPath = path.join(topicDir, name);
    if (fs.existsSync(inputPath)) {
      const base = name.replace(/\.md$/, '');
      tasks.push({
        input: inputPath,
        output: path.join(outDir, `${base}-cc.pdf`),
      });
    }
  }

  if (tasks.length === 0) {
    console.error(`Error: No article.md or cursor-article.md found in ${topicDir}`);
    process.exit(1);
  }

  for (const { input, output } of tasks) {
    const name = path.basename(input);
    console.log(`Exporting ${name}...`);
    await exportPdf(input, output);
  }

  console.log('\nDone.');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
