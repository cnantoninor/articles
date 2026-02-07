# Phase 12: Epistemic Debt Definition (Section II) - Context

**Gathered:** 2026-02-07
**Status:** Ready for planning

<domain>
## Phase Boundary

Establish epistemic debt as a distinct concept through:
- Mathematical definition (Ed = ∫[0 to T] (Cs(t) - Gc(t)) dt) with proper attribution
- Comparison framework distinguishing it from technical debt
- 3 dramatic "default events" showing real consequences
- Quantified industry data (breach rates, outage increases, cost multipliers)

This section sets the foundation for the article's argument. Mechanism of debt accumulation (Phase 13), boundary failures (Phase 14), and the Triangle framework (Phase 15) are separate phases.

</domain>

<decisions>
## Implementation Decisions

### Tone & Positioning
- **Opening hook**: Provocative question format (e.g., "Your tests are passing. Your code works. So why can't anyone explain how?")
- **Voice balance**: Practitioner-first throughout — lead with visceral reality developers face, then back with data. "You've felt this" before "here's the research"
- **Mathematical definition**: Lead with math — introduce Ed = ∫[Cs(t) - Gc(t)]dt upfront as rigorous foundation, then explain in practitioner terms
- **Term introduction**: Novel term in Software Engineering, but mathematically grounded. Present the integral formulation with footnoted attribution to nbang article and research foundations

### Example Selection
- **Type**: Cross-industry mix — 3 composite examples spanning different domains (fintech, healthcare, tech). Shows universality
- **Technical detail**: Technical specificity — include enough detail that practitioners recognize the pattern (e.g., "The OAuth callback validation..."). Credible to engineers
- **Attribution**: Composite examples synthesized from real incident patterns, not named companies. Captures reality without singling out specific parties
- **Primary lens**: Technical failure mode — center on the epistemic gap itself: what wasn't understood, how that manifested, why normal processes didn't catch it

### Comparison Structure
- **Format**: Comparison table (side-by-side Tech Debt vs Epistemic Debt)
- **Dimensions**: 5 rows:
  1. What accumulates (code quality issues vs understanding gaps)
  2. What pays it down (refactoring vs learning/documentation)
  3. Visibility & measurement (code metrics vs bus factor/onboarding pain)
  4. Consequences of default (maintenance burden vs catastrophic blind spots)
  5. Speed of accumulation (gradual vs sudden with AI assistance)
  - Claude's discretion: Add "Who it affects" dimension if it strengthens the distinction
- **Cell style**: Terse phrases — scannable, relies on surrounding text for depth

### Data Integration
- **Citation style**: Footnoted extensively — present claims cleanly in main text, move all citations and supporting data to footnotes
- **Quantified claim density**: Sparse but memorable — 1-2 shocking numbers that stick (e.g., "doubled", "tripled"). Let those carry the weight, keep rest narrative
- **Mathematical definition attribution**: Footnoted origins — present definition cleanly in main text, provide full attribution to nbang paper in footnote
- **Research studies**: Studies in footnotes only — main text makes claims (e.g., "40% of AI-generated suggestions..."), footnotes cite studies

### Claude's Discretion
- Whether to add "Who it affects" dimension to comparison table
- Exact phrasing of provocative opening question
- Selection of which composite examples from available research
- Calibration of technical detail depth per example
- Additional dimensions in comparison table if they strengthen distinction
- Placement of data to maximize argument effectiveness

</decisions>

<specifics>
## Specific Ideas

**Mathematical foundation:**
- Core formula: Ed = ∫[0 to T] (Cs(t) - Gc(t)) dt
  - Where Ed = Epistemic Debt
  - Cs(t) = System Complexity at time t
  - Gc(t) = Cognitive Grasp of the team at time t
- Source: nbang article (mathematical definition) in /home/arau6/projects/ai-articles/epistemic_debt/references/
- Related: Epistemic Credit (Ce) as inverse — accumulated surplus of understanding over complexity

**Research context:**
- References folder contains: Epistemic Debt Research Complete.pdf, literature-review-on-epistemic-debt.md, and supporting papers (paper1-5.pdf)
- Research provides backing for breach rates, incident data, and cost multipliers
- Epistemic_debt_definition.md has the formal mathematical treatment

**Tone examples:**
- "You've felt this" before "here's the research" — practitioner visceral experience first
- Opening should challenge assumptions about passing tests = understanding
- Make reader recognize epistemic debt in their own experience before defining it

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope. The solutioning trap mechanism (Phase 13), SDLC boundaries (Phase 14), and Triangle framework (Phase 15) are properly sequenced in separate phases.

</deferred>

---

*Phase: 12-epistemic-debt-definition-section-ii*
*Context gathered: 2026-02-07*
