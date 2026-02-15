# Codebase Structure

**Analysis Date:** 2026-02-15

## Directory Layout

```
ai-articles/
├── .cursorrules                # AI authoring guidelines (Cursor IDE auto-loads)
├── CLAUDE.md                   # Claude Code agent instructions
├── README.md                   # Repository docs, quickstart, structure overview
├── GLOSSARY.md                 # Shared domain terminology with AI usage notes
├── .gitignore                  # Ignores node_modules, .planning/phases
├── scripts/                    # Export automation and setup scripts
│   ├── setup.sh                # Installs pandoc, marp-cli, LaTeX
│   ├── export-all.sh           # Batch export orchestrator
│   ├── export-docx.sh          # Markdown → DOCX via pandoc
│   ├── export-slides.sh        # Marp → PPTX via marp-cli
│   └── export-pdf.sh           # Markdown/Marp → PDF via pandoc/marp
├── templates/                  # Content scaffolding templates
│   ├── article.md              # Article template with YAML front-matter
│   ├── slides.md               # Marp presentation template with speaker notes
│   └── research.md             # Topic README/research tracker template
├── topics/                     # All topic content lives here
│   └── epistemic_debt/         # Example topic (currently the only one)
│       ├── README.md           # Topic overview, status, gaps, next steps
│       ├── article.md          # Main article draft (~600 lines, 10K+ words)
│       ├── cursor-article.md   # Variant article (Cursor-focused audience)
│       ├── iris-learnings.md   # Internal presentation (Marp, ~540 lines)
│       ├── slides.md           # Public presentation (Marp, ~270 lines)
│       ├── raw_material/       # Working notes and brainstorms
│       │   ├── gsd-convo-1-on-epistemic-debt.md   # Conversation log (~90KB)
│       │   └── outline-v1-epistemic-debt.md        # Structured outline
│       ├── references/         # Source material and literature
│       │   ├── literature-review-on-epistemic-debt.md
│       │   ├── Epistemic_debt_definition.md
│       │   ├── epistemic-trade-off-triangle.md
│       │   ├── paper1.pdf ... paper5.pdf           # Academic papers
│       │   ├── article1.pdf
│       │   ├── Epistemic Debt Research Complete.pdf
│       │   └── Triangle Interaction Table.pdf
│       ├── assets/             # Images and diagrams
│       │   └── epistemic-trade-off-triangle.md     # Diagram description
│       ├── artifacts/          # Supplementary artifact storage
│       │   ├── articles/
│       │   │   ├── drafts/
│       │   │   └── published/
│       │   └── presentation/
│       │       ├── drafts/
│       │       └── published/
│       └── exports/            # Generated outputs
│           ├── export-pdf.js           # Node.js high-quality PDF exporter
│           ├── pdf-export-styles.css   # Typographic styles for Puppeteer PDF
│           ├── pdf-styles.css          # Alternative PDF stylesheet
│           ├── claude-article.pdf      # Exported article PDF
│           ├── claude-article-cc.pdf   # High-quality article PDF (via Puppeteer)
│           ├── cursor-article-cc.pdf   # High-quality variant PDF
│           ├── cursor-article.pdf      # Exported variant PDF
│           ├── iris-learnings.html     # Exported presentation HTML
│           ├── iris-learnings.pptx     # Exported presentation PPTX
│           └── iris-learnings-editable.pptx
├── tmp/                        # Temporary/scratch files (images, working docs)
├── .cursor/                    # Cursor IDE metadata
│   └── plans/                  # AI-generated planning artifacts
├── .claude/                    # Claude Code configuration
│   └── settings.local.json     # Local Claude settings
└── .planning/                  # Project planning and analysis
    ├── codebase/               # Codebase mapping documents (this file, etc.)
    ├── milestones/             # Milestone tracking
    ├── phases/                 # Phase planning (gitignored)
    └── research/               # Research planning
```

## Directory Purposes

**Root Directory:**
- Purpose: Repository-level documentation and AI configuration
- Contains: README, glossary, AI assistant config files, Git config
- Key files:
  - `README.md`: Getting started guide, quickstart for new topics, structure overview, export workflow docs
  - `.cursorrules`: Comprehensive AI authoring guidelines — tone, structure, terminology, file organization, gap markers
  - `GLOSSARY.md`: 74-line domain terminology reference with AI usage notes (e.g., "prefer 'understanding' over 'knowledge'")
  - `CLAUDE.md`: Claude Code agent instructions (currently empty — conventions primarily in `.cursorrules`)

**`scripts/`:**
- Purpose: Automation scripts for exporting content and setting up the development environment
- Contains: 5 bash scripts — 4 export scripts and 1 setup script
- Key files:
  - `export-all.sh`: Batch orchestrator — calls docx, slides, and pdf scripts; supports optional file targeting
  - `export-docx.sh`: Pandoc wrapper; generates timestamped + latest DOCX in `exports/`
  - `export-slides.sh`: Marp wrapper; generates timestamped + latest PPTX in `exports/`
  - `export-pdf.sh`: Mode-based (article/slides/both/custom); uses pandoc for articles, marp for slides
  - `setup.sh`: Cross-platform installer for pandoc, npm, marp-cli, and LaTeX (supports apt, dnf, pacman, brew)

**`templates/`:**
- Purpose: Scaffolding for new content — copy to a topic directory to start writing
- Contains: 3 Markdown templates with pre-filled structure
- Key files:
  - `article.md`: YAML front-matter (title, status, type, audience, dates) + Abstract → Introduction → Sections → Conclusion → References with `[GAP:]` markers
  - `slides.md`: Marp front-matter (marp: true, theme, paginate) + title slide → agenda → key concepts → summary → Q&A with speaker notes
  - `research.md`: Topic overview with status tracking, key questions, source tracking table, key quotes, working notes, gaps, connections, next steps

**`topics/`:**
- Purpose: Container for all topic workspaces — each topic is a self-contained directory
- Contains: One or more topic directories (currently only `epistemic_debt/`)
- Convention: Topic directories use `lowercase_underscores`

**`topics/<topic_name>/`:**
- Purpose: Complete workspace for a single subject — all content, research, and outputs in one place
- Contains: Markdown content files + standard subdirectories
- Key files:
  - `README.md`: Topic status tracker — overview, key questions, file inventory, gaps, next steps
  - `article.md`: Primary long-form article draft
  - `slides.md`: Primary presentation (Marp format)
  - Optional variants: Additional articles for different audiences (e.g., `cursor-article.md`, `iris-learnings.md`)

**`topics/<topic_name>/raw_material/`:**
- Purpose: Unstructured working notes, brainstorming, and conversation logs
- Contains: Early outlines, AI conversation logs, rough ideas
- Convention: Descriptive names with version markers — `outline-v1-epistemic-debt.md` not `notes.md`

**`topics/<topic_name>/references/`:**
- Purpose: Source material — literature reviews, academic papers, reference documents
- Contains: Markdown literature reviews, PDF papers, definition documents
- Convention: Mix of Markdown summaries and PDF originals

**`topics/<topic_name>/assets/`:**
- Purpose: Media files referenced by articles and presentations
- Contains: Images, diagrams, chart descriptions

**`topics/<topic_name>/artifacts/`:**
- Purpose: Supplementary artifact organization with drafts/published lifecycle
- Contains: Subdirectories `articles/{drafts,published}` and `presentation/{drafts,published}`
- Note: Currently empty — used for lifecycle-stage organization of finished artifacts

**`topics/<topic_name>/exports/`:**
- Purpose: Generated distributable files — the output of the export pipeline
- Contains: DOCX, PPTX, PDF, HTML files; also contains the Node.js PDF exporter and CSS stylesheets
- Convention: Timestamped files (`article-20260215.docx`) plus latest copies (`article.docx`)

**`tmp/`:**
- Purpose: Scratch space for temporary and in-progress files
- Contains: Image files (PNG), working documents (DOCX)
- Note: Not gitignored — consider adding to `.gitignore`

**`.planning/`:**
- Purpose: Project analysis and planning documentation
- Contains: Codebase mapping docs, milestone tracking, phase plans, research notes
- Note: `.planning/phases` is gitignored; `.planning/codebase/` is committed

## Key File Locations

**Entry Points for New Content:**
- `templates/article.md`: Copy to start a new article
- `templates/slides.md`: Copy to start a new presentation
- `templates/research.md`: Copy to create topic README

**Configuration (AI Context):**
- `.cursorrules`: Writing tone, structure conventions, terminology, AI assistant instructions — auto-loaded by Cursor IDE
- `GLOSSARY.md`: Domain vocabulary with definitions and AI usage notes
- `CLAUDE.md`: Claude Code agent instructions

**Export Pipeline:**
- `scripts/export-all.sh`: Batch export entry point
- `scripts/export-docx.sh`: Article → DOCX (pandoc)
- `scripts/export-slides.sh`: Slides → PPTX (marp)
- `scripts/export-pdf.sh`: Article/Slides → PDF (pandoc/marp)
- `topics/epistemic_debt/exports/export-pdf.js`: High-quality PDF with footnotes (Puppeteer + markdown-it)
- `topics/epistemic_debt/exports/pdf-export-styles.css`: Typography and layout for Puppeteer PDF output

**Active Content (epistemic_debt topic):**
- `topics/epistemic_debt/article.md`: Main article (~607 lines, sections I-VII, with footnotes and references)
- `topics/epistemic_debt/cursor-article.md`: Variant for Cursor-focused audience
- `topics/epistemic_debt/slides.md`: Public presentation (~276 lines, 14 slides)
- `topics/epistemic_debt/iris-learnings.md`: Internal team presentation (~540 lines)
- `topics/epistemic_debt/README.md`: Topic status, gaps, next steps

## Naming Conventions

**Files:**
- Lowercase with hyphens for general files: `export-docx.sh`, `literature-review-on-epistemic-debt.md`
- Standard names for topic content: `article.md`, `slides.md`, `README.md`
- Descriptive names with version markers for working files: `outline-v1-epistemic-debt.md`
- Shell scripts: `.sh` extension with executable permissions
- Markdown: `.md` extension for all text content

**Directories:**
- Lowercase with underscores for topic directories: `topics/epistemic_debt/`
- Lowercase with underscores for subdirectories: `raw_material/`, not `raw-material/`
- Hidden directories for tooling: `.cursor/`, `.planning/`, `.claude/`

**YAML Front-Matter Fields (articles):**
- `title`: Quoted string
- `status`: `draft` | `review` | `published`
- `type`: `article` | `slides` | `research`
- `audience`: Array of target reader types (e.g., `[engineering leaders, senior engineers]`)
- `target_length`: Word count target (e.g., `6000-10000`)
- `created`: `YYYY-MM-DD`
- `last_updated`: `YYYY-MM-DD`

**Marp Front-Matter Fields (slides):**
- `marp: true` (required)
- `theme`: Marp theme name (e.g., `default`)
- `paginate: true`
- `title`: Presentation title

## Where to Add New Code

**New Topic:**
1. Create directory: `mkdir topics/new_topic_name`
2. Copy templates: `cp templates/article.md topics/new_topic_name/`
3. Copy slides template: `cp templates/slides.md topics/new_topic_name/`
4. Create README: `cp templates/research.md topics/new_topic_name/README.md`
5. Create subdirectories: `mkdir -p topics/new_topic_name/{raw_material,references,assets,exports}`
6. Update `README.md` at root to list the new topic under "Current Topics"

**New Article Variant in Existing Topic:**
- Place in topic root: `topics/<topic_name>/<descriptive-name>.md`
- Use same YAML front-matter structure as `article.md`
- Example: `topics/epistemic_debt/cursor-article.md` (variant for different audience)

**New Export Format Script:**
- Script location: `scripts/export-<format>.sh`
- Follow existing pattern:
  1. Accept topic name as `$1`, optional file as `$2`
  2. Resolve `TOPIC_DIR="$REPO_ROOT/topics/$TOPIC"`
  3. Validate directory and source file existence
  4. Create `exports/` directory if missing
  5. Generate timestamped output + latest copy
- Register in `export-all.sh` if it should run during batch exports

**New Template:**
- Location: `templates/<type>.md`
- Include appropriate YAML front-matter structure
- Add `[GAP: description]` markers for placeholder sections
- Document in root `README.md` under quickstart

**New Terminology:**
- Add to `GLOSSARY.md` under appropriate H2 section
- Include definition and any AI usage notes
- If topic-specific, add under the topic's H2 heading

**New Research/Reference Material:**
- Working notes: `topics/<topic>/raw_material/<descriptive-name>.md`
- Literature: `topics/<topic>/references/<descriptive-name>.md` or `.pdf`

## Special Directories

**`topics/<topic>/exports/`:**
- Purpose: Generated distributable outputs
- Generated: Yes (by export scripts and manual exports)
- Committed: Partially — PDF/PPTX outputs and supporting scripts/CSS are committed
- Note: Should review what should be gitignored vs. committed

**`topics/<topic>/artifacts/`:**
- Purpose: Lifecycle-organized artifact storage (drafts → published)
- Generated: Mixed (manually organized)
- Committed: Yes (directory structure committed, contents may be empty)

**`.planning/`:**
- Purpose: Project analysis, codebase mapping, and phase planning
- Generated: Yes (by analysis tools and planning processes)
- Committed: Partially — `codebase/` committed, `phases/` gitignored

**`.cursor/`:**
- Purpose: Cursor IDE metadata and AI planning artifacts
- Generated: Yes (by Cursor IDE)
- Committed: Yes

**`tmp/`:**
- Purpose: Scratch/working files
- Generated: Manually
- Committed: Currently yes — should likely be gitignored

---

*Structure analysis: 2026-02-15*
