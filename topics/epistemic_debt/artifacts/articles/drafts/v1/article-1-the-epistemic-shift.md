---
title: The Epistemic Shift
subtitle: When code generation outpaces code comprehension
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 976
current_length: 1249
estimated_reading_time: 5 min
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



# The Epistemic Shift

*The feeling of knowing without the labor of knowing*

---

*This is Part 1 of a 7-part series on epistemic debt — when AI generation outpaces human comprehension.*

---

Imagine the following scenario not so far from reality: a cold day in February 2020, my friend and coworker John asked me a question in GitHub PR review: "Hey Antonino, why did you use binary search here?" I thought for a bit, took my time to replay the chain of thoughts I had while typing the code and dodging the compiler errors, and responded: "Good question. Initially I started creating a map but then, while I was writing a unit test, I noticed that the dataset is guaranteed to be sorted! So I made a judgment call with a mini trade-off analysis in my mind and in this context, the memory overhead wasn't worth it for our scale, and moreover, in any case, we'll need range queries later." John thumbs up my comment and replies "makes sense to me!" and approves it. The reasoning, i.e., the chain of cause and effect *grounded in the specific context* of our assumptions, requirements and user needs, is clear.

Now fast forward to December 2025, still a cold day. Same question. I look at the code in the code review, frown a little bit and shamefully respond: "Good question. Well... Claude coded it actually 😊. The unit tests pass — almost 100% coverage. I checked the edge cases I could think of and it looked ok. It handles the main scenarios. I guess it's ok. If you want I can deep dive into the code and explain it better but we have a train of PRs dependent on this... LMK." John scans the implementation. It looks professional. The logic seems sound. He approves it. The team is accumulating epistemic debt.

Same question. Same code. Actually, the one from 2025 is "better" in the sense that it has more comments, unit tests and docstrings, it looks more "confident" and "professional". 
But different (epistemic) warrant: in 2020, the team knew — in the sense of being able to rebuild the chain of cause and effect that led to the code, in 2025, we gained speed and apparent "confidence" (Epistemia as Quattrociocchi et al. (2025) call it) but we lost the cognitive grasp over the system because we didn't do the labor of knowing.

## The Seventy-Year Rupture

For roughly seventy years, programming has been grounded in deterministic authorship. A human agent with specific intent constructs a logical artifact. Software, in this view, is the **crystallization of human reason**. The epistemic warrant — the justification for claiming to understand the code — derives from a causal chain of authorship. You know the system because it is the product of your cognitive labor.

LLMs introduce a rupture in this framework. A **probabilistic layer** now sits between human intent and machine execution. Code becomes the product of stochastic pattern matching across vast vector spaces rather than direct symbolic reasoning. The developer's role shifts from *construction* — being the architect of every decision — to, in the best-case scenarios, *curation* — reviewing and selecting from probabilistically-generated suggestions. In the worst-case scenarios, *generation* — accepting the code as is without understanding it. We are liquefying the crystallization of human reasoning with a probabilistic layer. 

The question is: how solid should be the artifact that we are building for the task at hand? Not all the tasks require the same level of solidity.

This is not a minor adjustment. It is a change in the epistemic relationship between developer and code, or in general between author and artifact. We are moving from a deterministic to a probabilistic paradigm, and there is no way to avoid it, but there are ways to tame it that we will explore in the following articles.

## The Feeling of Knowing

The primary risk is not only technical correctness. It is epistemic opacity: the LLM produces what we might call the "feeling of knowing" without the "labor of knowing" -- a condition Quattrociocchi et al. (2025) term **Epistemia**, which in turn produces **Epistemic Debt** (Ngabang, 2026).

**Epistemic Debt**, like **Technical Debt**, represents a future cost: not the cost of *changing* code, but the cost of *comprehending* it. When you ship code you cannot explain, you have not just delivered a feature — you have created a comprehension obligation that compounds over time.

The velocity is exponential rather than linear. LLMs remove the natural friction that once limited how fast teams could accumulate code they didn't understand.

## Epistemia

Quattrociocchi, Capraro, and Perc (2025) identified a broader pattern they call *Epistemia*: a structural condition where linguistic plausibility substitutes for epistemic evaluation. The system produces fluent, confident outputs without the internal machinery, i.e., the causal chain of cause and effect that was implied by the writing process, that makes reliability accountable. Without taming this process, you risk experiencing the possession of an answer without having traversed the process of forming a justified belief.

Understanding risks to become optional when generation is cheap.

This is the condition software engineering, and in general any other domain where we are using AI to generate artifacts, now finds itself in. Code follows conventions, uses proper names, handles the obvious cases. The surface plausibility is high enough that the absence of deep understanding goes unnoticed.

## What's at Stake

This isn't a theoretical concern. The term "epistemic debt" originated in manufacturing, where Ionescu, Schlund, and Schmidbauer (2020) used it to describe technical ignorance in smart manufacturing systems. Ngabang (2026) brought it into software engineering with a precise definition: epistemic debt is the divergence between system complexity and the developer's cognitive model of that system.

That divergence is growing. Faster than most teams realize.

The question isn't whether to use LLMs. It's whether we can maintain the good-enough epistemic ownership for that task while we do it.

---

*Next in the series: **Epistemic Debt: A New Lens** — a precise definition, a mathematical foundation, and why this isn't just technical debt by another name.*

---

---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." viXra preprint. https://vixra.org/pdf/2601.0013v1.pdf
- Quattrociocchi, W., Capraro, V., & Perc, M. (2025). "Epistemological Fault Lines Between Human and Artificial Intelligence." arXiv:2512.19466. https://arxiv.org/html/2512.19466
- [Epistemic Debt: The Hidden Cost of AI Speed](https://failingfast.io/ai-epistemic-debt/) by Ben Hall, 2026.
- [The Epistemology Crisis in AI-Assisted Development: When Not Knowing Becomes the New Normal](https://medium.com/data-science-collective/the-epistemology-crisis-in-ai-assisted-development-when-not-knowing-becomes-the-new-normal-fc8c8e2a1788) by Nguyen Ha Thanh, 2025.
- Ionescu, T.B., Schlund, S., & Schmidbauer, C. (2020). "Epistemic Debt: A Concept and Measure of Technical Ignorance in Smart Manufacturing." Springer. https://link.springer.com/chapter/10.1007/978-3-030-20040-4_8

