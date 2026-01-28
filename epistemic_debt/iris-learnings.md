---
marp: true
theme: default
paginate: true
title: "Trade-offs in LLM-Assisted Development: IRIS Learnings"
---

# Trade-offs in LLM-Assisted Development

## IRIS Learnings

**Conscious Positioning on the Epistemic Debt/AI Blazing Speed/Quality Triangle**



<!--
Speaker notes: Internal Bloomberg team presentation — ~20 minute delivery
-->

---

## The Question

> Ask an engineer in 2020 why their code works:
> "I chose this algorithm because..., implemented it this way because..."

> Ask an engineer in 2025:
> "The LLM suggested it, the tests pass, looks good. Can you please review this 5,000 LOC PR?"

**Same confidence. Different warrants and (epistemic) debt.**

---

## The Epistemic Credit - Speed - Quality Triangle

**Three vertices in tension:**

```
                   EPISTEMIC CREDIT
                           ▲
                          / \
                         /   \
           Understanding/     \
                 Zone  /       \
                      /    ●    \    ← Balance Point
                     /   Ideal   \
                    /             \
                   /  ↙   TDD  ↘   \
                  / DDD         E2E \
                 /                   \
        Velocity/                   \Correctness
          Zone /                     \  Zone
              /                         \
              ▼───────────────────────────▼
           SPEED                       QUALITY
```

**Key relationships:**
- **Epistemic Credit ↔ Speed**: Trade-off (inverse)
- **Speed ↔ Quality**: Tension (can conflict)
- **Quality ↔ Epistemic Credit**: Synergy (mutually reinforcing)

---

## Defining Epistemic Credit

**Epistemic Credit (Ce)** is the accumulated surplus of cognitive understanding over system complexity:

$$Ce = \int_{0}^{T} (Gc(t) - Cs(t)) \, dt$$

Where:
- **Gc(t)** = Cognitive Grasp of the team at time t
- **Cs(t)** = System Complexity at time t

**Context matters**: Same practice yields different epistemic outcomes depending on domain complexity and team grasp.

*Source: Ngabang (2026), "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering"*

<!--
Speaker notes: Unlike simple "understanding," Epistemic Credit is relative to system complexity. A 1000-line codebase you fully understand has high credit. A 10,000-line codebase you partially understand might have the same or lower credit. It's the delta that matters.
-->

---

## IRIS 1.0: Development Metrics

** Almost-Solo development with disciplined AI assistance:**

| Metric | Value | Context |
|--------|-------|---------|
| **Time to Production** | 2 months | Would have taken 4-6 months without AI assistance |
| **Velocity** | ~5,000 LOC/week | vs. typical 400-800 LOC/week baseline from studies |
| **Test Ratio** | ~40% of codebase | Excluding comments |
| **Coverage** | >85% | Including 30+ real E2E integration tests |

**How**: Structured AI-assisted workflow with strong guardrails, domain modeling, continuous validation (pre-push hooks), and tight feedback loops.

**Result**: Conscious positioning in mid/lower-triangle zone (epistemic credit + quality emphasis).

<!--
Speaker notes: These numbers demonstrate that high velocity AND high quality AND maintainable understanding are achievable together—but require deliberate practices. This wasn't "vibe coding" at 5K LOC/week; it was structured workflow enabling sustainable speed.
-->

---

## Epistemic Credit Vertex: DDD in Practice

**Bounded contexts** — 5 glob-activated context files:
- `.cursor/rules/*.mdc` (general, experiments, datasets, cli, application, testing)
- Each activates based on working directory

**Ubiquitous language** — Domain types in code:
- `constants.py`: `EvaluatorTypes`, `DatasetFiles`
- LLM output uses domain vocabulary, not generic names

**Business rules as constraints** — Enforced in context:
- `experiments.mdc`: "Experiment MUST have control variant"

**Impact**: LLM output aligns with domain boundaries → raises Gc(t) faster than Cs(t) grows → positive epistemic credit accumulation.

<!--
Speaker notes: Glob activation means LLM sees only relevant context for current work. Example: editing experiment code loads experiments.mdc with business rules. This pulls toward Epistemic Credit vertex—slower to set up initially, but LLM suggestions respect domain boundaries. You understand the output because it speaks your domain language.
-->

---

## Quality Vertex: Breaking Circular Validation

**Human-authored E2E test** — The circular validation breaker:
- `tests/integration/test_user_journey_e2e.py` (972 lines)
- Full user workflow: import dataset → run experiment → download results
- Human intent captured end-to-end

**Mock boundaries defined** — Where to stop testing:
- `testing.mdc` defines integration vs unit scope
- Explicit rule: "Do NOT Over-Generate Tests"

**Impact**: Human-written integration tests verify LLM-generated code, not vice versa → Quality ↔ Epistemic Credit synergy.

<!--
Speaker notes: Why E2E tests break circular validation—if LLM writes both code and tests, tests validate LLM's mental model of correctness, not actual requirements. A human-authored E2E test encodes real workflow understanding, catching when LLM-generated code drifts from intent. This demonstrates the Quality/Epistemic Credit synergy: good tests both verify correctness AND serve as living documentation that builds understanding.
-->

---

## Speed Vertex: Structured LLM Interaction

**Initial custom workflow commands** (IRIS 1.0):
- `.cursor/commands/` (5 commands)
- `prdescription.md`: Generate structured PR descriptions
- `verifyeventuallyfix.md`: Verification-before-fix workflow

**LOC metrics** — Track LLM vs human contributions:
- PR descriptions include "Pure Code Added" column
- Visibility into what LLM generates vs human writes

**Evolution to GSD** (post-IRIS 1.0):
- Leo pointed out the Get Shit Done (GSD) workflow
- Broader applicability than project-specific commands
- Now adopted in IRIS and other projects
- Phases, plans, autonomous execution with checkpoints

**Impact**: Verification-first workflow prevents solutioning trap → enables speed without sacrificing rigor.

<!--
Speaker notes: The custom commands were a stepping stone. They established the pattern: structure LLM interaction explicitly rather than ad-hoc prompting. GSD generalizes this—systematic workflow for any project. The verification-before-fix pattern (run tests → analyze failures → then fix) came from this work. It forces you to understand the problem before asking LLM for a solution. This is Speed vertex work: making repetitive tasks fast while maintaining quality gates.
-->

---

## Meta: Workflow as Triangle Amplifier

**Multi-AI context sync** — Context coherence across tools:
- `scripts/sync-ai-instructions.sh` keeps Claude and Cursor aligned
- Solved context drift problem (changes in one AI not visible to other)

**GSD workflow** — Systematic approach:
- Phases, plans, autonomous execution with checkpoints
- Not a vertex choice—an amplifier of all three vertices

**Key insight**: Meta practices don't pick a position on the triangle—they enable more effective execution of whatever position you choose.

- Better DDD context → Amplifies epistemic credit
- More reliable test generation → Amplifies quality
- Faster iteration cycles → Amplifies speed

<!--
Speaker notes: Multi-AI sync addresses epistemic boundary problem: when you have multiple AI tools, keeping their context synchronized prevents divergence. GSD evolved from IRIS learnings into a general workflow. These are amplifiers because they make it easier to maintain whatever position you choose on the triangle. They don't solve the fundamental trade-offs, they help you execute your chosen position more effectively.
-->

---

## Key Takeaways

**Conscious positioning on the triangle:**

1. **Bounded contexts as guardrails** — Glob-activated context files (`.cursor/rules/*.mdc`) ensure LLM output aligns with domain boundaries. Raises Gc(t) relative to Cs(t). *Pull: Epistemic Credit.*

2. **Human E2E tests break circular validation** — One comprehensive integration test (`test_user_journey_e2e.py`) validates LLM-generated code against real user workflow. *Pull: Quality. Synergy: Epistemic Credit through living documentation.*

3. **Verification-before-fix workflow** — Structure LLM interaction with explicit phases (run tests → analyze → then fix). Prevents solutioning trap. *Pull: Speed with quality gates.*

4. **Multi-AI context sync** — When using multiple AI tools (Claude, Cursor), synchronize their context explicitly to prevent divergence. *Amplifies all vertices.*

**Trade-offs are real choices.** Pick your position deliberately based on domain context.

---

## References

**Primary theoretical framework:**
- Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." *ViXra*, January 2. https://vixra.org/pdf/2601.0013v1.pdf
  - Defines epistemic debt as De = ∫(Cs(t) - Gc(t))dt
  - Proposes "Cognitive Ratchet" methodology

**Related work on epistemic debt:**
- Ionescu, T.B., Schlund, S., Schmidbauer, C. (2020). "Epistemic Debt: A Concept and Measure of Technical Ignorance in Smart Manufacturing." *Springer*.
- "Epistemic Opacity, Confirmation Holism and Technical Debt: Computer Simulation in the Light of Empirical Software Engineering." *Springer*.
- Codemanship. "Comprehension Debt: The Ticking Time Bomb of LLM-Generated Code." https://codemanship.wordpress.com/2025/09/30/

**IRIS project context:**
- Internal Bloomberg IRIS 1.0 deployment metrics and practices
- Get Shit Done (GSD) workflow documentation

---


<!--
Speaker notes: These references ground the talk in both academic theory (Ngabang's formalization) and practical reality (IRIS metrics). The triangle framework synthesizes multiple sources into an actionable mental model.
-->
