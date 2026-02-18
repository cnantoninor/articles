---
title: 'Epistemic Debt: A New Lens'
subtitle: A framework for the understanding gap in AI-assisted development
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 1133
current_length: 1175
estimated_reading_time: 5 min
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


# Epistemic Debt: A New Lens

*A framework for the understanding gap in AI-assisted development*

---

*This is Part 2 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

Your tests are passing. Your code works. Your deployment succeeded. So why can't anyone on your team explain how the authentication flow actually works?

You've felt this. You've approved pull requests because the tests passed, not because you understood the logic. You've shipped code you couldn't fully explain. The velocity was intoxicating — entire features appearing in hours. But something was lost in that speed: the labor of knowing.

In the previous article, we named this accumulated opacity: *epistemic debt*. Now we need to define it precisely — because precision matters when you're trying to manage something that resists measurement.

## The Formula

Ngabang (2026) provides a mathematical foundation for understanding epistemic debt:

**Ed = ∫[0 to T] (Cs(t) - Gc(t)) dt**

Where:

- **Ed** = Epistemic Debt
- **Cs(t)** = System Complexity at time *t*
- **Gc(t)** = Cognitive Grasp of the team at time *t*
- **T** = Time period

In simpler terms: epistemic debt accumulates when your system grows more complex faster than your team's understanding grows. Cs(t) is "how complicated is our system?" Gc(t) is "how well do we understand it?" The integral captures how this gap compounds over time.

This isn't just an abstraction. Think about the last six months on your team. How many features shipped? How much new code entered the codebase? Now ask: how much of that new code could your team explain, line by line, without reading it? The gap between those two numbers — that's your epistemic debt.

## Epistemic Credit

The inverse concept is just as important. **Epistemic Credit (Ce)** represents surplus understanding — when your team's cognitive grasp *exceeds* system complexity.

**Ce = ∫[0 to T] (Gc(t) - Cs(t)) dt**

When you have epistemic credit, you have a buffer. You can absorb new complexity without immediately falling into debt. A team that deeply understands its architecture can accept an LLM-generated module and integrate it safely — because they know the boundaries, the invariants, the places where a subtle mistake would cascade.

Teams build epistemic credit through:

- **Human review** of all or the most important lines of code produced by the LLM
- **Manually documenting** AI-generated code (raising Gc)
- **Deliberate simplification** (reducing Cs while maintaining Gc)
- **Deep architectural review** (raising Gc faster than Cs grows)
- **Knowledge transfer** (spreading understanding across the team)

The practical implication: teams with accumulated credit can safely accept AI-generated complexity. Teams without it cannot — every new module of LLM-generated code pushes them deeper into debt.

## Technical Debt vs. Epistemic Debt

The analogy to technical debt is deliberate, but the differences are critical. They are not the same thing, and conflating them leads to the wrong interventions.

| Dimension | Technical Debt | Epistemic Debt |
|-----------|---------------|----------------|
| **What accumulates** | Code quality issues, shortcuts, workarounds | Understanding gaps, comprehension deficits |
| **What pays it down** | Refactoring, code cleanup | Learning, documentation, knowledge transfer |
| **Visibility** | Code metrics, static analysis | Bus factor, onboarding time, incident diagnosis |
| **Consequences of default** | Maintenance burden, slower changes | Catastrophic blind spots, production incidents |
| **Speed of accumulation** | Gradual (linear with velocity) | Exponential with AI (entire modules in hours) |
| **Who it affects** | Individual developers (local pain) | Entire team (systemic risk) |

The distinctions run deeper than the table suggests.

**Social dynamics differ.** Technical debt carries social stigma — you "cut corners." Epistemic debt is normalized — it feels like collaboration. When you accept an LLM suggestion and ship it, there's no cognitive dissonance. No sense that you've taken on risk. It feels like productivity.

**Localization differs.** Technical debt is localized to specific files and modules. You can point at it: "this function needs refactoring." Epistemic debt is diffuse. It's not in any particular file — it's in the gap between the codebase and the team's mental model. You can't grep for it.

**When it manifests differs.** Technical debt shows up in code review — the reviewer sees the shortcut and flags it. Epistemic debt shows up in crisis — the production incident that nobody can diagnose, the security vulnerability that nobody knew existed, the integration failure that nobody can explain.

**And crucially, the compounding dynamics differ.** Technical debt at one boundary can be corrected at the next. Poor requirements can still lead to good implementation if the engineer understands the domain. But epistemic debt compounds across boundaries. Unclear intent produces opaque code produces circular tests produces false confidence. By the time the system fails in production, the entire chain must be unwound to find the root cause.

## The Pre-LLM vs. Post-LLM Shift

It's worth being explicit about what changed.

Pre-LLM, epistemic gaps were rare and visible. You knew you copied that Stack Overflow snippet without fully understanding it. There was friction — you had to type it, integrate it, feel the cognitive dissonance of placing someone else's solution into your codebase. The friction was pedagogical: it slowed you down just enough to notice what you didn't understand.

Post-LLM, the gaps are pervasive and invisible. Entire modules appear. The code looks professional. The tests pass. And nobody remembers how any of it works — because nobody ever knew. The friction that once limited how fast teams could accumulate code they didn't understand has been removed. And with it, the natural brake on epistemic debt accumulation.

This is the core challenge. The velocity is real. The capability is real. But the gap between what we can generate and what we can understand is widening. And unlike technical debt, which announces itself through code smells and increasing maintenance burden, epistemic debt hides behind passing tests and successful deployments — right up until the moment it doesn't.

## What Comes Next

Understanding what epistemic debt is — and how it differs from technical debt — sets the foundation for understanding what happens when it comes due. The velocity we've gained from LLMs is real. The debt we're accumulating is also real.

In the next article, we'll look at what happens when epistemic debt defaults: the case studies are vivid, the industry data is sobering, and the pattern is clearer than most teams want to admit.

---

*Next in the series: **When Epistemic Debt Defaults** — three case studies and the industry data that says they aren't outliers.*

---



---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." viXra preprint.
- Ionescu, T.B., Schlund, S., & Schmidbauer, C. (2020). "Epistemic Debt: A Concept and Measure of Technical Ignorance in Smart Manufacturing." Springer.
