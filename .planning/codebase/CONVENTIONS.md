# Coding Conventions

**Analysis Date:** 2026-02-15

## Writing Conventions (Primary Codebase Output)

This is primarily a content authoring repository, not a software project. "Coding conventions" map to writing conventions, template adherence, and script consistency.

### Front-Matter Format

**Convention (from `CLAUDE.md`):**
All articles must include YAML front-matter with these fields:
```yaml
---
title: "Article Title"
subtitle: "A short tagline or secondary description"
status: draft | review | published
type: article | slides | research
audience: [list of target readers]
target_length: word count target
estimated_reading_time: "X min"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

**Adherence in existing content:**

| File | title | subtitle | status | type | audience | target_length | created | last_updated | Verdict |
|------|-------|----------|--------|------|----------|---------------|---------|--------------|---------|
| `topics/epistemic_debt/article.md` | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Missing subtitle** |
| `topics/epistemic_debt/cursor-article.md` | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Missing subtitle** |
| `topics/epistemic_debt/slides.md` | ✓ (Marp) | — | — | — | — | — | — | — | **Marp format (expected)** |
| `topics/epistemic_debt/iris-learnings.md` | ✓ (Marp) | — | — | — | — | — | — | — | **Marp format (expected)** |
| `topics/epistemic_debt/README.md` | — | — | — | — | — | — | — | — | — | **No front-matter (acceptable for README)** |

**Assessment:** Article files follow front-matter convention well. Marp slides use Marp-specific front-matter (marp: true, theme, paginate, title) which is correct for their format. README uses plain markdown headings per the research template.

### Template Adherence

**Article template** (`templates/article.md`):
- Requires: Abstract, Introduction, Section headings, Conclusion, References
- `topics/epistemic_debt/article.md`: **Mostly compliant** — Uses Roman numeral sections (I-VII) instead of descriptive section titles. Has Abstract, Introduction-equivalent (Section I), and Conclusion (Section VII). Uses `---` horizontal rules between sections as template suggests.
- `topics/epistemic_debt/cursor-article.md`: **Mostly compliant** — Same structure, slightly different section naming.

**Research template** (`templates/research.md`):
- Requires: Overview (with Status, Created, Last Updated), Key Questions, Source Tracking table, Key Quotes, Working Notes, Gaps, Connections, Next Steps
- `topics/epistemic_debt/README.md`: **Partially compliant** — Has Overview with Status/Created/Last Updated, Key Questions, Central Concepts (custom section), Files in This Topic (custom section), Current Gaps, Next Steps. Missing: Source Tracking table, Key Quotes, Working Notes, Connections to Other Topics.

**Slides template** (`templates/slides.md`):
- Requires: Marp front-matter, title slide, agenda, content slides with speaker notes, Q&A
- `topics/epistemic_debt/slides.md`: **Compliant** — Has Marp front-matter, title slide, content slides with speaker notes, Q&A. Missing: explicit Agenda slide.
- `topics/epistemic_debt/iris-learnings.md`: **Compliant** — Full Marp presentation with speaker notes throughout.

### Section Heading Hierarchy

**Convention:**
- H1 (`#`) for article title only
- H2 (`##`) for major sections
- H3 (`###`) for subsections
- Avoid deeper than H4

**Assessment:**
- `article.md`: **Compliant** — H1 for title, H2 for major sections (I-VII), H3 for subsections, H4 for specific examples. One H4 level used (`#### The Database Deletion`) — acceptable.
- `cursor-article.md`: **Compliant** — Same pattern.
- Slides: N/A (Marp uses headings differently for slide separation).

### Gap/TODO Marking

**Convention:**
- `[GAP: description]` — Content to write
- `[TODO: task]` — Task to complete
- `[QUESTION: question]` — Open question
- `[EXAMPLE NEEDED]` — Needs concrete example

**Assessment:**
- Only one remaining `[GAP:]` marker found in active content: `slides.md` line 271: `[GAP: Add contact information and resources]`
- The outline file (`raw_material/outline-v1-epistemic-debt.md`) uses `🔴 GAP:` markers extensively — deviates from convention but is in raw material, so acceptable.
- Both article versions have filled in all major gaps identified in the outline.

### Citation Format

**Convention:**
- Inline: Author (Year) or footnotes
- Reference list: `Author. "Title." *Publication*, Year. [URL]`

**Assessment:**
- `article.md`: **Compliant** — Uses markdown footnotes (`[^1]`, `[^2]`, etc.) with full citations. Reference list at end follows convention. Strong citation practice with URLs included.
- `cursor-article.md`: **Compliant** — Same footnote pattern, slightly different reference formatting in the endnotes (numbered list instead of bullet list), but consistent internally.
- `slides.md`: Minimal citations (appropriate for slides format).
- `iris-learnings.md`: Has References slide with proper formatting.

### Naming Conventions

**Convention:**
- Topic directories: lowercase with underscores (`topics/topic_name/`)
- Files: lowercase with hyphens (`file-name.md`)
- Descriptive names: `outline-v1.md` not `notes.md`

**Assessment:**
- `topics/epistemic_debt/`: **Compliant** — lowercase with underscores.
- File names: **Mostly compliant** — `article.md`, `slides.md`, `cursor-article.md`, `iris-learnings.md`, `outline-v1-epistemic-debt.md` all use lowercase with hyphens.
- Exception: `references/Epistemic_debt_definition.md` — Uses uppercase first letter and underscores instead of hyphens. Should be `epistemic-debt-definition.md`.
- Exception: `references/Epistemic Debt Research Complete.pdf` — Contains spaces and uppercase. Should be `epistemic-debt-research-complete.pdf`.
- Exception: `references/Triangle Interaction Table.pdf` — Contains spaces and uppercase. Should be `triangle-interaction-table.pdf`.

## Script Conventions

### Shell Script Pattern

All export scripts follow a consistent pattern:
1. `#!/bin/bash` shebang
2. Comment block with description and usage
3. `set -e` for error-on-failure
4. Argument validation with usage message
5. `SCRIPT_DIR` / `REPO_ROOT` / `TOPIC_DIR` derivation
6. Topic directory existence check
7. `mkdir -p` for exports directory
8. Timestamp generation
9. Export operation
10. Timestamped + latest copy output

**Assessment:** Highly consistent across all four scripts (`export-docx.sh`, `export-slides.sh`, `export-pdf.sh`, `export-all.sh`). Good practice.

### Script Error Handling

- All scripts use `set -e`
- Input validation present (check for arguments, check directory exists, check file exists)
- `export-pdf.sh` uses `|| true` for "both" mode to continue even if one export fails
- `export-all.sh` tracks whether anything was exported

**Gaps:**
- No tool availability checks (scripts don't verify `pandoc`, `marp` are installed before attempting to use them)
- No shellcheck compliance verification
- `setup.sh` uses `set -e` but some installation sections could fail silently on unsupported platforms (e.g., Linux without apt/dnf/pacman for Node.js installation)

## Publishing Conventions

### Publication Workflow
- **Primary platform**: Substack (The AI Mirror) — weekly cadence
- **Distribution**: LinkedIn (professional framing), Twitter/X (hook+insight), Instagram (visual+caption), Substack Notes (organic discovery)
- **Teaser tone**: Must match the exploratory writing style — no clickbait, no prescriptive claims
- **Workflow**: Publish on Substack → create platform-specific teasers → cross-post to social channels
- **Rules file**: `.ai/rules/publication.md` (glob-activated on `topics/**/artifacts/**`)

### Article Front-Matter (Publication Fields)
New articles should include `subtitle` (used as Substack subtitle and social teaser hook), `estimated_reading_time`, and publication fields in YAML front-matter:
```yaml
subtitle: "A short tagline or secondary description"
estimated_reading_time: "X min"
published_date:
publication_url: ""
social_teasers:
  linkedin: ""
  twitter: ""
  instagram_caption: ""
  substack_notes: ""
```

**Assessment:** Template updated. Existing articles not retroactively updated (acceptable for pre-publication content).

---

## Glossary Consistency

### GLOSSARY.md Coverage

**Terms defined in GLOSSARY.md:**
1. Epistemic (general)
2. Epistemic Warrant
3. Epistemic Opacity
4. Epistemic Debt
5. Solutioning Trap
6. Construction Paradigm
7. Curation Paradigm
8. Epistemic Boundary
9. Circular Validation
10. Velocity Trap
11. Domain-Driven Design (DDD)
12. Ubiquitous Language
13. E2E Integration Testing

**Terms used prominently in articles but MISSING from GLOSSARY.md:**
1. **Epistemic Credit** — Used in `article.md`, `cursor-article.md`, `iris-learnings.md`, and `references/Epistemic_debt_definition.md`. Has a formal mathematical definition. Should be in glossary.
2. **Automation Bias** — Used extensively in both article versions. A well-documented cognitive bias concept.
3. **Stochastic Spaghetti Effect** — Coined by Ngabang (2026), used in `article.md`. A specific concept worth defining.
4. **Context Window Amnesia** — From Ngabang (2026), used in `cursor-article.md` and `iris-learnings.md`.
5. **Vibe Coding** — Coined by Karpathy (2025), central concept in both articles.
6. **Spec-Driven Development** — From Thoughtworks (2025), used in `cursor-article.md`.
7. **Epistemia** — From Quattrociocchi et al. (2025), used in `article.md`.
8. **Rubber-Stamp Culture** — Used in both article versions.
9. **Trade-off Triangle** — The central framework of the article. Deserves a glossary entry.
10. **Bus Factor** — Used in measurement discussions. Common term but worth defining in context.

**Assessment:** GLOSSARY.md covers foundational terms well but has not been updated to reflect the many concepts introduced during article development. Approximately 10 significant terms used in published content are missing.

## Tone and Style Compliance

### CLAUDE.md Tone Requirements

| Requirement | article.md | cursor-article.md |
|-------------|-----------|-------------------|
| Exploratory, not prescriptive | ✓ Explicitly frames guardrails as "practices worth examining" | ✓ Same framing |
| Thoughtful and nuanced | ✓ Acknowledges trade-offs, counter-arguments | ✓ Same pattern |
| Accessible but rigorous | ✓ Defines terms, uses concrete examples | ✓ Same approach |
| Honest about limitations | ✓ Section VI explicitly about measurement uncertainty | ✓ Same section |
| Define terms on first use | ✓ Most terms defined; "epistemic" defined in opening | ✓ Same |
| Concrete examples | ✓ Multiple scenarios (database deletion, 10:1 ratio, healthcare) | ✓ Same examples + additional ones |
| Prefer "understanding" over "knowledge" | ✓ Consistently uses "understanding" | ✓ Same |
| Active voice | ✓ Predominantly active | ✓ Same |

**Assessment:** Both article versions demonstrate excellent adherence to the tone and style guidelines in `CLAUDE.md`. The articles practice what they preach — they're exploratory, acknowledge uncertainty, and provide concrete examples.

---

*Convention analysis: 2026-02-15*
