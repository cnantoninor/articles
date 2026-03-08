---
title: 'Epistemic Debt: The Math, The Cost, and Why It''s Not Technical Debt'
subtitle: A mathematical definition of epistemic debt, its economic cost, and why
  technical debt analogies break down
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 2200
current_length: 2539
estimated_reading_time: 11 min
created: 2026-02-15
last_updated: 2026-03-08
published_date: null
publication_url: ''
social_teasers:
  linkedin: ''
  twitter: ''
  instagram_caption: ''
  substack_notes: ''
---




# Epistemic Debt: The Math, The Cost, and Why It's Not Technical Debt

*A mathematical definition of epistemic debt, its economic cost, and why technical debt analogies break down.*

---

*This is Part 2 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

In the previous article, we surfaced a concept emerging in academic and industry literature as *epistemic debt*: the accumulated opacity of code that works but the team can't understand without investing time and effort to reverse-engineer it. That labour can outweigh the speed benefits of AI-assisted development as we will try to show in this article.

Before we formalize the concept, one economic idea sets the stage: the cost of change. You can catch a scope mismatch in a two-minute design conversation, or discover it later, woven through 400 lines of generated code. The second path costs a lot more. Barry Boehm's Cost of Change Curve made this explicit in the 1980s: fix a requirements misunderstanding at design time and you pay a fraction; find it in production and the price jumps by orders of magnitude. 

AI collaboration pushes these costs higher because of two compounding factors: the velocity at which code is generated and the level of abstraction at which the debt is incurred. Pre-LLM, copying a Stack Overflow snippet came with friction that forced you to notice what you didn't understand. Post-LLM, entire modules appear without that friction. The natural brake on epistemic debt accumulation has been removed.

Now we need to define epistemic debt more precisely to understand its economic implications. We'll then use the well-known concept of technical debt to help, showing where the two concepts converge and, more importantly, where they diverge.

## The Formula

Ngabang (2026) provides a mathematical definition:

**Ed = ∫[0 to T] (Cs(t) - Gc(t)) dt**

Where:

- **Ed** = Epistemic Debt
- **Cs(t)** = System Complexity at time *t*
- **Gc(t)** = Cognitive Grasp of the team at time *t*
- **T** = Time period

Epistemic debt accumulates when your system grows more complex faster than your team's understanding grows. Cs(t) is "how complicated is our system?" Gc(t) is "how well do we understand it?" The integral captures how this gap compounds over time. 

This isn't just an abstraction. Think about the last six months on your team. How many features shipped? How much new code entered the codebase? Now ask: how much of that new code could your team explain, line by line, without investing time and effort reading it, and not a function but entire modules and sometime architecture and latent requirements injected by the AI? 
The gap between those two numbers — that's your epistemic debt.

The formula also reveals a personnel risk. When Cs rises far above Gc, individual developers become what Prather et al. (2026) call **"Fragile Experts"** — engineers whose high *functional utility* (the ability to deliver code quickly with AI assistance) masks a critically low *corrective competence* (the ability to fix the code when it breaks). The formula captures the systemic condition, while the Fragile Expert is its human manifestation.

### Decomposing Across Abstraction Layers

Building on Ngabang's formula, I propose an expansion that makes the abstraction layer and recovery cost explicit. The formula above treats system complexity and cognitive grasp as single values. In practice, both are distributed across abstraction layers with different economic implications as shown by Barry Boehm's Cost of Change Curve — requirements (L4), architecture (L3), design (L2), and implementation (L1). Decomposing reveals where debt actually lives:

**Ed = Σ_k ∫[0 to T] (Cs_k(t) - Gc_k(t)) dt**

Where k ranges over abstraction layers. Each layer contributes independently to total epistemic debt, and — crucially — each layer has a different recovery cost.

### The Recovery Cost

To close an epistemic gap, a team must invest recovery time τ_k at each layer. Let t₀ be the moment the team acknowledge the issue and decide to invest in recovery, to invest in recovery — the point at which they recognize the gap and begin the work of understanding. At t₀, the team already has some level of understanding Gc_k(t₀), but it falls short of system complexity Cs_k. If understanding grows proportionally with effort:

**Gc_k(τ) = Gc_k(t₀) + r_k · τ_k**

Where r_k is the learning rate at layer k. The time needed to fully close the gap at a given layer — that is, for Gc_k to reach Cs_k — can be derived by setting Gc_k(τ) = Cs_k and solving for τ_k:

**Gc_k(t₀) + r_k · τ_k = Cs_k**

**τ_k = (Cs_k - Gc_k(t₀)) / r_k**

The numerator is the gap (how much understanding is missing at t₀); the denominator is the learning rate (how fast the team closes it). Bigger gap or slower learning means more recovery time. Note that this assumes the gap must be fully closed — that Gc_k must reach Cs_k exactly. In practice, some subdomains tolerate a margin of ignorance: a team may not need to understand every detail of a generic CRUD module the way it needs to understand core business logic. We'll return to this tolerance factor and what determines it when we examine how domain boundaries shape recovery priorities using a Domain Driven Design approach.

The total recovery time across all layers:

**T_recovery = Σ_k τ_k = Σ_k (Cs_k - Gc_k(t₀)) / r_k**

**This formula assumes recovery proceeds top-down:** from requirements (L4) down to implementation (L1) for the scope and components the understanding is needed. So that by the time a team addresses a lower layer, the higher layers that give it meaning are already understood. 

Under that assumption, each τ_k reflects a genuine learning rate and the total is a simple sum. In practice, teams that attempt bottom-up recovery — debugging implementation before understanding the requirement behind it — find that r_k at lower layers is artificially depressed: you can't truly close an L1 gap if the L3 or L4 gap above it remains open. The effective cost in that case exceeds T_recovery because understanding must be reworked once the higher-layer gap is eventually addressed.

This ordering effect reinforces Boehm's Cost of Change Curve: r_k decreases as k increases — recovering understanding at the implementation level (L1) might take minutes, given the higher layers are understood; recovering a misaligned requirement (L4) might take several hours to reverse engineer the code that was generated to implement it.

### When Recovery Outweighs AI Speed

T_recovery tells us how long it takes to *learn* what we don't understand, but learning isn't the only cost. Recovering understanding at a higher layer often invalidates work already done at the layers below it. Discover a requirements misunderstanding (L4) and you don't just spend τ_4 relearning the requirement — you may also have to re-recover the architecture, design, and implementation that were built on the wrong assumption.

This cascade gives us a cost multiplier that emerges directly from the recovery model. When closing a gap at layer k triggers re-recovery of all layers below it, the effective cost is not just τ_k but the sum of recovery times from L1 up to k:

**C_k = Σ_{j=1}^{k} τ_j**

The cost multiplier at each layer is therefore:

**c_k = C_k / τ_k = (Σ_{j=1}^{k} τ_j) / τ_k**

At L1, c_1 = 1 — recovery is local, no downstream rework. At higher layers, c_k grows because closing the gap forces re-recovery of every layer below. The exact values depend on the team's gap sizes and learning rates, but for typical projects — where r_k decreases sharply with abstraction — they approximate the order-of-magnitude escalation Boehm observed empirically.

With this, we can state the critical economic question. Let **δ** be the development time saved by AI-assisted generation. The net benefit is:

**Net benefit = δ - Σ_k c_k · τ_k**

AI speed is outweighed when:

**Σ_k c_k · τ_k > δ**

In plain language: *the time you saved generating code is consumed — and then exceeded — by the time needed to understand what was generated, multiplied by the rework it triggers at every layer below.* A team that generates 400 lines of implementation code (L1) and recovers understanding cheaply may still benefit. A team that accepts AI-generated architecture (L3) or discovers a requirements mismatch woven through the codebase (L4) may find that the recovery cost dwarfs the original time savings.

This is why the level of abstraction at which epistemic debt is incurred matters more than the volume of code generated.

### The Importance of t₀

The break-even condition reveals a lever that teams can actually pull: **when** they discover the gap matters as much as **how large** it is. The earlier t₀ occurs — the earlier a team recognizes that Gc_k has fallen behind Cs_k — the smaller the accumulated gap (Cs_k - Gc_k(t₀)) and the cheaper the recovery.

This is the fail-fast principle applied to epistemic debt. Deterministic mechanisms — practices that force understanding gaps to surface early — effectively shift t₀ leftward in time. The earlier you catch the gap, the less it costs to close. Examples of such mechanisms are:

- **End-to-end tests of requirements** surface misalignment at L4 before it propagates downward
- **Architectural fitness functions** catch structural drift at L3 before it becomes embedded
- **Integration tests for contracts** verify design assumptions at L2 before implementation hardens around them
- **Domain-Driven Design bounded contexts** constrain the scope at which debt can accumulate at any layer, forcing humans to specifying context and boundaries for the LLM.

Ngabang (2026) proposes a complementary mechanism: the **"Cognitive Ratchet,"** which shifts t₀ to commit-time itself — do not commit AI-generated code until you can explain it back to the AI. This closes the loop on cognitive outsourcing by ensuring the developer has converted the AI's output into their own mental representation before it enters the codebase.

Without these mechanisms, t₀ defaults to the moment the system fails in production, when the gap is widest and c_k is at its maximum. With them, t₀ shifts to design time, review time, or at worst integration time, when the gap is still narrow and recovery is affordable.

The goal is not to eliminate epistemic debt entirely — that would mean forfeiting the speed advantage of AI-assisted development. The goal is to keep **Σ_k c_k · τ_k < δ**: to ensure that recovery costs never exceed the time saved. Deterministic mechanisms achieve this by catching gaps at lower abstraction layers and earlier in the process, where c_k is small and τ_k is short. Later articles in this series will examine these mechanisms in detail.[^1]

[^1]: The linear recovery model assumes understanding grows proportionally with effort. A more realistic model uses logarithmic growth: **Gc_k(τ) = Gc_k(t₀) + α_k · ln(1 + β_k · τ_k)**, where α_k scales total learnable understanding and β_k controls how fast diminishing returns set in. Under this model, recovery time becomes **τ_k = (e^((Cs_k - Gc_k(t₀)) / α_k) - 1) / β_k** — note the exponential. As the gap widens, recovery cost doesn't just grow linearly; it explodes. A small epistemic gap is cheap to close, but once it passes a threshold, recovery becomes impractical — Ngabang (2026) argues the system effectively becomes "Legacy Code the moment it is written," unmaintainable and opaque to its own creators. The linear model is sufficient for the argument here; the logarithmic model strengthens it.

## Epistemic Credit: The Buffer

The inverse concept matters for the same economic reason. **Epistemic Credit (Ce)** represents surplus understanding — when your team's cognitive grasp *exceeds* system complexity: **Ce = ∫[0 to T] (Gc(t) - Cs(t)) dt**. When you have epistemic credit, you have a buffer. You can absorb new complexity without immediately falling into debt. A team that deeply understands its architecture can accept an LLM-generated module and integrate it safely — because they know the boundaries, the invariants, the places where a subtle mistake would cascade. Teams build epistemic credit through human review, deliberate simplification (reducing Cs while maintaining Gc), and knowledge transfer. The practical implication: teams with accumulated credit can safely accept AI-generated complexity. Teams without it cannot — every new module pushes them deeper into debt.

## How Epistemic Debt Differs from Technical Debt

The analogy to technical debt is deliberate, but the differences are critical. Conflating them leads to the wrong interventions.

| Dimension | Technical Debt | Epistemic Debt |
|-----------|---------------|----------------|
| **What accumulates** | Code quality issues, shortcuts, workarounds | Understanding gaps, comprehension deficits |
| **What pays it down** | Refactoring, code cleanup | Learning, documentation, knowledge transfer |
| **Visibility** | Code metrics, static analysis (though "technical lag" from outdated dependencies can be equally invisible — González-Barahona et al., 2026) | Bus factor, onboarding time, incident diagnosis |
| **Consequences of default** | Maintenance burden, slower changes | Catastrophic blind spots, production incidents, security exposure |
| **Speed of accumulation** | Gradual (linear with velocity) | Exponential with AI (entire modules in hours) |
| **Who it affects** | Individual developers (local pain) | Entire team (systemic risk) |

The deepest distinction is in the compounding dynamics. Technical debt at one boundary can be corrected at the next. Poor requirements can still lead to good implementation if the engineer understands the domain. But epistemic debt compounds across boundaries. Unclear intent produces opaque code produces circular tests produces false confidence. By the time the system fails in production, the entire chain must be unwound to find the root cause.

One mechanism makes this compounding invisible: the **Green CI Trap.** When AI-generated tests validate AI-generated code, the result is circular confirmation — a state Ngabang (2026) calls "Verification Opacity." The CI pipeline shows green. Coverage metrics look healthy. But the tests may confirm the AI's *interpretation* of a requirement without validating the actual business need. This is why the deterministic mechanisms described earlier target *human understanding* rather than automated metrics.

## What Comes Next

The formula gives us a way to reason about epistemic debt. The economics tell us when it becomes costly. But what happens when that cost comes due?

In the next article, we'll look at what happens when epistemic debt defaults: the case studies are vivid, the industry data is sobering, and the pattern is clearer than most teams want to admit.

---

*Next in the series: **When Epistemic Debt Defaults** — three case studies and the industry data that says they aren't outliers.*

---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- Ngabang, K. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." viXra.org. https://vixra.org/pdf/2601.0013v1.pdf
- Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv. https://arxiv.org/html/2602.20206
- González-Barahona, J.M. et al. (2026). "Technical Lag as Latent Technical Debt: A Rapid Review." arXiv. https://arxiv.org/abs/2601.11693
- "Epistemic Debt: The Hidden Cost of AI Speed." Failing Fast. https://failingfast.io/ai-epistemic-debt/
- "Why AI Systems Create New Forms of Technical Debt." AlterSquare.io. https://altersquare.io/ai-systems-create-new-forms-technical-debt/
- "Panel: Technical Debt in the AI Era." ICSE 2026. https://conf.researchr.org/info/icse-2026/panels
- Fowler, M. "Design-First Collaboration." https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
- Fowler, M. "Knowledge Priming." https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html
