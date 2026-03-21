---
title: The Trade-off Triangle
subtitle: A framework for conscious positioning in LLM-augmented development
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 2090
current_length: 2470
estimated_reading_time: 10 min
created: 2026-02-15
last_updated: 2026-02-15
published_date: null
publication_url: ''
social_teasers:
  linkedin: ''
  twitter: ''
  instagram_caption: ''
  substack_notes: ''
---








# The Trade-off Triangle

*A framework for conscious positioning in LLM-augmented development*

---

*This is Part 5 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

The patterns described in the previous articles — epistemic debt accumulation, the solutioning trap, boundary failures — share a common structure. The case studies in [When Epistemic Debt Defaults]([ARTICLE_URL]) — a production database deleted by an AI agent, a team's 200-hour savings becoming 2,000 hours of remediation — are what these trade-offs look like when the Speed corner is chosen by default rather than by design. They all involve trade-offs between three competing qualities. Understanding these trade-offs requires a framework.

## The Universal Triangle

LLM-augmented development exists in a three-dimensional trade-off space:

- **Speed** — How fast can we ship?
- **Understanding** — Do we have epistemic ownership of the code?
- **Reliability** — Does the code actually work correctly?

```
                    UNDERSTANDING
                   (Epistemic Credit)
                        ▲
                       /·\
                      / · \
                     / · \
                    / ● \         ← Unguarded AI Use
                   / /·\ \         (Pure Vibe Coding)
                  / / · \ \
                 / / · \ \
                / ↙   · ↘ \
               / DDD · TDD \       ← Strategy forces
              / ║     · ║   \       pull toward corners
             / ║     · ║ ╳ \
            / ║     · ╳   \     ← ╳ TRAP: Circular
           / ↘     · ↙     \       Validation
          / ↘   · ↙       \
         / ↘ ● ↙         \
        /   Conscious       \
       /   Trade-off         \
      /   Zone                \
     ▼────────────●────────────▼
   SPEED      ↑    RELIABILITY
  (Velocity)  │   (Verified Correctness)
              │
         Human Review
        (pulls to both)
```

Reading the triangle:

- **Corners** represent the three qualities you can optimize for
- **Position** shows what you're trading off
- **Arrows** show how strategies shift your position
- **╳** marks traps that give false confidence

The key relationships between vertices:

- **Understanding ↔ Speed:** Tension. Inverse trade-off — deeper understanding takes time.
- **Speed ↔ Reliability:** Tension. Can conflict — shipping fast may skip verification.
- **Reliability ↔ Understanding:** Synergy. Mutually reinforcing — understanding helps you verify; verification deepens understanding.

The critical insight: **you cannot maximize all three simultaneously.** Every LLM interaction involves a positioning choice — whether you make it consciously or not. Unguarded AI use ("vibe coding") defaults to the Speed corner. The debt accumulates in the Understanding and Reliability corners.

## The Circular Validation Trap

Before discussing the strategies that pull you toward understanding and reliability, we need to address a failure mode that masquerades as verification. This is the third SDLC boundary from Article 4 — Implementation → Validation — and it deserves special attention because it's so deceptive.

When LLMs generate both code and tests, the tests inherit the same blind spots as the code. The system *appears* verified — coverage is high, tests pass — but the reliability is illusory. The tests validate that the code matches itself, not that the code matches intent. IBM Research has identified the broader version of this problem — what IBM Fellow Kush Varshney calls "validating validators": in any feedback system where AI evaluates its own output, errors get amplified rather than corrected. What I'm calling *circular validation* is a specific manifestation in code testing: the closed loop between generated code and generated tests.

A developer generates an API endpoint using an LLM. They then ask the same LLM: "Write tests for this endpoint." The LLM produces unit tests that achieve 95% coverage. Every test passes. The developer, seeing high coverage and green checks, gains confidence the code is correct.

But examine what happened. The LLM generated code that embodies certain assumptions about input handling. Then the same LLM generated tests that validate those same assumptions. If the code mishandles null values in a specific edge case, the tests won't check for that edge case either — because both code and tests share the same blind spots.

Here's what this looks like concretely:

```python
# LLM generates validation function:
def validate_email(email):
    return '@' in email and '.' in email.split('@')[1]

# LLM generates tests:
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False
    assert validate_email("test@com") == True  # This should FAIL — but doesn't
```

The tests pass. Coverage is 100%. But the validation logic is wrong — it accepts "test@com" which lacks a valid domain. The LLM-generated tests also miss this edge case because they share the same blind spots.

**Detection method:** Ask a simple question: "Could I explain to a new team member exactly what edge cases these tests cover and why?" If the answer is "I'd have to read the tests carefully first," you're in circular validation territory.

### How Boundaries Compound

The three SDLC boundaries don't fail independently — they compound. A vague specification (Boundary 1, from Article 4) produces code with implicit assumptions (Boundary 2, from Article 4), which gets validated by tests that share those assumptions (Boundary 3, above). The result is a system that appears correct at every checkpoint but is built on an unexamined foundation.

"Build me a dashboard" → LLM generates dashboard with generic metrics → LLM generates tests that verify the generic metrics display correctly → all tests pass → nobody questions whether the metrics are the right ones. Each boundary crossing added epistemic debt, and each subsequent crossing inherited the debt from the previous one.

## Strategy Forces

The triangle isn't just diagnostic — it suggests specific practices that pull your development toward the vertices you care about. Here are four, examined through the lens of a real project.

### IRIS-2: The Concrete Example

IRIS-2 is an internal IR experimentation platform built with approximately 90% AI assistance over two months. It serves 20-40 users with complex workflows including LLM-as-judge evaluation components. It shipped at roughly 5,000 LOC per week — compared to a typical 400-800 — with over 85% test coverage. It is the proving ground for the practices described below.

### Domain-Driven Design → Understanding

IRIS-2 used five bounded contexts, each with glob-activated context files (`.cursor/rules/*.mdc`). When the developer worked on experiment logic, the LLM loaded `experiments.mdc` with business rules: "Experiment MUST have control variant." When working on datasets, `datasets.mdc` defined the domain vocabulary. A centralized ubiquitous language (`constants.py` defining `EvaluatorTypes`, `DatasetFiles`) ensured the LLM used domain terms, not generic names.

**The mechanism:** DDD front-loads epistemic work into domain modeling. When the team has a precise shared vocabulary — "aggregate root," "bounded context," "domain event" — the LLM's output can be verified against that vocabulary. Does this code express our domain concept? DDD is ontological and lexicon-based, making it a natural fit for lexicon-based prediction machines like LLMs.

Eric Evans, the creator of DDD, has encouraged practitioners to experiment with LLMs, noting that domain modeling creates a vocabulary that constrains and validates AI output. When domain models are well-defined, LLMs can operate within those constraints rather than hallucinating abstractions.

**Impact on the triangle:** DDD pulls toward Understanding because it forces LLM output to align with domain boundaries. Cs(t) still grows as code is generated, but Gc(t) grows faster because every generated line speaks the team's language. The result is epistemic credit accumulation even at high velocity.

**Limitation:** What prevents teams from using LLMs to skip domain modeling too? If the LLM generates both the domain model and the implementation, circular validation emerges at a higher level.

### Human-Authored E2E Tests → Reliability

IRIS-2 had one comprehensive human-authored integration test: `test_user_journey_e2e.py` at 972 lines. It encoded the complete user workflow: import dataset → configure experiment → run evaluation → download results. This test was written by a human, not generated by an LLM.

**The mechanism:** Human-authored tests break circular validation. The E2E test encodes human understanding of what "correct" means. LLM-generated unit tests can safely fill in the details because they're constrained by the human-defined integration boundary. Unlike unit tests, which risk testing that the code matches itself, E2E tests verify that the system does what users actually need.

**Impact on the triangle:** TDD pulls toward Reliability by verifying correctness against human intent. The synergy with Understanding is significant — a well-written E2E test also serves as living documentation of the system's intended behavior.

### Human-in-Loop Review → Both

Code review in the LLM era must shift from line-by-line correctness to epistemic validation. The question changes from "does this code work?" to "can the PR author explain this code?"

What PR review should validate:

1. **Intent clarity** — Does the engineer understand WHAT they're building and WHY?
2. **Epistemic ownership** — Can they explain HOW the code works, regardless of who wrote it?
3. **Test quality** — Do tests validate intent, not just implementation?
4. **Architectural coherence** — Does it fit the system, not just work in isolation?

Reviewers should focus on architectural coherence — does it respect system invariants? — rather than defensive coding patterns, which LLMs handle reliably. The shift is from policing the code to ensuring the team understands the code.

**Risk:** Rubber-stamping. If the reviewer doesn't understand the code either, review becomes ceremony rather than checkpoint.

### Structured Workflows → Amplifies All

IRIS-2 developed custom workflow commands (`.cursor/commands/`) including a verification-before-fix pattern: run tests, analyze failures, then ask the LLM for a fix. This prevents the solutioning trap by forcing diagnosis before solution. LOC tracking in PR descriptions ("Pure Code Added" column) made AI contribution visible.

This pattern evolved into a systematic workflow — research → plan → execute → verify — with human gates between phases. Each phase runs in a fresh context, preventing context window amnesia.

**The key workflow elements and their effects:**

| Workflow Element | Epistemic Debt Reduction |
|---|---|
| Bite-sized prompts | LLM output stays within human comprehension |
| Context-focused tasks | Reduces "unknown unknowns" from context amnesia |
| Atomic commits | Each change is small enough to verify |
| Phase checkpoints | Forces human understanding before proceeding |
| Persistent state files | Makes progress visible, prevents drift across sessions |

A structured workflow doesn't just add another arrow to the triangle — it makes the lower-triangle zones accessible without sacrificing too much speed. The key: structure enables conscious positioning rather than defaulting to the Speed corner.

**Limitation:** Workflow overhead. Best suited for substantial features rather than quick fixes.

[TODO: Connect each strategy force back to the t₀ and break-even formula from Article 2. DDD shifts t₀ leftward at L3-L4 (architectural/requirements gaps surface during domain modeling). Human-authored E2E tests shift t₀ leftward at L1-L2 (integration failures surface before production). Structured workflows create multiple t₀ checkpoints across all layers. Frame the strategies as deterministic mechanisms that keep Σ_k c_k · τ_k < δ — preserving AI speed advantage while bounding debt risk. Consider adding a column to the strategy summary table showing which abstraction layer (L1-L4) each strategy primarily guards.]

### The Strategy Forces Summary

| Strategy | Primary Pull | Effect on Epistemic Debt | Risk/Trap |
|---|---|---|---|
| DDD (ubiquitous language) | → Understanding | Builds ownership, aligns AI output | Terminology drift if not enforced |
| TDD (esp. integration tests) | → Reliability | Verifies correctness, slight ownership gain | Circular validation if LLM-generated |
| Human-in-loop review | → Both | Ensures alignment + catches blind spots | Rubber-stamping if reviewer doesn't understand |
| Structured Workflow | Amplifies all | Meta-strategy enabling sustainable AI use | Overhead for small tasks |

## Domain-Based Positioning

[TODO: Introduce the tolerance factor ε_k here, connecting back to Article 2's recovery formula. In Article 2 we derived τ_k = (Cs_k - Gc_k(t₀)) / r_k assuming the gap must be fully closed. Here, with DDD subdomain classification providing the motivation, introduce ε_k as a tolerance threshold so the recovery target becomes Gc_k(τ) = Cs_k - ε_k, yielding τ_k = (Cs_k - Gc_k(t₀) - ε_k) / r_k. Core domains → ε_k ≈ 0 (full understanding required). Supporting domains → moderate ε_k. Generic domains → large ε_k (strategic ignorance is economically rational). This formalizes the "not all code deserves equal epistemic investment" argument mathematically and closes the seed planted in Article 2.]

Not all code deserves equal epistemic investment. The triangle maps naturally to DDD's subdomain classification:

**Core domains** (competitive advantage, security-sensitive, long-lived):
Lower-triangle positioning — DDD + TDD + Human Review. Errors have highest business impact. Epistemic debt = existential risk. In IRIS-2: experiment execution logic got bounded contexts + human E2E tests.

**Supporting domains** (enables core, internal tools):
Mid-triangle positioning — at least one of DDD or TDD. Balance speed with some guardrails. Failures are recoverable. In IRIS-2: CLI commands got workflow structure.

**Generic domains** (commodity, boilerplate, CRUD):
Upper-triangle positioning acceptable — minimal or no specific strategies. Speed may outweigh deep understanding. Well-established patterns, low risk. In IRIS-2: utility functions were pure LLM output with basic review.

Epistemic debt, like technical debt, can be a deliberate trade-off. The triangle provides visual language for these conversations: "We're operating upper-triangle on this module — speed priority, we accept the epistemic debt." "This is core domain — we need lower-triangle positioning."

## Practitioner Takeaways

1. **Know your position on the triangle.** Before starting any significant work, ask: "Are we optimizing for Speed, Understanding, or Reliability here?" Make the choice explicit.

2. **Match practices to domain criticality.** Core business logic needs lower-triangle positioning. Supporting code can operate mid-triangle. Generic boilerplate can tolerate the Speed corner. Not all code needs equal epistemic investment.

3. **Break circular validation.** If LLMs generate both your code and your tests, you have false confidence. Write at least one comprehensive integration test by hand. Define what "correct" means before generating implementations.

4. **Measure understanding, not just output.** Add epistemic health indicators to your team's metrics: bus factor trends, onboarding velocity, incident diagnosis time. They won't give you a precise number, but they'll show you the trend.

5. **Invest in structured workflow.** The friction of discuss → plan → execute → verify isn't overhead — it's the mechanism that maintains understanding at velocity. Unstructured LLM use defaults to the Speed corner. Structure enables conscious positioning.

---

*Next in the series: **Measuring the Unmeasurable** — proxy indicators, honest caveats, and what we don't yet know about quantifying epistemic debt.*

---



---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe for **free**](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- IRIS-2 project (internal case study)
- Thoughtworks (2025). "Spec-Driven Development."
- Evans, E. Domain-Driven Design references.
- Yang, E. "Code Review as Human Alignment in the Era of LLMs."
- Pan, Q., Ashktorab, Z., Desmond, M., et al. (2024). "Human-Centered Design Recommendations for LLM-as-a-Judge." IBM Research. arXiv:2407.03479. https://arxiv.org/abs/2407.03479
- IBM Think (2025). "Who watches the AI watchers? The challenge of self-evaluating AI." https://www.ibm.com/think/news/ai-testing-advances
- GSD framework documentation.
- Ngabang, L.A. (2026). "The Illusion of Competence."
