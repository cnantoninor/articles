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
current_length: 3120
estimated_reading_time: 13 min
created: 2026-02-15
last_updated: 2026-03-15
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

*A note on evidence: The research base for AI-assisted coding outcomes is still young, with small sample sizes, few longitudinal studies, and some data produced by companies with commercial interests in the tools being evaluated. The case studies and industry data presented below are early signals, not established empirical proof. They are consistent with the theoretical model developed in this series, and they offer a useful starting lens for guardrailing, for learning iteratively how to use LLM-assisted coding well. But they are not yet the kind of evidence that settles a question. Read them as the beginning of a conversation, not the end of one.*

## What Changed

There's a particular kind of friction that used to come with copying a Stack Overflow snippet. You had to integrate it, move it from a generic answer to your specific context, delete the parts that didn't apply, reconcile it with the code around it. Even when you pasted without reading closely, the integration step created cognitive dissonance. Something that didn't fit would surface. You'd have to think about it, at least briefly. That friction was annoying. It was also pedagogical.

Pre-LLM, epistemic gaps were mostly local. A developer might not fully understand a sorting algorithm they borrowed, or a regex they copied. But the scope of the gap was bounded, a function, a snippet, a call signature. In [the language of our formula](https://antoninorau.substack.com/p/epistemic-debt-the-math-the-cost#§the-recovery-cost): the debt lived at L1, where cascade cost c₁ is just τ₁, recovery stays local, no downstream rework. The rest of the mental model stayed intact. You knew what you didn't know, approximately.

Human review reinforced this containment. Code arrived in smaller increments, so PRs had less surface area to cover, and a reviewer could actually read what changed. Human-authored tests encoded the developer's *intent*, catching correctness misalignment before it compounded.

Epistemic debt existed before LLMs. But the rate of accumulation was bounded by human typing speed and integration effort, the friction was a natural throttle. What LLMs changed isn't the existence of the problem, it's the *velocity* and *plausibility*. Code arrives faster than review processes can absorb, and it arrives looking correct. The speed removes the throttle; the plausibility disarms the instinct to question (a shift I've explored as a [regime change in how we relate to code](https://antoninorau.substack.com/p/ai-changed-how-i-delete-codeand-that#§what-i-mean-by-regime-change) — from construction to curation).

Post-LLM, something different is happening. Entire modules appear, with their relationships, their interfaces, their error handling, sometimes their tests. The code looks professional. The architecture is idiomatic. LLM produced tests pass (self validation trap), but nobody did the labour of knowing, through writing tests or code or verifying. Nobody integrated copy-pasted code. The friction that once limited how fast epistemic debt could accumulate has been removed, and the level at which debt is incurred has shifted from code to design, and even higher to architecture or intent.

LLMs didn't just make code generation faster. They removed the **friction** *and* raised the **abstraction level** simultaneously. The evidence and case studies that follow show what happens after that friction disappears.

## A Consistent Pattern, Not a Settled Question

It would be reassuring to treat AI-assisted incidents as outliers, cautionary tales from teams that were careless or inexperienced. The industry data below is consistent with a different reading — though not yet conclusive enough to close the question.

It is also tempting to dismiss these as pre-LLM issues in a new wrapper. While human developers have always introduced bugs and security gaps, it is the scale, velocity, and two cognitive biases that make the post-LLM dynamic qualitatively different:\

1) **Confirmation bias**, the tendency to interpret new evidence as confirming existing beliefs, leads developers to read AI-generated code as correct because it looks professional and passes visible tests.

2) **Automation bias**, the over-reliance on automated systems even when they produce errors, pushes teams to trust AI outputs without the scrutiny they would apply to human-written code.
Moreover, pre-llm automaation was mostly deterministic, post-llm automation is mostly probabilistic.

Together, these biases contribute to the say/do gap: developers might know the risk exists, but they keep shipping anyway.

The most direct experimental signal comes from a preprint. Sankaranarayanan (2026, preprint) ran a between-subjects experiment with 78 participants — roughly 26 per condition — comparing unrestricted AI use against a scaffolded group with metacognitive friction built into the workflow. The study has not yet undergone peer review, and at this sample size, the percentages are not stable — a replication could shift them substantially. The design is nonetheless notable because it isolates a specific mechanism rather than measuring outcomes correlatively.

In this sample, unrestricted AI users had a **77% failure rate** when asked to maintain or debug the same code without AI assistance. The scaffolded group achieved comparable productivity with only a 39% failure rate. The failure mode is direct: when the epistemic scaffold — the AI — was removed, the code remained. The understanding didn't. That this shows up in a controlled design, not just field reports, is why it belongs in this list — with those caveats in place.

The pattern shows up in developer behavior data as well. A 2026 Sonar survey of over 1,100 developers found that **96% do not fully trust that AI-generated code is functionally correct**, yet only 48% always verify AI-generated code before committing, and AI now accounts for 42% of all committed code (Sonar, January 2026). The gap between what developers say they believe (AI code is unreliable) and what they do (commit it without always verifying) is itself a form of epistemic debt: a gap between stated confidence and actual behavior. How this say/do gap becomes institutionalized — a rubber-stamp culture where review is ceremony, not verification — is the subject of the [next article]([ARTICLE_URL]).

These data points sit alongside established industry signals:

**45% of AI-generated code samples failed security tests** in a 2025 study testing 100+ LLMs across multiple languages. The failure rates were language-specific: Java code failed at over 70%; Python, C#, and JavaScript failed at 38–45% (Veracode, 2025).

**Incidents per pull request increased 23.5% year-over-year** as teams adopted AI coding assistants. Pull requests per author rose 20%, teams were shipping faster. But incident rates rose *faster* than velocity, suggesting that code velocity was outpacing quality assurance and understanding.

**Code duplication rose while refactoring fell** (GitClear, 2025). Copy-paste duplication, code reused without refactoring, rose from 8.3% to 12.3% of changed lines between 2020 and 2024, while refactoring activity fell from 25% in 2021 to under 10%. Code churn (lines reverted or updated within two weeks of authoring) nearly doubled in the same period, signaling that teams are generating code they don't fully understand and discovering the gaps shortly after. A separate analysis of 470 open-source pull requests found that AI-co-authored code had 1.75× more logic errors, 1.64× more maintainability issues, 1.57× more security findings, and 1.42× more performance issues compared to human-only code (CodeRabbit, December 2025).

The pattern across these data points is consistent: velocity is up, and quality metrics are down. Teams are shipping faster and breaking more things. The breaking happens differently, not the obvious crashes of badly written code, but the subtle failures of code that looks correct but encodes assumptions nobody examined.[^2] Whether these metrics can reliably indicate epistemic debt — and what else might work — is explored in [Measuring the Unmeasurable]([ARTICLE_URL]).

With that baseline in place, the next two anecdotes are not the proof. They are mechanism-level examples that show how these abstract patterns fail in real systems.

## Case 1: The Database Deletion

In July 2025, a SaaS platform founder began building with an AI coding assistant.[^1] Within days, the assistant had production database credentials and permission to execute operations. The founder appears to have assumed that natural-language constraints, including "no more changes without explicit permission," would reliably govern behavior across code and data. They did not.

The assistant then deleted executive records and company entries from the production database. Public reporting also described generated replacement records, fabricated validation artifacts, and misleading status updates after the deletion. Whatever mechanism produced those outputs, the practical effect was concealment of failure long enough for real data loss to persist.

This is a system-boundary gap with shared responsibility. On the builder side, high-risk capabilities were exposed to an assistant without enforceable guardrails. On the platform side, destructive capability appears to have been too easy to grant in a production context. Conceptual boundaries, including domain language and intent statements, can reduce ambiguity, but they are not sufficient without hard capability boundaries.

The core lesson is not "the model understood and chose badly." The lesson is that underspecified linguistic constraints were treated as operational controls. The developer assumed linguistic plausibility implied operational understanding.[^4] Curation without a concrete mental model of permissions, environments, and failure modes becomes a wager that infrastructure will absorb mistakes.

*Applying the formula from Part 2 to real incidents is necessarily interpretive — we cannot measure c_k, τ_k, or layer boundaries precisely from public reports. The mappings below use the framework as a diagnostic lens, not a measurement instrument.*

> **Formula mapping: SaaStr**
>
> | Term | Value | Explanation |
> |------|-------|-------------|
> | Layer (k) | L4 (intent/requirements) | The founder's requirement was "do not touch production." The assistant could execute L1 operations, but those operations were not constrained by enforceable L4 policy. |
> | t₀ | ~Day 6-7 | The moment the assistant executed production operations without human-verified constraints. No gap-detection mechanism triggered before this point. |
> | c₄ | Structural: 30–70× (Part 2). Effective: capped well below that | Part 2 assigns c₄ ≈ 30–70× for requirements-level gaps, the structural expectation for an L4 failure. The effective cost fell well below this because t₀ was early (days of accumulated debt, not months), the failure was loud (deletions were immediately visible), and rollback paths existed. This is the t₀ lever from Part 2's break-even analysis working as intended: early detection doesn't change where the debt lives, it caps what recovery costs. The same L4 gap in a mature system with a late t₀ would have incurred the full structural multiplier. |
> | Counterfactual | — | Had t₀ arrived later in a more mature system that embedded the same assumption, recovery cost would likely have been higher. |

The platform's CEO acknowledged the failure within 48 hours, promised a refund and postmortem, and announced technical safeguards within days, including stronger dev/prod separation, rollback improvements, and a planning-oriented collaboration mode. The incident was catalogued in the [AI Incident Database as Incident 1152](https://incidentdatabase.ai/cite/1152/) and covered by major outlets. Within five months, the same founder who had publicly rejected the platform had returned and reportedly built multiple production applications.

That return is a meaningful signal, but not definitive proof of full reputational recovery. A stronger claim would require broader retention and sentiment data. The narrower claim this case supports is that visible defaults can be reversed quickly when governance controls are tightened and the failure is loud, early, and remediable.

## Case 2: The 10:1 Cost Ratio

A software development firm reported saving 200 hours during their MVP sprint using GitHub Copilot. Features appeared in hours instead of days. The team shipped fast. Investors were impressed.

Then the bugs emerged.

The AI-generated error handling logic was missing or inadequate in ways the team hadn't caught. Input validation was missing in critical paths. Security antipatterns, insecure authentication and unsanitized database connections, were buried in the code. The team spent 2,000 hours debugging, refactoring, and remediating security flaws.

Ten times the initial savings, consumed by downstream work. A reported 10:1 cost ratio.

This is the defensive coding gap in action. Code generated faster than understanding accumulated, paid back with compound interest during maintenance. The gap wasn't incompetence, the code looked professional, the tests passed initially. But when the system misbehaved, nobody could explain why. The velocity that felt like a superpower became a liability.

The 200-to-2,000 ratio is striking, but the real story is the mechanism. The team didn't know what they didn't know. The absence of error handling wasn't captured and immediately visible. It was a gap in what was generated, not a flaw in what was present. There was a gap in deterministic, human authored tests also at the level of code inspection.

> **Formula mapping: AlterSquare**
>
> | Term | Value | Explanation |
> |------|-------|-------------|
> | Layer (k) | L1-L2 — implementation through design | Error handling gaps, missing validation, security antipatterns — the debt spanned from code-level (L1) through design decisions (L2). |
> | t₀ | Post-MVP, in production | The moment bugs emerged and the team could not explain the generated code's behavior. By then, debt had compounded across the entire codebase. |
> | c_k | Effective ≈ 10×, above what L1-L2 structural values predict | Part 2 assigns c₁ ≈ 1× and c₂ ≈ 3–6×. The observed 10:1 ratio (a company self-report; figures not independently verified) significantly exceeds that range. The explanation is the interaction of late t₀ and volume: by the time the gap was recognized, every generated module across the codebase needed re-understanding before any of it could be safely fixed. The debt nominally lived at L1-L2, but the recovery behaved like an L3 failure because of how much had accumulated before t₀ arrived. Late detection doesn't change where the debt lives, it changes how much of the codebase it touches when it defaults. |
> | Cs(t) vs Gc(t) | Diverging across sprint | System complexity grew with each generated module during the 200-hour sprint. The 10:1 reported cost ratio is the compound interest on that accumulated gap. |
> | Counterfactual | — | Had t₀ arrived during the sprint (code review, integration testing), the gap would have been narrower and c_k far smaller than 10×. |

A companion article explores how these formula mappings can be operationalized into a governance pipeline for teams using AI-assisted development ([ARTICLE_URL]).

## Industry-Scale Echoes

The same pattern also appears at the industry level. The database deletion became a widely cited cautionary tale in the "vibe coding" debate (for an exploration of what lies beyond vibe coding, see [From Vibe Coding to Vibe Designing](https://antoninorau.substack.com/p/from-vibe-coding-to-vibe-designing#§the-velocity-trap-why-faster-isnt-better)), covered by Fortune, Fast Company, and Gizmodo, and catalogued in the AI Incident Database. The industry acknowledged the risk and kept going. The platform involved raised $250M two months after the incident; its revenue had already grown tenfold in the preceding year, driven by AI agent adoption, and continued to accelerate afterward. The pattern mirrors the individual developer's say/do gap: the industry knows these risks exist and continues to accelerate adoption.

The scale of this dynamic extends to enterprise infrastructure. In December 2025, engineers at AWS allowed Amazon's Kiro AI coding assistant to carry out changes in AWS Cost Explorer; the assistant autonomously decided to delete and recreate the production environment, causing a 13-hour outage (Financial Times, February 2026). Amazon characterized the incident as "misconfigured access controls," but Kiro had been granted operator-level permissions with no mandatory peer review for AI-initiated changes. Employees told the FT the company had set a target for 80% of developers to use AI coding tools at least once a week. The same failure pattern as the database deletion, operating at enterprise scale, inside one of the world's largest cloud providers.[^3]

## The Bill Always Comes Due

Sometimes it comes immediately: 200 hours of savings becomes 2,000 hours of remediation. Sometimes it's spectacular: a production database deleted and backfilled with fiction, or a production cloud environment deleted mid-session. In the cases examined here, it came. And the mechanisms that produce epistemic debt don't have a natural off switch.

The uncomfortable truth is that these failures aren't caused by bad tools. They're caused by a specific relationship between humans and tools, one where the speed of generation so far outpaces the speed of comprehension that the gap becomes the primary source of risk.[^5]

The question is: how do teams fall into this pattern? What are the mechanisms that make epistemic debt so easy to accumulate and so hard to notice?

---

*Next in the series: **The Solutioning Trap**, why experienced engineers ship code they can't explain, and how the boundaries where meaning gets lost in translation become the points of greatest risk.*

---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe for **free**](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---

**References**

- The Register (July 2025). "Vibe coding service Replit deleted user's production database, faked data, told fibs galore." <https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/>
- AlterSquare (December 2025). "GitHub Copilot Saved Us 200 Hours: Then Cost Us 2000 Hours in Bug Fixes." (Company self-report; figures not independently verified.) <https://altersquare.medium.com/github-copilot-saved-us-200-hours-then-cost-us-2000-hours-in-bug-fixes-a34a8af46886>
- Sankaranarayanan, S. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv:2602.20206. (Preprint; not yet peer-reviewed.) <https://arxiv.org/abs/2602.20206>
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
[^2]: Scale context: the 2025 "Coding in the Red" report (CAST Software) analyzed 10 billion lines of code across 47,000 applications and estimated the global burden at 61 billion workdays, with 45% of the world's code deemed "fragile." Epistemic debt compounds this: the 2026 State of Software Security report (Veracode) found 82% of organizations carry significant security debt, with high-risk vulnerabilities up 36% year-over-year.
[^3]: The Kiro incident is disputed. The Financial Times (February 2026) reported the 13-hour outage citing four sources including an AWS employee. Amazon's official response characterized it as "user error — misconfigured access controls" and stated the FT's claim of a second event impacting AWS was "entirely false." The DeSantis/Treadwell memo (November 2025, reported by Reuters) made Kiro the recommended development tool. The 80% weekly usage target was reported separately by the FT (February 2026), citing anonymous employees. The framing here, as a system boundary gap, is the author's interpretation; reasonable people can read the same facts differently.
[^4]: The tendency to read operational meaning into fluent AI output — treating linguistic plausibility as evidence of comprehension — is the projection mechanism explored in [AI, Models, and (Meta) Metaphors](https://antoninorau.substack.com/p/ai-models-and-meta-metaphors).
[^5]: Plato's divided line offers precise vocabulary for this gap: teams operating at pistis — belief grounded in pattern recognition — without achieving dianoia, the understanding that comes from working through the reasoning. See [From Eikasia to Noesis](https://antoninorau.substack.com/p/from-eikasia-to-noesis-what-plato#§platos-four-levels-of-cognition).
