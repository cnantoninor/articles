# Project Research Summary

**Project:** Epistemic Debt Series — Articles 3–7 (v3.0 milestone)
**Domain:** Long-form technical Substack series — AI epistemology and software engineering
**Researched:** 2026-03-14
**Confidence:** HIGH
**Supersedes:** v2.0 SUMMARY.md dated 2026-02-07

## Executive Summary

The Epistemic Debt series is a 7-part practitioner-facing Substack series where articles 0–2 are published and immutable. The v3.0 milestone is to polish and publish articles 3–7 by integrating new research that has emerged since the February 2026 research cycle. The "stack" for this work is entirely an evidence base — no software infrastructure is involved. Since February 2026, several high-confidence empirical studies have materially strengthened the series' core arguments: the Anthropic RCT (Jan 2026) provides the first peer-reviewed confirmation that AI delegation reduces comprehension without offsetting speed gains; arXiv 2602.20206 (Feb 2026) documents a 77% failure rate when AI scaffold is removed vs 39% for scaffolded groups; and the Amazon Kiro incident (Dec 2025 – Mar 2026) provides enterprise-scale evidence of mandated AI adoption producing cascading production failures. These upgrade the series' core claims from "observed patterns" to "empirically demonstrated mechanisms."

The recommended approach is to build articles in strict order — 3, 4, 5, 6, 7 — because the content forms a hard dependency chain. Article 3 establishes the failure taxonomy that article 4 references; article 4 introduces SDLC boundaries 1 and 2 that article 5 completes with boundary 3; article 5's triangle framework is what article 7 generalizes. The core work for each article is not writing from scratch but integrating specific, already-identified TODO items and writing social teasers. All five articles exist as drafts; the work is targeted polish, not open-ended drafting.

The key risks are editorial rather than conceptual: tone drift toward prescription in framework articles (5 and 7), evidence overload in the already-dense article 3, measurement caveats in article 6 accidentally destabilizing earlier established claims, and the capstone (article 7) becoming anticlimactic through repetitive domain-table generalization. Each pitfall has a known prevention strategy. The series' credibility rests on maintaining the exploratory-not-prescriptive voice throughout — this is the most fragile element and must be actively guarded during each polish pass, especially in articles 5 and 7 where frameworks invite imperative-mood drift.

## Key Findings

### Evidence Base (from STACK.md)

This is a content project. The "stack" is the series' evidence base. Research since February 2026 has added material that strengthens specific articles without changing the overall series structure.

**Core new evidence sources:**
- **Anthropic Skill Formation RCT (Jan 2026):** Randomized trial with 52 junior engineers; AI delegation users scored 17% lower on comprehension (50% vs 67%); debugging gap is the sharpest finding — the exact skill needed to oversee AI output. Developers using AI for conceptual questions scored 65%+; those delegating code generation scored below 40%. HIGH confidence. Primary backbone for article 4's mechanism.
- **arXiv 2602.20206 — "Fragile Experts" RCT (Feb 2026):** 78 participants; unrestricted AI users hit 77% failure rate on maintenance tasks when AI scaffold removed vs 39% for scaffolded group; introduces "Explanation Gate" as mitigation. HIGH confidence. Clearest empirical measurement of epistemic debt yet available — directly supports articles 3 and 6.
- **Amazon Kiro Incident (Dec 2025 – Mar 2026):** 13-hour AWS outage; 6.3M orders lost across incidents; 80% adoption mandated; Amazon denied AI causation (blaming user error). Adds the "denial" dynamic — organizations cannot admit AI caused failures without undermining their mandates. HIGH confidence. Strongest enterprise-scale case study for article 3.
- **Sonar 2026 Verification Gap (Jan 2026):** 96% distrust AI output; only 48% verify before committing; 42% of committed code is AI-generated. HIGH confidence. Sharpest quantification of stated skepticism vs actual behavior.
- **METR Study Design Change (Feb 2026):** METR abandoning RCT design due to 30-50% task refusal bias. The organization doing the most rigorous work on developer productivity concluded the problem resists clean measurement. HIGH confidence. Validates article 6's measurement difficulty argument.

**New conceptual vocabulary (since February 2026):**
- *Cognitive debt* (Storey, Feb 2026) — epistemic debt that lives in developers' minds; complementary framing to the series' knowledge-systems vocabulary
- *Verification gap* (Sonar, Jan 2026) — the gap between stated distrust and actual verification behavior
- *Explanation Gate* (arXiv 2602.20206) — a teachback checkpoint before AI code integration; concrete mitigation practice for article 6
- *Epistemia* (PNAS, Oct 2025) — illusion of knowledge when surface plausibility replaces verification; useful for article 7's domain generalization
- *Vibe coding hangover* (Elektor, Jan 2026) — three-part consequence of unreviewed AI code reaching production: instability, security exposure, accountability ambiguity

**Honest gaps that remain:**
- No longitudinal data on epistemic debt accumulation — all studies cross-sectional, weeks to months; 5-year trajectory unmeasured
- No successful counter-examples at scale — no organization has published "we used AI at scale AND maintained comprehension"; IRIS-2 remains the only documented mitigation case
- No standardized epistemic debt metric — cognitive debt, epistemic debt, comprehension debt all in circulation without field convergence; worth naming explicitly in article 6
- Domain-generalization evidence for article 7 is uneven — journalism paper (Tandfonline) is strong and peer-reviewed; medicine and legal evidence is governance-focused, not epistemological

### Expected Features (from FEATURES.md)

All five articles exist as drafts. The v3.0 feature work is targeted integration of specific content items, not open-ended writing.

**Must have (universal table stakes — all articles):**
- Series continuity header and navigation footer — templated from articles 1–2
- YAML front matter with complete metadata — already in all drafts
- Exploratory (not prescriptive) tone — most at-risk in articles 5 and 7
- Reference list in footnoted format — pattern established

**Must have (article-specific, unresolved — priority order):**

*Article 3:*
- Prather et al. "Fragile Experts" data integrated into "These Aren't Isolated Incidents" — upgrades observational-only evidence with experimental evidence (P1)
- Pre-LLM vs. Post-LLM opening context — causal framing before case studies (P1)
- Stochastic Spaghetti Effect (Ngabang) named as distinct failure type (P1)
- CAST + Veracode 2026 statistics (P2)

*Article 4:*
- Anthropic skill formation study (17% comprehension gap, debugging gap) as quantitative backbone (P1)
- Social invisibility subsection — explains why teams don't notice the trap forming (P1)
- t₀ connection to SDLC boundaries as one paragraph per boundary (P2)
- fast.ai "dark flow" framing in automation bias section (P2)

*Article 5:*
- ASCII triangle rendering verified in Substack preview (P1)
- ε_k tolerance factor integration — closes mathematical arc planted in article 2 (P1)
- Strategy forces connected to t₀ and break-even formula (P2)

*Article 6:*
- Senior Expertise Gap as new subsection under "The Honest Caveat" (P1)
- Architectural decision temporal validity as brief practical recommendation (P1)
- Bus factor team-level formulation as English thought experiment (P2)

*Article 7:*
- Journalistic epistemic authority citation added to content creation domain (P1)
- Human Debt as one-paragraph forward reference in the closing (P1)
- Open-source epistemic debt angle under HITL meta-pattern section (P2)
- Dual-track opening paragraph for non-software readers (P1)

*All articles:*
- Social teasers (LinkedIn, Twitter, Instagram, Substack Notes) — all currently empty in YAML

**Defer to v3.x (post-publication if engagement warrants):**
- Interactive triangle positioning tool
- Companion single-document synthesis article
- "Human Debt" article (series part 8 or separate)
- Domain-specific deep dives for non-software audiences

**Anti-features to avoid:**
- Prescriptive "here's what to do" framework language — violates series brand promise
- Heavy academic citation density — breaks Substack reading flow
- New case studies introduced after article 3 — dilutes article function identity
- Resolving all TODOs as new H2 sections — risks bloating articles past target length
- Ed formula repeated in articles 4–7 body — one back-reference per article is sufficient
- "Human Debt" as a full section anywhere in articles 3–7 — concept is underdeveloped; use as one-paragraph forward reference in article 7 only

### Architecture Approach (from ARCHITECTURE.md)

This is a content architecture problem. All seven draft articles exist. The dependency chain is hard and must be respected. Articles 0–2 are published and immutable — their terminology (t₀, c_k, τ_k, δ, Ed formula, Circular Confirmation Trap) cannot be redefined or reframed in later articles.

**Content component responsibilities:**
1. **Article 3 (Evidence)** — Establishes the failure taxonomy (system boundary gap, defensive coding gap, edge case reasoning gap) that articles 4 and 5 reference by name; the evidence article that makes the phenomenon visceral
2. **Article 4 (Mechanism)** — Introduces SDLC boundaries 1 and 2; explains the solutioning trap (psychology → social → structural); must not gain a fourth boundary or boundary 3 will break in article 5
3. **Article 5 (Framework)** — The pivot article; introduces the triangle, resolves boundary 3 (circular validation), fulfills article 2's ε_k tolerance factor promise, presents IRIS-2; most complex article
4. **Article 6 (Measurement)** — Deliberately honest about limits; the honest caveat posture is architecturally load-bearing — do not "strengthen" measurement claims; must not be weakened or the series loses intellectual credibility
5. **Article 7 (Capstone)** — Generalizes the triangle to five domains; closes the series; self-referential closing is the tonal anchor; must come last

**Critical cross-article obligations (currently open as TODOs):**
- Art 4 must connect SDLC boundaries to t₀ concept — each boundary is a potential t₀ (CRITICAL — breaks mathematical thread from Art 2 if skipped)
- Art 5 must connect strategy forces to t₀ + break-even formula (CRITICAL — leaves "Later articles will look at these mechanisms" unfulfilled)
- Art 5 must introduce ε_k tolerance factor (CRITICAL — fulfills Art 2's explicit "we'll return to this" promise)
- Art 5 must link to Art 2's "Circular Confirmation Trap" terminology when introducing Boundary 3 (HIGH — closes a planted cross-reference)
- Art 7 must add dual-track opening for non-software entry-point readers (HIGH — Article 0 explicitly invites this audience to start at 7)

**Publication status gap to verify:**
- ARCHITECTURE.md flags that PROJECT.md says article 2 is published, but its YAML frontmatter shows `draft` status and empty `published_date` — this must be confirmed before scheduling article 3

**File modifications required (no new files needed):**
- `topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md`
- `topics/epistemic_debt/artifacts/articles/article-4-the-solutioning-trap.md`
- `topics/epistemic_debt/artifacts/articles/article-5-the-trade-off-triangle.md`
- `topics/epistemic_debt/artifacts/articles/article-6-measuring-the-unmeasurable.md`
- `topics/epistemic_debt/artifacts/articles/article-7-beyond-software.md`

### Critical Pitfalls (from PITFALLS.md)

All pitfalls are editorial. The series does not involve software implementation risk.

1. **Recapping prior articles as filler, not as anchor** — Avoid plot summary ("in the previous article, we defined X"); use opening paragraphs to apply prior concepts to a new frame rather than restate them. Prevention: opening paragraph must end with forward momentum; recap should be activating, not reciting. Highest risk: article 5's current draft.

2. **Tone drift toward prescription in framework articles** — Articles 5 and 7 present frameworks; frameworks invite numbered steps; numbered steps invite imperative mood. Prevention: audit for "you should" language; replace with "teams that adopt X find..."; framework sections should read as field observations, not methodology guides.

3. **Evidence overload in article 3 breaking the narrative** — The draft plus all new TODO data risks genre-shifting from practitioner narrative to literature review. Prevention: "one study per claim" discipline; choose the most concrete single data point per claim and footnote the rest. The Prather et al. RCT is the most actionable TODO because it demonstrates a mechanism, not just a correlation.

4. **Measurement caveats in article 6 undermining series credibility** — The honest limits framing risks readers concluding the whole series was speculation. Prevention: explicit tier separation at article opening — Tier 1 (conceptual claims, high confidence, established) vs Tier 2 (empirical measurement, provisional). The technical debt parallel must appear earlier and carry more structural weight.

5. **Capstone anticlimactic through over-generalization** — Five domains with identical three-element structure (table, failure mode, strategy) produces diminishing returns. Prevention: lead with one domain done deeply — the "voice loss in content creation" angle is most non-obvious; move self-referential closing section earlier; treat domain tables as reference material, not argument.

6. **Solutioning trap thesis fragmentation in article 4** — Four distinct concepts (vibe coding, automation bias, junior developer crisis, SDLC boundaries) risk leaving readers unable to state the trap in one sentence. Prevention: one connecting sentence per section back to the trap definition: "jumping to implementation before understanding the problem well enough to evaluate the solution."

## Implications for Roadmap

The build order is non-negotiable: 3 → 4 → 5 → 6 → 7. This matches the publication order and is architecturally required, not a preference.

### Phase 1: Article 3 — Evidence Layer Completion
**Rationale:** Article 3 establishes the failure taxonomy that all subsequent articles reference by name. It must be locked first. Article 4's back-reference to "the 200-to-2000 pattern" and the named failure types require article 3's vocabulary to be stable before article 4 can be finalized.
**Delivers:** Published article 3 — experimental evidence integrated alongside observational, enterprise-scale Amazon Kiro case study, Pre-LLM vs Post-LLM causal framing, social teasers complete
**Addresses:** Prather et al. Fragile Experts data (P1), Pre-LLM opening (P1), Stochastic Spaghetti Effect naming (P1), CAST + Veracode statistics (P2)
**Avoids:** Evidence overload pitfall — apply "one study per claim" discipline in a curation pass after all TODOs are resolved; do not introduce new mechanisms or frameworks here

### Phase 2: Article 4 — Mechanism Layer Completion
**Rationale:** Article 4 introduces SDLC boundaries 1 and 2 — hard prerequisite for article 5's boundary 3. The solutioning trap mechanism must be locked before the framework article that references it. The SDLC boundary count (2, with boundary 3 belonging to article 5) must be fixed here and not changed during polish.
**Delivers:** Published article 4 — Anthropic RCT as quantitative backbone, social invisibility subsection, t₀ connection to SDLC boundaries, solutioning trap thesis coherent across all four sub-concepts, social teasers complete
**Addresses:** Anthropic skill formation study (P1), social invisibility subsection (P1), t₀ boundary connection (P2), fast.ai dark flow framing (P2)
**Avoids:** Solutioning trap fragmentation pitfall — add one connecting sentence per section; tone drift — psychological sections must remain observational, not prescriptive

### Phase 3: Article 5 — Framework Layer Completion
**Rationale:** The pivot article — most complex in the series. Depends on article 4's SDLC boundary count being locked at 2. Fulfills two mathematical obligations planted in article 2 (ε_k tolerance factor and t₀ strategy forces connection). Must be locked before article 7 can generalize the triangle. Highest-risk article for tone drift and IRIS-2 over-specificity.
**Delivers:** Published article 5 — ε_k tolerance factor resolved, strategy forces connected to t₀ and break-even formula, Art 2 "Circular Confirmation Trap" linked at Boundary 3, IRIS-2 abstracted (specific detail → generalizable principle at each instance), ASCII triangle verified in Substack, social teasers complete
**Addresses:** ε_k tolerance factor (critical), t₀ strategy forces connection (critical), ASCII rendering check (critical), cross-reference terminology alignment
**Avoids:** Tone prescription drift pitfall — framework sections must read as field observations; IRIS-2 over-specificity pitfall — each specific detail must be followed immediately by the generalizable principle

### Phase 4: Article 6 — Measurement Layer Completion
**Rationale:** Short article that uses article 5's triangle vocabulary. Can proceed once article 5 is locked. The honest caveat posture is architecturally load-bearing — this article must not be strengthened into overclaims. The tier separation (Tier 1 established, Tier 2 provisional) must appear before the "not well, not yet" admission, not after it.
**Delivers:** Published article 6 — explicit Tier 1/Tier 2 separation at opening, Senior Expertise Gap as new subsection, architectural decision temporal validity recommendation, proxy indicator section longer than caveat section, social teasers complete
**Addresses:** Senior Expertise Gap (P1), architectural decision temporal validity (P1), bus factor team formulation (P2)
**Avoids:** Caveats undermining credibility pitfall — tier separation must come before the admission of measurement limits; do not add new measurement approaches that aren't honestly caveated

### Phase 5: Article 7 — Capstone Completion and Series Closure
**Rationale:** Must come last. Explicitly references "for six articles, we've explored..." — can only be finalized when articles 3–6 are locked. The self-referential closing only works if the series has maintained consistent epistemic discipline throughout. Article 0's publication URLs for all articles need updating as each article is published.
**Delivers:** Published article 7 — dual-track opening for non-software readers, one lead domain done deeply before comparative tables, journalistic epistemic authority citation in content creation domain, Human Debt as one-paragraph forward reference, open-source epistemic debt angle in HITL section, social teasers complete; Article 0 updated with publication URLs for articles 3–7
**Addresses:** Dual-track opening (P1), journalistic epistemic authority citation (P1), Human Debt forward reference (P1), open-source epistemic debt angle (P2)
**Avoids:** Capstone anticlimactic pitfall — lead with content creation voice-loss insight (most non-obvious); self-referential closing moved earlier; domain tables are reference, not argument; audience confusion at entry point — two-sentence embedded definition of epistemic debt for new readers

### Phase Ordering Rationale

- The order 3→4→5→6→7 mirrors the publication order; the narrative arc was designed so each article is a prerequisite for the next — reordering requires restructuring cross-references that are already embedded in all five drafts
- Article 5 is the most complex and risky phase: it carries two unfulfilled mathematical promises from article 2, the highest pitfall exposure (framework tone drift, IRIS-2 over-specificity), and serves as the pivot that both closes the mechanism arc and opens the generalization arc
- Article 6 is the shortest and least structurally risky phase, but its tone discipline is the most fragile — a single revision pass can accidentally turn honest caveats into overclaims
- Article 7 cannot begin final structural decisions until article 5 is locked (triangle vocabulary must be stable) and article 3 is locked (failure taxonomy must be stable for domain generalization tables)

### Research Flags

Phases likely needing deeper research or verification during planning:
- **Phase 1 (Article 3):** Verify Amazon Kiro incident details before publishing as a named case study — cross-check "6.3M orders" figure against the particula.tech post-mortem and Fortune reporting. Also verify Article 0's description of article 3 matches the final draft content before publishing (Pitfall I-1).
- **Phase 3 (Article 5):** Test ASCII triangle diagram in actual Substack draft preview before scheduling publication — email rendering may degrade the diagram; a fallback format decision is needed in advance.
- **Pre-Phase 1:** Verify article 2's publication status before scheduling article 3 — PROJECT.md and YAML frontmatter are inconsistent on whether article 2 is live.

Phases with standard patterns (no additional research needed):
- **Phase 2 (Article 4):** All TODO integrations are additive insertions; sources already verified in STACK.md at HIGH confidence
- **Phase 4 (Article 6):** Both remaining TODOs are well-defined insertions; METR study design change already at HIGH confidence; no new evidence required
- **Phase 5 (Article 7):** Journalistic epistemic authority source already verified (Tandfonline, HIGH confidence); Human Debt is a one-paragraph forward reference requiring no new research; open-source epistemic debt angle sourced from InfoQ (MEDIUM confidence, acceptable for brief mention)

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Evidence Base (STACK.md) | HIGH | Primary sources directly fetched; multiple peer-reviewed RCTs; Anthropic, METR, and PNAS are authoritative; Amazon Kiro cross-referenced across multiple independent sources |
| Features / Content Requirements (FEATURES.md) | HIGH | Based on direct reading of all seven draft articles; TODOs precisely identified and prioritized; no inference required; anti-features clearly defined |
| Architecture / Build Order (ARCHITECTURE.md) | HIGH | Based on direct inspection of all articles; cross-article references explicitly mapped; dependency chain verified; hard vs soft dependencies distinguished |
| Pitfalls (PITFALLS.md) | HIGH | Identified from direct reading of drafts and published series context; each pitfall has specific textual evidence from the drafts; recovery costs and strategies provided |

**Overall confidence:** HIGH

### Gaps to Address

- **Article 2 publication status ambiguity:** ARCHITECTURE.md flags that PROJECT.md says article 2 is published but its YAML frontmatter shows draft status and empty `published_date`. Resolve before Phase 1 begins — downstream articles' back-references will point to unpublished content if article 2 is not live.
- **No longitudinal epistemic debt data:** All studies are cross-sectional. Article 6's honest caveat section should name this gap explicitly. Framing: the 5-7x velocity-comprehension gap is a point-in-time finding, not a trajectory claim.
- **Domain generalization evidence uneven:** Journalism study is peer-reviewed and strong; medicine and legal evidence is governance-focused, not epistemological. Article 7's domain generalization should be framed as applying an analytical framework, not as empirically validated universal claims.
- **ε_k tolerance factor integration complexity:** The highest-difficulty TODO in the series — mathematical precision without losing practitioner accessibility. The English explanation must stand alone; the formula belongs in a footnote. No additional research needed, but careful editorial judgment required.
- **No successful counter-examples at scale:** IRIS-2 remains the only documented mitigation case. Article 5 should frame IRIS-2 as a proof-of-concept, not a proven general approach.

## Sources

### Primary (HIGH confidence)
- Anthropic Research (Jan 2026). "How AI assistance impacts the formation of coding skills." https://www.anthropic.com/research/AI-assistance-coding-skills
- arXiv 2602.20206 (Feb 2026). Prather et al. "Mitigating Epistemic Debt in Novice Programming using Metacognitive Scripts." https://arxiv.org/abs/2602.20206
- arXiv 2601.20245 (Jan 2026). Full methodology paper for Anthropic skill formation study. https://arxiv.org/abs/2601.20245
- METR (Feb 2026). "Changing Developer Productivity Experiment Design." https://metr.org/blog/2026-02-24-uplift-update/
- Sonar (Jan 2026). "Verification Gap Press Release." https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/
- Stack Overflow Developer Survey (Dec 2025). AI results. https://survey.stackoverflow.co/2025/ai
- Stack Overflow Blog (Jan 2026). "Are Bugs and Incidents Inevitable with AI Coding Agents?" https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/
- Particula Tech (Dec 2025). "Amazon Kiro Production Incident." https://particula.tech/blog/ai-agent-production-safety-kiro-incident
- Fortune (Jul 2025). "Replit Wiped Database." https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/
- PNAS (Oct 2025). "Simulation of Judgment in LLMs (Epistemia)." https://www.pnas.org/doi/10.1073/pnas.2518443122
- Tandfonline (2026). "Journalistic Epistemic Authority in the Age of AI." https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2640421
- Stanford HAI (2026). "AI Expert Predictions 2026." https://hai.stanford.edu/news/stanford-ai-experts-predict-what-will-happen-in-2026
- Margaret-Anne Storey (Feb 2026). "Cognitive Debt." https://margaretstorey.com/blog/2026/02/09/cognitive-debt/
- Springer (2025). "Automation Bias in Human-AI Collaboration — Systematic Review." https://link.springer.com/article/10.1007/s00146-025-02422-7
- CACM (2025). "Program Comprehension as Central Skill in CS Education." https://cacm.acm.org/blogcacm/program-comprehension-as-a-central-skill-in-cs-education-in-the-era-of-generative-ai/
- McKinsey (2026). "Trust in the Age of Agents." https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/trust-in-the-age-of-agents
- Addy Osmani (2026). "Code Review in the Age of AI." https://addyo.substack.com/p/code-review-in-the-age-of-ai

### Secondary (MEDIUM confidence)
- arXiv 2510.04226 (Oct 2025). Epistemic Diversity and Knowledge Collapse. https://arxiv.org/abs/2510.04226
- arXiv 2511.02922 (Nov 2025). Comprehension-Performance Gap in Brownfield Codebases. https://arxiv.org/pdf/2511.02922
- GitClear (Jan 2026). Developer AI Productivity Analysis. https://www.gitclear.com/developer_ai_productivity_analysis_tools_research_2026 (full report paywalled)
- byteiota (2026). "Cognitive Debt: 5-7x Gap." https://byteiota.com/cognitive-debt-ai-coding-agents-outpace-comprehension-5-7x/
- The New Stack (Jan 2026). "Vibe Coding Could Cause Catastrophic Explosions." https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/
- Elektor Magazine (Jan 2026). "Vibe Coding Hangover." https://www.elektormagazine.com/articles/2026-an-ai-odyssey-vibe-coding-hangover
- Wits University (Mar 2026). "Securing Vibe Coding — Hidden Risks." https://www.wits.ac.za/news/latest-news/opinion/2026/2026-03/securing-vibe-coding-the-hidden-risks-behind-ai-generated-code.html
- Speakerdeck (2026). "Spec-Driven Development — DevLand 2026." https://speakerdeck.com/danielsogl/spec-driven-development-the-end-of-vibe-coding-devland-2026
- JetBrains (Mar 2026). "Ethics of AI Code Review." https://blog.jetbrains.com/qodana/2026/03/ethics-of-ai-code-review/
- fast.ai (Jan 2026). "Breaking the Spell of Vibe Coding." https://www.fast.ai/posts/2026-01-28-dark-flow/
- InfoQ (Feb 2026). "AI Vibe Coding Threatens Open Source." https://www.infoq.com/news/2026/02/ai-floods-close-projects/
- Medium / Heinan Cabouly (Mar 2026). "Amazon Forced Engineers to Use AI Coding Tools." https://medium.com/@heinancabouly/amazon-forced-engineers-to-use-ai-coding-tools-then-it-lost-6-3-million-orders-256a7343b01d
- HBS Working Knowledge (2026). "AI Trade-offs: Building Change Fitness." https://www.library.hbs.edu/working-knowledge/ai-trends-for-2026-building-change-fitness-and-balancing-trade-offs
- TechEmpower (Dec 2025). "AI Coding Tools Metrics." https://www.techempower.com/blog/2025/12/01/ai-coding-tools-metrics/

### Tertiary (LOW confidence or working papers)
- SSRN (2024). "Epistemic Risk and Democracy." https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4805026
- Ngabang, L.A. (2026). "The Illusion of Competence." viXra:2601.0013v1
- Pertama Partners (2026). "AI Project Failure Statistics 2026." https://www.pertamapartners.com/ai-project-failure-statistics-2026 (aggregator site — use primary sources instead)

---
*Research completed: 2026-03-14*
*Additive to: v2.0 SUMMARY.md (2026-02-07) — supersedes for v3.0 planning purposes*
*Ready for roadmap: yes*
