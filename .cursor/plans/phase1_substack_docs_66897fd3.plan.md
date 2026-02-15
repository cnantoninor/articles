---
name: Phase1 Substack Docs
overview: "Execute Phase 1 of the Substack Publication Workflow: commit baseline, create centralized `.ai/` directory with concise rulebook and modular glob-activated rules, sync script for dual symlinks into both `.cursor/rules/` and `.claude/rules/`, update remaining docs (README, GLOSSARY, templates, .gitignore), run gsd-codebase-mapper, and validate rule activation across both tools."
todos:
  - id: commit-baseline
    content: Commit current uncommitted changes as a clean baseline
    status: pending
  - id: create-ai-structure
    content: Create .ai/ directory, write context.md (concise rulebook), and rules/ subdirectory with writing-style.md, publication.md, terminology.md
    status: pending
  - id: create-sync-script
    content: Write .ai/sync-rules.sh to create/update/verify all symlinks (root + .cursor/rules/ + .claude/rules/)
    status: pending
  - id: run-sync-script
    content: Run sync-rules.sh, verify all symlinks resolve correctly
    status: pending
  - id: update-readme
    content: Add Publication section, .ai/ references, and symlink notes to README.md
    status: pending
  - id: run-gsd-mapper
    content: Run gsd-codebase-mapper, review and adjust .planning/codebase/ files for distribution-layer content
    status: pending
  - id: update-glossary
    content: Add novel/niche distribution terms to GLOSSARY.md
    status: pending
  - id: update-article-template
    content: Add publication front-matter fields to templates/article.md
    status: pending
  - id: update-gitignore
    content: Add .mcp.json, .env, analytics/credentials/ to .gitignore
    status: pending
  - id: validate-rules
    content: Test rule activation in both Cursor and Claude Code, iterate frontmatter format based on findings
    status: pending
isProject: false
---

# Phase 1: Documentation Updates (Substack Publication Workflow)

## Reference

- **Source plan**: `.cursor/plans/substack_publication_workflow_a205b421.plan.md`
- **Scope**: Phase 1 only (documentation restructure + updates)

## Publication Metadata

- **Platform**: Substack | **Name**: The AI Mirror | **URL**: [https://antoninorau.substack.com/](https://antoninorau.substack.com/)
- **Tagline**: AI, philosophy, and spirituality
- **LinkedIn**: [https://www.linkedin.com/in/antoninorau/](https://www.linkedin.com/in/antoninorau/)
- **Twitter/X**: [https://x.com/antoninorau](https://x.com/antoninorau)
- **Instagram**: [https://www.instagram.com/eckardius_/](https://www.instagram.com/eckardius_/)
- **Subscribers**: 26-50 (goal: 100) | **Cadence**: Weekly

---

## Architecture

```
.ai/
├── context.md              # Concise rulebook (always-applied via root symlinks)
├── rules/                  # Source-of-truth glob-activated rules
│   ├── writing-style.md
│   ├── publication.md      # NEW
│   └── terminology.md
└── sync-rules.sh           # Creates/updates all symlinks automatically

# Root symlinks -> .ai/context.md (always-applied)
.cursorrules -> .ai/context.md       # Cursor reads (deprecated but functional)
CLAUDE.md -> .ai/context.md          # Claude Code reads (always loaded)

# Tool-specific symlinks (created by sync-rules.sh)
.cursor/rules/                       # Cursor activation (.mdc extension)
├── writing-style.mdc -> ../../.ai/rules/writing-style.md
├── publication.mdc -> ../../.ai/rules/publication.md
└── terminology.mdc -> ../../.ai/rules/terminology.md

.claude/rules/                       # Claude Code activation (.md extension)
├── writing-style.md -> ../../.ai/rules/writing-style.md
├── publication.md -> ../../.ai/rules/publication.md
└── terminology.md -> ../../.ai/rules/terminology.md
```

### Frontmatter Format (hedges both tools)

```yaml
---
globs: topics/**/*.md
paths: topics/**/*.md
description: "Rule description"
alwaysApply: false
---
```

Both `globs` and `paths` included. Cursor uses `globs` + `description` + `alwaysApply`. Claude Code documents `paths` (buggy) but `globs` works as fallback. Including both maximizes compatibility. Validated in Step 8.

---

## Step 0: Commit Current State

Commit all uncommitted changes (topics/ migration, modified docs) as a clean baseline before Phase 1.

---

## Step 1: Create `.ai/` Directory and Write Files

### 1a. `.ai/context.md` -- Concise Rulebook (~50-60 lines)

Always-applied via root symlinks. **Rules only, no detailed content.** Content goes in `.ai/rules/` or respective files.

Proposed structure:

```markdown
# AI Articles Repository

## Project
- Structured repo for AI-related articles, presentations, and research
- Publication: The AI Mirror (https://antoninorau.substack.com/)
- Audience: Technical professionals interested in AI and software development

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
- MCP servers for drafting and cross-posting are planned (Phase 2)
- Teasers must match the exploratory writing tone

### Content
- YAML front-matter required (see templates/article.md)
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
```

### 1b. `.ai/rules/writing-style.md`

Source: current `.cursorrules` sections 1-4 (lines 1-119), cleaned up.

```yaml
---
globs: topics/**/*.md
paths: topics/**/*.md
description: "Writing style, content structure, and AI assistant guidelines for articles"
alwaysApply: false
---
```

Contains: Full writing style (tone, audience, language, sentences), content structure (front-matter, headings, gap markers, citations), AI assistant guidelines (writing help, new content, reviewing). Remove the incomplete "Target publication" stub at lines 48-50.

### 1c. `.ai/rules/publication.md` (NEW)

```yaml
---
globs: topics/**/artifacts/**
paths: topics/**/artifacts/**
description: "Publication workflow, social media distribution, and teaser conventions"
alwaysApply: false
---
```

Contains: Substack details (URL, name, tagline), social media channels with URLs, platform-specific teaser conventions (LinkedIn professional framing, Twitter hook+insight, Instagram visual+caption, Substack Notes), distribution workflow overview, planned MCP servers marked as Phase 2.

### 1d. `.ai/rules/terminology.md`

Source: current `.cursorrules` section 3 (lines 77-94).

```yaml
---
globs: topics/**/*.md
paths: topics/**/*.md
description: "Domain terminology, key concepts, and terms to avoid or clarify"
alwaysApply: false
---
```

Contains: Reference to GLOSSARY.md, key concepts per topic (epistemic debt terms), terms to avoid or clarify.

---

## Step 2: Create Sync Script and Symlinks

### `.ai/sync-rules.sh`

Bash script that:

1. Creates `.cursor/rules/` and `.claude/rules/` directories if missing
2. For each `.md` file in `.ai/rules/`:
  - Creates symlink in `.cursor/rules/` with `.mdc` extension
  - Creates symlink in `.claude/rules/` with `.md` extension
3. Creates root symlinks: `.cursorrules -> .ai/context.md`, `CLAUDE.md -> .ai/context.md`
4. Removes stale symlinks for rules that no longer exist in `.ai/rules/`
5. Verifies all symlinks resolve correctly
6. Prints summary of created/updated/removed symlinks

Run: `bash .ai/sync-rules.sh`

---

## Step 3: Update [README.md](README.md)

- Add **Publication** section (after "Export Workflow"): The AI Mirror on Substack, social channels with URLs, brief workflow
- Update **Repository Structure** to show `.ai/` directory
- Note about `.ai/sync-rules.sh` for setting up rule symlinks
- Note about symlink compatibility (Linux/WSL2 native; Windows may need developer mode)

---

## Step 4: Run gsd-codebase-mapper + Review

Run mapper to regenerate `.planning/codebase/` files. Review and manually add:

- **ARCHITECTURE.md**: Distribution Layer above Export Layer
- **INTEGRATIONS.md**: Planned MCP integrations
- **STACK.md**: MCP servers and social tools
- **STRUCTURE.md**: `.ai/` directory, `.claude/rules/`, planned `docs/` and `analytics/`
- **CONVENTIONS.md**: Publishing conventions
- **CONCERNS.md**: Token security, API fragility, analytics limitations

---

## Step 5: Update [GLOSSARY.md](GLOSSARY.md)

Add only novel/niche/author-introduced terms:

- **Cross-posting**: Publishing/promoting content across platforms with platform-specific adaptations
- **Social teaser**: Short, platform-adapted excerpt to drive traffic to the primary publication
- **Substack Notes**: Substack's native short-form posting for organic discovery
- **Distribution layer**: Workflow stage between content export and audience reach

---

## Step 6: Update [templates/article.md](templates/article.md)

Add publication fields to YAML front-matter:

```yaml
published_date:
publication_url: ""
social_teasers:
  linkedin: ""
  twitter: ""
  instagram_caption: ""
  substack_notes: ""
```

Existing articles NOT retroactively updated.

---

## Step 7: Update [.gitignore](.gitignore)

Add:

```
.mcp.json
.env
analytics/credentials/
```

---

## Step 8: Validate Rule Activation

Heuristic validation across both tools:

### 8a. Cursor Validation

1. Open a file matching `topics/**/*.md` -- check if writing-style and terminology rules appear in AI context
2. Open a file matching `topics/**/artifacts/**` -- check if publication rule appears
3. Open a non-matching file (e.g., `scripts/`) -- check rules do NOT appear
4. If glob activation fails: try `alwaysApply: true` as fallback, note which rules needed it

### 8b. Claude Code Validation

1. Start a Claude Code session, ask it to list loaded rules
2. Work on a file in `topics/` -- check if relevant rules are loaded
3. If `paths` works: note it. If only `globs` works: remove `paths` from frontmatter to reduce noise
4. If neither scoping works (all rules load globally): note it as acceptable (small rule set)

### 8c. Iterate

- Based on findings, update frontmatter format across all `.ai/rules/` files
- Re-run `sync-rules.sh` to propagate changes
- Document working configuration in `.ai/context.md` for future reference

---

## Assumptions

1. Symlinks work transparently on WSL2 for both Cursor and Claude Code
2. `.cursor/rules/*.mdc` can be symlinks
3. `.claude/rules/*.md` can be symlinks
4. Cursor frontmatter (`description`, `alwaysApply`) is harmless for Claude Code
5. Including both `globs` and `paths` in frontmatter causes no conflicts
6. gsd-codebase-mapper output is reviewable and adjustable
7. Glossary: only novel/niche/author-introduced terms

## Risks

- **Symlink compatibility**: Linux/WSL2 fine. Windows clones may need developer mode. Document in README.
- **Cursor .mdc symlinks**: May or may not resolve. Fallback: sync script copies instead of symlinks.
- **Glob activation bugs**: Cursor 2.0 may not auto-load glob rules. Claude Code may load all rules globally. Validated in Step 8.
- **Frontmatter compatibility**: Unknown if both tools gracefully ignore each other's fields. Validated in Step 8.

