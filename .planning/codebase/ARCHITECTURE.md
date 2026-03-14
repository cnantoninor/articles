# Architecture

**Analysis Date:** 2026-03-14

## Pattern Overview

**Overall:** Content-driven authoring system with validation and export pipeline

**Key Characteristics:**
- Topic-centric organization (epistemic_debt, philosophy_of_ai, ai_craft)
- Template-driven content creation with YAML front-matter
- Markdown-first workflow with multi-format export
- Automated validation and metadata management
- Git-based versioning with pre-push checks

## Layers

**Content Generation Layer:**
- Purpose: Author articles, slides, and research materials
- Location: `topics/*/` and `templates/`
- Contains: Markdown files with YAML front-matter, research notes, references
- Depends on: GLOSSARY.md for terminology consistency
- Used by: Export and validation layers

**Metadata & Validation Layer:**
- Purpose: Ensure consistency and completeness of front-matter
- Location: `scripts/validate-frontmatter.py`, `scripts/refresh-frontmatter.py`
- Contains: Python validators for YAML structure, date format, reading time calculations
- Depends on: YAML parsing library (pyyaml)
- Used by: Pre-push hook (via Makefile)

**Export Pipeline Layer:**
- Purpose: Convert Markdown to multiple output formats
- Location: `scripts/export-*.sh` (export-docx.sh, export-slides.sh, export-pdf.sh, export-all.sh)
- Contains: Bash wrapper scripts that invoke pandoc and marp-cli
- Depends on: External tools (pandoc, marp-cli) and markdown-it/puppeteer
- Used by: Content distribution workflow

**Configuration & Context Layer:**
- Purpose: Maintain AI authoring rules and conventions
- Location: `.ai/` (context.md, rules/), `.claude/rules/`, `.cursor/rules/`
- Contains: Writing style rules, terminology guidelines, publication workflow
- Depends on: Symlink synchronization (sync-rules.sh)
- Used by: AI tools (Claude, Cursor) for code generation and editing

**Planning & Tracking Layer:**
- Purpose: Organize article development phases and milestones
- Location: `.planning/` (phases/, milestones/, STATE.md, ROADMAP.md)
- Contains: Phase plans, verification docs, research notes, milestone definitions
- Depends on: GSD orchestration commands
- Used by: Project planning and progress tracking

## Data Flow

**Content Creation Flow:**

1. Author creates topic directory (`topics/{topic_name}/`)
2. Author copies templates to topic (article.md, slides.md, research.md)
3. Author fills YAML front-matter: title, status, audience, created date
4. Author writes content in Markdown (H1 title, H2 sections max, uses GLOSSARY terms)
5. Git pre-push hook triggered by `git push`

**Validation & Refresh Flow:**

1. `make pre-push-check` invoked by git hook
2. `bash .ai/sync-rules.sh` syncs symlinked rules to .cursor/ and .claude/
3. `python scripts/check-cta.py` validates call-to-action fields
4. `python scripts/refresh-frontmatter.py` computes current_length and estimated_reading_time from actual word count
5. `python scripts/validate-frontmatter.py` runs comprehensive validation:
   - Required fields (title, status, type) present
   - Date formats valid (YYYY-MM-DD)
   - Reading time consistent with word count (238 wpm baseline)
   - Status='published' requires all publication fields filled
   - Social teasers complete for published articles
6. Pre-push hook fails if validation errors detected; waits for manual fix and new commit

**Export Flow:**

1. `./scripts/export-docx.sh {topic} [file.md]` converts Markdown to DOCX via pandoc
2. `./scripts/export-slides.sh {topic} [file.md]` converts Markdown slides to PPTX via marp-cli
3. `./scripts/export-pdf.sh {topic} {article|slides|both}` converts via pandoc/puppeteer
4. `./scripts/export-all.sh {topic}` runs all exports in sequence
5. Outputs saved to `topics/{topic}/exports/` with timestamp in filename
6. Latest version symlinked without timestamp

**Publication Flow:**

1. Article status changed from 'draft' to 'review' in front-matter
2. Validation passes with all publication fields
3. Article status changed to 'published' with publication_url and published_date
4. Social teasers populated (linkedin, twitter, instagram_caption, substack_notes)
5. Exported to PDF/DOCX for Substack publication
6. Teasers distributed to LinkedIn, Twitter/X, Instagram, Substack Notes

**State Management:**

- File system of record: Git repository with topic directories
- Metadata source of truth: YAML front-matter in each article file
- Computation: Word counts and reading times computed on-demand, stored back in front-matter
- Versioning: Git commits track all changes; timestamps in export filenames track output revisions

## Key Abstractions

**Topic:**
- Purpose: Organize related articles, research, and assets around a central theme
- Examples: `topics/epistemic_debt/`, `topics/philosophy_of_ai/`, `topics/ai_craft/`
- Pattern: Each topic is self-contained directory with article/, artifacts/, exports/, references/, assets/, raw_material/

**Article Template:**
- Purpose: Standardize front-matter structure and content sections
- Examples: `templates/article.md`, `templates/slides.md`, `templates/research.md`
- Pattern: YAML front-matter followed by Markdown body with H1 title, H2 sections, H3 subsections (no deeper)

**YAML Front-Matter:**
- Purpose: Centralize metadata without duplicating in body text
- Schema: title, subtitle, status, type, audience[], target_length, current_length, estimated_reading_time, created, last_updated, published_date, publication_url, social_teasers{}
- Validation: Enforced by validate-frontmatter.py with field-level constraints

**Export:**
- Purpose: Convert single-source Markdown to multiple distribution formats
- Examples: DOCX for Google Docs editing, PPTX for presentations, PDF for final publication
- Pattern: Format-specific shell wrappers delegate to pandoc or marp-cli; outputs stored with timestamps

## Entry Points

**Author Starting New Topic:**
- Location: `templates/article.md`, `templates/slides.md`, `templates/research.md`
- Triggers: `cp templates/article.md topics/my_topic/article.md`
- Responsibilities: Provide consistent structure with YAML front-matter placeholders and content skeleton

**Pre-Push Git Hook:**
- Location: `.git/hooks/pre-push` (installed by `make install-pre-push-check`)
- Triggers: Git push operation
- Responsibilities: Run validation pipeline; fail with clear errors if front-matter or CTA invalid; auto-refresh computed fields

**Export Script User:**
- Location: `scripts/export-all.sh` (main entry), delegating to export-docx.sh, export-slides.sh, export-pdf.sh
- Triggers: `./scripts/export-all.sh epistemic_debt`
- Responsibilities: Parse topic directory, invoke pandoc/marp-cli, create exports/ directory, generate timestamped outputs

**Planning Orchestrator:**
- Location: `.planning/config.json`, phase and milestone definitions in `.planning/phases/` and `.planning/milestones/`
- Triggers: GSD commands (`/gsd:map-codebase`, `/gsd:plan-phase`, etc.)
- Responsibilities: Track project phases, generate analysis documents to `.planning/codebase/`

## Error Handling

**Strategy:** Fail-fast validation with human-readable error messages

**Patterns:**

- **Pre-push validation:** Front-matter errors block push; message directs to fix
- **Missing required fields:** ERROR level blocks publication; suggests field name and expected value
- **Invalid dates:** ERROR level if format not YYYY-MM-DD; accepts placeholder "YYYY-MM-DD" with INFO message
- **Inconsistent reading time:** WARN level if claimed reading_time differs >1 minute from computed (actual_words / 238 wpm)
- **Word count drift:** WARN level if current_length differs >10% from actual word count; triggers refresh-frontmatter.py to auto-correct
- **YAML parse errors:** ERROR level with yaml.YAMLError message; halts validation
- **Missing export tools:** Bash scripts check for pandoc/marp-cli presence; fail early with installation instructions

## Cross-Cutting Concerns

**Logging:** Console output from shell scripts and Python validators; color-coded via ANSI codes (RED=error, YELLOW=warn, GREEN=pass, CYAN=info)

**Validation:** Centralized in validate-frontmatter.py; multi-level (required, recommended, publication, computed consistency)

**Authentication:** None (local file-based system; publication credentials managed externally via Substack/social APIs)

**Terminology:** GLOSSARY.md is single source of truth; validated by `.ai/rules/terminology.md`

**Rules Synchronization:** `.ai/sync-rules.sh` creates symlinks from `.ai/rules/` to `.claude/rules/` and `.cursor/rules/` so all AI tools see same rules

---

*Architecture analysis: 2026-03-14*
