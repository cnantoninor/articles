# Pitfalls Research

**Domain:** Mid-to-late-series Substack articles for a practitioner-focused series on epistemic debt in LLM-assisted work
**Researched:** 2026-03-14
**Confidence:** HIGH (based on direct review of all seven draft articles, published articles 0-2, and project documentation)

---

## Context: What Makes This Situation Specific

Articles 0-2 are published and have established:

- A specific prose register: exploratory, first-person plural where fitting, no bullet-point prescriptions in the body
- A conceptual foundation: the Ed formula (Cs(t) − Gc(t) integral), the six-dimension comparison with technical debt, and three published case studies
- An audience expectation: practitioners who chose to follow a series, not one-off readers
- A cross-reading contract: Article 0 promises specific paths (Evidence-First → Article 3 then 1, Leaders → 1, 2, 5, etc.)

The pitfalls below are specific to this context. Generic "how to write good articles" advice is omitted.

---

## Critical Pitfalls

### Pitfall 1: Recapping Prior Articles as Filler, Not as Anchor

**What goes wrong:**
Each article 3-7 opens with a summary of what came before. Done carelessly, the recap pads word count and punishes readers who have been following from the start. Done too briefly, it alienates readers entering mid-series (which Article 0 explicitly invites). The result is a recap that serves neither audience.

**Why it happens:**
The impulse to orient the reader is correct, but the execution defaults to plot summary ("in the previous article, we defined X"). Plot summary rehashes rather than reactivates. The reader who has been following doesn't need facts restated; they need their existing understanding mobilized for what's coming next.

**How to avoid:**
Use the opening paragraph to *apply* prior concepts to a new frame rather than restate them. Article 3 does this well: "In the previous articles, we defined epistemic debt as the growing gap between system complexity and team understanding. We gave it a formula. We distinguished it from technical debt. Now let's see what happens when the bill comes due." This is two sentences of anchor and one of propulsion — not a recap. Article 5 does it less well ("The patterns described in the previous articles...") — it names the patterns without activating them. Prefer activation over recitation.

**Warning signs:**
- The first paragraph ends without forward momentum
- The recap could be deleted without affecting the body of the article
- The recap contains information only useful to someone who *hasn't* read prior articles
- The recap runs longer than three sentences before introducing the article's new contribution

**Phase to address:**
Article 3 draft review — establish the recap discipline early so it carries through 4-7.

---

### Pitfall 2: Tone Drift Toward Prescription in Framework Articles

**What goes wrong:**
Articles 5 and 7 present frameworks (the Trade-off Triangle, the 5-step protocol). The series' entire posture is exploratory and non-prescriptive — "here's what I've found worth examining." Framework articles create structural pressure to flip into "do this, not that" mode. When they do, they betray the series' voice and audience contract.

**Why it happens:**
Frameworks invite numbered steps. Numbered steps invite imperative mood. Imperative mood is prescriptive. The slide from "here is how teams have navigated this trade-off" to "here is how you should navigate this trade-off" is a single word change — and an easy slip to make at revision time, when tightening sentences tends to strip hedges.

**How to avoid:**
Preserve first-person-plural and investigative framing throughout framework sections. "Teams that adopt DDD find that..." rather than "You should adopt DDD." "One approach that consistently pulls toward Understanding..." rather than "Always use DDD for core domains." The 5-step protocol in Article 7 is the highest-risk section — each step should be framed as what practitioners report doing, not what practitioners must do. The closing line of Article 5 ("The framework is deliberately non-prescriptive. It doesn't tell you where to position — it gives you language for making the choice conscious") is the correct register; make sure the body earns that claim.

**Warning signs:**
- Numbered steps written in imperative mood without hedging
- Absence of qualifiers like "for teams with X constraint," "when the context is Y"
- The article reads like a methodology guide rather than a field observation
- The IRIS-2 example disappears and the article speaks in universal terms without grounding

**Phase to address:**
Article 5 revision pass; Article 7 protocol section.

---

### Pitfall 3: Evidence Overload in Article 3 Breaking the Narrative

**What goes wrong:**
Article 3 is the evidence-heavy article (case studies + industry data). The draft contains the three case studies *plus* four TODO blocks adding more data (Fragile Expert study, CAST Software report, Veracode 2026, Ngabang stochastic spaghetti effect). Adding all of these creates an article that is dense with numbers and risks becoming a literature review rather than a practitioner narrative.

**Why it happens:**
Evidence accumulates because each piece is legitimately relevant. The instinct to be thorough is correct. But the audience (practitioners, not academics) chose a Substack series, not a meta-analysis. They need enough evidence to believe the phenomenon is real, not a comprehensive citation of all evidence.

**How to avoid:**
Apply a "one study per claim" discipline. The claim "velocity is up, quality metrics are down" is supported by three data points in the current draft (GitClear churn, Cortex incidents, Veracode security failures). Adding the CAST report adds a fourth data point for the same claim. More evidence for the same claim does not strengthen the reader's conviction — it shifts the genre. Select the most concrete single data point per claim and footnote the rest. The Fragile Expert study (Prather et al., arXiv) is the most actionable addition because it demonstrates a *mechanism* (metacognitive friction), not just a correlation — consider it as the one TODO to integrate.

**Warning signs:**
- Three or more statistics in a single paragraph
- The industry data section runs longer than the case studies section
- The reader needs to track multiple studies to understand one point
- The article starts feeling like an evidence dump rather than a narrative

**Phase to address:**
Article 3 final draft — evidence curation pass after all TODOs are resolved.

---

### Pitfall 4: Honest Measurement Caveats Undermining Series Credibility

**What goes wrong:**
Article 6 ("Measuring the Unmeasurable") is deliberately honest about what we cannot yet measure. The risk: a reader who has been following the series reaches Article 6 and concludes "so the whole series was speculation." The caveats, meant to demonstrate intellectual honesty, instead destabilize the conceptual foundation built in Articles 1-2.

**Why it happens:**
Honesty about measurement limitations is methodologically correct. The failure mode is structural rather than factual: the caveats appear without being anchored to what *is* established. The article concedes "we don't have controlled longitudinal studies" but does not explicitly protect the prior articles' conceptual claims. A reader who is looking for a reason to dismiss the framework finds ammunition.

**How to avoid:**
Separate epistemic claims into two explicit tiers at the article's opening:
- Tier 1: Conceptual claims with high confidence (the accumulation mechanism, the formula structure, the qualitative case studies) — these are established
- Tier 2: Empirical measurement claims with low confidence (precise Ed values, controlled longitudinal data, proxy indicator validity) — these are provisional

Make this separation explicit rather than leaving the reader to infer it. The technical debt parallel is the right anchor: "We couldn't precisely measure technical debt for decades, but we knew it when we saw it." This line already exists in Article 6 — it should appear earlier and be given more structural weight.

**Warning signs:**
- The article leads with "not well. Not yet." without first anchoring what is well-established
- Caveats appear before the proxy indicators are introduced
- The final impression of the article is uncertainty rather than "honest about limits, confident about the phenomenon"
- The measurement paradox section runs longer than the "what we can measure" section

**Phase to address:**
Article 6 structural revision — reorder to establish before conceding.

---

### Pitfall 5: Series Fatigue in the Capstone Through Over-Generalization

**What goes wrong:**
Article 7 ("Beyond Software") must generalize the framework to content creation, LLM-as-judge, research, decision support, and data analysis. At five domains, each covered in a table and two paragraphs, the article risks becoming a pattern-matching exercise. The reader has been following for six articles; they recognize the triangle; they can predict what the software→content mapping will say before reading it. The capstone becomes anticlimactic.

**Why it happens:**
The obligation to generalize is real — Article 0 promises it, non-software readers were explicitly invited to jump to Article 7. But meeting that obligation through repetition of the triangle structure across five domains produces diminishing returns after the second or third domain.

**How to avoid:**
Lead with one domain generalization done deeply — the one with the most non-obvious insight — before moving to the comparative tables. The current draft buries the most interesting insight: "over time, authors who rely on LLM drafting can lose their own voice... the loss of the capacity for original expression." That is a qualitatively different kind of epistemic debt than software understanding loss, and it deserves expansion. The domain tables are useful as reference material but should not carry the article's argument. The self-referential closing section ("This article, self-referentially") is the capstone's strongest moment — the draft buries it after the protocol; consider moving it earlier.

**Warning signs:**
- All five domain sections have the same three-element structure (table, failure mode paragraph, strategy mention)
- No domain generalization surfaces a genuinely new insight not implied by the software case
- The 5-step protocol is the article's climax rather than an appendix
- Readers who only joined at Article 7 cannot tell which domain the author finds most interesting

**Phase to address:**
Article 7 structural planning — decide which domain is the lead example before drafting.

---

### Pitfall 6: Conceptual Drift in Article 4 — Vibe Coding Scope Creep

**What goes wrong:**
Article 4 introduces "vibe coding," automation bias, the junior developer crisis, and SDLC translation boundaries. These are four distinct concepts. The current draft handles all four well individually, but the article's thesis — what the "solutioning trap" actually *is* — risks becoming fuzzy. A reader finishing the article may understand each concept but not be able to state what the solutioning trap is in one sentence.

**Why it happens:**
The draft grew from a richer conceptual source (the longer article.md) and carries more material than a single-thesis article needs. Each section was individually justified, so no single section is obviously cuttable, but the article lacks a single spine.

**How to avoid:**
The solutioning trap has a clear definition in the draft: "jumping to implementation before understanding the problem well enough to evaluate the solution." Every section should be explicitly connected to this definition. Automation bias is a mechanism that makes the trap harder to escape. The junior developer crisis is an amplified consequence. The SDLC boundaries are the *locations* where the trap fires. The velocity trap is the *temporal pattern* of consequences. This is a coherent structure — it needs to be made explicit, not left for the reader to assemble. Consider adding a one-sentence spine at the end of each section that explicitly names how that section connects to the trap definition.

**Warning signs:**
- The article's subtitle ("Why experienced engineers ship code they can't explain") is not answered until the automation bias section
- The junior developer section feels like a separate article about career trajectories
- The translation boundaries section is longer than the trap definition section
- A reader asked to define "the solutioning trap" after reading gives a different answer depending on which section they found most memorable

**Phase to address:**
Article 4 final revision — add connective tissue between sections.

---

## Integration Pitfalls

These pitfalls are specific to adding articles to an existing published series.

### Pitfall I-1: Breaking the Cross-Reading Paths Established in Article 0

**What goes wrong:**
Article 0 establishes explicit reading paths: "Evidence-First readers → Article 3, then 1." "Leaders → 1, 2, 5." These paths create reader expectations about what each article delivers. If the final drafts of articles 3, 5, and 7 don't deliver what Article 0 promised at each entry point, returning to Article 0 to fix the description after publication requires a correction to a published article.

**How to avoid:**
Before finalizing each article, verify it against its Article 0 description. Article 3 is promised as "45% security failure rates, incident increases per PR, 4× code churn. My personal examples and lessons learned." The current draft has the statistics but the personal examples are light. Article 5 is promised as "Strategy forces to control the trade-off: Domain Driven Design, human driven tests." The draft delivers this. Article 7 is promised as "Five-step protocol for any domain" — the draft delivers the protocol but it is positioned as an appendix rather than a deliverable.

**Warning signs:**
- A section promised in Article 0 does not appear in the corresponding article
- An article covers material not mentioned in Article 0 without flagging it as a bonus
- The "Evidence-First" reader jumping to Article 3 encounters a different opening than what Article 0 implies

**Phase to address:**
Pre-publication review for each article — cross-check against Article 0 description.

---

### Pitfall I-2: Tone Drift Through the Series Arc

**What goes wrong:**
Articles 1-2 establish a philosophical, exploratory tone. Articles 3-4 are more evidence-dense and mechanism-focused. Articles 5-7 are framework-oriented. The natural drift is for later articles to feel more prescriptive and less exploratory. By Article 7, the series has accidentally shifted genre from "practitioner investigation" to "methodology guide."

**Why it happens:**
Evidence articles (3) use authoritative language to present data. Framework articles (5, 7) use structured language to present frameworks. Both register shifts are locally justified but cumulatively represent tone drift.

**How to avoid:**
The investigative register must be actively maintained, not just preserved by default. In Articles 5 and 7, make the author's uncertainty visible: "IRIS-2 is one data point — whether these practices generalize is a genuine open question." In Article 6, model the epistemic honesty that the series advocates for. In Article 7, the self-referential closing is the tonal anchor — move it forward.

**Warning signs:**
- Articles 5, 6, and 7 could be read in isolation without any indication they are part of an exploratory series
- The author's first person ("I've been finding," "This strikes me as") disappears from the later articles
- The later articles feel like they could appear in a practitioner handbook rather than a Substack series

**Phase to address:**
Article 5, then sustained attention through 6 and 7.

---

### Pitfall I-3: Audience Confusion at Article 7 Entry Point

**What goes wrong:**
Article 0 explicitly invites non-software readers to enter at Article 7. Article 7 opens with "For six articles, we've explored epistemic debt through a software engineering lens." A non-software reader starting at Article 7 immediately encounters framing that presupposes software engineering context and six prior articles. The invite and the execution are misaligned.

**How to avoid:**
The first paragraph of Article 7 needs a dual-track opening: enough context for a non-software reader to understand what epistemic debt is without requiring them to have read Articles 1-6, while maintaining continuity for readers arriving at the capstone. The current draft can be fixed with a brief embedded definition: "epistemic debt — the accumulated gap between system complexity and team understanding — was framed in this series through software engineering." This lets Article 0's entry point promise be fulfilled without restructuring the article.

**Warning signs:**
- Article 7's opening paragraph uses "the previous articles" as the primary orientation device
- The Trade-off Triangle diagram in Article 5 is referenced in Article 7 without being reintroduced for new readers
- A non-software reader arriving at Article 7 via the Article 0 link would need to backtrack to understand the first two paragraphs

**Phase to address:**
Article 7 opening section revision.

---

## Narrative Momentum Pitfalls

### Pitfall N-1: The Conceptual Cliffhanger Is Not Being Paid Off

**What goes wrong:**
Each article ends with a "next in the series" teaser. These teasers create forward momentum expectations. If the next article's opening does not fulfill the specific expectation created, readers feel a narrative seam. Article 3 ends promising "why experienced engineers ship code they can't explain" — Article 4 delivers this but the connection is implicit, not explicit.

**How to avoid:**
The first paragraph of each article should name what the previous article's teaser promised and confirm that it is being delivered. This is not recap — it is promise fulfillment. "Article 3 asked how teams fall into the epistemic debt pattern. This article examines the specific mechanism: the solutioning trap — jumping to implementation before understanding the problem well enough to evaluate the solution."

**Warning signs:**
- The article opening does not echo the previous article's closing teaser language
- A reader would not immediately recognize that the opening answers the previous article's closing question
- The teaser promised a specific framing that the article opens with a different framing

**Phase to address:**
Article 4 opening; then 5, 6, 7 in sequence.

---

### Pitfall N-2: The IRIS-2 Case Study Overstaying Its Welcome

**What goes wrong:**
IRIS-2 appears heavily in Article 5 as the concrete grounding for the Trade-off Triangle strategies. It is the right case study for Article 5 — specific enough to be credible. The risk is that IRIS-2 details (specific file names, LOC numbers, bounded context names) appear so heavily that readers who are not software practitioners cannot follow Article 5, undermining the cross-domain audience.

**How to avoid:**
IRIS-2 details should be progressively abstracted: present a specific detail, then immediately state the generalizable principle. "IRIS-2 used five bounded contexts, each with glob-activated context files (.cursor/rules/*.mdc). The principle: DDD front-loads epistemic work into domain modeling so that LLM output can be verified against a shared vocabulary rather than generic plausibility." The specific detail establishes credibility; the principle statement makes it useful to non-IRIS-2 readers.

**Warning signs:**
- More than three IRIS-2 specific details (file names, LOC counts, specific tool names) in a single section without abstraction
- An engineering leader audience member could not extract actionable insight from the IRIS-2 sections
- The article could not be read by a content professional or researcher who entered via Article 7

**Phase to address:**
Article 5 IRIS-2 sections.

---

## "Looks Done But Isn't" Checklist

For each article in the 3-7 sequence before publication:

- [ ] **Conceptual anchor:** Article opens with a reference to prior content that activates (not just recaps) the prior work
- [ ] **Promise fulfillment:** The article's opening reflects the previous article's closing teaser
- [ ] **Article 0 alignment:** The article delivers what Article 0's description of it promises
- [ ] **Tone register:** First-person investigative voice is present — not just in opening, but sustained through framework sections
- [ ] **Evidence discipline:** No more than one study per claim; additional evidence footnoted rather than embedded
- [ ] **Framework framing:** Numbered steps and framework elements framed as observations or practices, not prescriptions
- [ ] **Dual-track opening (Article 7 only):** Non-software readers can orient without having read prior articles
- [ ] **TODO blocks resolved or explicitly deferred:** No unresolved TODOs in published text; deferred items noted in draft header
- [ ] **Cross-article formula references:** Ed formula and triangle references consistent with Articles 2 and 5 definitions
- [ ] **Closing teaser:** Each article's closing teaser names exactly what the next article will deliver

---

## Recovery Strategies

When pitfalls occur despite prevention, how to recover.

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Recapping as filler (caught post-publication) | LOW | Substack allows post-publication edits; revise opening paragraph |
| Tone drift toward prescription | MEDIUM | Revision pass adding investigative hedges; audit for imperative mood |
| Evidence overload (Article 3) | LOW | Remove or footnote excess statistics; narrative reads faster after removal |
| Caveats undermining credibility (Article 6) | MEDIUM | Add explicit tier-separation paragraph to opening; reorder measurement section to lead with what works |
| Capstone anticlimax (Article 7) | HIGH | Requires structural reorganization — self-referential closing moved forward, domain lead example expanded |
| Article 0 cross-reading paths broken | MEDIUM | Update Article 0 entry-point descriptions to match actual article content (possible post-publication) |
| Audience confusion at Article 7 entry | LOW | Add two-sentence embedded definition to Article 7 opening paragraph |
| Solutioning trap thesis fragmentation (Article 4) | LOW | Add one connecting sentence per section back to trap definition |

---

## Pitfall-to-Phase Mapping

How roadmap phases should address these pitfalls.

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| Recap as filler | Article 3 draft (establish the discipline early) | First paragraph of each article reviewed against "activation vs. recitation" test |
| Tone drift to prescription | Article 5 draft (highest framework risk) | Read framework sections aloud — passive/investigative vs. active/imperative |
| Evidence overload | Article 3 TODO resolution | Count statistics per paragraph; no more than one study per claim |
| Caveats undermining credibility | Article 6 structure planning | Article opens with tier separation; proxy indicator section is longer than caveat section |
| Capstone anticlimactic | Article 7 structure planning (before drafting) | Non-software reader can identify the article's strongest insight without reading all five domain tables |
| Cross-reading path breakage | Pre-publication review for each article | Article 0 descriptions cross-checked against final article content |
| Tone drift through arc | Article 5, sustained review | First-person investigative voice present in last two sections of each article |
| Article 7 audience confusion | Article 7 opening (first revision) | Non-software reader test: read first two paragraphs without prior series context |
| IRIS-2 over-specificity | Article 5 IRIS-2 sections | Each IRIS-2 specific detail followed by generalizable principle |
| Cliffhanger not paid off | Each article's opening paragraph | Opening paragraph names the prior teaser's promise explicitly |
| Solutioning trap fragmentation | Article 4 final revision | Reader can state the solutioning trap definition after reading any single section |

---

## Sources

- Direct review: `topics/epistemic_debt/artifacts/articles/article-0` through `article-7` (all draft and published versions)
- Project context: `.planning/PROJECT.md`
- Series constraints: `CLAUDE.md`, `.ai/rules/writing-style.md`, `.ai/rules/terminology.md`
- Established patterns from published articles 0, 1, 2

---
*Pitfalls research for: Epistemic Debt series, articles 3-7*
*Researched: 2026-03-14*
