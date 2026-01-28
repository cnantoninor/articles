# Technology Stack

**Analysis Date:** 2026-01-26

## Languages

**Primary:**
- Markdown - Content authoring (articles, slides, templates)
- Bash Shell Script - Automation and export workflows

**Secondary:**
- YAML - Front-matter metadata in Markdown files
- Python 3.13.7 - Available in environment (not actively used in codebase)

## Runtime

**Environment:**
- Bash 5.2.21(1)-release
- Linux 5.15.167.4-microsoft-standard-WSL2 (WSL2 environment)

**Package Manager:**
- npm 11.7.0 (for Marp CLI installation)
- No lockfile present

## Frameworks

**Core:**
- Marp - Markdown-based presentation framework (slides.md → PPTX/PDF conversion)
  - Expected installation: `@marp-team/marp-cli` via npm global
  - Status: Required but not currently installed on system

**Build/Dev:**
- Pandoc 3.1.3 - Markdown → DOCX/PDF conversion
  - Features: Lua 5.4 scripting engine
  - PDF engine: pdflatex (TeX Live 2023/Debian)

**Testing:**
- None detected

## Key Dependencies

**Critical:**
- pandoc 3.1.3 - Article export to DOCX and PDF formats
  - Why it matters: Core workflow for sharing articles with non-technical audiences
  - Used by: `scripts/export-docx.sh`, `scripts/export-pdf.sh`

**Infrastructure:**
- pdflatex (TeX Live 2023/Debian) - PDF rendering engine for pandoc
  - Used by: `scripts/export-pdf.sh` via `--pdf-engine=pdflatex`

**Expected but Missing:**
- @marp-team/marp-cli - Slide deck export
  - Expected by: `scripts/export-slides.sh`, `scripts/export-pdf.sh`
  - Installation command documented in `README.md`: `npm install -g @marp-team/marp-cli`

## Configuration

**Environment:**
- No environment variables required
- No secrets or API keys needed
- No `.env` files present

**Build:**
- Front-matter in Markdown files controls metadata:
  - `templates/article.md` - Article template with YAML front-matter
  - `templates/slides.md` - Marp presentation template with YAML configuration
  - `epistemic_debt/article.md` - Example configuration with title, status, audience, target_length

**Marp Configuration:**
- Configured via YAML front-matter in `*.md` files:
  ```yaml
  marp: true
  theme: default
  paginate: true
  ```

**Cursor AI Configuration:**
- `.cursorrules` (4564 bytes) - AI authoring guidelines and conventions
- Symlinked as `CLAUDE.md` for compatibility
- Located: `/home/arau6/projects/ai-articles/.cursorrules`

## Platform Requirements

**Development:**
- Linux/Unix-like environment (uses bash scripts)
- pandoc 3.x
- pdflatex (for PDF export)
- npm + Node.js 22.x (for Marp CLI installation)
- Cursor AI editor (optional but optimized for)

**Production:**
- Static content repository
- No deployment infrastructure
- Manual export workflow to Google Docs/Slides
- Exports stored locally in `<topic>/exports/` directories

---

*Stack analysis: 2026-01-26*
