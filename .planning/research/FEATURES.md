# Feature Research: Epistemic Debt Series Articles 3–7

**Domain:** Technical Substack article series — evidence-based AI/software epistemology
**Researched:** 2026-03-14
**Confidence:** HIGH

---

## Overview

This document maps table stakes, differentiators, and anti-features for articles 3–7 of the Epistemic Debt series. Each article has a distinct content type and narrative role. Features are described at the article level, not the series level.

**Existing foundation (articles 0–2) provides:**
- Core concept definitions (epistemic debt, Ed formula, construction vs. curation paradigm)
- Comparison with technical debt (6-dimension table)
- Series navigation via article 0
- Three named default events (SaaStr, AlterSquare, healthcare) used as evidence anchors

**New literature since February 2026 research:**
- Anthropic randomized controlled trial (Jan 2026): AI use caused 17% lower comprehension scores; biggest gap was in debugging — the exact skill needed to oversee AI output. Developers who used AI for *conceptual questions* scored 65%+, while those delegating code generation scored below 40%. (HIGH confidence — Anthropic official research)
- Prather et al. (2026) "Fragile Experts" study: unrestricted AI users hit 77% failure rate on maintenance tasks vs. 39% for scaffolded group. Metacognitive scripts restored understanding without sacrificing velocity. (HIGH confidence — peer-reviewed arXiv)
- Vibe coding open-source crisis (InfoQ, Feb 2026): 72% of developers say vibe coding is not part of professional work; AI-flooded open-source projects creating maintainer burnout and eroding contribution incentives. (MEDIUM confidence — single news source)
- Journalistic epistemic authority study (Tandfonline, 2026): epistemic debt concept applied to newsroom AI adoption — directly supports article 7's generalization argument. (MEDIUM confidence — academic journal)
- fast.ai "Breaking the Spell of Vibe Coding" (Jan 2026): psychological analysis of automation bias and "dark flow" states in vibe coding. Relevant to article 4's mechanism section. (MEDIUM confidence — practitioner blog)

---

## Feature Landscape

### Table Stakes (Readers Expect These)

Features readers assume exist in a Substack series of this type. Missing these makes the article feel incomplete or breaks the series contract.

#### All Articles (Universal Table Stakes)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Series continuity header | Readers arrive mid-series via shares or recommendations; need context anchoring | LOW | Standard: "This is Part N of a 7-part series on [epistemic debt — link]." Already set up in articles 1–2. |
| Series navigation footer | Readers want to find adjacent articles; orphan articles feel incomplete | LOW | Link to article 0 (series overview) in every footer. Articles 1–2 set the pattern. |
| Closing call to comment/subscribe | Substack's discovery mechanism rewards engagement; readers expect this from newsletter format | LOW | Already templated in articles 1–2. Do not deviate from established pattern. |
| Reference list | Evidence-heavy series requires citations; readers will check claims | LOW | Footnoted, not inline. Pattern established in articles 2–3. |
| YAML front matter | Required by publication rules; controls Substack metadata | LOW | Templates/article.md provides the schema. |
| Exploratory (not prescriptive) tone | Series brand promise; readers self-selected for this voice | MEDIUM | Every article must explicitly present ideas as investigations, not mandates. The "The trade-offs are real. Make them conscious." closing of article 7 sets the capstone register. |

#### Article 3: When Epistemic Debt Defaults (Evidence/Case Study Article)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Named, attributable case studies | Readers expect concrete evidence, not vague references; series has set this standard in article 2 | LOW | SaaStr, AlterSquare, and healthcare composite are already written and sourced. The TODO items (Prather et al., Ngabang, CAST/Veracode statistics) are additive enhancements. |
| Industry statistics section | Article 3's subtitle promises "industry data that says they aren't outliers" — this is the contract with the reader | MEDIUM | Four statistics blocks already exist. New 2026 data (CAST "61B workdays", Veracode security debt) needs integration into the existing "These Aren't Isolated Incidents" section. |
| The pattern synthesis | Case studies without a unifying mechanism feel like a list; readers need the structural insight | LOW | Already written: "Three different domains. Three different failure modes. The same underlying mechanism." |
| Bridge to article 4 | Readers want to know what comes next; dangling ending breaks series pacing | LOW | Already written: "What are the mechanisms that make epistemic debt so easy to accumulate and so hard to notice?" |

#### Article 4: The Solutioning Trap (Mechanism/Psychology Article)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Named mechanism with clear definition | Mechanism articles must crystallize the insight; "solutioning trap" is already the named concept | LOW | Already named and defined. The article delivers on its subtitle promise. |
| Concrete scenario illustrating the mechanism | Readers need a worked example, not just a description; rate limiter scenario already serves this | LOW | Rate limiter scenario (distributed counter bug) is already written and effective. |
| Automation bias explanation | Psychology section is core to "why" this happens; readers with technical background still need the cognitive framing | MEDIUM | Written. New fast.ai "dark flow" material (Jan 2026) can add depth to the psychological register. |
| Junior developer crisis section | Amplifies stakes; connects to career-level readers | MEDIUM | Written. Anthropic skill formation study (Jan 2026) is directly relevant here — 17% comprehension gap is the quantitative backbone this section needs. |
| SDLC boundary analysis | Provides the structural map of *where* debt accumulates, moving from "why" to "where" | HIGH | Two of three boundaries are written (Intent→Spec, Spec→Implementation). Boundary 3 (Implementation→Validation) is moved to article 5 for narrative flow. The TODO items about social invisibility and t₀ connections need resolution. |
| Bridge to article 5 | Readers must be primed for the framework article | LOW | Already written: "Now we know how debt accumulates — at the boundaries where meaning gets lost in translation. The remaining question: what do we do about it?" |

#### Article 5: The Trade-off Triangle (Framework Article)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Visual framework (the triangle diagram) | Framework articles require a visual anchor; this series built up to it across 4 articles | LOW | Already written using ASCII art. Needs export check for Substack rendering — ASCII diagrams sometimes degrade in email delivery. |
| Circular validation explanation with code example | The "╳ trap" on the triangle must be concrete; readers need to recognize it in their own work | LOW | Already written with the Python email validation example. |
| IRIS-2 as proof-of-concept case | Credibility requires a real implementation example, not just theory | MEDIUM | Already written with specific file-path level detail (`.cursor/rules/*.mdc`, `test_user_journey_e2e.py` at 972 lines). |
| Domain-based positioning section | Readers need guidance on where to apply what level of rigor | MEDIUM | Written (core/supporting/generic domains). The TODO about ε_k tolerance factor needs resolution before publication. |
| Practitioner takeaways | Framework articles must close with actionable guidance | LOW | Five takeaways already written. |
| Bridge to article 6 | Primes the measurement question | LOW | Already written. |

#### Article 6: Measuring the Unmeasurable (Measurement Article)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Honest admission that measurement is hard | Measurement articles that oversell precision lose credibility; the title promises honesty | LOW | Already the lead: "The answer is: not well. Not yet." |
| Concrete proxy indicator list | Readers need something actionable even if it's imprecise | LOW | Five indicators already documented (bus factor, onboarding velocity, incident diagnosis time, code archaeology ratio, code churn). |
| Measurement paradox explanation | The why-it's-hard is as valuable as the how-to-measure; readers in engineering teams face this | MEDIUM | Written: "understanding is a property of minds, not codebases." |
| Correlation-causation warning | Evidence-heavy technical readers will push back if this isn't addressed | LOW | Written with three concrete examples. |
| Research frontier section | Shows the field is moving; prevents the article feeling like a dead end | MEDIUM | EEG and think-aloud protocols already documented. |

#### Article 7: Beyond Software (Capstone/Generalization Article)

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Triangle generalization to non-software domains | The article title promises it; the series has been building to this claim | HIGH | Five domains already mapped (content, LLM-as-judge, research, decision support, data analysis). |
| Domain comparison tables | Readers in non-software fields need the vertex definitions translated for their context | MEDIUM | Already written for all five domains. |
| Universal meta-patterns | Readers need the structural insight, not just a list of domains | MEDIUM | Four patterns (HITL, Pre-Specification, RAG, Adversarial Testing) already documented. |
| 5-step application protocol | Capstone must leave readers with something to do | LOW | Already written. |
| Self-referential closing | Series about epistemic debt in AI-assisted work, written with AI assistance — the meta-observation is obligatory | LOW | Already written as a deliberate choice. Effective. |
| Series closure | Readers have invested across 7 articles; need a satisfying close | MEDIUM | Written: "The trade-offs are real. Make them conscious." Must not introduce new concepts at this stage. |

---

### Differentiators (Series Competitive Advantage)

Features that set these articles apart from generic AI risk writing. These align with the series' core value: showing practitioners how to consciously position on the Speed/Understanding/Reliability trade-off triangle.

#### Article 3 Differentiators

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Prather et al. "Fragile Experts" data as new named concept | 77% maintenance failure rate is more compelling than general statistics; "Fragile Experts" gives readers a concrete term to recognize and share | MEDIUM | Flagged as TODO in article 3. The study is directly cited — 78 participants, scaffolded vs. unrestricted condition. HIGH confidence. Strengthens the "these aren't outliers" section with experimental (not just observational) evidence. |
| Stochastic Spaghetti Effect (Ngabang, 2026) as named failure mechanism | Named mechanisms are memorable and shareable; "stochastic spaghetti" is distinctive enough to become a reusable vocabulary term for the series | MEDIUM | Flagged as TODO in article 3. Already partially woven into article 4 (email validation scenario). Positioning this here, in the failure taxonomy article, creates forward reference consistency. |
| Pre-LLM vs. Post-LLM shift as structural opening | Framing what changed (not just that it changed) gives readers a causal model before the case studies | LOW | Flagged as TODO. The friction-as-pedagogy argument is the strongest philosophical contribution this article makes — the friction that once limited epistemic debt has been removed. |
| Explicit failure taxonomy (boundary gaps, not just incidents) | Moving from "bad things happened" to "the gap was in X" is the analytic value-add; connects case studies to article 4's mechanism | LOW | Already partially written in "The Pattern" section. Each case study's gap type should be explicitly named: system boundaries, defensive coding, edge case reasoning. |
| CAST Software + Veracode 2026 security debt connection | Positions epistemic debt as the upstream cause of security debt, not just correlated with it — this is a causal claim that most AI risk writing doesn't make | MEDIUM | Flagged as TODO. Security debt as downstream consequence of epistemic debt is the key insight. Requires careful phrasing to avoid overstating causation. |

#### Article 4 Differentiators

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Anthropic skill formation study as quantitative backbone | Most articles about junior developer crisis use anecdote; a randomized controlled trial with 17% comprehension gap is a stronger anchor | MEDIUM | NEW (Jan 2026). 52 junior engineers, Trio library, randomized design. The debugging gap finding directly supports the "skills gap" section. The divide between conceptual-AI-users (65%+) vs code-delegation users (below 40%) is the series' clearest quantitative statement of the learning mechanism. |
| Social invisibility framing for solutioning trap | Explains *why* teams don't notice the trap forming — technical debt has social stigma, epistemic debt feels like collaboration | MEDIUM | Flagged as TODO. The three distinctions (social dynamics, localization, manifestation timing) are the most philosophically precise contribution article 4 makes. This is what separates the series from generic "AI code is risky" writing. |
| t₀ connection to SDLC boundaries | Links the mathematical framework from article 2 to the practical boundary analysis; gives mathematical readers an anchor | HIGH | Flagged as TODO. t₀ = point where deterministic mechanisms surface gaps early enough to keep Σ_k c_k · τ_k < δ. This is a medium-difficulty integration — needs to be light enough to not lose practitioner readers, substantive enough to satisfy technically-oriented readers. |
| fast.ai "dark flow" psychological analysis | Adds psychological depth to automation bias — vibe coding produces a flow state that actively resists interruption, making the trap self-reinforcing | LOW | NEW (Jan 2026). "Breaking the Spell of Vibe Coding" — psychological analysis of why vibe coding feels productive even when it isn't. Framing this as "dark flow" (a corrupted version of Csikszentmihalyi's flow state) gives the mechanism a memorable name. |

#### Article 5 Differentiators

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| ε_k tolerance factor integration | Formalizes the "not all code deserves equal epistemic investment" claim mathematically — closes a seed planted in article 2 | HIGH | Flagged as TODO. Core domains: ε_k ≈ 0. Generic domains: large ε_k (strategic ignorance is economically rational). This closes the mathematical arc. Medium complexity to write correctly without losing non-mathematical readers. |
| Strategy forces as t₀ shifters | Connects the four strategies (DDD, human E2E tests, human review, structured workflow) back to the article 2 formula — makes the framework mechanistic, not just descriptive | HIGH | Flagged as TODO. DDD shifts t₀ leftward at L3-L4. Human E2E tests shift t₀ at L1-L2. Frame as deterministic mechanisms that keep Σ_k c_k · τ_k < δ. |
| File-path-level IRIS-2 specificity | Most practitioner case studies describe practices at a high level; naming the actual files (`test_user_journey_e2e.py`, `.cursor/rules/experiments.mdc`) makes the claim verifiable | LOW | Already written. This is what separates IRIS-2 from a generic "we used DDD" claim. Preserve this specificity in all revisions. |
| Epistemic review vs. code review distinction | Shifts PR review from quality assurance to knowledge validation — "can you explain this?" vs. "does this work?" | MEDIUM | Already written. The four questions for reviewers are the most actionable takeaway in the series. |

#### Article 6 Differentiators

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Bus factor team-level formulation | Makes the bus factor concept mathematical — Gc_k,team = min over critical members (the chain-breaks-at-weakest-link formulation) | MEDIUM | Flagged as TODO. Should be presented as a thought experiment, not a formula, to maintain practitioner accessibility. |
| Senior Expertise Gap as systemic measurement concern | r_k (learning rate) is not a constant — it degrades as junior pipeline narrows. This makes recovery cost projections underestimates. A 5-10 year structural problem, not a team-level problem. | MEDIUM | Flagged as TODO. Connects to Anthropic skill formation data (NEW). Emeritus LinkedIn Economic Graph data on entry-level hiring slowdown in AI-exposed sectors. This is the most forward-looking claim in the article — flag as speculative. |
| Honest framing of what EEG research implies | Self-reported understanding metrics may systematically underestimate epistemic debt — the gap between "think I understand" and "actually understand" may be larger than assumed | LOW | Already written. The Dunning-Kruger connection is the uncomfortable implication the article needs to name explicitly. |
| Architectural decision temporal validity | AI-assisted engineering should track the epistemic status and temporal validity of architectural decisions — decisions made when nobody understood the codebase have a different epistemic status than decisions made with full comprehension | MEDIUM | Flagged as TODO in article 6 ("AI-ASSISTED ENGINEERING SHOULD TRACK THE EPISTEMIC STATUS AND TEMPORAL VALIDITY OF ARCHITECTURAL DECISIONS"). This is a concrete, actionable idea that no existing writing in the series has developed. |

#### Article 7 Differentiators

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Journalistic epistemic authority framing | The 2026 Tandfonline study on journalistic epistemic authority in AI newsrooms gives article 7's content creation domain a peer-reviewed anchor — not just a thought experiment | MEDIUM | NEW (2026). "Journalistic Epistemic Authority in the Age of AI" — directly validates the content creation domain analysis. Provides an academic citation for what was previously inference. |
| Self-referential meta-section | Series about epistemic debt in AI-assisted work, written with AI assistance — author's positioning on their own triangle is the closing argument that the framework is real and usable | LOW | Already written. This is the unique move no other technical writing makes. Preserve it exactly as written. |
| "Wrong question" reframing | "Will AI replace X?" is the economic frame. The epistemic frame is the series' actual contribution — the risk is comprehension, not employment. | LOW | Already written as the series close. The most memorable line in article 7. |
| Human Debt forward reference | Accumulated psychological burden (impostor phenomenon, anxiety, burnout) from AI-assisted work compounds with epistemic debt — naming this as a distinct concept that deserves its own article creates a credible "what comes next" signal | LOW | Flagged as TODO in article 3 (moved from article 2). Best placed as a brief forward reference in article 7's closing, not as a full section. Signals series continuity beyond article 7. |
| Vibe coding open-source crisis angle | AI-flooded open-source contributions are creating epistemic debt at a community level, not just an organizational level — maintainers can't audit AI-generated PRs | MEDIUM | NEW (InfoQ, Feb 2026). Extends the "beyond software" framing to include community-scale epistemic debt. Strong differentiator — this is ecosystem-level, not just team-level. Belongs in the "universal meta-patterns" section as a case where HITL breaks down at scale. |

---

### Anti-Features (Commonly Tempting, Specifically Problematic)

Features that seem like improvements but would damage the series' core value or publication properties.

| Anti-Feature | Why Tempting | Why Problematic | Alternative |
|--------------|--------------|-----------------|-------------|
| Prescriptive "here's what to do" framework | Readers often want action plans; feels complete | Violates the series brand promise; the series is explicitly non-prescriptive. Turning the triangle into a checklist removes the philosophical substance that makes it credible. | Present the 5-step protocol in article 7 as "a way to ask the questions," not "the answer." Maintain conditional language: "core domains may warrant," not "core domains require." |
| Heavy academic citation style | Looks rigorous; feels authoritative | Audience is practitioners, not academics. Citation density appropriate for a journal paper breaks the Substack reading flow. The series already has exactly the right citation density (footnoted references, not inline). | Maintain: one or two prominent studies per section, cited in references. Let the evidence do the work through narrative, not citation count. |
| Adding new case studies that duplicate article 3's function | More examples feels more convincing | Articles 4–7 each have a distinct function. Adding new default events in article 4 (mechanism) or article 5 (framework) dilutes those articles' identity and creates redundancy. Article 3 is the evidence article. | Forward-reference article 3 examples when articles 4–7 need evidence. Do not introduce new failure incidents after article 3. |
| Resolving all TODO items as new H2 sections | TODOs are flagged content; resolving all of them seems thorough | Not all TODOs should become new sections. Some are integrations (Prather et al. data into existing section), some are connection notes (t₀ references as brief paragraph additions), some should be deferred (Human Debt to future series). Adding sections risks bloating articles already at or above target length. | Resolve each TODO as a targeted insertion: sentence, paragraph, or data point within existing sections. New sections only if the content is structurally new (e.g., "Social Invisibility of Epistemic Debt" in article 4). |
| Introducing the Ed formula in articles 4–7 | Mathematical rigor; connects to article 2's foundation | Articles 4–7 are practitioner-facing. Repeating the formula in multiple articles would feel redundant for series readers and confusing for article-specific arrivals. | One brief back-reference per article ("as defined in article 2") is sufficient. The ε_k and t₀ extensions should be explained in English with the formula in parentheses or footnote. |
| Covering "Human Debt" as a full section | Real concept; emotionally resonant | The concept is introduced in article 2's TODO but is genuinely underdeveloped for article-length treatment. Including it as a full section in any article 3–7 would be incomplete and risk misleading readers. | Mention once in article 7's closing as a named concept deserving future exploration ("A companion pattern we'll return to: Human Debt — the psychological burden that compounds with epistemic debt"). |
| Self-referential meta-content as more than one section | The series-written-with-AI angle is interesting | If overused, the meta-observation becomes navel-gazing. Article 7 already has the definitive self-referential section. Articles 3–6 should not mention this. | Keep the self-referential material in article 7 only, exactly as written. |
| Extending article 7 to include a "future research agenda" section | Academic framing; seems comprehensive | Breaks the non-academic register. Also, the series closes with practitioner action, not academic agenda-setting. | Replace with the Human Debt forward reference and a single closing note that the framework is evolving. |

---

## Feature Dependencies

```
[Article 3: Evidence]
    └── establishes──> [Named failure types: system boundaries, defensive coding, edge case reasoning]
                           └── required by──> [Article 4: Mechanism explanation]
                                                  └── required by──> [Article 5: Triangle framework]

[Article 2: Ed formula + δ threshold]
    └── extends──> [Article 5: ε_k tolerance factor] (closes mathematical arc)
    └── extends──> [Article 4: t₀ connection to SDLC boundaries]
    └── extends──> [Article 6: r_k degradation, Senior Expertise Gap]

[Article 3: Three case studies]
    └── forward-referenced──> [Articles 4, 5, 7]
    └── must NOT be repeated in──> [Articles 4–7 as new incidents]

[Article 5: Triangle framework + strategy forces]
    └── generalizes──> [Article 7: Beyond software domains]
    └── provides measurement hooks──> [Article 6: What to measure]

[Article 6: Measurement difficulty]
    └── sets honest expectations for──> [Article 7: Protocol doesn't promise measurement]

[Article 7: Self-referential close]
    └── only works if──> [Articles 1–6: Established author's epistemic ownership of the series]
```

### Dependency Notes

- **Article 3 establishes the failure taxonomy**: Articles 4 and 5 reference specific failure types (system boundary gap, edge case reasoning gap) by name. If article 3's "The Pattern" section changes the taxonomy, articles 4–5 need consistency checks.
- **Article 2's formula extends into articles 4, 5, and 6**: The t₀ connection (article 4), ε_k factor (article 5), and r_k degradation (article 6) are all mathematical extensions of article 2. Each extension should be brief enough that readers who skipped article 2 are not blocked — a one-sentence orientation is sufficient before each extension.
- **Article 5's triangle is required context for article 7**: Article 7 opens with "The triangle generalizes" — readers who arrive at article 7 without reading article 5 need enough embedded context to follow. The domain comparison tables are self-contained enough to serve standalone readers.
- **IRIS-2 appears only in article 5**: Do not introduce new IRIS-2 details in articles 3, 4, 6, or 7. Article 5 is the designated case study home.
- **Article 7's self-referential close depends on series coherence**: The meta-observation ("this series was written with LLM assistance") only works if the series has maintained consistent epistemic discipline across all articles. Sloppy evidence handling in articles 3–6 would undermine the closing claim.

---

## MVP Definition

### Publish With (v3.0)

Minimum viable set for each article to stand on its own and function within the series.

- [ ] **Article 3**: Integrate Prather et al. "Fragile Experts" data into "These Aren't Isolated Incidents" section — this is the most important gap; it provides experimental evidence where all other evidence is observational. Integrate CAST + Veracode 2026 statistics. Add Pre-LLM vs. Post-LLM opening context. Resolve Ngabang naming. Verify all citations are properly formatted.
- [ ] **Article 4**: Integrate Anthropic skill formation study (17% comprehension gap, debugging gap) into junior developer section — replaces the less precise existing statistics. Add social invisibility framing as a discrete subsection before "Translation Boundaries." Resolve t₀ connection as one paragraph in each boundary section (not a new section). Check TODO about Boundary 3 being moved to article 5 — update bridge accordingly.
- [ ] **Article 5**: Resolve ε_k tolerance factor TODO (one paragraph, formula in footnote). Resolve strategy forces t₀ connection TODO (column addition to the strategy table). Verify ASCII triangle diagram renders correctly in Substack. Check that Boundary 3 (Implementation→Validation / Circular Validation) is fully explained here, since it moved from article 4.
- [ ] **Article 6**: Integrate Senior Expertise Gap material as a new subsection under "The Honest Caveat" (flags r_k as a degrading variable, connects to Anthropic data). Integrate architectural decision temporal validity as a brief practical recommendation. Resolve bus factor team formulation as a bracketed thought experiment (no formula, English framing).
- [ ] **Article 7**: Add journalistic epistemic authority citation to content creation domain section. Add Human Debt as a one-paragraph forward reference in the closing. Add open-source epistemic debt angle (brief paragraph under HITL meta-pattern section, noting HITL breaks down at community scale). Verify series close lands correctly.

### Add After Publication if Engagement Warrants (v3.x)

Features to add once core articles are live and reader response is known.

- [ ] Interactive triangle positioning tool — readers enter their project context and get positioning guidance. Deferred: requires technical implementation outside Substack. Add if article 5 generates high engagement requests for "what does this mean for my project."
- [ ] Companion full-length article synthesizing all 7 articles — referenced in article 7 but not yet written. Add if series generates demand for a single-document reference.
- [ ] "Human Debt" article (Series Part 8 or separate series) — referenced as forward signal in article 7. Add if reader response to the human dimension of epistemic debt is strong.
- [ ] Domain-specific deep dives (content epistemic debt, research epistemic debt) — article 7 covers them in ~300 words each. Add if specific audiences (journalists, researchers) respond strongly to their domain section.

### Future Consideration (v4+)

- [ ] Academic paper version — explicitly out of scope for current milestone, but article 3's evidence + article 5's framework could form the basis.
- [ ] Conference talk adaptation — the IRIS-2 presentation (v1.0) already demonstrated this is viable.

---

## Feature Prioritization Matrix

### Article 3

| Feature | Reader Value | Implementation Cost | Priority |
|---------|-------------|---------------------|----------|
| Prather et al. Fragile Experts data integration | HIGH — experimental evidence upgrades all observational data in the article | LOW — targeted paragraph insertion | P1 |
| Pre-LLM vs. Post-LLM opening context | HIGH — causal framing before case studies | LOW — one new section opening | P1 |
| Stochastic Spaghetti Effect naming (Ngabang) | MEDIUM — adds vocabulary, consistency with article 4 | LOW — naming and short description | P1 |
| CAST + Veracode 2026 statistics | MEDIUM — strengthens "not outliers" argument | LOW — data insertion into existing paragraph | P2 |
| Human Debt concept (reserve for article 7) | LOW for article 3 specifically | LOW to add; risk of scope creep | P3 — defer to article 7 |

### Article 4

| Feature | Reader Value | Implementation Cost | Priority |
|---------|-------------|---------------------|----------|
| Anthropic skill formation study (17% gap) | HIGH — quantitative anchor for mechanism | LOW — replaces weaker statistics | P1 |
| Social invisibility subsection | HIGH — explains why the trap goes unnoticed; most philosophically novel content in the article | MEDIUM — new subsection, ~300 words | P1 |
| t₀ connection to SDLC boundaries | MEDIUM — connects to article 2 math; rewards series readers | MEDIUM — one paragraph per boundary | P2 |
| fast.ai "dark flow" psychological framing | LOW-MEDIUM — adds color to automation bias section | LOW — brief addition | P2 |

### Article 5

| Feature | Reader Value | Implementation Cost | Priority |
|---------|-------------|---------------------|----------|
| ε_k tolerance factor integration | HIGH — closes mathematical arc from article 2 | MEDIUM — requires careful English explanation | P1 |
| Strategy forces as t₀ shifters | MEDIUM — rewards mathematically-oriented readers | MEDIUM — table column addition + brief prose | P2 |
| ASCII triangle rendering check | HIGH — framework article fails if the visual is broken | LOW — test in Substack preview | P1 |

### Article 6

| Feature | Reader Value | Implementation Cost | Priority |
|---------|-------------|---------------------|----------|
| Architectural decision temporal validity | HIGH — the most actionable new idea in the article | MEDIUM — new practical recommendation paragraph | P1 |
| Senior Expertise Gap integration | MEDIUM — forward-looking structural concern | MEDIUM — new subsection under honest caveat | P1 |
| Bus factor team formulation | LOW-MEDIUM — mathematical precision; accessible to fewer readers | LOW — English thought experiment | P2 |

### Article 7

| Feature | Reader Value | Implementation Cost | Priority |
|---------|-------------|---------------------|----------|
| Journalistic epistemic authority citation | MEDIUM — credibility boost for content creation domain | LOW — citation addition | P1 |
| Human Debt forward reference | MEDIUM — signals series continuity, rewards loyal readers | LOW — one paragraph | P1 |
| Open-source epistemic debt angle | LOW-MEDIUM — extends "beyond software" to ecosystem level | LOW — brief addition to HITL section | P2 |

---

## Article-Type Content Patterns

Recommendations for structural patterns based on each article's genre within the series.

### Article 3 Pattern: Evidence-First, Mechanism-Close

Evidence articles build credibility and create emotional stakes before delivering the analytical payoff.

**Effective structure:**
1. Bridge from prior articles (one paragraph — already written)
2. Pre-LLM vs. Post-LLM shift (new opening context — explains *why defaults are worse now*)
3. Case studies (dramatic → quantified → domain-generalizing — already written in this order)
4. The pattern synthesis (names the mechanism across all three cases)
5. Industry statistics (validates that cases are not outliers — expands with 2026 data)
6. Closing hook (already written: "The question is: how do teams fall into this pattern?")

**What to avoid:** Introducing new mechanisms or frameworks in the evidence article. Article 3 is for establishing stakes, not explaining causes. The "stochastic spaghetti effect" naming is appropriate as a named failure *type*, not as a new mechanism requiring extended explanation.

### Article 4 Pattern: Mechanism-Then-Map

Mechanism articles must explain *why* before showing *where*. Psychological underpinning precedes structural analysis.

**Effective structure:**
1. Bridge from article 3 (already written)
2. Name and define the mechanism (solutioning trap)
3. Worked scenario (rate limiter — already effective)
4. Psychological layer (automation bias + dark flow — new Anthropic data strengthens this)
5. Social invisibility layer (new subsection — explains why mechanism goes unnoticed)
6. Structural map (SDLC boundaries — where the mechanism operates)
7. Velocity trap arc (temporal compounding — already written)
8. Closing hook (bridge to article 5)

**What to avoid:** Starting with the structural map before the psychological mechanism. The insight is *why* the trap works (psychology), not just *where* it shows up (structure). The "where" section is only satisfying after readers understand "why."

### Article 5 Pattern: Framework-Grounded-in-Practice

Framework articles fail when theory precedes proof. IRIS-2 must appear early enough to ground the framework, not as an afterthought.

**Effective structure (current article 5 follows this well):**
1. Bridge from article 4
2. Universal triangle introduction (with the visual)
3. Circular validation trap (Boundary 3, moved from article 4 — the "╳ trap" on the triangle)
4. Strategy forces through IRIS-2 (proof that the framework is not just theory)
5. Domain-based positioning (how to apply different levels of rigor)
6. Practitioner takeaways (actionable close)

**What to avoid:** Separating the framework introduction from the IRIS-2 case too much. The triangle should feel like something that *emerged from practice*, not something applied to practice.

### Article 6 Pattern: Honest-Then-Practical

Measurement articles that lead with "here's how to measure it" lose credibility. The honest admission must precede the practical guidance.

**Effective structure (current article 6 follows this):**
1. The fundamental challenge (understanding is in minds, not codebases)
2. The measurement paradox
3. The correlation-causation trap (with concrete examples)
4. What we can measure today (proxy indicators)
5. Triangulation table
6. What's emerging (research frontier)
7. The honest caveat (including Senior Expertise Gap as new material)

**What to avoid:** Positioning the proxy indicators as "the solution." The article's value is in being honest about the limits of measurement, not in providing a measurement framework. The triangulation section should be presented as "useful signal in the absence of direct measurement," not as a substitute for direct measurement.

### Article 7 Pattern: Generalize-Apply-Close

Capstone articles should move from generalization to application to closure in a single arc, without introducing new evidence or mechanisms.

**Effective structure (current article 7 follows this):**
1. Bridge from article 6 + series summary (already written)
2. Why the triangle generalizes (structural properties argument)
3. Domain applications (five domains, comparison tables)
4. Universal meta-patterns (HITL, Pre-Specification, RAG, Adversarial Testing)
5. 5-step application protocol
6. Self-referential meta-section
7. Series closure

**What to avoid:** Adding new evidence or case studies in article 7. The generalization works because it is *structural*, not because it adds more examples. Any new evidence introduced here would feel like the article didn't trust its own argument.

---

## Sources

### HIGH Confidence (Official Research)
- Anthropic (2026). "How AI assistance impacts the formation of coding skills." https://www.anthropic.com/research/AI-assistance-coding-skills
- Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv:2602.20206. https://arxiv.org/html/2602.20206

### MEDIUM Confidence (Industry/Academic Sources)
- Tandfonline (2026). "Journalistic Epistemic Authority in the Age of AI." https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2640421
- InfoQ (Feb 2026). "AI 'Vibe Coding' Threatens Open Source as Maintainers Face Crisis." https://www.infoq.com/news/2026/02/ai-floods-close-projects/
- fast.ai (Jan 2026). "Breaking the Spell of Vibe Coding." https://www.fast.ai/posts/2026-01-28-dark-flow/
- Emeritus (2026). "The Hidden Cost of AI Adoption." https://emeritus.org/blog/lnd-the-hidden-cost-of-ai-adoption/

### Existing HIGH Confidence Sources (from v2.0 research)
- CodeRabbit (2025). "State of AI vs Human Code Generation Report."
- GitClear (2025). "AI Copilot Code Quality: 2025 Research."
- Stack Overflow Developer Survey (2025).
- AlterSquare (Dec 2025). "GitHub Copilot Saved Us 200 Hours: Then Cost Us 2000 Hours in Bug Fixes."
- CAST Software (2025). "Coding in the Red."
- Veracode (2026). "2026 State of Software Security."
- Ngabang, L.A. (2026). "The Illusion of Competence." viXra:2601.0013v1.

---

*Feature research for: Epistemic Debt Series Articles 3–7*
*Researched: 2026-03-14*
