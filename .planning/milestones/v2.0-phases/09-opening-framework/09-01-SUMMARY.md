---
phase: 09-opening-framework
plan: 01
subsystem: presentation
tags: [marp, slides, epistemic-debt, trade-off-triangle, iris-2]

# Dependency graph
requires:
  - phase: 01-opening-hook
    provides: "2020 vs 2025 contrast hook with 'Same confidence. Different warrant.'"
  - phase: quick-task
    provides: "Trade-off Triangle visual framework in epistemic_debt/assets/"
provides:
  - "Opening slides (1-4) for IRIS-2 learnings presentation"
  - "Marp presentation file ready for vertex content addition"
  - "Hook and framework adapted from proven general slides"
affects: [10-vertex-content, 11-close-polish]

# Tech tracking
tech-stack:
  added: []
  patterns: ["Marp slide format with speaker notes", "ASCII diagrams in code blocks"]

key-files:
  created: ["epistemic_debt/iris2-learnings.md"]
  modified: []

key-decisions:
  - "Adapted proven hook from slides.md lines 18-30 for immediate audience engagement"
  - "Simplified triangle visual to core vertices without complex annotations"
  - "Positioned IRIS-2 as case study on slide 4 (framework before examples pattern)"

patterns-established:
  - "Marp frontmatter: theme default, paginate true, title"
  - "Speaker notes on each slide for delivery guidance"
  - "ASCII diagrams in triple-backtick code blocks for proper spacing"

# Metrics
duration: 1min
completed: 2026-01-27
---

# Phase 09 Plan 01: Opening Framework Summary

**Four-slide Marp presentation opening with 2020/2025 hook and Trade-off Triangle framework, positioning IRIS-2 as concrete case study**

## Performance

- **Duration:** 1 min
- **Started:** 2026-01-27T04:02:54Z
- **Completed:** 2026-01-27T04:03:46Z
- **Tasks:** 1
- **Files modified:** 1

## Accomplishments
- Created IRIS-2 learnings presentation file with opening slides
- Adapted proven hook ("Same confidence. Different warrant.") from general slides
- Established Trade-off Triangle as mental model with ASCII visual
- Positioned IRIS-2 practices (DDD, E2E tests, GSD) as case study

## Task Commits

Each task was committed atomically:

1. **Task 1: Create IRIS-2 learnings presentation with opening slides** - `0a99094` (feat)

## Files Created/Modified
- `epistemic_debt/iris2-learnings.md` - Marp presentation with 4 opening slides (Title, Hook, Triangle, IRIS-2 positioning)

## Decisions Made

1. **Adapted hook from slides.md** - Used proven 2020 vs 2025 contrast for immediate engagement
2. **Simplified triangle visual** - Kept core vertices (SPEED, UNDERSTANDING, RELIABILITY) with basic annotations; removed complex theory for this focused presentation
3. **Framework-first ordering** - Slide 3 introduces triangle framework, slide 4 positions IRIS-2 as example (establishes mental model before concrete practices)

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

**Ready for Phase 10 (Vertex Content):**
- Opening framework established (slides 1-4 complete)
- Triangle visual with labeled vertices in place
- IRIS-2 introduced as case study
- File structure ready to accept vertex content slides (Understanding practices, Reliability practices, Speed enablers)

**Structure for Phase 10:**
- Add slide 5: Understanding vertex (DDD bounded contexts detail)
- Add slide 6: Reliability vertex (Human-authored E2E tests detail)
- Add slide 7: Speed enabler (GSD workflow detail)
- Add slide 8: Conscious positioning result

**Phase 11 will add:**
- Closing slide with key takeaways

**No blockers or concerns.**

---
*Phase: 09-opening-framework*
*Completed: 2026-01-27*
