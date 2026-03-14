# Export Styles & Assets

Shared stylesheets and helper scripts used by the PDF/HTML export pipeline.

## Files

| File | Purpose |
|------|---------|
| `pdf-export-styles.css` | Primary CSS for Puppeteer-based PDF export (A4, Georgia serif, footnotes, page numbers) |
| `pdf-styles.css` | Alternate CSS for pandoc-based PDF export |
| `export-pdf.js` | Node.js Puppeteer exporter (reference implementation — the `ar-export-pdf` command wraps this logic) |

## Usage

These assets are consumed by:
- The `ar-export-pdf` skill (invoked via `/ar-export-pdf` in Claude Code or Cursor)
- The `scripts/export-pdf.sh` shell script (pandoc path)
