# Codebase Concerns

**Analysis Date:** 2026-01-26

## Tech Debt

**Incomplete Article Content:**
- Issue: Multiple content gaps marked throughout primary article requiring substantial writing work
- Files: `/home/arau6/projects/ai-articles/epistemic_debt/article.md`
- Impact: Article cannot be published or presented without completing 9+ major gaps including opening hook, concrete examples, conclusion, and emotional landing
- Fix approach: Systematic gap filling working from outline, prioritizing concrete examples first (lines 21, 49, 63, 79, 89, 99, 139, 167, 173, 181)

**Missing References Integration:**
- Issue: Literature review completed but not integrated into article
- Files: `/home/arau6/projects/ai-articles/epistemic_debt/article.md` (line 187), `/home/arau6/projects/ai-articles/epistemic_debt/references/literature-review-on-epistemic-debt.md`
- Impact: Article lacks academic grounding and citation support, reducing credibility
- Fix approach: Add formal references section with citations from Ngabang (2026), Ionescu et al. (2020), and supporting blog posts

**Incomplete Slides Presentation:**
- Issue: Contact information and resources section not filled in
- Files: `/home/arau6/projects/ai-articles/epistemic_debt/slides.md` (line 191)
- Impact: Presentation cannot be delivered without speaker contact/resource information
- Fix approach: Add author contact details and links to resources (article URL, literature review, etc.)

**Empty Export Directories:**
- Issue: Export directories created but no generated artifacts present
- Files: `/home/arau6/projects/ai-articles/epistemic_debt/exports/`, `/home/arau6/projects/ai-articles/epistemic_debt/artifacts/articles/`, `/home/arau6/projects/ai-articles/epistemic_debt/artifacts/presentation/`
- Impact: No publishable formats exist; manual export required before sharing
- Fix approach: Run export scripts once content gaps are filled: `/home/arau6/projects/ai-articles/scripts/export-docx.sh`, `/home/arau6/projects/ai-articles/scripts/export-slides.sh`, `/home/arau6/projects/ai-articles/scripts/export-pdf.sh`

**Artifacts Directory Confusion:**
- Issue: Both `artifacts/` and `exports/` directories exist with similar purposes but different conventions
- Files: `/home/arau6/projects/ai-articles/epistemic_debt/artifacts/`, `/home/arau6/projects/ai-articles/epistemic_debt/exports/`
- Impact: Unclear which directory to use for generated outputs; README.md specifies `exports/` but `artifacts/` also exists
- Fix approach: Consolidate to single export location (per README.md convention use `exports/`), remove or repurpose `artifacts/`

## Known Bugs

**No bugs detected** - This is a content repository without executable code.

## Security Considerations

**No External Dependencies:**
- Risk: Repository relies on external tools (pandoc, marp-cli) not managed in project
- Files: `/home/arau6/projects/ai-articles/scripts/export-docx.sh`, `/home/arau6/projects/ai-articles/scripts/export-slides.sh`, `/home/arau6/projects/ai-articles/scripts/export-pdf.sh`
- Current mitigation: README.md documents prerequisites
- Recommendations: Add dependency version checking in export scripts to warn if tools are missing or outdated

**No Sensitive Data Controls:**
- Risk: Repository structure doesn't prevent accidental commit of sensitive data in raw_material/ directories
- Files: All directories under `/home/arau6/projects/ai-articles/*/raw_material/`
- Current mitigation: None detected
- Recommendations: Add `.gitignore` patterns for common sensitive file types (.env, credentials, API keys) and document raw_material/ security guidelines in README.md

## Performance Bottlenecks

**Not applicable** - Static content repository has no runtime performance concerns.

## Fragile Areas

**Gap Marker Convention Dependency:**
- Files: `/home/arau6/projects/ai-articles/epistemic_debt/article.md`, `/home/arau6/projects/ai-articles/.cursorrules` (lines 54-59)
- Why fragile: Entire workflow depends on consistent use of `[GAP:]`, `[TODO:]`, `[QUESTION:]`, `[EXAMPLE NEEDED]` markers; inconsistent usage breaks tracking
- Safe modification: Always use exact marker syntax from .cursorrules; search for markers before considering content "complete"
- Test coverage: No automated validation that markers are used correctly

**Front-Matter Schema Enforcement:**
- Files: All article/slides files, template defined in `/home/arau6/projects/ai-articles/.cursorrules` (lines 34-46)
- Why fragile: No validation that YAML front-matter matches expected schema (title, status, type, audience, target_length, created, last_updated)
- Safe modification: Always copy template structure; validate YAML syntax before committing
- Test coverage: None - could fail silently if export scripts expect specific fields

**Cross-Reference Integrity:**
- Files: `/home/arau6/projects/ai-articles/GLOSSARY.md`, all articles referencing terminology
- Why fragile: No automated checking that article terminology matches GLOSSARY.md definitions
- Safe modification: Always verify GLOSSARY.md when introducing new domain terms; update both locations
- Test coverage: Manual review only

**Script Path Assumptions:**
- Files: `/home/arau6/projects/ai-articles/scripts/export-docx.sh` (lines 16-18), similar in other export scripts
- Why fragile: Export scripts use relative path navigation assuming specific directory structure
- Safe modification: Run scripts from repository root only; don't rename topic directories while exports are running
- Test coverage: None - scripts fail with unclear errors if directory structure changes

## Scaling Limits

**Single Topic Limitation:**
- Current capacity: 1 topic (epistemic_debt)
- Limit: README.md describes multi-topic structure, but no automation for creating new topics
- Scaling path: Create topic scaffolding script to automate directory creation, template copying, and README.md updates

**No Content Organization for Large Articles:**
- Current capacity: Single-file articles work for 4000-word target
- Limit: Articles exceeding ~10,000 words become unwieldy in single file; no chunking strategy
- Scaling path: Add section-per-file convention with assembly script for long-form content

**Export Script Serial Processing:**
- Current capacity: `export-all.sh` runs exports sequentially
- Limit: Slow for multiple large topics
- Scaling path: Parallelize exports in `/home/arau6/projects/ai-articles/scripts/export-all.sh`

## Dependencies at Risk

**pandoc:**
- Risk: External tool, version compatibility unknown
- Impact: DOCX/PDF exports break if pandoc syntax changes
- Migration plan: Document tested pandoc version; consider containerized export environment

**marp-cli:**
- Risk: External NPM package, global install required
- Impact: Slide exports fail without global npm install; potential version drift
- Migration plan: Add package.json to lock marp-cli version; use npx for version-specific execution

## Missing Critical Features

**No Version Control Integration:**
- Problem: Repository described as not a git repo (per environment info)
- Blocks: Collaboration, change tracking, backup, CI/CD for exports
- Priority: High - git init recommended immediately

**No Draft/Review Workflow Enforcement:**
- Problem: Front-matter has `status` field (draft/review/published) but no validation or workflow automation
- Blocks: Quality control, publication pipeline, preventing accidental publication of drafts
- Priority: Medium - add pre-commit hook or CI check for status field validation

**No Automated Gap Detection:**
- Problem: Content gaps tracked manually with markers; no automated reporting
- Blocks: Knowing completion status without manual file inspection
- Priority: Medium - script to extract and report all `[GAP:]`, `[TODO:]`, `[QUESTION:]`, `[EXAMPLE NEEDED]` markers across codebase

**No Template Validation:**
- Problem: Templates exist but no enforcement that new content follows template structure
- Blocks: Consistency across topics as repository scales
- Priority: Low - add linting script to validate article structure matches conventions

## Test Coverage Gaps

**Export Script Functionality:**
- What's not tested: Scripts in `/home/arau6/projects/ai-articles/scripts/` have no automated tests
- Files: `/home/arau6/projects/ai-articles/scripts/export-docx.sh`, `/home/arau6/projects/ai-articles/scripts/export-slides.sh`, `/home/arau6/projects/ai-articles/scripts/export-pdf.sh`, `/home/arau6/projects/ai-articles/scripts/export-all.sh`
- Risk: Export failures discovered only when running scripts; invalid exports could be created silently
- Priority: Medium

**Markdown Syntax Validity:**
- What's not tested: No validation that markdown files are syntactically valid or will render correctly
- Files: All `.md` files under `/home/arau6/projects/ai-articles/`
- Risk: Broken links, malformed tables, invalid YAML front-matter discovered during export or presentation
- Priority: Medium

**Glossary-Article Terminology Sync:**
- What's not tested: No validation that terms used in articles match GLOSSARY.md definitions
- Files: `/home/arau6/projects/ai-articles/GLOSSARY.md`, `/home/arau6/projects/ai-articles/epistemic_debt/article.md`
- Risk: Inconsistent terminology across repository; confusion for readers and AI assistants
- Priority: Low

**Convention Compliance:**
- What's not tested: No automated checking that files follow .cursorrules conventions (heading hierarchy, gap markers, citation format, naming patterns)
- Files: All content files, conventions defined in `/home/arau6/projects/ai-articles/.cursorrules`
- Risk: Content drift from established conventions as repository grows
- Priority: Low

---

*Concerns audit: 2026-01-26*
