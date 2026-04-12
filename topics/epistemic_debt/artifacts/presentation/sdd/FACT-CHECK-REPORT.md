---
title: SDD Governance Slides — Fact-Check Report
created: 2026-03-14
scope: sdd-governance-slides.md + sdd-epistemic-debt.md
type: slides
status: review
current_length: 1458
estimated_reading_time: 6 min
---


# Fact-Check Report: SDD Governance Presentation

## Overview

Three independent research agents reviewed the presentation slides against publicly available sources. This report documents every factual issue found, its severity, and the fix applied.

---

## 1. Incorrect Claims

### 1.1 BMAD: "Always heavy, no lightweight mode"

- **Severity:** Incorrect
- **Slide:** "Why One Tool, Not Four?"
- **What the slide said:** BMAD "Poorly" modulates ceremony — "Always heavy; no lightweight mode"
- **What's actually true:** BMAD has an explicit lightweight mode called **Quick Flow** (`bmad-quick-spec` / `bmad-quick-dev`) that skips PRD, Architecture doc, and Epic/Story breakdown entirely. BMAD also has **scale-adaptive routing** across three tracks (Quick Flow → BMad Method → Enterprise) with automatic scope-creep detection and escalation.
- **Source:** [BMAD Quick Flow Documentation](https://docs.bmad-method.org/explanation/quick-flow/), [BMAD GitHub](https://github.com/bmad-code-org/BMAD-METHOD)
- **Fix:** Changed to "Partially — Quick Flow (lightweight) ↔ full Agile + Enterprise tracks, scale-adaptive routing." Reframed GSD's advantage as **policy-driven enforcement** rather than unique modulation capability.
- **Files changed:** `sdd-governance-slides.md`, `sdd-epistemic-debt.md`

### 1.2 OpenSpec: "Lightweight default, no heavy mode"

- **Severity:** Misleading
- **Slide:** "Why One Tool, Not Four?"
- **What the slide said:** OpenSpec "Somewhat" modulates — "Lightweight default, no heavy mode"
- **What's actually true:** OpenSpec has an **expanded workflow profile** that adds `/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:sync`, `/opsx:bulk-archive`, and `/opsx:onboard`. The framework describes itself as "scalable from personal projects to enterprises." It also has Workspaces for multi-repo planning.
- **Source:** [OpenSpec GitHub](https://github.com/Fission-AI/OpenSpec), [OpenSpec on YC](https://www.ycombinator.com/companies/openspec)
- **Fix:** Changed to "Partially — Lightweight default + expanded profile, but no policy-driven enforcement." GSD's advantage reframed around governance integration.
- **Files changed:** `sdd-governance-slides.md`, `sdd-epistemic-debt.md`

### 1.3 GSD framed as "the only tool that explicitly scales ceremony up and down"

- **Severity:** Incorrect (consequence of 1.1 and 1.2)
- **Location:** Source document, Section "Why GSD Over the Others"
- **What it said:** "GSD is the only tool that explicitly scales ceremony up and down"
- **What's actually true:** BMAD and OpenSpec also scale ceremony. GSD's differentiator is **policy-driven enforcement** — repo tags automatically determine ceremony level.
- **Fix:** Changed to "GSD is the tool best suited for policy-driven ceremony modulation" with explanation of how BMAD and OpenSpec compare.
- **Files changed:** `sdd-epistemic-debt.md`

---

## 2. Overstated Claims

### 2.1 Epistemic debt accumulates "Exponentially" vs. "Linear" for tech debt

- **Severity:** Overstated — presented as fact, actually a model prediction
- **Slide:** "What is Epistemic Debt?" (comparison table)
- **What the slide said:** Technical debt has "Linear accumulation" vs. epistemic debt's "**Exponential** with LLM velocity"
- **What's actually true:** This is a theoretical argument from Ngabang (2026, viXra — not peer-reviewed). The directional claim (LLMs widen the gap faster) is supported by multiple sources (Sankaranarayanan 2026/ACM, Chroma Research 2025), but **no study has directly measured or compared accumulation rates**. The "exponential" characterization is derived from model assumptions, not empirical measurement.
- **Fix:** Changed "Exponential" to "**Accelerating** with LLM velocity ¹" with a speaker note footnote explaining the evidence status.
- **Files changed:** `sdd-governance-slides.md`

### 2.2 Boehm multipliers "validated across decades of software projects"

- **Severity:** Overstated
- **Slide:** "The Layers Where Debt Hides" (speaker note)
- **What the speaker note said:** "These multipliers come from Boehm's Cost of Change Curve, validated across decades of software projects."
- **What's actually true:**
  - Boehm's data (1981) measured **temporal phases** (when a defect is found), not **abstraction layers** (what kind of gap). The L1–L4 layer mapping is the author's adaptation, not Boehm's model.
  - The ~10× for L3 (architecture) is **interpolated** — Boehm didn't separate architecture from design.
  - The curve has been **partially validated** (NASA JSC 2010) but also **seriously contested** (Bossavit's *Leprechauns of Software Engineering* 2012; Mountain Goat Software 2026; agile research showing modern practices flatten the curve).
  - The individual multiplier values (30–70×, 3–6×, ~1×) are within Boehm's published ranges for large projects.
- **Sources:** Boehm (1981) p. 40; NASA JSC (2010); Bossavit (2012); Mountain Goat Software (2026)
- **Fix:** Changed speaker note to "adapted from Boehm's Cost of Change Curve (1981; validated by NASA JSC 2010)" with caveats about modern criticism, the layer adaptation, and the ~10× interpolation.
- **Files changed:** `sdd-governance-slides.md`, `sdd-epistemic-debt.md` (added full caveat blockquote)

---

## 3. Missing Attribution / Provenance

### 3.1 Epistemic debt formula presented without source quality context

- **Severity:** Missing context
- **Slide:** "What is Epistemic Debt?"
- **What the slide showed:** The formula $E_d = \sum_k \int_0^T (C_{s,k}(t) - G_{c,k}(t)) dt$ without noting the base formula's provenance.
- **What's actually true:**
  - The **base formula** (without layer decomposition) is from Ngabang (2026), published on **viXra** — a preprint server with no quality review threshold (Wikipedia notes ~15% of viXra papers pass peer review elsewhere).
  - The **layer decomposition** ($\sum_k$) is the author's (Rau's) original extension.
  - The **term "epistemic debt"** originates from Ionescu et al. (2020, Springer — peer-reviewed), applied to smart manufacturing.
- **Fix:** Added "(Ngabang 2026 ³, extended by Rau 2026)" inline, with speaker note footnote explaining viXra's review status and the term's peer-reviewed origin.
- **Files changed:** `sdd-governance-slides.md`, `sdd-epistemic-debt.md`

### 3.2 "Circular validation" presented as established terminology

- **Severity:** Missing context
- **Slide:** "The Cognitive Ratchet"
- **What the slide implied:** "Circular Validation Trap" is a standard term.
- **What's actually true:** The **problem** is widely recognized and well-documented — IBM Research (2025, "Beyond Blind Spots") showed evaluator LLMs failed to detect quality drops in 50%+ of cases. However, the **specific term "circular validation"** is the author's framing. Ngabang uses "Verification Opacity" for a related concept. Other authors use different terms.
- **Fix:** Added "(a widely recognized phenomenon; IBM Research 2025)" to the slide text. Speaker note now credits the term as the author's framing of a documented problem.
- **Files changed:** `sdd-governance-slides.md`, `sdd-epistemic-debt.md`

### 3.3 "Cognitive Ratchet" not flagged as non-peer-reviewed

- **Severity:** Missing context
- **Location:** Slides + source document
- **What's actually true:** The Cognitive Ratchet concept is from Ngabang (2026, viXra — not peer-reviewed). The underlying concern it addresses is well-documented, but the specific mechanism hasn't been through academic review.
- **Fix:** Added "(Ngabang 2026, viXra preprint — not peer-reviewed)" attribution in both files.
- **Files changed:** `sdd-governance-slides.md`, `sdd-epistemic-debt.md`

---

## 4. Claims Verified as Accurate

| Claim | Verdict | Source |
|---|---|---|
| Boehm L4 multiplier: 30–70× | **Within range** (Boehm cites up to 100× for large projects) | Boehm (1981), NASA JSC (2010) |
| Boehm L2 multiplier: 3–6× | **Matches** Boehm's design-phase numbers | Boehm (1981) |
| Boehm L1 multiplier: ~1× | **Accurate** for same-phase detection | Boehm (1981) |
| GSD `/quick` ↔ full workflow modulation | **Confirmed** | GSD GitHub, The New Stack, codecentric.de |
| GSD fresh 200k-token contexts per task | **Confirmed** | GSD GitHub, multiple independent reviews |
| GSD atomic commits / wave-based parallelism | **Confirmed** | GSD GitHub |
| Spec-Kit ~800-line ceremony overhead | **Confirmed** | Hashrocket comparison, GitHub Issue #1174 |
| "Context rot" as established concept | **Confirmed** — well-researched | Chroma Research (2025): 18 frontier models tested |
| "Epistemic debt" as established term | **Confirmed** — coined 2020, peer-reviewed | Ionescu et al. (2020, Springer) |
| Bloomberg Law examples | **Intentionally fictional** — now marked as such | Author confirmation |

---

## 5. Assumptions Made Explicit

### Author's assumptions (not verified — internal data)

- "~80% brownfield" org profile
- "~30% senior, ~70% mid/junior" developer experience distribution
- "Majority Claude Code, some Cursor" tooling reality
- "Hundreds of repos, tens of teams" scale
- Graduation model thresholds (3, 5, 10 cycles; <20% rework rate) are proposed, not empirically derived

### Author's methodological assumptions

- Boehm's temporal-phase cost curve maps meaningfully onto abstraction layers (L1–L4)
- Ceremony modulation is the decisive differentiator for SDD tool selection (weakened by BMAD also having multi-track modulation)
- Policy-driven enforcement (`.gsd-policy.yaml`) is more valuable than manual ceremony selection
- The net benefit formula ($\delta - \sum_k c_k \cdot \tau_k$) is a useful framing even though its terms can't be precisely measured

### Reviewer's assumptions

- Tool documentation and GitHub repos accurately reflect shipped capabilities
- The "Our Reality" slide describes the author's actual organization
- The GSD entity model → Jira mapping is a proposal, not a claim about existing integration

---

## 6. Sources Added

The following references were added to `sdd-epistemic-debt.md` to support the corrections:

- Ionescu, T.B. et al. (2020). "Epistemic Debt." *Springer, AHFE 2019*. — Original coinage
- Sankaranarayanan, S. (2026). "Mitigating Epistemic Debt." *arXiv* (accepted ACM L@S '26). — Empirical evidence
- IBM Research (2025). "Beyond Blind Spots." *arXiv*. — Circular validation evidence
- Chroma Research (2025). "Context Rot." — Empirical LLM degradation study
- Boehm, B. (1981). *Software Engineering Economics*. — Original cost curve
- NASA JSC (2010). "Error Cost Escalation." — Independent validation
- Bossavit, L. (2012). *The Leprechauns of Software Engineering*. — Cost curve critique
