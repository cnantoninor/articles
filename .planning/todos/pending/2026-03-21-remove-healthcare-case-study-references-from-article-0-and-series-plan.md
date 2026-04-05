---
created: 2026-03-21T19:19:21.779Z
title: Remove healthcare case study references from article-0 and series plan
area: docs
files:
  - topics/epistemic_debt/artifacts/articles/article-0-the-epistemic-debt-series.md:127
  - "topics/epistemic_debt/assets/0. series-plan.md:68"
---

## Problem

The healthcare case study ("The Silent Data Loss — Healthcare HL7 validation") was removed from article-3 during Phase 13 because it was not factual. Two stale references remain:

1. `article-0-the-epistemic-debt-series.md` line 127 — the article-3 blurb reads: *"Unwanted incidents: database deletion at scale, 10:1 cost ratio, silent data loss in healthcare."* — remove "silent data loss in healthcare" from this list.
2. `assets/0. series-plan.md` line 68 — entry: *"The Silent Data Loss — Healthcare HL7 validation. Malformed patient identifiers silently dropped..."* — remove this planned case study entry entirely.

## Solution

Edit both files to remove the healthcare references. Article-3 blurb in article-0 should list only the two remaining cases (database deletion and 10:1 cost ratio). Series plan entry should be deleted.
