---
phase: 13-article-3-when-epistemic-debt-defaults
plan: 02
subsystem: content
tags: [epistemic-debt, article, social-teasers, publication, linkedin, twitter, instagram, substack-notes]

requires:
  - phase: 13-01
    provides: Complete Article 3 body with final content, case studies, failure taxonomy, and 0 GAP markers — required for teasers to reference final content

provides:
  - Social teasers for all four platforms in YAML front-matter (LinkedIn, Twitter/X, Instagram, Substack Notes)
  - Article status updated to "review" (pending user publication approval)
  - Publication readiness checkpoint (Task 2) awaiting human verification

affects:
  - 13-03 and beyond: Article 3 publication must be confirmed before cross-series links from later articles resolve correctly

tech-stack:
  added: []
  patterns:
    - "Social teaser pattern: lead with quantified evidence (10:1 ratio, 77% failure rate), follow with mechanism, end with [ARTICLE_URL] placeholder"
    - "Platform-specific tone differentiation: LinkedIn = professional/exploratory, Twitter = punchy/evidence-first, Instagram = accessible/casual, Substack Notes = exploratory/direct"

key-files:
  created: []
  modified:
    - topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md

key-decisions:
  - "LinkedIn teaser leads with the 10:1 cost ratio (more tangible for engineering leaders) rather than the database deletion incident (more dramatic but less generalizable)"
  - "Twitter teaser pairs both key statistics (10:1 ratio + 77% failure rate) for maximum impact in 2 tweets"
  - "Instagram teaser focuses on mechanism (friction removal + abstraction level shift) rather than specific statistics — more accessible to a broader audience"
  - "Substack Notes teaser includes all three key facts (200h/2000h, 77%, failure taxonomy) as a complete standalone summary"
  - "All teasers use exploratory framing ('I look at', 'case studies', 'industry data that says') — no prescriptive claims"

patterns-established:
  - "Teaser quantification pattern: use the most striking ratio first (10:1) to hook, then supporting evidence (77%) to substantiate"

requirements-completed: [ART3-06]

duration: 2min
completed: 2026-03-14
---

# Phase 13 Plan 02: Social Teasers and Publication Readiness Summary

**Four platform-specific social teasers written and added to Article 3 YAML front-matter; article status set to review — publication gated on user confirmation of Article 2 live status and content approval (Task 2 checkpoint)**

## Performance

- **Duration:** ~2 min
- **Started:** 2026-03-14T21:07:00Z
- **Completed:** 2026-03-14T21:09:01Z (Task 1 only; Task 2 is checkpoint:human-verify)
- **Tasks:** 1 of 2 complete (Task 2 requires human action)
- **Files modified:** 1

## Accomplishments

- Wrote LinkedIn teaser (3 paragraphs, 4 hashtags, exploratory professional tone) leading with the 10:1 cost ratio hook
- Wrote Twitter/X teaser (2-tweet format) pairing the 10:1 ratio with the 77% failure rate
- Wrote Instagram caption (2 paragraphs, accessible tone) focusing on the core mechanism
- Wrote Substack Notes teaser (2-sentence summary with series framing)
- Updated article status from "draft" to "review"
- All teasers verified against final article content (Plan 01 output) — no earlier draft content referenced

## Task Commits

1. **Task 1: Write social teasers and update YAML front-matter** - `0615124` (feat)
2. **Task 2: Publication readiness review** - PENDING (checkpoint:human-verify)

## Files Created/Modified

- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md` — social_teasers block populated for all four platforms; status updated to review

## Decisions Made

- LinkedIn teaser leads with 10:1 cost ratio (more relatable to engineering leaders) rather than the database deletion (dramatic but edge-case)
- Twitter teaser pairs both key statistics to maximize impact in limited format
- Instagram focuses on mechanism not statistics — broader audience, less context for numbers
- All teasers maintain exploratory voice ("I look at", "the data that says") per publication rules — no prescriptive claims

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

Task 2 (publication readiness checkpoint) requires user to:
1. Confirm Article 2 is live at https://antoninorau.substack.com/
2. Review Article 3 content and social teasers
3. Approve for publication or request changes
4. Resolve any remaining [GAP] markers (13-01 SUMMARY reports 0 GAP markers — verify holds)

## Next Phase Readiness

- Article 3 teasers complete; article in "review" status
- Blocked on user confirmation: Article 2 publication status must be confirmed before Article 3 can go live (series cross-link in header points to Article 2 URL)
- ART3-06 complete; ART3-07 gated on user approval in Task 2 checkpoint

---
*Phase: 13-article-3-when-epistemic-debt-defaults*
*Completed: 2026-03-14 (partial — Task 2 checkpoint pending)*
