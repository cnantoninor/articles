---
phase: XX-PHASE-SLUG
plan: 00
type: execute
wave: 0
depends_on: []
files_modified:
  - topics/TOPIC/artifacts/articles/ARTICLE-SLUG-fact-check-report.md
autonomous: true
requirements: []

must_haves:
  truths:
    - "Every factual claim, statistic, and data point in the article draft is individually verified against primary sources via online research"
    - "Claims that cannot be verified are flagged with a confidence rating and explanation"
    - "Opinions or interpretations presented as facts are identified and flagged"
    - "Overstated claims (stronger than the source supports) are identified with the actual source language"
    - "Data points that are incorrect, misinterpreted, or taken out of context are flagged with corrections"
    - "A structured fact-check report is produced that subsequent plans use during editing"
  artifacts:
    - path: "topics/TOPIC/artifacts/articles/ARTICLE-SLUG-fact-check-report.md"
      provides: "Comprehensive fact-check report"
      contains: "Verification status for every claim"
---

<objective>
Deep online research fact-check of every factual claim, statistic, case study detail, and data point in ARTICLE_TITLE's draft. Produce a structured report that categorizes each claim using the classification framework. This report feeds into Plan 01's content editing.

Purpose: Ensure the article publishes with factual integrity. Every specific number, attribution, and case study must be traceable to a primary source, and the framing must not overstate what the source actually says.
Output: A fact-check report at topics/TOPIC/artifacts/articles/ARTICLE-SLUG-fact-check-report.md
</objective>

<execution_context>
@/home/arau6/.claude/get-shit-done/workflows/execute-plan.md
@/home/arau6/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
<!-- Add phase-specific context files here -->
<!-- @.planning/phases/XX-PHASE-SLUG/XX-CONTEXT.md -->
<!-- @.planning/phases/XX-PHASE-SLUG/XX-RESEARCH.md -->

<!-- The article draft to fact-check -->
<!-- @topics/TOPIC/artifacts/articles/ARTICLE-SLUG.md -->
</context>

<tasks>

<task type="auto">
  <name>Task 1: Deep online research fact-check of all article claims</name>
  <files>topics/TOPIC/artifacts/articles/ARTICLE-SLUG-fact-check-report.md</files>
  <action>
Read the full article draft. Identify EVERY factual claim, statistic, case study detail, and data point (including any TODO/GAP blocks that contain claims to be integrated later).

For each claim, perform deep online research to verify against primary sources.

**What to check:**
- Statistics and exact figures — trace to the original study/report
- Case study details — names, dates, timelines, outcomes
- Academic references — paper existence, correct attribution, DOIs/URLs
- Industry reports — figures match the source, not secondary coverage
- Named concepts — accurate attribution
- Multipliers, ratios, percentages — source language vs article language

**Classification framework:**

| Rating | Meaning |
|--------|---------|
| VERIFIED | Claim matches primary source accurately |
| OVERSTATED | Source exists but claim is stronger than what source says — note the actual source language |
| REFRAMED | Source exists but the article reinterprets it in a way that may not be supported |
| OPINION-AS-FACT | An interpretation or editorial judgment presented as established fact |
| INCORRECT | Data point is wrong or misattributed — provide correction |
| UNVERIFIED | Cannot find primary source to confirm — may be true but unverifiable online |
| COMPOSITE | Constructed/hypothetical scenario presented as a real incident |

**Report structure:**

```markdown
# [Article Title] — Fact-Check Report

**Date:** YYYY-MM-DD
**Article:** [title]
**Scope:** All factual claims, statistics, case studies, and data points

## Executive Summary
[X verified, Y flagged, Z unverified — overall assessment]

## [Organized by claim category]
| Claim | Rating | Source | Notes |
|-------|--------|--------|-------|

## Critical Findings
[Items that MUST be addressed before publication]

## Recommendations
[Specific edits suggested based on findings]
```

Use WebSearch and WebFetch to access primary sources. For academic papers, check arxiv, Google Scholar, and publisher sites. For industry reports, check the company websites directly. For news stories, check the original reporting.

Be thorough and skeptical. The goal is to catch problems BEFORE publication, not to confirm what the article already says.
  </action>
  <verify>
    <automated>test -f topics/TOPIC/artifacts/articles/ARTICLE-SLUG-fact-check-report.md && echo "PASS: Fact-check report created" || echo "FAIL: Report not found"</automated>
    Additionally verify:
    - Every claim from the article appears in the report
    - Each claim has a rating from the classification framework
    - Sources are cited for verified claims
    - Critical findings section is present
  </verify>
  <done>
    Comprehensive fact-check report produced covering every factual claim. Each claim rated using the classification framework. Primary sources accessed via online research. Critical findings identified for resolution in subsequent plans.
  </done>
</task>

</tasks>

<verification>
- Every factual claim in the article draft is covered in the report
- Each claim has a clear verification rating
- Primary sources are cited for verified claims
- Overstated claims include the actual source language for comparison
- Opinion-as-fact instances are identified with explanation
- All reference URLs are checked for accessibility
- Critical findings section summarizes must-fix items
</verification>

<success_criteria>
A complete fact-check report exists that covers every factual claim in the article draft. Subsequent plans can reference this report to ensure the article only publishes verified claims, properly hedges unverified claims, and corrects any inaccuracies.
</success_criteria>

<output>
After completion, create `.planning/phases/XX-PHASE-SLUG/XX-00-SUMMARY.md`
</output>
