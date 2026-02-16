---
marp: true
theme: default
paginate: true
title: 'Epistemic Debt: The Hidden Cost of LLM-Generated Code'
current_length: 950
estimated_reading_time: 4 min
---


# Epistemic Debt

## The Hidden Cost of LLM-Generated Code

<!--
Speaker notes: This presentation explores how LLMs change the nature of developer understanding and introduces "epistemic debt" as a framework for discussing the risks.
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

## From Construction to Curation

### The Traditional Model (Construction)
- Engineer = architect of every decision
- Understanding derives from authorship
- "I know this code because I wrote it"

### The Emerging Model (Curation)
- Engineer = reviewer of probabilistic suggestions
- Understanding must be actively established
- "The code works, but do I understand it?"

<!--
Speaker notes: This is a fundamental shift in how developers relate to their code.
-->

---

## What is Epistemic Debt?

| Technical Debt | Epistemic Debt |
|----------------|----------------|
| Works but hard to change | Works but nobody understands |
| Future maintenance cost | Future comprehension cost |
| Visible in code structure | Invisible until crisis |

**Epistemic debt = code that works but nobody understands**

<!--
Speaker notes: The analogy to technical debt makes the concept accessible and actionable.
-->

---

## Debt Accumulation: Before and After

### Pre-LLM
- **Localized** (one snippet, one library)
- **Visible** (you knew you copied it)
- **Stigmatized** (copy-paste had a cost)
- **Linear** (natural speed limits)

### Post-LLM
- **Pervasive** (entire features)
- **Invisible** (feels like collaboration)
- **Normalized** (no stigma)
- **Exponential** (velocity removes friction)

<!--
Speaker notes: The key insight is that LLMs accelerate debt accumulation, not just debt creation.
-->

---

## The Solutioning Trap

> Jumping to implementation before clarifying the epistemic scope of the problem

- LLMs make it trivially easy to generate solutions
- Velocity outpaces understanding
- Debt compounds before teams notice

**This affects experienced engineers too.**

<!--
Speaker notes: Emphasize this is not about skill level—it's about the reduced friction between idea and code.
-->

---

## Epistemic Boundaries

Where debt accumulates in the SDLC:

1. **Intent → Specification**
   "Build me a dashboard" → LLM generates → "Looks good"

2. **Specification → Implementation**
   Code "mostly" matches intent with unexplained edge cases

3. **Implementation → Validation**
   LLM tests validate LLM code (circular validation)

<!--
Speaker notes: Walk through each boundary with concrete examples if available.
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

## Strategy Forces

| Strategy | Primary Pull | Effect |
|----------|-------------|--------|
| **DDD** | → Understanding | Aligns output with domain |
| **TDD** | → Reliability | Verifies correctness |
| **Human Review** | → Both | Catches blind spots |
| **Workflow** | Amplifies all | Enables lower-triangle zones |

**Goal:** Consciously choose where to operate, not maximize speed.

<!--
Speaker notes: Emphasize that the goal is conscious positioning, not avoiding trade-offs.
-->

---

## The Circular Validation Trap

When LLMs generate both code AND tests:

```
    LLM Code ──→ LLM Tests ──→ "Verified"
        ↑              ↓
        └──────────────┘
         Same blind spots
```

**Coverage is high. Confidence is false.**

**Solution:** Human-authored tests break the circularity.

<!--
Speaker notes: This is a critical failure mode that looks like success.
-->

---

## Domain-Based Strategy Selection

Not all code needs the same rigor:

| Domain Type | Acceptable Zone | Required Strategies |
|-------------|-----------------|---------------------|
| **Core** | Lower-triangle | DDD + TDD + Review |
| **Supporting** | Mid-triangle | One or two strategies |
| **Generic** | Upper-triangle OK | Speed over understanding |

**Epistemic debt as conscious choice, not accident.**

<!--
Speaker notes: This maps to DDD's subdomain classification.
-->

---

## Structured Workflows

Frameworks that enforce human checkpoints amplify all strategies:

- **Bite-sized prompts** → Stay within comprehension
- **Context-focused tasks** → Reduce unknown unknowns
- **Atomic commits** → Each change is verifiable
- **Phase checkpoints** → Force understanding before proceeding

Example: GSD (Get Shit Done) implements research → plan → execute → verify cycles.

<!--
Speaker notes: Mention that workflow overhead is worth it for substantial features.
-->

---

## The Measurement Problem

How do we know epistemic debt is accumulating?

- Bug/incident metrics (harder-to-diagnose issues?)
- Knowledge loss velocity (bus factor acceleration?)
- Code archaeology costs (time understanding vs. writing?)
- Self-reported understanding

**Challenge:** Correlation vs. causation

<!--
Speaker notes: Be honest that we don't yet know how to measure this well.
-->

---

## Reframing the Debate

Not: "Will AI replace programmers?"

But: **"What practices maintain epistemic warrant?"**

The question is not about job security.
It's about maintaining understanding of our systems.

<!--
Speaker notes: This reframing is the key message of the whole presentation.
-->

---

## A Provocative Thought

> Maybe LLMs are forcing us toward better epistemic practices by exposing our prior dependency on a false warrant—the assumption that authorship equals understanding.

Code authorship was always a convenient fiction.

<!--
Speaker notes: Leave the audience with this tension to consider.
-->

---

## Questions?

[GAP: Add contact information and resources]

<!--
Speaker notes: Be prepared for questions about specific practices, measurement approaches, and whether this is overstated.
-->
