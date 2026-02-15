# Technology Stack

**Analysis Date:** 2026-02-15

## Languages

**Primary:**
- Markdown — All content authoring (articles, slides, templates, glossary, research notes)
- Bash Shell Script — Export automation and setup (`scripts/*.sh`)

**Secondary:**
- JavaScript (Node.js) — Custom high-quality PDF export pipeline (`topics/epistemic_debt/exports/export-pdf.js`)
- CSS — PDF export styling (`topics/epistemic_debt/exports/pdf-export-styles.css`, `topics/epistemic_debt/exports/pdf-styles.css`)
- YAML — Front-matter metadata in every Markdown content file

## Runtime

**Environment:**
- Node.js v22.17.1 (via nvm)
- Bash (Linux shell)
- Linux 6.6.87.2-microsoft-standard-WSL2 (WSL2 environment)

**Package Manager:**
- npm 10.9.2 (for local Node.js dependencies and Marp CLI)
- No `package.json` at repo root — dependencies installed directly into `node_modules/`
- Lockfile: `.package-lock.json` inside `node_modules/` (auto-generated, no root lockfile)

## Frameworks & Tools

**Content Authoring:**
- Marp — Markdown-based presentation framework
  - Configured via YAML front-matter in slide `.md` files:
    ```yaml
    marp: true
    theme: default
    paginate: true
    ```
  - Expected installation: `@marp-team/marp-cli` via npm (global or local)
  - Used by: `scripts/export-slides.sh`, `scripts/export-pdf.sh`

**Document Conversion:**
- Pandoc — Universal document converter
  - Installed version: 3.1.3 (at `/usr/bin/pandoc` — not currently installed in this environment)
  - Converts: Markdown → DOCX, Markdown → PDF
  - PDF engine: pdflatex via `--pdf-engine=pdflatex`
  - Used by: `scripts/export-docx.sh`, `scripts/export-pdf.sh`

**PDF Rendering:**
- pdflatex (TeX Live 2023/Debian) — PDF rendering engine for Pandoc
  - Installed at: `/usr/bin/pdflatex`
  - LaTeX packages: texlive-latex-base, texlive-fonts-recommended, texlive-fonts-extra, texlive-latex-extra
  - Used by: `scripts/export-pdf.sh` (article mode)

**Custom PDF Pipeline:**
- markdown-it 14.1.0 + markdown-it-footnote 4.0.0 — Markdown-to-HTML rendering with footnote support
- Puppeteer (borrowed from system-level `md-to-pdf` package at `/home/arau6/.nvm/versions/node/v22.17.1/lib/node_modules/md-to-pdf/node_modules/puppeteer`) — Headless Chrome for HTML-to-PDF
- Used in: `topics/epistemic_debt/exports/export-pdf.js`
- Purpose: Higher-quality PDF output with custom CSS styling, proper footnote rendering, A4 format with page numbers

**Testing:**
- None detected — no test framework or test files

## Key Dependencies

**Local Node.js Packages (in `node_modules/`):**
- `markdown-it` 14.1.0 — Markdown parsing and HTML rendering
- `markdown-it-footnote` 4.0.0 — Footnote syntax extension for markdown-it
- `argparse` 2.0.1 — Argument parsing (transitive dep of markdown-it)
- `entities` 4.5.0 — HTML entity encoding (transitive dep)
- `linkify-it` 5.0.0 — URL auto-linking (transitive dep)
- `mdurl` 2.0.0 — URL utilities (transitive dep)
- `punycode.js` 2.3.1 — Punycode encoding (transitive dep)
- `uc.micro` 2.1.0 — Unicode character classes (transitive dep)

**System-level Dependencies:**
- `pandoc` 3.x — Document conversion (installed via system package manager)
- `pdflatex` (TeX Live) — PDF rendering engine
- `@marp-team/marp-cli` — Slide export (installed via npm globally or locally)
- `md-to-pdf` — System-level npm package providing Puppeteer (referenced by `export-pdf.js`)

**Binary available in `node_modules/.bin/`:**
- `markdown-it` — CLI for markdown-it (not actively used in workflows)

## Content Formats

**Input Formats:**
- Markdown with YAML front-matter (articles): Standard CommonMark with extensions
  - Front-matter fields: `title`, `status`, `type`, `audience`, `target_length`, `created`, `last_updated`
  - Footnote syntax: `[^n]` / `[^n]: text` (markdown-it-footnote format)
- Marp Markdown (slides): Markdown with `---` slide separators and HTML speaker notes
  - Front-matter: `marp: true`, `theme`, `paginate`, `title`
  - Speaker notes: `<!-- Speaker notes: ... -->`

**Output Formats:**
- DOCX — Microsoft Word Open XML (for Google Docs import)
- PPTX — Microsoft PowerPoint Open XML (for Google Slides import)
- PDF — Portable Document Format (standalone distribution)
  - Two pipelines: pandoc+pdflatex (standard) and markdown-it+Puppeteer (high-quality with custom CSS)
- HTML — Generated as intermediate format by Marp and export-pdf.js

**Styling:**
- `topics/epistemic_debt/exports/pdf-export-styles.css` (287 lines) — High-quality PDF styles (Georgia/serif font, A4 format, footnote styling, print-optimized)
- `topics/epistemic_debt/exports/pdf-styles.css` (180 lines) — Simpler PDF styles (alternate stylesheet)
- Both CSS files handle: typography, tables, code blocks, footnotes, blockquotes, page break control, print media

## Configuration

**Environment:**
- No environment variables required
- No secrets or API keys
- No `.env` files

**Build Configuration:**
- No build config files (no `Makefile`, no `*.config.*`)
- Export parameters controlled via shell script arguments
- Marp configuration inline in Markdown front-matter
- Pandoc options hardcoded in shell scripts

**AI Authoring Configuration:**
- `.cursorrules` — AI writing guidelines, style conventions, domain terminology, file organization rules
- `CLAUDE.md` — Claude Code context file
- `GLOSSARY.md` — Shared domain terminology definitions
- `templates/` — Content scaffolding templates (article, slides, research)
- `.planning/config.json` — GSD planning tool configuration

## Platform Requirements

**Development:**
- Linux/Unix-like environment (bash scripts required)
- Node.js 22.x + npm (for Marp CLI and markdown-it dependencies)
- pandoc 3.x (for DOCX and standard PDF export)
- pdflatex / TeX Live (for PDF rendering via Pandoc)
- @marp-team/marp-cli (for PPTX and slide PDF export)
- Cursor AI editor (optional but optimized for AI-assisted authoring)

**Setup:**
- Run `scripts/setup.sh` to install all dependencies automatically
- Detects OS (Linux/macOS) and uses appropriate package manager
- Installs: Pandoc, Node.js/npm, Marp CLI (global, falls back to local), LaTeX (texlive)

**Production:**
- Static content repository — no deployment infrastructure
- Manual export workflow to Google Workspace (Docs/Slides)
- Exports stored locally in `topics/<topic>/exports/` directories
- Git-based version control

---

*Stack analysis: 2026-02-15*
