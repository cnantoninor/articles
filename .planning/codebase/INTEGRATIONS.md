# External Integrations

**Analysis Date:** 2026-02-15

## APIs & External Services

**Current:**
- No API clients or SDKs in use
- Content is self-contained Markdown files processed by local CLI tools

**Planned (Phase 2):**
- **Substack MCP Server**: Drafting and publishing articles directly from the editor
- **Social Media MCP Server**: Cross-posting teasers to LinkedIn, Twitter/X, Instagram, Substack Notes
- **Analytics Integration**: Tracking reach and engagement across platforms

## Data Storage

**Databases:**
- None — Local filesystem only

**File Storage:**
- Local filesystem with structured topic directories:
  - Articles: `topics/<topic>/article.md`
  - Slides: `topics/<topic>/slides.md`
  - Exports: `topics/<topic>/exports/` (DOCX, PPTX, PDF, HTML)
  - Raw material: `topics/<topic>/raw_material/`
  - References: `topics/<topic>/references/` (PDFs, Markdown notes)
  - Assets: `topics/<topic>/assets/` (diagrams, images)
  - Artifacts: `topics/<topic>/artifacts/` (flat articles/ and presentation/ only, no published subdir; version/status in frontmatter and git)

**Caching:**
- None

## Authentication & Identity

**Auth Provider:**
- None — Local content repository with no authentication layer

**Access Control:**
- Filesystem permissions only
- Git-based collaboration (if shared)

## Monitoring & Observability

**Error Tracking:**
- None — Shell scripts use `set -e` for fail-fast error handling

**Logs:**
- Shell script stdout/stderr only
- Echo-based progress messages in export scripts
- No structured logging or log aggregation

## CI/CD & Deployment

**Hosting:**
- Primary publication: Substack (The AI Mirror — https://antoninorau.substack.com/)
- Exports shared via Google Docs/Slides for collaboration

**CI Pipeline:**
- None detected
- No GitHub Actions, GitLab CI, or other CI/CD configuration

**Version Control:**
- Git repository at `/home/arau6/projects/ai-articles`
- Branch: `main`
- `.gitignore` excludes: `node_modules`, `.planning/phases`

## Environment Configuration

**Required env vars:**
- None

**Secrets location:**
- Not applicable — No secrets required

**Configuration files:**
- `.ai/context.md` — Concise AI rulebook (symlinked to `CLAUDE.md`)
- `.ai/rules/` — Glob-activated rules (writing-style, publication, terminology)
- `GLOSSARY.md` — Shared terminology definitions
- `.planning/config.json` — GSD planning tool settings

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None

## Export Pipelines (Primary Integration Surface)

This repository's main "integrations" are its export pipelines — local CLI tools that transform Markdown content into distributable formats.

### Pipeline 1: Article → DOCX (Google Docs)

- **Script:** `scripts/export-docx.sh`
- **Tool:** Pandoc
- **Command:** `pandoc <input>.md -o <output>.docx --from=markdown --to=docx --standalone`
- **Output:** `topics/<topic>/exports/<name>-<YYYYMMDD>.docx` + latest copy without timestamp
- **Target:** Import into Google Docs for collaboration and sharing

### Pipeline 2: Article → PDF (Standard)

- **Script:** `scripts/export-pdf.sh` (article mode)
- **Tool:** Pandoc + pdflatex
- **Command:** `pandoc <input>.md -o <output>.pdf --from=markdown --to=pdf --pdf-engine=pdflatex --standalone`
- **Output:** `topics/<topic>/exports/<name>-<YYYYMMDD>.pdf` + latest copy
- **Target:** Standalone PDF distribution

### Pipeline 3: Article → PDF (High-Quality Custom)

- **Script:** `topics/epistemic_debt/exports/export-pdf.js` (topic-specific)
- **Tools:** markdown-it + markdown-it-footnote → HTML → Puppeteer (headless Chrome) → PDF
- **Features:** Custom CSS styling, proper footnote rendering, A4 with page numbers, Georgia serif typography
- **Styles:** `topics/epistemic_debt/exports/pdf-export-styles.css`
- **Output:** `topics/epistemic_debt/exports/claude-article-cc.pdf`, `cursor-article-cc.pdf`
- **Target:** Publication-quality PDF with polished formatting

### Pipeline 4: Slides → PPTX (Google Slides)

- **Script:** `scripts/export-slides.sh`
- **Tool:** Marp CLI
- **Command:** `marp <input>.md -o <output>.pptx --allow-local-files`
- **Output:** `topics/<topic>/exports/<name>-<YYYYMMDD>.pptx` + latest copy
- **Target:** Import into Google Slides for presentations

### Pipeline 5: Slides → PDF

- **Script:** `scripts/export-pdf.sh` (slides mode)
- **Tool:** Marp CLI
- **Command:** `marp <input>.md -o <output>.pdf --allow-local-files --pdf`
- **Output:** `topics/<topic>/exports/slides-<YYYYMMDD>.pdf` + latest copy
- **Target:** Standalone slide deck PDF

### Pipeline 6: Batch Export

- **Script:** `scripts/export-all.sh`
- **Orchestrates:** Pipelines 1, 2, 4, 5 for a given topic
- **Usage:** `./scripts/export-all.sh <topic>` or `./scripts/export-all.sh <topic> <specific-file.md>`
- **Behavior:** Auto-detects article.md and slides.md; routes slide files to Marp, article files to Pandoc

## AI Tools

**Cursor AI Editor:**
- Primary authoring environment
- Configuration: `.ai/context.md` (via `CLAUDE.md` symlink) + `.cursor/rules/*.mdc` (glob-activated symlinks)
- Integration: File-based context loading (no API integration)
- Key files:
  - `.ai/context.md` → `CLAUDE.md` — Always-applied concise rulebook
  - `.ai/rules/` → `.cursor/rules/` — Writing style, publication, terminology rules
  - `GLOSSARY.md` — Domain terminology
  - `templates/` — Content scaffolding (article, slides, research)

**Claude Code:**
- Context file: `.ai/context.md` (via `CLAUDE.md` symlink)
- Glob-activated rules: `.claude/rules/*.md` (symlinked from `.ai/rules/`)
- Planning infrastructure: `.planning/` directory with project docs

**No LLM APIs:**
- No OpenAI, Anthropic, or other LLM API integrations in scripts
- AI usage is editor-based (Cursor) and CLI-based (Claude Code), not programmatic

---

*Integration audit: 2026-02-15*
