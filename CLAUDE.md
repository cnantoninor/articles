# AI Articles Repository — Claude Code Context

## Project Overview

A structured repository for developing articles, presentations, and research on AI-related topics. Designed for AI-assisted authoring with consistent conventions and export workflows.

## Repository Structure

```
ai-articles/
├── CLAUDE.md                    # This file (Claude Code context)
├── .cursorrules                 # AI context for Cursor sessions
├── GLOSSARY.md                  # Shared terminology across all topics
├── scripts/                     # Export and setup scripts
│   ├── setup.sh                 # Install prerequisites
│   ├── export-docx.sh           # Markdown → DOCX
│   ├── export-slides.sh         # Marp → PPTX
│   ├── export-pdf.sh            # Markdown → PDF
│   └── export-all.sh            # Batch export
├── templates/                   # Starting templates for new content
│   ├── article.md
│   ├── slides.md
│   └── research.md
└── topics/                      # All article topics
    └── [topic_name]/
        ├── README.md            # Topic overview and status
        ├── article.md           # Main article draft
        ├── slides.md            # Marp presentation
        ├── raw_material/        # Working notes, brainstorms
        ├── references/          # Literature, citations
        ├── assets/              # Images, diagrams
        ├── artifacts/           # Polished outputs (articles/, presentation/)
        └── exports/             # Generated DOCX, PPTX, PDF
```

## Key Conventions

- **Topics directory**: All content lives under `topics/<topic_name>/`
- **Templates**: New topics should start from files in `templates/`
- **Terminology**: Check `GLOSSARY.md` for consistent definitions
- **Front-matter**: All articles use YAML front-matter (see `.cursorrules` for format)
- **Gap markers**: Use `[GAP: ...]`, `[TODO: ...]`, `[QUESTION: ...]`, `[EXAMPLE NEEDED]`

## Writing Style

- Exploratory, not prescriptive — present ideas as investigations
- Thoughtful and nuanced — acknowledge trade-offs
- Accessible but rigorous — define technical/philosophical terms on first use
- Mark uncertainties explicitly rather than inventing content

## Export Workflow

```bash
# Export a topic to all formats
./scripts/export-all.sh <topic_name>

# Individual exports
./scripts/export-docx.sh <topic_name> [file.md]
./scripts/export-slides.sh <topic_name> [file.md]
./scripts/export-pdf.sh <topic_name> [article|slides|both|file.md]
```

## Current Topics

- **epistemic_debt** — Epistemic risks of LLM-based software engineering

## Important Notes

- See `.cursorrules` for full writing style guidelines, content structure conventions, and AI assistant instructions
- See `GLOSSARY.md` for domain terminology definitions
- Multiple article variants may exist within a topic (not just `article.md`)
- The `artifacts/` directory holds polished, distribution-ready versions
- The `exports/` directory holds script-generated output files
