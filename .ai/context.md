# AI Articles Repository

## Project
- Structured repo for AI-related articles, presentations, and research
- Publication: The AI Mirror (https://antoninorau.substack.com/)
- **Audience, terminology, language, and tone are topic-dependent** -- the values below are the *default*, but each topic may override them via a rule in `.ai/rules/` (activated by file path). Always check for a topic-specific rule before assuming the default applies.
- Default audience: Technical professionals interested in AI and software development (assumes familiarity with programming concepts)
- Example override: `topics/divulgative/` targets a general, non-technical readership in Italian -- see `.ai/rules/divulgative-articles.md`

## Repository Layout
- topics/<name>/   -- all content (articles, slides, references, exports)
- templates/       -- starting templates for new content
- scripts/         -- export scripts (pandoc, marp)
- .ai/             -- centralized AI context (this file + rules/)
- .ai/rules/       -- detailed rules activated by file path
- GLOSSARY.md      -- shared terminology

## Core Rules

### Writing
- Exploratory, not prescriptive -- present ideas as investigations
- Define domain-specific terms on first use
- Mark uncertainties: [GAP:], [TODO:], [QUESTION:], [EXAMPLE NEEDED]
- Never invent content -- mark gaps instead
- Preserve the author's voice

### Glossary
- Only add novel, niche, or author-introduced terms
- Skip common industry terms
- Each term needs a one-line definition

### Publication
- Primary: Substack (The AI Mirror) -- weekly cadence
- Promotion: LinkedIn, Twitter/X, Instagram, Substack Notes
- MCP servers for drafting and cross-posting are documented (Phase 2); see docs/mcp-setup.md and docs/publishing-workflow.md
- Teasers must match the exploratory writing tone
- **Fact-check required before publication** -- every article needs a completed fact-check report (see .ai/rules/fact-checking.md); in GSD phases, this is always Plan 00

### Content
- YAML front-matter required (see templates/article.md) -- includes title, subtitle, status, type, audience, estimated_reading_time, dates
- H1 title only, H2 sections, H3 subsections, no deeper than H4
- Start new content from templates/
- Check GLOSSARY.md for consistent terminology

### File Organization
- Topic dirs: lowercase with underscores (topics/topic_name/)
- Files: lowercase with hyphens (file-name.md)
- Descriptive names (outline-v1.md not notes.md)

## Export
./scripts/export-all.sh <topic_name>

## Current Topics
- epistemic_debt -- Epistemic risks of LLM-based software engineering
- philosophy_of_ai -- Metaphors, epistemology, and cognitive limits (TAM1, TAM2)
- ai_craft -- Development practice, design, and identity (TAM3, TAM4, TAM5)
- divulgative -- General-audience essays on AI and culture, in Italian (non-technical readership; see .ai/rules/divulgative-articles.md)
