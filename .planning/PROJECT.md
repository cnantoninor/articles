# Epistemic Debt Content

## What This Is

Content exploring the epistemological risks of integrating LLMs into software engineering workflows. The core thesis: LLMs create "epistemic debt"—code that works but nobody understands. Current focus is a concrete presentation using IRIS-2 project learnings to illustrate the Trade-off Triangle.

## Core Value

Show practitioners how to consciously position their LLM-assisted development on the Speed/Understanding/Reliability trade-off triangle.

## Current Milestone: IRIS-2 Learnings Presentation

**Goal:** 5-10 slide presentation for internal Bloomberg team demonstrating Trade-off Triangle through concrete IRIS-2 practices.

**Core message:** Trade-offs are real — Speed/Understanding/Reliability require conscious positioning, not speed maximization.

**Target features:**
- Trade-off Triangle visual with IRIS-2 examples
- DDD as Understanding pull (bounded contexts, ubiquitous language)
- Human E2E tests as Reliability pull (circular validation breaker)
- Workflow commands as Speed enabler (now replaced by GSD)
- Concrete "what I actually did" examples with file paths

## Requirements

### Validated

(None yet — ship to validate)

### Active

**Milestone 2: IRIS-2 Learnings Presentation**
- [ ] 5-10 slides in Marp format
- [ ] Trade-off Triangle as central visual
- [ ] Concrete IRIS-2 examples for each triangle vertex
- [ ] Actionable takeaways for Bloomberg colleagues

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
| Trade-off Triangle as central framework | Visual, memorable, actionable | — Pending |
| IRIS-2 as sole case study | Concrete > abstract; internal audience knows context | — Pending |
| Pause article for focused presentation | Ship smaller deliverable first | — Pending |
| "Trade-offs are real" core message | Not prescriptive; emphasizes conscious choice | — Pending |

---
*Last updated: 2026-01-27 after pivoting to IRIS-2 presentation milestone*
