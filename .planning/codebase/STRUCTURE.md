# Codebase Structure

**Analysis Date:** 2026-03-14

## Directory Layout

```
ai-articles/
├── .ai/                    # Centralized AI authoring context (source of truth)
│   ├── context.md          # Rules and conventions (symlinked as CLAUDE.md)
│   ├── rules/              # Glob-activated rule files
│   │   ├── writing-style.md
│   │   ├── publication.md
│   │   ├── terminology.md
│   │   └── python.md
│   ├── commands/           # Custom AI commands for Claude/Cursor
│   │   ├── ar-create-execution-plan-for-phase.md
│   │   ├── ar-export-pdf.md
│   │   ├── ar-grammar-review.md
│   │   ├── ar-humanize.md
│   │   └── ar-infographics.md
│   └── sync-rules.sh       # Symlink synchronizer for .claude/ and .cursor/
├── .claude/                # Cursor AI rules (symlinked from .ai/rules/)
├── .cursor/                # Claude Code rules (symlinked from .ai/rules/)
├── .planning/              # GSD project planning artifacts
│   ├── config.json         # GSD orchestrator configuration
│   ├── STATE.md            # Current project state
│   ├── ROADMAP.md          # Project roadmap
│   ├── MILESTONES.md       # Milestone definitions
│   ├── codebase/           # Codebase analysis documents (ARCHITECTURE.md, STRUCTURE.md, etc.)
│   ├── phases/             # Phase plans and verification (numbered 01-, 09-, 10-, 11-, 12-, etc.)
│   └── milestones/         # Milestone requirements and roadmap
├── .github/                # GitHub workflows and actions
├── scripts/                # Utility and export scripts
│   ├── setup.sh            # Install prerequisites (pandoc, marp, LaTeX)
│   ├── export-docx.sh      # Export markdown to DOCX
│   ├── export-slides.sh    # Export marp slides to PPTX
│   ├── export-pdf.sh       # Export markdown/slides to PDF
│   ├── export-all.sh       # Batch export all formats
│   ├── check-cta.py        # Validate call-to-action fields
│   ├── refresh-frontmatter.py # Auto-compute current_length and reading_time
│   ├── validate-frontmatter.py # Comprehensive YAML front-matter validation
│   ├── run-analytics.sh    # Analytics execution
│   └── styles/
│       └── export-pdf.js   # Node.js PDF export via puppeteer + markdown-it
├── templates/              # Content templates for new articles/slides/research
│   ├── article.md          # Article template with YAML front-matter
│   ├── slides.md           # Marp presentation template
│   ├── research.md         # Research/notes template
│   └── social-teasers.md   # Social media teaser template
├── topics/                 # All article topics (main content directory)
│   ├── epistemic_debt/     # Epistemic risks of LLM-based software engineering
│   │   ├── README.md       # Topic overview and status
│   │   ├── article.md      # Main article draft
│   │   ├── slides.md       # Presentation draft
│   │   ├── sdd-epistemic-debt.md # SDD-format document
│   │   ├── iris-learnings.md # Research findings
│   │   ├── raw_material/   # Working notes, brainstorms, conversation logs
│   │   ├── references/     # Literature, citations, source material
│   │   ├── assets/         # Images, diagrams, media
│   │   ├── artifacts/      # Polished outputs (articles/, presentation/)
│   │   ├── exports/        # Generated DOCX, PPTX, PDF files
│   │   └── [...build artifacts...]
│   ├── philosophy_of_ai/   # Metaphors, epistemology, cognitive limits (TAM1, TAM2)
│   │   ├── README.md
│   │   ├── [same subdirectory structure as epistemic_debt]
│   │   └── exports/
│   ├── ai_craft/           # Development practice, design, identity (TAM3-TAM5)
│   │   ├── README.md
│   │   ├── code/           # Executable code samples
│   │   │   ├── ship_of_theseus/  # Python package for Ship of Theseus concept
│   │   │   └── vibe_designing/   # Python package for vibe designing concept
│   │   └── [standard topic structure]
│   └── [topic_name]/       # New topics follow this structure
├── analytics/              # Analytics and metrics tracking
├── docs/                   # Project documentation
├── .venv/                  # Python virtual environment
├── node_modules/           # npm dependencies
├── CLAUDE.md               # Symlink to .ai/context.md (always-applied rules)
├── GLOSSARY.md             # Domain terminology (single source of truth)
├── README.md               # Project overview and quickstart
├── Makefile                # Build automation (setup, pre-push checks)
├── package.json            # npm dependencies (markdown-it, puppeteer, etc.)
├── package-lock.json       # npm lockfile
├── requirements.txt        # Python dependencies (pyyaml)
├── requirements-dev.txt    # Dev dependencies
├── pyproject.toml          # Python project metadata
├── pytest.ini              # Pytest configuration
├── .python-version         # Python version specification (3.13)
├── .gitignore              # Git ignore rules
└── .mcp.json.example       # Example MCP server configuration
```

## Directory Purposes

**`.ai/` (Source of Truth for AI Context):**
- Purpose: Centralized authoring rules and conventions for Claude/Cursor
- Contains: context.md (master rules), rules/ (glob-activated by file path), custom commands
- Key files: `context.md`, `rules/writing-style.md`, `rules/publication.md`, `rules/terminology.md`

**`.planning/` (GSD Project Management):**
- Purpose: Organize article development phases, track progress, store analysis documents
- Contains: Phase definitions (01-, 09-, 10-, 11-, 12-), milestone definitions, config, codebase analysis
- Key files: `config.json`, `STATE.md`, `ROADMAP.md`, `codebase/ARCHITECTURE.md`

**`scripts/` (Automation and Tooling):**
- Purpose: Export, validation, setup, analytics
- Contains: Shell wrappers (export-*.sh), Python validators, Node.js PDF export
- Key files: `validate-frontmatter.py`, `refresh-frontmatter.py`, `export-all.sh`, `setup.sh`

**`templates/` (Content Blueprints):**
- Purpose: Provide starting structure for new articles, slides, research
- Contains: YAML front-matter skeleton, Markdown section placeholders
- Key files: `article.md`, `slides.md`, `research.md`, `social-teasers.md`

**`topics/` (Article Content):**
- Purpose: Organize all articles by topic; each topic is self-contained
- Contains: Article drafts, research notes, assets, published artifacts, exports
- Key directories: `epistemic_debt/`, `philosophy_of_ai/`, `ai_craft/` + subdirectories per topic

**`topics/{topic_name}/` (Topic Structure - All Topics Follow This):**
- `README.md`: Topic overview, current status, links to related articles
- `article.md`: Main article draft (YAML front-matter + markdown body)
- `slides.md`: Presentation draft for marp compiler
- `raw_material/`: Working notes, brainstorms, conversation logs, internal thoughts
- `references/`: Literature, citations, research sources
- `assets/`: Images, diagrams, infographics, media files
- `artifacts/articles/`: Polished article versions (versioned by filename, status in frontmatter)
- `artifacts/presentation/`: Polished presentation versions
- `exports/`: Generated DOCX, PPTX, PDF files (timestamped filenames + latest symlink)

**`topics/ai_craft/code/` (Special: Executable Code):**
- Purpose: Python packages demonstrating concepts from articles
- Examples: `ship_of_theseus/` (Ship of Theseus refactoring concept), `vibe_designing/` (intuitive design pattern)
- Pattern: Each package is importable Python module with __init__.py, tests, documentation

## Key File Locations

**Entry Points:**

- `templates/article.md`: Copy this to start new article in topic directory
- `scripts/export-all.sh`: Main entry point for exporting a topic to all formats
- `.git/hooks/pre-push`: Git hook triggered by push (installed by `make install-pre-push-check`)
- `.planning/config.json`: GSD orchestrator configuration

**Configuration:**

- `CLAUDE.md` → `.ai/context.md`: Master authoring rules (symlinked)
- `GLOSSARY.md`: Domain terminology (single source of truth)
- `.ai/rules/writing-style.md`: Writing conventions
- `.ai/rules/publication.md`: Publication and social teaser workflow
- `.ai/rules/terminology.md`: Term definitions and usage
- `Makefile`: Build automation targets

**Core Logic:**

- `scripts/validate-frontmatter.py`: YAML validation, date checking, reading time calculation, consistency checks
- `scripts/refresh-frontmatter.py`: Auto-compute current_length and estimated_reading_time from word count
- `scripts/export-docx.sh`: Pandoc wrapper for Markdown → DOCX conversion
- `scripts/export-slides.sh`: Marp wrapper for Markdown → PPTX conversion
- `scripts/export-pdf.sh`: Pandoc/puppeteer wrapper for Markdown → PDF conversion

**Testing:**

- `pytest.ini`: Pytest configuration (Python tests for scripts/)
- No traditional test files detected; validation tested via pre-push hook

**Analytics:**

- `analytics/`: Analytics tracking and metrics
- `scripts/run-analytics.sh`: Analytics execution script

## Naming Conventions

**Files:**

- Markdown: lowercase with hyphens (`article.md`, `sdd-epistemic-debt.md`, `iris-learnings.md`)
- Scripts: lowercase with hyphens or underscores (`.sh`, `.py`) — `export-docx.sh`, `validate-frontmatter.py`
- Exports: `{basename}-{YYYYMMDD}.{ext}` for timestamped, `{basename}.{ext}` for latest symlink
- Phase plans: numbered `{NN}-{topic}/` e.g., `phases/01-opening-framing/`

**Directories:**

- Topics: lowercase with underscores (`epistemic_debt`, `philosophy_of_ai`, `ai_craft`)
- Standard subdirs in topics: `raw_material`, `references`, `assets`, `artifacts`, `exports`
- Phase dirs: zero-padded numeric prefix (`01-`, `09-`, `10-`) followed by descriptive name
- Nested code packages: lowercase with underscores (`ship_of_theseus`, `vibe_designing`)

**YAML Front-Matter Fields:**

- Metadata: `title`, `subtitle`, `status`, `type`, `audience`, `target_length`, `current_length`, `estimated_reading_time`
- Dates: `created`, `last_updated`, `published_date` (format: YYYY-MM-DD)
- Publication: `publication_url`, `social_teasers` (object with linkedin, twitter, instagram_caption, substack_notes keys)

## Where to Add New Code

**New Article:**
- Primary code: Copy `templates/article.md` to `topics/{topic_name}/article.md`
- Tests: No traditional tests; validation via `make pre-push-check` (validates front-matter and CTA)
- Pattern: Use YAML front-matter for metadata; write Markdown body with H1 title only, H2 sections, H3 subsections max

**New Topic:**
- Primary directory: Create `topics/{new_topic_name}/`
- Initialize: Create subdirs: `raw_material/`, `references/`, `assets/`, `artifacts/{articles,presentation}/`, `exports/`
- README: Copy `templates/research.md` to `topics/{new_topic_name}/README.md`
- Article: Copy `templates/article.md` to `topics/{new_topic_name}/article.md`
- Slides: Copy `templates/slides.md` to `topics/{new_topic_name}/slides.md`

**New Script:**
- Bash utilities: Add to `scripts/`, follow naming convention `lowercase-with-hyphens.sh`
- Python utilities: Add to `scripts/`, follow naming convention `lowercase_with_underscores.py`; use argparse for CLI
- Node.js: Add to `scripts/styles/`, follow pattern in `export-pdf.js`

**Terminology:**
- Glossary entry: Add to `GLOSSARY.md` with format: `**Term**: One-line definition.` (only novel/niche terms)
- Preserve author's voice: Do not prescribe definitions; document how author uses terms

## Special Directories

**`.planning/` (GSD Orchestration):**
- Purpose: Project planning and progress tracking
- Generated: Yes (by GSD commands)
- Committed: Yes (phases, milestones, config, analysis)

**`topics/{topic}/exports/` (Generated Export Files):**
- Purpose: DOCX, PPTX, PDF outputs from export scripts
- Generated: Yes (by export-*.sh scripts)
- Committed: No (add to .gitignore or use .gitkeep for structure)

**`topics/{topic}/artifacts/` (Polished Outputs):**
- Purpose: Distribution-ready articles and presentations
- Generated: No (manually curated, committed)
- Committed: Yes (versioning via filename and frontmatter status field)

**`node_modules/` and `.venv/` (Dependencies):**
- Purpose: Installed packages
- Generated: Yes (by npm install or make install)
- Committed: No (.gitignore'd)

**`.ai/rules/` and `.claude/` / `.cursor/` (Symlinked Rules):**
- Purpose: AI tool configuration
- Generated: No (source of truth in `.ai/rules/`)
- Committed: Symlinks committed; synced by `bash .ai/sync-rules.sh`

---

*Structure analysis: 2026-03-14*
