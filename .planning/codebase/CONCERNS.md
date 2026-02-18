# Codebase Concerns

**Analysis Date:** 2026-02-15 | **Refreshed:** 2026-02-18

## 1. Directory Restructure Inconsistencies

### 1.1 Git Status Shows Deleted Files from Old Location

*(Historical; no content — was about pre-restructure state.)*

### 1.3 Modified Scripts Not Committed

- **Issue:** `scripts/export-all.sh`, `scripts/export-docx.sh`, `scripts/export-pdf.sh`, `scripts/export-slides.sh` are all modified but not committed. These were likely updated to reflect the new `topics/` path prefix.
- **Impact:** Scripts in git HEAD may reference old paths, making them non-functional if someone checks out a clean copy.
- **Fix approach:** Include in the restructure commit.

### 1.4 Modified `CLAUDE.md` and `README.md` Not Committed

- **Issue:** Both root files are modified, likely updated for the `topics/` restructure.
- **Impact:** Documentation and AI context reference old paths in the committed version.
- **Fix approach:** Include in the restructure commit.

---

## 2. Incomplete .gitignore

### 2.1 Generated Exports Not Gitignored

- **Issue:** `.gitignore` contains only `node_modules` and `.planning/phases`. The `topics/*/exports/` directories contain generated binary files (PDFs: 292KB–5.2MB, PPTX: 65KB–5.2MB, HTML, CSS) that should not be version-controlled.
- **Files affected:**
  - `topics/epistemic_debt/exports/claude-article-cc.pdf` (393 KB)
  - `topics/epistemic_debt/exports/claude-article.pdf` (292 KB)
  - `topics/epistemic_debt/exports/cursor-article-cc.pdf` (431 KB)
  - `topics/epistemic_debt/exports/cursor-article.pdf` (328 KB)
  - `topics/epistemic_debt/exports/iris-learnings.pptx` (5.2 MB)
  - `topics/epistemic_debt/exports/iris-learnings-editable.pptx` (65 KB)
  - `topics/epistemic_debt/exports/iris-learnings.html` (169 KB)
- **Impact:** Repository bloat. Binary files inflate git history. Each export regeneration creates a new large blob.
- **Status:** Resolved — `.gitignore` now includes `topics/*/exports/*.pdf`, `*.pptx`, `*.docx`, `*.html`; CSS and JS in exports/ remain tracked.

### 2.2 tmp/ Directory Not Gitignored

- **Issue:** `tmp/` directory at repository root contains 6 PNG files (259KB–585KB) and a DOCX file. These appear to be working/scratch files (triangle diagram iterations).
- **Impact:** ~2.3MB of temporary binary files that will bloat git history if committed. Names with spaces (`01 simple triangle.png`) also suggest these are informal working assets, not final content.
- **Status:** Resolved — `tmp/` added to `.gitignore`.

### 2.3 node_modules/ Present but Minimal

- **Issue:** `node_modules/` exists and is correctly gitignored. Contains markdown-it and footnote plugin for the custom `export-pdf.js` script. No `package.json` or `package-lock.json` in the repository root to track these dependencies.
- **Impact:** Dependencies are installed but not declared. Running `npm install` would fail because there's no package.json. The custom `export-pdf.js` script also hardcodes an absolute path to puppeteer: `/home/arau6/.nvm/versions/node/v22.17.1/lib/node_modules/md-to-pdf/node_modules/puppeteer`.
- **Fix approach:** Either:
  - Add a `package.json` declaring `markdown-it` and `markdown-it-footnote` as dependencies
  - Or document the manual install requirement in README
  - Fix the hardcoded puppeteer path in `scripts/styles/export-pdf.js`

---

## 3. Content Organization Issues

### 3.1 Duplicate Triangle Framework File

- **Issue:** `topics/epistemic_debt/assets/epistemic-trade-off-triangle.md` and `topics/epistemic_debt/references/epistemic-trade-off-triangle.md` were identical files (verified via diff).
- **Impact:** Maintenance burden — edits to one wouldn't propagate to the other. Unclear which was canonical.
- **Status:** Resolved — `references/` copy removed; `assets/epistemic-trade-off-triangle.md` is canonical.

### 3.2 Two Parallel Article Versions with Unclear Relationship

- **Issue:** `topics/epistemic_debt/article.md` (7,912 words) and `topics/epistemic_debt/cursor-article.md` (7,493 words) are both full article drafts covering the same topic with the same structure, same title, same abstract, and many shared passages.
- **Differences:** 
  - `article.md` has more polished prose and a "Beyond Software" generalization section
  - `cursor-article.md` has more practitioner-focused content, vibe coding details, additional references, and a spec-driven development section
  - Both are dated differently (article.md: created 2026-01-25, cursor-article.md: created 2026-02-08)
- **Impact:** Unclear which is the "canonical" article. Risk of divergent editing. README lists only `article.md` as the "Main article draft" — `cursor-article.md` is not mentioned.
- **Fix approach:** Either:
  - Merge the best content from both into one canonical article
  - Rename/reorganize to make the relationship clear (e.g., `article-v1.md` and `article-v2.md`, or `article-academic.md` and `article-practitioner.md`)
  - Update README to document both files and their intended audiences

### 3.3 Artifacts Directory Structure

- **Status:** Resolved. `topics/<topic>/artifacts/` uses a flat layout: `articles/` and `presentation/` only (no `drafts/` or `published/` subdirs). Publication state is kept in the artifact's frontmatter (`published_date`, `status`) and git history.

### 3.4 Content Files Outside Topic Directory Structure

- **Issue:** `iris-learnings.md` is a standalone Marp presentation in the topic root. It's not `slides.md` (the convention) and not mentioned in the README's "Files in This Topic" table.
- **Impact:** New contributors won't discover it. It breaks the convention of one `slides.md` per topic.
- **Fix approach:** Either:
  - Mention it in README
  - Rename to something like `iris-presentation.md` and update README
  - Keep `slides.md` as the general-audience presentation and `iris-learnings.md` as a specialized internal one, but document this in README

---

## 4. Script Robustness Issues

### 4.1 No Tool Availability Checks in Export Scripts

- **Issue:** Export scripts (`export-docx.sh`, `export-slides.sh`, `export-pdf.sh`) assumed `pandoc` and `marp` were installed but didn't verify before attempting export.
- **Impact:** Cryptic errors if tools were missing. Users would see "command not found" instead of a helpful message.
- **Status:** Resolved — each export script now checks for required tools at start and exits with a message pointing to `./scripts/setup.sh` if missing.

### 4.2 export-pdf.js Has Hardcoded Absolute Path

- **Issue:** `scripts/styles/export-pdf.js` line 12 contains:
  ```javascript
  const puppeteer = require('/home/arau6/.nvm/versions/node/v22.17.1/lib/node_modules/md-to-pdf/node_modules/puppeteer');
  ```
- **Impact:** This would fail on any other machine or if nvm version changed. The script was completely non-portable.
- **Status:** Resolved — `puppeteer` is now a dependency in `package.json`; script uses `require('puppeteer')`.

### 4.3 export-pdf.js Has Hardcoded Export Targets

- **Issue:** The `main()` function in `scripts/styles/export-pdf.js` hardcodes specific files to export (`article.md` → `claude-article-cc.pdf`, `cursor-article.md` → `cursor-article-cc.pdf`). The script also resolves paths relative to `scripts/` (basedir = `__dirname/..`), so it looks for `article.md` under `scripts/`, not under a topic directory; it is broken for the current repo layout.
- **Impact:** Adding new articles required editing the JS file. The naming convention (`claude-article-cc.pdf`) didn't follow any documented pattern.
- **Status:** Resolved — script accepts topic name as first argument (e.g. `node scripts/styles/export-pdf.js epistemic_debt`), resolves paths from `topics/<topic>/`, writes PDFs to `topics/<topic>/exports/`; auto-discovers `article.md` and `cursor-article.md`.

### 4.4 setup.sh Platform Coverage Gaps

- **Issue:** `setup.sh` handles:
  - Linux: apt-get, dnf, pacman
  - macOS: brew
  But for Node.js installation on Linux:
  - Only handles apt-get (line 52): `sudo apt-get install -y nodejs npm`
  - Missing: dnf, pacman fallbacks for Node.js (unlike pandoc which handles all three)
  - Missing: Windows/WSL detection (relevant since user is on WSL2)
- **Impact:** On Fedora/Arch Linux, setup.sh would fail to install Node.js if npm wasn't already present.
- **Status:** Resolved — setup.sh now includes dnf and pacman fallbacks for Node.js installation.

### 4.5 setup.sh LaTeX Installation Incomplete on Some Platforms

- **Issue:** LaTeX installation only handles apt-get on Linux and brew on macOS. Missing dnf/pacman fallbacks.
- **Impact:** Users on Fedora/Arch wouldn't get LaTeX installed automatically.
- **Status:** Resolved — setup.sh now includes dnf (`texlive-scheme-basic`) and pacman (`texlive-bin`, `texlive-core`) fallbacks for LaTeX.

### 4.6 export-all.sh Unconditionally Calls export-pdf.sh with "both"

- **Issue:** When no specific MD file is provided, `export-all.sh` (line 79) calls `export-pdf.sh "$TOPIC" both` regardless of whether `article.md` or `slides.md` exist. The `|| true` in `export-pdf.sh` handles the missing files gracefully, but it still prints confusing warning messages.
- **Impact:** Minor — users would see "Warning: No file found at..." messages during batch export.
- **Status:** Resolved — `export-all.sh` now calls `export-pdf.sh` only when at least one of `article.md` or `slides.md` exists.

---

## 5. Glossary Staleness

### 5.1 Ten+ Terms Missing from GLOSSARY.md

- **Issue:** GLOSSARY.md has not been updated since article development added many new concepts. See CONVENTIONS.md §Glossary Consistency for full list.
- **Missing terms:** Epistemic Credit, Automation Bias, Stochastic Spaghetti Effect, Context Window Amnesia, Vibe Coding, Spec-Driven Development, Epistemia, Rubber-Stamp Culture, Trade-off Triangle, Bus Factor.
- **Impact:** AI assistants referencing GLOSSARY.md for consistent terminology would miss key concepts. New article development might use inconsistent definitions.
- **Status:** Resolved — GLOSSARY.md updated with Epistemic Credit, Automation Bias, Stochastic Spaghetti Effect, Context Window Amnesia, Vibe Coding, Spec-Driven Development, Epistemia, Rubber-Stamp Culture, Trade-off Triangle, Bus Factor.

---

## 6. File Naming Violations

### 6.1 Reference Files with Spaces and Mixed Case

- **Issue:** Several reference files violated the naming convention (lowercase with hyphens):
  - `references/Epistemic_debt_definition.md` → `epistemic-debt-definition.md`
  - `references/Epistemic Debt Research Complete.pdf` → `epistemic-debt-research-complete.pdf`
  - `references/Triangle Interaction Table.pdf` → `triangle-interaction-table.pdf`
  - `tmp/` files (spaces in names) remain; `tmp/` is gitignored.
- **Impact:** Inconsistency. Scripts that handle filenames with spaces need quoting. Git operations on files with spaces are error-prone.
- **Status:** Resolved — reference files under `topics/epistemic_debt/references/` renamed to lowercase-with-hyphens; planning docs updated.

---

## 7. Missing Package Management

### 7.1 No package.json for Node.js Dependencies

- **Issue:** `node_modules/` exists with `markdown-it`, `markdown-it-footnote`, and related packages, but there's no `package.json` or `package-lock.json` at the repository root.
- **Impact:** Could not reproduce the dependency installation. `npm install` in a fresh clone would fail. Dependencies were invisible to contributors.
- **Status:** Resolved — root `package.json` added with `markdown-it`, `markdown-it-footnote`, and `puppeteer`; run `npm install` to install.

---

## 8. Orphaned/Outdated Content References

### 8.1 README "Files in This Topic" Table Incomplete

- **Issue:** `topics/epistemic_debt/README.md` lists only 5 files in its table. Missing:
  - `cursor-article.md` (second full article draft)
  - `iris-learnings.md` (IRIS presentation)
  - `assets/epistemic-trade-off-triangle.md` (triangle framework reference)
  - `references/epistemic-debt-definition.md`
  - `exports/export-pdf.js` (custom export tool)
- **Impact:** Incomplete discoverability. Contributors won't know about all available content.
- **Status:** Resolved — table now includes `cursor-article.md`, `iris-learnings.md`, `assets/epistemic-trade-off-triangle.md`, `artifacts/`, `exports/`.

### 8.2 README "Last Updated" Dates May Be Stale

- **Issue:** `topics/epistemic_debt/README.md` shows `Last Updated: 2026-01-26` but content files have been modified through 2026-02-08.
- **Impact:** Misleading freshness indicator.
- **Status:** Resolved — topic README "Last Updated" set to 2026-02-18.

---

## 9. Export Workflow Fragmentation

### 9.1 Two Competing PDF Export Mechanisms

- **Issue:** There are two PDF export paths:
  1. **Shell script** (`scripts/export-pdf.sh`): Uses pandoc/marp CLI tools. Part of the standard export workflow.
  2. **Node.js script** (`scripts/styles/export-pdf.js`): Uses markdown-it + puppeteer for higher-quality output with footnote support. Topic-specific, not integrated into the standard workflow.
- **Impact:** Confusing. Which should be used? The Node.js script produces better output (proper footnote rendering) but is non-portable and topic-specific. The shell script is portable but may not handle footnotes well.
- **Fix approach:** Either:
  - Integrate the Node.js approach into the standard export workflow
  - Document when to use which tool
  - Consolidate into one approach

### 9.2 Export File Naming Inconsistency

- **Issue:** Export files use mixed naming patterns:
  - Shell scripts produce: `article-YYYYMMDD.pdf`, `article.pdf` (latest)
  - Node.js script produces: `claude-article-cc.pdf`, `cursor-article-cc.pdf`
  - Manually created: `iris-learnings.pptx`, `iris-learnings-editable.pptx`
- **Impact:** Unclear provenance. Hard to tell which export was generated by which tool, or which article it corresponds to.
- **Fix approach:** Standardize export naming to `{source-filename}-{format}.{ext}` or similar.

---

## 10. CLAUDE.md is Empty

### 10.1 No Project Context for Claude Code

- **Issue:** `CLAUDE.md` previously existed at the repository root but was empty.
- **Impact:** Claude Code (terminal-based) sessions had no project context.
- **Status:** Resolved — `CLAUDE.md` is now a symlink to `.ai/context.md`, providing always-applied context for both Cursor and Claude Code. The legacy `.cursorrules` symlink has been removed to avoid duplicating context tokens.

---

## 11. Distribution Layer Concerns (Phase 2 Prep)

### 11.1 Token and API Key Security

- **Issue:** Phase 2 will introduce MCP servers for Substack publishing and social media cross-posting, requiring API tokens and credentials.
- **Impact:** Accidental commit of `.mcp.json`, `.env`, or analytics credentials could expose tokens.
- **Mitigation:** `.gitignore` updated to exclude `.mcp.json`, `.env`, and `analytics/credentials/`. Documented in `.ai/rules/publication.md`.

### 11.2 API Fragility

- **Issue:** Social media APIs (Twitter/X, LinkedIn, Instagram) are notoriously unstable — rate limits, breaking changes, deprecation.
- **Impact:** MCP servers may need frequent maintenance. Cross-posting workflow should not depend on all platforms being available.
- **Mitigation:** Manual workflow documented as fallback. MCP integrations planned as progressive enhancement, not hard dependency.

### 11.3 Analytics Limitations

- **Issue:** Substack provides limited analytics. Cross-platform analytics (LinkedIn impressions, Twitter engagement) require separate tracking.
- **Impact:** Difficult to measure content reach and optimize distribution strategy.
- **Mitigation:** Marked as Phase 2 scope. Initial focus on manual observation and simple metrics.

---

## Priority Summary

| Priority | Issue | Impact | Effort |
|----------|-------|--------|--------|
| ~~**Critical**~~ | ~~§1: Uncommitted directory restructure~~ | ~~Data loss risk, broken git state~~ | ~~Resolved (baseline commit)~~ |
| ~~**High**~~ | ~~§2.1: Exports not gitignored~~ | ~~Repository bloat~~ | ~~Resolved (.gitignore)~~ |
| **High** | §3.2: Two parallel article versions | Content confusion | Medium (editorial decision) |
| ~~**High**~~ | ~~§5: Glossary staleness~~ | ~~Inconsistent AI assistance~~ | ~~Resolved (GLOSSARY.md updated)~~ |
| ~~**Medium**~~ | ~~§2.2: tmp/ not gitignored~~ | ~~Repository bloat~~ | ~~Resolved (.gitignore)~~ |
| ~~**Medium**~~ | ~~§4.2: Hardcoded path in export-pdf.js~~ | ~~Non-portable tooling~~ | ~~Resolved (package.json + require)~~ |
| ~~**Medium**~~ | ~~§7: No package.json~~ | ~~Non-reproducible setup~~ | ~~Resolved (package.json added)~~ |
| ~~**Medium**~~ | ~~§10: Empty CLAUDE.md~~ | ~~Missing AI context~~ | ~~Resolved (.ai/context.md + symlink)~~ |
| **Low** | §11: Distribution layer concerns | Token security, API fragility, analytics limits | Phase 2 |
| ~~**Low**~~ | ~~§3.1: Duplicate triangle file~~ | ~~Maintenance burden~~ | ~~Resolved (references/ copy removed)~~ |
| **Low** | §3.3: Empty artifacts/ directory | Confusing structure | Low |
| ~~**Low**~~ | ~~§4.1: No tool checks in scripts~~ | ~~Poor error messages~~ | ~~Resolved (pandoc/marp checks)~~ |
| ~~**Low**~~ | ~~§6.1: Reference file naming~~ | ~~Inconsistency~~ | ~~Resolved~~ |
| ~~**Low**~~ | ~~§8.1: README table incomplete~~ | ~~Discoverability~~ | ~~Resolved~~ |
| ~~**Low**~~ | ~~§8.2: Stale README "Last Updated"~~ | ~~Discoverability~~ | ~~Resolved~~ |
| **Low** | §9: Export workflow fragmentation | Confusion | Medium |

---

*Concerns audit: 2026-02-15 | Analysis refreshed: 2026-02-18*
