---
marp: true
paginate: true
title: 'SDD Governance Framework: Managing Epistemic Debt at Scale'
status: draft
type: slides
audience:
  - engineering leadership
  - technical leads
target_length: 0
current_length: 0
estimated_reading_time: 30 min
created: 2026-03-14
last_updated: 2026-03-14
style: |
  :root {
    --bg: #0c0e13;
    --bg-light: #141720;
    --bg-card: #1a1d28;
    --text: #e2e8f0;
    --text-dim: #94a3b8;
    --orange: #f97316;
    --blue: #3b82f6;
    --green: #22c55e;
    --red: #ef4444;
    --yellow: #eab308;
    --purple: #a855f7;
  }
  section {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
    font-size: 26px;
    padding: 50px 60px;
  }
  h1 {
    color: var(--orange);
    font-size: 2.2em;
    font-weight: 700;
    border-bottom: none;
  }
  h2 {
    color: var(--orange);
    font-size: 1.5em;
    font-weight: 600;
    border-bottom: 2px solid var(--orange);
    padding-bottom: 8px;
    margin-bottom: 20px;
  }
  h3 {
    color: var(--blue);
    font-size: 1.15em;
    font-weight: 600;
  }
  strong {
    color: var(--orange);
  }
  em {
    color: var(--blue);
  }
  a {
    color: var(--blue);
  }
  code {
    background: var(--bg-card);
    color: var(--green);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.85em;
  }
  pre {
    background: var(--bg-card) !important;
    border: 1px solid #2a2d38;
    border-radius: 8px;
    padding: 20px !important;
  }
  pre code {
    background: transparent;
    color: var(--text);
    font-size: 0.78em;
  }
  table {
    font-size: 0.82em;
    width: 100%;
    border-collapse: collapse;
  }
  th {
    background: var(--bg-card);
    color: var(--orange);
    padding: 10px 14px;
    text-align: left;
    border-bottom: 2px solid var(--orange);
  }
  td {
    padding: 8px 14px;
    border-bottom: 1px solid #2a2d38;
  }
  tr:nth-child(even) td {
    background: var(--bg-light);
  }
  blockquote {
    border-left: 4px solid var(--orange);
    background: var(--bg-card);
    padding: 16px 24px;
    margin: 16px 0;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: var(--text-dim);
  }
  section.title-slide {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.title-slide h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
  }
  section.title-slide h2 {
    border-bottom: none;
    color: var(--text-dim);
    font-size: 1.1em;
    font-weight: 400;
  }
  section.section-break {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.section-break h2 {
    font-size: 2em;
    border-bottom: none;
    color: var(--orange);
  }
  section.section-break h3 {
    font-size: 1.2em;
    color: var(--text-dim);
    font-weight: 400;
  }
  .highlight-box {
    background: var(--bg-card);
    border-left: 4px solid var(--orange);
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
    margin: 12px 0;
  }
  .metric-box {
    background: var(--bg-card);
    border: 1px solid var(--blue);
    border-radius: 8px;
    padding: 12px 16px;
    margin: 8px 0;
    text-align: center;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }
  .col {
    padding: 0;
  }
  footer {
    color: var(--text-dim);
    font-size: 0.6em;
  }
  section::after {
    color: var(--text-dim);
    font-size: 0.7em;
  }
---

<!-- _class: title-slide -->
<!-- _paginate: false -->

# SDD Governance Framework

## Managing Epistemic Debt at Scale

<br>

**Tag → Triangle → Ceremony**

A proposal for structured AI-assisted development governance

<!-- Speaker notes: 30-minute presentation. Goal: get approval for a 3-phase pilot of the governance framework. The audience is technical, somewhat familiar with epistemic debt, comfortable with math. -->

---

## Agenda

1. **The Problem** — Why AI speed creates a comprehension gap
2. **The Framework** — Tag → Triangle → Ceremony pipeline
3. **Worked Examples** — Bloomberg Law: two teams, two dynamics
4. **Observability** — Making epistemic debt measurable
5. **The Ask** — 3-phase rollout proposal

<!-- Speaker notes: Five sections, roughly 6 minutes each. The worked examples are the meat — they ground everything in real sprint dynamics. -->

---

## The Speed–Understanding Gap

<div class="columns">
<div class="col">

### 2020

> Ask an engineer why their code works:
> *"I chose this algorithm because..., implemented it this way because..."*

Understanding derives from **authorship**.

</div>
<div class="col">

### 2025

> Ask an engineer why their code works:
> *"The LLM suggested it, the tests pass, looks good."*

Understanding must be **actively established**.

</div>
</div>

<br>

**Same confidence. Different warrant.**

<!-- Speaker notes: Start with this contrast. The shift from construction to curation means understanding no longer comes for free — it has to be engineered into the workflow. -->

---

## What is Epistemic Debt?

| Technical Debt | Epistemic Debt |
|---|---|
| Works but hard to **change** | Works but nobody **understands** |
| Future maintenance cost | Future comprehension cost |
| Visible in code structure | **Invisible until crisis** |
| Linear accumulation | **Exponential** with LLM velocity |

<br>

Formally: $E_d = \sum_k \int_0^T \bigl(C_{s,k}(t) - G_{c,k}(t)\bigr)\, dt$

Where $C_{s,k}(t)$ = system complexity at layer $k$, $G_{c,k}(t)$ = cognitive grasp at layer $k$

<!-- Speaker notes: Ed is the integral of the gap between system complexity and team understanding, summed across abstraction layers. When LLMs generate faster than teams comprehend, this integral grows — silently. -->

---

## The Layers Where Debt Hides

| Layer | What Goes Wrong | Recovery Cost |
|---|---|---|
| **L4** Requirements | Intent misalignment — built the wrong thing | **30–70×** |
| **L3** Architecture | Structural misfit — wrong abstractions | **~10×** |
| **L2** Design | Implementation approach — wrong patterns | **3–6×** |
| **L1** Implementation | Code-level gaps — bugs, edge cases | **~1×** |

<br>

Recovery at layer $k$ triggers rework at **all underlying layers**.

An L4 gap caught after release costs **30–70×** more than catching it during requirements.

<!-- Speaker notes: These multipliers come from Boehm's Cost of Change Curve, validated across decades of software projects. The key insight: LLMs accelerate L1 work but do nothing for L4–L3 comprehension. -->

---

## The Net Benefit Condition

AI-assisted development is a net positive **only when:**

$$\text{Net benefit} = \delta - \sum_k c_k \cdot \tau_k$$

Where:
- $\delta$ = time saved by AI-assisted velocity
- $c_k$ = recovery cost multiplier at layer $k$
- $\tau_k$ = recovery time for epistemic gaps at layer $k$

<br>

When $\sum_k c_k \cdot \tau_k > \delta$, the team is **losing time to epistemic debt recovery faster than AI saves it.**

<!-- Speaker notes: This is the formula that grounds the entire proposal. Every framework decision we make is about minimizing the right side of this equation — catching gaps early where c_k is low, not late where it's 30-70x. -->

---

## Our Reality

| Dimension | Our Reality | Implication |
|---|---|---|
| **AI coding agents** | Majority Claude Code, some Cursor | Can standardize tooling |
| **Brownfield vs greenfield** | ~80% brownfield | Tool must handle existing codebases |
| **Scale** | Hundreds of repos, tens of teams | Rollout friction is the dominant constraint |
| **Developer experience** | ~30% senior, ~70% mid/junior | Tool must work without deep prompting expertise |
| **Free cycles** | Limited | Cannot build or maintain a complex meta-tool |

<br>

**The core problem:** Balancing speed, reliability, and epistemic debt — across all of this.

<!-- Speaker notes: These constraints are non-negotiable. Any governance model must work within them. The 70% mid/junior number is the most important — they're the ones most likely to accumulate epistemic debt with LLMs. -->

---

<!-- _class: section-break -->

## The Framework

### Tag → Triangle → Ceremony

---

## The Proposal: Tag → Triangle → Ceremony

```
┌──────────────┐     ┌────────────────────┐     ┌─────────────────────┐
│  Repo Tags   │────→│  Triangle Position  │────→│  GSD Ceremony Level │
│  (Team Lead) │     │  (Derived)          │     │  (Enforced)         │
└──────────────┘     └────────────────────┘     └─────────────────────┘
```

**Three steps:**
1. **Tag** — TLs classify repos on 4 dimensions (once, update as needed)
2. **Derive** — Tags map to a position on the epistemic trade-off triangle
3. **Enforce** — Triangle position determines the required ceremony level

<br>

Untagged repos fall back to sensible defaults → **mid-triangle** (standard ceremony).

<!-- Speaker notes: This is the whole model in one slide. Everything after this is details. The key insight: we're not asking TLs to make ceremony decisions per-ticket — we're asking them to classify repos once, and the ceremony follows automatically. -->

---

## Step 1: Repo Tagging

Team Leads tag repos in `.gsd-policy.yaml` — 4 dimensions:

| Dimension | Values | Default |
|---|---|---|
| **Subdomain** | `core`, `supporting`, `generic`, `spike` | `supporting` |
| **Size** | `small`, `medium`, `large` | `medium` |
| **Codebase** | `greenfield`, `brownfield` | `brownfield` |
| **Clarity** | `clear`, `ambiguous` | `ambiguous` |

```yaml
# .gsd-policy.yaml (repo root)
subdomain: supporting
size: medium
codebase: brownfield
clarity: ambiguous
```

Fully untagged repo → `supporting + medium + brownfield + ambiguous` → **mid-triangle**

<!-- Speaker notes: Defaults are designed to be safe — mid-triangle means standard ceremony. TLs only need to override when a repo is more or less critical than the default. Most repos never need all 4 tags changed. -->

---

## Step 2: Derive Triangle Position

| Subdomain | Small + Clear | Medium or Ambiguous | Large + Ambiguous |
|---|---|---|---|
| **Spike** | upper | upper | mid |
| **Generic** | upper | mid | mid |
| **Supporting** | mid | mid | lower |
| **Core** | mid | lower | lower |

```
              SPEED
                ▲
               / \         ← Upper: accept epistemic debt
              /   \
             / mid \       ← Mid: balanced trade-off
            /       \
           ▼─────────▼
    UNDERSTANDING   RELIABILITY  ← Lower: minimize epistemic debt
```

<!-- Speaker notes: The triangle is the mental model. Upper-triangle repos accept epistemic debt in exchange for speed. Lower-triangle repos invest in understanding because the cascade cost of gaps is too high. Mid is the default. -->

---

## Step 3: Map to Ceremony Level

| Triangle | GSD Ceremony | Phases Required | Who Leads |
|---|---|---|---|
| **Upper** | `/gsd:quick` only | Execute | Any developer |
| **Mid** | Standard | Discuss → Plan → Execute | TL specs, dev executes |
| **Lower** | Full | Discuss → Plan → Execute → Verify | TL mandatory all phases |

<br>

**The key principle:** Ceremony scales with cascade cost.

- Upper-triangle: L1 gaps cost ~1× → minimal ceremony is rational
- Lower-triangle: L3–L4 gaps cost 10–70× → full ceremony pays for itself

<!-- Speaker notes: This is where the framework connects to the cost model. We're not adding ceremony for its own sake — we're investing ceremony where the ROI is highest, based on the recovery cost multipliers. -->

---

## Why One Tool, Not Four?

| | Single Tool (GSD) | Meta-Tool (route to N tools) |
|---|---|---|
| **Adoption friction** | Learn one thing | Learn routing logic + N tools |
| **Maintenance burden** | Zero (upstream maintains) | Permanent (we own the glue) |
| **Training cost** | One curriculum | N curricula + decision framework |

<br>

**The decisive question:** Which tool can *modulate ceremony*?

| Tool | Can it modulate? | How? |
|---|---|---|
| **GSD** | **Yes** | `/quick` (upper) ↔ full workflow (lower) |
| Spec-Kit | Poorly | Same ~800-line ceremony for everything |
| OpenSpec | Somewhat | Lightweight default, no heavy mode |
| BMAD | Poorly | Always heavy, no lightweight mode |

<!-- Speaker notes: GSD is the only tool that explicitly scales ceremony up AND down. This maps directly to our governance model. The others are either always light or always heavy — they can't modulate across the triangle. -->

---

## TL-Led Workflow: Tiered Self-Service

| Triangle | TL Involvement | Junior | Mid | Senior |
|---|---|---|---|---|
| **Upper** | None | Self-serve `/quick` | Self-serve | Self-serve |
| **Mid** | Specs only | Execute only | Graduated self-serve | Full self-serve |
| **Lower** | All phases | Execute only | Execute only | Self-serve specs, TL verifies |

<br>

**Why this works:**
- TLs aren't bottlenecked on Generic/Spike work
- Junior developers have guardrails on Core/Supporting subdomains
- Seniors self-serve where their expertise warrants it

<!-- Speaker notes: This prevents the two failure modes: 1) TL becomes a bottleneck gating every task, or 2) juniors run /quick on core subdomains and accumulate L3-L4 debt. The graduation model gives juniors a path to self-service. -->

---

## The Graduation Model

```
Junior Developer Journey
─────────────────────────────────────────────────────────

Step 1  Execute-only on TL-prepared plans (all repos)
  │
  │  After 3 TL-guided cycles
  ▼
Step 2  Self-serve /gsd:quick on upper-triangle repos
  │
  │  After 5 TL-guided cycles
  ▼
Step 3  Self-serve Discuss + Plan on mid-triangle repos
        (TL reviews async)
  │
  │  After 10 cycles with <20% rework rate
  ▼
Step 4  Full self-service on mid-triangle repos
```

**Measurable gates, not vibes.** Rework rate is the objective signal.

<!-- Speaker notes: The 20% rework rate threshold is measurable from GSD artifacts — we can actually track this. It's not a subjective TL assessment. The graduation model scales: as juniors improve, TL capacity is freed up. -->

---

## GSD Workflow Overview

```
┌─────────┐    ┌──────┐    ┌─────────┐    ┌──────────┐
│ Discuss  │───→│ Plan │───→│ Execute │───→│  Verify  │
│ (intent) │    │(arch)│    │ (build) │    │  (check) │
└─────────┘    └──────┘    └─────────┘    └──────────┘
  catches       catches      fresh 200k     catches
  L4 gaps       L3–L2 gaps   contexts       all layers
  (30–70×)      (3–10×)      per task       post-build
```

**Key properties:**
- **Fresh context per task** — 200k tokens, no context rot
- **Atomic commits** — each task = one commit, `git bisect`-friendly
- **Wave-based parallelism** — independent tasks execute simultaneously
- **Artifact trail** — CONTEXT.md, PLAN.md, SUMMARY.md, VERIFICATION.md

<!-- Speaker notes: The fresh context per task is the most underappreciated feature. Context rot — where the LLM's output degrades as its context window fills — is the #1 quality killer in long AI sessions. GSD solves this by spawning fresh 200k-token agents per task. -->

---

## GSD Entity Model → Jira Mapping

| Jira | GSD | Notes |
|---|---|---|
| Project | PROJECT | One root entity per repo |
| Epic | MILESTONE | Versioned release boundary |
| Story / Task | PHASE | Assignable unit of work |
| Sub-task | PLAN task | Executable step within a phase |
| Acceptance Criteria | Success Criteria | Observable truths per phase |
| Definition of Done | VERIFICATION | Gate before merge / advance |
| Sprint | Wave of phases | Time-boxed parallel batch |

<br>

**GSD artifacts live in `.planning/`** — version-controlled alongside the code they describe.

<!-- Speaker notes: The Jira mapping is important for adoption. Teams don't change their Jira workflow — they add GSD as the spec layer underneath. Jira tracks the what and when; GSD tracks the how and why. -->

---

<!-- _class: section-break -->

## Worked Examples

### Bloomberg Law: Two Teams, Two Dynamics

---

## Example 1: Mixed-Seniority Team

**Product:** Bloomberg Law AI Assistant — AI-powered legal research platform

**The team:**
- **Sarah** (TL, senior) — 8 years in legal tech, owns the AI inference pipeline
- **Marco** (mid, 3 years) — graduated past TL-guided discuss on mid-triangle
- **Priya** (junior, 8 months) — execute-only phase, first sprint on comparison engine

**Repo tags:**

| Repo | Subdomain | Triangle | Ceremony |
|---|---|---|---|
| `ai-inference-engine` | core / large / brownfield / ambiguous | **lower** | full |
| `comparison-ui` | supporting / medium / brownfield / ambiguous | **mid** | standard |
| `export-service` | supporting / small / brownfield / clear | **mid** | standard |
| `research-spike-vectordb` | spike / small / greenfield / ambiguous | **upper** | quick |

<!-- Speaker notes: This team has one TL, one graduated mid, and one junior. The repos span the full triangle. Watch how ceremony modulates across them. -->

---

## Example 1: Five Tickets, Three Ceremony Levels

**Epic:** BLAW-1200 — AI-Powered Jurisdiction Comparison

| Ticket | Type | Repo | Triangle | Ceremony |
|---|---|---|---|---|
| BLAW-1201 | Story | `ai-inference-engine` | **lower** | full |
| BLAW-1205 | Story | `export-service` | **mid** | standard |
| BLAW-1210 | Task | `comparison-ui` | **mid** | standard |
| BLAW-1215 | Bug | `ai-inference-engine` | **lower** | debug → quick |
| BLAW-1220 | Spike | `research-spike-vectordb` | **upper** | quick only |

<br>

**Same sprint. Same team. Five different ceremony levels** — all derived from repo tags, not ad-hoc decisions.

<!-- Speaker notes: This is the governance model in action. Sarah doesn't decide ceremony per ticket — the tags decide. She focuses on the work, not the process. -->

---

## Example 1: Discuss Catches an L3 Gap

**BLAW-1201** (core, lower-triangle, full ceremony) — Sarah runs `/gsd:discuss-phase`:

> **GSD:** *"What does 'compare' mean — textual diff, semantic similarity, or structured field-by-field?"*
> **Sarah:** *"Structured field-by-field. Attorneys need to see how specific provisions differ across jurisdictions."*

Then `/gsd:list-phase-assumptions`:

> **GSD:** *"I assume we'll extend the existing CourtOpinion schema with a JurisdictionMapping table..."*
> **Sarah:** *"No — statutes and court opinions are different entity types. We need a new StatuteProvision model."*

<div class="highlight-box">

**L3 architecture gap caught before a single line of code.**
Recovery cost avoided: **~10×** multiplier.

</div>

<!-- Speaker notes: This is the moment that justifies the entire framework. Without the discuss phase, GSD would have built on the wrong data model. The fix at L3 (architecture) after code is written costs ~10x more than catching it here. -->

---

## Example 1: Debug → Quick, Verify Catches L2

**BLAW-1215** (bug, lower-triangle) — Mid-sprint, Docket Key returns duplicates:

```
Sarah: /gsd:debug "Docket Key duplicates for multi-district litigation"
→ Root cause: deduplication uses case_number alone, but MDL cases
  share case_number across transferor and transferee courts.
Sarah: /gsd:quick "Add court_id to deduplication composite key"
→ Fix + test update, one atomic commit. Backlog → Done in-sprint.
```

**BLAW-1201** (core story) — Sarah runs `/gsd:verify-work`:

```
✓ Compare NY vs CA vs TX statute of limitations
✓ Handle jurisdiction with no equivalent provision (graceful N/A)
✓ AI Assistant responds to natural language comparison queries
✗ Chart rendering breaks when provision text exceeds 2000 characters
```

<div class="highlight-box">

**L2 design gap caught before merge.** Recovery cost avoided: **~4×** multiplier.

</div>

<!-- Speaker notes: Two different patterns: the bug used debug-then-quick (lightweight ceremony for a clear fix), while the core story's verify phase caught a design assumption that would have shipped broken. Both demonstrate ceremony paying for itself. -->

---

## Example 1: Epistemic Debt Trace

| Ticket | Triangle | Gaps Caught | When | Cost Avoided |
|---|---|---|---|---|
| BLAW-1201 (Core Story) | lower | L3: wrong data model | **Discuss** | **~10×** |
| BLAW-1201 (Core Story) | lower | L2: chart text overflow | **Verify** | **~4×** |
| BLAW-1215 (Bug) | lower | L1: dedup key incomplete | **Debug** | ~1× |
| BLAW-1220 (Spike) | upper | Not measured | — | N/A (accepted) |
| BLAW-1205, 1210 | mid | None significant | — | — |

<br>

The core story's discuss phase saved an estimated **10× rework multiplier** on an architecture-level misunderstanding — *before planning even began*.

The spike **deliberately accepted** epistemic debt. Upper-triangle. Correct trade-off.

<!-- Speaker notes: This is the data that makes the case. Two gaps caught early, both on lower-triangle repos where the ceremony was mandatory. The spike accepted debt deliberately — that's fine, it's upper-triangle. The mid-triangle tickets had no significant gaps — which is also fine. The framework matched ceremony to risk. -->

---

## Example 2: Senior-Led Search Overhaul

**Developer:** Daniel (senior, 10 years) — search infrastructure specialist, wrote the Boolean parser 4 years ago.

**Epic:** BLAW-1300 — Hybrid Search (Boolean + Natural Language Fusion)

| Repo | Subdomain | Triangle | Daniel's Self-Service Level |
|---|---|---|---|
| `search-engine-core` | core / large | **lower** | Self-serve discuss+plan; TL verifies |
| `search-api-gateway` | supporting / medium | **mid** | Full self-service, no TL gate |
| `search-analytics-dashboard` | generic / small | **upper** | `/quick` only |

<br>

**Key contrast with Example 1:** Daniel runs his own discuss and plan phases. Sarah's role shifts from co-authoring specs to **async review and verification gating**.

<!-- Speaker notes: This example shows the graduation model in practice. Daniel is a senior who has earned full self-service on mid-triangle repos. On lower-triangle, he self-serves the spec phases but the TL still gates verification. The governance model flexes with seniority. -->

---

## Example 2: Even Seniors Catch Their Own Gaps

**BLAW-1301** (core, lower-triangle) — Daniel runs `/gsd:discuss-phase` himself:

> **GSD:** *"I assume the lexical classifier runs before query parsing, operating on the raw input string."*
> **Daniel:** *"Wrong — it must run after tokenization but before parsing. The tokenizer normalizes citation formats, and the classifier needs normalized tokens to distinguish citations from Boolean operators."*

<div class="highlight-box">

**Self-caught L3 gap.** Even a 10-year veteran benefits from forced intent articulation. The discuss phase's value scales with **domain complexity**, not inversely with seniority.

</div>

**BLAW-1305** (bug, lower-triangle) — A 3-year-old parser limit Daniel wrote himself:

> Depth-4 parenthetical limit was a deliberate performance guardrail... documented **nowhere**. This is epistemic debt that **predates LLMs** — a human decision whose rationale was lost.

GSD debug session → recovered **L4-level epistemic debt** at **~30× recovery cost avoided**.

<!-- Speaker notes: Two critical findings: 1) Even deep experts have assumptions that the discuss phase catches — this isn't just a training wheel for juniors. 2) The 3-year-old bug shows that epistemic debt isn't exclusively an LLM problem — LLMs accelerate it, but structured workflows can recover pre-existing debt too. The debug artifact converted "a decision nobody remembered" into a documented, searchable rationale. -->

---

## Examples Comparison

| Dimension | Example 1 (Mixed Team) | Example 2 (Senior-Led) |
|---|---|---|
| **TL in discuss** | Co-authors CONTEXT.md | Reviews async |
| **TL in plan** | Co-authors PLAN.md | Approves/rejects async |
| **TL in verify** | Runs UAT directly | Lower-triangle only |
| **Junior self-service** | Execute only | N/A |
| **Mid self-service** | Quick + graduated discuss | N/A |
| **Senior self-service** | N/A | Full on mid; specs on lower |
| **Ceremony overhead** | Higher (TL synchronous) | Lower (TL async) |
| **Throughput bottleneck** | TL availability | Review queue |

<br>

**Same framework, different dynamics.** The governance model adapts to team composition — it doesn't impose a one-size-fits-all process.

<!-- Speaker notes: This slide drives home the adaptability of the framework. Same tags, same triangle, same ceremony levels — but the human dynamics are completely different. The framework provides structure; the graduation model provides flexibility. -->

---

<!-- _class: section-break -->

## Observability

### Making Epistemic Debt Measurable

---

## Making Epistemic Debt Visible

GSD artifacts are **epistemic debt sensors** — they produce observable proxies for team understanding:

| GSD Artifact | What It Measures | Epistemic Layer |
|---|---|---|
| **CONTEXT.md** depth | Intent articulation quality | L4 (Requirements) |
| **PLAN.md** checker rejections | Ambiguity caught at design time | L3–L2 (Arch/Design) |
| **Atomic commits** vs rework | First-pass understanding | L2–L1 (Design/Impl) |
| **VERIFICATION.md** outcomes | Circular validation detection | All layers |
| `/quick` on lower-triangle repos | **Policy violations** | Governance health |

<br>

**Key insight:** We can't directly measure $G_{c,k}(t)$ (team cognitive grasp). But GSD artifacts let us detect when the gap $C_{s,k}(t) - G_{c,k}(t)$ is growing.

<!-- Speaker notes: This is the observability play. We're not asking developers to self-report understanding — we're mining the artifacts that structured workflows produce. The data is already there; we just need to aggregate it. -->

---

## Leading vs Lagging Indicators

<div class="columns">
<div class="col">

### Leading (Preventive)

- Low discuss depth on **core** subdomain
  → *Intervene before code is written*

- High plan rejection rate
  → *Ambiguity is being caught (good!)*

- Phase skips on lower-triangle repos
  → *Policy non-compliance detected*

</div>
<div class="col">

### Lagging (Detective)

- High rework commit ratio
  → *L1/L2 gaps already manifested*

- Low UAT pass rate despite green CI
  → *Circular validation detected*

- Incident root cause: "nobody understood this code"
  → *Epistemic debt default event*

</div>
</div>

<br>

**Leading indicators let us act *before* the cascade cost is paid.** Lagging indicators confirm the model is working (or isn't).

<!-- Speaker notes: The leading vs lagging distinction is critical. Leading indicators fire before code is written — we can still intervene cheaply. Lagging indicators fire after the damage is done — they're useful for calibration but not prevention. The goal is to drive leading indicator coverage up. -->

---

## The Epistemic Debt Observatory

```
┌─────────────────────────────────────────────────────────────────┐
│  EPISTEMIC DEBT OBSERVATORY                          Sprint 14 │
├──────────────────────┬──────────────────────────────────────────┤
│  LEADING INDICATORS  │  LAGGING INDICATORS                      │
│                      │                                          │
│  Discuss Depth       │  Rework Ratio        ████░░░░ 34%        │
│  by subdomain:       │  (target: <20%)                          │
│  Core:    ████████   │                                          │
│  Support: █████░░░   │  UAT Pass Rate       ██████░░ 71%        │
│  Generic: ██░░░░░░   │  (target: >85%)                          │
│                      │                                          │
│  Plan Rejections     │  Recovery Cost Estimate                  │
│  This sprint: 12     │  L4 events: 0 (good)                     │
│  (healthy: >0)       │  L3 events: 2 (~20× hours)               │
│                      │  L2 events: 8 (~4× hours)                │
│  Phase Compliance    │  L1 events: 31 (~1× hours)               │
│  Lower: 94%          │                                          │
│  Mid:   87%          │  /quick on lower-triangle: 3 repos ⚠️    │
│  Upper: N/A          │  Phase skips on mid: 7 instances ⚠️      │
└──────────────────────┴──────────────────────────────────────────┘
```

<!-- Speaker notes: This is a sketch of what the dashboard could look like. The left panel shows leading indicators — things we can act on now. The right panel shows lagging indicators — things that already happened. The warning icons on policy violations are the governance teeth — they tell us where teams are bypassing ceremony. The playground has an interactive version of this. -->

---

## The Cognitive Ratchet

A **commit-time understanding gate** — scaled by triangle position:

| Triangle | Ratchet Mechanism | What the Developer Must Show |
|---|---|---|
| **Lower** | Verify phase | Articulate *why* the implementation satisfies requirements — not just that tests pass |
| **Mid** | Plan review | TL confirms the developer understands the plan before execution |
| **Upper** | None | Epistemic debt is an accepted trade-off |

<br>

**The ratchet prevents the Circular Validation Trap:**

```
    LLM Code ──→ LLM Tests ──→ "Verified" ──→ ← Ratchet breaks this
        ↑              ↓                          loop by requiring
        └──────────────┘                          human articulation
         Same blind spots
```

<!-- Speaker notes: The cognitive ratchet is GSD's defense against circular validation — where LLMs test LLM code and everything looks green. The verify phase forces a human to explain the implementation, not just check boxes. This only applies to lower-triangle repos where the stakes justify the overhead. -->

---

<!-- _class: section-break -->

## The Ask

### A Proposal, Not a Mandate

---

## 3-Phase Rollout

### Phase 1: Pilot (4 weeks)
- Select **3–5 repos** across triangle positions (1 core, 2 supporting, 1–2 generic/spike)
- TLs tag repos, team uses GSD at prescribed ceremony levels
- Collect artifact metrics from day one

### Phase 2: Measure (2 sprints)
- Compare rework rates, UAT pass rates, discuss depth ratios
- Identify where ceremony felt like waste vs. where it caught gaps
- Survey developer experience (too heavy? too light? just right?)

### Phase 3: Expand
- Refine tag defaults based on pilot data
- Roll out to remaining teams with updated playbook
- Stand up the Epistemic Debt Observatory dashboard

<br>

**Pilot cost:** ~2 hours of TL time per repo for initial tagging + first discuss cycle.

<!-- Speaker notes: The ask is deliberate and low-risk. 3-5 repos, 4 weeks, measurable outcomes. We're not asking to transform the org — we're asking to test the model on a small scale and let the data make the case for expansion. The 2-hour TL cost estimate is realistic: 30 min to tag, 90 min for first TL-led discuss. -->

---

## Questions?

<br>

**Resources:**
- Source document: `sdd-epistemic-debt.md` (governance model + worked examples)
- GSD entity model: `gsd-class-diagram.md` (Jira mapping + workflows)
- Interactive playground: `sdd-governance-playground.html` (configurator + observatory)

<br>

**Try it now:** The playground lets you configure repo tags and see the derived triangle position, ceremony level, and who leads what — in real time.

<!-- Speaker notes: Direct them to the playground for hands-on exploration. If time permits, do a live demo: pick a repo they know, tag it, and show how the ceremony level follows. Prepare for questions about: 1) "What if TLs don't have time?" — graduation model reduces TL load over time. 2) "Is this too much process?" — upper-triangle repos have zero overhead. 3) "How do we measure success?" — observatory metrics, compare pilot vs control repos. -->
