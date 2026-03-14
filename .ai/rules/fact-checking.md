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

## Recommendations
[Specific edits suggested based on findings]
```

## AI Assistant Guidelines

When editing or reviewing articles:

1. Check whether a fact-check report exists before suggesting the article is ready
2. Cross-reference claims against the report when editing
3. Flag new claims introduced during editing that were not in the original fact-check
4. Do not weaken verified claims — only adjust flagged ones
5. Preserve the author's exploratory tone when hedging unverified claims
