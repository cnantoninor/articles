---
title: "Epistemic Debt: The Hidden Cost of LLM-Generated Code"
status: draft
type: article
audience: [engineering leaders, senior engineers, architects, researchers]
target_length: 4000-6000
created: 2026-01-25
last_updated: 2026-01-26T18:30:00Z
---

# Epistemic Debt: The Hidden Cost of LLM-Generated Code

## Abstract

The integration of Large Language Models into software engineering marks a fundamental shift in how developers relate to their code. This article is about the novel concept, in software engineering, of "epistemic debt": _code that works but nobody understands_. It is a lens for examining the risks of LLM-augmented development. We explore how the shift from construction to curation changes the nature of developer understanding, examine where epistemic debt accumulates in the software development lifecycle, and suggest practices worth examining as potential guardrails.

---

## I. The Epistemic Shift

A code review in 2020: The reviewer asks, "Why binary search here?" The engineer responds, "The dataset is sorted, and we need O(log n) lookups. I considered a hash table, but the memory overhead wasn't worth it for our scale, and we need range queries later." The reviewer nods. The reasoning is clear.

A code review in 2025: The same question. The engineer responds, "Claude suggested it. The tests pass—100% coverage. I checked the edge cases I could think of. It handles the main scenarios." The reviewer scans the implementation. It looks professional. The logic seems sound. They approve it.

Same confidence. Different warrant.

The code works. The tests pass. But if you asked the 2025 engineer to explain *why* binary search is correct here, or what assumptions it makes about data distribution, or how it would fail if those assumptions broke, they might hesitate. The code appeared quickly—ten seconds to generate, ten minutes to review. The team moved fast. But something was lost in the velocity: the labor of knowing.

For roughly seventy years, programming has been grounded in deterministic authorship. A human agent with specific intent constructs a logical artifact. Software, in this view, is the crystallization of human reason. The epistemic warrant—the justification for claiming to understand the code—derives from a causal chain of authorship. You know the system because it is the product of your cognitive labor.

LLMs introduce a rupture in this epistemological framework. A probabilistic layer now sits between human intent and machine execution. Code becomes the product of stochastic pattern matching across vast vector spaces rather than direct symbolic reasoning. The developer's role shifts from **construction**—being the architect of every decision—to **curation**—reviewing and selecting from probabilistically-generated suggestions.

The primary risk is not merely technical correctness. It is **epistemic opacity**: the LLM produces what we might call the "feeling of knowing" without the "labor of knowing."

We can think of this as **epistemic debt**—code that works but nobody understands.[^1] Like technical debt, it represents a future cost: not the cost of changing code, but the cost of comprehending it. Ngabang (2026) offers a precise definition: epistemic debt is the divergence between system complexity and the developer's cognitive model of that system.[^2] When you ship code you cannot explain, you have not just delivered a feature—you have created a comprehension obligation that compounds over time.

The shift from construction to curation makes this debt accumulate differently. Pre-LLM, epistemic gaps were localized (one Stack Overflow snippet), visible (you knew you copied it), and socially stigmatized (copy-paste carried reputational cost). Post-LLM, they are pervasive (entire modules), invisible (feels like collaboration), and normalized (no stigma attached). The velocity is exponential rather than linear—LLMs remove the natural friction that once limited how fast teams could accumulate code they didn't understand.

This is what Quattrociocchi et al. (2025) call *Epistemia*: a structural condition where linguistic plausibility substitutes for epistemic evaluation.[^3] The system produces fluent, confident outputs without the internal machinery that makes reliability accountable. You experience the possession of an answer without having traversed the process of forming a justified belief. Understanding becomes optional when generation is cheap.

[^1]: The term originates in manufacturing (Ionescu et al., 2020) but maps precisely to LLM-assisted development.

[^2]: Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." *viXra preprint*.

[^3]: Quattrociocchi, W., Capraro, V., & Perc, M. (2025). "Epistemological Fault Lines Between Human and Artificial Intelligence." *arXiv:2512.19466*.

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

The core problem is not inexperience or lack of skill. It is **jumping to creating a solution for a software without clarifying the epistemic scope of the problem**.

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

The developer asks the LLM to generate tests for the LLM-generated code. The tests pass. Coverage is high. But the tests don't cross an epistemic boundary—they validate that the code matches the code, not that the code matches the intent. (TDD as a guardrail against circular validation.)

**Debt accumulated:** False confidence in correctness.

[EXAMPLE NEEDED: Example of circular validation in practice]

---

## V. The Trade-off Triangle: A Framework for Guardrails

Before examining specific practices, we need a framework for understanding what we're trading off.

LLM-augmented development exists in a three-dimensional space:

- **Speed** — How fast can we ship?
- **Understanding** — Do we have epistemic ownership of the code?
- **Reliability** — Does the code actually work correctly?

```
                              SPEED
                                ▲
                               / \
                              /   \
                             /     \
                            /   ●   \         ← Unguarded AI Use
                           /   / \   \           (Pure Vibe Coding)
                          /   /   \   \
                         /   ↙     ↘   \
                        / DDD       TDD  \     ← Strategy forces
                       /  ║           ║   \      pull toward corners
                      /   ║           ╳    \
                     /    ↘     ●    ↙      \  ← ╳ TRAP: Circular
                    /       Conscious        \      Validation
                   /       Trade-off          \
                  /          Zone              \
                 ▼─────────────────────────────▼
          UNDERSTANDING                   RELIABILITY
         (Epistemic Ownership)       (Verified Correctness)
```

Each guardrail exerts a **force** that pulls development toward certain corners of this triangle:

| Strategy | Primary Pull | Secondary Effect |
|----------|-------------|------------------|
| **DDD** | → Understanding | Aligns AI output with domain concepts |
| **TDD** | → Reliability | Verifies correctness against human-defined tests |
| **Human Review** | → Both | Ensures alignment and catches blind spots |
| **Structured Workflow** | Amplifies all | Makes lower-triangle zones accessible |

The goal is not to eliminate speed—that would defeat the purpose of using LLMs. The goal is to **consciously choose where to operate** based on domain importance:

- **Core domains:** Lower-triangle operation (DDD + TDD + Review)
- **Supporting domains:** Mid-triangle acceptable (one or two strategies)
- **Generic domains:** Upper-triangle tolerable (speed over deep understanding)

With this framework in mind, let's examine specific practices.

---

### The Circular Validation Trap

Before discussing TDD, we must address a failure mode that masquerades as verification.

When LLMs generate both code and tests, the tests inherit the same blind spots as the code. The system appears verified—coverage is high, tests pass—but the reliability is illusory. The tests validate that the code matches *itself*, not that it matches *intent*.

```
    LLM Code ──→ LLM Tests ──→ "Verified" ──→ FALSE CONFIDENCE
        ↑              ↓
        └──────────────┘
         Same blind spots
```

**Solution:** Human-authored tests, especially integration tests, break this circularity by crossing an epistemic boundary.

---

The following are **practices worth examining**, not prescriptive solutions. Each offers a potential mechanism for restoring epistemic warrant in an LLM-augmented workflow.

### Domain-Driven Design

**Mechanism:** Ubiquitous language creates a shared problem definition that constrains LLM context and provides verification criteria.

DDD front-loads epistemic work into domain modeling. When the team has a precise shared vocabulary—"aggregate root," "bounded context," "domain event"—the LLM's output can be verified against that vocabulary. Does this code express our domain concept? . DDD is ontological and lexicon based, so it is a natural fit for lexicon based prediction machines like LLMs.

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

### Structured Workflows

**Mechanism:** Workflow frameworks that enforce human checkpoints between phases amplify all other guardrails.

A structured workflow doesn't just add another arrow to the triangle—it makes the **lower-triangle zones accessible without sacrificing too much speed**. The key mechanisms:

| Workflow Element | Epistemic Debt Reduction |
|------------------|--------------------------|
| **Bite-sized prompts** | LLM output stays within human comprehension |
| **Context-focused tasks** | Reduces "unknown unknowns" from context amnesia |
| **Atomic commits** | Each change is small enough to verify |
| **Phase checkpoints** | Forces human understanding before proceeding |
| **Persistent state files** | Makes progress visible, prevents drift across sessions |

Emerging frameworks like GSD (Get Shit Done) implement these patterns through multi-agent orchestration: research → plan → execute → verify cycles with human gates between phases. The orchestrator never performs heavy lifting—it integrates results from specialized agents, each operating with a fresh context window.

**Limitation:** Workflow overhead. Best suited for substantial features rather than quick fixes.

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
