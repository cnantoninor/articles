---
phase: 10-vertex-content
plan: 01
subsystem: content
tags: [marp, presentation, ddd, tdd, iris-2, trade-off-triangle]

# Dependency graph
requires:
  - phase: 09-opening-framework
    provides: Opening slides (1-4) with Trade-off Triangle framework
provides:
  - Vertex content slides (5-8) with concrete IRIS-2 examples
  - Understanding vertex: DDD practices (bounded contexts, ubiquitous language)
  - Reliability vertex: E2E testing breaking circular validation
  - Speed vertex: Workflow commands with LOC metrics
  - Meta practices positioned as amplifiers (GSD, multi-AI sync)
affects: [11-close-polish]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Vertex-specific examples with concrete file paths"
    - "Meta practices as amplifiers, not vertices"

key-files:
  created: []
  modified:
    - epistemic_debt/iris2-learnings.md

key-decisions:
  - "Meta practices (GSD, multi-AI sync) positioned as amplifiers that enable conscious positioning, not vertex choices"
  - "Each vertex backed by specific IRIS-2 file paths for Bloomberg team context"
  - "Speaker notes explain WHY each practice matters for its vertex (trade-off implications)"

patterns-established:
  - "Concrete over abstract: Every vertex claim backed by actual file path"
  - "Trade-off explicit: Speaker notes explain vertex positioning implications"

# Metrics
duration: 1min
completed: 2026-01-27
---

# Phase 10 Plan 01: Vertex Content Summary

**Four vertex slides with concrete IRIS-2 examples: DDD bounded contexts, human E2E tests, workflow commands, and meta amplifiers**

## Performance

- **Duration:** 1 min
- **Started:** 2026-01-27T21:34:15Z
- **Completed:** 2026-01-27T21:35:36Z
- **Tasks:** 1
- **Files modified:** 1

## Accomplishments
- Added Understanding vertex slide with 5 bounded contexts, ubiquitous language, and business rules
- Added Reliability vertex slide with 972-line human E2E test breaking circular validation
- Added Speed vertex slide with custom workflow commands and LOC metrics
- Added Meta practices slide positioning GSD and multi-AI sync as amplifiers

## Task Commits

Each task was committed atomically:

1. **Task 1: Add vertex content slides with IRIS-2 examples** - `8ac8624` (feat)

## Files Created/Modified
- `epistemic_debt/iris2-learnings.md` - Extended from 4 slides to 8 slides with vertex content

## Decisions Made

**1. Meta practices as amplifiers, not vertices**
- Rationale: GSD and multi-AI sync don't pick a position on the triangle — they enable better execution of whatever position you choose
- Impact: Prevents confusion that workflow is a "solution" to trade-offs; it's a multiplier

**2. Each vertex backed by specific file paths**
- Rationale: Bloomberg audience knows IRIS-2 context; concrete references make examples verifiable
- Impact: Slides ground abstract triangle concepts in real implementation

**3. Speaker notes explain trade-off implications**
- Rationale: Not just "here's what we did" but "why this matters for Understanding/Reliability/Speed"
- Impact: Reinforces conscious positioning theme throughout presentation

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Presentation core content complete (slides 1-8). Ready for Phase 11 (Close & Polish) to add:
- Closing slide with takeaways
- Opening refinement if needed
- Final polish and speaker notes review

No blockers.

---
*Phase: 10-vertex-content*
*Completed: 2026-01-27*
