---
description: "Command: Export markdown articles to high-quality PDF using Puppeteer pipeline with custom styling."
alwaysApply: false
---

# Export Articles to PDF

Export one or more markdown articles to PDF using the Puppeteer-based pipeline
with custom CSS styling, proper footnote rendering, and page numbers.

## Placeholders

| Placeholder | Description | Example |
| ----------- | ----------- | ------- |
| `{{TOPIC}}` | Topic directory name | `epistemic_debt` |
| `{{SOURCE_PATH}}` | Relative path under `topics/{{TOPIC}}/artifacts/` to the source folder or file(s) | `articles` or `articles/article-0-the-epistemic-debt-series.md` |

## Rules

### Export directory mirrors artifacts directory

The `exports/` folder **must mirror** the `artifacts/` folder structure within
each topic. The output path is derived by replacing `artifacts/` with `exports/`
and swapping the `.md` extension for `.pdf`.

```
artifacts/articles/article-0-the-epistemic-debt-series.md
    ↓
exports/articles/article-0-the-epistemic-debt-series.pdf
```

### Styling assets live in `scripts/styles/`

- **CSS**: `scripts/styles/pdf-export-styles.css` — primary stylesheet
- **Reference script**: `scripts/styles/export-pdf.js` — Puppeteer exporter

Do **not** place style files or export tooling inside topic directories.

---

## Prompt

Export the markdown article(s) at `topics/{{TOPIC}}/artifacts/{{SOURCE_PATH}}`
to PDF.

### Steps

1. **Resolve source files** — If `{{SOURCE_PATH}}` points to a directory, export
   every `.md` file in it. If it points to a single file, export only that file.

2. **Create output directory** — Derive the output path by replacing `artifacts/`
   with `exports/` in the source path. Create it if it does not exist.

3. **Export each file** using this pipeline:
   - Read the markdown file.
   - Strip YAML front matter (`---` ... `---` block at the top).
   - Render markdown to HTML using **markdown-it** with **markdown-it-footnote**.
   - Wrap the HTML in a full document with the CSS from
     `scripts/styles/pdf-export-styles.css`.
   - Generate the PDF with **Puppeteer**:
     - Format: A4
     - Margins: top 2.2 cm, right 2 cm, bottom 2.5 cm, left 2 cm
     - Print background: enabled
     - Footer: page number / total pages (8 pt, #999, centered)
   - Write the PDF to the mirrored output path.

4. **Report** the exported files with their sizes.

### Example invocation

> Export all articles in artifacts for the epistemic_debt topic to PDF.

With placeholders filled:
- `{{TOPIC}}` = `epistemic_debt`
- `{{SOURCE_PATH}}` = `articles`
