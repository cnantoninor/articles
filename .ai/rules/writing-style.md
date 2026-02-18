---
globs: topics/**/*.md
paths: topics/**/*.md
description: "Writing style, content structure, and AI assistant guidelines for articles"
alwaysApply: false
---

# Writing Style & Content Structure

## Writing Style Guidelines

### Tone
- **Exploratory, not prescriptive**: Present ideas as investigations, not mandates
- **Thoughtful and nuanced**: Acknowledge trade-offs and uncertainties
- **Accessible but rigorous**: Technical concepts explained for broad tech audience
- **Honest about limitations**: Clearly mark gaps, uncertainties, and open questions

### Audience Awareness
- Primary audience: Technical professionals interested in AI and software development
- Assume familiarity with programming concepts
- Define domain-specific or philosophical terms on first use
- Use concrete examples to ground abstract concepts

### Language Preferences
- Prefer "understanding" over "knowledge" when discussing comprehension
- Use active voice for clarity
- Avoid jargon without definition
- Keep sentences focused—one idea per sentence when possible
- Use parallel structure in lists

### Sentence Structure
- Lead with the main point, then elaborate
- Use transitional phrases to connect ideas
- Vary sentence length for rhythm, but favor clarity
- Break complex ideas into digestible pieces

---

## Content Structure Conventions

### Front-Matter Format (YAML)
All articles should include:
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

### Section Heading Hierarchy
- Use H1 (`#`) for article title only
- Use H2 (`##`) for major sections
- Use H3 (`###`) for subsections
- Avoid going deeper than H4

### Marking Gaps and TODOs
Use consistent markers for incomplete sections:
- `[GAP: description]` — Content that needs to be written
- `[TODO: task]` — Specific task to complete
- `[QUESTION: question]` — Open question to address
- `[EXAMPLE NEEDED]` — Place where a concrete example is required

### Citation Format
For inline references:
- Academic: Author (Year) or (Author, Year)
- Web/informal: linked text or footnote

For reference lists:
```markdown
- Author. "Title." *Publication*, Year. [URL]
```

---

## AI Assistant Guidelines

### When Helping with Writing
1. Maintain the exploratory, non-prescriptive tone
2. Check GLOSSARY.md for consistent terminology
3. Mark new gaps with `[GAP: ...]` rather than inventing content
4. Suggest concrete examples when abstract concepts need grounding
5. Preserve the author's voice while improving clarity

### When Creating New Content
1. Start from appropriate template in `templates/`
2. Fill in front-matter with accurate metadata
3. Follow section heading hierarchy
4. Use consistent citation format
5. Mark areas of uncertainty explicitly

### When Reviewing Content
1. Check for jargon that needs definition
2. Verify consistency with GLOSSARY.md terms
3. Identify claims that need examples or evidence
4. Suggest where to mark gaps or open questions
5. Ensure structure follows conventions

---

## File Organization

### Topic Directory Structure
All topics live under the `topics/` directory:
```
topics/
└── topic_name/
    ├── README.md            # Topic overview and status
    ├── article.md           # Main article draft
    ├── slides.md            # Presentation (Marp format)
    ├── raw_material/        # Working notes, brainstorms
    ├── references/          # Literature, citations
    ├── assets/              # Images, diagrams
    ├── artifacts/           # Polished outputs for distribution (flat; no drafts/published subdirs)
    │   ├── articles/        #   Article artifacts; version and status in frontmatter and git
    │   └── presentation/    #   Presentation artifacts; version and status in frontmatter and git
    └── exports/             # Generated outputs (DOCX, PPTX, PDF)
```

Note: A topic may contain multiple article or slide variants (e.g., `cursor-article.md`, `iris-learnings.md`) beyond the standard `article.md` and `slides.md`.

### Naming Conventions
- Use lowercase with underscores for topic directories: `topics/topic_name/`
- Use lowercase with hyphens for files: `file-name.md`
- Use descriptive names: `outline-v1.md` not `notes.md`
