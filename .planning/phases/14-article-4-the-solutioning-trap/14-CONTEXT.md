# Phase 14: Article 4 — The Solutioning Trap - Context

**Gathered:** 2026-04-12
**Revised:** 2026-04-12 (practical pivot)
**Status:** Ready for planning

<domain>
## Phase Boundary

Rewrite Article 4 as a **practical, tool-anchored** piece on the solutioning trap. The article introduces two concrete defensive prompt macros (`<asin>`, `<soltree>`) hosted in the pmacros tool, which the reader can use immediately. The cognitive-bias discussion is compressed into a brief psychological justification for why these macros are needed — it is no longer the center of gravity. The existing 2607-word draft is a starting point for tone and some sections only; structure and emphasis change substantially. The Anthropic RCT, SDLC boundaries, r_k degradation, and social invisibility threads are relaxed or moved to Article 5 so this article can be concrete and actionable.

**pmacros dependency:** Decoupled. Article references pmacros and describes the two macros as designed. Shipping pmacros publicly is coordinated separately outside the ai-articles repo and does not block this phase.

</domain>

<decisions>
## Implementation Decisions

### Article Orientation

- **D-01:** Article 4 is **practical-first**. Structure: (1) short problem framing — the solutioning trap; (2) brief psychological justification (why it happens) — ~15-20% of article length, not more; (3) concrete defensive practices anchored in the two pmacros default macros; (4) how to use them, example prompts, expected behavior; (5) bridge to Article 5.
- **D-02:** The cognitive-bias section is **compressed to a single short section**. It cites automation bias and 1-2 supporting mechanisms as justification for why the defensive macros are needed. No deep mechanism exposition, no multiple studies, no long TODO resolutions.
- **D-03:** The existing draft (`article-4-the-solutioning-trap.md`, 2607 words) is a **voice/tone reference**. Rate limiter example, rubber-stamp culture section, and junior dev crisis section may be reused in compressed form or cut entirely at the planner's discretion. The SDLC boundary sections are removed from this article (moved to Article 5).

### pmacros Integration — The Center of Gravity

- **D-04:** pmacros is introduced as **the vehicle** for the two default macros. The article explains what pmacros is in 1-2 paragraphs (a Claude Code UserPromptSubmit hook that expands `<tagname>` tags into longer prompt text) and links to the pmacros PROJECT.md and/or public repo if available at publish time.
- **D-05:** The article should position pmacros as "one concrete way I am operationalizing these defenses" — **not as a product pitch**. Author voice stays exploratory; the reader is invited to use, adapt, or ignore pmacros. The anti-patterns and the macro prompt bodies are valuable even without pmacros installed.
- **D-06:** Two default macros are the practical payload:

  **`<asin>`** — assumption + intent surfacing. Expands to a prompt that asks the LLM to list, as separate explicit categories BEFORE answering:
  1. The LLM's own assumptions (from its training knowledge and defaults)
  2. Assumptions the LLM inferred from the user's prompt
  3. Gaps — what is missing, unknown, or underspecified
  4. The user's intent as the LLM understands it
  The goal is to force the model to externalize what it is about to silently assume, so the user can correct course before the model commits to a solution path. Planner and researcher to refine the exact wording; D-06 locks the four categories and their order.

  **`<soltree>`** — solution tree exploration. Expands to a prompt that asks the LLM, before implementing, to surface **unexplored alternative paths** from the problem root. It does **not** require an exhaustive tree. It surfaces 2-4 plausible alternatives the model would not have offered by default, names their tradeoffs briefly, and **asks the user to pick one** before proceeding. The macro is explicitly interactive — the model must stop and wait. Planner and researcher to refine wording; D-06 locks the interactive + non-exhaustive behavior and the "surface unexplored paths and ask the user to pick" contract.

- **D-07:** Macro names are locked: `<asin>` and `<soltree>`. Short, lowercase, memorable.
- **D-08:** The article shows **at least one worked example per macro** — a realistic prompt, what the macro injects, what the model output looks like after expansion, and how it changes the interaction. Planner decides whether examples are real (captured from actual use) or constructed; fact-check gate (Plan 00) determines which is appropriate.

### Draft Treatment

- **D-09:** The current 2607-word draft is treated as a quarry, not a template. Sections can be fully rewritten, cut, or reordered. Word count target is **≤1800 words** for the practical reorientation.
- **D-10:** Series continuity elements that MUST survive: (a) "Part 4 of 7" header, (b) back-reference to Article 3's failure taxonomy by name, (c) bridge to Article 5 at the close.

### Claude's Discretion

- Exact wording of the two macro bodies — planner drafts based on research, user reviews during execution
- Whether and how to reuse the rate limiter example (kept / compressed / cut)
- Whether to include 1-2 sentences on "rubber-stamp culture" or cut entirely
- Exact pmacros introduction length (1-3 paragraphs)
- Which 1-2 cognitive-bias mechanisms to cite in the short justification section
- Whether the worked examples are real captures or constructed illustrations
- Structure of the bridge to Article 5

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Article Draft
- `topics/epistemic_debt/artifacts/articles/article-4-the-solutioning-trap.md` — Existing draft (2607 words); voice/tone reference only, structure is open (D-03, D-09)

### pmacros Tool (external project)
- `/home/arau6/projects/pmacros/.planning/PROJECT.md` — pmacros design doc: what it is, how injection works, scopes, tag format, decisions. Article 4 uses this as the authoritative source on what pmacros does.

### Series Context
- `topics/epistemic_debt/artifacts/articles/article-2-a-new-lens.md` — Article 2 (published): Ed formula, t₀, c_k, abstraction layers. Article 4 back-references these briefly.
- `topics/epistemic_debt/artifacts/articles/article-3-when-debt-defaults.md` — Article 3 (published): failure taxonomy (system boundary gap, defensive coding gap, edge case reasoning gap, Stochastic Spaghetti Effect) — Article 4 references these by name in the problem framing.

### Prior Phase Context
- `.planning/phases/13-article-3-when-epistemic-debt-defaults/13-CONTEXT.md` — Phase 13 decisions

### Project Rules
- `.ai/rules/fact-checking.md` — Fact-check gate: Plan 00 must be a fact-check; no article moves to published without completed report
- `.ai/rules/writing-style.md` — Tone, structure conventions, no em-dashes in prose
- `.ai/rules/publication.md` — Social teaser conventions per platform

### Requirements
- `.planning/REQUIREMENTS.md` §ART4 — **Being rewritten in this phase** (see <requirements_changes> below). The original ART4-01..08 are being relaxed to reflect the practical pivot.

</canonical_refs>

<requirements_changes>
## Proposed Changes to REQUIREMENTS.md §ART4

The original ART4-01..08 required the article to be an academic-weight exposition of automation bias, Anthropic RCT, r_k degradation, and SDLC boundaries. The practical pivot relaxes these. Proposed rewrite:

**Keep (relaxed):**
- **ART4-01** (rewritten): "Solutioning trap problem framed in ≤400 words, references Article 3's failure taxonomy by name"
- **ART4-03** (rewritten): "Solutioning trap briefly framed as a t₀-delaying mechanism (1-2 sentences, not a section)"
- **ART4-07**: Social teasers — unchanged
- **ART4-08**: Article published on Substack — unchanged

**Dropped or moved to Article 5:**
- **ART4-02** (dropped from Article 4): Anthropic RCT 17% data — no longer required as backbone. May be mentioned in the short bias-justification section if the planner judges it adds value within the ≤1800 word budget.
- **ART4-04** (moved to Article 5): r_k degradation + junior dev crisis connection — belongs to the trade-off triangle article.
- **ART4-05** (dropped from Article 4): SDLC boundaries conceptual introduction — moved entirely to Article 5.
- **ART4-06** (dropped): TODO items around social invisibility and t₀ connection — deferred; not required for practical pivot.

**New requirements (added):**
- **ART4-09**: Article introduces pmacros as a concrete Claude Code tool (1-3 paragraphs) with link to PROJECT.md
- **ART4-10**: `<asin>` macro documented — purpose, the four categories it surfaces (LLM assumptions, prompt-derived assumptions, gaps, user intent), worked example
- **ART4-11**: `<soltree>` macro documented — purpose, the surface-unexplored-paths-and-ask-user behavior, worked example
- **ART4-12**: Article grounded in concrete usage (at least one worked example per macro)
- **ART4-13**: Word count ≤ 1800 words
- **ART4-14**: Cognitive-bias section compressed to ≤20% of total length, frames bias as justification for the macros, not as primary subject

The planner should update REQUIREMENTS.md §ART4 in Plan 00 or Plan 01 to match this list.

</requirements_changes>

<specifics>
## Specific Ideas

- The trade-off reframe (bias as "cost-side disappearance") is preserved but compressed — it becomes the 1-paragraph justification for why `<asin>` and `<soltree>` are worth the friction they add.
- `<asin>` is the defense against the **first failure mode** of the solutioning trap: the LLM silently baking in wrong assumptions and wrong intent, then building on top. It externalizes the hidden contract before work begins.
- `<soltree>` is the defense against the **second failure mode**: collapsing to the first plausible solution and never revealing that alternatives existed. It preserves optionality at the decision point rather than after the code is written.
- These two failure modes map cleanly to two moments in the interaction: (a) before the model interprets the problem, (b) before the model commits to a path. The article can use this two-moment framing as its backbone.
- pmacros's status line integration and scoping (user vs project) make the macros a low-friction habit — this is part of why the article can credibly call them "defensive practices you can adopt today."

</specifics>

<deferred>
## Deferred Ideas

- Extended discussion of automation bias mechanisms (processing fluency, cognitive offloading, diffusion of responsibility, effort asymmetry) — deferred; brief mention only
- Anthropic RCT deep dive — deferred; optional light citation
- SDLC boundaries as conceptual introduction — moved to Article 5
- r_k degradation + junior dev crisis — moved to Article 5
- Social invisibility of epistemic debt — deferred entirely
- Amazon Kiro accountability-denial angle — deferred (was already deferred from Phase 13)
- Rate limiter example — at planner's discretion whether to retain in compressed form
- Rubber-stamp culture discussion — at planner's discretion whether to retain in 1-2 sentences or cut

</deferred>

---

*Phase: 14-article-4-the-solutioning-trap*
*Context gathered: 2026-04-12; revised same day for practical pivot*
