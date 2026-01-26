# Roadmap: Epistemic Debt Article & Presentation

**Created:** 2026-01-26
**Milestones:** 2 (Article, Presentation)
**Phases:** 8 total

---

## Milestone 1: Complete Article

### Phase 1: Opening & Framing
**Goal:** Establish the epistemic shift thesis with an accessible, compelling opening

**Requirements:** OPEN-01, OPEN-02, OPEN-03

**Success Criteria:**
1. Reader understands the 2020 vs 2025 contrast within first paragraph
2. "Epistemic warrant" is defined without philosophy jargon
3. Construction → Curation shift is clear and memorable
4. Tone is exploratory, not alarmist

**Depends on:** None

**Plans:** 1 plan

Plans:
- [ ] 01-01-PLAN.md — Draft Section I with 2020/2025 hook and epistemic shift thesis

---

### Phase 2: Core Concepts
**Goal:** Define epistemic debt and the solutioning trap with concrete grounding

**Requirements:** CORE-01, CORE-02, CORE-03, CORE-04

**Success Criteria:**
1. Technical debt comparison table is clear and useful
2. At least one vivid "default event" scenario (what crisis looks like)
3. Solutioning trap explained with recognizable behavior pattern
4. Velocity vs. ownership framed as trade-off, not binary

**Depends on:** Phase 1 (framing established)

---

### Phase 3: SDLC Analysis
**Goal:** Show where epistemic debt accumulates across three boundaries

**Requirements:** SDLC-01, SDLC-02, SDLC-03

**Success Criteria:**
1. Intent → Spec boundary has concrete "vibe requirements" example
2. Spec → Implementation boundary shows subtle misalignment scenario
3. Implementation → Validation boundary demonstrates circular validation problem
4. Each boundary shows: risk, manifestation, debt accumulated

**Depends on:** Phase 2 (debt concept defined)

---

### Phase 4: Guardrails
**Goal:** Present practices worth examining without being prescriptive

**Requirements:** GUARD-01, GUARD-02, GUARD-03, GUARD-04

**Success Criteria:**
1. DDD mechanism clear: ubiquitous language (bounded Contexts, DDD Patterns lexicon defining them well build, codebase reflect it) → LLM constraint (path based rules for context engineering) → verification
2. E2E testing (human wrote or verified to avoid circularity) positioned against circular validation risk
3. PR review transformation has 4 concrete validation criteria
4. [Optional] At least 2 additional practices explored (ADRs, documentation, pair programming) - Do preliminary research on existing online literature to understand what is already out there.
5. Frame maintained: "worth examining" not "you must do this"

**Depends on:** Phase 3 (boundaries where guardrails apply)

---

### Phase 5: Measurement

Sacrificable phase for word count. If the article is too long, this can be removed or minimized.

**Goal:** Honestly address how we'd know epistemic debt is accumulating

**Requirements:** MEAS-01, MEAS-02, MEAS-03, MEAS-04

**Success Criteria:**
1. Bug/incident metrics presented as possible indicators
2. "Knowledge loss velocity" concept is clear and memorable
3. Code archaeology costs quantified conceptually
4. Difficulty of measurement honestly acknowledged
5. Section positioned as most exploratory/open

**Depends on:** Phase 4 (context for what we're measuring against)

---

### Phase 6: Conclusion
**Goal:** Reframe the debate and land with appropriate emotional tone

**Requirements:** CONCL-01, CONCL-02, CONCL-03

**Success Criteria:**
1. Explicit pivot from "replacement" to "practices" framing
2. Paradox articulated: LLMs expose problems + make them worse
3. Emotional landing chosen and executed (document decision)
4. Call to action is clear but not preachy

**Depends on:** Phases 1-5 (all content complete)

---

### Phase 7: Polish & Quality
**Goal:** Article ready for publication

**Requirements:** QUAL-01, QUAL-02, QUAL-03, QUAL-04

**Success Criteria:**
1. Zero [GAP] or [EXAMPLE NEEDED] markers remain
2. References section has at least 3-5 citations
3. Word count is 3500-6000 words
4. Front-matter dates and status updated
5. Passes CLAUDE.md style guidelines check

**Depends on:** Phase 6 (all content drafted)

---

## Milestone 2: Presentation

### Phase 8: Presentation Transformation

This presentation is for internal Bloomberg team meeting. More technical than the article per se and with concrete examples and calls to action.

**Goal:** Article adapted to 10-20 slides presentation with visuals centered on concrete projects with calls to action.

**Requirements:** PRES-01, PRES-02, PRES-03, VIS-01, VIS-02, VIS-03, ADAPT-01, ADAPT-02, ADAPT-03

**Success Criteria:**
1. 10 slides in valid Marp format
2. Epistemic boundaries diagram exists (text-based or described)
3. Debt accumulation comparison visualized
4. Key phrases from article as slide headlines
5. Speaker notes on at least 5 key slides
6. Narrative arc works for 20 minute delivery

**Depends on:** Milestone 1 complete (Phase 7)

---

## Summary

| Phase | Name | Requirements | Dependencies |
|-------|------|--------------|--------------|
| 1 | Opening & Framing | OPEN-01, OPEN-02, OPEN-03 | None |
| 2 | Core Concepts | CORE-01, CORE-02, CORE-03, CORE-04 | Phase 1 |
| 3 | SDLC Analysis | SDLC-01, SDLC-02, SDLC-03 | Phase 2 |
| 4 | Guardrails | GUARD-01, GUARD-02, GUARD-03, GUARD-04 | Phase 3 |
| 5 | Measurement | MEAS-01, MEAS-02, MEAS-03, MEAS-04 | Phase 4 |
| 6 | Conclusion | CONCL-01, CONCL-02, CONCL-03 | Phases 1-5 |
| 7 | Polish & Quality | QUAL-01, QUAL-02, QUAL-03, QUAL-04 | Phase 6 |
| 8 | Presentation | PRES-*, VIS-*, ADAPT-* | Phase 7 |

**Milestone 1 (Article):** Phases 1-7
**Milestone 2 (Presentation):** Phase 8

---
*Roadmap created: 2026-01-26*
