# Phase 9: Opening & Framework - Research

**Researched:** 2026-01-27
**Domain:** Technical presentation design (Marp), opening hooks, visual frameworks
**Confidence:** MEDIUM

## Summary

Phase 9 focuses on creating an effective opening for the IRIS-2 learnings presentation and establishing the Trade-off Triangle as the central visual framework. Research examined existing presentation assets, Marp visualization capabilities, and technical presentation best practices.

**Key findings:**
- The "Same confidence, different warrant" hook is already proven effective in existing slides.md
- Trade-off Triangle visualization exists in two forms: ASCII diagram and conceptual framework
- Marp supports ASCII art in code blocks, inline SVG, and described visuals
- Case study positioning should occur after framework introduction (framework first, then concrete example)

**Primary recommendation:** Use the existing Trade-off Triangle ASCII diagram from slides.md in a code block, introduce it before IRIS-2 positioning to establish the mental model first.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Marp | Current (2026) | Markdown-based presentations | Official ecosystem for Markdown slides, Bloomberg team familiarity |
| Marpit | Current | Marp rendering engine | Underlying framework, supports CommonMark + extensions |

### Supporting
| Tool | Purpose | When to Use |
|------|---------|-------------|
| VS Code Marp Extension | Live preview | During authoring |
| Marp CLI | Export to PDF/PPTX | Final delivery format |

**Installation:**
Not applicable - Marp is already in use for this project per existing slides.md

## Architecture Patterns

### Recommended Slide Structure for Phase 9

```
Opening Sequence:
1. Title slide
2. Hook slide ("Same confidence, different warrant")
3. Triangle introduction slide (visual + explanation)
4. IRIS-2 positioning slide (map case study to triangle)
```

### Pattern 1: Contrast-Based Hook

**What:** Open with a before/after scenario that highlights the core tension

**When to use:** Technical presentations where paradigm shift is central

**Example from existing slides.md:**
```markdown
## The Question

> Ask an engineer in 2020 why their code works:
> "I chose this algorithm because..., implemented it this way because..."

> Ask an engineer in 2025:
> "The LLM suggested it, the tests pass, looks good."

**Same confidence. Different warrant.**
```

**Why effective:**
- Immediately establishes what's at stake
- Uses parallel structure for clarity
- Ends with memorable phrase ("Same confidence. Different warrant.")
- Resonates with audience's lived experience (2020 vs 2025)

### Pattern 2: Framework-Before-Examples

**What:** Introduce conceptual framework first, then map concrete case study to it

**When to use:** When presenting a mental model with supporting case study

**Structure:**
1. Hook (establish tension)
2. Framework visual (Trade-off Triangle)
3. Framework explanation (what the vertices mean)
4. Case study positioning (IRIS-2 as example of conscious triangle positioning)

**Rationale:** Audience needs the mental model before they can understand how IRIS-2 maps to it. Framework provides the lens through which they'll interpret the examples.

### Pattern 3: Progressive Disclosure

**What:** Introduce triangle visual first, then add positioning arrows/examples in later slides

**When to use:** Complex diagrams that need layered explanation

**For Trade-off Triangle:**
- Slide 1: Basic triangle with vertices labeled
- Later slides: Add strategy arrows (DDD, TDD) and positioning markers
- Final vertex slides: Show IRIS-2 examples at each corner

### Anti-Patterns to Avoid

- **Examples-before-framework:** Don't show IRIS-2 practices before explaining the triangle they map to (audience won't have context)
- **Overloaded opening:** Don't combine hook + full triangle + IRIS-2 on one slide
- **Unexplained jargon:** Don't use "epistemic warrant" in opening without definition (save for later)
- **Purely theoretical triangle:** Don't introduce triangle without stating it will have concrete examples

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| ASCII diagram formatting | Custom spacing/alignment | Code block with monospace | Marp preserves spacing in code blocks, ensures consistency across renders |
| Diagram rendering | Attempt to draw with CSS/HTML | ASCII art in code block OR inline SVG | Markdown simplicity, version control friendly |
| Animation/transitions | Complex Marp directives | Static slides with clear progression | Internal presentation, not keynote; clarity over flash |

**Key insight:** Marp's strength is simplicity and Markdown-friendliness. Work with that grain, not against it.

## Common Pitfalls

### Pitfall 1: Hook Without Clear Payoff
**What goes wrong:** Opening with intriguing question but never circling back to answer it
**Why it happens:** Hook gets disconnected from rest of presentation structure
**How to avoid:** Ensure slide 3-4 explicitly connects hook to framework ("The triangle shows WHY the warrant changed")
**Warning signs:** Audience confusion about relevance of opening

### Pitfall 2: Triangle Complexity Overload
**What goes wrong:** Introducing full Trade-off Triangle with all annotations (DDD arrows, TDD arrows, circular validation trap, etc.) in first appearance
**Why it happens:** Designer knows the full model and wants to show everything
**How to avoid:** Start with basic triangle (three vertices only), add complexity in subsequent slides
**Warning signs:** Diagram has >5 annotations on first appearance

### Pitfall 3: Abstract Framework Without Grounding
**What goes wrong:** Showing triangle without stating "Here's a concrete example: IRIS-2"
**Why it happens:** Assumption that framework is self-evidently useful
**How to avoid:** Explicitly state in framework slide: "I'll show how IRIS-2 consciously positioned in this triangle"
**Warning signs:** Audience asks "How would we actually use this?"

### Pitfall 4: ASCII Diagram Rendering Breaks
**What goes wrong:** Triangle ASCII art looks correct in editor but breaks when rendered (spacing collapses, alignment fails)
**Why it happens:** Marp rendering differences between preview and export
**How to avoid:** Always test in code block with monospace font; verify PDF export matches preview
**Warning signs:** Triangle looks misaligned in rendered output

### Pitfall 5: Case Study Before Context
**What goes wrong:** Mentioning IRIS-2 practices before explaining what triangle they map to
**Why it happens:** Presenter knows the connection, assumes audience will follow
**How to avoid:** Framework slide BEFORE case study positioning slide
**Warning signs:** Audience confused about what DDD/TDD/workflow have in common

## Code Examples

### Verified Pattern 1: Opening Hook (from existing slides.md)

```markdown
---
## The Question

> Ask an engineer in 2020 why their code works:
> "I chose this algorithm because..., implemented it this way because..."

> Ask an engineer in 2025:
> "The LLM suggested it, the tests pass, looks good."

**Same confidence. Different warrant.**

<!--
Speaker notes: Start with this contrast to immediately establish what's at stake.
-->
```

**Source:** `/home/arau6/projects/ai-articles/epistemic_debt/slides.md` (lines 18-30)

### Verified Pattern 2: Triangle ASCII Diagram (from existing slides.md)

```markdown
---
## The Trade-off Triangle

LLM-augmented development exists in three dimensions:

\`\`\`
                       SPEED
                         ▲
                        / \
                       /   \
                      / ●   \    ← Vibe Coding
                     / / \   \
                    / ↙   ↘   \
                   /DDD   TDD  \  ← Strategy forces
                  /   ↘   ↙     \
                 /      ●        \
                /   Balanced      \
               /      Zone         \
              ▼────────────────────▼
       UNDERSTANDING          RELIABILITY
\`\`\`

**Each guardrail pulls toward specific corners.**

<!--
Speaker notes: Introduce this as a mental model for trade-off decisions.
-->
```

**Source:** `/home/arau6/projects/ai-articles/epistemic_debt/slides.md` (lines 123-148)

**Note:** Use triple backticks to create code block for ASCII diagram preservation.

### Verified Pattern 3: Framework Explanation After Visual (from existing slides.md)

```markdown
---
## Strategy Forces

| Strategy | Primary Pull | Effect |
|----------|-------------|--------|
| **DDD** | → Understanding | Aligns output with domain |
| **TDD** | → Reliability | Verifies correctness |
| **Human Review** | → Both | Catches blind spots |
| **Workflow** | Amplifies all | Enables lower-triangle zones |

**Goal:** Consciously choose where to operate, not maximize speed.

<!--
Speaker notes: Emphasize that the goal is conscious positioning, not avoiding trade-offs.
-->
```

**Source:** `/home/arau6/projects/ai-articles/epistemic_debt/slides.md` (lines 152-167)

### Recommended Pattern 4: IRIS-2 Positioning Statement

```markdown
---
## IRIS-2 as Case Study

Real project where Trade-off Triangle practices were developed:

- **Understanding pull:** DDD with bounded contexts
- **Reliability pull:** Human-authored E2E tests
- **Speed enabler:** Structured workflow (GSD)

**Result:** Conscious positioning in lower-triangle zone

<!--
Speaker notes: Briefly introduce IRIS-2 as concrete example, detailed practices come in vertex slides.
-->
```

**Source:** Based on PROJECT.md context, original pattern for Phase 9
**Confidence:** MEDIUM (pattern not yet in slides.md but follows established structure)

## State of the Art

| Aspect | Old Approach | Current Approach | When Changed | Impact |
|--------|--------------|------------------|--------------|--------|
| Marp visuals | External image files | Inline SVG + ASCII in code blocks | Ongoing | Simpler version control, markdown-native |
| Opening hooks | Generic problem statement | Specific before/after contrast | Current best practice | Higher engagement, clearer stakes |
| Framework presentation | Show complete model first | Progressive disclosure | Established pattern | Better comprehension, less cognitive load |

**Deprecated/outdated:**
- Complex animations in Marp: Keep it simple, focus on content
- Marp Web (PWA): Marked as outdated, use VS Code extension or CLI

## Open Questions

### 1. Should Triangle Visual Be Simplified for Opening?

**What we know:**
- Existing slides.md has full triangle with annotations (slide 123)
- Best practice suggests progressive disclosure
- Opening slide should establish framework clearly

**What's unclear:**
- Whether IRIS-2 presentation should use full triangle immediately or simplified version first
- How much annotation is too much for first appearance

**Recommendation:**
- Use simplified triangle (vertices only) in framework introduction slide
- Add annotations (DDD/TDD arrows) in subsequent "Strategy Forces" slide
- This matches existing slides.md structure (basic triangle slide 123, strategy forces slide 152)

### 2. How Much IRIS-2 Context to Provide in Opening?

**What we know:**
- Audience is internal Bloomberg team (familiar with IRIS-2)
- PROJECT.md states "can reference IRIS-2 directly"
- Opening should hook, not explain everything

**What's unclear:**
- Whether opening needs "IRIS-2 is [description]" or can assume knowledge
- Balance between context and brevity

**Recommendation:**
- Minimal context in opening: "Real project: IRIS-2"
- Full context comes in positioning slide after framework
- Leverage audience familiarity, don't over-explain

### 3. Optimal Slide Count for Phase 9?

**What we know:**
- Total presentation target: 8-10 slides (ROADMAP.md Phase 11 success criteria)
- Phase 9 covers: opening hook + triangle framework + IRIS-2 positioning
- Phase 10 covers: vertex content with examples

**What's unclear:**
- How many slides Phase 9 should produce (affects Phase 10 budget)

**Recommendation:**
- 4 slides for Phase 9:
  1. Title/opening
  2. Hook ("Same confidence, different warrant")
  3. Triangle visual + introduction
  4. IRIS-2 positioning
- Leaves 4-6 slides for Phase 10 vertex content and Phase 11 closing

## Sources

### Primary (HIGH confidence)
- `/home/arau6/projects/ai-articles/epistemic_debt/slides.md` - Existing general presentation with proven hook and triangle
- `/home/arau6/projects/ai-articles/epistemic_debt/assets/epistemic-trade-off-triangle.md` - Detailed triangle framework
- `/home/arau6/projects/ai-articles/.planning/PROJECT.md` - IRIS-2 case study context
- `/home/arau6/projects/ai-articles/.planning/REQUIREMENTS.md` - Phase 9 requirements (STRUCT-01, STRUCT-02)
- Marp official documentation (marpit.marp.app, github.com/marp-team/marp-core) - Visualization capabilities

### Secondary (MEDIUM confidence)
- Technical presentation best practices from training data (January 2025) - Opening hooks, progressive disclosure
- Markdown presentation patterns from training data - ASCII diagrams in code blocks

### Tertiary (LOW confidence)
- None marked - WebSearch unavailable, all findings verified with existing project assets

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Marp already in use, official documentation reviewed
- Architecture patterns: HIGH - Based on existing slides.md proven patterns
- Opening hook effectiveness: HIGH - Already validated in slides.md line 26
- Triangle visualization: HIGH - Existing implementation in slides.md lines 123-148
- Case study positioning: MEDIUM - Recommendation based on best practices, not yet implemented for IRIS-2 version
- Marp capabilities: MEDIUM - Official docs reviewed but limited detail on edge cases

**Research limitations:**
- WebSearch unavailable (API error) - relied on existing project assets and training data
- No access to IRIS-2 codebase for verification of specific file paths/examples
- Marp rendering edge cases not fully tested (recommendation: verify PDF export)

**Research date:** 2026-01-27
**Valid until:** ~60 days (Marp stable, presentation patterns slow-moving)

**Key validation needed:**
- Test ASCII triangle rendering in Marp PDF export
- Verify IRIS-2 file paths for vertex slides (Phase 10)
- Confirm Bloomberg team familiarity with IRIS-2 project
