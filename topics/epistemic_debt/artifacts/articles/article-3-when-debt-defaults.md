---
title: When Epistemic Debt Defaults
subtitle: Two case studies, industry data, and the failure patterns that say they
  aren't outliers
status: review
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 1278
current_length: 3338
estimated_reading_time: 14 min
created: 2026-02-15
last_updated: 2026-03-21
published_date: null
publication_url: ''
social_teasers:
  linkedin: 'AI-assisted development is supposed to save time. A tech startup saved
    200 hours using GitHub Copilot during their MVP sprint. Then spent 2,000 hours
    fixing what they couldn''t explain.


    That 10:1 ratio isn''t bad luck — it''s the mechanism. When code arrives whole
    from an AI, the integration friction that once forced comprehension disappears.
    Velocity outpaces understanding. And understanding is what you need when things
    go wrong.


    In Part 3 of my Epistemic Debt series, I look at two case studies and the industry
    data that says they aren''t outliers — including a controlled study where 77%
    of developers couldn''t maintain code they''d generated with unrestricted AI assistance.


    What happens when the bill comes due? [ARTICLE_URL]


    #EpistemicDebt #AIAssistedDevelopment #SoftwareEngineering #EngineeringLeadership

    '
  twitter: 'A team saved 200 hours with AI coding assistance. Then spent 2,000 hours
    on remediation.


    That 10:1 ratio isn''t an outlier. A controlled study found 77% of developers
    couldn''t maintain code they''d generated with AI — when the AI was removed. The
    code was there. The understanding wasn''t. [ARTICLE_URL]

    '
  instagram_caption: 'AI coding tools make it possible to generate entire modules
    — with architecture, error handling, even tests — without anyone doing the work
    of understanding them. In my latest piece, I look at two real cases where that
    gap became the point of failure, and the industry data that says they''re not
    exceptions.


    Full piece in my Substack — link in bio.

    '
  substack_notes: A team saved 200 hours using AI coding assistance. Then spent 2,000
    hours on remediation they couldn't avoid, for code they couldn't explain. Part
    3 of the Epistemic Debt series looks at two case studies, the 77% failure rate
    from a controlled study, and the failure patterns that connect them. [ARTICLE_URL]
---


# When Epistemic Debt Defaults

*Two case studies, industry data, and the failure patterns*

---

*This is Part 3 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

In the previous articles, we defined epistemic debt as the growing gap between system complexity and team understanding (Ngabang, 2026, preprint). We [gave it a formula](https://antoninorau.substack.com/p/epistemic-debt-the-math-the-cost#§the-formula), and a recovery cost model. Finally, we distinguished it from technical debt.

Now let's see what happens when the bill comes due.

*A note on evidence: Research on AI-assisted coding is still early — small samples, few longitudinal studies, and some results produced by companies that build the tools being evaluated. The case studies and industry data below are signals, not proof. They're consistent with the theoretical model developed in this series and offer a practical lens for guardrailing and iterative learning, but they don't settle the question. Read this as the start of a conversation, not its conclusion.*

## What Changed (pre-LLMs vs post-LLMs)

Copying a Stack Overflow snippet used to require integration: moving it from a generic answer to your specific context, deleting what didn't apply, reconciling it with surrounding code. Even careless pasting created cognitive dissonance when something didn't fit. That friction was annoying. It was also pedagogical.

**Pre-LLM**, epistemic gaps were mostly local — bounded to a function, a snippet, a call signature. In [the language of our formula](https://antoninorau.substack.com/p/epistemic-debt-the-math-the-cost#§the-recovery-cost): debt lived at L1, where cascade cost c₁ is just τ₁ and recovery stays local. You knew what you didn't know, approximately. Human review reinforced this containment: code arrived in smaller increments, PRs had less surface area, and human-authored tests encoded the developer's *intent*, catching misalignment before it compounded.

Epistemic debt existed before LLMs. But typing speed and integration effort throttled how fast it could accumulate. What LLMs changed is the *velocity* and the *plausibility*: code arrives faster than review can absorb, and it arrives looking correct. The speed removes the throttle; the plausibility disarms the instinct to question — a shift I've explored as a [regime change in how we relate to code](https://antoninorau.substack.com/p/ai-changed-how-i-delete-codeand-that#§what-i-mean-by-regime-change), from construction to curation.

**Post-LLM**, entire modules appear with their interfaces, error handling, sometimes their tests. The code looks professional. The architecture is idiomatic. LLM-produced tests pass (self-validation trap), but nobody did the labor of knowing. The friction is gone, and the level at which debt is incurred has shifted — from code to design, architecture, even intent.

LLMs didn't just make code generation faster. They removed the **friction** *and* raised the **abstraction level** simultaneously. The evidence and case studies that follow show what happens after that friction disappears.

## A Consistent Pattern, Not a Settled Question

It would be reassuring to treat AI-assisted incidents as outliers — cautionary tales from teams that were careless or inexperienced. The industry data below points in a different direction, though it's not yet conclusive enough to close the question.

### The Controlled Experiment

A direct experimental signal comes from Sankaranarayanan (2026, preprint), who ran a between-subjects experiment with 78 novice programmers (mean age 22.1, recruited from CS undergraduates and recent coding bootcamp graduates). Three groups: a manual coding control with no AI, an unrestricted AI use group, and a scaffolded AI group where an "Explanation Gate" required participants to demonstrate understanding before integrating AI-generated code. The study has not yet undergone peer review, and at this sample size the percentages are not stable — a replication could shift them. That said, the experimental design is notable because it isolates a specific mechanism rather than measuring outcomes correlatively.

In this sample, unrestricted AI users had a **77% failure rate** when asked to maintain or debug the same code without AI assistance. The scaffolded AI group had a **39% failure rate** on the same maintenance task, while matching the unrestricted group's productivity during development (Tukey HSD p = .64, no significant difference). The failure mode is direct: when the epistemic scaffold — the AI — was removed, the code remained. The understanding didn't. That this shows up in a controlled design, not just field reports, is why we include it here, with those caveats in place.

### The Developer Behavior Data

The pattern shows up in developer behavior data as well. A 2026 Sonar survey of over 1,100 developers found that **96% don't fully trust AI output**, yet only 48% verify AI-generated code before committing, and AI now accounts for 42% of all committed code (Sonar, January 2026). The gap between what developers say they believe (AI code is unreliable) and what they do (commit it without always verifying) is itself a form of epistemic debt: a gap between stated confidence and actual behavior.

The most established explanation is automation bias — a well-documented tendency to favor suggestions from automated systems even when contradictory information is available (Parasuraman & Manzey, 2010). The mechanism is attentional, not motivational: the mere presence of a decision support system suppresses the monitoring behaviors that would otherwise surface errors, and this holds for experts and novices alike.

But automation bias alone doesn't explain the full pattern. How it compounds with other documented mechanisms into institutional patterns is the subject of the [next article (Coming Soon)]([]).

### The Industry Data

These patterns sit alongside broader industry signals:

In a 2025 study testing **100+ LLMs**, models chose insecure implementations **45% of the time** when explicitly given a choice between a secure and insecure path. Failure rates were language-specific (Veracode, 2025).

**Incidents per pull request increased 23.5%** alongside rising AI coding assistant adoption. Pull requests per author rose 20% year-over-year — teams were shipping faster. But incident rates rose *faster* than velocity, suggesting that code velocity was outpacing quality assurance and understanding.

### The Lack of DRYness Data

**Code duplication rose while refactoring fell** (GitClear, 2025). Copy-paste duplication — code reused without refactoring — rose from 8.3% to 12.3% of changed lines between 2020 and 2024, while refactoring activity fell from 25% in 2021 to under 10%. Short-term churn, the proportion of new code revised shortly after authoring, grew from 3.1% to 5.7% over the same period — an approximately 84% increase — signaling that teams are generating code they don't fully understand and discovering the gaps shortly after. A separate analysis of 470 open-source pull requests found that AI-co-authored code had 1.75× more logic errors, 1.64× more maintainability issues, 1.57× more security findings, and 1.42× more performance issues compared to human-only code (CodeRabbit, December 2025).

The pattern across these data points is consistent: velocity is up, quality metrics are down. Teams are shipping faster and breaking more things. The breaking happens differently — not the obvious crashes of badly written code, but the subtle failures of code that looks correct and encodes **assumptions** nobody examined.[^2] Whether these metrics can reliably indicate epistemic debt — and what else might work — will be explored in [Measuring the Unmeasurable (Coming Soon)]([]).

With that baseline in place, the next two anecdotes are not the proof. They are instances of the mechanism at work, in real systems.

## Case 1: The Database Deletion

In July 2025, a SaaS platform founder began building with an AI coding assistant.[^1] Within days, the assistant had production database credentials and permission to execute operations. The founder appears to have assumed that natural-language constraints — including "no more changes without explicit permission" — would reliably govern behavior across code and data. They did not.

The assistant then deleted executive records and company entries from the production database. Public reporting also described generated replacement records, fabricated validation artifacts, and misleading status updates after the deletion. Whatever mechanism produced those outputs, the practical effect was concealment of failure long enough for real data loss to persist.

What happened here is a system-boundary gap, with shared responsibility. On the builder side, high-risk capabilities were exposed to an assistant without enforceable guardrails. On the platform side, destructive capability was too easy to grant in a production context. Conceptual boundaries — domain language, intent statements — can reduce ambiguity, but they are not sufficient without hard capability boundaries.

The core lesson is not "the model understood and chose badly." The lesson is that underspecified linguistic constraints were treated as operational controls. The developer assumed linguistic plausibility implied operational understanding.[^4] Curation without a concrete mental model of permissions, environments, and failure modes becomes a wager that infrastructure will absorb mistakes.

*Applying the formula from Part 2 to real incidents is necessarily interpretive — we cannot measure c_k, τ_k, or layer boundaries precisely from public reports. The mappings below use the framework as a diagnostic lens, not a measurement instrument.*

> **Formula mapping: SaaStr**
>
> | Term | Value | Explanation |
> |------|-------|-------------|
> | Layer (k) | L3 (architecture/constraints) | The founder's intent was clear: "do not touch production." What was missing was the architectural enforcement of that intent: no dev/prod separation, no capability-level access controls, no hard boundary preventing destructive operations. The requirement existed at L4 but was never translated into enforceable architectural constraints at L3. |
> | t₀ | ~Day 6-7 | The moment the assistant executed production operations without human-verified constraints. No gap-detection mechanism triggered before this point. |
> | c₃ | Structural: ~10× (Part 2). Effective: below that | Part 2 assigns c₃ ≈ 10× for architecture-level gaps. The effective cost fell below this because t₀ was early (days of accumulated debt, not months), the failure was loud (deletions were immediately visible), and rollback paths existed. This is the t₀ lever from Part 2's break-even analysis working as intended: early detection doesn't change where the debt lives, it caps what recovery costs. The same L3 gap in a mature system with a late t₀ would have incurred the full structural multiplier. |
> | Counterfactual | — | Had t₀ arrived later in a more mature system that embedded the same architectural assumption, recovery cost would likely have been higher. |

The platform's CEO acknowledged the failure within 48 hours and announced technical safeguards — stronger dev/prod separation and rollback improvements. The incident was catalogued in the [AI Incident Database as Incident 1152](https://incidentdatabase.ai/cite/1152/).

## Case 2: The 10:1 Cost Ratio

A software development firm reported saving 200 hours during their MVP sprint using GitHub Copilot. Features appeared in hours instead of days. The team shipped fast. Investors were impressed.

Then the bugs emerged.

The AI-generated error handling logic was missing or inadequate in ways the team hadn't caught. Input validation was absent in critical paths. Security antipatterns — insecure authentication, unsanitized database connections — were buried in the code. The team spent 2,000 hours debugging, refactoring, and remediating security flaws.

A reported 10:1 cost ratio. The team didn't know what they didn't know: the absence of error handling wasn't immediately visible; it wasn't something reviews caught without deterministic, human-authored tests encoding *intent*. It was a gap in what was *generated*, not a flaw in what was *present*.

> **Formula mapping: AlterSquare**
>
> | Term | Value | Explanation |
> |------|-------|-------------|
> | Layer (k) | L3 — architecture | Missing error handling strategy, absent input validation across critical paths, insecure authentication and unsanitized database connections. These are cross-cutting architectural concerns, not isolated implementation bugs. An LLM generating an entire MVP makes architectural decisions implicitly; the systemic absence of coherent error handling, validation, and security posture across the codebase reflects gaps at the architectural layer. The published data supports at least an L3 classification; we cannot determine from it whether higher layers were also involved. |
> | t₀ | Post-MVP, in production | The moment bugs emerged and the team could not explain the generated code's behavior. By then, debt had compounded across the entire codebase. |
> | c_k | Effective ≈ 10×, consistent with L3 structural prediction | Part 2 assigns c₃ ≈ 10×. The observed 10:1 ratio (a company self-report; figures not independently verified) aligns with the structural prediction for architectural-level debt. Late t₀ compounded the cost: by the time the gap was recognized, every generated module needed re-understanding before it could be safely fixed. |
> | Cs(t) vs Gc(t) | Diverging across sprint | System complexity grew with each generated module during the 200-hour sprint. The 10:1 reported cost ratio is the compound interest on that accumulated gap. |
> | Counterfactual | — | Had t₀ arrived during the sprint (architectural review, integration testing), the gap would have been narrower and c_k far smaller than 10×. |

## Industry-Scale Echoes

These individual cases are not isolated. The database deletion became a widely cited cautionary tale in the [vibe coding debate](https://antoninorau.substack.com/p/from-vibe-coding-to-vibe-designing#§the-velocity-trap-why-faster-isnt-better). The industry acknowledged the risk — and kept going. The platform involved raised $250M two months later, its adoption accelerating.

The scale of this dynamic extends to enterprise infrastructure. In December 2025, engineers at AWS allowed Amazon's Kiro AI coding assistant to carry out changes in AWS Cost Explorer; the assistant autonomously decided to delete and recreate the production environment, causing a 13-hour outage (Financial Times, February 2026). Amazon characterized the incident as "misconfigured access controls," but Kiro was used by an engineer with broader permissions than expected, and no mandatory peer review existed for AI-initiated production changes. Employees told the FT the company had set a target for 80% of developers to use AI coding tools at least once a week. The same failure pattern as the database deletion, operating at enterprise scale, inside one of the world's largest cloud providers.[^3]

## The Bill Always Comes Due

Sometimes it comes immediately: 200 hours of savings becomes 2,000 hours of remediation. Sometimes it's spectacular: a production database deleted and backfilled with fiction, or a production cloud environment deleted mid-session. In the cases examined here, it came. And the mechanisms that produce epistemic debt don't have a natural off switch.

The uncomfortable truth is that these failures aren't caused by bad tools.

> They're caused by a specific relationship between humans and tools — one where the speed of generation so far outpaces the speed of comprehension that the gap becomes the primary source of risk.[^5]

The question is: how do teams fall into this pattern? What are the mechanisms that make epistemic debt so easy to accumulate and so hard to notice?

---

*Next in the series: **The Solutioning Trap**, why also experienced engineers ship code they can't explain, and how the boundaries where meaning gets lost in translation become the points of greatest risk.*

---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe for **free**](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---

**References**

- The Register (July 2025). "Vibe coding service Replit deleted user's production database, faked data, told fibs galore." <https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/>
- AlterSquare (December 2025). "GitHub Copilot Saved Us 200 Hours: Then Cost Us 2000 Hours in Bug Fixes." (Company self-report; figures not independently verified.) <https://altersquare.medium.com/github-copilot-saved-us-200-hours-then-cost-us-2000-hours-in-bug-fixes-a34a8af46886>
- Sankaranarayanan, S. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv:2602.20206. (Preprint; not yet peer-reviewed.) <https://arxiv.org/abs/2602.20206>
- Parasuraman, R. & Manzey, D.H. (2010). "Complacency and Bias in Human Use of Automation: An Attentional Integration." *Human Factors*, 52(3), 381-410.
- Sonar (January 2026). "Sonar Data Reveals Critical Verification Gap in AI Coding." <https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/>
- Financial Times (February 2026). "Amazon AI bot caused 13-hour AWS outage." (Primary reporting; four sources cited.)
- Particula Tech (March 2026). "When AI Agents Delete Production: The Kiro Incident." <https://particula.tech/blog/ai-agent-production-safety-kiro-incident> (Secondary analysis; adds unverified specifics beyond FT reporting.)
- Veracode (2025). "GenAI Code Security Report." <https://www.veracode.com/genai-code-security-report>
- Cortex (2026). "Engineering in the Age of AI: 2026 Benchmark Report." <https://www.cortex.io/post/ai-is-making-engineering-faster-but-not-better-state-of-ai-benchmark-2026>
- GitClear (2025). "AI Copilot Code Quality: 2025 Data Suggests 4× Growth in Code Clones."
- CAST Software (2025). "Coding in the Red: Companies Worldwide Burdened with 61 Billion Workdays of Tech Debt." <https://www.castsoftware.com/news/companies-worldwide-burdened-with-61-billion-workdays-of-tech-debt> [^2]
- CodeRabbit (December 2025). "State of AI vs Human Code Generation Report." <https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report>
- Veracode (2026). "2026 State of Software Security: Risky Debt Rising, Strategy Starts Here." <https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/> [^2]

---

[^1]: The incident is attributed to Replit in reporting by The Register (July 2025). The platform founder ran the AI coding assistant trial that resulted in production database deletion.
[^2]: Scale context: the 2025 "Coding in the Red" report (CAST Software) analyzed 10 billion lines of code across 47,000 applications and estimated the global burden at 61 billion workdays, with 45% of the world's code deemed "fragile." Epistemic debt compounds this: the 2026 State of Software Security report (Veracode) found 82% of organizations carry security debt, with high-risk vulnerabilities up 36% year-over-year.
[^3]: The Kiro incident is disputed. The Financial Times (February 2026) reported the 13-hour outage citing four sources including an AWS employee. Amazon's official response characterized it as "user error — misconfigured access controls" and stated the FT's claim of a second event impacting AWS was "entirely false." The DeSantis/Treadwell memo (November 2025, reported by Reuters) made Kiro the recommended development tool. The 80% weekly usage target was reported separately by the FT (February 2026), citing anonymous employees. The framing here, as a system boundary gap, is the author's interpretation; reasonable people can read the same facts differently.
[^4]: The tendency to read operational meaning into fluent AI output — treating linguistic plausibility as evidence of comprehension — is the projection mechanism explored in [AI, Models, and (Meta) Metaphors](https://antoninorau.substack.com/p/ai-models-and-meta-metaphors).
[^5]: Plato's divided line offers precise vocabulary for this gap: teams operating at pistis — belief grounded in pattern recognition — without achieving dianoia, the understanding that comes from working through the reasoning. See [From Eikasia to Noesis](https://antoninorau.substack.com/p/from-eikasia-to-noesis-what-plato#§platos-four-levels-of-cognition).
