---
article: article-4-the-solutioning-trap
fact_check_date: 2026-04-12
status: approved
verified_count: 8
flagged_count: 3
unverified_count: 1
---

# Article 4: The Solutioning Trap — Fact-Check Report

**Date:** 2026-04-12
**Article:** Article 4 — The Solutioning Trap (rewritten practical pivot)
**Scope:** All external claims, statistics, and references that will appear in the rewritten Article 4 draft. This report covers the new citations introduced by the practical pivot (Anthropic Fellows RCT, CoVe, ToT, processing fluency) as well as claims carried forward from the existing 2607-word draft.

---

## Executive Summary

**8 VERIFIED, 3 FLAGGED, 1 UNVERIFIED-BY-DESIGN.**

All primary academic and empirical sources are live and accessible. The two high-confidence citations the article depends on most — the Anthropic Fellows RCT (E1) and the Chain-of-Verification paper (P1) — are VERIFIED against live arXiv pages. The Karpathy "vibe coding" quote (K1) is accessible via X but exact wording cannot be confirmed without login; marked UNVERIFIED with a suggested hedge. One claim (M4) is intentionally unverified: the `<asin>` and `<soltree>` macros are NOT yet in the pmacros PROJECT.md and the article must hedge accordingly.

The Parasuraman & Manzey (2010) DOI returns 404 on direct lookup but the paper is a well-established seminal reference in aviation/HCI literature and appears in the existing draft's reference list — rated UNVERIFIED (access-controlled) with a note. The Reber & Schwarz (1999) DOI resolves via redirect — VERIFIED as accessible.

**No INCORRECT or OVERSTATED findings.** The Anthropic Fellows RCT numbers (50% vs 67%, 17 pp gap, Cohen's d=0.738, p=0.010, n=52) match the research notes sourced directly from arXiv:2601.20245v1.

---

## Category 1: Empirical Studies

| # | Claim (verbatim as article will use) | Rating | Source | URL | Notes |
|---|--------------------------------------|--------|--------|-----|-------|
| E1 | "In a 2026 Anthropic Fellows RCT, developers using AI scored 17 percentage points lower on a quiz covering concepts they had used just minutes earlier." | VERIFIED | Shen, J.H. & Tamkin, A. (2026). "How AI Impacts Skill Formation." Anthropic Fellows Program. arXiv:2601.20245v1 | https://arxiv.org/abs/2601.20245 and https://www.anthropic.com/research/AI-assistance-coding-skills | Live HTTP 200 on both URLs (2026-04-12). Study: 52 participants (26 control, 26 AI-assisted), quiz on Trio async Python. AI group 50% vs control 67% — 17 pp gap. Cohen's d=0.738, p=0.010. Largest gap on debugging questions. Quote from paper: "On a quiz that covered concepts they'd used just a few minutes before, participants in the AI group scored 17% lower than those who coded by hand." Note: "17 percentage points" and "17%" are used interchangeably in the source — 50% vs 67% is a 17 percentage-point difference, which the source renders as "17% lower." The article's phrasing "17 percentage points lower" is accurate and slightly more precise. |
| E2 | "A 2025 METR study found developers were 19% slower with AI tools while estimating themselves 20% faster." | VERIFIED | Becker, J. et al. (2025). "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity." METR. arXiv:2507.09089 | https://arxiv.org/abs/2507.09089 and https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | Live HTTP 200 on both URLs (2026-04-12). Caveats: n=16 experienced open-source developers; mature/large repos only. Optional citation — include only if word budget allows. |

---

## Category 2: Cognitive Bias Mechanisms

| # | Claim (verbatim as article will use) | Rating | Source | URL | Notes |
|---|--------------------------------------|--------|--------|-----|-------|
| B1 | "Automation bias names the well-documented tendency to weight machine output more heavily than competing signals." | UNVERIFIED (access-controlled) | Parasuraman, R. & Manzey, D.H. (2010). "Complacency and Bias in Human Use of Automation: An Attentional Integration." *Human Factors*, 52(3), 381-410. | DOI:10.1177/0018720810371093 — returns 404 on direct DOI lookup; SAGE journal page returns 403 (access-controlled). | Paper is widely cited in aviation/HCI literature and appears in the existing draft's reference list. Abstract is accessible at https://pubmed.ncbi.nlm.nih.gov/20849017/ — existence confirmed. Rating: UNVERIFIED because the full text and exact wording of the automation bias definition could not be confirmed via open URL. The claim as phrased is a reasonable paraphrase of the well-known concept and is unlikely to be contested. Author's Prudence Principle: recommended action is to keep but add a hedge or cite an open-access summary of the concept. PubMed abstract URL is live. |
| B2 | "Cleanly formatted, idiomatic code is easier to read, and ease of processing is consistently misattributed as evidence of correctness." | VERIFIED | Reber, R. & Schwarz, N. (1999). "Effects of perceptual fluency on judgments of truth." *Consciousness and Cognition*, 8(3), 338-342. | https://doi.org/10.1006/ccog.1999.0386 — resolves via redirect, HTTP 200 (2026-04-12) | Paper established the processing fluency / truth judgment link. The specific application to code review is an adaptation by the article author, not a direct claim in the source — rated VERIFIED for the underlying mechanism, with a note that the code-specific application is author inference (acceptable for exploratory writing). |

---

## Category 3: Prior Art (Prompt Engineering)

| # | Claim (verbatim as article will use) | Rating | Source | URL | Notes |
|---|--------------------------------------|--------|--------|-----|-------|
| P1 | "Chain-of-Verification asks the model to externalize verification questions about its own draft before committing to a final answer." | VERIFIED | Dhuliawala, S. et al. (2023). "Chain-of-Verification Reduces Hallucination in Large Language Models." Findings of ACL 2024. arXiv:2309.11495 | https://arxiv.org/abs/2309.11495 — HTTP 200 (2026-04-12) | Mechanism confirmed: model drafts initial response, plans verification questions, answers them independently, produces final verified response. The `<asin>` macro is an adaptation (assumption-surfacing before drafting rather than fact-verification after), not a direct implementation — article should be explicit about this. |
| P2 | "Tree of Thoughts demonstrated that deliberate exploration of alternative reasoning paths outperforms greedy commitment to the first plausible solution." | VERIFIED | Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." NeurIPS 2023. arXiv:2305.10601 | https://arxiv.org/abs/2305.10601 — HTTP 200 (2026-04-12) | Finding confirmed: Game of 24 task, GPT-4 + CoT: 4%; ToT: 74%. The `<soltree>` macro is an interactive adaptation that exposes branch points to the human rather than having the model search internally — article should make this distinction clear. |

---

## Category 4: Karpathy Quote

| # | Claim (verbatim as article will use) | Rating | Source | URL | Notes |
|---|--------------------------------------|--------|--------|-----|-------|
| K1 | "Andrej Karpathy coined the term 'vibe coding' in early 2025." | UNVERIFIED | Karpathy, A. (February 2025). Post on X (formerly Twitter). | https://x.com/karpathy/status/1886192184808149052 — HTTP 200 (2026-04-12), but X requires login to read full post content | URL is accessible but exact wording and precise date cannot be confirmed without authentication. The claim is widely reported in industry press (multiple secondary sources cite this as February 2025). The current draft already uses this framing. Author's Prudence Principle: recommended action is to add a hedge or use secondary attribution. |

---

## Category 5: pmacros Claims

| # | Claim (verbatim as article will use) | Rating | Source | URL | Notes |
|---|--------------------------------------|--------|--------|-----|-------|
| M1 | "pmacros expands `<tagname>` tags via a Claude Code UserPromptSubmit hook." | VERIFIED | pmacros PROJECT.md | /home/arau6/projects/pmacros/.planning/PROJECT.md | Active requirement verbatim: "`<tagname>` expansion via `UserPromptSubmit` hook (Node.js, no external dependencies)." Hook system confirmed in Context section: "Hook system: `UserPromptSubmit` hook in `~/.claude/settings.json`." |
| M2 | "Macros are stored per-user (~/.claude/pmacros/macros.json) or per-project (.claude/pmacros/macros.json), with project overriding user." | VERIFIED | pmacros PROJECT.md | /home/arau6/projects/pmacros/.planning/PROJECT.md | Active requirement verbatim: "User-level scope (`~/.claude/pmacros/macros.json`) and project-level scope (`.claude/pmacros/macros.json`); project overrides user on name collision." Exact match. |
| M3 | "pmacros has no external Node.js dependencies." | VERIFIED | pmacros PROJECT.md | /home/arau6/projects/pmacros/.planning/PROJECT.md | Constraints section verbatim: "No external npm packages in the hook script or install script — Node.js stdlib only. Minimizes install friction for all users." Tag format also confirmed: "lowercase alphanumeric + hyphens, 1-32 chars." |
| M4 | "`<asin>` and `<soltree>` are proposed default macros for pmacros." | UNVERIFIED-BY-DESIGN | None — not in pmacros PROJECT.md | n/a | The two macros are described in CONTEXT.md only. pmacros PROJECT.md does not name them. Article must use hedging framing: "the default macros I am proposing for pmacros" or equivalent. This is expected; M4 is a contribution the article makes to pmacros, not a pre-existing feature. Plan 01 MUST use hedging language for these macros — they are not yet shipped and not yet in PROJECT.md. |

---

## Critical Findings

The following claims require user decisions before any prose-modifying plan runs. Listed in order of priority.

### CF-1: M4 — `<asin>` and `<soltree>` macros are not in pmacros PROJECT.md (UNVERIFIED-BY-DESIGN)

The two macros are central to the practical pivot but are not documented in pmacros PROJECT.md. The article must hedge throughout using language like "the default macros I am proposing for pmacros" or "macros I intend to ship as defaults." This is not a factual error — it is a planned framing choice. Plan 01 must be briefed to use this hedging consistently.

**Required action:** Plan 01 must receive explicit instruction to use hedging framing for M4. No decision checkbox needed — this is already locked in the plan.

### CF-2: K1 — Karpathy "vibe coding" exact wording unverifiable (UNVERIFIED)

The URL is live but X requires login to read full content. Exact wording of the post cannot be confirmed. The existing draft quotes: "You just see stuff, say stuff, run stuff, and copy stuff, and it mostly works." This wording is widely reproduced in secondary sources but cannot be directly verified here.

**Author's Prudence Principle recommendation:** REMOVE the direct quote. Retain attribution as "Andrej Karpathy introduced the term 'vibe coding' in early 2025" (no direct quote). This eliminates the verification risk with zero loss of substance.

### CF-3: B1 — Parasuraman & Manzey (2010) full text not open-access (UNVERIFIED)

The DOI does not resolve to an open-access copy. The paper exists (PubMed abstract confirmed) and is a seminal foundational reference, but exact definition wording cannot be confirmed. The claim as written ("well-documented tendency to weight machine output more heavily than competing signals") is a standard paraphrase of the automation bias concept and unlikely to be contested.

**Author's Prudence Principle recommendation:** Keep the claim but soften the framing to "well-documented tendency" (already done) and do not present the paraphrase as a direct quote. Add "(Parasuraman & Manzey, 2010)" as an inline citation. This is the standard academic convention for established concepts.

---

## Actionable Suggestions

| # | Location | Current Text | Suggested Change | Rationale | Decision |
|---|----------|-------------|-----------------|-----------|----------|
| 1 | Anywhere K1 appears (problem framing section or bias section) | `Andrej Karpathy coined the term "vibe coding" in early 2025: "You just see stuff, say stuff, run stuff, and copy stuff, and it mostly works."` | `Andrej Karpathy introduced the term "vibe coding" in early 2025, describing a mode of development where you prompt, run, and ship without deeply understanding the code.` | The exact quote cannot be verified without X login. The paraphrase captures the concept accurately. Author's Prudence Principle: remove direct quote, retain attribution. | **Accept** (author 2026-04-12) |
| 2 | Bias justification section | Any phrasing that implies Parasuraman & Manzey defined automation bias with the exact wording used | Add parenthetical inline citation: `automation bias — the tendency to weight machine output more heavily than competing signals (Parasuraman & Manzey, 2010)` — no direct quote marks | The paraphrase is accurate but presenting it without citation creates attribution ambiguity. The inline citation covers the reference; no full-text access is needed for a well-established concept. | **Accept** (author 2026-04-12) |
| 3 | pmacros intro + any mention of `<asin>` or `<soltree>` | Any phrasing implying these macros are shipped or current features of pmacros | Replace with: "the default macros I am proposing for pmacros" or "macros I intend to include as defaults" — every instance. | M4 is UNVERIFIED-BY-DESIGN. The macros are described in Article 4 as a contribution to pmacros, not a pre-existing feature. Consistent hedging is required throughout Plan 01 prose. | **Accept** (author 2026-04-12) |

---

## Notes on Non-Flagged Claims

**E1 (Shen & Tamkin):** The 17-percentage-point figure is confirmed. The source uses "17% lower" as a shorthand for the 50%-vs-67% gap. The article's phrasing "17 percentage points lower" is more precise and accurate — no change needed.

**E2 (METR):** Confirmed. Mark as optional (include if word budget allows after primary content). The perception-vs-reality angle complements E1's comprehension angle.

**B2 (Reber & Schwarz):** The processing fluency link to truth judgments is confirmed. The specific application to code review is a well-reasoned adaptation; exploratory framing ("ease of processing is consistently misattributed as evidence of correctness") is accurate and appropriate.

**P1 (CoVe) + P2 (ToT):** Both papers confirmed live. The novelty framing is honest — article should say "`<asin>` adapts the CoVe insight for assumption-surfacing" and "`<soltree>` puts the ToT branching decision in the human's hands." These phrasings do not overclaim.

**M1, M2, M3 (pmacros):** All three claims match verbatim wording in pmacros PROJECT.md Active requirements. No hedging needed; note that all pmacros requirements are still "Active" (none "Validated") — the article's framing as "one concrete way I am operationalizing these defenses" is exactly right and requires no change.

---

## Worked Examples Classification

Per plan instructions, worked examples (`<asin>` rate limiter scenario, `<soltree>` auth decision scenario) will be constructed illustrations, not real captured interactions. The fact-check report classifies these as COMPOSITE by design — they are illustrative, not presented as captured incidents. No Actionable Suggestion is required for COMPOSITE claims that are explicitly framed as illustrations.

---

*Fact-check report generated: 2026-04-12. Status: **approved** (2026-04-12). Plans 01-04 are unblocked.*
