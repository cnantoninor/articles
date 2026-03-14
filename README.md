# AI Articles Repository

A structured repository for developing articles, presentations, and research on AI-related topics. Designed for AI-assisted authoring with consistent conventions and export workflows.

## Prerequisites

The easiest way to set up the required tools is to run the setup script:

```bash
./scripts/setup.sh
```

This script will detect your OS and install **Pandoc**, **Marp CLI**, and **LaTeX** for you.

Alternatively, you can install them manually:

- **pandoc** - For Markdown → DOCX/PDF conversion
  ```bash
  # Ubuntu/Debian
  sudo apt install pandoc
  
  # macOS
  brew install pandoc
  ```

- **marp-cli** - For Markdown → PPTX/PDF slides
  ```bash
  npm install -g @marp-team/marp-cli
  ```

## Quickstart: Creating a New Topic

1. Create a new directory for your topic under `topics/`:
   ```bash
   mkdir topics/my_new_topic
   ```

2. Create supporting directories:
   ```bash
   mkdir -p topics/my_new_topic/{raw_material,references,assets,exports,artifacts/{articles,presentation}}
   ```

3. Add a topic README and first article:
   ```bash
   cp templates/research.md topics/my_new_topic/README.md
   cp templates/article.md topics/my_new_topic/artifacts/articles/my-article.md
   ```

4. Start writing!

## Repository Structure

```
ai-articles/
├── README.md                    # This file
├── CLAUDE.md -> .ai/context.md  # AI context (symlink, always-applied)
├── GLOSSARY.md                  # Domain terms across all topics
├── .gitignore                   # Git ignore rules
├── Makefile                     # Build/dev convenience targets
├── .mcp.json.example            # MCP config template (real .mcp.json is gitignored)
├── .ai/                         # Centralized AI context (source of truth)
│   ├── context.md               # Concise rulebook (always-applied)
│   ├── commands/                # AI prompt commands (ar-export-pdf, ar-humanize, etc.)
│   ├── rules/                   # Glob-activated rules
│   │   ├── writing-style.md     # Writing style & content structure
│   │   ├── publication.md       # Publication workflow & social teasers
│   │   ├── python.md            # Python coding conventions
│   │   └── terminology.md       # Domain terminology & key concepts
│   └── sync-rules.sh            # Creates/updates symlinks for all tools
├── analytics/                   # GA4 + manual analytics pipeline
│   ├── scripts/                 # fetch_ga4.py, ingest.py, merge.py, report.py, analyze.py
│   ├── data/                    # Raw and combined CSV data
│   ├── reports/                 # Generated weekly reports
│   ├── prompts/                 # Claude Chrome plugin extraction prompts
│   ├── credentials/             # GA4 service account keys (gitignored)
│   └── COLLECTION-CHECKLIST.md  # Weekly analytics checklist
├── docs/                        # Project documentation
│   ├── mcp-setup.md             # MCP server setup guide
│   └── publishing-workflow.md   # End-to-end publishing workflow
├── scripts/
│   ├── setup.sh                 # Install prerequisites (Pandoc, Marp, LaTeX)
│   ├── export-docx.sh           # Markdown → DOCX (for Google Docs)
│   ├── export-slides.sh         # Marp → PPTX (for Google Slides)
│   ├── export-pdf.sh            # Markdown → PDF
│   ├── export-all.sh            # Batch export for a topic
│   ├── run-analytics.sh         # Full analytics pipeline
│   ├── check-cta.py             # Validate article CTAs
│   ├── validate-frontmatter.py  # Validate YAML front-matter
│   ├── refresh-frontmatter.py   # Refresh front-matter fields
│   └── styles/                  # CSS and JS for PDF/HTML export
├── templates/
│   ├── article.md               # Article template with front-matter
│   ├── slides.md                # Marp presentation template
│   ├── research.md              # Research/notes template
│   └── social-teasers.md        # Social teaser drafting template
└── topics/                      # All article topics live here
    ├── epistemic_debt/          # Epistemic risks of LLM-based software engineering
    ├── philosophy_of_ai/        # Metaphors, epistemology, Plato and AI (TAM1, TAM2)
    ├── ai_craft/                # Deleting code, vibe designing, Ship of Theseus (TAM3–TAM5); includes code/
    └── [topic_name]/            # New topics follow this structure:
        ├── README.md            # Topic overview, status, links
        ├── raw_material/        # Working notes, brainstorms
        ├── references/          # Literature, citations
        ├── assets/              # Images, diagrams
        ├── artifacts/           # Polished outputs for distribution (flat; no drafts/published subdirs)
        │   ├── articles/        #   Article artifacts; status in frontmatter
        │   └── presentation/    #   Presentation artifacts; status in frontmatter
        └── exports/             # Generated DOCX, PPTX, PDF
```

## Export Workflow

Export a topic to various formats:

```bash
# Export article to DOCX (for Google Docs)
./scripts/export-docx.sh epistemic_debt

# Export slides to PPTX (for Google Slides)
./scripts/export-slides.sh epistemic_debt

# Export to PDF (article, slides, or both)
./scripts/export-pdf.sh epistemic_debt article
./scripts/export-pdf.sh epistemic_debt slides
./scripts/export-pdf.sh epistemic_debt both

# Export all formats at once
./scripts/export-all.sh epistemic_debt
```

All exports are saved to `topics/<topic>/exports/`.

## Publication

Articles are published on **[The AI Mirror](https://antoninorau.substack.com/)** — a Substack publication exploring AI, philosophy, and spirituality.

**Social channels:**
- [LinkedIn](https://www.linkedin.com/in/antoninorau/) — professional framing, industry relevance
- [Twitter/X](https://x.com/antoninorau) — hook + insight teasers
- [Instagram](https://www.instagram.com/eckardius_/) — visual + caption format
- Substack Notes — native short-form for organic discovery

**Workflow:** Publish on Substack → create platform-specific teasers → cross-post to social channels.

See `.ai/rules/publication.md` for detailed teaser conventions and distribution workflow.

## Folder Conventions

- **raw_material/**: Working notes, brainstorming sessions, conversation logs
- **references/**: Literature reviews, citations, source material
- **assets/**: Images, diagrams, and other media
- **artifacts/**: Polished, distribution-ready versions of articles and presentations; flat `articles/` and `presentation/` only (no `drafts/` or `published/` subdirs); version and publication state in frontmatter and git
- **exports/**: Generated output files (DOCX, PPTX, PDF) from export scripts

## Current Topics

- **[epistemic_debt](topics/epistemic_debt/)** - Exploring epistemic risks of LLM-based software engineering
- **[philosophy_of_ai](topics/philosophy_of_ai/)** - Metaphors, epistemology, and cognitive limits (TAM1, TAM2)
- **[ai_craft](topics/ai_craft/)** - Development practice, design, and identity (TAM3, TAM4, TAM5)

## AI Authoring

This repository is optimized for AI-assisted writing in both Cursor and Claude Code.

- **Rules source of truth**: `.ai/` directory (context + glob-activated rules)
- **Symlink**: `CLAUDE.md` points to `.ai/context.md` (always-applied by both Cursor and Claude Code)
- **Glob rules**: `.cursor/rules/` and `.claude/rules/` are symlinked from `.ai/rules/`
- **Sync**: Run `bash .ai/sync-rules.sh` to create or update all symlinks
- **Terminology**: See `GLOSSARY.md` for consistent domain terms

> **Note (symlink compatibility)**: Symlinks work natively on Linux and WSL2. On Windows, you may need to enable Developer Mode or run `git config core.symlinks true`.
