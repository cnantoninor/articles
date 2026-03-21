---
title: 'Beyond Software: The Universal Framework'
subtitle: Epistemic debt wherever humans collaborate with LLMs
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
- content and research professionals
target_length: 2085
current_length: 2127
estimated_reading_time: 9 min
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



# Beyond Software: The Universal Framework

*Epistemic debt wherever humans collaborate with LLMs*

---

*This is Part 7 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation). This is the final article.*

---

For six articles, we've explored epistemic debt through a software engineering lens. We defined it, showed what happens when it defaults, traced the mechanisms that cause it to accumulate, presented a framework for managing it, and confronted the difficulty of measuring it.

But the pattern is not unique to software. The Speed/Understanding/Reliability trade-off appears wherever LLMs augment human work. The framework generalizes — and the failure modes travel with it.

## The Triangle Generalizes

The structural properties of the trade-off triangle are universal:

- Three vertices represent fundamentally conflicting optimization targets
- Trade-off dynamics: maximizing any two constrains the third
- Lower-triangle positioning (Understanding + Reliability) always requires higher cognitive overhead
- The circular validation trap appears in every domain when an LLM validates its own output

What changes across domains is what each vertex *means*. The structure is invariant; the semantics adapt.

## Content Creation

| Vertex | Software Engineering | Content Creation |
|---|---|---|
| Speed | Code generation velocity | Content production rate |
| Understanding | Comprehension of system behavior | Grasp of subject matter and audience |
| Reliability | Verified correctness (tests pass) | Factual accuracy and coherent argument |

A journalist who prompts an LLM to draft an article about climate policy gains Speed but risks Understanding (do they grasp the nuances of what they're publishing?) and Reliability (are the claims accurate?). The trade-off triangle applies directly: fact-checking pulls toward Reliability, subject-matter expertise pulls toward Understanding, and editorial workflow amplifies all.

**The domain-specific failure mode:** voice drift and echo chambers. When LLMs generate content that sounds like the author but isn't grounded in the author's actual understanding, the result is indistinguishable from authentic writing — until someone asks the author to defend a specific claim. This parallels circular validation in software: the output *looks* verified, but the verification is illusory.

A subtler risk: over time, authors who rely on LLM drafting can lose their own voice. The generated text becomes the default register. The author's distinctive perspective — the thing that made their writing worth reading — erodes through disuse. This is epistemic debt in a different register: not the loss of understanding, but the loss of the capacity for original expression.

## LLM-as-Judge Systems

| Vertex | Software Engineering | LLM-as-Judge |
|---|---|---|
| Speed | Code generation velocity | Evaluation throughput |
| Understanding | Comprehension of system behavior | Evaluator's grasp of quality criteria |
| Reliability | Verified correctness | Consistent, calibrated judgments |

When organizations use LLMs to evaluate other LLM outputs — grading essays, scoring customer service interactions, filtering content, assessing search relevance — they face the same triangle. Speed (evaluate thousands of items per hour) trades against Understanding (does anyone understand *why* the evaluator scores as it does?) and Reliability (are the scores consistent and calibrated?).

**The domain-specific failure mode:** benchmark overfitting. An LLM-as-judge system that scores high on benchmarks may have learned the surface features of quality without capturing the underlying criteria. This parallels test overfitting in software — the system passes the tests without embodying the intent behind them.

The circular validation trap is especially acute here: an LLM evaluating LLM output with LLM-generated rubrics creates a closed system where no external epistemic check exists. Human calibration samples break this circle — just as human-authored integration tests break circular validation in code.

## Research and Analysis

| Vertex | Software Engineering | Research & Analysis |
|---|---|---|
| Speed | Code generation velocity | Literature review and synthesis rate |
| Understanding | Comprehension of system behavior | Deep grasp of field and methodology |
| Reliability | Verified correctness | Accurate citations and valid conclusions |

A researcher using LLMs to accelerate literature review gains Speed but risks hallucinated citations (Reliability) and shallow synthesis (Understanding). The generated review may read fluently — proper academic register, logical structure, apparent breadth — while missing the methodological nuances that an expert would catch.

**The domain-specific failure mode:** citation concentration and filter bubbles. LLMs tend to over-represent highly-cited work and under-represent recent or niche contributions. The resulting synthesis looks comprehensive but is actually narrow — a parallel to architectural drift in software, where the system appears complete but is missing critical components.

Strategy forces: systematic source verification pulls toward Reliability, domain expertise and critical reading pull toward Understanding, and structured research workflows (methodology design before data collection, preregistered analysis plans) amplify all.

## Decision Support

| Vertex | Software Engineering | Decision Support |
|---|---|---|
| Speed | Code generation velocity | Analysis and recommendation speed |
| Understanding | Comprehension of system behavior | Grasp of business context and assumptions |
| Reliability | Verified correctness | Accuracy of data and validity of conclusions |

An executive using LLM-generated market analysis for strategic decisions faces the same triangle. Fast analysis (Speed) trades against understanding the assumptions behind the recommendations (Understanding) and verifying the underlying data (Reliability).

**The domain-specific failure mode:** context blindness. An LLM generating strategic recommendations may miss political dynamics, institutional history, or stakeholder relationships that a human analyst would weight heavily. The analysis looks rigorous — numbers, frameworks, clear recommendations — while being disconnected from the organizational reality where it must be implemented. This parallels missing business requirements in software: technically correct, practically useless.

## Data Analysis

| Vertex | Software Engineering | Data Analysis |
|---|---|---|
| Speed | Code generation velocity | Data-to-insights time |
| Understanding | Comprehension of system behavior | Methodology understanding |
| Reliability | Verified correctness | Statistical validity and reproducibility |

**The domain-specific failure mode:** statistical fishing expeditions. An LLM can quickly generate dozens of analyses, finding patterns in noise through sheer throughput. The results *look* like insights — visualizations, statistical tests, narrative interpretations — but may not survive scrutiny. This parallels the solutioning trap: generating answers before understanding the question.

## Universal Meta-Patterns

Four patterns emerge across every domain where LLMs augment human work. They are the same patterns, expressed differently.

### 1. Human-in-the-Loop (HITL)

A human checkpoint that breaks the automation bias cycle.

In software: code review. In content: editorial review. In research: peer review. In evaluation: human calibration samples. In decision support: stakeholder review.

The mechanism is identical across domains — a human with domain understanding validates AI output against intent. The challenge is also identical: the pressure to rubber-stamp increases with volume. When the LLM generates faster than humans can review, the checkpoint becomes a bottleneck, and the temptation to skip it grows.

HITL is essential in 2026 for high-stakes domains. Regulators expect human checkpoints. But the checkpoint is only as good as the human's understanding. A rubber-stamp review is worse than no review — it provides false assurance.

### 2. Pre-Specification

Defining what "correct" means *before* generating output.

In software: TDD — write tests first. In content: editorial brief before drafting. In research: methodology design before data collection. In evaluation: rubric development before scoring. In decision support: defining success criteria before analysis.

Pre-specification is the universal antidote to the solutioning trap. It establishes epistemic scope upfront: what are we trying to achieve, what counts as success, what are the boundaries? Without pre-specification, the LLM fills the gap with generic plausibility — and generic plausibility is the substrate on which epistemic debt grows.

### 3. Retrieval-Augmented Generation (RAG)

Grounding AI output in verified sources.

In software: DDD context files that constrain LLM vocabulary. In content: fact-checking against primary sources. In research: citation verification against actual papers. In decision support: grounding recommendations in verified internal data.

RAG pulls toward both Understanding and Reliability by anchoring generation in curated knowledge. It is the default approach in 2026 for serious LLM applications. The principle: the LLM should generate *from* verified sources rather than *instead of* them.

### 4. Adversarial Testing

Deliberately trying to break the output.

In software: integration testing, chaos engineering. In content: fact-checking, devil's advocate review. In research: replication attempts, methodological critique. In evaluation: calibration against known-quality examples. In decision support: red team analysis.

Adversarial testing catches the failures that circular validation misses. The key: the adversary must have domain understanding. An LLM adversarially testing another LLM's output is just another form of circular validation.

## Applying the Triangle to Your Domain: A 5-Step Protocol

For practitioners in any LLM-augmented domain:

**Step 1: Define your vertices.** What does Speed mean in your context? What constitutes Understanding? How do you measure Reliability? Use the domain tables above as templates.

**Step 2: Identify your current position.** Where are you operating on the triangle right now? Most teams default to the Speed corner without realizing it. Be honest with yourself.

**Step 3: Classify your domains.** Not all work needs the same rigor. Identify which tasks are "core" (high stakes, long-lived, hard to reverse), "supporting" (moderate stakes, enables core work), or "generic" (low stakes, disposable, well-established patterns).

**Step 4: Select strategy forces.** For each classification, choose which meta-patterns to apply. Core domains need multiple forces pulling toward Understanding and Reliability. Generic domains can tolerate the Speed corner.

**Step 5: Make the trade-off explicit.** Use the triangle as a communication tool. "We're accepting upper-triangle positioning on this task" is a legitimate choice. "We drifted to upper-triangle on core functionality without deciding to" is epistemic debt by accident.

The framework is deliberately non-prescriptive. It doesn't tell you where to position — it gives you language for making the choice conscious.

## This Article, Self-Referentially

This series was written with LLM assistance. The triangle applied here too.

Speed: the entire series could have been generated in hours. Understanding: the author maintained epistemic ownership through research synthesis, multiple source verification, and deliberate structure. Reliability: citations verified, claims backed by research, alternative perspectives acknowledged.

Position: lower-triangle. This is thought leadership content where authentic voice and factual accuracy are critical for credibility. Speed was sacrificed for depth.

The meta-lesson: the framework applies to itself. You are reading an artifact produced through LLM-augmented work, where the author chose to prioritize Understanding and Reliability over Speed. Whether that choice was worthwhile is for you to judge.

## Closing the Series

The debate about LLMs is framed wrong — in software, in content, in research, in every domain they touch. "Will AI replace X?" is the wrong question. It assumes the risk is economic. The actual risk is epistemic.

LLMs are extraordinarily capable tools. They generate working output at unprecedented velocity. They lower barriers. They accelerate prototyping. These benefits are real. Dismissing them would be dishonest.

But the velocity comes with a cost that traditional productivity metrics don't capture. Every output generated faster than it can be understood adds to a comprehension deficit that compounds over time.

Perhaps LLMs are forcing us toward better epistemic practices by exposing a prior dependency on a false warrant — the assumption that authorship equals understanding. Code authorship was always a convenient fiction. We copied from Stack Overflow, used framework magic we didn't understand, inherited legacy code we never fully grasped. The epistemic warrant from authorship — "I know this because I made it" — was often weaker than we admitted. The same is true for writing, analysis, research, and evaluation.

The real warrant always came from verification, documentation, review, domain expertise, and production monitoring. LLMs just make the need for these practices more urgent.

Epistemic debt is not a reason to stop using LLMs. It is a reason to use them consciously. The teams that thrive in the LLM era will not be the fastest or the most AI-reliant. They will be the ones that maintain epistemic ownership — that can explain, at every level, not just *what* their output does but *why* it does it that way.

The trade-offs are real. Make them conscious.

---

*This concludes the Epistemic Debt series. For the full framework and all references, see the companion article: "Epistemic Debt: When AI Generation Outpaces Human Comprehension" (full-length version).*

---



---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe for **free**](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- All domain-specific analysis synthesized from patterns documented across the series.
- Ionescu, T.B., Schlund, S., & Schmidbauer, C. (2020). "Epistemic Debt: A Concept and Measure of Technical Ignorance in Smart Manufacturing." Springer.
- Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." viXra preprint.
- Quattrociocchi, W., Capraro, V., & Perc, M. (2025). "Epistemological Fault Lines Between Human and Artificial Intelligence." arXiv:2512.19466.
