# Codebase Concerns

**Analysis Date:** 2026-02-15

## 1. Directory Restructure Inconsistencies

### 1.1 Git Status Shows Deleted Files from Old Location

- **Issue:** Git status shows many `D` (deleted) entries for files under `epistemic_debt/` (without the `topics/` prefix). This indicates the content was moved from a top-level `epistemic_debt/` directory to `topics/epistemic_debt/` but the deletion of the old files was never committed.
- **Files affected:** All files previously at `epistemic_debt/*` are shown as deleted in git status — 30+ files including articles, exports, references, and raw material.
- **Impact:** The working tree is cluttered with uncommitted changes. New contributors running `git status` will see confusing deletion noise. Risk of accidentally reverting the restructure.
- **Fix approach:** Stage and commit the directory move: `git add -A && git commit -m "Move epistemic_debt/ to topics/epistemic_debt/"`. This is the most critical pending action.

### 1.2 Untracked `topics/` Directory

- **Issue:** Git status shows `?? topics/` — the entire new directory structure is untracked.
- **Impact:** All content in `topics/epistemic_debt/` is not version-controlled. Data loss risk if the working directory is cleaned or lost.
- **Fix approach:** Add `topics/` to version control as part of the restructure commit above. Ensure `.gitignore` excludes only what should be excluded (exports, node_modules).

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
- **Fix approach:** Add to `.gitignore`:
  ```
  topics/*/exports/*.pdf
  topics/*/exports/*.pptx
  topics/*/exports/*.docx
  topics/*/exports/*.html
  ```
  Keep CSS and JS export tooling files tracked.

### 2.2 tmp/ Directory Not Gitignored

- **Issue:** `tmp/` directory at repository root contains 6 PNG files (259KB–585KB) and a DOCX file. These appear to be working/scratch files (triangle diagram iterations).
- **Impact:** ~2.3MB of temporary binary files that will bloat git history if committed. Names with spaces (`01 simple triangle.png`) also suggest these are informal working assets, not final content.
- **Fix approach:** Either:
  - Add `tmp/` to `.gitignore` (if purely scratch)
  - Move relevant files to `topics/epistemic_debt/assets/` and gitignore the rest

### 2.3 node_modules/ Present but Minimal

- **Issue:** `node_modules/` exists and is correctly gitignored. Contains markdown-it and footnote plugin for the custom `export-pdf.js` script. No `package.json` or `package-lock.json` in the repository root to track these dependencies.
- **Impact:** Dependencies are installed but not declared. Running `npm install` would fail because there's no package.json. The custom `export-pdf.js` script also hardcodes an absolute path to puppeteer: `/home/arau6/.nvm/versions/node/v22.17.1/lib/node_modules/md-to-pdf/node_modules/puppeteer`.
- **Fix approach:** Either:
  - Add a `package.json` declaring `markdown-it` and `markdown-it-footnote` as dependencies
  - Or document the manual install requirement in README
  - Fix the hardcoded puppeteer path in `exports/export-pdf.js`

---

## 3. Content Organization Issues

### 3.1 Duplicate Triangle Framework File

- **Issue:** `topics/epistemic_debt/assets/epistemic-trade-off-triangle.md` and `topics/epistemic_debt/references/epistemic-trade-off-triangle.md` are identical files (verified via diff).
- **Impact:** Maintenance burden — edits to one won't propagate to the other. Unclear which is canonical.
- **Fix approach:** Keep one copy. The `assets/` location makes more sense (it's an authored asset, not a reference). Remove the `references/` copy, or vice versa.

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

### 3.3 Empty `artifacts/` Directory Structure

- **Issue:** `topics/epistemic_debt/artifacts/` contains subdirectories (`articles/drafts`, `articles/published`, `presentation/drafts`, `presentation/published`) but all are empty.
- **Impact:** This structure doesn't appear in the documented topic directory structure (in `CLAUDE.md` or `README.md`). It's either an abandoned organizational experiment or an incomplete migration.
- **Fix approach:** Either populate it with content (move final exports here?) or remove the empty structure. If kept, document it in `CLAUDE.md` topic directory structure.

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

- **Issue:** Export scripts (`export-docx.sh`, `export-slides.sh`, `export-pdf.sh`) assume `pandoc` and `marp` are installed but don't verify before attempting export.
- **Impact:** Cryptic errors if tools are missing. Users see "command not found" instead of a helpful message pointing to `setup.sh`.
- **Fix approach:** Add checks at script start:
  ```bash
  if ! command -v pandoc &>/dev/null; then
      echo "Error: pandoc not found. Run ./scripts/setup.sh first."
      exit 1
  fi
  ```

### 4.2 export-pdf.js Has Hardcoded Absolute Path

- **Issue:** `topics/epistemic_debt/exports/export-pdf.js` line 12 contains:
  ```javascript
  const puppeteer = require('/home/arau6/.nvm/versions/node/v22.17.1/lib/node_modules/md-to-pdf/node_modules/puppeteer');
  ```
- **Impact:** This will fail on any other machine or if nvm version changes. The script is completely non-portable.
- **Fix approach:** Either:
  - Add `puppeteer` as a proper dependency
  - Use a relative require path
  - Document the manual puppeteer setup requirement

### 4.3 export-pdf.js Has Hardcoded Export Targets

- **Issue:** The `main()` function in `export-pdf.js` hardcodes specific files to export (`article.md` → `claude-article-cc.pdf`, `cursor-article.md` → `cursor-article-cc.pdf`).
- **Impact:** Adding new articles requires editing the JS file. The naming convention (`claude-article-cc.pdf`) doesn't follow any documented pattern and mixes tool-specific names with content names.
- **Fix approach:** Accept input/output as command-line arguments, or make the script auto-discover markdown files in the topic directory.

### 4.4 setup.sh Platform Coverage Gaps

- **Issue:** `setup.sh` handles:
  - Linux: apt-get, dnf, pacman
  - macOS: brew
  But for Node.js installation on Linux:
  - Only handles apt-get (line 52): `sudo apt-get install -y nodejs npm`
  - Missing: dnf, pacman fallbacks for Node.js (unlike pandoc which handles all three)
  - Missing: Windows/WSL detection (relevant since user is on WSL2)
- **Impact:** On Fedora/Arch Linux, setup.sh will fail to install Node.js if npm isn't already present.
- **Fix approach:** Add dnf/pacman fallbacks for Node.js installation, matching the pandoc pattern.

### 4.5 setup.sh LaTeX Installation Incomplete on Some Platforms

- **Issue:** LaTeX installation only handles apt-get on Linux and brew on macOS. Missing dnf/pacman fallbacks.
- **Impact:** Users on Fedora/Arch won't get LaTeX installed automatically.
- **Fix approach:** Add `dnf install texlive-scheme-basic` and `pacman -S texlive-basic` fallbacks.

### 4.6 export-all.sh Unconditionally Calls export-pdf.sh with "both"

- **Issue:** When no specific MD file is provided, `export-all.sh` (line 79) calls `export-pdf.sh "$TOPIC" both` regardless of whether `article.md` or `slides.md` exist. The `|| true` in `export-pdf.sh` handles the missing files gracefully, but it still prints confusing warning messages.
- **Impact:** Minor — users see "Warning: No file found at..." messages during batch export even though the script continues.
- **Fix approach:** Check for file existence before calling export-pdf.sh for each type.

---

## 5. Glossary Staleness

### 5.1 Ten+ Terms Missing from GLOSSARY.md

- **Issue:** GLOSSARY.md has not been updated since article development added many new concepts. See CONVENTIONS.md §Glossary Consistency for full list.
- **Missing terms:** Epistemic Credit, Automation Bias, Stochastic Spaghetti Effect, Context Window Amnesia, Vibe Coding, Spec-Driven Development, Epistemia, Rubber-Stamp Culture, Trade-off Triangle, Bus Factor.
- **Impact:** AI assistants referencing GLOSSARY.md for consistent terminology will miss key concepts. New article development may use inconsistent definitions.
- **Fix approach:** Update GLOSSARY.md with definitions for all terms used in published content.

---

## 6. File Naming Violations

### 6.1 Reference Files with Spaces and Mixed Case

- **Issue:** Several reference files violate the naming convention (lowercase with hyphens):
  - `references/Epistemic_debt_definition.md` → should be `epistemic-debt-definition.md`
  - `references/Epistemic Debt Research Complete.pdf` → should be `epistemic-debt-research-complete.pdf`
  - `references/Triangle Interaction Table.pdf` → should be `triangle-interaction-table.pdf`
  - `tmp/01 simple triangle.png` → should use hyphens not spaces
  - `tmp/Triangle Interaction Table.docx` → should use hyphens not spaces
- **Impact:** Inconsistency. Scripts that handle filenames with spaces need quoting. Git operations on files with spaces are error-prone.
- **Fix approach:** Rename to follow convention. Update any references to these files.

---

## 7. Missing Package Management

### 7.1 No package.json for Node.js Dependencies

- **Issue:** `node_modules/` exists with `markdown-it`, `markdown-it-footnote`, and related packages, but there's no `package.json` or `package-lock.json` at the repository root.
- **Impact:** Cannot reproduce the dependency installation. `npm install` in a fresh clone will fail. Dependencies are invisible to contributors.
- **Fix approach:** Run `npm init -y` and `npm install markdown-it markdown-it-footnote` to create proper package management files.

---

## 8. Orphaned/Outdated Content References

### 8.1 README "Files in This Topic" Table Incomplete

- **Issue:** `topics/epistemic_debt/README.md` lists only 5 files in its table. Missing:
  - `cursor-article.md` (second full article draft)
  - `iris-learnings.md` (IRIS presentation)
  - `assets/epistemic-trade-off-triangle.md` (triangle framework reference)
  - `references/Epistemic_debt_definition.md`
  - `exports/export-pdf.js` (custom export tool)
- **Impact:** Incomplete discoverability. Contributors won't know about all available content.
- **Fix approach:** Update the table to include all significant files.

### 8.2 README "Last Updated" Dates May Be Stale

- **Issue:** `topics/epistemic_debt/README.md` shows `Last Updated: 2026-01-26` but content files have been modified through 2026-02-08.
- **Impact:** Misleading freshness indicator.
- **Fix approach:** Update to reflect actual last modification date.

---

## 9. Export Workflow Fragmentation

### 9.1 Two Competing PDF Export Mechanisms

- **Issue:** There are two PDF export paths:
  1. **Shell script** (`scripts/export-pdf.sh`): Uses pandoc/marp CLI tools. Part of the standard export workflow.
  2. **Node.js script** (`topics/epistemic_debt/exports/export-pdf.js`): Uses markdown-it + puppeteer for higher-quality output with footnote support. Topic-specific, not integrated into the standard workflow.
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
| **High** | §2.1: Exports not gitignored | Repository bloat | Low |
| **High** | §3.2: Two parallel article versions | Content confusion | Medium (editorial decision) |
| **High** | §5: Glossary staleness | Inconsistent AI assistance | Medium |
| **Medium** | §2.2: tmp/ not gitignored | Repository bloat | Low |
| **Medium** | §4.2: Hardcoded path in export-pdf.js | Non-portable tooling | Low |
| **Medium** | §7: No package.json | Non-reproducible setup | Low |
| ~~**Medium**~~ | ~~§10: Empty CLAUDE.md~~ | ~~Missing AI context~~ | ~~Resolved (.ai/context.md + symlink)~~ |
| **Low** | §11: Distribution layer concerns | Token security, API fragility, analytics limits | Phase 2 |
| **Low** | §3.1: Duplicate triangle file | Maintenance burden | Low |
| **Low** | §3.3: Empty artifacts/ directory | Confusing structure | Low |
| **Low** | §4.1: No tool checks in scripts | Poor error messages | Low |
| **Low** | §6: File naming violations | Inconsistency | Low |
| **Low** | §8: Stale README | Discoverability | Low |
| **Low** | §9: Export workflow fragmentation | Confusion | Medium |

---

*Concerns audit: 2026-02-15*
