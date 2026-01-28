# Epistemic Debt in LLM-Generated Code - Article Development Session

**Date:** 2026-01-25
**Topic:** Substack article on epistemic risks of LLM-based software engineering

---

## Initial Thesis

The integration of Large Language Models (LLMs) into software engineering marks a **rupture in the epistemological status of code**.

### Core Argument

**Historical paradigm (70 years):** Programming grounded in deterministic authorship
- Human agent with specific intent constructs logical artifact
- Software = crystallization of human reason
- Epistemic warrant derived from causal chain of authorship
- Engineer knows system because it's product of their cognitive labor

**Current shift:** Dissolution of deterministic warrant
- Probabilistic layer between human intent and machine execution
- Code = product of stochastic pattern matching (vector spaces vs. symbolic logic)
- Shift from **Construction** (architect of every decision) to **Curation** (reviewer of probabilistic suggestions)

### Primary Risk

Not just technical correctness, but **"Epistemic Opacity"**
- LLMs produce "feeling of knowing" without "labor of knowing"
- Epistemic deficit manifests across SDLC phases

---

## Key Discussion & Insights

### 1. Reframing: Epistemic Debt (not just Warrant)

**Decision:** Use "epistemic debt" as primary framing
- More accessible than "epistemic warrant" for broad tech audience
- Actionable (debt can be measured, paid down, defaulted on)
- Connects to existing mental models in software engineering

**Definition:**
- **Technical debt:** Code that works but is hard to change (future maintenance cost)
- **Epistemic debt:** Code that works but nobody understands (future comprehension cost)

### 2. The Solutioning Trap

**Key insight:** Problem is NOT juniority/experience level

**Actual problem:** "Jumping to solutioning without clarifying the epistemic scope of the problem"
- Affects experienced engineers too
- LLMs make it trivially easy to generate solutions before understanding problem
- Velocity trap: can accumulate epistemic debt much faster than pre-LLM era

**Velocity vs. Ownership Trade-off:**
- Faster code generation
- Less ownership of reasoning
- Gap compounds before teams notice

### 3. Debt Accumulation at Scale

**Pre-LLM epistemic gaps:**
- Localized (one Stack Overflow snippet, one library)
- Visible (you know you copied it)
- Social pressure (stigma around copy-paste)
- Linear accumulation (natural speed limits)

**Post-LLM epistemic gaps:**
- Pervasive (entire modules, whole features)
- Invisible (feels like collaboration)
- Socially normalized (no stigma)
- Exponential accumulation (velocity removes friction)

### 4. Transformed PR Review Purpose

**What PR review should validate in LLM era:**
1. **Intent clarity** - Does engineer understand WHAT they're building and WHY?
2. **Epistemic ownership** - Can they explain HOW the code works, regardless of who wrote it?
3. **Test coverage** - Focus on test quality/comprehensiveness (especially E2E integration testing)
4. **Architectural coherence** - System-level design validation over line-by-line review

**Historical role:** Validate chain of reasoning (requirements → design → implementation)
**New role:** Validate understanding and intent, not just code correctness

### 5. Guardrails to Restore Warrant

#### Domain-Driven Design (DDD)
**Mechanism:**
- Ubiquitous language → shared problem definition → constrains LLM context
- Lexicon coherence feeds LLM context
- Creates verification criteria for PR review

**Value as epistemic anchor:**
- Shared language becomes the chain of reasoning (previously embodied in individual authorship)
- Front-loads epistemic work into problem definition
- Makes intent verifiable: "Does this code express our domain concept?"

**Limitation:** What prevents LLMs from being used to skip domain modeling too?

#### E2E Integration Testing
**Why E2E over unit tests:**
- Unit tests risk circular validation (LLM-generated tests validate LLM-generated code)
- E2E tests validate **behavior** against **requirements** - crosses epistemic boundary
- Integration tests verify seams between components (where misunderstandings compound)

**Value:**
- Harder to fake (requires understanding whole system)
- Validates against user intent, not implementation details
- Catches emergent behavior that unit tests miss
- Provides empirical validation independent of implementation

#### CI/CD & Automated Testing
- Importance of human-written/approved tests
- Automatically validate software to balance velocity vs. ownership trade-off

### 6. The Counterpoint: Exposing Existing Problems

**Question:** Were authorship and deterministic warrant always the real source of epistemic confidence?

**Counter-argument:** Code authorship was always a convenient fiction

**Pre-LLM practices with similar epistemic gaps:**
- Copy-paste from Stack Overflow
- Framework magic (Rails, Spring) - abstractions developers don't understand
- Legacy code maintenance - inheriting code you didn't write

**Real warrant always came from:**
1. Tests (behavioral validation)
2. Documentation (intent capture)
3. Code review (social validation)
4. Production monitoring (empirical validation)

**Provocative claim:** Maybe LLMs are **forcing us toward better epistemic practices** by exposing our dependency on a false warrant (authorship = understanding)

**Article position:** "Partially true" - some problems existed, but LLMs make them worse/more common in terms of velocity and scale

---

## Article Structure (Draft with Gaps)

### I. Opening: The Epistemic Shift (500-700 words)

**Hook:** Comparison - ask engineer in 2020 vs. 2025 why their code works
- 2020: "I chose this algorithm because..., implemented it this way because..."
- 2025: "The LLM suggested it, the tests pass, looks good"
- Same confidence, different warrant

**Thesis:** LLMs represent epistemological rupture - from deterministic authorship (Construction) to probabilistic curation

**Key concepts:**
- Epistemic warrant (traditional)
- Construction paradigm
- Curation paradigm

**🔴 GAP:** How technical/philosophical for broad tech audience?

---

### II. Epistemic Debt: A New Lens (400-600 words)

**Define epistemic debt:** Code that works but nobody understands

**Parallel to technical debt:**
- Both involve trade-offs
- Both accumulate over time
- Both can "default"

**Debt accumulation problem:**
- Pre-LLM: Linear (natural speed limits - typing, frustration, code review catches copy-paste)
- Post-LLM: Exponential (entire features in an afternoon, debt compounds before teams notice)

**🔴 GAP:** Concrete examples of epistemic debt "default events" - what does failure look like?

---

### III. The Solutioning Trap (500-700 words)

**Core problem:** Jumping to solutioning without clarifying epistemic scope

**Why LLMs enable this:**
- Reduce friction between idea and code
- Create "feeling of knowing without labor of knowing"
- Socially normalized (no stigma)

**Velocity vs. Ownership trade-off**

**🔴 GAP:** What does "clarifying epistemic scope" mean concretely in practice?

---

### IV. Epistemic Debt in the SDLC (800-1200 words)

**Reframe from phases to three epistemic boundaries:**

#### Boundary 1: Intent → Specification (Requirements/Design)
**Risk:** Vibe-based requirements → vibe-based design
**Manifestation:** "Build me a dashboard" → LLM generates → "looks good"
**Debt accumulated:** Team doesn't understand user needs, just has a dashboard

#### Boundary 2: Specification → Implementation
**Risk:** Probabilistic drift, subtle misalignment
**Manifestation:** Code that "mostly" matches intent with unexplained edge cases
**Debt accumulated:** Nobody can explain why it works (or doesn't) in specific scenarios

#### Boundary 3: Implementation → Validation (Testing/Review)
**Risk:** Circular validation (LLM tests validate LLM code)
**Manifestation:** 100% test coverage, all passing, but tests don't validate intent
**Debt accumulated:** False confidence in correctness

**🔴 GAP:** Need concrete examples for each boundary - real or realistic scenarios

---

### V. Possible Guardrails (600-900 words)

**Frame:** "Practices worth examining, not prescriptive solutions"

#### Domain-Driven Design
- **Mechanism:** Ubiquitous language → shared problem definition → constrains LLM context
- **How it helps:** Front-loads epistemic work into domain modeling
- **Limitation:** LLMs could skip this too
- **Value:** Creates verification criteria for PR review, lexicon coherence

#### E2E Integration Testing
- **Mechanism:** Validates behavior against requirements, crosses epistemic boundary
- **How it helps:** Harder to fake, requires system understanding
- **Limitation:** Still requires humans to define correct behavior
- **Value:** Empirical validation independent of implementation

#### Transformed PR Review
**What to validate:**
- Intent clarity (WHAT and WHY)
- Epistemic ownership (HOW it works)
- Test quality (validates intent, not just coverage)
- Architectural coherence (system-level)

**Shift:** Less line-by-line, more conceptual

#### CI/CD & Automated Testing
- Human-written/approved tests
- Continuous validation
- Balance velocity vs. ownership

**🔴 GAP:** Other practices to explore?
- Documentation practices
- Pair programming with LLMs
- Architectural Decision Records (ADRs)
- Etc.?

---

### VI. The Measurement Problem (500-700 words)

**Frame:** "Most exploratory section - we don't even know how to measure this yet, and that's revealing"

**Possible empirical indicators:**

1. **Bug/incident metrics**
   - More production issues
   - Harder-to-diagnose bugs
   - Regression rates

2. **Knowledge loss velocity** (emphasized)
   - Bus factor acceleration
   - How quickly teams lose context when engineers leave
   - Onboarding difficulty for new team members

3. **Code archaeology costs**
   - Ratio of time understanding existing code vs. writing new code
   - Mean time to diagnose issues in own code

4. **Self-reported understanding**
   - Surveys: "How well do you understand your codebase?"
   - Track over time

**The challenge:** Correlation vs. causation - isolating LLM impact from other factors

**Call for research:** Longitudinal studies, controlled experiments, better metrics

**🔴 GAP:** This section needs MOST development
- What other measurement approaches?
- How make concrete without being prescriptive?
- Any existing research/data?

---

### VII. Conclusion: Reframing the Debate (300-500 words)

**Main moves:**
- Shift from "will AI replace programmers?" to "what practices maintain epistemic warrant?"
- Acknowledge trade-off: velocity vs. ownership (not binary good/bad)
- Emphasize paradox: LLMs expose problems that always existed, but make them worse
- Call to action: Not to reject LLMs, but to consciously address epistemic debt

**Possible ending:** Maybe LLMs are forcing us toward better practices by making our bad habits visible?

**🔴 GAP:** What's the emotional landing? Optimistic? Cautionary? Uncertain?

---

## Article Goals & Audience

### Primary Goals
1. **Reframe the debate** - Shift conversation from "will LLMs replace engineers?" to "what practices restore warrant?"
2. **Explore the paradox** - Examine tension between velocity and ownership without prescribing solutions
3. **Suggest ideas for discussion** - Propose DDD, automated testing, CI/CD, human-focused PR review as starting points (NOT formalized/prescriptive framework)

### Target Audience
**Broad tech audience** - anyone interested in how AI changes software development
- Engineering leaders/CTOs
- Senior engineers/architects
- Researchers/academics
- Practitioners

### Tone
- Exploratory essay (not prescriptive)
- Philosophically informed but accessible
- Raises tensions and questions
- Suggests practices worth examining
- Invites discussion

---

## Key Uncertainties to Address

### 1. The Philosophical Framing
**Question:** Is "epistemic warrant/debt" the right lens? Am I overstating the rupture?
**Decision:** Use "epistemic debt" as primary framing (more accessible)
**Still uncertain:** How much philosophical depth for broad audience?

### 2. The Practical Remedies
**Question:** Will DDD/E2E testing actually help, or am I reaching?
**Position:** Frame as "guardrails to restore warrant" - compensatory practices
**Still uncertain:** Are there other practices? How avoid being too prescriptive?

### 3. The Measurement Problem
**Question:** How do we empirically validate that epistemic warrant is degrading?
**Position:** Be maximally open/exploratory in this section
**Most uncertain:** Need concrete measurement approaches without being prescriptive

---

## Summary of Identified Gaps

1. **Section I:** How technical/philosophical for broad audience?
2. **Section II:** Concrete examples of epistemic debt default events
3. **Section III:** What "clarifying epistemic scope" means in practice
4. **Section IV:** Real examples for each epistemic boundary
5. **Section V:** Other guardrail practices to explore?
6. **Section VI:** MOST development needed - measurement approaches
7. **Section VII:** Emotional tone of conclusion?

---

## Next Steps

- Decide on philosophical depth for introduction
- Collect concrete examples for each section
- Develop measurement section (most critical gap)
- Research existing literature on code comprehension metrics
- Draft introduction to test tone/framing
- Consider case studies or interviews to ground abstract concepts

---

## Key Quotes & Phrases to Consider

- "The feeling of knowing without the labor of knowing"
- "Velocity trap" - jumping to solutioning without clarifying epistemic scope
- "From Construction to Curation"
- "Epistemic debt compounds before teams notice"
- "Lexicon coherence feeds LLM context" (DDD connection)
- "Tests pass, ship it" - new engineering confidence without warrant
- "Code authorship was always a convenient fiction"
- "LLMs expose our dependency on false warrants"
