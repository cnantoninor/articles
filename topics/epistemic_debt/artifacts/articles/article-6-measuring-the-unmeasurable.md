---
title: Measuring the Unmeasurable
subtitle: Proxy indicators, honest caveats, and what we don't yet know
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 1381
current_length: 1423
estimated_reading_time: 6 min
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


# Measuring the Unmeasurable

*Proxy indicators, honest caveats, and what we don't yet know*

---

*This is Part 6 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

If epistemic debt is real, can we measure it?

This is the most honest article in this series. The answer is: not well. Not yet. And that difficulty is itself revealing.

## The Measurement Paradox

The aspects of epistemic debt that are easiest to measure correlate weakly with the thing we actually care about. Code coverage is measurable — but 95% coverage with circular validation tells you nothing about understanding. Lines of code per developer is measurable — but velocity doesn't measure comprehension. Even "time to resolve incidents" conflates multiple factors: code quality, team experience, documentation quality, and system complexity.

The core problem: **understanding is a property of minds, not codebases.** You can measure code complexity (cyclomatic complexity, dependency depth). You can measure process outputs (coverage, churn, incident rates). But the gap between system complexity and team comprehension — Ngabang's Cs(t) - Gc(t) — lives in the heads of your engineers, not in your metrics dashboards.

As GitHub Copilot research discovered: "Net lines of code had essentially no relationship with the feeling of being more productive." Classic complexity metrics "do not accurately represent the mental effort involved in code comprehension." Documentation quality metrics remain an "elusive, holy-grail type task that almost no one has nailed down."

This doesn't mean measurement is impossible. It means we need proxy indicators and triangulation rather than a single metric.

## The Correlation-Causation Trap

Before discussing indicators, a warning. Every measurement suffers from multi-causality, and the correlation-causation trap is particularly dangerous in this domain.

**Example 1:** A team adopts AI coding assistants and their bug rate increases 30% over six months. Is this because of epistemic debt? Or because they're shipping 3× more code? Or because they hired three junior developers in that period? Or because they migrated to a new framework?

**Example 2:** A team's mean time to resolve incidents doubles after adopting LLM-assisted development. This could indicate epistemic debt — engineers can't diagnose code they don't understand. It could also indicate increased system complexity. Or it could reflect changes in incident classification methodology.

**Example 3:** PR review time increases 40%. Is this epistemic debt? The code could be genuinely complex (legitimate), or reviewers could lack domain knowledge (epistemic gap), or AI-generated code could be inscrutable (epistemic gap), or the review culture could be broken (not epistemic debt), or reviewers could simply be overloaded (not epistemic debt).

We can measure symptoms. We cannot isolate root causes.

Most studies of AI-assisted development (2024-2026) suffer from these confounding factors. The field is too new for longitudinal studies that control for team composition, project complexity, and organizational changes. We should treat early results as suggestive, not definitive.

## What We Can Measure Today

Despite the paradox, several proxy indicators provide useful signal — not individually, but when triangulated.

**Bus Factor Analysis.** The bus factor — how many team members must leave before critical knowledge is lost — has always been relevant, but LLM-assisted development changes its dynamics. Pre-LLM, bus factor tracked slowly because code was authored incrementally and knowledge distributed through pairing and review. Post-LLM, entire subsystems can be created by a single developer in a single session, creating knowledge silos faster than traditional development.

Practical approach: for each major subsystem, ask: "Who can explain how this works without reading the code?" If the answer is "the person who prompted the LLM to generate it," your bus factor for that subsystem is 1. If even they can't explain it, your bus factor is 0.

**Onboarding Velocity.** How long does it take a new team member to make their first meaningful contribution to a specific part of the codebase? If onboarding time increases despite stable codebase size, epistemic debt may be accumulating — the code is growing harder to understand per unit of functionality.

**Incident Diagnosis Time.** Not just "how long to fix" but "how long to understand." When a production incident occurs, track the time between "someone is looking at it" and "we understand the root cause." Rising diagnosis times, controlling for system complexity, suggest growing epistemic debt. The key distinction: time to *fix* includes implementation, which might be fast with LLMs. Time to *understand* is the epistemic debt signal.

**Code Archaeology Ratio.** The ratio of time spent understanding existing code versus writing new code. If engineers spend 80% of their time reading LLM-generated code they can't follow, the codebase has high epistemic debt. Self-reported surveys, while imperfect, can capture this: "What percentage of your time this sprint was spent understanding code you didn't write or don't remember writing?"

**Code Churn Rates.** Lines reverted or updated within two weeks of authoring. High churn suggests teams are generating code they don't fully understand and discovering gaps shortly after. Not conclusive alone — churn has many causes — but directionally useful.

## Triangulation

No single metric captures epistemic debt. But combining multiple indicators provides useful signal:

| Indicator | What It Measures | Epistemic Debt Signal |
|---|---|---|
| Bus factor | Knowledge concentration | Decreasing over time |
| Onboarding time | Code comprehensibility | Increasing per unit of functionality |
| Incident diagnosis time | System understanding depth | Rising diagnosis time, stable fix time |
| Code churn rate | Understanding gaps | High churn (frequent early rewrites) |
| Self-reported confidence | Subjective understanding | Declining confidence in "own" code |

When three or more indicators trend in the same direction, the signal is meaningful even if individual indicators are noisy.

## What's Emerging

Research at the frontier explores more direct measures of developer understanding, though none are practical for routine use yet.

**Eye-tracking studies** during code review show different gaze patterns for understood versus unfamiliar code. Developers spend longer on control flow statements in code they don't understand, and their fixation patterns differ measurably from code they authored.

**EEG research** proves that developer-reported comprehension correlates poorly with actual cognitive load. Studies show theta, alpha, and beta brain waves have highest discriminative power for identifying mentally demanding code. "EEG results reveal evidence of mental effort saturation as code complexity increases." This is significant: it suggests self-reported understanding metrics — surveys, confidence ratings — may systematically underestimate epistemic debt. The gap between what developers *think* they understand and what they *actually* understand may be larger than we assume.

**Think-aloud protocols** where developers explain code as they review it reveal understanding depth more directly than any automated metric.

These approaches are currently research-only — too expensive and intrusive for routine measurement. But they suggest a future where epistemic debt measurement becomes more direct. They also provide an uncomfortable validation: the problem is real, even if we can't yet measure it precisely.

## The Honest Caveat

Most data on AI-assisted development comes from 2024-2026 — a period of rapid adoption, tool evolution, and methodological immaturity. We should be transparent about what we don't know.

We don't have controlled longitudinal studies comparing epistemic debt accumulation rates between LLM-assisted and traditional development. We can't reliably separate epistemic debt effects from confounding factors like team growth, system complexity, and organizational change. Self-reported measures of understanding are subjective and subject to the Dunning-Kruger effect — the engineers with the most epistemic debt may be the least able to recognize it.

This uncertainty is not a reason to ignore the problem. The proxy indicators we have — bus factor, onboarding time, incident diagnosis, code churn — are sufficient to detect trends. The inability to measure precisely doesn't mean the phenomenon isn't real.

We couldn't precisely measure technical debt for decades, but we knew it when we saw it. Epistemic debt may follow the same trajectory.

---

*Next in the series: **Beyond Software** — epistemic debt wherever humans collaborate with LLMs, and a protocol for applying the trade-off triangle to any domain.*

---



---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- GitHub Copilot Research (2025). Developer productivity studies.
- EEG/Cognitive Load Studies (2025). Research on direct measurement of code comprehension difficulty.
- Documentation Quality Research (2025). Industry consensus on measurement challenges.
- Ngabang, L.A. (2026). "The Illusion of Competence."
- Sharafi, Z. et al. (2015). "A Systematic Literature Review on the Usage of Eye-Tracking in Software Engineering."
