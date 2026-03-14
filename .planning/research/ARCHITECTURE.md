# Architecture Research

**Domain:** Long-form Substack article series (content architecture, not software architecture)
**Researched:** 2026-03-14
**Confidence:** HIGH — based on direct reading of all seven draft articles, the series plan, published articles 1-2, and prior research files

---

## System Overview

This is a content architecture document, not a software architecture document. The "system" is a 7-part Substack article series where articles 3-7 must integrate with the already-published foundation (articles 0-2) and with each other. The architecture question is: how do the content components fit together, what dependencies exist between them, and in what order should they be built?

```
┌─────────────────────────────────────────────────────────────────┐
│                     PUBLISHED (immutable)                        │
├──────────────────────┬──────────────────────────────────────────┤
│  Article 0           │  Series overview, links to all articles  │
│  Article 1           │  Core concept: epistemic shift, Epistemia│
│  Article 2           │  Formula (Ed integral), tech debt table, │
│                      │  recovery model, t₀, break-even          │
└──────────────────────┴──────────────────────────────────────────┘
              │ All downstream articles inherit these
              │ definitions — changing them is NOT possible
              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     TO BUILD (articles 3-7)                      │
├──────────────────┬──────────────────────────────────────────────┤
│  Article 3       │  Evidence (case studies + industry data)      │
│  Article 4       │  Mechanisms (vibe coding, automation bias,    │
│                  │  SDLC boundaries 1 & 2)                       │
│  Article 5       │  Framework (triangle, SDLC boundary 3,       │
│                  │  strategy forces, IRIS-2, positioning)        │
│  Article 6       │  Measurement (proxies, honest caveats)        │
│  Article 7       │  Generalization (beyond software, capstone)   │
└──────────────────┴──────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Status |
|-----------|----------------|--------|
| Article 0 | Series hub — links to all articles, entry point for new readers | Published |
| Article 1 | Concept introduction — epistemic shift, construction vs. curation, Epistemia | Published |
| Article 2 | Formal foundation — Ed integral, recovery formula, technical debt comparison, t₀ | Draft (published per PROJECT.md) |
| Article 3 | Evidence layer — makes abstract concept visceral through case studies and data | Draft, needs TODO integration |
| Article 4 | Mechanism layer — explains *how* debt accumulates (psychology + SDLC boundaries 1-2) | Draft, needs TODO integration |
| Article 5 | Framework layer — the triangle, boundary 3 (circular validation), strategy forces, IRIS-2 | Draft, needs TODO integration |
| Article 6 | Measurement layer — proxy indicators, honest caveat about what we cannot know | Draft, needs TODO integration |
| Article 7 | Capstone — generalizes triangle beyond software, closes series | Draft, near-complete |

---

## Recommended Build Order

### Dependency Analysis

The articles form a chain of conceptual dependencies. Each article requires the prior one's concepts to be stable before it can be finalized. However, they can be *drafted* and *polished* in a looser order because draft content already exists for all five articles. The constraint is publication order on Substack, not writing order.

**Concept dependency chain:**

```
Art 3: "what happens when debt defaults"
    └── requires Art 1 (epistemic debt defined) + Art 2 (formula)
        └── STABLE — both published

Art 4: "why debt accumulates"
    └── requires Art 3's case studies for back-references ("the 200-to-2000 pattern")
        └── SOFT dependency — can finalize Art 4 before Art 3 publishes

Art 5: "what to do about it"
    └── requires Art 4's SDLC boundaries 1 & 2 to set up boundary 3
    └── requires Art 2's t₀ / break-even formula (connects strategy forces to math)
        └── HARD dependency — boundary 3 is the third of three SDLC boundaries intro'd in Art 4

Art 6: "can we measure it"
    └── requires Art 5's triangle vocabulary (upper/lower triangle positioning)
    └── references Art 2's Ed formula in the measurement paradox
        └── SOFT dependency — concept-level, not structural

Art 7: "beyond software"
    └── requires Art 5's triangle (generalizes it)
    └── closes the whole series — must come last
        └── HARD dependency — is the capstone
```

**Recommended build order:**

```
Phase 1: Article 3 (foundation for 4's back-references)
Phase 2: Article 4 (sets up SDLC boundary 3 for Art 5)
Phase 3: Article 5 (the bookmark article — deepest, most complex)
Phase 4: Article 6 (short, honest, uses Art 5 vocabulary)
Phase 5: Article 7 (capstone — requires all prior articles stable)
```

This matches the publication order (Art 3 → 4 → 5 → 6 → 7), which is not a coincidence: the narrative arc was designed so each article is a prerequisite for the next.

### Why Not Reorder?

Article 5 is tempting to tackle first because it contains the central framework. However, Article 4 introduces SDLC boundaries 1 and 2 — the dashboard vibe-coding scenario and the email validation regex — and Article 5 only works if readers have seen those two boundaries. Boundary 3 (circular validation) is explicitly called out in Article 5 as "the third SDLC boundary from Article 4." Reordering would require restructuring that dependency.

Article 7 must come last: it explicitly says "For six articles, we've explored epistemic debt through a software engineering lens" and closes by referencing the whole series. It cannot be finalized until all other articles are locked.

---

## Content Flow: How Themes Thread Across Articles

### Recurring Theme 1: Circular Validation

The circular validation trap is the series' most important recurring mechanism. It is introduced, extended, and resolved across five articles.

```
Art 2  → introduces "Circular Confirmation Trap" and "Verification Opacity" (Ngabang)
          as a risk with AI-generated tests — PLANTED

Art 4  → Boundary 2 (Spec → Impl) surfaces the stochastic spaghetti effect;
          the TODO about connecting boundaries to t₀ concept seeds the setup
          for Art 5

Art 5  → Boundary 3 (Impl → Validation) gives circular validation its full
          treatment: named, illustrated with Python code example, diagnosed,
          detected — RESOLVED as a named pattern with counter-practice

Art 6  → Triangulation section implicitly relies on it: "LLM-generated tests
          may provide false confidence" — circular validation explains why
          coverage metrics are insufficient

Art 7  → Circular validation appears in each domain as the universal failure
          mode: voice drift in content, benchmark overfitting in LLM-as-judge,
          citation concentration in research — GENERALIZED
```

**Cross-reference management:** Article 5 should explicitly name Art 2's "Circular Confirmation Trap" terminology when introducing Boundary 3, to close the planted reference. Current draft calls it "circular validation" without explicitly linking back. A single sentence resolves this.

### Recurring Theme 2: The t₀ / Break-Even Formula

Article 2 introduced t₀ (the moment debt is recognized) and the break-even condition Σ_k c_k · τ_k < δ. Articles 4 and 5 both contain TODOs asking to connect content back to this formula. These are high-priority because they close the mathematical arc the series opened.

```
Art 2  → t₀ defined, break-even formula introduced, deterministic mechanisms
          listed (E2E tests, fitness functions, integration tests, DDD) — PLANTED

Art 4  → TODO: "Connect translation boundaries to t₀ concept — each boundary
          is a potential t₀" — needs execution

Art 5  → TODO: "Connect each strategy force back to t₀ and break-even formula"
          — needs execution; also TODO on tolerance factor ε_k that closes the
          "partial understanding" seed planted in Art 2

Art 6  → Formula appears implicitly (the measurement paradox section mentions
          Gc(t₀) and Cs(t₀) conceptually); no explicit t₀ reference needed

Art 7  → Formula not needed; generalization works without the math
```

**Cross-reference management:** The Art 4 and Art 5 TODOs should be resolved when those articles are polished. The ε_k tolerance factor TODO in Art 5 is particularly important — Art 2 explicitly planted a seed ("some areas tolerate partial understanding... we'll return to this") that Art 5 must fulfill.

### Recurring Theme 3: IRIS-2 Case Study

IRIS-2 is the series' only named concrete project example. It appears only in Article 5, which is correct — it is the proof-of-concept for the framework. Articles 3, 4, 6, and 7 use composite or anonymized scenarios; only Art 5 uses a named internal case.

**No cross-reference needed** — IRIS-2 is self-contained in Art 5. Other articles should not reference it to avoid creating a dependency on Art 5 vocabulary in earlier articles.

### Recurring Theme 4: The Narrative Arc (Diagnosis → Solution → Honest Caveat → Generalization)

The series has a deliberate four-stage arc that must be preserved:

```
Stage 1 (Art 1-2): What it is and why it matters (diagnosis)
Stage 2 (Art 3-4): What happens when it defaults and how (evidence + mechanism)
Stage 3 (Art 5):   What to do about it (framework + practices)
Stage 4 (Art 6-7): What we don't know and where it generalizes (humility + scope)
```

Article 6's "honest caveat" tone is architecturally important: it prevents the series from overclaiming. After the confident framework in Art 5, Art 6 deliberately steps back. This is not a weakness — it is the exploratory-not-prescriptive tone from CLAUDE.md applied at the series level. Resist the urge to strengthen Art 6's claims when polishing.

### Recurring Theme 5: The "Fragile Expert" (Junior Developer Crisis)

Article 2 introduces the Fragile Expert concept (Prather et al., 2026). Article 4 contains the full junior developer crisis section. This is a one-way dependency: Art 4 extends Art 2's term. No further cross-reference needed in later articles unless Art 5's structured workflow section wants to address the training pipeline gap explicitly.

---

## Integration Points Between Articles

### Explicit Forward/Backward Pointers

Every draft article already contains explicit forward pointers at its end ("Next in the series: ..."). These must be consistent with what the next article actually delivers. Current state:

| Source | Points Forward To | Matches Actual Art? |
|--------|-------------------|---------------------|
| Art 2 | "what happens when debt defaults" | Yes — Art 3 delivers exactly this |
| Art 3 | "The Solutioning Trap — mechanisms that make debt easy to accumulate" | Yes — Art 4 delivers this |
| Art 4 | "The Trade-off Triangle — conscious positioning + concrete practices" | Yes — Art 5 delivers this |
| Art 5 | "Measuring the Unmeasurable — proxy indicators, honest caveats" | Yes — Art 6 delivers this |
| Art 6 | "Beyond Software — epistemic debt wherever humans collaborate with LLMs" | Yes — Art 7 delivers this |

All forward pointers are aligned. No restructuring needed.

### Back-Reference Language to Maintain

Articles use specific language to refer back to previous articles. When polishing, preserve these:

- Art 4 references "the 200-to-2,000 pattern from Article 3" — exact phrasing, do not change to a generic description
- Art 5 references "three SDLC boundaries" with boundary 3 completing the count from Art 4's two — do not renumber
- Art 5 references "Boundary 1 and 2 from Article 4" explicitly in the circular validation section — this is load-bearing cross-reference language
- Art 7 closes with "for six articles, we've explored..." — this is a series-count reference that only works if Art 7 is actually the seventh

### Series Boilerplate

Each article carries a consistent boilerplate structure:
1. Series identifier: "*This is Part N of a 7-part series on [epistemic debt...](url)*"
2. Opening recap: One paragraph bridging from the prior article
3. Content
4. Closing forward pointer: "*Next in the series: [Title] — [subtitle]*"
5. Footer: Subscribe call to action
6. References

Articles 3-7 all have this structure in place. The publication URLs in the forward pointers will need updating as each article is published (currently empty strings in YAML frontmatter).

---

## File Structure: Existing and New Components

### Existing (Modify)

```
topics/epistemic_debt/artifacts/articles/
├── article-3-when-debt-defaults.md     # Needs TODO integration (3 high-priority TODOs)
├── article-4-the-solutioning-trap.md   # Needs TODO integration (4 TODOs) + social teasers
├── article-5-the-trade-off-triangle.md # Needs TODO integration (2 critical TODOs: ε_k, t₀ connection)
├── article-6-measuring-the-unmeasurable.md  # Needs TODO integration (2 TODOs) + social teasers
└── article-7-beyond-software.md        # Nearest to complete; needs social teasers only
```

### New Components Needed

```
topics/epistemic_debt/artifacts/articles/
└── (no new files — all 7 articles exist as drafts)

topics/epistemic_debt/assets/
└── (no new diagrams required — Art 5 triangle diagram is ASCII, already in draft)

Social teasers (within YAML frontmatter of each article):
├── article-3: linkedin, twitter, instagram_caption, substack_notes — all empty
├── article-4: all empty
├── article-5: all empty
├── article-6: all empty
└── article-7: all empty
```

The only net-new content work is:
1. Resolving TODOs in articles 3-6
2. Writing social teasers for all five articles
3. Updating `publication_url` in each YAML frontmatter after Substack publication
4. Updating `status` from `draft` to `published` in each YAML after publication

---

## Architectural Patterns

### Pattern 1: The TODO Resolution Pattern

**What:** Each article contains bracketed TODO markers that flag content that was deferred from an earlier draft or cross-referenced from another article. These are not optional polish — several are load-bearing for the series' mathematical arc.

**Hierarchy by priority:**

| Priority | TODO | Location | Risk if Skipped |
|----------|------|----------|-----------------|
| Critical | Connect SDLC boundaries to t₀ concept | Art 4 | Breaks the mathematical thread from Art 2 |
| Critical | Connect strategy forces to t₀ + break-even formula | Art 5 | Leaves "Later articles will look at these mechanisms in detail" unfulfilled (planted in Art 2) |
| Critical | Introduce tolerance factor ε_k | Art 5 | Leaves "we'll return to this" seed from Art 2 unfulfilled |
| High | Add Fragile Expert / Prather et al. data (77% failure rate) | Art 3 | Missing key evidence for the case studies article |
| High | Add Stochastic Spaghetti Effect as named failure | Art 3 | Missing named mechanism that Art 4 will reference |
| High | Social invisibility of epistemic debt section | Art 4 | Gap in the "why teams don't notice" explanation |
| High | Senior Expertise Gap as measurement concern | Art 6 | r_k degradation argument adds rigor to measurement section |
| Medium | Add team-level Gc formulation | Art 6 | Nice mathematical closure but not reader-facing load-bearing |
| Low | Track epistemic status of architectural decisions | Art 6 | Side comment, does not affect series arc |

**When to use:** Resolve Critical and High priority TODOs during article polish. Medium and Low can be resolved or dropped at editorial discretion.

### Pattern 2: The Bridge Paragraph Pattern

**What:** Every article opens with a one-paragraph bridge from the prior article. These bridges are already written in all five drafts. They are the primary mechanism for series coherence for new-to-a-given-article readers.

**Maintenance rule:** When the prior article changes significantly in its closing argument, update the bridge paragraph of the next article. The current drafts are aligned — do not break alignment during polish.

**Example (Art 4 bridge):** "The core problem is not inexperience or lack of skill. It is jumping to creating a solution before clarifying the epistemic scope of the problem." This correctly follows Art 3's close: "The question is: how do teams fall into this pattern?"

### Pattern 3: The Concrete Example Anchor Pattern

**What:** Each abstract claim is anchored by a concrete scenario. The series uses a consistent set of named scenarios:
- Database deletion (SaaStr/Replit) — Art 3
- 10:1 cost ratio (AlterSquare) — Art 3, back-referenced in Art 4
- Rate limiter in-memory counter — Art 4
- Dashboard vibe-coding scenario — Art 4 (Boundary 1)
- Email validation regex / RFC 5321 — Art 4 (Boundary 2), Art 5 (Boundary 3 Python example)
- IRIS-2 project — Art 5 exclusively
- Healthcare data loss — Art 3

**Maintenance rule:** Do not introduce a new scenario in Art 5-7 that references a concept first introduced in Art 5. Art 6 and 7 must use scenarios that are either self-contained or reference only previously introduced vocabulary.

---

## Anti-Patterns

### Anti-Pattern 1: Resolving TODOs with New Concepts

**What people do:** When a TODO asks to "connect X to the t₀ concept," writers introduce new terms or reframe the t₀ concept itself.

**Why it's wrong:** Article 2 is published and immutable. Any reframing of t₀ in Art 4 or 5 will create an inconsistency that readers who read in series will notice.

**Do this instead:** Use the exact terminology from Art 2 (t₀, c_k, τ_k, δ, break-even). Add domain-specific examples that apply the formula rather than redefining it.

### Anti-Pattern 2: Weakening the Art 6 Honest Caveat

**What people do:** Treat Art 6's "we don't yet know how to measure this precisely" as a problem to be fixed by strengthening measurement claims.

**Why it's wrong:** The series's credibility rests on the exploratory-not-prescriptive tone. Art 6 builds trust precisely because it refuses to overclaim. Strengthening it would make the series feel prescriptive.

**Do this instead:** Add new measurement approaches only if they are honestly caveated. The existing triangulation approach is correct — present indicators, not metrics.

### Anti-Pattern 3: Breaking the SDLC Boundary Count

**What people do:** Add or rename SDLC boundaries during polish (e.g., adding "Model Drift" as a fourth boundary).

**Why it's wrong:** Article 5 explicitly calls Circular Validation "the third SDLC boundary from Article 4." If Art 4 gains a fourth boundary, Art 5's framing breaks and Art 4's existing ending ("the remaining question: what do we do about it?") needs rework.

**Do this instead:** If the Model Drift boundary material from the old research is valuable, present it as a related failure mode within an existing boundary rather than a new numbered boundary.

### Anti-Pattern 4: Adding IRIS-2 Material to Articles Outside Art 5

**What people do:** Cite IRIS-2 specific details (bounded contexts, 972-line E2E test, cursor rules) in Art 6 or Art 7 to add concreteness.

**Why it's wrong:** IRIS-2 is a software engineering case study. Art 7's architecture requires it to generalize beyond software. IRIS-2 examples in Art 7 would undermine the "beyond software" framing and feel like regression from the article's broadening purpose.

**Do this instead:** In Art 7, use the IRIS-2 DDD context files as one instance of the universal RAG pattern (briefly, without naming specifics), then immediately move to a non-software example.

---

## Integration Points

### External Integration: Substack Platform

| Integration | Pattern | Notes |
|-------------|---------|-------|
| Article 0 (series overview) | Forward links to Art 1-7 | Art 0 links will need updating as each article is published with its permanent URL |
| Substack publication | Manual publish + copy-paste of markdown | Export pipeline (`scripts/export-all.sh`) handles formatting |
| Social teasers | Written in YAML frontmatter, posted manually | All five articles have empty teaser fields |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Art 3 ↔ Art 4 | Art 4 back-references "the 200-to-2000 pattern" | Art 3 must finalize this case study first |
| Art 4 ↔ Art 5 | Art 5 completes the third SDLC boundary | Art 4's boundary count (2) must be locked before Art 5 is finalized |
| Art 2 ↔ Art 5 | Art 5 fulfills Art 2's "we'll return to this" promise on tolerance factor | Both the ε_k TODO and the t₀ connection TODO in Art 5 are cross-article obligations |
| Art 5 ↔ Art 7 | Art 7 generalizes the triangle — structure must be stable in Art 5 first | Triangle vertex definitions and strategy forces vocabulary must be locked |

---

## Data Flow: How Themes Move Through the Series

```
CONCEPT INTRODUCED                EXTENDED              RESOLVED
─────────────────────────────────────────────────────────────────

Epistemic debt (named)
    Art 1 ──────────────────────────────────────────────────────▶

Ed formula / t₀ / break-even
    Art 2 ──────── Art 4 (t₀ per boundary) ── Art 5 (strategy
    │              forces close the loop) ──────────────────────▶
    └── ε_k seed ─────────────────────────── Art 5 (ε_k TODO) ──▶

Circular validation trap
    Art 2 (planted) ─── Art 4 (Boundary 2 primes it) ── Art 5
    │                   (Boundary 3 full treatment) ─── Art 7
    │                   (per-domain generalization) ────────────▶

Vibe coding / solutioning trap
    Art 4 ──────────────────── Art 5 (named as trap to avoid) ──▶

Trade-off triangle
    Art 5 (introduced) ──────────────────── Art 7 (generalized) ▶

Measurement paradox
    Art 6 (standalone, honest) ─────────────────────────────────▶

Junior developer crisis / Fragile Expert
    Art 2 (named) ──── Art 4 (full treatment) ──────────────────▶
```

---

## Scaling Considerations

This is a content system, not a software system. The relevant "scaling" concern is publication cadence and reader experience.

| Consideration | Implication |
|---------------|-------------|
| Weekly Substack cadence | 5 articles = ~5 weeks of content after Art 2 publishes |
| Reader entry points | Art 0 links to each article; each article stands alone enough for new readers |
| Series completeness | Art 7 closes with "This concludes the Epistemic Debt series" — all 7 must publish for the close to land |
| Article 2 publication status | PROJECT.md says published; YAML frontmatter shows draft and empty `published_date` — verify before scheduling Art 3 |

---

## Sources

- Direct inspection of `topics/epistemic_debt/artifacts/articles/article-[0-7]-*.md`
- `topics/epistemic_debt/assets/0. series-plan.md` (master narrative plan)
- `.planning/PROJECT.md` (v3.0 milestone scope, key decisions)
- `.planning/research/SUMMARY.md` (v2.0 research findings)
- `CLAUDE.md` (writing rules, file conventions)
- `.ai/rules/writing-style.md`, `.ai/rules/terminology.md`

---

*Architecture research for: Epistemic Debt article series (articles 3-7 integration)*
*Researched: 2026-03-14*
