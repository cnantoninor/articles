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
