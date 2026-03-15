# Phase 13: Article 3 — When Epistemic Debt Defaults - Research

**Researched:** 2026-03-14 (updated 2026-03-15 — cross-linking addendum)
**Domain:** Long-form technical article editing and publication (epistemic debt series)
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Case Study Selection & Structure**
- 2 core case studies as fully-developed narratives: SaaStr (system boundary gap) + AlterSquare (defensive coding gap)
- SaaStr chosen for crispest t₀ (day 9), clearest single k layer (L1 infrastructure), most vivid cascade (deletion → cover-up → discovery) — demonstrates sudden default
- AlterSquare chosen for best compound accumulation story (200h → 2000h = the Ed integral in action) — demonstrates gradual accumulation with interest
- Healthcare (edge case reasoning gap): demoted to prominent mention (1-2 sentences) — formula mapping is diffuse (t₀ invisible for weeks)
- Amazon Kiro (system boundary gap at enterprise scale): prominent mention in "Not Isolated Incidents" section — facts only (13h outage, cascading failures, mandated 80% adoption), no accountability-denial angle (deferred to Article 4 as TODO)

**Pre-LLM vs Post-LLM Framing**
- New opening section before the case studies (3-4 paragraphs)
- Lead with friction-as-pedagogy: Stack Overflow copying had friction — that friction was pedagogical
- Follow with abstraction level shift: pre-LLM gaps were at code level; post-LLM gaps are at design/architecture levels
- Sets the causal frame: LLMs removed the friction AND raised the abstraction level

**Evidence Density & Industry Data**
- "One study per claim" discipline to avoid evidence overload
- Fragile Experts (Prather et al., 77% failure rate) and Sonar verification gap (96% distrust / 48% verify / 42% AI-committed) open the "Not Isolated Incidents" section as lead evidence
- Existing 3 data points (45% security failure, 23.5% incident increase, 4× churn) follow as supporting evidence
- CAST (61B workdays) and Veracode 2026 (82% security debt) move to footnotes
- Amazon Kiro mention also appears in this section

**Formula Annotations**
- Inline sidenotes (blockquote-styled) after each core case study
- Each sidenote maps the case to Ed framework: which layer k, cascade multiplier c_k, when t₀ occurred
- Use LaTeX for formula variables where appropriate
- Positioning as Substack sidenote (visually distinct from body text)
- Rendering approach (LaTeX images vs plain text) at Claude's discretion

### Claude's Discretion
- Formula sidenote rendering approach (LaTeX images vs styled plain text) — should be consistent with Article 2's visual language
- Healthcare mention placement (in Pattern section or Not Isolated Incidents)
- Stochastic Spaghetti Effect (Ngabang) naming and integration — named as a mechanism, not a case study
- Exact section ordering and transitions
- Subtitle update if needed (current: "Three case studies" → may need adjustment for "Two case studies")
- Loading of existing TODOs: Human Debt reservation (one-line footnote vs separate note)

### Deferred Ideas (OUT OF SCOPE)
- Amazon Kiro accountability-denial pattern — Article 4
- Human Debt concept — Article 7 (one-paragraph forward reference only, concept is underdeveloped)
- Ship of Theseus (A5/B5) cross-link — ON HOLD per author decision, do not implement
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| ART3-01 | Existing case studies (SaaStr, AlterSquare, healthcare) polished to publication quality | COMPLETE — article body is at 221 lines with both case studies, formula sidenotes, and healthcare mention fully written |
| ART3-02 | Amazon Kiro incident integrated as fourth case study with accountability-denial pattern | COMPLETE — Kiro appears as prominent mention in "Not Isolated Incidents" with footnote [^3] marking disputed facts |
| ART3-03 | Each case study annotated with formula mapping (which layer k, cascade multiplier c_k, when t₀ occurred) | COMPLETE — both SaaStr and AlterSquare have blockquote formula mapping tables |
| ART3-04 | Industry data block updated with new sources (Fragile Experts 77% failure rate, Sonar verification gap) | COMPLETE — both sources integrated with Sonar citation at sonarsource.com |
| ART3-05 | TODO items resolved (Stochastic Spaghetti naming, pre-LLM vs post-LLM context, CAST/Veracode data) | COMPLETE — all TODOs resolved; Stochastic Spaghetti Effect named in Article 4 (not Article 3) |
| ART3-06 | Social teasers written (LinkedIn, Twitter/X, Instagram, Substack Notes) | COMPLETE — all four platforms have content in YAML front-matter |
| ART3-07 | Article published on Substack with series cross-links updated | PENDING — requires cross-linking (Plan 03) then actual Substack publication |
</phase_requirements>

---

## Summary

Plans 00-02 are complete. Article 3 body is at 221 lines in `topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md` — all case studies, formula sidenotes, industry data, and social teasers are done. ART3-07 is the remaining requirement: publish on Substack with series cross-links updated. Plan 03 implements the cross-linking half of ART3-07.

The cross-linking plan (`.cursor/plans/article_3_cross-linking_8f17d07e.plan.md`) is already fully specified. This addendum documents what the executor needs to know about the target articles' actual content to write accurate, non-cluttering cross-link text.

**Primary recommendation:** Execute Plan 03 as specified. The link text proposed in the cross-linking plan is well-reasoned — implement it with attention to the exact line numbers and the stub vs. draft distinction for reverse links.

---

## Standard Stack

This phase has no software libraries. The "stack" is the editorial and publishing toolchain.

### Core

| Asset | Location | Purpose | Notes |
|-------|----------|---------|-------|
| Article 3 draft | `topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md` | The working document | 221 lines, status: review, social teasers complete |
| Article 2 (published) | `topics/epistemic_debt/artifacts/articles/article-2-a-new-lens.md` | Formula definitions, visual language reference | YAML shows draft/null published_date — verify actual Substack status |
| LaTeX formula reference | `topics/epistemic_debt/artifacts/articles/article-2-latex-formulas.md` | All formula variables for sidenotes | Use for consistent c_k, τ_k, t₀ notation |
| Social teaser template | `templates/social-teasers.md` | Per-platform teaser conventions | Final text goes into YAML social_teasers block |
| Publication rules | `.ai/rules/publication.md` | Platform-specific tone/format conventions | LinkedIn 3-5 hashtags, Twitter hook+insight, etc. |
| Cross-linking plan | `.cursor/plans/article_3_cross-linking_8f17d07e.plan.md` | Full specification for Plan 03 | All A1-A9, B1-B9 links specified with placement guidance |

### Supporting

| Asset | Location | Purpose | When to Use |
|-------|----------|---------|-------------|
| Series plan | `topics/epistemic_debt/assets/0. series-plan.md` | Series arc and inter-article dependencies | Verifying cross-link text and Article 4 bridge line |
| GLOSSARY.md | `/home/arau6/projects/ai-articles/GLOSSARY.md` | Consistent terminology | Check failure taxonomy names before finalizing |

---

## Architecture Patterns

### Established Article Structure (from Articles 1-2)

```
YAML front-matter (title, subtitle, status, social_teasers block)
TODOs block (to be cleared)
# Article Title
*Subtitle line*
---
*Series continuity header: "This is Part X of a 7-part series..."*
---
Opening paragraph(s)
## [Sections...]
## The Pattern (taxonomy summary)
## These Aren't Isolated Incidents (industry data)
## [Closing section]
---
*Next in series bridge line*
---
*Subscribe CTA*
---
**References**
```

### Pattern 1: Formula Sidenote (NEW to Article 3)

**What:** A blockquote-styled callout after each core case study that maps the narrative to the Ed framework. Contains: layer k identification, cascade multiplier c_k order of magnitude, t₀ timing.

**When to use:** After SaaStr case study section and after AlterSquare case study section.

**Format decision (Claude's discretion — recommendation):** Use styled plain text rather than LaTeX images for sidenotes. Article 2 used LaTeX blocks for the formal formulas. Sidenotes are annotations of the narrative, not the formal framework itself — plain text with Unicode symbols (t₀, c_k, τ_k) matches Article 2's inline formula style and avoids Substack LaTeX rendering inconsistencies in blockquote contexts.

**Example structure:**
```markdown
> **Formula mapping — SaaStr**
> Layer: k = L1 (infrastructure/implementation)
> t₀: Day 9 of trial — moment the AI executed production operations
> Cascade multiplier: c₁ ≈ 1× (gap stayed at implementation layer; no architectural rework required — only data recovery)
> The Ed integral accumulated across 9 days at L1, with Cs(t) rising as database permissions expanded and Gc(t) remaining flat. The sudden default corresponds to t₀ arriving before any gap-detection mechanism triggered.
```

### Pattern 2: Pre-LLM vs Post-LLM Opening Section (NEW to Article 3)

**What:** 3-4 paragraphs before the case studies that establish WHY defaults are happening now, not just THAT they happen.

**Structure:**
1. Friction-as-pedagogy paragraph: Stack Overflow copying required integrating the snippet (cognitive work) — that friction was a natural brake
2. Abstraction level shift paragraph: post-LLM gaps are at design/architecture levels, not just snippet level
3. Causal bridge paragraph: LLMs removed friction AND raised the abstraction level simultaneously — this is the mechanism that makes the case studies possible
4. Transition sentence into first case study

**Tone note:** This section should feel like "setting the stage" — explaining WHY before showing WHAT. The exploratory voice applies here: "here's what changed, here's what I think it means."

### Pattern 3: Prominent Mention Format

**What:** 1-2 sentence integration of healthcare (edge case reasoning gap) and Amazon Kiro.

**When to use:** Healthcare — either in "The Pattern" section or "Not Isolated Incidents." Amazon Kiro — in "Not Isolated Incidents" alongside the industry data.

**Kiro mention content:** 13-hour AWS outage, cascading infrastructure failures, company subsequently mandated 80% AI adoption. Present as a system boundary gap at enterprise scale — not as accountability denial (deferred to Article 4).

### Pattern 4: Industry Data Section Restructuring

**Current order in draft:** 45% security failure → 23.5% incident increase → 4× churn

**New order (locked decision):**
1. Fragile Experts (Prather et al.): 77% failure rate, N=78 experimental study — lead position because experimental (not correlational)
2. Sonar verification gap: 96% distrust / 48% verify / 42% AI-committed — second lead because directly measures the gap between concern and action
3. Amazon Kiro mention (1-2 sentences)
4. Existing 3 data points as supporting evidence
5. CAST (61B workdays) and Veracode (82% security debt) → footnotes

### Pattern 5: Stochastic Spaghetti Effect (Named Mechanism)

**What:** Ngabang (2026) term for locally optimized AI-generated code that lacks global architectural coherence. Name it as a mechanism, not a case study.

**Integration point:** "The Pattern" section or a brief mention in the pre-LLM opening. The effect explains why the edge case reasoning gap appears: AI generates L1 code that passes local tests but encodes no L2/L3 coherence.

**NOT:** A full case study. NOT: a new section. One precise sentence that names the mechanism.

### Anti-Patterns to Avoid

- **Reopening structural decisions:** CONTEXT.md decisions are locked — do not reconsider case study selection or restructure the taxonomy
- **Accountability-denial angle for Kiro:** Explicitly deferred to Article 4. Present facts only.
- **LaTeX blocks in sidenotes:** Inconsistent rendering in Substack blockquotes — use Unicode inline variables
- **Human Debt elaboration:** One-line footnote maximum, forward reference to Article 7 only
- **Adding new evidence sources:** "One study per claim" discipline — do not add beyond what CONTEXT.md specifies
- **Prescriptive closing:** Article tone is exploratory — the closing bridge to Article 4 should open a question, not deliver a verdict

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Formula variable notation | Custom notation system | Article 2 LaTeX formulas file + Unicode inline | Consistency with published Article 2 is the constraint |
| Social teaser format | Platform-specific formats from scratch | `templates/social-teasers.md` conventions | Template already captures all platform rules |
| Series cross-link text | New phrasing | Existing pattern from Articles 1-2 headers | Series continuity requires identical format |
| Sidenote visual treatment | Custom HTML/CSS | Substack blockquote (native) | Substack renders blockquotes natively; no custom markup |
| Cross-link placement decisions | Re-derive from scratch | `.cursor/plans/article_3_cross-linking_8f17d07e.plan.md` | Already fully specified with line numbers and rationale |

---

## Common Pitfalls

### Pitfall 1: Subtitle Mismatch After Restructuring

**What goes wrong:** Current subtitle reads "Three case studies and the industry data that says they aren't outliers." After demoting healthcare to a mention and reframing Kiro as a prominent mention, the subtitle no longer accurately describes the article. A reader who counts will notice.

**Why it happens:** Subtitle was written for the original three-case-study structure.

**How to avoid:** Update subtitle to reflect two core case studies. Candidate: "Two case studies, industry data, and the failure taxonomy that says they aren't outliers." Exact wording is Claude's discretion.

**Warning signs:** Subtitle contains the word "three" after editing is complete.

### Pitfall 2: Formula Sidenote Circular Reference

**What goes wrong:** Sidenotes describe t₀ and c_k without being fully grounded in what those terms mean for a reader who hasn't read Article 2 carefully.

**Why it happens:** Article 3 assumes the reader has Article 2 in mind, but the series is also findable without reading sequentially.

**How to avoid:** Each sidenote should contain one plain-language gloss of the key variable it uses. Example: "t₀ — the moment the gap became visible" in the first sidenote; subsequent sidenotes can drop the gloss.

**Warning signs:** Sidenote uses τ_k or c_k with no English equivalent.

### Pitfall 3: Amazon Kiro Scope Creep

**What goes wrong:** The accountability-denial angle (AWS blaming the customer; team dynamics; organizational cover-up) is compelling and easy to slip into the Kiro mention.

**Why it happens:** The incident has a richer narrative than "system boundary gap at enterprise scale."

**How to avoid:** Facts only: 13h outage, cascading failures, mandated 80% adoption. Stop there. The deferred TODO note in the article's TOADD block makes the Article 4 scope explicit — preserve that note.

**Warning signs:** Kiro mention exceeds 3 sentences or includes language about blame/denial/organizational response.

### Pitfall 4: Article 2 Publication Dependency

**What goes wrong:** Article 3's series header links to Article 2 by Substack URL. If Article 2 hasn't been published, that URL is a dead link when Article 3 goes live.

**Why it happens:** Article 2's YAML shows `status: draft` and `published_date: null` but PROJECT.md/STATE.md note it may be published. The discrepancy has not been resolved.

**How to avoid:** The planner must include a verification step before ART3-07 (publish). Options: (a) verify Article 2 Substack URL resolves before scheduling; (b) publish Article 2 first if not yet live; (c) use a placeholder link and update post-publish.

**Warning signs:** Article 3 is scheduled for publishing without confirming `article-2-a-new-lens.md` YAML has a `published_date` value.

### Pitfall 5: Evidence Framing Drift

**What goes wrong:** Fragile Experts and Sonar data are inserted as raw statistics without narrative framing that connects them to the epistemic debt thesis.

**Why it happens:** It's easy to drop data points into a section without writing the connecting sentence that explains why this data confirms the argument.

**How to avoid:** Each data point needs one sentence of interpretation — "This matters because..." or "The pattern here mirrors..." The existing three data points in the draft model this correctly; Fragile Experts and Sonar should follow the same format.

**Warning signs:** A data point paragraph ends with a statistic rather than an interpretive sentence.

### Pitfall 6: Social Teasers Written Before Article Is Stable

**What goes wrong:** Teasers reference content that was later edited out, or don't reflect the final framing.

**Why it happens:** Writing teasers while article is still changing.

**How to avoid:** Write social teasers after the article body is final. ART3-06 should be a task that runs after ART3-01 through ART3-05 are done.

---

## Code Examples

Verified patterns from project files:

### Series Continuity Header (from Article 2)

```markdown
*This is Part 2 of a 7-part series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*
```

Article 3 uses the same structure with "Part 3."

### Bridge Line to Next Article (Article 2 → 3 pattern)

```markdown
*Next in the series: **When Epistemic Debt Defaults** — case studies and industry data that says they aren't outliers.*
```

Article 3's bridge to Article 4 must follow this exact format:

```markdown
*Next in the series: **The Solutioning Trap** — [brief description matching Article 4's thesis].*
```

The existing Article 3 draft closing already has this bridge; verify it matches Article 4's actual title and thesis before finalizing.

### YAML Social Teasers Block (from template)

```yaml
social_teasers:
  linkedin: |
    [Opening hook]

    [1-2 sentences on what the article investigates.]

    [CTA with link]
    #hashtag1 #hashtag2 #hashtag3
  twitter: |
    [One sharp hook. Key insight. link]
  instagram_caption: |
    [Core insight in plain language.]

    Link in bio.
  substack_notes: |
    [Main idea.] [What reader gets.] [Substack URL]
```

### Formula Variable Reference (from `article-2-latex-formulas.md`)

For inline use in sidenotes (Unicode, not LaTeX blocks):
- Epistemic Debt: Ed = ∫[0 to T] (Cs(t) - Gc(t)) dt
- Per layer: Ed = Σ_k ∫[0 to T] (Cs_k(t) - Gc_k(t)) dt
- Recovery time: τ_k = (Cs_k(t₀) - Gc_k(t₀)) / r_k
- Net benefit loss condition: Σ_k c_k · τ_k > δ

For LaTeX blocks (Substack LaTeX renderer, for formal formula sections only):
```
E_d = \int_0^T \left( C_s(t) - G_c(t) \right) dt
```

### Substack Blockquote (sidenote styling)

Substack renders `>` blockquotes as visually distinct pull-quote style. Use:
```markdown
> **Formula mapping**
> [content]
```

No custom HTML needed. This is the correct approach for formula sidenotes.

### Reference List Format (from Article 3 draft, established pattern)

```markdown
- Author (Year). "Title." [URL]
```

New references to add:
- Prather, J. et al. (2026). "Mitigating 'Epistemic Debt' in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts." arXiv. https://arxiv.org/html/2602.20206
- Sonar (year TBC). "[Report title]." [URL — see note below]
- CAST Software (2025). "Coding in the Red." https://www.castsoftware.com/news/companies-worldwide-burdened-with-61-billion-workdays-of-tech-debt (move to footnote)
- Veracode (2026). "2026 State of Software Security." https://www.veracode.com/blog/2026-state-of-software-security-report-risky-security-debt/ (move to footnote)

---

## State of the Art

| Old Approach | Current Approach | Impact |
|--------------|------------------|--------|
| Three case studies (SaaStr + AlterSquare + healthcare as full narratives) | Two core case studies + two prominent mentions | Tighter narrative; two failure modes demonstrated (sudden vs. gradual) rather than three separate stories |
| Industry data after pattern section (correlational data only) | Experimental data (Fragile Experts, Sonar) leads; correlational follows | Stronger argument; experimental evidence validates thesis directly |
| No formula annotations | Inline sidenotes after each core case study | Reader can see the Ed framework applied to real events |
| No pre-LLM framing | New opening section explaining WHY defaults happen now | Causal frame established before evidence presented |
| Stochastic Spaghetti Effect in TODO block | Named in article body as a mechanism | Taxonomy is complete for Articles 4-7 reference |

---

## Open Questions

1. **Sonar verification gap figures — exact source**
   - What we know: CONTEXT.md specifies 96% distrust / 48% verify / 42% AI-committed as the Sonar figures
   - What's unclear: The exact Sonar report title, publication year, and URL are not present in any project file. The draft references list does not include Sonar.
   - Recommendation: The planner should include a task to locate and add the Sonar citation before the article is finalized. The figures are specific enough (three percentages in a defined relationship) that they appear to come from a real report — but the citation needs to be confirmed and added to the references section.

2. **Amazon Kiro exact facts for the "prominent mention"**
   - What we know: CONTEXT.md specifies "13h outage, cascading failures, mandated 80% adoption"
   - What's unclear: These facts are not currently in any project file — not the draft, not the references. No URL or source is cited.
   - Recommendation: The planner should include a task to verify these three specific claims (outage duration, cascade description, adoption mandate percentage) against a primary source and add it to the references list. This is a factual assertion in a published article.

3. **Article 2 publication status**
   - What we know: STATE.md flags this explicitly — "PROJECT.md says published but YAML frontmatter shows draft status and empty published_date"
   - What's unclear: Whether Article 2 is actually live on Substack and what its URL is
   - Recommendation: Make ART3-07 dependent on this check. The planner should treat this as a pre-condition task in Wave 1 or a gate before ART3-07.

4. **Human Debt TODO resolution — footnote vs. note**
   - What we know: CONTEXT.md says "one-line footnote vs separate note" is at Claude's discretion
   - What's unclear: Whether a markdown footnote (`[^1]`) is the right mechanism in Substack, or whether an inline parenthetical is preferable
   - Recommendation: Use an inline parenthetical. Substack's footnote rendering is less reliable than in-body text; a brief parenthetical "(The psychological toll of this dynamic—what some researchers are calling 'Human Debt'—is a thread we'll pick up in the final article.)" integrates cleanly without requiring markdown footnote syntax.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | None — this is a content/editorial phase |
| Config file | N/A |
| Quick run command | Manual review against checklist |
| Full suite command | Manual review against all ART3-XX success criteria |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| ART3-01 | Case studies polished to publication quality | manual | Read article, verify narrative completeness | ✅ Complete |
| ART3-02 | Amazon Kiro integrated (facts only, no accountability angle) | manual | Read "Not Isolated Incidents" section, verify Kiro mention is ≤3 sentences, facts only | ✅ Complete |
| ART3-03 | Formula sidenotes after each core case study | manual | Read article, verify 2 sidenotes present with k, c_k, t₀ fields | ✅ Complete |
| ART3-04 | Fragile Experts (77%) and Sonar (96%/48%/42%) present with citations | manual | Read "Not Isolated Incidents," verify both sources present, cited, with interpretive sentence | ✅ Complete |
| ART3-05 | All TODOs resolved (Stochastic Spaghetti, pre-LLM framing, CAST/Veracode, Fragile Experts block) | manual | Read article — zero TODO markers should remain | ✅ Complete |
| ART3-06 | Social teasers present in YAML front-matter (all 4 platforms) | manual | Read YAML, verify social_teasers block has non-empty values for linkedin, twitter, instagram_caption, substack_notes | ✅ Complete |
| ART3-07 | Article live on Substack with series cross-links updated | manual | Verify Substack URL resolves; check cross-links added per Plan 03 | ❌ Plan 03 pending |

### Sampling Rate

- **Per task commit:** Author reads the edited section for voice/tone consistency and that no deferred scope leaked in
- **Per wave merge:** Full article read-through against success criteria checklist
- **Phase gate:** All ART3-XX criteria met; Article 2 publication status confirmed; cross-links approved at human checkpoint

### Wave 0 Gaps

- [ ] Article 2 publication URL — confirm actual Substack URL before series cross-links can be finalized
- [ ] Article 3 Substack URL — needed for reverse links in stub files and intra-series articles (currently `[ARTICLE_URL]` placeholder)

*(Sonar and Kiro citations are now resolved in the article body — they are no longer Wave 0 gaps.)*

---

## Cross-Linking Research Addendum

*Added 2026-03-15. This section focuses specifically on Plan 03 — bidirectional cross-linking between Article 3 and 9 other articles. Plans 00-02 are complete.*

### Current Article 3 State (Confirmed)

Article 3 is at 221 lines (`topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md`), status: review. The article body is finished. Key anchor points for outbound links:

| Section | Approximate Lines | Cross-link opportunity |
|---------|-------------------|----------------------|
| "What Changed" — friction removal discussion | ~87-99 | A3 (Deleting Code — "regime change" framing) |
| Case 1 — "linguistic plausibility implied operational understanding" | ~109 | A4 (Metaphors — projecting meaning onto AI) |
| Formula mapping tables after each case | ~113-147 | A9 (Governance companion — operationalizes these mappings) |
| "The Pattern" — failure taxonomy summary | ~149-159 | A7 (Article 5 — triangle framework formalizes these positions) |
| "These Aren't Isolated Incidents" — vibe coding mention | ~169 | A1 (Vibe Designing — beyond vibe coding) |
| Sonar data / say-do gap | ~167 | A6 (Article 4 forward-ref — rubber-stamp culture) |
| Code churn / measurement data | ~179-181 | A8 (Article 6 forward-ref — proxy metrics) |
| "The Bill Always Comes Due" closing | ~183-191 | A2 (Eikasia — philosophical lens for epistemic gap) |

### Target Article Content Summary

The cross-topic article stubs (Vibe Designing, Eikasia, Deleting Code, Metaphors) contain only `[GAP]` placeholders — their full text lives on Substack, not in the repo. The cross-linking plan's rationale for each link is drawn from knowledge of the published articles, not from the repo stubs. The executor should trust the rationale in `.cursor/plans/article_3_cross-linking_8f17d07e.plan.md` rather than re-reading the stubs.

The intra-series articles (4, 5, 6, 7, governance companion) are full drafts with actual content:

**Article 4 (The Solutioning Trap)** — Line 140 already contains: "This is the 200-hours-to-2,000-hours pattern from Article 3, generalized across organizations." This is the existing B6 backlink. No changes to Article 4 are needed.

**Article 5 (The Trade-off Triangle)** — The triangle is introduced at line 38. The "Universal Triangle" section (~lines 42-91) discusses Speed/Understanding/Reliability positioning without naming specific examples. The B7 backlink fits naturally in the introduction (~line 38-39) where it says "The patterns described in the previous articles — epistemic debt accumulation, the solutioning trap, boundary failures — share a common structure." Article 3's case studies are those patterns. A brief reference connecting the SaaStr and AlterSquare cases to the Speed corner of the triangle would be natural here.

**Article 6 (Measuring the Unmeasurable)** — The "What We Can Measure Today" section (~lines 69-98) discusses bus factor, onboarding velocity, incident diagnosis time, and code churn. The B8 backlink fits in the code churn discussion (~line 85) or the bus factor discussion (~line 75-78). Article 3's 10:1 ratio and the "bus factor = 0" concept (from Article 4 line 80, which references Article 3's case) make the connection precise.

**Article 7 (Beyond Software: The Universal Framework)** — The "Content Creation" section (~lines 51-63) discusses voice drift as epistemic debt in non-software domains. The failure mode described is "code that looks professional" — directly paralleled in software by Article 3's case studies. The B9 backlink fits in the Content Creation section's domain-specific failure mode paragraph (~line 61-63) or in the "Universal Meta-Patterns" section (~lines 116-151).

**Governance Companion** — The article is mostly `[GAP]` blocks. The introduction section has `[GAP]` markers explaining that the article operationalizes the formula from Article 2 and the triangle from Article 5 into a governance pipeline. The formula mappings in Article 3 (the blockquote sidenotes after each case study) are explicitly the narrative precursor to what the governance companion operationalizes. The B-governance backlink fits in the Introduction `[GAP]` block's narrative, or as a note near the "Measuring What Was Invisible" section (~line 116) which bridges to Article 6's "we can't measure well" framing.

### Substack Rendering Constraints for Cross-Links

Based on confirmed Substack behavior:

**Links render correctly:** Standard markdown `[text](url)` renders as clickable hyperlinks in Substack. Both inline links and footnote-style links work.

**Footnotes:** Substack does render `[^n]` footnotes but the rendering quality varies by reader platform (web vs. email). The cross-linking plan correctly recommends footnotes only for philosophical references (A2 Eikasia, A4 Metaphors) where the connection needs brief explanation. Practical references (A1 Vibe Designing, A3 Deleting Code) should use inline parentheticals.

**Anchor links:** Substack does not support anchor links within an article (e.g., `#section-name`). Cross-links must point to full article URLs, not to sections within articles. All links in the cross-linking plan correctly use full Substack post URLs.

**Unpublished articles:** For Articles 4-7 and the governance companion (all unpublished), use `[ARTICLE_URL]` as the placeholder. This is the established convention in Article 3's YAML front-matter social teasers.

**Link density:** The cross-linking plan targets 5-7 outbound links from Article 3. Article 3 at 221 lines has roughly 8-9 major sections. One link per major section is the natural maximum before it feels cluttered. The plan's guidance to prioritize A1-A4 (published, with real URLs) and include A6-A9 only where they add genuine value is correct.

### Reverse Link Conventions

**Cross-topic stub files** (Vibe Designing, Eikasia, Deleting Code, Metaphors): These files contain only `[GAP]` placeholder sections. They have no existing cross-reference sections. Add a `## Cross-References` section at the end, before the closing CTA line (the *"If you found this article..."* italicized paragraph). The `## Cross-References` heading must come after `## References` but before the CTA.

Confirmed structure of each stub (e.g., `article-2-vibe-designing.md`):
```
# Title
## Abstract [GAP]
## Introduction [GAP]
## Conclusion [GAP]
---
*If you found this article...*   ← CTA line
---
## References [GAP]
```

Insert `## Cross-References` between `## References` and the end of the file, or after the References `[GAP]` line. The CTA line is the last content before the file ends — place `## Cross-References` before it.

**Intra-series drafts** (Articles 5, 6, 7, governance): These have actual content. Insert reverse links inline at the natural anchor points identified above, or as footnotes. Keep to one sentence per reverse link. Match the surrounding text's tone.

### Link Text Quality Criteria

The cross-linking plan proposes specific link text for each connection. The executor should evaluate each proposed text against:

1. **Accuracy to target article**: Does the description match what the target article actually argues? For cross-topic stubs, trust the plan's rationale (drawn from published Substack content). For intra-series drafts, verify against the actual draft content.

2. **Non-interruption**: The link should feel like a natural aside, not a sales pitch for another article. Parenthetical asides ("(explored in depth in [X]([URL]))") or footnotes work better than full sentences dedicated to the link.

3. **Exploratory tone**: Article 3's tone is investigative. Cross-link text should use the same register: "For a closer look at..." or "The philosophical vocabulary for this..." rather than "This is fully explained in..." or "You should read..."

4. **Specificity**: Vague cross-links ("for more on this, see Article X") add noise without value. Specific cross-links name what the reader will find ("the 'velocity trap' framing in [Vibe Designing]") and why it connects to the current point.

### Confirmed Substack URLs for Published Articles

From YAML front-matter (HIGH confidence — verified in repo files):

| Article | Substack URL |
|---------|-------------|
| Vibe Designing (A1) | `https://antoninorau.substack.com/p/from-vibe-coding-to-vibe-designing` |
| Eikasia to Noesis (A2) | `https://antoninorau.substack.com/p/from-eikasia-to-noesis-what-plato` |
| Deleting Code (A3) | `https://antoninorau.substack.com/p/ai-changed-how-i-delete-codeand-that` |
| AI Metaphors (A4) | `https://antoninorau.substack.com/p/ai-models-and-meta-metaphors` |
| Articles 4-7, Governance | `[ARTICLE_URL]` placeholder |

### Cross-Link Implementation Checklist

For the executor of Plan 03:

**Outbound links from Article 3 (A1-A4, A6-A9):**
- [ ] A1 (Vibe Designing): inline parenthetical near "vibe coding debate" mention (~line 169)
- [ ] A2 (Eikasia): footnote in "The Bill Always Comes Due" closing (~lines 183-191)
- [ ] A3 (Deleting Code): inline parenthetical in "What Changed" section (~lines 87-99)
- [ ] A4 (Metaphors): footnote near "linguistic plausibility implied operational understanding" (~line 109)
- [ ] A6 (Article 4 forward-ref): brief mention near Sonar survey data (~line 167) about rubber-stamp culture
- [ ] A7 (Article 5 forward-ref): brief mention in conclusion (~lines 185-191) about trade-off triangle
- [ ] A8 (Article 6 forward-ref): brief mention near code churn data (~line 179-181) about measurement proxies
- [ ] A9 (Governance companion): brief mention near formula mapping tables (~lines 113-147)
- [ ] Ship of Theseus: EXCLUDED — do not add

**Reverse links in cross-topic stubs (B1-B4):**
- [ ] B1 (Vibe Designing stub): `## Cross-References` section with Article 3 link and 10:1 ratio connection
- [ ] B2 (Eikasia stub): `## Cross-References` section with Article 3 link and 77% failure rate connection
- [ ] B3 (Deleting Code stub): `## Cross-References` section with Article 3 link and "surface deceptions at scale" connection
- [ ] B4 (Metaphors stub): `## Cross-References` section with Article 3 link and database deletion projection-mechanism connection
- [ ] Ship of Theseus: EXCLUDED — do not add

**Reverse links in intra-series drafts (B7-B9, B-governance):**
- [ ] B6 (Article 4): ALREADY EXISTS at line 140 — no changes needed
- [ ] B7 (Article 5): one sentence in introduction or "Universal Triangle" section connecting SaaStr/AlterSquare cases to Speed corner positioning
- [ ] B8 (Article 6): one sentence in bus factor or code churn discussion connecting 10:1 ratio / bus factor = 0 to proxy metrics
- [ ] B9 (Article 7): one sentence in Content Creation or Universal Meta-Patterns section connecting "code that looks professional" to software-domain epistemic debt
- [ ] B-governance: one sentence in Introduction or "Measuring What Was Invisible" section connecting Article 3 formula sidenotes to governance operationalization

---

## Sources

### Primary (HIGH confidence)

- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md` — Article 3 at 221 lines, current state confirmed
- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-4-the-solutioning-trap.md` — confirmed B6 backlink at line 140
- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-5-the-trade-off-triangle.md` — draft content, B7 anchor points identified
- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-6-measuring-the-unmeasurable.md` — draft content, B8 anchor points identified
- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-7-beyond-software.md` — draft content, B9 anchor points identified
- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-sdd-epistemic-governance.md` — mostly GAP blocks, B-governance placement identified
- `/home/arau6/projects/ai-articles/.cursor/plans/article_3_cross-linking_8f17d07e.plan.md` — full cross-linking specification, confirmed complete
- YAML front-matter of all four cross-topic stub files — Substack URLs confirmed

### Secondary (MEDIUM confidence)

- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-2-a-new-lens.md` — Ed formula definitions, visual language, established series patterns
- `/home/arau6/projects/ai-articles/topics/epistemic_debt/artifacts/articles/article-2-latex-formulas.md` — all formula variables in LaTeX and Unicode
- `/home/arau6/projects/ai-articles/.planning/phases/13-article-3-when-epistemic-debt-defaults/13-CONTEXT.md` — all locked decisions

### Tertiary (LOW confidence — needs verification before publication)

- Article 3 Substack URL — not yet published; needed for reverse links that reference it
- Article 2 Substack URL — YAML shows draft status; needs human verification before Article 3 can go live

---

## Metadata

**Confidence breakdown:**
- Article body (Plans 00-02): HIGH — all edits confirmed complete in article review
- Cross-link specification: HIGH — fully documented in `.cursor/plans/article_3_cross-linking_8f17d07e.plan.md`
- Target article content (intra-series): HIGH — read directly from draft files
- Target article content (cross-topic stubs): MEDIUM — stubs contain only GAP placeholders; rationale draws on plan author's knowledge of published Substack content
- Substack rendering behavior: MEDIUM — based on established Substack markdown conventions; no project-specific verification
- Article 3 Substack URL: LOW — article not yet published at time of this research

**Research date:** 2026-03-14 (original); 2026-03-15 (cross-linking addendum)
**Valid until:** 2026-04-14 (stable editorial domain; cross-linking addendum valid until Article 3 is published)
