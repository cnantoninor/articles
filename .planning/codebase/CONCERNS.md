# Codebase Concerns

**Analysis Date:** 2026-03-14

## Tech Debt

**Fragmented Article Architecture:**
- Issue: Seven article variants exist across epistemic_debt topic, all in draft status, with no clear single source of truth. Files include `article-0.md` through `article-7.md` plus `whole-cc-article-v1.md` and `whole-cursor-article-v1.md`, creating merge/navigation difficulty.
- Files: `topics/epistemic_debt/artifacts/articles/article-{0-7}.md`, `whole-cc-article-v1.md`, `whole-cursor-article-v1.md`
- Impact: Content maintenance becomes complex; unclear which draft is canonical; risk of conflicting updates; publishing requires explicit version selection without clear criteria.
- Fix approach: Define single publication draft file with version tracking in front-matter. Archive earlier variants to `raw_material/archive/` if needed. Use Roadmap (ROADMAP.md) to guide which section takes priority at each phase.

**Unfinished Content Scaffolding:**
- Issue: Articles contain extensive [TODO:] and [TODO MOVED FROM] markers indicating content is partially developed across multiple files. Article 3 has 7+ TODOs; Article 4 has 2+ TODOs; Article 6 has research notes mixed with draft text.
- Files: `article-3-when-debt-defaults.md` (lines 25-39), `article-4-the-solutioning-trap.md` (lines 88-92), `article-6-measuring-the-unmeasurable.md` (lines 27, 73)
- Impact: Articles cannot be published as-is; content gaps block phase execution; TODO items track research work needed but aren't linked to phase plans.
- Fix approach: Convert all [TODO:] markers to GitHub Issues with links in relevant phase plans. Link research documents (.planning/research/*.md) to specific TODOs. Complete research documents before articles reference them.

**Missing CSS for PDF Export:**
- Issue: `scripts/styles/export-pdf.js` references `pdf-export-styles.css` (line 37) but file does not exist in repository.
- Files: `scripts/styles/export-pdf.js`, missing `scripts/styles/pdf-export-styles.css`
- Impact: PDF export fails at runtime with file not found error; export feature unusable despite being documented.
- Fix approach: Create `scripts/styles/pdf-export-styles.css` with base styles (margins, fonts, footnote formatting). Test with actual article export before committing.

## Failing Features

**PDF Export Not Functional:**
- Symptoms: `npm run export-pdf <topic>` fails due to missing CSS file
- Files: `scripts/styles/export-pdf.js` line 37
- Current mitigation: None; feature listed in package.json scripts but blocked
- Recommendation: Restore or recreate `pdf-export-styles.css` with proper styling for article export.

## Known Gaps

**Content Research-Implementation Mismatch:**
- Problem: Research documents (.planning/research/) document findings but articles don't directly cite or integrate them. CONTENT-GAPS.md lists 3+ concrete findings (SaaStr incident, AlterSquare case, Veracode 2026 data) that should appear in Article 3 but don't yet.
- Files: `.planning/research/CONTENT-GAPS.md` lines 24-79 vs `article-3-when-debt-defaults.md` lines 51-59 (only partial integration of SaaStr incident)
- Current mitigation: TODO markers in articles signal where content belongs
- Recommendations: Create explicit content mapping in phase plans linking each TODO to corresponding research document section. Update article drafts to pull from research documents during phase execution.

**Incomplete Phase Definitions:**
- Problem: Phases 13-17 in ROADMAP.md show "TBD during planning" for all plans. Phase descriptions exist but detailed execution steps missing.
- Files: `.planning/ROADMAP.md` lines 64, 77, 92, 107, 122
- Current mitigation: STATE.md indicates Phase 12 complete; next step is `/gsd:plan-phase 13`
- Recommendations: Run full phase planning for 13-17 before execution to surface content gaps earlier.

## Security Considerations

**Environment Configuration Incomplete:**
- Risk: `.mcp.json` listed in .gitignore but not documented; analytics credentials expected in `analytics/credentials/` but structure undefined; potential for secrets to leak if credentials accidentally committed.
- Files: `.gitignore` lines 12-14, `analytics/` directory structure undefined
- Current mitigation: .gitignore files present; .gitkeep preventing empty directory commit
- Recommendations: Document .env template with required keys. Create `analytics/credentials/.example.json` showing required structure (without actual values). Add pre-commit hook to verify no credentials files in commits.

**Dependency Chain Risk - Puppeteer:**
- Risk: Puppeteer 23.x used for PDF export launches browser process with `--no-sandbox` flag (export-pdf.js line 55), disabling security sandbox in some environments.
- Files: `scripts/styles/export-pdf.js` line 55, `package.json` line 11
- Current mitigation: Sandbox disabled intentionally (comment suggests CI/container usage)
- Recommendations: Document when sandbox must be disabled. Consider splitting into environment-specific export scripts (local with sandbox vs. CI without). Add security note to export documentation.

## Performance Bottlenecks

**Node.js Nested Infographic Project:**
- Problem: `topics/epistemic_debt/artifacts/infographics/article-2/` contains full Next.js app with node_modules (14MB+) inside topic directory. Creates large nested git tree; npm install duplicates dependencies from parent package.json; build/dev workflow requires two separate package management contexts.
- Files: `topics/epistemic_debt/artifacts/infographics/article-2/package.json`, `package.json`, `node_modules/` (estimated 22901 total lines in tree)
- Cause: Infographics app developed independently before integration; separate npm context created to isolate React/Next.js dependencies from parent markdown tooling.
- Improvement path: Evaluate whether infographic app should be separate repository or monorepo structure. If keeping local, document build workflow clearly. Consider .gitignore for infographic node_modules or use git submodule.

**Large Untracked Planning Documents:**
- Problem: `.cursor/plans/` contains 9 plan files (335-531 lines each) tracked in git but not part of publication pipeline. These are internal planning artifacts that could be moved to separate branch or archived.
- Files: `.cursor/plans/*.plan.md`
- Current mitigation: .gitignore currently excludes `.cursor/plans` (line 16)
- Improvement path: Verify exclusion is working; these files inflate repository size without supporting publication.

## Fragile Areas

**Export Pipeline Single Point of Failure:**
- Files: `scripts/styles/export-pdf.js`, missing `pdf-export-styles.css`
- Why fragile: PDF export depends on external CSS file that doesn't exist. No fallback styling. Puppeteer browser context requires manual resource cleanup (line 77 `browser.close()` — if error thrown before this, browser process orphaned).
- Safe modification: Add try-catch wrapping browser.close(). Create CSS file with defensive defaults. Add logging to track resource cleanup.
- Test coverage: No tests for export-pdf.js; manually testing only. Add test that verifies CSS file exists before export attempt.

**Article Dependency Chain:**
- Files: Phase 12 (Section II) complete → Phases 13-17 pending. Articles reference each other across files (article-3 references article-2 concept; article-5 builds on article-3's framework).
- Why fragile: Phase execution depends on content in prior articles being finalized. If article-3 TODOs not resolved, article-4 and article-5 can't reference concrete examples accurately.
- Safe modification: Complete and publish each article before starting subsequent phase. Add final review checklist to verify all TODOs and GAPs resolved.
- Test coverage: Verification documents exist (.planning/phases/*/VERIFICATION.md) but don't explicitly test cross-article coherence.

**Infographic App Build State Unknown:**
- Files: `topics/epistemic_debt/artifacts/infographics/article-2/app/Infographics.js` (1024 lines), app/layout.js, app/page.js
- Why fragile: React/Next.js app embedded in article repo; unclear if it's actively maintained or frozen. Package.json shows next@14.2.0 but no recent commit history visible. No documentation of build/deployment process.
- Safe modification: Document whether app is production-ready. If needed, add explicit build/test steps. If frozen, move to separate archived repo or branch.
- Test coverage: No test files found in infographics directory; app untested.

## Test Coverage Gaps

**No Tests for Export Scripts:**
- What's not tested: `scripts/styles/export-pdf.js` has no test file. Cannot verify CSS file dependency exists, Puppeteer integration works, or malformed markdown is handled gracefully.
- Files: `scripts/styles/export-pdf.js`, no `.test.js` or `.spec.js` counterpart
- Risk: Broken export feature only discovered when user runs `npm run export-pdf`. CSS missing not caught during development.
- Priority: High — export pipeline is user-facing feature

**No Tests for Phase Execution:**
- What's not tested: Phase plan completion criteria (success_criteria in ROADMAP.md) have no automated verification. Phases mark complete by manual attestation.
- Files: `.planning/phases/*/VERIFICATION.md` documents manual checks but no automated test suite
- Risk: Phase success criteria missed silently; content gaps discovered post-publication.
- Priority: Medium — mitigated by manual verification docs, but automatable

**No Content Validation Tests:**
- What's not tested: Article front-matter consistency (title, subtitle, status fields), reference link validity, citation accuracy
- Files: All `topics/*/artifacts/articles/*.md`
- Risk: Broken links in exported PDFs, inconsistent metadata, unpublished articles marked as published
- Priority: Medium — catch-able with document linter

## Missing Critical Features

**MCP Server Integration Incomplete:**
- Feature gap: Docs mention MCP servers for Substack drafting, social cross-posting, and GA4 analytics (docs/mcp-setup.md) but no actual MCP server code or configuration templates found in repository.
- Blocks: Publishing workflow automation; cannot systematically cross-post to LinkedIn, Twitter, Instagram as described
- Files: `docs/mcp-setup.md` (documents workflow but no implementation), `.mcp.json` referenced but not tracked
- Recommendation: Either implement MCP servers documented in Phase 2 setup or remove documentation about them if out of scope.

**Measurement Framework Absent:**
- Feature gap: Epistemic debt article requires measurement approaches (Section VI) but research is incomplete. MEASUREMENT.md exists but content is partial research notes, not integrated into article structure.
- Blocks: Phase 16 (Measurement & Conclusion) cannot start until measurement framework documented
- Files: `.planning/research/MEASUREMENT.md` (554 lines but framework incomplete), `article-6-measuring-the-unmeasurable.md` (draft, 2600+ words but unfinished)
- Recommendation: Define measurement framework in research document first. Link framework to article-6 during phase execution.

## Scaling Limits

**Infographic App Deployment Target Unknown:**
- Current capacity: Next.js app in `topics/epistemic_debt/artifacts/infographics/article-2/` ready to build, unclear deployment target
- Limit: Where does built app run? No vercel.json, netlify.toml, or Docker config found (except mentioned in git log "added vercel deploy")
- Scaling path: Document deployment target (Vercel vs. Netlify vs. self-hosted). Add deployment config to repository with environment setup.

**Single Author Publication Pipeline:**
- Current capacity: All content authored by single person (Antonino Rau). Publication workflow entirely manual (Substack UI + manual social cross-posting).
- Limit: Cannot scale to multiple writers; publication frequency limited to author's availability
- Scaling path: Implement MCP servers for Substack/social integration. Define collaborative editing workflow (shared Google Doc → markdown → git).

## Dependencies at Risk

**Puppeteer Sandbox Bypass:**
- Risk: Puppeteer ^23.0.0 with --no-sandbox flag disables browser security features in PDF export
- Impact: If used in production with untrusted input, malicious PDF content could escape sandbox
- Migration plan: Review whether sandbox actually needed (is PDF export in container/CI environment?). If so, document explicitly. Consider using headless: 'new' strategy instead of sandbox bypass.

**Old Next.js Version in Infographics:**
- Risk: Next.js 14.2.0 (from Feb 2024) used in infographics app; security patches after release date uncertain
- Impact: Potential unpatched vulnerabilities if app serves public traffic
- Migration plan: Test upgrading to latest Next.js LTS. Verify React 18.3.0 compatibility. Document version lock reason if specific version required.

**Markdown-it Footnote Pinned:**
- Risk: markdown-it-footnote@4.0.0 pinned exact version; check for security advisories
- Impact: If vulnerability found, must manually update and test
- Migration plan: Review package advisories (`npm audit`). Consider allowing minor version updates (^4.0.0 to ^4.1.0 range if safe).

---

*Concerns audit: 2026-03-14*
