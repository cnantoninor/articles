---
title: 'Epistemic Debt: When AI Generation Outpaces Human Comprehension'
subtitle: A 7-part series on what we lose when content (code, research, decision support)
  writes itself
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
- content and research professionals
target_length: 800
current_length: 1117
estimated_reading_time: 5 min
created: 2026-02-15
last_updated: 2026-02-15
published_date: 2026-02-17
publication_url: https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation
social_teasers:
  linkedin: |
    We've shifted from building artifacts we can justify step by step to approving output that looks plausible. Tests pass, code runs — but who can explain the causal chain that produced it?

    I've been exploring what we lose when generation outpaces comprehension: epistemic debt. It compounds like technical debt but often stays invisible until something breaks. This 7-part series offers a framework to make the trade-off between AI-speed, understanding, and dependability conscious — in code, content, and research.

    If that gap between "it works" and "we know why" resonates, the overview and entry points are here: https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation

    #EpistemicDebt #AI #SoftwareEngineering #TechnicalDebt #LLM
  twitter: |
    Epistemic debt: when the artifact works but nobody can explain how or why. AI writes faster than we can digest — and the "feeling of knowing" replaces the labor of knowing. 7-part series on the trade-off we need to manage. https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation
  instagram_caption: |
    When code, copy, or analysis writes itself, we gain speed — and risk losing the "why." Epistemic debt is the work that functions but is hard to change because it's hard to explain. I wrote a 7-part series on what we lose and how to stay in the loop. Full piece in my Substack — link in bio.
  substack_notes: |
    Epistemic debt: when AI generation outpaces human comprehension and "it works" no longer means "we know why." A 7-part series on the shift from construction to curation, how the debt compounds, and a framework to balance AI-speed vs understanding vs dependability. https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation
---



# **Epistemic Debt: When AI Generation Outpaces Human Comprehension**

*A 7-part series on what we lose when content (code, research, decision support) writes itself*

---

*This is the series overview. Each article below will appear here as it's published.*

---

_The New Feeling of Knowing_

Your tests are passing and your code runs and doesn’t break in production - at least so far... 

Your article reads well or your data analysis research looks solid…

But how is it possible that nobody on the team can explain the causal chain that produced that “working” artifact? I.e. how it actually “works”?

LLMs generate code, copy, and analysis faster than we can digest and understand them, becuase we didn’t do the intellectual manual labor of translating the idea into artifacts, like coding, copywriting, and analyzing data. 

We’ve shifted from ideation and construction — building artifacts we can justify step by step — to  weak ideation and quick curation — approving output that looks plausible and right. 

The ideation phase was reinforced in the past by the construction phase, it was a virtuous circle that reinforce iteration over iteration. Now we need to find a different way to reinforce the ideation, the casual thinking that leads to the artifact, if we want to balance the quality of the artifact and the AI Speed of producing it.

That shift isn't dangerous per se, what is dangerous is the unawarness of it. The lack of a rigourous workflow to validate the output of the AI and stay in the loop of the causal chain of the artifact and hence the understanding of the artifact. 
There is a trade-off between AI-speed (Time-ot-Value) and minimizing epistemic debt that we must learn to manage.

The main problem is the [**Epistemic Debt**](https://vixra.org/pdf/2601.0013v1.pdf), work that functions but it's hard to change because it's hard to explain *how* and *why* it works. [Quattrociocchi and colleagues call *Epistemia*](https://www.pnas.org/doi/10.1073/pnas.2518443122) the illusion of knowledge when surface plausibility replaces verification — a sibling concept that shows also why epistemic debt so often goes unnoticed until something breaks. Like [Technical Debt](https://en.wikipedia.org/wiki/Technical_debt), it compounds. Unlike Technical Debt, it's often invisible until a crisis. 

This series offers a framework for making the trade-off between AI-speed, understanding, and dependability of the artifact (e.g. Reliability + Maintainability in software engineering terms) conscious. 

**Find your entry point**

You don't have to read the articles in order. If you're **NOT in software** and your work lives e.g. in content generation, research, or decision support, you can start with [**Article 1**](#§1-the-epistemic-shift-coming-soon) for the core shift, then skip ahead to [**7**](#§7-beyond-software-coming-soon) where the framework generalizes beyond code.

**Leaders** looking for an actionable framework and **Senior Practitioners** after the rigorous definition (how epistemic debt differs from "technical debt") share a natural path: [**1**](#§1-the-epistemic-shift-coming-soon), [**2**](#§2-epistemic-debt-a-new-lens-coming-soon), then [**5**](#§5-the-trade-off-triangle-coming-soon).

If you're **Evidence-First** — show me the case studies and data before the theory — go straight to [**3**](#§3-when-epistemic-debt-defaults-coming-soon), then circle back to [**1**](#§1-the-epistemic-shift-coming-soon) or [**2**](#§2-epistemic-debt-a-new-lens-coming-soon) for the conceptual grounding. Asking **"how did we get here?"** — vibe coding, automation bias, the mechanics of the trap — [**1**](#§1-the-epistemic-shift-coming-soon) and [**4**](#§4-the-solutioning-trap-coming-soon) are your articles.

**Skeptical about measurability?** Fair. [**6**](#§6-measuring-the-unmeasurable-coming-soon) lays out what we can and can't measure today; pair it with [**1**](#§1-the-epistemic-shift-coming-soon) or [**2**](#§2-epistemic-debt-a-new-lens-coming-soon) for the concept underneath. And if you **just want the hook** — the short opener that frames everything — [**1**](#§1-the-epistemic-shift-coming-soon) and [**2**](#§2-epistemic-debt-a-new-lens-coming-soon) will do it.

---

## 1. The Epistemic Shift — [Coming Soon]

*When generation outpaces comprehension*

A debatable mental experiment: two code reviews in 2020 vs. 2025. 

We ask the same question — "Why this approach?" — but we get radically different warrant. 

(Slow) deterministic authorship gives way to (fast) content - i.e. code - stochastic generation; "feeling of knowing" replaces "labor of knowing." Epistemic debt enters the vocabulary; the accumulation shift applies to code first and any domain where we approve output we didn't build or contributed in any phase of the process.

---

## 2. Epistemic Debt: The Math, The Cost, and Why It's Not Technical Debt — [Coming Soon]

*A framework for the understanding gap in AI-assisted work*

Definition: [Ngabang's formula](https://vixra.org/pdf/2601.0013v1.pdf), six-dimension comparison with technical debt. Why epistemic debt compounds across boundaries instead of staying contained. The conceptual foundation for the rest of the series; the logic carries to content generation and research analysis.

---

## 3. When Epistemic Debt Defaults — [Coming Soon]

*Three case studies and the industry data that says they aren't outliers*

Unwanted incidents: database deletion at scale, 10:1 cost ratio, silent data loss in healthcare. 45% security failure rates, incident increases per PR, 4× code churn. 
My personal examples and lessons learned.
Velocity without understanding creates debt and the bill always comes due. 
Article 7 maps this to other domains, like content generation and research analysis.

---

## 4. The Solutioning Trap — [Coming Soon]

*Why experienced practitioners ship work they can't explain*

Vibe coding is different from spec-driven development, and spec-driven development can be automated with LLMs, hence Vibe coding is not necessarily LLM assisted development.

Epistemic Debt accumulates at boundaries (intent → spec, spec → implementation) where meaning gets lost in translation. The solutioning trap, exhacerbated by automation bias, and AI speed, is the psychological mechanism that can cause this.

---

## 5. The Trade-off Triangle — [Coming Soon]

*A framework for conscious positioning in LLM-augmented work*

AI Speed vs. Understanding, AI Speed vs.Dependability (Reliability + Maintenability). 
You can't maximize all three. 
Strategy forces to control the trade-off: Domain Driven Design, human driven tests - especially end-to-end tests - epistemic reviews, structured workflows. 

---

## 6. Measuring the Unmeasurable — [Coming Soon]

*Proxy indicators, honest caveats, and what we don't yet know*

Understanding lives in minds, not in artifacts (code, documents, or dashboards). What we can measure today: bus factor, onboarding velocity, diagnosis time, "archaeology" ratio. 

Triangulation over a single metric. Honest caveats — we knew technical debt when we saw it long before we could measure it. But we can't measure understanding yet.

---

## 7. Beyond Software — [Coming Soon]

*Epistemic debt wherever humans collaborate with LLMs*

The triangle generalizes: content creation, LLM-as-judge, research, decision support, data analysis, etc. Same failure modes, same meta-patterns (human-in-the-loop, pre-specification, adversarial testing). Five-step protocol for any domain. 
Not "will AI replace us?" but "how do we maintain epistemic warrant?" balancing AI Speed vs. Understanding vs. Dependability.

---

The question isn't whether to use LLMs — in code, content, or analysis. It's whether we can keep ownership of what we claim to understand. Follow along as each piece goes live.


---

*If you found this article valuable, I'd love to hear your thoughts. Please [leave a comment](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation/comments), [share it](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation), and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
