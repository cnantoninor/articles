# Phase 14: Article 4 — The Solutioning Trap - Context

**Gathered:** 2026-04-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Polish and publish Article 4 (The Solutioning Trap). The existing draft (2607 words) is a starting point and a reference — it is NOT treated as definitive. The phase integrates the Anthropic RCT as quantitative backbone, resolves two TODO blocks, adds social invisibility and t₀-SDLC connections, and ships with social teasers. The article introduces exactly two SDLC boundaries; Boundary 3 belongs to Article 5.

</domain>

<decisions>
## Implementation Decisions

### Automation Bias Section — Core Reframe

- **D-01:** The automation bias section must be reframed around the **trade-off lens**: the engineer is making a rationally economical choice (fast delivery now, understanding later). Automation bias is the mechanism that makes this trade-off feel consequence-free — it hides the cost side, not the choice itself. This is not a cognitive failure framing; it is a structural incentive framing.
- **D-02:** Pick 2-3 cognitive mechanisms from the TODO list that specifically explain **why the future cost stays invisible** — not just why review is skipped. Claude has discretion on which mechanisms best serve this narrative (candidates: processing fluency, cognitive offloading, diffusion of responsibility, effort asymmetry).
- **D-03:** Mechanism selection and exact structure to be resolved during planning and research. The researcher should investigate which 2-3 mechanisms have the strongest evidence and most direct causal link to cost-side invisibility.

### Draft Treatment

- **D-04:** The current draft is a reference, not a constraint. The planner and researcher should approach the article structure with fresh eyes. Sections, ordering, and emphasis are all open.

### Claude's Discretion

- Exact mechanisms selected (2-3 from the TODO list) — researcher to recommend based on evidence quality
- Section structure and ordering
- Length management: current draft is 33% over target (2607 vs 1952 words); cuts vs. accepts at Claude's discretion given the trade-off framing decisions
- Social invisibility placement: TODO exists in SDLC section; planner decides whether it fits better there, in automation bias, or woven throughout
- Amazon Kiro accountability-denial angle: was deferred from Phase 13 but not in ART4 requirements; planner decides whether to include in rubber-stamp culture discussion or defer further
- t₀-SDLC boundary connection: how explicitly to connect each boundary to t₀ as a debt-surfacing mechanism

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Article Draft
- `topics/epistemic_debt/artifacts/articles/article-4-the-solutioning-trap.md` — Existing draft (2607 words); reference only, not definitive — see D-04

### Series Context
- `topics/epistemic_debt/artifacts/articles/article-2-a-new-lens.md` — Article 2 (published): Ed formula, t₀, c_k, abstraction layers defined here; Article 4 back-references these
- `topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md` — Article 3 (published): failure taxonomy (system boundary gap, defensive coding gap, edge case reasoning gap, Stochastic Spaghetti Effect) that Article 4 references by name

### Prior Phase Context
- `.planning/phases/13-article-3-when-epistemic-debt-defaults/13-CONTEXT.md` — Phase 13 decisions, including the deferred Amazon Kiro accountability-denial angle

### Project Rules
- `.ai/rules/fact-checking.md` — Fact-check gate: Plan 00 must be a fact-check; no article moves to published without completed report
- `.ai/rules/writing-style.md` — Tone, structure conventions, no em-dashes in prose
- `.ai/rules/publication.md` — Social teaser conventions per platform

### Requirements
- `.planning/REQUIREMENTS.md` §ART4 — ART4-01 through ART4-08: specific integration requirements including Anthropic RCT (ART4-02), r_k degradation connection (ART4-04), SDLC boundaries as conceptual intro (ART4-05), social invisibility TODO (ART4-06)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `topics/epistemic_debt/artifacts/articles/article-4-the-solutioning-trap.md`: 2607-word draft — rate limiter example, rubber-stamp culture section, junior dev crisis section, and two SDLC boundary sections are all present; automation bias section has large TODO block (lines 73-85) and SDLC section has TODO block (lines 105-109)
- `article-2-latex-formulas.md`: LaTeX formula reference — use for consistent rendering of Ed, t₀, c_k, r_k, ε_k

### Established Patterns
- Series continuity header: `*This is Part 4 of a 7-part series on [epistemic debt...]*`
- YAML front matter with complete metadata
- Reference list format: `- Author (Year). "Title." [URL]`
- Exploratory tone: "here's what I've found worth examining" — not prescriptive
- One study per claim discipline (established in Phase 13)

### Integration Points
- Article 3's closing bridges to Article 4: "how do teams fall into this pattern?"
- Article 4's closing must bridge to Article 5: "what do we do about it?" (already present in draft)
- Failure taxonomy names (system boundary gap, etc.) must appear by name — referenced from Article 3

</code_context>

<specifics>
## Specific Ideas

- The trade-off reframe is the key architectural decision: automation bias as "cost-side disappearance" rather than "cognitive weakness." This shifts tone from blame to structural analysis, consistent with the series' exploratory posture.
- The Anthropic RCT (17% comprehension gap, debugging gap) is designated as the quantitative backbone — it should anchor the junior dev crisis section's argument, not be a data point in a list.
- The TODO in the SDLC section notes three structural differences between technical debt and epistemic debt (social dynamics, localization, when it manifests) — this is the "social invisibility" angle. Its placement relative to the trade-off framing is open.

</specifics>

<deferred>
## Deferred Ideas

- Detailed mechanism selection (2-3 from 6) — deferred to research phase; researcher to recommend based on evidence quality and causal link to cost-side invisibility
- Amazon Kiro accountability-denial angle — was deferred from Phase 13; not in ART4 requirements; planner to decide inclusion vs. further deferral
- Length management decisions — deferred to planning; planner has discretion to cut sections or accept longer article

### Reviewed Todos (not folded)
- "Remove healthcare case study references from article-0 and series plan" — reviewed but not folded; this is cross-article cleanup, not scoped to Article 4 polish

</deferred>

---

*Phase: 14-article-4-the-solutioning-trap*
*Context gathered: 2026-04-12*
