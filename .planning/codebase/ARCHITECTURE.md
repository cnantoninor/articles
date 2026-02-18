# Architecture

**Analysis Date:** 2026-02-15

## Pattern Overview

**Overall:** Content Repository with Export Pipelines — Markdown-first authoring optimized for AI-assisted writing in Cursor IDE.

**Key Characteristics:**
- Markdown-first authoring: all content authored in Markdown with YAML front-matter metadata
- Topic-based content organization under `topics/` directory with standardized subdirectory layout
- Template-driven content creation for articles, presentations, and research notes
- Multi-format export pipeline converting Markdown to DOCX, PPTX, and PDF via shell scripts
- AI-assistant-aware: `CLAUDE.md` and `GLOSSARY.md` provide persistent context for Cursor/Claude sessions
- Dual PDF pipeline: shell-based (pandoc/marp) for standard exports, Node.js-based (Puppeteer) for high-quality typeset output

## Layers

**Content Layer:**
- Purpose: Stores all authored content in Markdown with structured YAML front-matter metadata
- Location: `topics/<topic_name>/`
- Contains: Article drafts (`article.md`), presentation slides (`slides.md`), variant articles (`cursor-article.md`, `iris-learnings.md`), topic overview (`README.md`)
- Depends on: Template Layer (initial scaffolding), Configuration Layer (conventions and terminology)
- Used by: Export Layer, AI authoring tools (Cursor IDE)

**Template Layer:**
- Purpose: Provides standardized starting points for new content types
- Location: `templates/`
- Contains: `article.md` (long-form with YAML front-matter and [GAP:] placeholders), `slides.md` (Marp format with speaker notes), `research.md` (topic README with source tracking and gap markers)
- Depends on: Nothing (foundational)
- Used by: Content Layer (copied when creating new topics)

**Export Layer:**
- Purpose: Transforms Markdown content into publishable distribution formats
- Location: `scripts/` (shell pipeline), `topics/<topic>/exports/export-pdf.js` (Node.js pipeline)
- Contains: Bash scripts for DOCX, PPTX, PDF generation; Node.js script for high-quality PDF with footnote support
- Depends on: External tools (pandoc, marp-cli, pdflatex, puppeteer), Content Layer
- Used by: Content creators to generate distributable outputs

**Configuration Layer:**
- Purpose: Provides authoring guidance, conventions, and shared vocabulary for human and AI authors
- Location: `.ai/` (source of truth), root symlink (`CLAUDE.md`), `.cursor/rules/`, `.claude/rules/`
- Contains: `.ai/context.md` (concise rulebook, always-applied), `.ai/rules/` (glob-activated: writing-style, publication, terminology), `GLOSSARY.md` (domain terminology with usage notes for AI)
- Sync: `.ai/sync-rules.sh` creates symlinks into `.cursor/rules/*.mdc`, `.claude/rules/*.md`, and root `CLAUDE.md`
- Depends on: Nothing
- Used by: AI assistants (Cursor, Claude Code), content creators

**Research Material Layer:**
- Purpose: Stores source material, working notes, and reference literature for each topic
- Location: `topics/<topic_name>/raw_material/`, `topics/<topic_name>/references/`
- Contains: Conversation logs, outlines, literature reviews, academic papers (PDF), definition documents
- Depends on: Nothing
- Used by: Content Layer (informs article writing), AI assistants (context for generation)

**Distribution Layer:**
- Purpose: Publishes content and promotes it across platforms with platform-specific adaptations
- Platform: Substack (The AI Mirror) — primary publication; LinkedIn, Twitter/X, Instagram, Substack Notes — promotion
- Contains: Publication workflow, social teasers, cross-posting conventions (documented in `.ai/rules/publication.md`)
- Depends on: Export Layer (distributable formats), Artifact Storage Layer (polished outputs)
- Used by: Author for publishing and audience engagement
- Status: Manual workflow; MCP server integrations planned for Phase 2

**Artifact Storage Layer:**
- Purpose: Stores generated outputs and intermediate artifacts
- Location: `topics/<topic_name>/exports/` (primary), `topics/<topic_name>/artifacts/` (supplementary; flat articles/ and presentation/ only, no published subdir; state in frontmatter)
- Contains: DOCX, PPTX, PDF files; CSS stylesheets for PDF rendering
- Depends on: Export Layer
- Used by: Distribution Layer, sharing, external presentation tools

## Data Flow

**Content Creation Flow:**

1. Create topic directory under `topics/`: `mkdir topics/<topic_name>`
2. Copy templates from `templates/` to topic directory
3. Create subdirectories: `raw_material/`, `references/`, `assets/`, `exports/`
4. Author content in Markdown, referencing `GLOSSARY.md` for consistent terminology
5. AI assistant reads `CLAUDE.md` for tone, structure, and gap-marking conventions
6. Store supporting materials in `raw_material/` (brainstorms, outlines) and `references/` (literature, papers)

**Export Pipeline Flow:**

1. User invokes export script with topic name: `./scripts/export-all.sh <topic_name>`
2. Script resolves topic path: `TOPIC_DIR="$REPO_ROOT/topics/$TOPIC"`
3. Script validates topic directory and source files exist
4. For DOCX: `pandoc` converts `article.md` → DOCX (for Google Docs)
5. For PPTX: `marp` converts `slides.md` → PPTX (for Google Slides)
6. For PDF: `pandoc` (articles via pdflatex) or `marp` (slides) → PDF
7. Timestamped output saved to `topics/<topic>/exports/<basename>-YYYYMMDD.<ext>`
8. Latest version copied without timestamp: `topics/<topic>/exports/<basename>.<ext>`

**High-Quality PDF Export Flow (Node.js):**

1. User runs `node topics/<topic>/exports/export-pdf.js` directly
2. Script reads Markdown source, strips YAML front-matter
3. `markdown-it` with `markdown-it-footnote` renders to HTML (proper footnote support)
4. Custom CSS from `pdf-export-styles.css` applied for typographic quality
5. Puppeteer generates A4 PDF with page numbers and proper margins
6. Output saved to `topics/<topic>/exports/`

**State Management:**
- Content state tracked via YAML front-matter `status` field: `draft` | `review` | `published`
- No database or external state store — all state is file-based
- Version control via Git on the `main` branch

## Key Abstractions

**Topic:**
- Purpose: Represents a complete subject area with all related content, research, and outputs
- Examples: `topics/epistemic_debt/`
- Pattern: Directory under `topics/` containing standardized files and subdirectories
- Convention: Lowercase with underscores for directory names

**Content Type:**
- Purpose: Defines the format, structure, and metadata of a content piece
- Examples: `article.md` (long-form article), `slides.md` (Marp presentation), `README.md` (topic overview/research tracker)
- Pattern: YAML front-matter (title, subtitle, status, type, audience, dates) followed by Markdown sections with H1 title, H2 sections, H3 subsections
- Variants: A topic may have multiple article variants (e.g., `article.md`, `cursor-article.md`, `iris-learnings.md`) for different audiences or contexts

**Export Target:**
- Purpose: Represents a format transformation from Markdown to a distributable format
- Examples: DOCX (Google Docs), PPTX (Google Slides), PDF (distribution)
- Pattern: Shell script accepting topic name as `$1`, validating inputs, invoking external converter, outputting to `exports/`
- Dual output: Every export creates both a timestamped file and a "latest" copy

**Gap Marker:**
- Purpose: Marks incomplete or uncertain content for future attention
- Examples: `[GAP: description]`, `[TODO: task]`, `[QUESTION: question]`, `[EXAMPLE NEEDED]`
- Pattern: Inline bracket notation used in article drafts and templates

## Entry Points

**Content Creation:**
- Location: `templates/article.md`, `templates/slides.md`, `templates/research.md`
- Triggers: Manual copy by content creator to a new topic directory
- Responsibilities: Provides structure, front-matter fields, and placeholder sections

**Batch Export:**
- Location: `scripts/export-all.sh`
- Triggers: `./scripts/export-all.sh <topic_name>` (manual or scripted)
- Responsibilities: Orchestrates DOCX, PPTX, and PDF exports for a topic; auto-detects which files exist; supports optional specific file argument

**Individual Export Scripts:**
- Location: `scripts/export-docx.sh`, `scripts/export-slides.sh`, `scripts/export-pdf.sh`
- Triggers: Called by `export-all.sh` or directly by user
- Responsibilities: Single-format transformation with input validation and dual-output (timestamped + latest)

**High-Quality PDF Export:**
- Location: `topics/epistemic_debt/exports/export-pdf.js`
- Triggers: Manual `node` invocation
- Responsibilities: Renders Markdown → HTML with footnotes → PDF via Puppeteer; topic-specific (hardcoded paths to `article.md` and `cursor-article.md`)

**Environment Setup:**
- Location: `scripts/setup.sh`
- Triggers: Manual execution when setting up a new machine
- Responsibilities: Detects OS, installs pandoc, npm, marp-cli, and LaTeX (pdflatex)

**AI Authoring Context:**
- Location: `.ai/context.md` (via root symlink `CLAUDE.md`), `.ai/rules/` (via `.cursor/rules/` and `.claude/rules/` symlinks), `GLOSSARY.md`
- Triggers: Always-applied context loaded at session start; glob-activated rules loaded when working on matching files
- Responsibilities: Provides writing tone, structure conventions, terminology, publication workflow, and AI-specific instructions

## Error Handling

**Strategy:** Fail-fast with input validation at script entry.

**Patterns:**
- All export scripts use `set -e` to exit on first error
- Scripts validate topic directory existence before proceeding: `if [ ! -d "$TOPIC_DIR" ]`
- Scripts validate source file existence before attempting conversion
- `export-all.sh` tracks whether any exports occurred; warns if no exportable files found
- `export-pdf.sh` uses `|| true` for optional targets (article or slides may not exist)
- Missing external tools (pandoc, marp) cause clear failure messages
- Node.js PDF exporter uses async/await with `.catch()` for error propagation

## Cross-Cutting Concerns

**Logging:** Shell scripts output progress to stdout. No structured logging framework.

**Validation:**
- YAML front-matter validated implicitly by downstream tools (malformed YAML causes converter failures)
- Directory structure validated in export scripts before processing
- Content quality validated through human review and AI-assisted editing with gap markers

**Path Resolution:**
- Export scripts resolve paths relative to script location: `SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"`
- Repository root derived from script directory: `REPO_ROOT="$(dirname "$SCRIPT_DIR")"`
- Topic directory resolved as `$REPO_ROOT/topics/$TOPIC`
- File arguments support absolute paths, relative paths (`./ or ../`), or topic-relative names

**Authentication:** Not applicable — all operations are local filesystem.

**AI Context Loading:**
- `CLAUDE.md` automatically loaded by Cursor IDE and Claude Code for all sessions in workspace
- `GLOSSARY.md` referenced by AI instructions for consistent terminology
- Topic-specific context (e.g., `README.md` with gaps and status) informs AI assistance

---

*Architecture analysis: 2026-02-15*
