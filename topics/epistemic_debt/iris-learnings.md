---
marp: true
theme: default
paginate: true
title: 'Trade-offs in LLM-Assisted Development: IRIS Learnings'
current_length: 3652
estimated_reading_time: 15 min
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

## Epistemic Debt: The New Technical Debt

**Comparison to familiar concept:**

| Technical Debt | Epistemic Debt |
|----------------|----------------|
| Code that works but is hard to change | Code that works but nobody understands |
| Future maintenance cost | Future comprehension cost |
| Visible in code structure | Invisible until crisis |

**Critical difference in LLM era:**
- Pre-LLM: Epistemic gaps were **localized**, **visible**, **socially stigmatized**
- With LLMs: Debt accumulates at **scale**, remains **invisible**, feels **productive**

**The problem isn't that LLMs generate bad code—it's that they generate working code faster than we can understand it.**

<!--
Speaker notes: Everyone knows technical debt. Epistemic debt is the same pattern applied to understanding rather than changeability. The key insight: with LLMs, you can ship code that works perfectly but that nobody—including you—truly understands. The tests pass, the code runs, but the comprehension cost compounds silently.
-->

---

## The Trade-off Triangle

**Three qualities you can optimize for:**

```
                      UNDERSTANDING
                   (Epistemic Credit)
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
      SPEED                              RELIABILITY
 (Velocity)                        (Verified Correctness)
```

**Reading the triangle:**
- **Corners** = the three qualities you can optimize
- **Position** = what you're trading off
- **Arrows** = how strategies pull your position
- **╳** = traps that give false confidence

**Key relationships:**
- **Understanding ↔ Speed**: Trade-off (inverse)
- **Speed ↔ Reliability**: Tension (can conflict)
- **Reliability ↔ Understanding**: Synergy (mutually reinforcing)

---

## Defining the Debt/Credit Dynamic

**Two sides of the same coin:**

**Epistemic Debt (De)** = accumulated gap when complexity outpaces understanding:
$$De = \int_{0}^{T} (Cs(t) - Gc(t)) \, dt$$

**Epistemic Credit (Ce)** = accumulated surplus when understanding exceeds complexity:
$$Ce = \int_{0}^{T} (Gc(t) - Cs(t)) \, dt$$

Where:
- **Gc(t)** = Cognitive Grasp of the team at time t
- **Cs(t)** = System Complexity at time t

**The inversion:**
- When Cs(t) > Gc(t): You're accumulating **debt** (code you don't understand)
- When Gc(t) > Cs(t): You're building **credit** (understanding surplus)

**Context matters**: Same practice yields different outcomes based on domain complexity and team grasp.

*Source: Ngabang (2026), "The Illusion of Competence"*

<!--
Speaker notes: We use both terms contextually. "Epistemic debt" describes the problem (unguarded AI use creates debt). "Epistemic credit" describes what we actively build through practices like DDD. They're mathematical inverses—when grasp exceeds complexity, you have credit; when complexity exceeds grasp, you have debt. IRIS was about deliberately building credit through structured practices.
-->

---

## Strategy Forces: How to Move on the Triangle

Different practices **pull** your position toward different vertices:

| Strategy | Primary Pull | Effect on Epistemic Debt | Risk/Trap |
|----------|-------------|--------------------------|-----------|
| **DDD** (ubiquitous language) | → Understanding | Builds ownership, doesn't verify correctness | Terminology drift if not enforced |
| **TDD** (esp. integration tests) | → Reliability | Verifies correctness, slight ownership gain | Circular validation if LLM-generated |
| **Human-in-loop review** | → Both | Ensures alignment + catches blind spots | Rubber-stamping if reviewer doesn't understand |
| **Structured Workflow** | Amplifies all | Meta-strategy enabling sustainable AI use | — |

**Key insight:** You can't maximize all three simultaneously. Choose your position based on domain criticality.

<!--
Speaker notes: This isn't abstract theory—these are practical levers. DDD pulls toward Understanding because it forces LLM output to use your domain language. TDD pulls toward Reliability by verifying correctness. Human review can pull toward both if done rigorously. Structured workflow (like GSD) doesn't pick a position—it amplifies whichever position you choose by adding discipline.
-->

---

## IRIS 1.0: Development Metrics

** Almost-Solo development with disciplined AI assistance:**

| Metric | Value | Context |
|--------|-------|---------|
| **Team Size** | 1 | Solo developer |
| **AI Assistance** | 90% | 10% manual review |
| **AI Tools** | Cursor, Claude | |
| **Project Type** | Internal tool - brand new | |
| **Main Language** | Python | |
| **Components** | CLI, Lib API, Web app, multiple storage systems, multiple external systems | |
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

## Understanding Vertex: DDD in IRIS

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
Speaker notes: Glob activation means LLM sees only relevant context for current work. Example: editing experiment code loads experiments.mdc with business rules. This pulls toward Understanding vertex—slower to set up initially, but LLM suggestions respect domain boundaries. You understand the output because it speaks your domain language.
-->

---

## DDD Pattern: Why It Builds Understanding

**General principle beyond IRIS:**

Domain-Driven Design creates epistemic credit through:

1. **Bounded Contexts** — Limits scope LLM needs to understand at once
2. **Ubiquitous Language** — Shared vocabulary between team, domain experts, and LLM
3. **Business Rules as Constraints** — Explicit encoding prevents LLM from generating "plausible but wrong" code

**The mechanism:**
- Without DDD: LLM generates generic variable names, you translate mentally
- With DDD: LLM uses `ExperimentVariant` not `item`, `ControlGroup` not `default`
- Result: Code reads like domain documentation → Understanding persists

**Trade-off:** Slower initial setup, ongoing terminology discipline required.

<!--
Speaker notes: This is why DDD pulls toward Understanding—it forces alignment between code structure and domain concepts. The upfront cost is documenting your domain boundaries and language. The payoff is LLM-generated code you can actually understand without reverse-engineering. In IRIS, this meant spending time defining bounded contexts, but then every LLM interaction respected those boundaries automatically.
-->

---

## Reliability Vertex: Human Tests in IRIS

**Human-authored E2E test** — The circular validation breaker:
- `tests/integration/test_user_journey_e2e.py` (972 lines)
- Full user workflow: import dataset → run experiment → download results
- Human intent captured end-to-end

**Mock boundaries defined** — Where to stop testing:
- `testing.mdc` defines integration vs unit scope
- Explicit rule: "Do NOT Over-Generate Tests"

**Impact**: Human-written integration tests verify LLM-generated code, not vice versa → Reliability ↔ Understanding synergy.

<!--
Speaker notes: Why E2E tests break circular validation—if LLM writes both code and tests, tests validate LLM's mental model of correctness, not actual requirements. A human-authored E2E test encodes real workflow understanding, catching when LLM-generated code drifts from intent. This demonstrates the Reliability/Understanding synergy: good tests both verify correctness AND serve as living documentation that builds understanding.
-->

---

## The Circular Validation Trap

**Why LLM-generated tests don't validate LLM-generated code:**

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

**The illusion:** Tests pass ✓ → Code must be correct
**The reality:** Tests verify LLM's mental model, not your requirements

**How to break it:**
- Write at least one comprehensive E2E test yourself
- Define test boundaries before asking LLM to fill in unit tests
- Use human-authored tests as the source of truth

<!--
Speaker notes: This is the ╳ trap on the triangle. When LLMs generate both code and tests, you get false confidence—everything looks verified, but both outputs share the same misunderstandings. In IRIS, writing one 972-line E2E test by hand was expensive, but it encoded the actual workflow. Then LLM-generated unit tests could safely fill in the details, because they were constrained by the human-defined integration boundary.
-->

---

## Human Tests: Why They Build Reliability

**General principle beyond IRIS:**

Human-authored tests create reliability through:

1. **Independent validation** — Tests encode *your* understanding of correctness, not LLM's
2. **Requirement capture** — Integration tests document intended workflow
3. **Living documentation** — Future maintainers see what "correct" means

**The mechanism:**
- Without human tests: LLM generates code + tests from same prompt → circular
- With human tests: Your test defines "correct" → LLM code must satisfy it
- Result: Verified against real requirements, not inferred assumptions

**Trade-off:** Writing comprehensive integration tests is time-intensive.

**Synergy with Understanding:** Good tests serve double duty—they verify AND document.

<!--
Speaker notes: This explains why Reliability and Understanding have synergy on the triangle. A well-written integration test both verifies correctness AND teaches future maintainers (including future you) what the system is supposed to do. This is why we didn't just say "write tests"—we specifically said "human-authored integration tests" to break the circular validation problem unique to LLM-generated code.
-->

---

## Speed Vertex: Workflow Evolution in IRIS

**IRIS 1.0 custom workflow commands:**
- `.cursor/commands/` (5 custom commands)
- `prdescription.md`: Generate structured PR descriptions with LOC metrics
- `verifyeventuallyfix.md`: Verification-before-fix pattern

**Key innovation — Verification-first:**
1. Run tests → analyze failures → *then* ask LLM for fix
2. Prevents "solutioning trap" (jumping to implementation before understanding problem)

**LOC tracking** — Visibility into AI contributions:
- PR descriptions include "Pure Code Added" column
- Track what LLM generates vs what humans write

**Evolution beyond IRIS:**
- These project-specific commands proved the pattern
- Led to adopting GSD (Get Shit Done) workflow
- Now used across multiple projects at Bloomberg

**Impact**: Structure enables speed *with* quality gates → sustainable velocity.

<!--
Speaker notes: The custom commands were IRIS-specific but established a critical principle: structure LLM interaction through explicit workflows, not ad-hoc prompting. The verification-before-fix pattern was crucial—it forces you to understand the problem space before asking LLM for solutions. This prevents the common trap of generating solutions to the wrong problem. The LOC tracking gave visibility: "This 500-line PR has 450 lines LLM-generated, 50 human-written"—helps calibrate trust appropriately.
-->

---

## GSD Workflow: The Four Phases

**Systematic approach that evolved from IRIS learnings:**

```
    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │ DISCUSS │───→│  PLAN   │───→│ EXECUTE │───→│ VERIFY  │
    └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘
         │              │              │              │
         ↓              ↓              ↓              ↓
    Align intent   Atomic tasks   Fresh context   Human gates
    + scope        + specs        windows         + tests
```

**Each phase has specific epistemic impact:**

1. **DISCUSS** — Capture decisions before planning (forces human articulation of intent)
2. **PLAN** — Create atomic task specs with verification criteria (scope management)
3. **EXECUTE** — Fresh 200k context per agent, parallel waves (prevents context amnesia)
4. **VERIFY** — Automated tests + human acceptance (breaks circular validation if tests pre-defined)

**Not IRIS-specific:** Applicable to any LLM-assisted development project.

<!--
Speaker notes: GSD generalizes the workflow patterns proven in IRIS. The key innovation is phase separation with human gates between. Each phase runs in fresh context, preventing the "context window amnesia" problem. The DISCUSS phase forces you to articulate what you want before planning how to build it. EXECUTE uses multiple parallel agents, each with fresh 200k context windows. VERIFY ensures human validation before considering work complete.
-->

---

## GSD Mechanisms: Countering Epistemic Debt

**How structured workflow addresses LLM-specific problems:**

| Problem | GSD Solution |
|---------|--------------|
| **Context Window Amnesia** | Fresh context per execution wave + persistent STATE.md artifacts |
| **Stochastic Spaghetti** | Multi-agent with single orchestrator; atomic commits enable git bisect |
| **Circular Validation** | Plan checker validates BEFORE execute; verification uses predefined criteria |
| **Scope Creep** | REQUIREMENTS.md scopes v1 vs v2; atomic tasks with clear boundaries |
| **Loss of Human Ownership** | Discussion phase forces articulation; STATE.md tracks decisions; human gates between phases |

**The pattern:** Add just enough structure to maintain comprehension without killing velocity.

<!--
Speaker notes: Each mechanism addresses a specific epistemic debt accumulation pattern unique to LLM development. Context amnesia happens when conversation history grows beyond LLM's window—fresh contexts solve this. Stochastic spaghetti is when LLM generates different implementations of "same" feature across sessions—atomic commits + git bisect make this debuggable. The key is these aren't bureaucracy—they're targeted solutions to real problems we hit in IRIS.
-->

---

## GSD Epistemic Impact by Phase

**How each phase reduces epistemic debt:**

| GSD Phase | What It Does | Epistemic Debt Reduction Mechanism |
|-----------|--------------|-----------------------------------|
| **DISCUSS** | Captures decisions *before* planning | Forces human articulation of intent → **Understanding** |
| **PLAN** | Creates atomic task specs with verification criteria | Scope management + testable outcomes → **Both** |
| **EXECUTE** | Fresh 200k context per agent, parallel waves | Prevents context amnesia, bite-sized comprehension → **Understanding** |
| **VERIFY** | Automated tests + human acceptance testing | Breaks circular validation if tests are pre-defined → **Reliability** |

**Key insight:** Each phase has dual purpose—it produces output AND builds/preserves understanding.

**Result:** Workflow doesn't just ship code—it maintains epistemic credit throughout development.

<!--
Speaker notes: This table shows why GSD is an amplifier, not a vertex choice. It doesn't pick Speed vs Understanding vs Reliability—it helps you maintain whichever position you chose. DISCUSS builds Understanding by forcing articulation. PLAN touches both by creating comprehensible scopes. EXECUTE maintains Understanding despite high velocity. VERIFY builds Reliability through predefined test criteria. The workflow makes it possible to operate in the lower-triangle zone without accumulating unsustainable epistemic debt.
-->

---

## Workflow Enables Lower-Triangle Operation

**Without structured workflow:**
```
                      UNDERSTANDING
                           ▲
                          /·\
                         /···\
                        / Pure \
                       / Vibe   \
                      /  Zone    \
                     /────────────\  ← Accessible without workflow
                    /              \
                   /    UNSAFE      \
                  /      ZONE        \
                 /    (High debt)     \
                ▼──────────────────────▼
              SPEED              RELIABILITY
```

**With structured workflow (GSD):**
```
                      UNDERSTANDING
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
                 /   ┌───────────┐   \
                /    │ ACCESSIBLE │   \  ← Workflow makes this
               /     │   WITH     │    \    zone reachable
              /      │ WORKFLOW   │     \
             /       └───────────┘      \
            ▼──────────────────────────▼
          SPEED                    RELIABILITY
```

**The shift:** Structure enables high Speed + Understanding + Reliability simultaneously through:
- Parallelization (multiple agents working concurrently)
- Pre-computed plans (no planning during execution)
- Fresh contexts (no cognitive overload accumulation)

<!--
Speaker notes: This is the payoff visualization. Without workflow, the lower triangle is dangerous—high speed or high reliability, but you're accumulating epistemic debt invisibly. With workflow, you can operate in zones that were previously unsustainable. The workflow doesn't eliminate the fundamental trade-offs, but it makes previously inaccessible positions achievable. In IRIS, we hit 5K LOC/week (Speed) with >85% coverage (Reliability) while maintaining understanding through DDD + workflow structure.
-->

---

## Multi-AI Context Sync (IRIS Meta Practice)

**The problem:** Using multiple AI tools (Claude, Cursor) creates context divergence
- Change captured in Claude → not visible to Cursor
- Cursor learns new pattern → Claude doesn't know about it
- Result: Inconsistent suggestions, duplicated explanations, epistemic drift

**The IRIS solution:** `scripts/sync-ai-instructions.sh`
- Synchronizes `.cursor/rules/` with Claude's context files
- Keeps domain boundaries aligned across tools
- Updates happen automatically on context changes

**Why this matters for the triangle:**
- **Understanding:** Consistent domain language across all AI interactions
- **Reliability:** Both tools validate against same business rules
- **Speed:** No need to re-explain context to each tool

**Meta insight:** When using multiple AIs, synchronize their worldview—otherwise you're managing N different mental models instead of one.

<!--
Speaker notes: This was a late addition to IRIS but solved a real pain point. When you use Claude for planning and Cursor for coding, keeping their understanding synchronized prevents expensive context re-establishment. The script is simple—it copies context files—but the impact is significant. It's another amplifier: it doesn't pick your triangle position, but it makes whichever position you chose more sustainable across tools.
-->

---

## Domain-Based Strategy Selection

**Not all code deserves equal epistemic investment:**

| Domain Type | Acceptable Zone | Required Strategies | Rationale |
|-------------|-----------------|---------------------|-----------|
| **Core** (competitive advantage) | Bottom center | DDD + TDD + Human Review | Errors have highest business impact |
| **Supporting** (enables core) | Mid-triangle | At least one of DDD or TDD | Balance speed with some guardrails |
| **Generic** (commodity) | Upper-triangle OK | Minimal or none | Speed may outweigh deep understanding |

**Mapping to DDD's subdomain classification:**
- Core subdomain → Lower triangle (high Understanding + Reliability)
- Supporting subdomain → Mid triangle (balance)
- Generic subdomain → Upper triangle (Speed acceptable)

**IRIS example:**
- Core: Experiment execution logic → DDD + E2E tests
- Supporting: CLI commands → Workflow structure only
- Generic: Utility functions → Let LLM generate freely

<!--
Speaker notes: This is the practical decision framework. You don't need to apply DDD + TDD + workflow to every line of code—that would kill velocity unnecessarily. Instead, consciously position different parts of your codebase on the triangle based on business criticality. IRIS core experiment logic got the full treatment (bounded contexts + human E2E test). CLI tooling got workflow structure but lighter guardrails. Utility functions were often pure LLM output with basic review. The key is making this choice deliberately, not accidentally.
-->

---

## Conscious Choice Framework

**Epistemic debt, like technical debt, can be a deliberate trade-off.**

**When epistemic debt is acceptable:**
- Generic domains (authentication wrappers, CRUD boilerplate)
- Prototype/exploration phases
- Code with short expected lifespan
- Low business impact areas

**When epistemic debt is critical risk:**
- Core business logic
- Security-sensitive code
- Long-lived systems
- Code that others will maintain

**The triangle provides visual language for these conversations:**
- "We're operating upper-triangle on this module—Speed priority, accept the epistemic debt"
- "This is core domain—we need lower-triangle positioning"
- "Let's move this to mid-triangle by adding DDD context"

**Key question:** Not "how do we eliminate epistemic debt?" but "where is it acceptable and where is it dangerous?"

<!--
Speaker notes: This reframes the entire conversation. Epistemic debt isn't inherently bad—it's a trade-off. Just like you might ship technical debt in a prototype, you can deliberately accept epistemic debt in non-critical code. The framework gives you language to make this explicit. In team discussions, instead of arguing "should we use AI here?" you can say "this is core domain, so lower-triangle" or "this is commodity, upper-triangle is fine." The triangle makes the trade-off visible and discussable.
-->

---

## Key Takeaways

**Conscious positioning on the Speed/Understanding/Reliability triangle:**

1. **Bounded contexts build Understanding** — Glob-activated DDD context files (`.cursor/rules/*.mdc`) ensure LLM output aligns with domain boundaries. IRIS: 5 bounded contexts with business rules. *Pull: Understanding vertex.*

2. **Human E2E tests build Reliability** — One comprehensive integration test (`test_user_journey_e2e.py`, 972 lines) validates LLM-generated code against real user workflow, breaking circular validation. *Pull: Reliability. Synergy: Understanding through living documentation.*

3. **Structured workflow enables Speed** — Verification-before-fix pattern + GSD phases prevent solutioning trap while maintaining velocity. IRIS: 5K LOC/week with >85% coverage. *Pull: Speed with quality gates.*

4. **Multi-AI sync amplifies all** — When using multiple AI tools (Claude, Cursor), synchronize their context (`sync-ai-instructions.sh`) to prevent divergence. *Amplifies all vertices.*

5. **Choose your position deliberately** — Map domains to triangle positions: Core → lower triangle (Understanding + Reliability), Generic → upper triangle (Speed). **Trade-offs are real—make them conscious.**

<!--
Speaker notes: Five concrete, actionable takeaways from IRIS. Each maps to a specific file path or practice you can adopt. The final point is the meta-lesson: you can't maximize all three simultaneously, so choose your position based on domain criticality. The framework gives you language to make these trade-offs explicit rather than accidental.
-->

---

## References

**Epistemic Debt Definition:**
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
