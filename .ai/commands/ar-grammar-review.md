---
description: "Command: Review article for grammatical and syntactical issues using a tiered approach with trade-off analysis, preserving the author's voice and style."
alwaysApply: false
---

# Grammar and Syntax Review with Trade-Off Analysis

Review an article for grammatical and syntactical issues using a tiered, risk-based approach. Each correction includes pros/cons analysis to preserve the author's unique voice while fixing non-native English speaker issues.

## Placeholders

| Placeholder | Description | Example |
| ----------- | ----------- | ------- |
| `{{ARTICLE_PATH}}` | Path to the markdown article file | `topics/epistemic_debt/artifacts/articles/drafts/v1/article-1-the-epistemic-shift.md` |
| `{{DIALECT}}` | English dialect preference (optional) | `american` or `british` (default: `american`) |

## Prompt

Read and review deeply `{{ARTICLE_PATH}}` and propose a plan to fix grammatical and syntactical issues, **WITHOUT modifying the style at all!** I don't want to sound robotic or AI. I want to keep or raise the humanized factor of the text style and tone. But I want to fix my non-native English speaker issues.

Give me pros and cons for every correction and let's do a trade-off analysis together.

---

## Review Methodology

### Tiered Risk Assessment

Categorize all issues into tiers based on risk to the author's voice:

#### Tier 1: Clear Typos and Mechanical Errors (Zero Risk)
- Unambiguous typos (misspellings, transposed letters, missing characters)
- Mechanical errors (missing spaces, capitalization of proper nouns)
- **Action**: Fix all. No trade-off analysis needed.

#### Tier 2: Grammar Fixes (Low-to-Medium Risk)
- Question word order
- Missing articles
- Subject-verb agreement
- Preposition/idiom choices (e.g., "in the meaning of" vs "in the sense of")
- Spelling consistency (American vs British English)
- Punctuation (commas, periods)
- **Action**: For each issue, provide:
  - Current text
  - Proposed fix
  - Pros of fixing
  - Cons of fixing (voice/style impact)
  - Recommendation with rationale

#### Tier 3: Tense Consistency (Medium Risk -- Voice at Stake)
- Mixed tenses in narrative passages
- Present vs past tense choices
- **Action**: Present multiple options (fix vs preserve) with voice impact analysis. Ask author to decide.

#### Tier 4: Punctuation and Hyphenation (Low Risk)
- Compound adjective hyphenation
- Dash vs comma choices
- **Action**: Provide options with readability vs formality trade-offs.

#### Tier 5: Capitalization and Formatting (Low Risk)
- Title case vs sentence case
- Subtitle formatting
- **Action**: Present standard conventions vs stylistic choices.

#### Tier 6: Repetition and Flow (Medium Risk)
- Verbatim repetition
- Sentence flow improvements
- **Action**: Show original vs reworked versions with emphasis/flow trade-offs.

---

## Output Format

### 1. Initial Questions (if needed)

Before creating the plan, ask clarifying questions about:
- English dialect preference (American vs British)
- Intentional stylistic choices that might look like errors
- Any passages the author wants to preserve exactly as-is

### 2. Plan Structure

Create a detailed plan document with:

```markdown
# Grammar and Syntax Fix Plan for [Article Title]

Target file: [path]

Standard: **[Dialect] English** (per author preference).

---

## Tier 1: Clear Typos and Mechanical Errors (Zero Risk to Voice)

[List all unambiguous fixes]

---

## Tier 2: Grammar Fixes (Low-to-Medium Risk, Needs Discussion)

### 2a -- [Issue Name] (line X)

- **Current**: *"[exact text]"*
- **Option A**: *"[proposed fix]"*

**Pros**: [why fix it]
**Cons**: [voice/style impact]
**Recommendation**: [with rationale]

[Repeat for each issue]

---

## Tier 3: Tense Consistency (Medium Risk -- Voice at Stake)

[Present options with voice analysis]

---

## Tier 4: Punctuation and Hyphenation (Low Risk)

[Present options with trade-offs]

---

## Tier 5: Capitalization and Formatting (Low Risk)

[Present options]

---

## Tier 6: Repetition and Flow (Medium Risk)

[Show original vs reworked with trade-offs]

---

## Summary: Decision Matrix

- **Tier 1**: Fix all. Zero risk.
- **Tier 2**: [Summary of recommendations]
- **Tier 3**: [Author decision needed]
- **Tier 4**: [Author decision needed]
- **Tier 5**: [Author decision needed]
- **Tier 6**: [Author decision needed]
```

### 3. Interactive Discussion

After presenting the plan:
- Wait for author decisions on Tier 2-6 items
- Discuss trade-offs for borderline cases
- Adjust recommendations based on author preferences
- Only proceed with fixes after explicit approval

---

## Principles

1. **Preserve voice above all** -- When in doubt, ask rather than assume.
2. **Explain, don't just fix** -- Every correction should have a rationale.
3. **Respect intentional choices** -- Mixed tenses, casual phrasing, and stylistic fragments may be deliberate.
4. **Non-native patterns vs style** -- Distinguish between errors and voice. Fix errors; preserve voice.
5. **Trade-off transparency** -- Always show what's gained and what's lost with each fix.

---

## Example Invocation

> Review `topics/epistemic_debt/artifacts/articles/drafts/v1/article-1-the-epistemic-shift.md` for grammar issues using the tiered approach with trade-off analysis.
