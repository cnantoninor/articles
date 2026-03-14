---
phase: 13
slug: article-3-when-epistemic-debt-defaults
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-14
---

# Phase 13 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | None — content/editorial phase |
| **Config file** | N/A |
| **Quick run command** | Manual review against section checklist |
| **Full suite command** | Full article read-through against all ART3-XX success criteria |
| **Estimated runtime** | ~5 minutes per review pass |

---

## Sampling Rate

- **After every task commit:** Read the edited section for voice/tone consistency and verify no deferred scope leaked in
- **After every plan wave:** Full article read-through against success criteria checklist
- **Before `/gsd:verify-work`:** All ART3-XX criteria met; Article 2 publication status confirmed; citations verified
- **Max feedback latency:** N/A (manual editorial review)

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 13-01-01 | 01 | 1 | ART3-05 | manual | Read article header — zero TODO markers remain | ✅ article exists | ⬜ pending |
| 13-01-02 | 01 | 1 | ART3-04 | manual | Verify Fragile Experts 77% + Sonar 96%/48%/42% present with citations | ❌ W0: citation gaps | ⬜ pending |
| 13-01-03 | 01 | 1 | ART3-02 | manual | Read "Not Isolated Incidents" — Kiro ≤3 sentences, facts only | ❌ W0: not yet written | ⬜ pending |
| 13-01-04 | 01 | 1 | ART3-03 | manual | Verify 2 formula sidenotes with k, c_k, t₀ fields | ❌ W0: not yet written | ⬜ pending |
| 13-01-05 | 01 | 1 | ART3-01 | manual | Full narrative read for publication quality | ✅ article exists | ⬜ pending |
| 13-01-06 | 01 | 2 | ART3-06 | manual | Read YAML — social_teasers has non-empty values for all 4 platforms | ❌ W0: fields empty | ⬜ pending |
| 13-01-07 | 01 | 2 | ART3-07 | manual | Verify Substack URL resolves; series cross-links updated | ❌ W0: not published | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] Sonar report citation — locate title, year, URL for the 96%/48%/42% figures
- [ ] Amazon Kiro primary source — verify 13h outage, cascading failures, 80% adoption mandate with citation
- [ ] Article 2 publication URL — confirm actual Substack URL before series cross-links can be finalized

*These are research/verification tasks that must complete before dependent content tasks can proceed.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Case studies polished to publication quality | ART3-01 | Subjective editorial judgment | Full narrative read, check voice consistency with Articles 1-2 |
| Amazon Kiro integrated as facts only | ART3-02 | Content judgment — ≤3 sentences, no accountability angle | Read "Not Isolated Incidents" section |
| Formula sidenotes correctly formatted | ART3-03 | Substack rendering must be visually verified | Preview in Substack editor — blockquote with Unicode formulas |
| Industry data with citations | ART3-04 | Citation accuracy requires source verification | Check Fragile Experts + Sonar figures match sources |
| All TODOs resolved | ART3-05 | Grep for TODO/GAP markers in article file | `grep -c 'TODO\|GAP\|QUESTION' article-3*.md` returns 0 |
| Social teasers match exploratory tone | ART3-06 | Tone judgment per platform conventions | Read each teaser, verify matches publication.md rules |
| Article live with cross-links | ART3-07 | External system (Substack) publication | Load URL, verify rendering and series navigation |

---

## Validation Sign-Off

- [ ] All tasks have manual verify instructions mapped
- [ ] Sampling continuity: every task commit gets a section read-through
- [ ] Wave 0 covers all citation/source gaps
- [ ] No automated test infrastructure needed (editorial phase)
- [ ] `nyquist_compliant: true` set in frontmatter
- [ ] Feedback latency acceptable for manual review

**Approval:** pending
