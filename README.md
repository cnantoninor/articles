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

2. Copy templates to get started:
   ```bash
   cp templates/article.md topics/my_new_topic/article.md
   cp templates/slides.md topics/my_new_topic/slides.md
   ```

3. Create supporting directories:
   ```bash
   mkdir -p topics/my_new_topic/{raw_material,references,assets,exports,artifacts/{articles/{drafts,published},presentation/{drafts,published}}}
   ```

4. Add a topic README:
   ```bash
   cp templates/research.md topics/my_new_topic/README.md
   ```

5. Start writing!

## Repository Structure

```
ai-articles/
├── README.md                    # This file
├── CLAUDE.md                    # AI context for Claude Code sessions
├── .cursorrules                 # AI context for Cursor sessions
├── GLOSSARY.md                  # Domain terms across all topics
├── .gitignore                   # Git ignore rules
├── scripts/
│   ├── setup.sh                 # Install prerequisites (Pandoc, Marp, LaTeX)
│   ├── export-docx.sh           # Markdown → DOCX (for Google Docs)
│   ├── export-slides.sh         # Marp → PPTX (for Google Slides)
│   ├── export-pdf.sh            # Markdown → PDF
│   └── export-all.sh            # Batch export for a topic
├── templates/
│   ├── article.md               # Article template with front-matter
│   ├── slides.md                # Marp presentation template
│   └── research.md              # Research/notes template
└── topics/                      # All article topics live here
    └── [topic_name]/            # Each topic follows this structure:
        ├── README.md            # Topic overview, status, links
        ├── article.md           # Main article draft
        ├── slides.md            # Marp presentation
        ├── raw_material/        # Working notes, brainstorms
        ├── references/          # Literature, citations
        ├── assets/              # Images, diagrams
        ├── artifacts/           # Polished outputs for distribution
        │   ├── articles/        #   Article versions (drafts/, published/)
        │   └── presentation/    #   Slide versions (drafts/, published/)
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

## Folder Conventions

- **raw_material/**: Working notes, brainstorming sessions, conversation logs
- **references/**: Literature reviews, citations, source material
- **assets/**: Images, diagrams, and other media
- **artifacts/**: Polished, distribution-ready versions of articles and presentations
  - `articles/drafts/` and `articles/published/` for article versions
  - `presentation/drafts/` and `presentation/published/` for slide versions
- **exports/**: Generated output files (DOCX, PPTX, PDF) from export scripts

## Current Topics

- **[epistemic_debt](topics/epistemic_debt/)** - Exploring epistemic risks of LLM-based software engineering

## AI Authoring

This repository is optimized for AI-assisted writing in Cursor. See `.cursorrules` for style guidelines and conventions. Reference `GLOSSARY.md` for consistent terminology.
