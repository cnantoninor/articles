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
current_length: 2586
estimated_reading_time: 11 min
created: 2026-02-15
last_updated: 2026-03-08
published_date: null
publication_url: 'https://antoninorau.substack.com/p/epistemic-debt-the-math-the-cost'
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

In the previous article, we surfaced a concept emerging in academic and industry literature as *epistemic debt*: the accumulated opacity of code that works but the team can't understand without investing time and effort to reverse-engineer it. That labor can outweigh the speed benefits of AI-assisted development as we will try to show in this article.

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

Epistemic debt accumulates when your system grows more complex faster than your team's understanding keeps up. Cs(t) is "how complicated is our system?" Gc(t) is "how well do we actually understand it?" The integral, rather than a point-in-time snapshot, is deliberate: two teams can have the same gap today yet face very different recovery costs depending on how long that gap has been open. Code written during a period of low understanding becomes the foundation for everything built after it, depositing layers of opacity that compound silently.
A one-time measure would treat a gap opened yesterday the same as one six months old. The integral captures total exposure, which is what actually determines the cost of closing it.

This isn't just an abstraction. Think about the last six months on your team. How many features shipped? How much new code entered the codebase? Now ask: how much of that code could your team explain line by line without sitting down to study it — not a single function, but entire modules, architectural choices, and latent requirements the AI baked in? The gap between those two numbers, that's your epistemic debt.

The formula also reveals a personnel risk. When Cs rises far above Gc, individual developers become what Prather et al. (2026) call **"Fragile Experts"** — engineers whose high *functional utility* (delivering code quickly with AI assistance) masks a critically low *corrective competence* (fixing that code when it breaks). The formula captures the systemic condition; the Fragile Expert is its human face.

### Decomposing Across Abstraction Layers

Building on Ngabang's formula, I propose an expansion that makes abstraction layers and recovery cost explicit. The original formula treats system complexity and cognitive grasp as single values, but in practice both are distributed across layers — requirements (L4), architecture (L3), design (L2), and implementation (L1) — each with different economic implications, as Boehm's Cost of Change Curve shows. Decomposing reveals where debt actually lives:

**Ed = Σ_k ∫[0 to T] (Cs_k(t) - Gc_k(t)) dt**

Here k indexes the abstraction layers. Each one contributes independently to total epistemic debt, and each one costs a different amount to recover from.

### The Recovery Cost

Closing an epistemic gap takes time — call it τ_k for each layer. The clock starts at t₀: the moment the team recognizes the gap and decides to do something about it. At that point, they already understand the system to some degree — Gc_k(t₀) — but not enough to match its actual complexity Cs_k(t₀). Assuming understanding grows proportionally with effort:

**Gc_k(τ) = Gc_k(t₀) + r_k · τ_k**

Where r_k is the learning rate at layer k. To find how long recovery takes, set Gc_k(τ) = Cs_k(t₀) and solve:

**Gc_k(t₀) + r_k · τ_k = Cs_k(t₀)**

**τ_k = (Cs_k(t₀) - Gc_k(t₀)) / r_k**

Read it as: recovery time equals the size of the gap divided by how fast the team learns. Bigger gap or slower learning, more time. This assumes full closure — that Gc_k must reach Cs_k(t₀) exactly. In practice, some areas tolerate partial understanding: nobody needs to internalize every line of a generic CRUD module the way they need to understand core business logic. We'll return to this tolerance factor when we look at how domain boundaries shape recovery priorities through a Domain-Driven Design lens.

The total recovery time across all layers:

**T_recovery = Σ_k τ_k = Σ_k (Cs_k(t₀) - Gc_k(t₀)) / r_k**

**This formula assumes recovery proceeds top-down** — from requirements (L4) down to implementation (L1). By the time a team reaches a lower layer, the layers above it are already understood.

That assumption matters. Teams that try bottom-up recovery — debugging implementation before understanding the requirement behind it — hit a wall: you can't truly close an L1 gap when the L3 or L4 gap above it remains open. Learning rates at lower layers are artificially depressed, and the effective cost exceeds T_recovery because work must be redone once the higher-layer gap is eventually addressed.

This reinforces Boehm's Cost of Change Curve. Recovering understanding at the implementation level (L1) might take minutes if the higher layers are clear. Recovering a misaligned requirement (L4) might take hours of reverse-engineering the generated code.

### When Recovery Outweighs AI Speed

T_recovery tells you how long it takes to *learn* what you don't understand — but learning isn't the only cost. Recovering understanding at a higher layer often invalidates work already done below. Uncover a requirements misunderstanding (L4) and you don't just spend τ_4 relearning the requirement; you may have to re-recover the architecture, design, and implementation that were built on the wrong assumption.

That cascade acts as a cost multiplier. Close a gap at layer k and you may have to re-recover every layer beneath it. The effective cost is the sum of recovery times from L1 up to k:

**C_k = Σ_{j=1}^{k} τ_j**

(j runs from 1 to k: add up what it costs to re-learn each layer from implementation up to where the gap sits.)

We can express the same idea per-layer: define **c_k** as the dimensionless cascade multiplier at layer k — a weight that captures how much rework a gap at that layer triggers relative to a purely local fix. Boehm's empirical data on the cost of change gives illustrative orders of magnitude: a gap caught at implementation (L1) stays local, c₁ ≈ 1×; at design (L2), rework ripples into implementation, c₂ ≈ 3–6×; at architecture (L3), the cascade deepens, c₃ ≈ 10×; at requirements (L4), everything built on the wrong assumption must be revisited, c₄ ≈ 30–70×. Exact values vary by project and team; the point is the order-of-magnitude escalation as you climb layers.

At L1 the cost is just τ_1 — recovery stays local, no downstream rework. Climb to higher layers and the cost grows, because closing the gap forces re-recovery of everything below. Exact numbers depend on the team's gap sizes and learning rates; for typical projects, where r_k drops sharply with abstraction, they land in the same order-of-magnitude escalation Boehm saw empirically.

So: the economic question. Call **δ** the development time you saved by using AI. Net benefit is:

**Net benefit = δ - Σ_k c_k · τ_k**

AI speed turns into a net loss when:

**Σ_k c_k · τ_k > δ**

— when the total cost of understanding what was generated, including the rework it triggers at every layer below, exceeds the time you saved generating it. A team that generates 400 lines of implementation (L1) from solid human written specs can recover understanding cheaply and still come out ahead. A team that accepts AI-generated architecture (L3) or later finds a requirements mismatch woven through the codebase (L4) may discover that recovery cost dwarfs the original time savings.

That's why the level of abstraction at which epistemic debt is incurred matters more than the volume of code generated.

### The Importance of t₀

The break-even condition gives teams a lever they can actually use: **when** you discover the gap matters as much as **how large** it is. Catch it early — as soon as Gc_k has fallen behind Cs_k — and the accumulated gap (Cs_k(t₀) - Gc_k(t₀)) stays small and recovery stays cheap.

That’s fail-fast applied to epistemic debt. Deterministic mechanisms — practices that force understanding gaps to surface early — shift t₀ leftward. Examples:

- **End-to-end tests of requirements** surface misalignment at L4 before it propagates downward
- **Architectural fitness functions** catch structural drift at L3 before it becomes embedded
- **Integration tests for contracts** verify design assumptions at L2 before implementation hardens around them
- **Domain-Driven Design bounded contexts** constrain the scope at which debt can accumulate at any layer, forcing humans to specify context and boundaries for the LLM.

One caveat: each of these mechanisms must be authored with epistemic debt near zero (Ed ≈ 0) — that is, written or thoroughly reviewed by humans — or we risk the **circular confirmation trap**, e.g., when AI-generated tests validate AI-generated code, the result is circular confirmation — what Ngabang (2026) calls "Verification Opacity".

Ngabang (2026) proposes a complementary mechanism, the **"Cognitive Ratchet"**: shift t₀ to commit-time — don’t commit AI-generated code until you can explain it back to the AI. That closes the loop on cognitive outsourcing: the developer has turned the AI’s output into their own mental representation before it enters the codebase.

Without mechanisms like these, t₀ defaults to the moment the system fails in production, when the gap is widest and c_k is at its maximum. With them, t₀ moves to design time, review time, or at worst integration time, when the gap is still narrow and recovery is affordable.

The aim isn’t to eliminate epistemic debt entirely — that would mean giving up the speed gain of AI-assisted development. It’s to keep **Σ_k c_k · τ_k < δ**: recovery costs must not exceed the time saved. Deterministic mechanisms do that by catching gaps at lower abstraction layers and earlier in the process, where c_k is small and τ_k is short. Later articles in this series will look at these mechanisms in detail.[^1]

[^1]: The linear recovery model assumes understanding grows proportionally with effort. A more realistic model uses logarithmic growth: **Gc_k(τ) = Gc_k(t₀) + α_k · ln(1 + β_k · τ_k)**, where α_k scales total learnable understanding and β_k controls how fast diminishing returns set in. Under this model, recovery time becomes **τ_k = (e^((Cs_k(t₀) - Gc_k(t₀)) / α_k) - 1) / β_k** — note the exponential. As the gap widens, recovery cost doesn't just grow linearly; it explodes. A small epistemic gap is cheap to close, but once it passes a threshold, recovery becomes impractical — Ngabang (2026) argues the system effectively becomes "Legacy Code the moment it is written," unmaintainable and opaque to its own creators. The linear model is sufficient for the argument here; the logarithmic model strengthens it.

## Epistemic Credit: The Buffer

The flip side matters for the same economic reason. **Epistemic Credit (Ce)** is surplus understanding: your team's cognitive grasp *exceeds* system complexity, **Ce = ∫[0 to T] (Gc(t) - Cs(t)) dt**. That surplus is a buffer. You can take on new complexity without sliding straight into debt. A team that really understands its architecture can accept an LLM-generated module and integrate it safely — they know the boundaries, the invariants, where a subtle mistake would cascade. Credit accumulates through human review, deliberate simplification (reducing Cs while keeping Gc), and knowledge transfer. So: teams with credit can absorb AI-generated complexity. Teams without it can't; every new module deepens the hole.

## How Epistemic Debt Differs from Technical Debt

The analogy to technical debt is deliberate. The differences are what make it dangerous to treat them the same; wrong diagnosis, wrong fix.

| Dimension | Technical Debt | Epistemic Debt |
|-----------|---------------|----------------|
| **What accumulates** | Code quality issues, shortcuts, workarounds | Understanding gaps, comprehension deficits |
| **What pays it down** | Refactoring, code cleanup | Learning, documentation, knowledge transfer |
| **Visibility** | Code metrics, static analysis (though "technical lag" from outdated dependencies can be equally invisible — González-Barahona et al., 2026) | Bus factor, onboarding time, incident diagnosis |
| **Consequences of default** | Maintenance burden, slower changes | Catastrophic blind spots, production incidents, security exposure |
| **Speed of accumulation** | Gradual (linear with velocity) | Exponential with AI (entire modules in hours) |
| **Who it affects** | Individual developers or teams (local pain) | Entire teams or organizations (systemic risk) |

The sharpest difference is how it compounds. Technical debt at one boundary can often be corrected at the next — poor requirements can still yield a good implementation if the engineer understands the domain. Epistemic debt doesn't stay put. Unclear intent produces opaque code produces circular tests produces false confidence. When the system finally fails in production, you have to unwind the whole chain to find the root cause.

One mechanism keeps that compounding hidden: the **Green CI Trap.** AI-generated tests validating AI-generated code give you circular confirmation — what Ngabang (2026) calls "Verification Opacity." The pipeline is green. Coverage looks fine. The tests may be confirming the AI's *interpretation* of the requirement, not the actual business need. That's why the deterministic mechanisms we looked at earlier aim at *human understanding*, not at the metrics.

## What Comes Next

The formulas give us a way to reason about epistemic debt. The economics tell us when it becomes costly. But what happens when that cost comes due?

In the next article, we'll look at what happens when epistemic debt defaults.

---

*Next in the series: **When Epistemic Debt Defaults** — case studies and industry data that says they aren't outliers.*

---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- Ngabang, K. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." viXra.org. <https://vixra.org/pdf/2601.0013v1.pdf>
- Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv. <https://arxiv.org/html/2602.20206>
- González-Barahona, J.M. et al. (2026). "Technical Lag as Latent Technical Debt: A Rapid Review." arXiv. <https://arxiv.org/abs/2601.11693>
- "Epistemic Debt: The Hidden Cost of AI Speed." Failing Fast. <https://failingfast.io/ai-epistemic-debt/>
- "Why AI Systems Create New Forms of Technical Debt." AlterSquare.io. <https://altersquare.io/ai-systems-create-new-forms-technical-debt/>
- "Panel: Technical Debt in the AI Era." ICSE 2026. <https://conf.researchr.org/info/icse-2026/panels>
- Garg, R. "Design-First Collaboration." <https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html>
- Garg, R. "Knowledge Priming." <https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html>
