# Architecture

**Analysis Date:** 2026-01-26

## Pattern Overview

**Overall:** Content Repository with Export Pipelines

**Key Characteristics:**
- Markdown-first authoring workflow for articles and presentations
- Template-based content creation with YAML front-matter
- Export-oriented architecture converting Markdown to multiple formats (DOCX, PPTX, PDF)
- Topic-based organization with standardized directory structure

## Layers

**Content Layer:**
- Purpose: Stores all content in Markdown format with structured metadata
- Location: `/<topic-name>/`
- Contains: Article drafts, presentation slides, research notes, references
- Depends on: Templates (`/templates/`)
- Used by: Export scripts, AI authoring tools

**Template Layer:**
- Purpose: Provides standardized starting points for different content types
- Location: `/templates/`
- Contains: `article.md`, `slides.md`, `research.md` templates
- Depends on: Nothing (foundational)
- Used by: Content layer (copied when creating new topics)

**Export Layer:**
- Purpose: Transforms Markdown content into publishable formats
- Location: `/scripts/`
- Contains: Bash scripts for DOCX, PPTX, and PDF generation
- Depends on: External tools (pandoc, marp-cli), content layer
- Used by: Content creators to generate outputs

**Configuration Layer:**
- Purpose: Provides authoring guidance and conventions
- Location: Root directory (`.cursorrules`, `CLAUDE.md`, `GLOSSARY.md`)
- Contains: Writing style guidelines, terminology definitions, AI assistant instructions
- Depends on: Nothing
- Used by: AI assistants, content creators

**Artifact Storage Layer:**
- Purpose: Stores generated outputs and intermediate artifacts
- Location: `/<topic-name>/exports/`, `/<topic-name>/artifacts/`
- Contains: DOCX, PPTX, PDF files
- Depends on: Export layer
- Used by: Distribution, sharing

## Data Flow

**Content Creation Flow:**

1. Copy template from `/templates/` to `/<topic-name>/`
2. Edit Markdown file with YAML front-matter
3. Reference `GLOSSARY.md` for consistent terminology
4. Store supporting materials in `raw_material/`, `references/`, `assets/`
5. Invoke export scripts to generate publishable formats
6. Outputs saved to `/<topic-name>/exports/`

**State Management:**
- Content state tracked via YAML `status` field (draft, review, published)
- No database or external state store
- Version control managed externally via Git (repository not initialized in working directory)

## Key Abstractions

**Topic:**
- Purpose: Represents a single subject area with all related content
- Examples: `/epistemic_debt/`
- Pattern: Directory containing standardized subdirectories (raw_material, references, assets, exports, artifacts)

**Content Type:**
- Purpose: Defines the format and structure of content pieces
- Examples: `article.md` (long-form writing), `slides.md` (Marp presentations), `README.md` (research notes)
- Pattern: YAML front-matter followed by Markdown sections

**Export Target:**
- Purpose: Represents a publishable format transformation
- Examples: DOCX (for Google Docs), PPTX (for Google Slides), PDF (for distribution)
- Pattern: Shell script invoking external converter tool

## Entry Points

**Content Creation:**
- Location: `/templates/article.md`, `/templates/slides.md`, `/templates/research.md`
- Triggers: Manual copy operation by content creator
- Responsibilities: Provides structure for new content with placeholder sections

**Export Workflows:**
- Location: `/scripts/export-all.sh`
- Triggers: Manual execution with topic name as argument
- Responsibilities: Orchestrates all export scripts (DOCX, PPTX, PDF) for a topic

**Individual Export Scripts:**
- Location: `/scripts/export-docx.sh`, `/scripts/export-slides.sh`, `/scripts/export-pdf.sh`
- Triggers: Called by `export-all.sh` or manually
- Responsibilities: Transforms specific content type to target format using pandoc or marp-cli

**AI Authoring Context:**
- Location: `.cursorrules` (symlinked as `CLAUDE.md`)
- Triggers: Loaded by AI assistant (Cursor IDE)
- Responsibilities: Provides writing guidelines, terminology, conventions to AI

## Error Handling

**Strategy:** Fail-fast with validation checks

**Patterns:**
- Scripts validate topic directory exists before proceeding
- Scripts check for required source files (article.md, slides.md) before export
- Shell scripts use `set -e` to exit on first error
- Missing dependencies (pandoc, marp-cli) cause export failures with clear error messages

## Cross-Cutting Concerns

**Logging:** None (shell scripts output to stdout/stderr)

**Validation:**
- YAML front-matter validation implicit (tools fail if malformed)
- Directory structure validation in export scripts
- Content validation handled by human review and AI assistance

**Authentication:** Not applicable (local filesystem operations only)

---

*Architecture analysis: 2026-01-26*
