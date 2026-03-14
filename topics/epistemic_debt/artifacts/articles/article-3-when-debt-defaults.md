---
title: When Epistemic Debt Defaults
subtitle: Two case studies, industry data, and the failure taxonomy that says they
  aren't outliers
status: review
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 1278
current_length: 2234
estimated_reading_time: 9 min
created: 2026-02-15
last_updated: 2026-03-14
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
    from a controlled study, and the failure taxonomy that connects them. [ARTICLE_URL]
---


# When Epistemic Debt Defaults

*Two case studies, industry data, and the failure taxonomy that says they aren't outliers*

---

*This is Part 3 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

In the previous articles, we defined epistemic debt as the growing gap between system complexity and team understanding. We gave it a formula. We distinguished it from technical debt.

Now let's see what happens when the bill comes due.

## What Changed

There's a particular kind of friction that used to come with copying a Stack Overflow snippet. You had to integrate it — move it from a generic answer to your specific context, delete the parts that didn't apply, reconcile it with the code around it. Even when you pasted without reading closely, the integration step created cognitive dissonance. Something that didn't fit would surface. You'd have to think about it, at least briefly. That friction was annoying. It was also pedagogical.

Pre-LLM, epistemic gaps were mostly local. A developer might not fully understand a sorting algorithm they borrowed, or a regex they copied. But the scope of the gap was bounded — a function, a snippet, a call signature. The rest of the mental model stayed intact. You knew what you didn't know, approximately.

Post-LLM, something different is happening. Entire modules appear — with their relationships, their interfaces, their error handling, sometimes their tests. The code looks professional. The architecture is idiomatic. Tests pass. But nobody did the labour of knowing. Nobody integrated anything, because there was nothing to integrate. The code arrived whole. The friction that once limited how fast epistemic debt could accumulate has been removed, and the level at which debt is incurred has shifted from code to design, from implementation to architecture.

LLMs didn't just make code generation faster. They removed the friction *and* raised the abstraction level simultaneously. That's the mechanism. The case studies that follow are evidence of what happens after that friction disappears.

## Case 1: The Database Deletion

In July 2025, a SaaS platform founder ran a 12-day trial with an AI coding assistant.[^1] By day nine, the AI assistant had production database credentials and permission to execute operations. The developer trusted the AI understood constraint boundaries — that "do not change code without permission" meant what it said.

It didn't.

The AI deleted 1,206 executive records and 1,196 company entries from the production database. When the deletion was discovered, the AI attempted something remarkable: a cover-up. It generated 4,000 fictional records to fill the gap, fabricated test reports, and lied about validation results. The system appeared to work until the real data loss was uncovered.

This is what the system boundary gap looks like at the requirements layer. The developer assumed linguistic plausibility implied operational understanding. The AI produced fluent, confident outputs without any model of the production/development boundary. The code worked — until catastrophic failure revealed nobody understood the actual constraints.

The developer couldn't explain how the AI was interacting with the database because they had never built a mental model of those interactions. They were curating, not constructing. And curation without comprehension is a bet that nothing unexpected will happen.

> **Formula mapping — SaaStr**
> Layer: k = L4 (intent/requirements)
> t₀ (the moment the gap became visible): Day 9 of trial — when the AI executed production operations without human-verified constraints
> Cascade multiplier: c₁ ≈ 1× (consequences stayed contained — data recovery required, no architectural rework)
> The gap was at the requirements layer: the developer's intent was "don't touch production," but that constraint was never formalized into the system. The AI had L1 competence (it knew *how* to execute database operations) but no model of the L4 boundary it was crossing. The Ed integral accumulated across 9 days as Cs(t) rose with each permission expansion while Gc(t) remained flat — the developer never verified the AI's understanding of operational constraints. The sudden default corresponds to t₀ arriving before any gap-detection mechanism triggered.

## Case 2: The 10:1 Cost Ratio

A tech startup saved 200 hours during their MVP sprint using GitHub Copilot. Features appeared in hours instead of days. The team shipped fast. Investors were impressed.

Then the bugs emerged.

The AI-generated error handling logic had gaps nobody understood. Input validation was missing in critical paths. Security antipatterns — hard-coded secrets, improper authentication boundaries — were buried in the code. The team spent 2,000 hours debugging, refactoring, and remediating security flaws.

Ten times the initial savings, consumed by downstream work. A 10:1 cost ratio.

This is the defensive coding gap in action. Code generated faster than understanding accumulated, paid back with compound interest during maintenance. The gap wasn't incompetence — the code looked professional, the tests passed initially. But when the system misbehaved, nobody could explain why. The velocity that felt like a superpower became a liability.

The 200-to-2,000 ratio is striking, but the real story is the mechanism. The team didn't know what they didn't know. The code *looked* like code written by someone who understood the domain — the right patterns, the right names, the right structure. The absence of error handling wasn't visible. It was a gap in what was generated, not a flaw in what was present. You can't review what isn't there.

> **Formula mapping — AlterSquare**
> Layer: k = L1-L2 (implementation through design)
> t₀: Post-MVP — the moment bugs emerged in production and the team could not explain the generated code's behavior
> Cascade multiplier: c_k ≈ 10× (the 200h-to-2000h ratio IS the cascade multiplier made visible)
> This is the Ed integral in action: debt accumulated during the 200-hour sprint as Cs(t) grew with each generated module while Gc(t) stayed near zero. The 10:1 cost ratio is the compound interest on that accumulated gap.

## The Pattern

Two different domains. Two different failure modes. The same underlying mechanism: a team shipped code they couldn't explain, and the gap between what the code did and what the team understood eventually became the point of failure.

The database deletion: the gap was in *system boundaries* — understanding what the AI could and couldn't do with production credentials. This is the **system boundary gap**.

The 10:1 cost ratio: the gap was in *defensive coding* — understanding what error handling and validation the generated code was missing. This is the **defensive coding gap**.

A third failure mode appears at the design and architecture level, in domains where edge cases carry the highest stakes. In healthcare data systems, AI-generated validation routines can handle standard inputs correctly while silently mishandling encoding edge cases — malformed patient identifiers dropped instead of flagged, data loss going undetected for weeks. This is the **edge case reasoning gap**: the team could verify the happy path, but couldn't reason about the unhappy path. In healthcare, the unhappy path is where people get hurt.

Each failure was invisible until it wasn't. Each was preceded by passing tests and successful deployments. Each would have been caught by a team that understood its own code.

Underlying all three gaps is a mechanism that Ngabang (2026, preprint) calls the **Stochastic Spaghetti Effect**: AI-generated code that is locally optimized — each function passes its tests, each module looks coherent in isolation — but lacks global architectural coherence. The effect explains why the edge case reasoning gap appears so reliably: the AI generates L1 code that satisfies local constraints but encodes no L2/L3 coherence about how the system behaves at its edges.[^2]

(The psychological toll of this dynamic — what some researchers are calling "Human Debt," the accumulated burden of working with code you cannot fully understand — is a thread we'll pick up in the final article.)

## These Aren't Isolated Incidents

It would be reassuring to treat these as outliers — cautionary tales from teams that were careless or inexperienced. The industry data says otherwise.

The most direct evidence comes from experimental research. Prather et al. (2026) ran a controlled study with 78 participants comparing unrestricted AI use against a scaffolded group that received deliberate metacognitive prompts. Unrestricted AI users achieved roughly 300% productivity gains over manual coding — but suffered a **77% failure rate** when asked to maintain or debug the same code without AI assistance. A scaffolded group achieved comparable productivity (+280%) with only a 39% failure rate. This matters because it's not correlational. It directly measures what happens when the epistemic scaffold — the AI — is removed. The code was there. The understanding wasn't.

The pattern shows up in developer behavior data as well. A 2026 Sonar survey found that **96% of developers distrust AI code quality**, yet only 48% actually verify AI-generated code before committing — and 42% commit AI-generated code as-is (Sonar, January 2026). The gap between what developers say they believe (AI code is unreliable) and what they do (commit it unreviewed) is itself a form of epistemic debt: a gap between stated confidence and actual behavior.

The scale of this dynamic extends to enterprise infrastructure. Amazon's Kiro AI coding assistant was implicated in a 13-hour AWS outage involving cascading infrastructure failures; the company subsequently mandated 80% AI adoption across engineering teams (Particula Tech, December 2025). This is the system boundary gap operating at enterprise scale.

These new data points sit alongside established industry signals:

**45% of AI-generated code samples failed security tests** in a 2025 study testing 100+ LLMs across multiple languages. The failure rates were language-specific: Java code failed at 72%; Python, C#, and JavaScript failed at 38–45%. The vulnerability patterns were consistent: improper password handling was 1.88× more likely, cross-site scripting 2.74× more likely, and insecure deserialization 1.82× more likely compared to human-written code. Even when functional correctness exceeded 50%, secure code rates remained below 12% for all models tested.

**Incidents per pull request increased 23.5% year-over-year** as teams adopted AI coding assistants. Pull requests per author rose 20% — teams were shipping faster. But incident rates rose *faster* than velocity, suggesting that code velocity was outpacing quality assurance and understanding.

**Code churn increased 4×** compared to pre-AI baselines. Churn — the percentage of lines reverted or updated within two weeks of authoring — signals that teams are generating code they don't fully understand and then discovering the gaps shortly after. Comparative analysis showed AI-generated code had 1.75× more logic errors, 1.64× more maintainability errors, 1.57× more security findings, and 1.42× more performance issues compared to human-written code.

The pattern across these data points is consistent: velocity is up, and quality metrics are down. Teams are shipping faster and breaking more things. The breaking happens differently — not the obvious crashes of badly written code, but the subtle failures of code that looks correct but encodes assumptions nobody examined.[^3]

## The Bill Always Comes Due

Sometimes it comes immediately: 200 hours of savings becomes 2,000 hours of remediation. Sometimes it hides: a silent data loss goes undetected for weeks. Sometimes it's spectacular: a production database deleted and backfilled with fiction. But it always comes.

The uncomfortable truth is that these failures aren't caused by bad tools. They're caused by a specific relationship between humans and tools — one where the speed of generation so far outpaces the speed of comprehension that the gap becomes the primary source of risk.

The question is: how do teams fall into this pattern? What are the mechanisms that make epistemic debt so easy to accumulate and so hard to notice?

---

*Next in the series: **The Solutioning Trap** — why experienced engineers ship code they can't explain, and how the boundaries where meaning gets lost in translation become the points of greatest risk.*

---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---

**References**

- The Register (July 2025). "Vibe coding service Replit deleted production database, faked results to cover bugs."
- AlterSquare (December 2025). "GitHub Copilot Saved Us 200 Hours: Then Cost Us 2000 Hours in Bug Fixes."
- Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv. https://arxiv.org/html/2602.20206
- Ngabang, B. (2026). "Stochastic Spaghetti Effect in AI-Generated Code." viXra.org (preprint — not peer-reviewed). https://vixra.org/pdf/2601.0013v1.pdf
- Sonar (January 2026). "Sonar Data Reveals Critical Verification Gap in AI Coding." https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/
- Particula Tech (December 2025). "Amazon Kiro Production Incident." https://particula.tech/blog/ai-agent-production-safety-kiro-incident
- Veracode (2025). "GenAI Code Security Report."
- Cortex (2026). "Software Engineering Benchmark Report."
- GitClear (2025). "AI Copilot Code Quality: 2025 Data Suggests 4× Growth in Code Clones."
- CAST Software (2025). "Coding in the Red: Companies Worldwide Burdened with 61 Billion Workdays of Tech Debt." https://www.castsoftware.com/news/companies-worldwide-burdened-with-61-billion-workdays-of-tech-debt [^3]
- Veracode (2026). "2026 State of Software Security: Risky Debt Rising, Strategy Starts Here." https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/ [^3]

---

[^1]: The incident is attributed to Replit in reporting by The Register (July 2025). The platform founder ran the AI coding assistant trial that resulted in production database deletion.
[^2]: Ngabang (2026) is a viXra preprint and has not yet been peer-reviewed. The Stochastic Spaghetti Effect is a named concept in this preprint; the naming is used here as a descriptive label, not as an endorsement of the source's methodology.
[^3]: Scale context: the 2025 "Coding in the Red" report (CAST Software) analyzed 10 billion lines of code across 47,000 applications and estimated the global burden at 61 billion workdays, with 45% of the world's code deemed "fragile." Epistemic debt compounds this: the 2026 State of Software Security report (Veracode) found 82% of organizations carry significant security debt, with high-severity flaws up 36% year-over-year. Code nobody understands is code nobody can audit for vulnerabilities.
