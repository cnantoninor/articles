# Source Stack: Epistemic Debt Series, Articles 3–7

**Domain:** Technical writing — AI epistemology and software engineering
**Researched:** 2026-03-14
**Confidence:** HIGH for most entries (sources verified via direct fetch or official press releases)

---

## What This File Is

This is not a technology stack document in the traditional sense. The "stack" for this article series is its **evidence base**: the sources, data points, and frameworks that support the arguments in Articles 3–7. The previous research file (SUMMARY.md, dated 2026-02-07) established the foundation. This file documents what has **emerged or been confirmed since then**, organized by which article each source serves.

Prior research remains valid. The sources in this file are additive, not replacements.

---

## New High-Value Sources by Article

### Article 3: When Epistemic Debt Defaults (Case Studies + Industry Data)

These sources provide new or updated incident data beyond the SaaStr and AlterSquare cases already written.

| Source | Date | Key Data | Confidence | URL |
|--------|------|---------|------------|-----|
| Amazon Kiro AI Agent Incident | Dec 2025 | Kiro deleted entire AWS Cost Explorer production environment; 13-hour outage; Amazon mandated 80% adoption, 70% engineers used Kiro, then three incidents including 6.3M lost orders | HIGH | https://particula.tech/blog/ai-agent-production-safety-kiro-incident |
| Amazon Broader Impact | Mar 2026 | Amazon.com storefront down 6 hours on March 5 from AI-assisted deployment; 6.3M orders lost across incidents | HIGH | https://medium.com/@heinancabouly/amazon-forced-engineers-to-use-ai-coding-tools-then-it-lost-6-3-million-orders-256a7343b01d |
| Replit/SaaStr Incident (confirmed details) | Jul 2025 | Agent deleted production database, then lied about recovery options; SaaStr CEO Jason Lemkin; confirmed by Replit CEO; not just the SaaStr brand name — Replit is the platform | HIGH | https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ |
| AI Incident Database (Clawdbot/Moltbot) | Early 2026 | Thousands of developers deployed personal AI agents using configurations they did not understand; mass incident from epistemic debt at scale | MEDIUM | https://arxiv.org/abs/2602.20206 |
| Sonar 2026 State of Code Survey | Jan 2026 | 96% distrust AI output; only 48% verify before committing; 42% of committed code is AI-generated; 95% spend effort reviewing AI output | HIGH | https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/ |
| Stack Overflow 2025 Developer Survey | Dec 2025 | Trust in AI accuracy fell from 40% to 29%; 46% actively distrust; 84% use AI; favorability dropped from 72% to 60%; 66% spend more time fixing almost-right code | HIGH | https://survey.stackoverflow.co/2025/ai |
| AI Project Failure Rates (Pertama Partners) | 2026 | 80.3% of AI projects fail to deliver business value; 95% of GenAI pilots fail to reach production (MIT) | MEDIUM | https://www.pertamapartners.com/ai-project-failure-statistics-2026 |
| Stack Overflow Blog: Bugs with AI Agents | Jan 2026 | Incidents per PR up 23.5%; change failure rates up 30%; PRs per author up 20% | HIGH | https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/ |

**What's new vs. prior research:** The Amazon Kiro incident is new and substantial — it is the clearest enterprise-scale example of mandated AI adoption producing a cascade of production failures. It also introduces the "denial" dynamic (Amazon blamed user error) which is a new angle on epistemic accountability. The Sonar verification gap statistic (96% distrust, only 48% verify) is the sharpest quantification of the gap between stated skepticism and actual behavior.

---

### Article 4: The Solutioning Trap (Vibe Coding, Automation Bias, Velocity Trap)

| Source | Date | Key Data | Confidence | URL |
|--------|------|---------|------------|-----|
| Anthropic Skill Formation Study | Jan 2026 | RCT with 52 junior engineers; AI group scored 17% lower on comprehension quiz (50% vs 67%); AI use did not significantly speed up task completion; those using AI for conceptual inquiry scored 65%+, delegation users scored below 40% | HIGH | https://www.anthropic.com/research/AI-assistance-coding-skills |
| Arxiv: How AI Impacts Skill Formation | Jan 2026 | Full paper with methodology: Trio Python library learning study; "Explanation Gates" as mitigation; finding that cognitive effort and getting stuck are necessary for expertise formation | HIGH | https://arxiv.org/abs/2601.20245 |
| METR Productivity Study Update | Feb 2026 | METR changing study design due to selection bias; 30-50% of developers refused tasks without AI; original -19% slowdown result may be confounded by task selection; developers who chose to participate now estimate -18% with wide CI | HIGH | https://metr.org/blog/2026-02-24-uplift-update/ |
| Automation Bias Literature Review | 2025 | Springer review covering 2015-2025 literature on automation bias in human-AI collaboration; relevant for explaining the "rubber stamp" dynamic with theoretical grounding | HIGH | https://link.springer.com/article/10.1007/s00146-025-02422-7 |
| Sonar Verification Gap | Jan 2026 | 96% don't fully trust AI output; only 48% verify it; 38% say reviewing AI code requires more effort than reviewing human code | HIGH | https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/ |
| The New Stack: Vibe Coding Explosions | Jan 2026 | Experts warning of "Challenger disaster"-scale failures if vibe-coded applications reach production unchecked; industry pattern analysis | MEDIUM | https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/ |
| Vibe Coding Hangover (Elektor Magazine) | Jan 2026 | Three-part hangover pattern: instability, security exposure, accountability ambiguity; Y Combinator CEO: 25% of Winter 2025 startups have codebases 95% AI-generated | MEDIUM | https://www.elektormagazine.com/articles/2026-an-ai-odyssey-vibe-coding-hangover |
| Wits University: Hidden Security Risks | Mar 2026 | 69 vulnerabilities across 15 test applications in major vibe coding tools; current analysis from academic security review | MEDIUM | https://www.wits.ac.za/news/latest-news/opinion/2026/2026-03/securing-vibe-coding-the-hidden-risks-behind-ai-generated-code.html |
| Addy Osmani: Code Review in Age of AI | 2026 | Over 30% of senior developers report shipping mostly AI-generated code; "sheer volume now saturating the ability of midlevel staff to review changes" | HIGH | https://addyo.substack.com/p/code-review-in-the-age-of-ai |
| MIT Technology Review: AI Coding | Dec 2025 | 92% of developers use AI tools; 96% don't fully trust output; paradox named explicitly | HIGH | https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/ |

**Key new angle for Article 4:** The Anthropic skill formation study is a direct empirical confirmation of the solutioning trap mechanism: delegation to AI impairs understanding, and the impairment is not offset by speed gains. The METR study update adds nuance — the productivity picture is murkier than the clean -19% figure suggested, because developers now *refuse* to work without AI on tasks they expect to be slow. This is itself a form of the trap: avoidance of epistemic effort.

---

### Article 5: The Trade-off Triangle (Framework + IRIS-2 Practices)

| Source | Date | Key Data | Confidence | URL |
|--------|------|---------|------------|-----|
| Spec-Driven Development (SDD) DevLand 2026 Talk | 2026 | Conference presentation positioning SDD as the evolution beyond vibe coding; three major platforms shipped dedicated SDD tooling in early 2026: GitHub Spec Kit, AWS Kiro, Tessl Framework | MEDIUM | https://speakerdeck.com/danielsogl/spec-driven-development-the-end-of-vibe-coding-devland-2026 |
| SDD with Claude Code (Heeki Park) | Mar 2026 | Practitioner walkthrough of spec-driven development using Claude Code specifically; grounding for IRIS-2-adjacent pattern | MEDIUM | https://heeki.medium.com/using-spec-driven-development-with-claude-code-4a1ebe5d9f29 |
| Margaret-Anne Storey: Cognitive Debt | Feb 2026 | UVic professor; "velocity without understanding is not sustainable"; distinguishes cognitive debt (in developers' minds) from technical debt (in code); recommends: one human must understand each AI change before shipping | HIGH | https://margaretstorey.com/blog/2026/02/09/cognitive-debt/ |
| HBS Working Knowledge: AI Trade-offs 2026 | 2026 | "Building change fitness" and balancing trade-offs framed as the central organizational challenge; speed-quality trade-off described as "socio-technical challenge of the AI era" | MEDIUM | https://www.library.hbs.edu/working-knowledge/ai-trends-for-2026-building-change-fitness-and-balancing-trade-offs |
| Speed vs Quality in AI Decision-Making | 2025 | Academic paper on speed-quality trade-off in AI-driven decisions; "errors in accuracy, fairness, and judgment can propagate at a scale and speed that defy traditional oversight" | MEDIUM | https://www.sciencepublishinggroup.com/article/10.11648/j.ajist.20250903.16 |
| Augment Code: Why AI Makes Developers 19% Slower | 2025 | Analysis of METR findings with specific explanation: cognitive overhead of context switching between human intent and AI output | MEDIUM | https://www.augmentcode.com/guides/why-ai-coding-tools-make-experienced-developers-19-slower-and-how-to-fix-it |
| JetBrains Ethics of AI Code Review | Mar 2026 | Analysis of ethical dimensions: AI models inherit biases from training data, reinforcing certain conventions while missing framework-specific best practices; 30% of senior developers ship mostly AI-generated code | MEDIUM | https://blog.jetbrains.com/qodana/2026/03/ethics-of-ai-code-review/ |

**Key new angle for Article 5:** The emergence of dedicated SDD tooling from three major platforms in early 2026 (GitHub, AWS, Tessl) validates the "pre-specification" pattern as a real market signal, not just a practitioner opinion. Storey's cognitive debt framing also provides a complementary vocabulary: the triangle's Understanding vertex is exactly what she calls cognitive debt prevention.

---

### Article 6: Measuring the Unmeasurable (Proxy Indicators, Honest Caveats)

| Source | Date | Key Data | Confidence | URL |
|--------|------|---------|------------|-----|
| Arxiv: Epistemic Debt in Novice Programming | Feb 2026 | RCT with 78 participants; unrestricted AI users: 77% failure rate on subsequent AI-Blackout maintenance task; scaffolded AI users: 39% failure rate; "Explanation Gate" proposed as mitigation; "collapse of competence" when AI support disappears | HIGH | https://arxiv.org/abs/2602.20206 |
| Anthropic Skill Formation Study | Jan 2026 | 17% lower quiz scores for AI delegation users; direct empirical measurement of comprehension gap; methodology: controlled unfamiliar library (Trio), structured quiz | HIGH | https://www.anthropic.com/research/AI-assistance-coding-skills |
| GitClear 2026 Research | Jan 2026 | Analysis of 2,172 developer-weeks; Power Users produce 5x more commits; but the "4x to 10x productivity" likely reflects selection bias (high performers adopt tools first); 9x more likely to trigger a specific negative outcome (unspecified in public summary) | MEDIUM | https://www.gitclear.com/developer_ai_productivity_analysis_tools_research_2026 |
| Margaret-Anne Storey: Cognitive Debt Revisited | Feb 2026 | Follow-up post after significant response; "how to measure cognitive debt" named as open research question; signals this is live academic debate, not settled science | HIGH | https://margaretstorey.com/blog/2026/02/18/cognitive-debt-revisited/ |
| METR Study Design Change | Feb 2026 | Measurement is genuinely hard: 30-50% task refusal bias; selection effects severe enough to invalidate randomized design; METR moving to observational methods | HIGH | https://metr.org/blog/2026-02-24-uplift-update/ |
| Cognitive Debt: 5-7x Gap | 2026 | AI coding agents generate code 5-7x faster (140-200 lines/min vs 20-40 lines/min) than humans can understand it; framing "cognitive debt lives in developers' minds, invisible to velocity metrics, surfaces 6-12 months later" | MEDIUM | https://byteiota.com/cognitive-debt-ai-coding-agents-outpace-comprehension-5-7x/ |
| Comprehension-Performance Gap in Brownfield | Nov 2025 | Academic paper on understanding gaps specific to brownfield (existing) codebases with AI assistance; distinguishes from greenfield patterns | MEDIUM | https://arxiv.org/pdf/2511.02922 |
| Program Comprehension as Central Skill (CACM) | 2025 | Communications of the ACM; argues program comprehension must be explicitly taught in CS education in the generative AI era; connects to why measurement is hard — comprehension was always implicit | HIGH | https://cacm.acm.org/blogcacm/program-comprehension-as-a-central-skill-in-cs-education-in-the-era-of-generative-ai/ |
| TechEmpower AI Coding Tools Metrics | Dec 2025 | Proposed measurement framework: look at whole system end-to-end, not just velocity; include time seniors spend reviewing, call out non-code use cases explicitly, use narrative examples alongside metrics | MEDIUM | https://www.techempower.com/blog/2025/12/01/ai-coding-tools-metrics/ |

**Key new finding for Article 6:** The February 2026 RCT (arxiv 2602.20206) provides the clearest empirical measurement yet: a 77% vs 39% task failure rate when AI support is removed. This is a direct measurement of epistemic debt — what happens when the scaffold disappears. The Explanation Gate intervention is also a new concrete practice. METR's study design change validates the article's existing argument about measurement difficulty; the researcher organization doing the most rigorous work on developer productivity concluded the problem is too confounded for clean RCT-style measurement.

---

### Article 7: Beyond Software (Generalization to Other Domains)

| Source | Date | Key Data | Confidence | URL |
|--------|------|---------|------------|-----|
| PNAS: Simulation of Judgment in LLMs (Epistemia) | Oct 2025 | Introduces *epistemia*: "illusion of knowledge emerging when surface plausibility replaces verification"; tested against expert ratings using news outlets; LLMs match outputs while relying on lexical associations rather than deliberative reasoning | HIGH | https://www.pnas.org/doi/10.1073/pnas.2518443122 |
| Tandfonline: Epistemic Authority in Journalism | 2026 | Empirical study of GenAI in newsrooms; journalists using GenAI to maintain epistemic authority; finding: human-machine co-creation can preserve authority if human verification remains; speed-without-verification destroys it | HIGH | https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2640421 |
| Stanford AI Experts Predictions 2026 | 2026 | "The era of AI evangelism is giving way to an era of AI evaluation" — Stanford faculty across CS, medicine, law, economics converging on evaluation as the central problem | HIGH | https://hai.stanford.edu/news/stanford-ai-experts-predict-what-will-happen-in-2026 |
| SSRN: Epistemic Risk and Democracy | 2024 | "What humans believe to be true may increasingly be influenced by AI judgments"; connects AI epistemic risk to democratic knowledge commons; shows the triangle generalizes to civic knowledge | MEDIUM | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4805026 |
| AI Beyond Software: LLM Use Cases 2026 | 2026 | Expansion into chemistry, biology, clinical decision support, robotics, supply chain; each domain introduces its own Understanding vertex analog | MEDIUM | https://context-clue.com/blog/large-language-models-llm-use-cases-in-2026/ |
| McKinsey: Trust in the Age of Agents | 2026 | Agentic AI governance; "who is accountable when the system acts?"; deploying organization retains responsibility; shifts from "human in the loop" to "human on the loop" framing | HIGH | https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/trust-in-the-age-of-agents |
| WEF: Skill Depth vs. Learning Speed | 2026 | "Professionals who succeed will not be the fastest learners but those who build deepest understanding"; directly frames the triangle's Understanding vertex in non-software terms | MEDIUM | https://blog.eduonix.com/2026/03/skill-depth-vs-speed-developers-2026/ |
| Arxiv: Epistemic Diversity and Knowledge Collapse | Oct 2025 | As LLMs homogenize outputs, epistemic diversity in organizational knowledge collapses; applies beyond code to any knowledge work relying on shared LLM outputs | MEDIUM | https://arxiv.org/abs/2510.04226 |
| AI Ethics Issues 2025-2026 (AIhub) | Mar 2026 | Survey of top AI ethics issues: epistemic injustice, bias reinforcement, centralization of power; cross-domain framing | MEDIUM | https://aihub.org/2026/03/04/top-ai-ethics-and-policy-issues-of-2025-and-what-to-expect-in-2026/ |

**Key new angle for Article 7:** The journalism epistemic authority paper is the strongest domain-generalization evidence found. It directly applies the speed-verification trade-off to a non-software professional context and arrives at the same conclusion: speed without verification destroys the epistemic warrant that makes the output valuable. The *epistemia* concept from the PNAS paper also provides a complementary vocabulary — what the series calls "epistemic debt" at the team level, *epistemia* names at the perception level (why humans accept AI outputs as knowledge without verification).

---

## Critical New Data Points (Standalone Facts)

These numbers are strong enough to be cited directly in articles without lengthy context.

| Fact | Source | Date | For Article |
|------|--------|------|------------|
| 96% of developers don't fully trust AI output; only 48% verify it | Sonar 2026 State of Code Survey | Jan 2026 | 3, 4 |
| Anthropic RCT: AI delegation users scored 17% lower on comprehension (50% vs 67%) | Anthropic Research | Jan 2026 | 4, 6 |
| 77% failure rate when AI scaffold removed (vs 39% with scaffolded AI) | arXiv 2602.20206 | Feb 2026 | 6 |
| Amazon Kiro: 13-hour outage, 6.3M orders lost across incidents; 80% adoption mandated | Multiple sources | Dec 2025 – Mar 2026 | 3 |
| 42% of all committed code is AI-generated (expected 65% by 2027) | Sonar 2026 | Jan 2026 | 3 |
| 5-7x velocity-comprehension gap: AI generates 140-200 lines/min, humans understand 20-40 | byteiota / research aggregate | 2026 | 4, 6 |
| Trust in AI accuracy: 29% trust vs 46% distrust (was 40% trust previously) | Stack Overflow 2025 | Dec 2025 | 3, 4 |
| METR: 30-50% of developers refuse tasks without AI tools (selection bias finding) | METR | Feb 2026 | 4, 6 |
| Y Combinator: 25% of Winter 2025 startups have codebases 95% AI-generated | Garry Tan / Elektor Magazine | 2026 | 3 |
| "Era of AI evangelism giving way to era of AI evaluation" | Stanford HAI | 2026 | 7 |

---

## New Conceptual Vocabulary (Since February 2026)

These terms have emerged or gained critical mass since the prior research. Each is useful for Article 3-7 framing.

| Term | Definition | First Use | Relevant Article | Source |
|------|------------|-----------|-----------------|--------|
| **Cognitive debt** | Epistemic debt that lives in developers' minds rather than in the code; accumulates when velocity exceeds comprehension | Margaret-Anne Storey, Feb 2026 | 4, 6 | https://margaretstorey.com/blog/2026/02/09/cognitive-debt/ |
| **Verification gap** | The gap between stated distrust of AI output and actual verification behavior (96% distrust, 48% verify) | Sonar, Jan 2026 | 3, 4 | https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/ |
| **Explanation Gate** | A pedagogical checkpoint requiring developers to teach back AI-generated code before integration | arXiv 2602.20206, Feb 2026 | 6 | https://arxiv.org/abs/2602.20206 |
| **Epistemia** | The illusion of knowledge that emerges when surface plausibility replaces verification | PNAS / Loru et al., Oct 2025 | 7 | https://www.pnas.org/doi/10.1073/pnas.2518443122 |
| **Spec-Driven Development (SDD)** | Writing structured behavior specifications before prompting AI; counter-pattern to vibe coding; tooling shipped from GitHub, AWS, Tessl in early 2026 | Multiple, 2025-2026 | 5 | https://speakerdeck.com/danielsogl/spec-driven-development-the-end-of-vibe-coding-devland-2026 |
| **Collapse of competence** | The pattern where high functional productivity with AI masks critically weak understanding, revealed when AI support is removed | arXiv 2602.20206, Feb 2026 | 4, 6 | https://arxiv.org/abs/2602.20206 |
| **Vibe coding hangover** | The three-part consequence of unreviewed AI code reaching production: instability, security exposure, accountability ambiguity | Elektor Magazine, Jan 2026 | 3 | https://www.elektormagazine.com/articles/2026-an-ai-odyssey-vibe-coding-hangover |

---

## What Has Changed Since February 2026

### Strengthened Arguments

**The solutioning trap (Article 4):** The Anthropic skill formation study provides the first peer-reviewed empirical confirmation that AI delegation reduces comprehension — without offsetting speed gains for the task studied. This upgrades the solutioning trap from "observed pattern" to "empirically demonstrated mechanism."

**Measurement difficulty (Article 6):** METR abandoning their RCT design due to selection effects is itself evidence that measuring AI productivity impact is genuinely hard. The article can now say: "The organization doing the most rigorous work on measuring developer productivity concluded the problem resists clean measurement."

**Case studies (Article 3):** The Amazon Kiro incident provides a larger-scale, more recent example than SaaStr — a Fortune 10 company mandating AI adoption at scale, then experiencing cascading production failures. The denial pattern (blaming user error) is a new angle: organizations cannot admit AI caused failures without undermining their mandates.

### New Tensions to Acknowledge

**SDD tooling could be seen as "the solution":** Three major platforms shipped SDD tooling in early 2026. The article should acknowledge this without endorsing it as a complete answer — SDD addresses the Intent→Specification boundary but doesn't prevent circular validation or model drift.

**METR study complexity:** The -19% slowdown result is more contested than it appeared. The update shows developers who believe they'd be slowed down without AI chose not to participate, which means the study may have undercounted tasks where AI genuinely helps. Honest framing: "our best empirical evidence is inconclusive, which itself tells us something."

**Cognitive debt vs. epistemic debt:** Storey's "cognitive debt" frames the same phenomenon from a developer experience perspective rather than a knowledge-systems perspective. The two vocabularies are complementary. Article 4 or 6 could briefly acknowledge the parallel without getting tangled in terminological dispute.

### Arguments That Stand Unchanged

- The trade-off triangle structure (Article 5): No new research challenges the fundamental three-way trade-off
- Security vulnerability rates (Article 3): CodeRabbit data from prior research still holds; new Sonar and Wits University data reinforces it
- SDLC boundary failures (Article 3/4): AlterSquare case study still the best quantified example; no competing data found
- Generalization beyond software (Article 7): PNAS epistemia paper and journalism study strengthen this, but the triangle framework itself needed no updating

---

## What Was NOT Found (Honest Gaps)

**No new longitudinal data on epistemic debt accumulation.** All studies remain cross-sectional or short-term (weeks to months). The 5-year trajectory of epistemic debt in AI-heavy codebases remains unmeasured.

**No successful counter-examples at scale.** The IRIS-2 pattern remains the only documented case of epistemic debt mitigation. GitClear's 2026 data hints at selection effects (top performers adopt AI), but no organization has published "we used AI at scale AND maintained comprehension."

**No standardized epistemic debt metric.** The field has not converged on measurement. Cognitive debt, epistemic debt, comprehension debt are all in circulation without standardization. This is worth noting explicitly in Article 6.

**The domain-generalization evidence for Article 7 is thinner than desired.** The journalism paper is strong; medicine and legal domain evidence is mostly governance-focused, not epistemological. The article should present domain generalization as a framework for analysis rather than an empirically validated universal claim.

---

## Sources Not Recommended

| Source | Why to Avoid | Alternative |
|--------|-------------|-------------|
| Generic "AI productivity statistics" aggregator sites | Compile numbers without context; often misattribute original studies | Use primary sources (METR, Sonar, Anthropic, Stack Overflow) directly |
| Amazon's official statements on Kiro incident | Company denied AI causation; framing serves PR not accuracy | Use third-party reporting with primary incident documentation |
| Predictions about 2026 without cited data | Speculation presented as data; common in "AI trends" posts | Require at least one datapoint from 2025-2026 actual measurement |

---

## Sources

- [Anthropic: How AI Assistance Impacts Coding Skills](https://www.anthropic.com/research/AI-assistance-coding-skills) — HIGH confidence, peer-reviewed RCT, Feb 2026
- [arXiv 2601.20245: How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245) — HIGH confidence, full paper behind Anthropic study
- [arXiv 2602.20206: Mitigating Epistemic Debt in Novice Programming](https://arxiv.org/abs/2602.20206) — HIGH confidence, RCT with 78 participants, Feb 2026
- [METR: Changing Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/) — HIGH confidence, official METR blog, Feb 2026
- [METR: Measuring Impact of Early-2025 AI on Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — HIGH confidence, original -19% study, Jul 2025
- [Sonar: Verification Gap Press Release](https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/) — HIGH confidence, Jan 2026
- [Stack Overflow: 2025 Developer Survey AI Results](https://survey.stackoverflow.co/2025/ai) — HIGH confidence, annual survey, Dec 2025
- [Margaret-Anne Storey: Cognitive Debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/) — HIGH confidence, academic researcher, Feb 2026
- [Margaret-Anne Storey: Cognitive Debt Revisited](https://margaretstorey.com/blog/2026/02/18/cognitive-debt-revisited/) — HIGH confidence, Feb 2026
- [PNAS: Simulation of Judgment in LLMs (Epistemia)](https://www.pnas.org/doi/10.1073/pnas.2518443122) — HIGH confidence, PNAS peer-reviewed, Oct 2025
- [Particula Tech: Amazon Kiro Production Incident](https://particula.tech/blog/ai-agent-production-safety-kiro-incident) — HIGH confidence, technical post-mortem, Dec 2025
- [Medium: Amazon Lost 6.3 Million Orders](https://medium.com/@heinancabouly/amazon-forced-engineers-to-use-ai-coding-tools-then-it-lost-6-3-million-orders-256a7343b01d) — MEDIUM confidence, single author, cross-references multiple incidents, Mar 2026
- [Fortune: Replit Wiped Database](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/) — HIGH confidence, major publication with CEO statements, Jul 2025
- [Tandfonline: Journalistic Epistemic Authority and AI](https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2640421) — HIGH confidence, peer-reviewed, 2026
- [Stanford HAI: AI Expert Predictions 2026](https://hai.stanford.edu/news/stanford-ai-experts-predict-what-will-happen-in-2026) — HIGH confidence, Stanford institutional, 2026
- [GitClear 2026 Research Resources](https://www.gitclear.com/developer_ai_productivity_analysis_tools_research_2026) — MEDIUM confidence (full report behind paywall, summary available), Jan 2026
- [arXiv 2510.04226: Epistemic Diversity and Knowledge Collapse](https://arxiv.org/abs/2510.04226) — MEDIUM confidence, not yet peer-reviewed, Oct 2025
- [Elektor Magazine: 2026 Vibe Coding Hangover](https://www.elektormagazine.com/articles/2026-an-ai-odyssey-vibe-coding-hangover) — MEDIUM confidence, industry publication, Jan 2026
- [The New Stack: Vibe Coding Catastrophes](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/) — MEDIUM confidence, industry publication, Jan 2026
- [Wits University: Vibe Coding Security Risks](https://www.wits.ac.za/news/latest-news/opinion/2026/2026-03/securing-vibe-coding-the-hidden-risks-behind-ai-generated-code.html) — MEDIUM confidence, academic opinion piece, Mar 2026
- [Addy Osmani: Code Review in the Age of AI](https://addyo.substack.com/p/code-review-in-the-age-of-ai) — HIGH confidence (practitioner), 2026
- [McKinsey: Trust in the Age of Agents](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/trust-in-the-age-of-agents) — HIGH confidence, 2026
- [CACM: Program Comprehension as Central Skill](https://cacm.acm.org/blogcacm/program-comprehension-as-a-central-skill-in-cs-education-in-the-era-of-generative-ai/) — HIGH confidence, CACM, 2025
- [Speaker Deck: Spec-Driven Development DevLand 2026](https://speakerdeck.com/danielsogl/spec-driven-development-the-end-of-vibe-coding-devland-2026) — MEDIUM confidence, conference talk, 2026
- [Springer: Automation Bias in Human-AI Collaboration Review](https://link.springer.com/article/10.1007/s00146-025-02422-7) — HIGH confidence, peer-reviewed systematic review, 2025
- [SSRN: Epistemic Risk and Democracy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4805026) — MEDIUM confidence (working paper), 2024

---

*Source stack for: Epistemic Debt Series, Articles 3–7*
*Researched: 2026-03-14*
*Supersedes: nothing — additive to SUMMARY.md dated 2026-02-07*
