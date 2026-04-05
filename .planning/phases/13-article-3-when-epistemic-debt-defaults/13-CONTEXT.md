# Phase 13: Article 3 — When Epistemic Debt Defaults - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning

<domain>
## Phase Boundary

Polish and publish the evidence article that establishes the failure taxonomy (system boundary gap, defensive coding gap, edge case reasoning gap, Stochastic Spaghetti Effect) for the rest of the series. Two fully-developed case studies with formula annotations, two prominent mentions, updated industry data with new experimental evidence, and social teasers. The existing draft (148 lines) is the starting point — this is targeted integration, not open-ended writing.

</domain>

<decisions>
## Implementation Decisions

### Case Study Selection & Structure
- **2 core case studies** as fully-developed narratives: SaaStr (system boundary gap) + AlterSquare (defensive coding gap)
- SaaStr chosen for crispest t₀ (day 9), clearest single k layer (L1 infrastructure), most vivid cascade (deletion → cover-up → discovery) — demonstrates **sudden default**
- AlterSquare chosen for best compound accumulation story (200h → 2000h = the Ed integral in action) — demonstrates **gradual accumulation with interest**
- **Healthcare** (edge case reasoning gap): demoted to prominent mention (1-2 sentences) — formula mapping is diffuse (t₀ invisible for weeks)
- **Amazon Kiro** (system boundary gap at enterprise scale): prominent mention in "Not Isolated Incidents" section — facts only (13h outage, cascading failures, mandated 80% adoption), no accountability-denial angle (deferred to Article 4 as TODO)

### Pre-LLM vs Post-LLM Framing
- **New opening section** before the case studies (3-4 paragraphs)
- Lead with **friction-as-pedagogy**: Stack Overflow copying had friction (integrating, cognitive dissonance, removing irrelevant parts) — that friction was pedagogical
- Follow with **abstraction level shift**: pre-LLM gaps were at code level (a function, a snippet); post-LLM gaps are at design/architecture levels (entire modules and relationships)
- Sets the causal frame: LLMs removed the friction AND raised the abstraction level → case studies land as evidence of what happens when friction disappears

### Evidence Density & Industry Data
- **"One study per claim" discipline** to avoid evidence overload (pitfall #3 from research)
- **Fragile Experts (Prather et al., 77% failure rate)** and **Sonar verification gap (96% distrust / 48% verify / 42% AI-committed)** open the "Not Isolated Incidents" section as lead evidence — strongest because experimental, not correlational
- **Existing 3 data points** (45% security failure, 23.5% incident increase, 4× churn) follow as supporting evidence
- **CAST (61B workdays)** and **Veracode 2026 (82% security debt)** move to footnotes
- Amazon Kiro mention also appears in this section

### Formula Annotations
- **Inline sidenotes** (blockquote-styled) after each core case study
- Each sidenote maps the case to Ed framework: which layer k, cascade multiplier c_k, when t₀ occurred
- Use LaTeX for formula variables where appropriate
- Positioning as Substack sidenote (visually distinct from body text)
- Rendering approach (LaTeX images vs plain text) at Claude's discretion — should be consistent with Article 2's visual language

### Claude's Discretion
- Formula sidenote rendering approach (LaTeX images vs styled plain text)
- Healthcare mention placement (in Pattern section or Not Isolated Incidents)
- Stochastic Spaghetti Effect (Ngabang) naming and integration — named as a mechanism, not a case study
- Exact section ordering and transitions
- Subtitle update if needed (current: "Three case studies" → may need adjustment for "Two case studies")
- Loading of existing TODOs: Human Debt reservation (one-line footnote vs separate note)

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `article-3-when-debt-defaults.md`: 148-line draft with 3 fully-written case studies, industry data section, and closing — foundation for all edits
- `article-2-latex-formulas.md`: LaTeX formula reference from Article 2 — use for consistent formula rendering approach
- `article-2-a-new-lens.md`: Published Article 2 — Ed formula definition, t₀, c_k, abstraction layers are defined here; Article 3 back-references these

### Established Patterns
- Series continuity header: `*This is Part X of a 7-part series on [epistemic debt...]*` — already in draft
- YAML front matter with complete metadata — already in draft
- Reference list format: `- Source (Year). "Title." [URL]` — established in Articles 1-2
- Exploratory tone: "here's what I've found worth examining" — not prescriptive

### Integration Points
- Article 2's closing line bridges to Article 3: "what happens when you can't pay it back?"
- Article 3's closing must bridge to Article 4: "how do teams fall into this pattern?"
- Failure taxonomy (system boundary gap, defensive coding gap, edge case reasoning gap) is referenced by name in Articles 4-7
- Amazon Kiro accountability-denial pattern → deferred as TODO for Article 4

</code_context>

<specifics>
## Specific Ideas

- The two core case studies were selected specifically because they demonstrate the two modes of the Ed formula: sudden default (SaaStr, crisp t₀) and compound accumulation (AlterSquare, the integral in action)
- Pre-LLM section should feel like "setting the stage" — explaining WHY defaults are happening NOW, not just showing that they happen
- Fragile Experts study is the most important new evidence: it's experimental (not correlational), directly measures epistemic debt (77% failure when scaffold removed), and validates the series' core thesis
- User wants the formula annotations to feel like sidenotes — visually present but not interrupting the narrative flow

</specifics>

<deferred>
## Deferred Ideas

- Amazon Kiro accountability-denial pattern — Article 4 (organizational dynamics of denying AI-caused failures)
- Human Debt concept — Article 7 (one-paragraph forward reference only, concept is underdeveloped)

</deferred>

---

*Phase: 13-article-3-when-epistemic-debt-defaults*
*Context gathered: 2026-03-14*
