# Epistemic Debt: The Hidden Cost of LLM-Generated Content with a Focus on Code

*A 7-part series on what we lose when content (code, research, decision support) writes itself*

---

*This is the series overview. Each article below will appear here as it’s published.*

---

Your tests pass. Your code works. Your article sounds good. Your research is sound. So why can’t anyone on your team explain how it actually works?

LLMs generate code, copy, and analysis faster than we can comprehend them. We’ve shifted from *construction* — building artifacts we can justify step by step — to *curation* — approving output that looks right. That shift has a name: **epistemic debt** — work that functions but nobody understands. (In software: code that runs but no one can vouch for. In content or research: output that reads well but the warrant is missing.) Like technical debt, it compounds. Unlike technical debt, it’s often invisible until a crisis. This series gives it a precise definition, shows where it comes from, and offers a framework for making the trade-off conscious. We use software engineering as the main lens; Article 7 generalizes to content, research, and decision support.

**Quick jump — find your entry point**

- **Not in software** — you work in content, research, or decision support and want to see the pattern in your domain. → **1** (hook, minimal jargon), then **7** (Beyond Software).
- **Engineering or content/research leader** — you want the actionable framework and how to position your team. → **1**, **2** (so the definition is clear), then **5** (The Trade-off Triangle).
- **Senior practitioner** (engineer, analyst, or writer) — you want a rigorous definition and how this differs from “technical debt” or “quality debt.” → **1** (context), then **2** (A New Lens); **5** if you want the practices.
- **Evidence-first** — you want case studies and data before theory (software-heavy examples, but the pattern is general). → **3** (When Epistemic Debt Defaults); **1** or **2** if you need the concept first.
- **“How did we get here?”** — vibe coding, automation bias, and where meaning gets lost (software-focused; parallels in **7**). → **1**, then **4** (The Solutioning Trap).
- **Skeptical about measurability** or want to know what we can actually measure today. → **1** or **2** (so the term is clear), then **6** (Measuring the Unmeasurable).
- **Just want the hook** — short, punchy opener (authorship and curation in any domain). → **1** (The Epistemic Shift); **2** if you want the rigorous definition next.

Here’s the full roadmap.

---

## 1. The Epistemic Shift — [Coming Soon]

*When generation outpaces comprehension*

Two code reviews: 2020 vs. 2025. Same question — “Why this approach?” — radically different warrant. We name the rupture: deterministic authorship giving way to probabilistic curation, and the “feeling of knowing” replacing the “labor of knowing.” Epistemic debt enters the vocabulary; the accumulation shift (localized → pervasive, visible → invisible, stigmatized → normalized) applies to code first and to any domain where we approve output we didn’t build. Sets the stage for everything that follows.

---

## 2. Epistemic Debt: A New Lens — [Coming Soon]

*A framework for the understanding gap in AI-assisted work*

Rigorous definition: Ngabang’s formula (from software), epistemic credit, and a six-dimension comparison with technical debt. Why epistemic debt compounds across boundaries instead of staying contained. The conceptual foundation for the rest of the series; the logic carries over to content and research.

---

## 3. When Epistemic Debt Defaults — [Coming Soon]

*Three case studies and the industry data that says they aren’t outliers*

Software-focused: database deletion at scale, a 10:1 cost ratio (hours saved vs. hours spent fixing), silent data loss in healthcare. Then the numbers: 45% security failure rates, incident increases per PR, 4× code churn. The pattern is general: velocity without understanding creates debt; the bill always comes due. Article 7 maps the same pattern to other domains.

---

## 4. The Solutioning Trap — [Coming Soon]

*Why experienced practitioners ship work they can’t explain*

Software frame: vibe coding, automation bias, rubber-stamp review. The junior developer crisis: who can still debug what they didn’t build? Where debt accumulates: at the boundaries (intent → spec, spec → implementation) where meaning gets lost in translation. The “how we got here” piece; the boundary pattern reappears in Article 7 for content and research.

---

## 5. The Trade-off Triangle — [Coming Soon]

*A framework for conscious positioning in LLM-augmented work*

Speed, Understanding, Reliability — you can’t maximize all three. The circular validation trap (e.g. LLM code + LLM tests = same blind spots; parallels in other domains in **7**), strategy forces (e.g. DDD, human E2E tests, epistemic review, structured workflows), and domain-based positioning. The one to bookmark; Article 7 gives the same triangle for content, research, and decision support.

---

## 6. Measuring the Unmeasurable — [Coming Soon]

*Proxy indicators, honest caveats, and what we don’t yet know*

Understanding lives in minds, not in artifacts (code, documents, or dashboards). What we can measure today: bus factor, onboarding velocity, diagnosis time, “archaeology” ratio (time understanding existing work vs. producing new). Triangulation over a single metric. Plus the honest caveats — and the reminder that we knew technical debt when we saw it long before we could measure it.

---

## 7. Beyond Software — [Coming Soon]

*Epistemic debt wherever humans collaborate with LLMs*

The triangle generalizes: content creation, LLM-as-judge, research, decision support, data analysis. Same failure modes, same meta-patterns (human-in-the-loop, pre-specification, RAG, adversarial testing). A five-step protocol for any domain, a self-referential close (this series applied the framework to itself), and the reframe: not “will AI replace us?” but “how do we maintain epistemic warrant?”

---

The question isn’t whether to use LLMs — in code, content, or analysis. It’s whether we can keep ownership of what we claim to understand. Follow along as each piece goes live.
