# The Epistemic Trade-off Triangle

A visual framework for understanding the relationship between Speed, Understanding, and Reliability in LLM-augmented software development.

---

## The Core Model

```
                              SPEED
                                ▲
                               /·\
                              / · \
                             /  ·  \
                            /   ●   \         ← Unguarded AI Use
                           /   /·\   \           (Pure Vibe Coding)
                          /   / · \   \
                         /   /  ·  \   \
                        /   ↙   ·   ↘   \
                       / DDD    ·    TDD  \     ← Strategy forces
                      /  ║      ·     ║    \      pull toward corners
                     /   ║      ·     ║ ╳   \
                    /    ║      ·     ╳      \  ← ╳ TRAP: Circular
                   /     ↘      ·     ↙       \      Validation
                  /       ↘     ·    ↙         \
                 /         ↘    ●   ↙           \
                /        Conscious               \
               /        Trade-off                 \
              /           Zone                     \
             ▼─────────────────●────────────────────▼
      UNDERSTANDING           ↑            RELIABILITY
     (Epistemic Ownership)    │       (Verified Correctness)
                              │
                        Human Review
                       (pulls to both)
```

**Reading the triangle:**
- **Corners** represent the three qualities you can optimize for
- **Position** shows what you're trading off
- **Arrows** show how strategies shift your position
- **╳** marks traps that give false confidence

---

## Legend: Approaches

| Position | Approach | Speed | Understanding | Reliability | Epistemic Debt |
|----------|----------|:-----:|:-------------:|:-----------:|:--------------:|
| Top | Pure Vibe Coding | High | Low | Unknown | **Maximum** |
| Upper-center | AI + Basic Oversight | High | Low-Med | Low | High |
| Left-center | AI + DDD | Medium | Medium-High | Low-Med | Moderate |
| Right-center | AI + TDD/Integration | Medium | Low-Med | High | Moderate |
| Center | Balanced (DDD + TDD) | Medium | Medium | Medium-High | **Managed** |
| Bottom-left | Traditional (No LLM) | Low | High | Medium | Minimal |

---

## Legend: Strategy Forces

| Strategy | Primary Pull | Effect on Epistemic Debt | Risk/Trap |
|----------|-------------|--------------------------|-----------|
| **TDD** (esp. integration testing) | → Reliability | Verifies *correctness*, slight ownership gain | Circular validation if tests are LLM-generated |
| **DDD** (ubiquitous language) | → Understanding | Builds *ownership*, doesn't verify correctness | Terminology drift if not enforced |
| **Human-in-loop review** | → Both | Ensures *alignment* + catches blind spots | Rubber-stamping if reviewer doesn't understand |
| **Structured Workflow** | Amplifies all | Meta-strategy that enables sustainable AI use | — |

---

## The Circular Validation Trap

```
    ┌─────────────────────────────────────────────────────┐
    │   APPEARS TO BE:           ACTUALLY IS:             │
    │                                                     │
    │   LLM Code ──→ Tests ──→    LLM Code ←──┐           │
    │       ↑           │             ↑       │           │
    │       └───────────┘             │       │           │
    │    "Verified"                   └───────┘           │
    │                              Circular: Same         │
    │                              blind spots            │
    └─────────────────────────────────────────────────────┘

    SOLUTION: Human-authored tests (especially integration)
              break the circular dependency
```

When LLMs generate both code and tests, the tests inherit the same blind spots as the code. The system appears verified but the reliability is illusory.

---

## Domain-Based Strategy Selection

| Domain Type | Acceptable Zone | Required Strategies | Rationale |
|-------------|-----------------|---------------------|-----------|
| **Core** (competitive advantage) | Bottom center | DDD + TDD + Human Review | Errors have highest business impact |
| **Supporting** (enables core) | Mid-triangle | At least one of DDD or TDD | Balance speed with some guardrails |
| **Generic** (commodity) | Upper-triangle OK | Minimal or none | Speed may outweigh deep understanding |

This maps to Domain-Driven Design's subdomain classification, allowing teams to consciously accept epistemic debt where appropriate.

---

## Structured Workflow as Amplifier

Structured workflows like GSD (Get Shit Done) don't just add another arrow to the triangle—they **amplify the effectiveness of all strategies** by enforcing discipline at each phase.

### GSD Cycle × Epistemic Triangle

```
    ┌────────────────────────────────────────────────────────────────┐
    │                         GSD WORKFLOW                           │
    │                                                                │
    │   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    │
    │   │ DISCUSS │───→│  PLAN   │───→│ EXECUTE │───→│ VERIFY  │    │
    │   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘    │
    │        │              │              │              │          │
    │        ↓              ↓              ↓              ↓          │
    │   Align intent   Atomic tasks   Fresh context   Human gates   │
    │   + scope        + specs        windows         + tests       │
    │        │              │              │              │          │
    │        └──────────────┴──────────────┴──────────────┘          │
    │                            ↓                                   │
    │              EPISTEMIC DEBT REDUCTION                          │
    │         Understanding ←────────────→ Reliability               │
    └────────────────────────────────────────────────────────────────┘
```

### Phase-by-Phase Epistemic Impact

| GSD Phase | What It Does | Epistemic Debt Reduction Mechanism |
|-----------|--------------|-----------------------------------|
| **DISCUSS** | Captures decisions *before* planning | Forces human articulation of intent → **Understanding** |
| **PLAN** | Creates atomic task specs with verification criteria | Scope management + testable outcomes → **Both** |
| **EXECUTE** | Fresh 200k context per agent, parallel waves | Prevents context amnesia, bite-sized comprehension → **Understanding** |
| **VERIFY** | Automated tests + human acceptance testing | Breaks circular validation if tests are pre-defined → **Reliability** |

### GSD Mechanisms That Counter Epistemic Debt Accumulation

| Problem | GSD Solution |
|---------|--------------|
| Context Window Amnesia | Fresh context per execution wave + persistent STATE.md artifacts |
| Stochastic Spaghetti | Multi-agent with single orchestrator; atomic commits enable git bisect |
| Circular Validation | Plan checker validates BEFORE execute; verification uses predefined criteria |
| Scope Creep | REQUIREMENTS.md scopes v1 vs v2; atomic tasks with clear boundaries |
| Loss of Human Ownership | Discussion phase forces articulation; STATE.md tracks decisions; human gates between phases |

### Where Structured Workflow Enables Operation

```
                              SPEED
                                ▲
                               /·\
                              /···\
                             / ··· \
                            / ····· \
                           /  Pure   \
                          /   Vibe    \
                         /    Zone     \
                        /───────────────\
                       /                 \
                      /   ┌───────────┐   \      Structured workflow
                     /    │ ACCESSIBLE │   \     makes this zone
                    /     │   WITH     │    \    reachable without
                   /      │ WORKFLOW   │     \   sacrificing too
                  /       └───────────┘      \   much speed
                 /                            \
                ▼──────────────────────────────▼
         UNDERSTANDING                    RELIABILITY
```

**Key insight:** Structured workflows don't eliminate speed—they make the **lower-triangle zones accessible** through:
- Parallelization (multiple agents working concurrently)
- Pre-computed plans (no planning during execution)
- Fresh contexts (no cognitive overload accumulation)

---

## Conscious Choice Framework

Epistemic debt, like technical debt, can be a deliberate trade-off. The question is not "how do we eliminate it?" but "where is it acceptable and where is it dangerous?"

**When epistemic debt is acceptable:**
- Generic domains (authentication wrappers, CRUD boilerplate)
- Prototype/exploration phases
- Code with short expected lifespan

**When epistemic debt is critical risk:**
- Core business logic
- Security-sensitive code
- Long-lived systems
- Code that others will maintain

The triangle provides a visual language for these conversations.

---

*Framework developed for: Epistemic Debt in LLM-Augmented Software Engineering*
