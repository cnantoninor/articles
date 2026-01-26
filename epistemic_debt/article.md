---
title: "Epistemic Debt: The Hidden Cost of LLM-Generated Code"
status: draft
type: article
audience: [engineering leaders, senior engineers, architects, researchers]
target_length: 4000
created: 2026-01-25
last_updated: 2026-01-26
---

# Epistemic Debt: The Hidden Cost of LLM-Generated Code

## Abstract

The integration of Large Language Models into software engineering marks a fundamental shift in how developers relate to their code. This article introduces "epistemic debt"—code that works but nobody understands—as a lens for examining the risks of LLM-augmented development. We explore how the shift from construction to curation changes the nature of developer understanding, examine where epistemic debt accumulates in the software development lifecycle, and suggest practices worth examining as potential guardrails.

---

## I. The Epistemic Shift

A code review in 2020: The reviewer asks, "Why binary search here?" The engineer responds, "The dataset is sorted, and we need O(log n) lookups. I considered a hash table, but the memory overhead wasn't worth it for our scale, and we need range queries later." The reviewer nods. The reasoning is clear.

A code review in 2025: The same question. The engineer responds, "Claude suggested it. The tests pass—100% coverage. I checked the edge cases I could think of. It handles the main scenarios." The reviewer scans the implementation. It looks professional. The logic seems sound. They approve it.

Same confidence. Different warrant.

The code works. The tests pass. But if you asked the 2025 engineer to explain *why* binary search is correct here, or what assumptions it makes about data distribution, or how it would fail if those assumptions broke, they might hesitate. The code appeared quickly—ten seconds to generate, ten minutes to review. The team moved fast. But something was lost in the velocity: the labor of knowing.

For roughly seventy years, programming has been grounded in deterministic authorship. A human agent with specific intent constructs a logical artifact. Software, in this view, is the crystallization of human reason. The epistemic warrant—the justification for claiming to understand the code—derives from a causal chain of authorship. You know the system because it is the product of your cognitive labor.

LLMs introduce a rupture in this epistemological framework. A probabilistic layer now sits between human intent and machine execution. Code becomes the product of stochastic pattern matching across vast vector spaces rather than direct symbolic reasoning. The developer's role shifts from **construction**—being the architect of every decision—to **curation**—reviewing and selecting from probabilistically-generated suggestions.

The primary risk is not merely technical correctness. It is **epistemic opacity**: the LLM produces what we might call the "feeling of knowing" without the "labor of knowing."

[GAP: How technical/philosophical should this section be for a broad tech audience?]

---

## II. Epistemic Debt: A New Lens

We can think of this accumulated opacity as **epistemic debt**—code that works but nobody understands.

The analogy to technical debt is deliberate. Both involve trade-offs. Both accumulate over time. Both can result in a kind of "default" when they exceed the team's capacity to manage them.

| Technical Debt | Epistemic Debt |
|----------------|----------------|
| Code that works but is hard to change | Code that works but nobody understands |
| Future maintenance cost | Future comprehension cost |
| Visible in code structure | Invisible until crisis |

The critical difference lies in how debt accumulates. Pre-LLM epistemic gaps were **localized** (one Stack Overflow snippet, one library abstraction), **visible** (you knew you copied it), **socially stigmatized** (copy-paste carried a cost), and accumulated **linearly** (natural speed limits from typing and frustration).

Post-LLM epistemic gaps are **pervasive** (entire modules, whole features), **invisible** (feels like collaboration), **socially normalized** (no stigma), and accumulate **exponentially** (velocity removes friction).

[GAP: Concrete examples of epistemic debt "default events" - what does failure look like?]

---

## III. The Solutioning Trap

The core problem is not inexperience or lack of skill. It is **jumping to solutioning without clarifying the epistemic scope of the problem**.

This affects experienced engineers too. LLMs make it trivially easy to generate solutions before understanding the problem. You can spin up an entire feature in an afternoon. The code compiles. The tests pass. Ship it.

But the gap between what the code does and what the team understands compounds silently. This is the **velocity trap**: we can now accumulate epistemic debt much faster than we can pay it down.

The velocity vs. ownership trade-off is not inherently bad. Speed matters. But when velocity consistently outpaces understanding, the debt compounds before teams even notice.

[GAP: What does "clarifying epistemic scope" mean concretely in practice?]

---

## IV. Epistemic Debt in the SDLC

Epistemic debt can accumulate at every boundary where meaning must be translated from one form to another.

### Boundary 1: Intent → Specification

**Risk:** Vibe-based requirements lead to vibe-based design.

A stakeholder says "build me a dashboard." The developer prompts an LLM. Something that looks like a dashboard appears. "Looks good." But the team hasn't clarified what decisions the dashboard should enable, what data is essential, or how users will actually work with it.

**Debt accumulated:** The team doesn't understand user needs—they just have a dashboard.

[EXAMPLE NEEDED: More concrete scenario]

### Boundary 2: Specification → Implementation

**Risk:** Probabilistic drift and subtle misalignment.

The LLM generates code that "mostly" matches the intent. Edge cases are handled in ways the developer doesn't fully understand. The code works for the happy path. The tests pass.

**Debt accumulated:** Nobody can explain why it works (or doesn't) in specific scenarios.

[EXAMPLE NEEDED: Concrete code example showing hidden complexity]

### Boundary 3: Implementation → Validation

**Risk:** Circular validation.

The developer asks the LLM to generate tests for the LLM-generated code. The tests pass. Coverage is high. But the tests don't cross an epistemic boundary—they validate that the code matches the code, not that the code matches the intent.

**Debt accumulated:** False confidence in correctness.

[EXAMPLE NEEDED: Example of circular validation in practice]

---

## V. Possible Guardrails

The following are **practices worth examining**, not prescriptive solutions. Each offers a potential mechanism for restoring epistemic warrant in an LLM-augmented workflow.

### Domain-Driven Design

**Mechanism:** Ubiquitous language creates a shared problem definition that constrains LLM context and provides verification criteria.

DDD front-loads epistemic work into domain modeling. When the team has a precise shared vocabulary—"aggregate root," "bounded context," "domain event"—the LLM's output can be verified against that vocabulary. Does this code express our domain concept?

**Limitation:** What prevents teams from using LLMs to skip domain modeling too?

### E2E Integration Testing

**Mechanism:** End-to-end tests validate behavior against requirements, crossing the epistemic boundary between implementation and intent.

Unlike unit tests, which risk circular validation, E2E tests verify that the system does what users actually need. They're harder to fake because they require understanding the whole system.

**Limitation:** Still requires humans to define what correct behavior looks like.

### Transformed PR Review

**Mechanism:** Shift code review from line-by-line correctness to epistemic validation.

What PR review should validate in the LLM era:
1. **Intent clarity** — Does the engineer understand WHAT they're building and WHY?
2. **Epistemic ownership** — Can they explain HOW the code works, regardless of who wrote it?
3. **Test quality** — Do tests validate intent, not just implementation?
4. **Architectural coherence** — Does it fit the system, not just work in isolation?

### CI/CD & Automated Testing

**Mechanism:** Continuous integration with human-approved test suites provides ongoing empirical validation.

Automated tests balance the velocity vs. ownership trade-off—they allow fast iteration while maintaining behavioral guardrails defined by humans.

[GAP: Other practices to explore - ADRs, documentation practices, pair programming with LLMs?]

---

## VI. The Measurement Problem

This is the most exploratory section. We don't yet know how to measure epistemic debt, and that's revealing in itself.

### Possible Empirical Indicators

**Bug and incident metrics:**
- Increase in production issues
- Harder-to-diagnose bugs
- Higher regression rates

**Knowledge loss velocity:**
- Bus factor acceleration (how quickly teams lose context when engineers leave)
- Onboarding difficulty for new team members
- Mean time to diagnose issues in "own" code

**Code archaeology costs:**
- Ratio of time understanding existing code vs. writing new code
- Self-reported understanding surveys over time

### The Challenge

Correlation vs. causation is difficult to establish. Is the codebase harder to understand because of LLMs, or because of growth, or because of turnover?

[GAP: This section needs the most development - need concrete measurement approaches without being prescriptive. Any existing research?]

---

## VII. Conclusion

[GAP: Write conclusion that reframes the debate from "will AI replace programmers?" to "what practices maintain epistemic warrant?"]

The question is not whether LLMs will replace engineers. It is how we maintain understanding of our systems in a world where code generation is cheap and comprehension remains expensive.

Perhaps LLMs are forcing us toward better epistemic practices by exposing our prior dependency on a false warrant—the assumption that authorship equals understanding. Code authorship was always a convenient fiction. Pre-LLM, we also copied from Stack Overflow, used framework magic we didn't understand, and inherited legacy code we never fully grasped.

The real warrant always came from tests, documentation, code review, and production monitoring. LLMs just make the need for these practices more urgent.

[GAP: What's the emotional landing? Optimistic? Cautionary? Uncertain?]

---

## References

[TODO: Add references from literature-review-on-epistemic-debt.md]
