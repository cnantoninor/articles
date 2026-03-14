# Epistemic Debt Content

## What This Is

A 7-part practitioner-focused article series exploring the epistemological risks of integrating LLMs into workflows. Published on Substack (The AI Mirror). The core thesis: LLMs create "epistemic debt" — outputs that work but nobody understands. The series presents the Speed/Understanding/Reliability trade-off triangle as a framework for conscious positioning, with concrete examples from software engineering and generalized applications to other LLM-assisted tasks.

## Core Value

Show practitioners how to consciously position their LLM-assisted work on the Speed/Understanding/Reliability trade-off triangle.

## Current State

**Published articles:**
- Article 0: Series overview — https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation
- Article 1: The Epistemic Shift (Section I) — published
- Article 2: Epistemic Debt: The Math, The Cost, and Why It's Not Technical Debt (Section II) — published

**Remaining articles (3-7):**
- Article 3: When Epistemic Debt Defaults (case studies + industry data)
- Article 4: The Solutioning Trap (vibe coding, automation bias, velocity trap)
- Article 5: The Trade-off Triangle (universal framework + domain generalizations)
- Article 6: Measuring the Unmeasurable (proxy indicators, honest caveats)
- Article 7: Beyond Software (generalization to content, research, decision support)

**Content on disk:** ~9,460 lines across topics/epistemic_debt/

## Requirements

### Validated

**v1.0 IRIS-2 Learnings Presentation** — shipped 2026-02-07
- ✓ 9-slide Marp presentation with Trade-off Triangle framework — v1.0
- ✓ Concrete IRIS-2 examples for each triangle vertex — v1.0
- ✓ Actionable takeaways for Bloomberg colleagues — v1.0

**v2.0 Article Completion** — shipped 2026-03-14 (partial)
- ✓ Section II: Mathematical definition (Ed integral), 6-dimension comparison table — v2.0
- ✓ Section II: 3 dramatic default-event examples (SaaStr, AlterSquare, healthcare) — v2.0
- ✓ Section II: Industry failure statistics with footnoted citations — v2.0
- ✓ Article 0: Series overview published on Substack — v2.0
- ✓ Article 2: Section II published on Substack — v2.0

### Active

## Current Milestone: v3.0 Epistemic Debt Series: Articles 3–7

**Goal:** Write and publish articles 3-7 of the epistemic debt series, completing the full 7-part series on Substack.

**Target features:**
- Article 3: When Epistemic Debt Defaults (case studies + industry data)
- Article 4: The Solutioning Trap (vibe coding, automation bias, SDLC boundaries)
- Article 5: The Trade-off Triangle (framework + IRIS-2 practices)
- Article 6: Measuring the Unmeasurable (proxy indicators, honest caveats)
- Article 7: Beyond Software (generalization to other domains)

### Out of Scope

- Prescriptive methodology — show trade-offs, not mandates
- Academic paper format — practitioner-focused article
- Heavy academic citations — minimize, focus on industry examples
- External conference version — not yet

## Context

**Origin:** Initial thesis explored in conversation on 2026-01-25.

**Publication:** The AI Mirror (Substack) — weekly cadence

**IRIS-2 as case study:** Real project where Trade-off Triangle practices were developed:
- 5 bounded contexts with glob-activated Cursor rules
- Human-authored E2E test (972 lines)
- Custom workflow commands and LOC metrics

**Existing content artifacts:**
- `topics/epistemic_debt/artifacts/articles/` — published articles
- `topics/epistemic_debt/article.md` — draft article with Sections I-III+ (gaps remain)
- `topics/epistemic_debt/slides.md` — general presentation
- `topics/epistemic_debt/iris2-learnings.md` — IRIS-2 presentation (v1.0)

## Constraints

- **Audience**: Practitioners (engineering leaders, senior engineers, content/research professionals)
- **Format**: Markdown → Substack
- **Tone**: Exploratory, not prescriptive — "here's what I've found worth examining"
- **Citations**: Practitioner-focused — minimize academic sources, emphasize concrete examples
- **Triangle Scope**: Universal framework, not software-only

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Trade-off Triangle as central framework | Visual, memorable, actionable | ✓ Good — Framework resonated |
| IRIS-2 as sole case study (v1.0) | Concrete > abstract | ✓ Good — File-path specificity made practices verifiable |
| Pause article for focused presentation | Ship smaller deliverable first | ✓ Good — Shipped v1.0 in single day |
| "Trade-offs are real" core message | Not prescriptive; conscious choice | ✓ Good — Non-prescriptive tone maintained |
| Meta practices as amplifiers, not vertices | Enable positioning, don't pick it | ✓ Good — Avoided workflow/solution confusion |
| 7-part series format | Break long article into digestible weekly posts | ✓ Good — Allows iterative publication |
| Mathematical definition + practitioner translation | Rigor + accessibility | ✓ Good — Ed integral formula bridges academic/practitioner |
| SaaStr incident with direct attribution | Public, well-documented, credible | ✓ Good — Concrete evidence > composite |
| Healthcare example as composite | No public incident, real pattern exists | ✓ Good — Shows universality without attribution risk |
| Close v2.0 with known gaps | Articles 1-2 published, articles 3-7 need fresh scope | — Pending (v3.0 will address) |

---
*Last updated: 2026-03-14 after v2.0 milestone completion*
