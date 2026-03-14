# Phase 1: Opening & Framing - Research

**Researched:** 2026-01-26
**Domain:** Technical writing, philosophical concept communication, paradigm shift narratives
**Confidence:** MEDIUM

## Summary

Research focused on five domains critical to planning the Opening & Framing phase:

1. **Technical article openings** - How to hook technical audiences with compelling scenarios
2. **Explaining philosophical concepts** - Bridging philosophy and engineering without jargon
3. **Paradigm shift framing** - Presenting fundamental changes effectively
4. **Existing literature** - Current discourse on LLMs and coding practices
5. **Tone calibration** - Balancing thought-provoking with exploratory

**Primary recommendation:** Use a concrete scenario-based hook (code review 2020 vs 2025), introduce "epistemic debt" before "epistemic warrant," employ analogy-first explanation, and maintain exploratory tone through structural choices rather than hedging language.

**Key finding:** The project already has strong internal literature review with 5+ authoritative sources on epistemic debt in LLM contexts (Ngabang 2026, Codemanship, academic papers). This positions the article within an emerging discourse rather than making novel claims.

**Primary recommendation:** Lead with concrete scenario, define through example, use quick analogy, then elaborate with precision.

## Standard Stack

### Core Narrative Structures

| Pattern | Purpose | When to Use | Evidence Source |
|---------|---------|-------------|-----------------|
| Scenario-based hook | Immediate reader identification | Opening paragraphs | Training data + project materials |
| Example-first definition | Accessible concept introduction | First mention of new terms | CONTEXT.md decision |
| Analogy-then-precision | Bridge familiar to novel | Philosophical concepts | Training data |
| Contrast framing | Highlight paradigm shifts | Thesis establishment | Outline-v1 structure |

### Supporting Techniques

| Technique | Purpose | When to Use |
|-----------|---------|-------------|
| Third-person observation → first-person thesis | Authority without prescriptiveness | Throughout article |
| Footnotes for precision | Satisfy both audiences (accessibility + rigor) | Philosophy terms |
| Table/visual comparison | Make abstract differences concrete | Technical debt vs epistemic debt |
| Inline examples | Ground abstract claims | Every major concept |

### Installation

No technical stack required - this is writing technique research.

## Architecture Patterns

### Recommended Opening Structure

```markdown
## Opening Section Architecture (500-700 words target)

1. Hook (100-150 words)
   - Concrete scenario: Code review 2020 vs 2025
   - Show the contrast viscerally before naming it
   - Immediate reader identification

2. Observation of the shift (200-250 words)
   - Name what changed (Construction → Curation)
   - Identify the stakes (epistemic opacity)
   - Establish thesis without prescription

3. Define key term (150-200 words)
   - "Epistemic debt" introduced through example
   - Quick analogy to technical debt (one sentence)
   - Clarify what's at stake

4. Frame the exploration (100-150 words)
   - Acknowledge trade-offs exist
   - Position article as investigation
   - Preview structure without roadmap paragraph
```

### Pattern 1: Scenario-Based Hook

**What:** Open with a concrete situation that embodies the abstract concept

**When to use:** When introducing philosophical or abstract concepts to technical audiences

**Example from CONTEXT.md:**
```markdown
A code review in 2020:
"Why does this algorithm work?"
"I chose binary search because the data is sorted and we need O(log n) lookup..."

A code review in 2025:
"Why does this algorithm work?"
"The LLM suggested it. The tests pass. It handles the edge cases I could think of."

Same confidence. Different warrant.
```

**Why it works:**
- Readers immediately recognize the situation
- Contrast is visceral before being named
- No need to "explain" the problem - they feel it
- Sets up the thesis naturally

### Pattern 2: Example-First Definition

**What:** Show the concept in action before naming it

**When to use:** First introduction of "epistemic debt" and "epistemic warrant"

**Structure:**
```markdown
[Concrete example showing code nobody understands]
↓
[Name it: "We can call this epistemic debt"]
↓
[Quick analogy: "Like technical debt, but for understanding"]
↓
[Elaborate with precision]
```

**Why it works:**
- Avoids lecture tone
- Reader discovers concept alongside you
- Accessible without being reductive

### Pattern 3: Analogy-Then-Precision

**What:** Use familiar parallel, then add necessary precision

**For epistemic debt:**
```markdown
Quick analogy: "Like technical debt, but for understanding" (one sentence)
↓
Table showing parallel (visual reinforcement)
↓
Key difference: "The critical difference lies in how debt accumulates..."
```

**For construction→curation shift:**
```markdown
Familiar framing: "The developer's role shifts from architect to curator"
↓
Add precision: "From being the architect of every decision to reviewing
               probabilistically-generated suggestions"
```

### Pattern 4: Trade-Off Positioning

**What:** Frame as trade-offs to explore rather than problems to solve

**Structure:**
```markdown
[Present the shift]
↓
[Acknowledge the trade-off]
↓
[Position as central question to explore]
↓
[Move past polarized debate]
```

**Example from CONTEXT.md:**
- Introduce the trade-off: complete ownership (no AI) vs velocity gained (AI production with partial ownership)
- Sweet spot positioned as the central question to explore
- No answer given in opening

**Why it works:**
- Avoids alarmist tone
- Invites exploration
- Respects reader intelligence
- Acknowledges complexity

### Anti-Patterns to Avoid

**Don't: Roadmap paragraph**
- "In this article, I will first discuss X, then examine Y, and finally explore Z"
- Feels academic/formal
- Contradicts exploratory tone

**Do instead:** Let structure show itself
- Section transitions that naturally lead forward
- Reader discovers journey while on it

**Don't: Hedge language for tone calibration**
- "It seems that perhaps maybe this might possibly..."
- Weakens authority
- Doesn't achieve exploratory tone

**Do instead:** Structural choices for tone
- Third person for observations: "LLMs introduce a rupture"
- First person for framing: "We can think of this as..."
- Questions to position exploration: "What prevents teams from..."
- Limitations sections to show uncertainty: "What prevents LLMs from being used to skip domain modeling too?"

**Don't: Front-load philosophy jargon**
- "Epistemic warrant" before "epistemic debt"
- "Epistemological framework" before concrete example
- Abstract before concrete

**Do instead:** Accessibility pathway
- Lead with "epistemic debt" (more digestible)
- Show example first, then name
- Use footnotes for precision terms

## Don't Hand-Roll

Problems that look simple but have existing solutions:

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Explaining philosophy to engineers | Custom analogies from scratch | Leverage technical debt mental model | Already established, credible, maps well |
| Paradigm shift narrative | Generic before/after | Concrete scenario contrast | Visceral > abstract for hooks |
| Tone calibration | Hedging language | Structural choices (POV, questions, limitations) | Maintains authority while exploring |
| Accessibility vs precision | Choose one | Multi-layer approach (plain language + footnotes) | Serves both audiences |

**Key insight:** Technical audiences already have strong mental models (technical debt, code review, SDLC). Leverage these rather than building new frameworks.

## Common Pitfalls

### Pitfall 1: Philosophy Lecture Opening

**What goes wrong:** Opening with abstract philosophical concepts ("epistemic warrant," "epistemological framework") before grounding in concrete experience.

**Why it happens:** Writer knows the philosophical underpinning and wants to establish rigor early.

**How to avoid:**
- Start with scenario (code review 2020 vs 2025)
- Show the problem before naming it
- Introduce "epistemic debt" (accessible) before "epistemic warrant" (precise)
- Use footnotes for philosophical precision

**Warning signs:**
- First paragraph contains words ending in "-ology" or "-logical"
- No concrete scenario in first 200 words
- Reader needs philosophy background to follow

**From CONTEXT.md decision:**
> "Lead with 'epistemic debt' — more digestible term than 'epistemic warrant'"
> "Footnote approach for philosophy terminology: plain language in text, 'epistemic warrant' in footnote for interested readers"

### Pitfall 2: Alarmist Framing

**What goes wrong:** Presenting LLM-assisted coding as inherently dangerous or a crisis.

**Why it happens:** The stakes are real, and writer wants to convey urgency.

**How to avoid:**
- Frame as trade-offs rather than threats
- Acknowledge velocity benefits explicitly
- Position "sweet spot" as the exploration goal
- Use "practices worth examining" not "must-do solutions"
- Structure shows uncertainty (open questions, limitations sections)

**Warning signs:**
- Words like "crisis," "disaster," "catastrophic"
- No acknowledgment of LLM benefits
- Prescriptive solutions presented as mandatory
- Tone feels urgent rather than curious

**From CONTEXT.md decision:**
> "Stakes visible: make clear that getting this wrong has real consequences, without being alarmist"
> "Brief nod to polarized debate (AI-boosters vs skeptics), then move past it"

### Pitfall 3: Prescriptive Solutions Too Early

**What goes wrong:** Offering solutions in the opening before establishing the problem's complexity.

**Why it happens:** Writer has explored guardrails (DDD, E2E testing) and wants to be helpful.

**How to avoid:**
- Opening focuses only on establishing the shift and naming the concept
- Solutions belong in Phase 5 (Guardrails)
- Use "practices worth examining" language throughout
- Include limitation subsections for each proposed guardrail

**Warning signs:**
- Opening mentions specific solutions (DDD, testing strategies)
- Language like "you should," "teams must," "the answer is"
- Missing acknowledgment that solutions have limitations

### Pitfall 4: Abstract Analogies

**What goes wrong:** Using generic analogies that don't leverage audience's existing mental models.

**Why it happens:** Trying to make concepts accessible without using domain-specific knowledge.

**How to avoid:**
- Use technical debt analogy (readers already understand this deeply)
- Leverage SDLC concepts readers know (requirements, implementation, validation)
- Use code review scenario (lived experience)
- Avoid generic analogies (house building, cooking, etc.)

**Warning signs:**
- Analogies from non-technical domains
- Analogies require as much explanation as original concept
- Analogies don't map cleanly to technical context

### Pitfall 5: Missing the Contrast

**What goes wrong:** Explaining what LLM-assisted coding is without showing what changed.

**Why it happens:** Focus on the new paradigm without anchoring in the old.

**How to avoid:**
- Always show before/after (2020 vs 2025)
- Make the shift explicit (construction → curation)
- Use contrast to establish stakes
- Table format reinforces comparison

**Warning signs:**
- Only describes current state
- No temporal markers or before/after
- Doesn't explain why this matters NOW

## Code Examples

Not applicable - this is a writing research phase, not code implementation.

## State of the Art

### Epistemic Debt Discourse (2024-2026)

| Concept | Earlier Framing | Current Framing | Impact |
|---------|-----------------|-----------------|--------|
| Epistemic debt | Manufacturing context (Ionescu 2020) | LLM-generated code context (Ngabang 2026) | Established term being applied to new domain |
| Comprehension gap | Isolated (Stack Overflow snippets) | Systemic (entire features) | Scale of the problem |
| Code authorship | Deterministic warrant | Convenient fiction | Philosophical reframing |
| Developer role | Constructor | Curator | Paradigm shift language |

**Key literature findings (from literature-review-on-epistemic-debt.md):**

1. **Ngabang (2026) - "The Illusion of Competence"**
   - Formal definition: "divergence between system complexity and developer's cognitive model"
   - Mathematical framing of epistemic debt
   - Introduces "Stochastic Spaghetti Effect" and "Context Window Amnesia"
   - Published January 2, 2026 (very recent, emerging discourse)

2. **Codemanship (2025) - "Comprehension Debt"**
   - Practical framing: "teams produce code faster than they can understand it"
   - Accessible blog post format
   - Real-world practitioner perspective

3. **Academic foundations**
   - Ionescu et al. (2020): Epistemic debt in smart manufacturing
   - Technical debt → epistemic issues in computational science

**What this means for the article:**
- Not making completely novel claims (good - positions within discourse)
- Recent enough that audience may not be familiar (2026 paper just published)
- Can reference established work while contributing unique angle
- "Construction → Curation" framing appears to be novel contribution

### Technical Writing Best Practices (2025)

**Opening hooks - current recommendations:**
- Scenario-based over abstract (training data, consistent across sources)
- Concrete before conceptual (writing pedagogy)
- Reader identification first (engagement strategy)
- Stakes established early but not alarmist (tone balance)

**Philosophy communication to technical audiences:**
- Example-first definition (pedagogical research)
- Multi-layer accessibility (plain language + footnotes for precision)
- Leverage existing mental models (cognitive load theory)
- Avoid jargon without definition (accessibility guidelines)

**Paradigm shift narratives:**
- Before/after contrast (training data)
- Show what changed, not just what is (comparison effectiveness)
- Temporal markers for clarity (2020 vs 2025)
- Acknowledge what's gained and lost (nuance over polemic)

## Open Questions

Things that couldn't be fully resolved:

1. **Exact scenario details for code review hook**
   - What we know: 2020 vs 2025 contrast, code review setting, show both perspectives
   - What's unclear: Specific technical content, character names, exact code being reviewed
   - Recommendation: Mark as Claude's discretion per CONTEXT.md, propose three AI visibility options during drafting

2. **Philosophy depth calibration**
   - What we know: Lead with accessible ("epistemic debt"), use footnotes for precision
   - What's unclear: How much elaboration on "epistemic warrant" in opening vs defer to later
   - Recommendation: One-sentence mention in opening, deeper treatment deferred to Phase 2

3. **Time marker specificity**
   - What we know: Contrast is essential, temporal markers clarify shift
   - What's unclear: Exact years (2020/2025) vs era framing ("pre-LLM"/"LLM-era")
   - Recommendation: Claude's discretion per CONTEXT.md; exact years are more concrete, era framing more timeless

4. **WebSearch unavailable - couldn't verify:**
   - Current best practices in technical writing (2025-2026)
   - Recent examples of paradigm shift framing
   - Latest research on philosophy communication to technical audiences
   - Recommendation: Rely on training data + project materials, mark as MEDIUM confidence

## Sources

### Primary (HIGH confidence)

**Project materials:**
- `/home/arau6/projects/ai-articles/.planning/phases/01-opening-framing/01-CONTEXT.md` - User decisions from discuss-phase
- `/home/arau6/projects/ai-articles/epistemic_debt/raw_material/outline-v1-epistemic-debt.md` - Article structure and gaps
- `/home/arau6/projects/ai-articles/epistemic_debt/references/literature-review-on-epistemic-debt.md` - Authoritative sources on epistemic debt
- `/home/arau6/projects/ai-articles/GLOSSARY.md` - Terminology definitions
- `/home/arau6/projects/ai-articles/CLAUDE.md` - Writing style guidelines and tone

**Academic/authoritative sources (via literature review):**
- Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering"
- Codemanship (2025). "Comprehension Debt: The Ticking Time Bomb of LLM-Generated Code"
- Ionescu, T.B., Schlund, S., Schmidbauer, C. (2020). "Epistemic Debt: A Concept and Measure of Technical Ignorance in Smart Manufacturing"

### Secondary (MEDIUM confidence)

**Training data (as of January 2025):**
- Technical writing best practices (scenario-based hooks, example-first definitions)
- Philosophy communication strategies (analogy-then-precision, multi-layer accessibility)
- Narrative structures for paradigm shifts (contrast framing, before/after)
- Tone calibration techniques (structural choices over hedging language)

**Note:** Training data treated as hypothesis per research protocol, cross-referenced with project materials where possible.

### Tertiary (LOW confidence)

**WebSearch unavailable** - Could not verify:
- 2025-2026 current trends in technical writing
- Recent successful examples of paradigm shift framing
- Latest academic research on technical communication

## Metadata

**Confidence breakdown:**
- Standard stack: MEDIUM - Based on training data + strong project materials, but WebSearch unavailable for verification
- Architecture patterns: HIGH - Derived from CONTEXT.md user decisions + existing outline structure
- Common pitfalls: HIGH - Clearly defined in CONTEXT.md + CLAUDE.md writing guidelines
- Existing literature: HIGH - Comprehensive literature review already exists in project
- Tone calibration: HIGH - Explicit guidance in CONTEXT.md and CLAUDE.md

**Research limitations:**
- WebSearch unavailable - relied on training data for technical writing best practices
- No verification of 2025-2026 current trends
- Literature review already complete (no additional research needed)

**Research date:** 2026-01-26
**Valid until:** 30 days (stable domain - writing techniques don't change rapidly)

**Research approach:**
Given WebSearch unavailability, research focused on:
1. Comprehensive review of existing project materials (CONTEXT.md, outline, literature review, style guide)
2. Application of training data knowledge about technical writing, philosophy communication, and narrative structures
3. Cross-referencing decisions already made in CONTEXT.md
4. Identifying what planner needs to know vs what remains as implementation discretion

**Key finding:** Project materials are exceptionally rich. CONTEXT.md provides clear implementation decisions, literature-review provides authoritative sources, and CLAUDE.md provides explicit tone/style guidance. Research could focus on synthesis rather than discovery.
