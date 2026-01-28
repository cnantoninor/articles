# Testing Patterns

**Analysis Date:** 2026-01-26

## Test Framework

**Runner:**
- Not applicable - This is a content repository, not a software project

**Assertion Library:**
- Not applicable

**Run Commands:**
Not applicable - No automated tests detected

## Test File Organization

**Location:**
- No test files found

**Naming:**
- No test naming conventions (no tests present)

**Structure:**
Not applicable

## Content Validation Strategy

This repository does not contain traditional software tests. Instead, validation occurs through:

**Manual review workflows:**
- Draft → Review → Published status progression (tracked in YAML front-matter)
- Gap markers (`[GAP: ...]`, `[TODO: ...]`) indicate incomplete sections
- Audience field in front-matter defines target reviewers

**Export validation:**
- Scripts use `set -e` to fail fast on export errors
- File existence checks before export attempts
- Both timestamped and "latest" versions created for comparison

## Export Scripts as "Tests"

The export scripts in `scripts/` serve as a form of integration testing for content:

**Export validation pattern:**
```bash
# Validate inputs
if [ ! -d "$TOPIC_DIR" ]; then
    echo "Error: Topic directory '$TOPIC_DIR' does not exist"
    exit 1
fi

if [ ! -f "$TOPIC_DIR/article.md" ]; then
    echo "Error: No article.md found in '$TOPIC_DIR'"
    exit 1
fi

# Execute export
pandoc "$TOPIC_DIR/article.md" -o "$OUTPUT_FILE" ...

# Confirm success
echo "Created: $OUTPUT_FILE"
```

**What these "tests" verify:**
- Content exists (`article.md`, `slides.md`)
- Directory structure is valid
- Markdown can be parsed by pandoc/marp
- YAML front-matter is well-formed (implicitly, via successful export)

## Quality Assurance Patterns

**Content quality checks:**
1. YAML front-matter completeness (all required fields present)
2. Gap markers track incomplete sections explicitly
3. GLOSSARY.md ensures terminology consistency
4. Templates provide starting structure to prevent format drift

**Script quality checks:**
1. Input validation before execution
2. Path existence verification
3. Clear error messages with examples
4. Exit on first error (`set -e`)

## Fixture Patterns

**Templates serve as fixtures:**
- `templates/article.md` - Standard article structure
- `templates/slides.md` - Standard presentation structure
- `templates/research.md` - Research notes structure

**Example "fixture" from `templates/article.md`:**
```yaml
---
title: ""
status: draft
type: article
audience: []
target_length: 0
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

## Coverage

**Requirements:** Not applicable (no code coverage)

**Content coverage approach:**
- Gap markers (`[GAP: ...]`) explicitly mark missing content
- Status field tracks completion: `draft`, `review`, `published`
- Front-matter `target_length` provides completeness metric

**Current coverage assessment (epistemic_debt topic):**
- `article.md`: 187 lines, status: draft, contains 11 gap markers
- `slides.md`: 195 lines, contains 1 gap marker
- References: 34 lines (literature review outline)

## Dependency Testing

**External tools required:**
- `pandoc` - For Markdown → DOCX/PDF conversion
- `marp-cli` - For Markdown → PPTX/PDF slides
- `pdflatex` - PDF rendering backend for pandoc

**Validation approach:**
- README.md documents prerequisites
- Scripts fail with clear errors if tools missing
- No automated dependency checks

## Content Integration Testing

**Export workflow serves as integration test:**
```bash
./scripts/export-all.sh epistemic_debt
```

**What this tests:**
1. All required files exist
2. Markdown is well-formed
3. YAML front-matter is valid
4. Pandoc can parse content
5. Marp can render slides
6. Output directory is writable

**Test output:**
- Timestamped files in `exports/`: `article-20260126.docx`, `slides-20260126.pdf`
- "Latest" versions: `article.docx`, `slides.pdf`

## Manual Testing Pattern

**Human review checklist (implicit in content workflow):**
1. Check YAML front-matter completeness
2. Verify terminology against GLOSSARY.md
3. Ensure heading hierarchy (H1 for title only, H2 for sections)
4. Validate citation format
5. Test export scripts produce readable outputs
6. Review gap markers for completeness tracking

## Continuous Integration

**CI Pipeline:** Not detected (no GitHub Actions, no `.gitlab-ci.yml`, etc.)

**Current workflow:**
- Local development and editing
- Manual export script execution
- Manual review of generated outputs

## Test Data

**Sample content:**
- `epistemic_debt/` topic serves as working example
- Templates provide minimal valid structure
- No synthetic test data fixtures

## Error Testing Patterns

**Scripts test error conditions:**
```bash
# Missing argument
if [ -z "$1" ]; then
    echo "Usage: $0 <topic-directory>"
    exit 1
fi

# Invalid directory
if [ ! -d "$TOPIC_DIR" ]; then
    echo "Error: Topic directory '$TOPIC_DIR' does not exist"
    exit 1
fi

# Missing file (with graceful degradation)
if [ ! -f "$TOPIC_DIR/slides.md" ]; then
    echo "Warning: No slides.md found in '$TOPIC_DIR', skipping slides PDF"
    return 1
fi
```

**Failure modes tested:**
- Missing required arguments
- Non-existent directories
- Missing input files
- Export tool failures (via `set -e`)

## Testing Anti-Patterns Avoided

**No automated tests, but content validation principles:**
- Gap markers prevent silent incompleteness
- Templates prevent format drift
- Export scripts catch structural errors early
- GLOSSARY.md prevents terminology inconsistency
- Front-matter status tracking prevents premature publishing

## Quality Metrics

**Measurable quality indicators:**
- Number of gap markers (lower is better)
- Status field progression (draft → review → published)
- Target length vs. actual length (from front-matter)
- Export script success/failure
- Consistency with GLOSSARY.md terms

**Current metrics (epistemic_debt topic):**
- Gap markers: 11 in article.md, 1 in slides.md
- Status: draft
- Target: 4000 words
- Actual: ~187 lines in article (estimated 2000-2500 words)
- Export: Not yet tested in this analysis

---

*Testing analysis: 2026-01-26*
