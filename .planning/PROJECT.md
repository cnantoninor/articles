# Epistemic Debt Content

## What This Is

A practitioner-focused article exploring the epistemological risks of integrating LLMs into workflows. The core thesis: LLMs create "epistemic debt"—outputs that work but nobody understands. The article presents the Speed/Understanding/Reliability trade-off triangle as a framework for conscious positioning, with concrete examples from software engineering (IRIS-2 case study) and generalized applications to other LLM-assisted tasks.

## Core Value

Show practitioners how to consciously position their LLM-assisted development on the Speed/Understanding/Reliability trade-off triangle.

## Current Milestone: v2.0 Article Completion

**Goal:** Complete the full epistemic debt article (Sections II-VII), filling content gaps with research and concrete examples, while generalizing the Trade-off Triangle framework beyond software engineering.

**Target sections:**
- Section II: Epistemic Debt: A New Lens (comparison table, default events)
- Section III: The Solutioning Trap (jumping to solutions without epistemic clarity)
- Section IV: Epistemic Debt in the SDLC (Intent→Spec, Spec→Impl, Impl→Validation boundaries)
- Section V: The Trade-off Triangle (adapt from IRIS-2 slides + generalize to any LLM task)
- Section VI: The Measurement Problem (empirical indicators)
- Section VII: Conclusion

**Shipped in v1.0:**
- 9-slide IRIS-2 Learnings Presentation (2026-02-07)
- Section I: The Epistemic Shift (Phase 1, 2026-01-26)

## Requirements

### Validated

**v1.0 IRIS-2 Learnings Presentation** — shipped 2026-02-07
- ✓ 5-10 slides in Marp format — v1.0 (delivered 9 slides)
- ✓ Trade-off Triangle as central visual — v1.0
- ✓ Concrete IRIS-2 examples for each triangle vertex — v1.0 (DDD, E2E, workflow, meta)
- ✓ Actionable takeaways for Bloomberg colleagues — v1.0 (4 takeaways with file paths)

### Active

**v2.0 Article Completion** — In progress
- Section II: Epistemic debt definition with tech debt comparison table and failure examples
- Section III: Solutioning trap analysis with concrete scenarios
- Section IV: SDLC boundary analysis (3 boundaries with examples)
- Section V: Trade-off Triangle framework adapted from IRIS-2 + generalized applications
- Section VI: Measurement approaches (empirical indicators, challenges)
- Section VII: Conclusion with practitioner takeaways
- Research-backed examples filling [GAP] markers
- Practitioner-focused tone with minimal academic citations


### Out of Scope

- Prescriptive methodology — show trade-offs, not mandates
- Academic paper format — practitioner-focused article
- Heavy academic citations — minimize, focus on industry examples
- External conference version — not yet

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

- **Audience**: Practitioners (engineering leaders, senior engineers, architects) — use accessible language
- **Length**: 4000-6000 words target (from article.md metadata)
- **Format**: Markdown article format
- **Tone**: Practical, experience-based, balanced — "here's what I've found worth examining"
- **Citations**: Practitioner-focused — minimize academic sources, emphasize concrete examples and industry experience
- **Triangle Scope**: Software engineering (IRIS-2) as primary + generalized applications (article writing, LLM-as-Judge, etc.)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Trade-off Triangle as central framework | Visual, memorable, actionable | ✓ Good — Framework resonated, grounded abstract concepts |
| IRIS-2 as sole case study | Concrete > abstract; internal audience knows context | ✓ Good — File-path specificity made practices verifiable |
| Pause article for focused presentation | Ship smaller deliverable first | ✓ Good — Shipped v1.0 in single day |
| "Trade-offs are real" core message | Not prescriptive; emphasizes conscious choice | ✓ Good — Non-prescriptive tone maintained throughout |
| Four takeaways structure (one per vertex + meta) | Maps to presentation structure, reinforces framework | ✓ Good — Clear synthesis of vertex learnings |
| Meta practices as amplifiers, not vertices | GSD/multi-AI sync enable positioning, don't pick it | ✓ Good — Avoided confusing workflow with solution |

| Resume article work from Phase 1 | v2.0 completes full article; v1.0 shipped presentation gave triangle validation | ✓ Good — Presentation validated framework resonates; ready to expand |

---
*Last updated: 2026-02-07 after v2.0 milestone start*
