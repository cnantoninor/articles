---
globs: topics/**/artifacts/articles/**
paths: topics/**/artifacts/articles/**
description: "Fact-checking requirements and classification framework for article publication"
alwaysApply: false
---

# Fact-Checking Requirements

## Pre-Publication Gate

No article may move to `status: published` without a completed fact-check report at:
`topics/<topic>/artifacts/articles/<article-slug>-fact-check-report.md`

When planning article publication phases (GSD or otherwise), fact-checking is always **Plan 00** — it runs first, and all subsequent editing plans depend on its output.

## What Gets Checked

Every article must have the following verified before publication:

- **Statistics and data points** — exact figures traced to primary sources
- **Case study details** — names, dates, timelines, outcomes verified against original reporting
- **Academic references** — paper existence, correct attribution, URL accessibility
- **Industry reports** — figures match the source document, not secondary coverage
- **Named concepts** — attribution is accurate (who coined it, where it appeared)
- **Multipliers and ratios** — source language matches the claim strength

## Claim Classification Framework

| Rating | Meaning |
|--------|---------|
| VERIFIED | Claim matches primary source accurately |
| OVERSTATED | Source exists but claim is stronger than what source says — note the actual source language |
| REFRAMED | Source exists but the article reinterprets it in a way that may not be supported |
| OPINION-AS-FACT | An interpretation or editorial judgment presented as established fact |
| INCORRECT | Data point is wrong or misattributed — provide correction |
| UNVERIFIED | Cannot find primary source to confirm — may be true but unverifiable online |
| COMPOSITE | Constructed/hypothetical scenario presented as a real incident |

## Report Template

See `templates/fact-check-plan.md` for the reusable GSD plan template.

The fact-check report itself follows this structure:

```
# [Article Title] — Fact-Check Report

**Date:** YYYY-MM-DD
**Article:** [title]
**Scope:** All factual claims, statistics, case studies, and data points

## Executive Summary
[X verified, Y flagged, Z unverified — overall assessment]

## [Section per claim category: Case Studies, Statistics, References, etc.]
| Claim | Rating | Source | Notes |
|-------|--------|--------|-------|

## Critical Findings
[Items that MUST be addressed before publication]

## Actionable Suggestions
[Each suggestion is a concrete, numbered item the author can accept, reject, or modify]

| # | Location | Current Text | Suggested Change | Rationale | Decision |
|---|----------|-------------|-----------------|-----------|----------|
| 1 | Section, ¶ | "exact quote..." | "proposed replacement..." | Why this change | ☐ Accept / ☐ Reject / ☐ Modify |

- Every flagged claim (OVERSTATED, REFRAMED, OPINION-AS-FACT, INCORRECT, COMPOSITE) MUST have at least one actionable suggestion
- UNVERIFIED claims must have a suggestion to either add hedging language or remove the claim
- Suggestions must include the exact current text and a proposed replacement — not vague guidance
```

## Mandatory User Review

The fact-check report is not complete until the author has reviewed and resolved every actionable suggestion. The workflow is:

1. **Report generated** — assistant produces the report with all actionable suggestions
2. **Report presented** — assistant presents findings to the user, highlighting critical items first
3. **User decides** — for each suggestion, the user marks: Accept, Reject (with reason), or Modify (with alternative)
4. **Decisions recorded** — the Decision column in the report is filled in with the user's choices
5. **Edits applied** — only accepted/modified suggestions are applied to the article

The assistant MUST NOT silently apply fact-check corrections. All changes flow through the user's explicit decisions.

## Author's Prudence Principle

The author prefers to **omit data or soften language rather than overstate or risk stating something false**. When in doubt:

- **Remove** unverifiable claims rather than hedging them — absence is better than a hedged falsehood
- **Soften** language to match what the source actually says, not what secondary coverage implies
- **Never** attribute figures to a source without confirming they appear in that source (including full/gated reports)
- **Prefer** verified absolute figures over unverified relative comparisons (e.g., "72% failure rate" over "X× more likely than human code" if the baseline isn't confirmed)
- **Flag** when a claim relies on a single unverified or non-peer-reviewed source — let the author decide whether to keep, hedge, or remove

This principle overrides the instinct to preserve dramatic statistics. A smaller, verified claim is always preferable to a larger, unverified one.

## AI Assistant Guidelines

When editing or reviewing articles:

1. Check whether a fact-check report exists before suggesting the article is ready
2. Cross-reference claims against the report when editing
3. Flag new claims introduced during editing that were not in the original fact-check
4. Do not weaken verified claims — only adjust flagged ones
5. Preserve the author's exploratory tone when hedging unverified claims
6. Apply the Prudence Principle: when a claim is unverified, default to removal or softening rather than creative hedging
7. Never invent parenthetical disclaimers (e.g., "from the full report") to justify unverified figures — if the figure can't be confirmed, remove it
