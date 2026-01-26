# Epistemic Debt Article & Presentation

## What This Is

An exploratory article examining the epistemological risks of integrating LLMs into software engineering workflows, followed by a presentation adaptation. The article argues that LLMs create "epistemic debt"—code that works but nobody understands—and explores practices that might help maintain developer understanding in an LLM-augmented world.

## Core Value

Reframe the "will AI replace programmers?" debate toward "what practices maintain epistemic warrant in LLM-assisted development?"

## Requirements

### Validated

(None yet — ship to validate)

### Active

**Milestone 1: Article**
- [ ] Complete 4000-word article with exploratory, non-prescriptive tone
- [ ] Fill all identified content gaps with concrete examples
- [ ] Maintain accessibility for broad tech audience while preserving philosophical rigor
- [ ] Integrate relevant research citations

**Milestone 2: Presentation**
- [ ] Transform article into conference/meetup presentation format
- [ ] Create Marp-compatible slides
- [ ] Design visual aids for key concepts (epistemic boundaries diagram, debt accumulation comparison)

### Out of Scope

- Prescriptive framework or methodology — this is exploratory
- Technical implementation guides — this is conceptual
- Academic paper format — this is for practitioners
- Video production — written/slide formats only

## Context

**Origin:** Initial thesis explored in conversation on 2026-01-25. Deep questioning covered:
- Epistemic warrant vs. epistemic debt framing (chose "debt" for accessibility)
- Solutioning trap concept (not about juniority, about skipping problem definition)
- Three epistemic boundaries where debt accumulates
- Guardrails worth examining (DDD, E2E testing, transformed PR review)
- Measurement problem (most open area)

**Existing work:**
- `epistemic_debt/article.md` — Draft with structure and gaps marked
- `epistemic_debt/raw_material/outline-v1-epistemic-debt.md` — Detailed outline
- `epistemic_debt/raw_material/gsd-convo-1-on-epistemic-debt.md` — Exploration transcript
- `epistemic_debt/slides.md` — Placeholder for presentation

**Key decisions from prior conversation:**
- Use "epistemic debt" not "epistemic warrant" (more accessible)
- Frame as exploratory essay, not prescriptive solutions
- Emphasize that LLMs expose existing problems but make them worse (velocity and scale)
- Measurement section should be most open/exploratory

## Constraints

- **Tone**: Exploratory, not prescriptive — present ideas for discussion
- **Audience**: Broad tech audience — define philosophical terms, use concrete examples
- **Length**: ~4000 words for article, 20-30 slides for presentation
- **Format**: Markdown (Marp for slides), following CLAUDE.md conventions

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| "Epistemic debt" framing over "warrant" | More accessible, connects to existing mental models (tech debt) | — Pending |
| Three epistemic boundaries structure | Intent→Spec, Spec→Code, Code→Tests captures where debt accumulates | — Pending |
| Exploratory tone, not prescriptive | Target audience wants discussion, not another methodology | — Pending |
| Milestones: Article first, then presentation | Article establishes content, presentation adapts it | — Pending |

---
*Last updated: 2026-01-26 after GSD initialization from prior conversation*
