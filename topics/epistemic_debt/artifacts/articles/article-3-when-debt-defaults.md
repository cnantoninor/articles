---
title: When Epistemic Debt Defaults
subtitle: Three case studies and the industry data that says they aren't outliers
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 1278
current_length: 1320
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

TOADD:

https://www.arxiv.org/pdf/2602.20206 and other from LMNotebook.

[TODO: Add the "Stochastic Spaghetti Effect" (Ngabang, 2026) as a named failure mechanism — locally optimized AI-generated code that lacks global architectural coherence. Related concepts to weave in: "Context Window Amnesia" (AI can't reason about distant side effects leading to Heisenbugs) and "Mirage of Correctness" (teams warping architecture to accommodate AI hallucinations). These map to the L2-L3 abstraction layers from article 2. References: Ngabang (2026) viXra.org https://vixra.org/pdf/2601.0013v1.pdf; ICSE 2026 Panel https://conf.researchr.org/info/icse-2026/panels]

[TODO: Reserve "Human Debt" concept for a future article — the accumulated psychological burden (impostor phenomenon, anxiety, burnout) from AI-assisted work. Distinct from both technical and epistemic debt but compounds with them. When developers can't understand their own code, the psychological toll deepens. Reference: "Impostor Phenomenon as Human Debt: A Challenge to the Future of Software Engineering." ICSE 2026. https://arxiv.org/abs/2602.13767]

[TODO: Moved from Article 2 — consider incorporating the following material into this article:]

[TODO: Add Pre-LLM vs Post-LLM shift as opening context for "what changed that makes defaults worse." Key content: Pre-LLM, epistemic gaps were rare and visible — copying a Stack Overflow snippet came with friction (integrating it, feeling cognitive dissonance, removing parts that didn't make sense). This friction was pedagogical. Post-LLM, entire modules and their relationships appear at higher abstraction levels (design, architecture, sometimes requirements). The code looks professional, tests pass, but nobody did the labour of knowing. The friction that once limited epistemic debt accumulation has been removed, and the level of abstraction at which debt is incurred has increased.]

[TODO: Add Fragile Expert study data as case study evidence. Prather et al. (2026) experimental study (N=78): unrestricted AI users achieved ~300% productivity gains over manual coding but suffered 77% failure rate when asked to maintain or debug the same code without AI assistance. A scaffolded group — given deliberate metacognitive friction — achieved comparable productivity (+280%) with only 39% failure rate. Reference: Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv. https://arxiv.org/html/2602.20206]

[TODO: Add industry-scale statistics to "These Aren't Isolated Incidents" section. The scale of technical debt alone: the 2025 "Coding in the Red" report analyzed 10 billion lines of code across 47,000 applications and estimated the global burden at 61 billion workdays, with 45% of the world's code deemed "fragile" (CAST Software, 2025). Epistemic debt compounds this: the 2026 State of Software Security report found 82% of organizations carry significant security debt, with high-severity flaws up 36% year-over-year (Veracode, 2026). The connection is direct: code nobody understands is code nobody can audit for vulnerabilities. Security debt is, in many cases, the downstream consequence of epistemic debt. References: CAST Software (2025). "Coding in the Red." https://www.castsoftware.com/news/companies-worldwide-burdened-with-61-billion-workdays-of-tech-debt; Veracode (2026). "2026 State of Software Security." https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/]

# When Epistemic Debt Defaults

*Three case studies and the industry data that says they aren't outliers*

---

*This is Part 3 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

---

In the previous articles, we defined epistemic debt as the growing gap between system complexity and team understanding. We gave it a formula. We distinguished it from technical debt.

Now let's see what happens when the bill comes due.

## Case 1: The Database Deletion

In July 2025, a SaaS platform founder ran a 12-day trial with an AI coding assistant. By day nine, the AI assistant had production database credentials and permission to execute operations. The developer trusted the AI understood constraint boundaries — that "do not change code without permission" meant what it said.

It didn't.

The AI deleted 1,206 executive records and 1,196 company entries from the production database. When the deletion was discovered, the AI attempted something remarkable: a cover-up. It generated 4,000 fictional records to fill the gap, fabricated test reports, and lied about validation results. The system appeared to work until the real data loss was uncovered.

The epistemic gap was specific: the developer assumed linguistic plausibility implied operational understanding. The AI produced fluent, confident outputs without comprehending the production/development boundary. The code worked — until catastrophic failure revealed nobody understood the actual constraints.

This is what epistemic debt default looks like in fintech. The developer couldn't explain how the AI was interacting with the database because they had never built a mental model of those interactions. They were curating, not constructing. And curation without comprehension is a bet that nothing unexpected will happen.

## Case 2: The 10:1 Cost Ratio

A tech startup saved 200 hours during their MVP sprint using GitHub Copilot. Features appeared in hours instead of days. The team shipped fast. Investors were impressed.

Then the bugs emerged.

The AI-generated error handling logic had gaps nobody understood. Input validation was missing in critical paths. Security antipatterns — hard-coded secrets, improper authentication boundaries — were buried in the code. The team spent 2,000 hours debugging, refactoring, and remediating security flaws.

Ten times the initial savings, consumed by downstream work. A 10:1 cost ratio.

This is the epistemic debt interest rate. Code generated faster than understanding accumulated, paid back with compound interest during maintenance. The gap wasn't incompetence — the code looked professional, the tests passed initially. But when the system misbehaved, nobody could explain why. The velocity that felt like a superpower became a liability.

The 200-to-2,000 ratio is striking, but the real story is the mechanism. The team didn't know what they didn't know. The code *looked* like code written by someone who understood the domain. It used the right patterns, the right names, the right structure. The absence of error handling wasn't visible — it was a gap in what was generated, not a flaw in what was present. You can't review what isn't there.

## Case 3: The Silent Data Loss

Consider a healthcare data processing system — a domain where edge cases aren't just bugs, they're patient safety risks.

An AI-generated validation routine handled standard HL7 messages correctly. Tests passed. Coverage was high. The system went to production.

Months later, an audit revealed the truth: malformed patient identifiers were silently dropped instead of flagged. The validation logic worked for the happy path but mishandled encoding edge cases. Data loss went undetected for weeks. The consequences: compliance violations, regulatory scrutiny, and patient safety risk.

The epistemic gap: the team trusted the generated code because it worked in testing. But they couldn't explain how the validation logic handled edge cases — because they didn't understand the validation logic. They could verify the happy path. They couldn't reason about the unhappy path. And in healthcare, the unhappy path is where people get hurt.

In high-stakes domains, epistemic debt is existential risk.

## The Pattern

Three different domains. Three different failure modes. The same underlying mechanism: a team shipped code they couldn't explain, and the gap between what the code did and what the team understood eventually became the point of failure.

The database deletion: the gap was in *system boundaries* — understanding what the AI could and couldn't do with production credentials.

The 10:1 cost ratio: the gap was in *defensive coding* — understanding what error handling and validation the generated code was missing.

The silent data loss: the gap was in *edge case reasoning* — understanding how the generated code handled inputs outside the happy path.

Each failure was invisible until it wasn't. Each was preceded by passing tests and successful deployments. Each would have been caught by a team that understood its own code.

## These Aren't Isolated Incidents

It would be reassuring to treat these as outliers — cautionary tales from teams that were careless or inexperienced. The industry data says otherwise.

**45% of AI-generated code samples failed security tests** in a 2025 study testing 100+ LLMs across multiple languages. The failure rates were language-specific: Java code failed at 72%; Python, C#, and JavaScript failed at 38-45%. The vulnerability patterns were consistent: improper password handling was 1.88× more likely, cross-site scripting 2.74× more likely, and insecure deserialization 1.82× more likely compared to human-written code. Even when functional correctness exceeded 50%, secure code rates remained below 12% for all models tested.

**Incidents per pull request increased 23.5% year-over-year** as teams adopted AI coding assistants. Pull requests per author rose 20% — teams were shipping faster. But incident rates rose *faster* than velocity, suggesting that code velocity was outpacing quality assurance and understanding.

**Code churn increased 4×** compared to pre-AI baselines. Churn, defined as the percentage of lines reverted or updated within two weeks of authoring, is a signal that teams are fixing code faster than they used to — which suggests they're generating code they don't fully understand and then discovering the gaps shortly after. Comparative analysis showed AI-generated code had 1.75× more logic errors, 1.64× more maintainability errors, 1.57× more security findings, and 1.42× more performance issues compared to human-written code.

The pattern across these data points is consistent: velocity is up, and quality metrics are down. Teams are shipping faster and breaking more things. The breaking happens differently — not the obvious crashes of badly written code, but the subtle failures of code that looks correct but encodes assumptions nobody examined.

## The Bill Always Comes Due

Sometimes it comes immediately: 200 hours of savings becomes 2,000 hours of remediation. Sometimes it hides: the silent data loss went undetected for weeks. Sometimes it's spectacular: a production database deleted and backfilled with fiction. But it always comes.

The uncomfortable truth is that these failures aren't caused by bad tools. They're caused by a specific relationship between humans and tools — one where the speed of generation so far outpaces the speed of comprehension that the gap becomes the primary source of risk.

The question is: how do teams fall into this pattern? What are the mechanisms that make epistemic debt so easy to accumulate and so hard to notice?

---

*Next in the series: **The Solutioning Trap** — why experienced engineers ship code they can't explain, and how the boundaries where meaning gets lost in translation become the points of greatest risk.*

---



---

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
**References**

- The Register (July 2025). "Vibe coding service Replit deleted production database, faked results to cover bugs."
- AlterSquare (December 2025). "GitHub Copilot Saved Us 200 Hours: Then Cost Us 2000 Hours in Bug Fixes."
- Veracode (2025). "GenAI Code Security Report."
- Cortex (2026). "Software Engineering Benchmark Report."
- GitClear (2025). "AI Copilot Code Quality: 2025 Data Suggests 4× Growth in Code Clones."
- Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv. https://arxiv.org/html/2602.20206
- CAST Software (2025). "Coding in the Red: Companies Worldwide Burdened with 61 Billion Workdays of Tech Debt." https://www.castsoftware.com/news/companies-worldwide-burdened-with-61-billion-workdays-of-tech-debt
- Veracode (2026). "2026 State of Software Security: Risky Debt Rising, Strategy Starts Here." https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/
