# Epistemic Debt Content

## What This Is

Content exploring the epistemological risks of integrating LLMs into software engineering workflows. The core thesis: LLMs create "epistemic debt"—code that works but nobody understands. Currently shipped: 9-slide IRIS-2 learnings presentation demonstrating the Trade-off Triangle framework.

## Core Value

Show practitioners how to consciously position their LLM-assisted development on the Speed/Understanding/Reliability trade-off triangle.

## Current State

**Version:** v1.0 IRIS-2 Learnings Presentation (shipped 2026-02-07)

**Shipped:**
- 9-slide Marp presentation ready for Bloomberg team delivery
- Trade-off Triangle framework with concrete IRIS-2 examples
- 4 actionable takeaways with specific file paths
- All slides have speaker notes for 20-minute delivery

**Next:** Planning next milestone (article revival or new content direction)

## Requirements

### Validated

**v1.0 IRIS-2 Learnings Presentation** — shipped 2026-02-07
- ✓ 5-10 slides in Marp format — v1.0 (delivered 9 slides)
- ✓ Trade-off Triangle as central visual — v1.0
- ✓ Concrete IRIS-2 examples for each triangle vertex — v1.0 (DDD, E2E, workflow, meta)
- ✓ Actionable takeaways for Bloomberg colleagues — v1.0 (4 takeaways with file paths)

### Active

(To be defined in next milestone)

### Paused

**Milestone 1: Article** — Paused indefinitely (Phase 1/7 complete)
- Section I drafted with 2020/2025 hook, Ngabang & Quattrociocchi citations
- Trade-off Triangle visualization framework added
- Remaining: Phases 2-7 (Core Concepts through Polish)

### Out of Scope

- Full article completion — paused for now
- Prescriptive methodology — show trade-offs, not mandates
- Academic format — this is for practitioners
- External conference version — internal team first

## Context

**Origin:** Initial thesis explored in conversation on 2026-01-25.

**IRIS-2 as case study:** Real project where Trade-off Triangle practices were developed:
- 5 bounded contexts with glob-activated Cursor rules (`.cursor/rules/*.mdc`)
- Centralized ubiquitous language (`constants.py`)
- Human-authored E2E test (`test_user_journey_e2e.py` — 972 lines)
- 5 custom workflow commands (`.cursor/commands/`)
- Multi-AI context sync script (`sync-ai-instructions.sh`)
- LOC metrics in PR descriptions ("Pure Code Added" column)

**Existing work:**
- `epistemic_debt/slides.md` — General presentation with Trade-off Triangle (slides 8-14)
- `epistemic_debt/article.md` — Draft article (paused)
- `epistemic_debt/assets/trade-off-triangle.md` — Triangle visualization framework

**Key IRIS-2 practices to feature:**
- DDD → Understanding: bounded contexts, business rules in context files
- E2E → Reliability: human-authored integration tests break circular validation
- Workflow → Speed: structured commands, LOC tracking, verification-before-fix
- GSD → Meta: obsoletes custom commands with systematic workflow

## Constraints

- **Audience**: Internal Bloomberg team — can reference IRIS-2 directly
- **Length**: 5-10 slides for 20-minute talk
- **Format**: Marp markdown, following CLAUDE.md conventions
- **Tone**: Practical, experience-based — "here's what I learned"

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Trade-off Triangle as central framework | Visual, memorable, actionable | ✓ Good — Framework resonated, grounded abstract concepts |
| IRIS-2 as sole case study | Concrete > abstract; internal audience knows context | ✓ Good — File-path specificity made practices verifiable |
| Pause article for focused presentation | Ship smaller deliverable first | ✓ Good — Shipped v1.0 in single day |
| "Trade-offs are real" core message | Not prescriptive; emphasizes conscious choice | ✓ Good — Non-prescriptive tone maintained throughout |
| Four takeaways structure (one per vertex + meta) | Maps to presentation structure, reinforces framework | ✓ Good — Clear synthesis of vertex learnings |
| Meta practices as amplifiers, not vertices | GSD/multi-AI sync enable positioning, don't pick it | ✓ Good — Avoided confusing workflow with solution |

---
*Last updated: 2026-02-07 after v1.0 milestone completion*
