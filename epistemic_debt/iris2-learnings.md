---
marp: true
theme: default
paginate: true
title: "Trade-offs in LLM-Assisted Development: IRIS-2 Learnings"
---

# Trade-offs in LLM-Assisted Development

## IRIS-2 Learnings

**Conscious Positioning on the Speed/Understanding/Reliability Triangle**

<!--
Speaker notes: Internal Bloomberg team presentation — ~20 minute delivery
-->

---

## The Question

> Ask an engineer in 2020 why their code works:
> "I chose this algorithm because..., implemented it this way because..."

> Ask an engineer in 2025:
> "The LLM suggested it, the tests pass, looks good."

**Same confidence. Different warrant.**

<!--
Speaker notes: Start with this contrast to immediately establish what's at stake.
-->

---

## The Trade-off Triangle

LLM-augmented development exists in three dimensions:

```
                       SPEED
                         ▲
                        / \
                       /   \
                      / ●   \    ← Vibe Coding
                     / / \   \
                    / ↙   ↘   \
                   /DDD   TDD  \  ← Strategy forces
                  /   ↘   ↙     \
                 /      ●        \
                /   Balanced      \
               /      Zone         \
              ▼────────────────────▼
       UNDERSTANDING          RELIABILITY
```

**Each guardrail pulls toward specific corners.**

<!--
Speaker notes: Introduce this as a mental model for trade-off decisions.
-->

---

## IRIS-2 as Case Study

Real project where Trade-off Triangle practices were developed:

- **Understanding pull:** DDD with bounded contexts
- **Reliability pull:** Human-authored E2E tests
- **Speed enabler:** Structured workflow (GSD)

**Result:** Conscious positioning in lower-triangle zone

<!--
Speaker notes: Briefly introduce IRIS-2 as concrete example; detailed practices come in vertex slides.
-->

---

## Understanding Vertex: DDD in Practice

**Bounded contexts** — 5 glob-activated context files:
- `.cursor/rules/*.mdc` (general, experiments, datasets, cli, application, testing)
- Each activates based on working directory

**Ubiquitous language** — Domain types in code:
- `constants.py`: `EvaluatorTypes`, `DatasetFiles`
- LLM output uses domain vocabulary, not generic names

**Business rules as constraints** — Enforced in context:
- `experiments.mdc`: "Experiment MUST have control variant"

**Key insight:** LLM output aligns with domain, not just syntax.

<!--
Speaker notes: Glob activation means LLM sees only relevant context for current work. Example: editing experiment code loads experiments.mdc with business rules. This pulls toward Understanding vertex — slower to set up initially, but LLM suggestions respect domain boundaries.
-->

---

## Reliability Vertex: Breaking Circular Validation

**Human-authored E2E test** — The circular validation breaker:
- `tests/integration/test_user_journey_e2e.py` (972 lines)
- Full user workflow: import dataset → run experiment → download results
- Human intent captured end-to-end

**Mock boundaries defined** — Where to stop testing:
- `testing.mdc` defines integration vs unit scope
- Explicit rule: "Do NOT Over-Generate Tests"

**Key insight:** Human-written integration tests verify LLM-generated code, not vice versa.

<!--
Speaker notes: Why E2E tests break circular validation — if LLM writes both code and tests, tests validate LLM's mental model of correctness, not actual requirements. A human-authored E2E test encodes real workflow understanding, catching when LLM-generated code drifts from intent. This is the Reliability pull — takes human effort to write, but provides epistemic ground truth.
-->

---

## Speed Vertex: Structured LLM Interaction

**Custom workflow commands** — Repeatable LLM patterns:
- `.cursor/commands/` (5 commands)
- `prdescription.md`: Generate structured PR descriptions
- `verifyeventuallyfix.md`: Verification-before-fix workflow

**LOC metrics** — Track LLM vs human contributions:
- PR descriptions include "Pure Code Added" column
- Visibility into what LLM generates vs human writes

**Verification-first workflow** — Prevents solutioning trap:
- Run tests → analyze failures → then fix
- Structure enables speed without sacrificing rigor

<!--
Speaker notes: These custom commands are now superseded by GSD workflow (broader applicability, not project-specific). But the principle holds — structured LLM interaction enables speed by making common tasks repeatable. The verification-before-fix pattern came from here: force yourself to understand the problem before asking LLM for solution.
-->

---

## Meta: Workflow as Amplifier

**GSD workflow** — Systematic successor to custom commands:
- Phases, plans, autonomous execution with checkpoints
- Positioned as amplifier, not a vertex choice

**Multi-AI sync** — Context coherence across tools:
- `scripts/sync-ai-instructions.sh` keeps Claude and Cursor aligned
- Solved context drift problem (changes in one AI not visible to other)

**Key insight:** Workflow doesn't pick a vertex — it enables conscious positioning.

Meta practices amplify all three vertices, they don't replace conscious choice.

<!--
Speaker notes: GSD is post-IRIS-2 learning — evolved from project-specific commands into general workflow. Multi-AI sync addresses epistemic boundary problem: when you have multiple AI tools, keeping their context synchronized prevents divergence. These are amplifiers because they make it easier to maintain whatever position you choose on the triangle — better DDD context, more reliable test generation, faster iteration cycles. They don't solve the trade-off, they help you execute your chosen position more effectively.
-->
