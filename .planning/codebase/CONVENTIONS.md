# Coding Conventions

**Analysis Date:** 2026-01-26

## Naming Patterns

**Files:**
- Lowercase with hyphens for markdown files: `file-name.md`
- Lowercase with underscores for directories: `topic_name/`
- Descriptive names preferred: `outline-v1-epistemic-debt.md` over `notes.md`
- Template files use base names: `article.md`, `slides.md`, `research.md`
- Exported files include timestamps: `article-20260126.docx`

**Scripts:**
- Executable shell scripts with `.sh` extension
- Action-oriented naming: `export-docx.sh`, `export-all.sh`
- Hyphen-separated words: `export-pdf.sh`

**Variables (Bash):**
- UPPERCASE for environment/config variables: `TOPIC_DIR`, `SCRIPT_DIR`, `REPO_ROOT`
- Lowercase for function parameters: `topic`
- Descriptive names: `OUTPUT_FILE`, `TIMESTAMP`

**Functions (Bash):**
- Lowercase with underscores: `export_article`, `export_slides`
- Verb-based naming indicating action

## Code Style

**Formatting:**
- Not applicable (content repository, not software project)

**Linting:**
- Not detected

**Shell Scripts:**
- Bash strict mode: `set -e` (exit on error)
- Comment headers with usage examples
- Validation before execution (check directory exists, file exists)

## Content Style (Markdown)

**Heading Hierarchy:**
- H1 (`#`) for article title only
- H2 (`##`) for major sections
- H3 (`###`) for subsections
- Avoid going deeper than H4

**Front-Matter:**
- YAML format at top of articles and slides
- Required fields: `title`, `status`, `type`, `audience`, `target_length`, `created`, `last_updated`
- Standard values: `status: draft | review | published`
- Standard types: `type: article | slides | research`

**Lists:**
- Parallel structure (consistent grammatical form)
- Prefer active voice

**Citations:**
- Academic: Author (Year) or (Author, Year)
- Web/informal: linked text or footnote
- Reference lists: `Author. "Title." *Publication*, Year. [URL]`

## Import Organization

**Not applicable** - This is a content repository without code imports.

## Error Handling

**Patterns (Bash scripts):**
- Use `set -e` to exit on first error
- Validate inputs at script start: check for required arguments, verify paths exist
- Print clear error messages to stderr
- Exit with non-zero status codes on failure
- Use `|| true` to continue after expected failures: `export_article || true`

**Example pattern from `scripts/export-pdf.sh`:**
```bash
if [ ! -d "$TOPIC_DIR" ]; then
    echo "Error: Topic directory '$TOPIC_DIR' does not exist"
    exit 1
fi
```

## Logging

**Framework:** `echo` commands to stdout/stderr

**Patterns:**
- Section headers with visual delimiters: `echo "=========================================="`
- Progress messages: `echo "Exporting $TOPIC/article.md to PDF..."`
- Completion confirmations: `echo "Created: $OUTPUT_FILE"`
- Warnings for non-fatal issues: `echo "Warning: No article.md found..."`

## Comments

**When to Comment:**

**Bash scripts:**
- File-level header with purpose, usage, and example
- Comments before validation blocks
- Speaker notes in Marp slides using `<!-- comment -->`

**Example from `scripts/export-all.sh`:**
```bash
#!/bin/bash
# Export all formats for a topic (DOCX, PPTX, PDF)
# Usage: ./scripts/export-all.sh <topic-directory>
#
# Example: ./scripts/export-all.sh epistemic_debt
```

**Markdown content:**
- Gap markers for incomplete sections: `[GAP: description]`
- TODO markers for specific tasks: `[TODO: task]`
- Questions to address: `[QUESTION: question]`
- Example placeholders: `[EXAMPLE NEEDED]`

## Gap Markers Convention

**Purpose:** Mark incomplete sections explicitly rather than leaving them blank

**Patterns:**
- `[GAP: description]` - Content that needs to be written
- `[TODO: task]` - Specific task to complete
- `[QUESTION: question]` - Open question to address
- `[EXAMPLE NEEDED]` - Place where concrete example is required

**Usage:** Used extensively in `epistemic_debt/article.md` and templates

## Directory Structure Convention

**Standard topic structure:**
```
topic_name/
├── README.md        # Topic overview and status
├── article.md       # Main article draft
├── slides.md        # Presentation (Marp format)
├── raw_material/    # Working notes, brainstorms
├── references/      # Literature, citations
├── assets/          # Images, diagrams
└── exports/         # Generated outputs (DOCX, PPTX, PDF)
```

**Root structure:**
```
ai-articles/
├── README.md
├── .cursorrules (symlinked as CLAUDE.md)
├── GLOSSARY.md
├── scripts/
├── templates/
└── [topic-name]/
```

## Script Design Patterns

**Parameter Handling:**
- Check for required arguments at script start
- Provide usage examples in error messages
- Support optional parameters with defaults: `MODE="${2:-both}"`

**Path Resolution:**
- Use absolute paths resolved from script location:
  ```bash
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  REPO_ROOT="$(dirname "$SCRIPT_DIR")"
  ```

**Directory Creation:**
- Create output directories if they don't exist: `mkdir -p "$TOPIC_DIR/exports"`

**Timestamping:**
- Generate timestamps for versioned outputs: `TIMESTAMP=$(date +%Y%m%d)`
- Create both timestamped and "latest" versions

**Example from `scripts/export-docx.sh`:**
```bash
OUTPUT_FILE="$TOPIC_DIR/exports/article-$TIMESTAMP.docx"
# ... export ...
cp "$OUTPUT_FILE" "$TOPIC_DIR/exports/article.docx"
```

## Terminology Conventions

**Defined in GLOSSARY.md:**
- Prefer "understanding" over "knowledge" when discussing comprehension
- Use "process" or "generate" instead of "understand" for AI
- Specify type when using "AI": LLM, ML model, etc.
- Hedge absolutes ("always", "never") appropriately

**Domain-specific terms:**
- See `GLOSSARY.md` for definitions of: epistemic debt, epistemic warrant, solutioning trap, construction vs. curation paradigm, epistemic boundary, circular validation

## Voice and Tone (Content)

**Style:**
- Exploratory, not prescriptive
- Thoughtful and nuanced
- Accessible but rigorous
- Honest about limitations

**Sentence Structure:**
- Lead with main point, then elaborate
- One idea per sentence when possible
- Use transitional phrases to connect ideas
- Vary sentence length for rhythm, but favor clarity

---

*Convention analysis: 2026-01-26*
