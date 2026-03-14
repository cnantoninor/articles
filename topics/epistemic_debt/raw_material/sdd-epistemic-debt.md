# SDD Tool Standardization: From Comparison to Governance

> **Last updated:** March 2026
> **Audience:** AI Enablement Team, Engineering Leadership
> **Status:** Recommendation draft for review
> **Scope:** Free, open-source SDD frameworks only. Excludes paid tools (Kiro, Intent), IDE-specific tools (Cursor .cursorrules), and coding agents that *host* these frameworks (Aider, Cline, Claude Code itself).

---

## Table of Contents

1. [Organizational Context & Assumptions](#organizational-context--assumptions)
2. [Tool Profiles](#tool-profiles)
3. [Comparison Dimensions](#comparison-dimensions)
4. [Why One Tool, Not Four](#why-one-tool-not-four)
5. [Recommendation: GSD as Org-Wide Standard](#recommendation-gsd-as-org-wide-standard)
6. [Governance Model: Tag → Triangle Position → Ceremony Level](#governance-model)
7. [TL-Led Workflow: Who Runs What](#tl-led-workflow-who-runs-what)
8. [Epistemic Debt Observability via GSD Artifacts](#epistemic-debt-observability-via-gsd-artifacts)
9. [GSD + Cursor: Bridging the Gap](#gsd--cursor-bridging-the-gap)
10. [Decision Matrix (Reference)](#decision-matrix-reference)
11. [When to Use No SDD Tool](#when-to-use-no-sdd-tool)
12. [Sources](#sources)

---

## Organizational Context & Assumptions

This document is written for an organization with these characteristics. If these change, revisit the recommendation.

| Dimension | Our Reality | Implication |
|---|---|---|
| **AI coding agents** | Majority Claude Code, some Cursor. Can be enforced. | Host lock-in is a soft constraint, not a dealbreaker |
| **Brownfield vs greenfield** | ~80% brownfield | Tool must handle existing codebases well |
| **Scale** | Hundreds of repos, tens of teams | Rollout friction is the dominant constraint |
| **Developer experience** | ~30% senior, ~70% mid/junior | Tool must work without deep prompting expertise |
| **Free cycles for tooling** | Limited | Cannot build or maintain a complex meta-tool |
| **Repo tagging** | Net-new governance overhead. Untagged repos fall back to a default. | Default must be sensible — mid-triangle |
| **Tagging & rollout ownership** | Team Leads | Distributed responsibility, not centralized bottleneck |
| **Core problem** | Balancing speed, reliability/maintainability, and epistemic debt | SDD tool is the "Structured Workflow" amplifier on the epistemic trade-off triangle |

### What We Mean by Epistemic Debt

Epistemic debt is **code that works but nobody understands**. Unlike technical debt (code that works but is hard to *change*), epistemic debt is invisible until crisis — and LLMs accelerate its accumulation at scale because they generate working code faster than teams can comprehend it.

Formally (per Ngabang 2026, Rau 2026):

```
Ed = Σₖ ∫₀ᵀ (Cs,k(t) - Gc,k(t)) dt
```

Where `Cs,k(t)` is system complexity at layer k, `Gc,k(t)` is cognitive grasp at layer k, and k indexes: L4 (requirements), L3 (architecture), L2 (design), L1 (implementation).

**Why this matters for SDD tool selection:** An SDD tool is not just a productivity framework. It is the primary mechanism for keeping `Gc(t)` growing at a rate that tracks `Cs(t)` — i.e., for preventing epistemic debt accumulation during AI-assisted development.

---

## Tool Profiles

### GSD (Get Shit Done)

| | |
|---|---|
| **License** | MIT |
| **GitHub Stars** | ~30k |
| **Primary Hosts** | Claude Code, OpenCode, Gemini CLI, Codex. Community adapter for Cursor. |
| **Install** | `npx get-shit-done-cc@latest` |

**Philosophy:** "The complexity is in the system, not in your workflow." GSD rejects enterprise ceremony in favor of invisible orchestration behind simple slash commands. Purpose-built to solve *context rot* — the quality degradation that occurs as an LLM fills its context window.

**Workflow:**

1. **New Project** (`/gsd:new-project`) — Guided vision capture, 4 parallel research agents, scoped requirements, phase-based roadmap with approval gate.
2. **Discuss** (`/gsd:discuss-phase N`) — Surfaces implementation gray areas, captures preferences in CONTEXT.md.
3. **Plan** (`/gsd:plan-phase N`) — Researches approaches, produces 2–3 atomic task plans in structured XML, verified against requirements.
4. **Execute** (`/gsd:execute-phase N`) — Wave-based parallel execution: independent tasks in fresh 200k-token contexts, atomic git commit per task.
5. **Verify** (`/gsd:verify-work N`) — Interactive UAT walkthrough, failure diagnosis, fix-plan generation.
6. **Quick Mode** (`/gsd:quick`) — Ad-hoc tasks skipping optional phases while maintaining atomic commits.

**Spec Artifacts:**

- `PROJECT.md` (vision), `REQUIREMENTS.md` (scoped features), `ROADMAP.md` (phases)
- Per-phase: `CONTEXT.md`, `RESEARCH.md`, `PLAN.md` (XML), `SUMMARY.md`, `VERIFICATION.md`
- `STATE.md` (decisions, blockers, current position)
- All stored in `.planning/` directory

**Strengths:** Context rot mitigation (fresh contexts per task), wave-based parallel execution, atomic git commits (`git bisect`-friendly), `/gsd:quick` for lightweight work, `/gsd:map-codebase` for brownfield, flexible phase management.

**Weaknesses:** Primary host is Claude Code (Cursor via community adapter), requires thoughtful discuss-phase input, atomic commits can create noise if granularity is too fine, less suited for pure exploratory spikes.

**Maturity:** High. 30k+ stars. Active development with frequent releases.

---

### GitHub Spec-Kit

| | |
|---|---|
| **License** | MIT |
| **GitHub Stars** | ~77k |
| **Primary Hosts** | Agent-agnostic: Copilot, Claude Code, Gemini CLI, Cursor, Windsurf, 20+ others |
| **Install** | `uv tool install spec-kit` (Python 3.11+) |

**Philosophy:** Intent-driven development where specifications define the *what* before the *how*. Reduces reliance on individual prompting skill by externalizing intent into reviewable, versionable artifacts.

**Workflow:** Constitution → Specify → Plan → Tasks → Implement (with optional `clarify`, `analyze`, `checklist` commands).

**Strengths:** Broadest agent compatibility (20+), constitutional approach for consistent standards, highly portable specs, large community.

**Weaknesses:** High spec overhead (~800+ lines/feature), no context management, markdown proliferation creates review burden, struggles with legacy codebases, no multi-agent orchestration, static specs drift during implementation.

**Maturity:** High. Largest community by stars. Backed by GitHub.

---

### OpenSpec

| | |
|---|---|
| **License** | MIT |
| **GitHub Stars** | ~30k |
| **Primary Hosts** | Agent-agnostic: 20+ AI assistants |
| **Install** | `npx openspec@latest init` (Node.js 20.19+) |

**Philosophy:** "Fluid not rigid, iterative not waterfall, built for brownfield not just greenfield."

**Workflow:** Propose → Plan → Apply → Archive.

**Strengths:** Lowest spec overhead (~250 lines), purpose-built brownfield support with delta markers (ADDED/MODIFIED/REMOVED), token-efficient, very low host lock-in.

**Weaknesses:** Limited greenfield support (no project-level scaffolding), no multi-agent orchestration, no built-in context management, less suited for multi-service initiatives.

**Maturity:** Growing. 30k stars, 50+ contributors.

---

### BMAD-METHOD

| | |
|---|---|
| **License** | MIT |
| **GitHub Stars** | ~41k |
| **Primary Hosts** | Agent-agnostic: Claude Code, Cursor, other AI IDEs |
| **Install** | Node.js v20+, clone from GitHub |

**Philosophy:** Simulates a full agile team with 12+ specialized AI personas (PM, Architect, Developer, QA, etc.) guiding structured process.

**Workflow:** Brainstorming → Analysis → Architecture → UX → Planning → Implementation → Quality (with "Party Mode" for multi-agent sessions).

**Strengths:** Most comprehensive lifecycle coverage, 34+ built-in workflows, role-based access control, extensible module ecosystem, scale-adaptive.

**Weaknesses:** Steepest learning curve (12+ agent roles, YAML config, handoff protocols), highest spec overhead, greenfield-focused, rigid phase transitions, bureaucratic for solo developers.

**Maturity:** Growing. 41k stars, 124 contributors.

---

## Comparison Dimensions

| Dimension | GSD | Spec-Kit | OpenSpec | BMAD |
|---|---|---|---|---|
| **Workflow flexibility** | High (skip with `/quick`) | Medium (fixed 5-step) | High (minimal gates) | Low (rigid SDLC) |
| **Learning curve** | Medium | Low–Medium | Low | High |
| **Spec overhead (lines/feature)** | ~400 | ~800+ | ~250 | Very High |
| **Brownfield support** | Good (`/map-codebase`) | Limited | Excellent (delta markers) | Limited |
| **Greenfield support** | Excellent | Good | Limited | Excellent |
| **Multi-agent orchestration** | Yes (parallel waves) | No | No | Yes (12+ personas) |
| **Context rot mitigation** | Yes (fresh 200k contexts) | No | Partial (token-efficient) | Partial (file handoffs) |
| **Team collaboration** | Medium | High (portable specs) | Medium | High (role separation) |
| **Host lock-in** | Medium (Claude Code primary) | Very Low | Very Low | Low |
| **Ceremony modulation** | Yes (`/quick` ↔ full) | No (always heavy) | Somewhat (light by default) | No (always heavy) |
| **Codebase analysis** | Built-in (`/map-codebase`) | None | None | None |

---

## Why One Tool, Not Four

### The Meta-Tool Temptation

The decision matrix in [Section 10](#decision-matrix-reference) shows that different tools are theoretically optimal for different scenarios. This suggests building a meta-tool that routes to the right SDD tool based on repo tags. **We reject this approach:**

| | Single Tool | Meta-Tool |
|---|---|---|
| **Adoption friction** | Learn one thing | Learn routing logic + N tools |
| **Maintenance burden** | Zero (upstream maintains) | Permanent (we own the glue layer) |
| **Failure modes** | Known tool limitations | Routing bugs + tool bugs + integration bugs |
| **Training cost** | One curriculum | N curricula + decision framework |
| **Flexibility** | Swap tools later if better one emerges | Locked into abstraction layer |

Given **hundreds of repos, tens of teams, 70% mid/junior developers, and limited free cycles**, adoption speed dominates. One tool learned well beats four tools learned poorly.

### Why GSD Over the Others

**The core question is: which tool can modulate ceremony across the epistemic trade-off triangle?**

| Tool | Can it modulate ceremony? | How? |
|---|---|---|
| **GSD** | Yes | `/gsd:quick` (upper triangle) ↔ full workflow (lower triangle) |
| **Spec-Kit** | Poorly | Same ~800-line ceremony for Core and Generic alike |
| **OpenSpec** | Somewhat | Lightweight by default, but no "heavy mode" for Core subdomains |
| **BMAD** | Poorly | Always heavy; no lightweight mode |

**GSD is the only tool that explicitly scales ceremony up and down**, which maps directly to the governance model we need: tag a repo → derive triangle position → enforce corresponding ceremony level.

Additional factors favoring GSD:

| Factor | GSD Advantage |
|---|---|
| **80% brownfield** | `/gsd:map-codebase` analyzes existing code before planning. Spec-Kit and BMAD struggle here. |
| **Context rot** | Only tool with fresh 200k-token contexts per task. Critical for mid/junior devs who produce longer, less focused prompts. |
| **Atomic commits** | Enables `git bisect`, clean reverts, and — crucially — epistemic debt measurement via artifact mining (see [Section 8](#epistemic-debt-observability-via-gsd-artifacts)). |
| **70% mid/junior** | Discuss phase with TL guidance gives structure without requiring deep prompting skill. |
| **Claude Code majority** | Primary host alignment. Cursor teams covered via community adapter. |

**What we give up:** Spec-Kit's 20+ agent portability (acceptable — we can enforce Claude Code). OpenSpec's ultra-lightweight brownfield deltas (GSD's `/quick` is close enough). BMAD's comprehensive SDLC personas (overkill for our brownfield-dominant profile).

---

## Governance Model

### The Pipeline: Tag → Triangle → Ceremony

```
┌──────────────┐     ┌────────────────────┐     ┌─────────────────────┐
│  Repo Tags   │────→│  Triangle Position  │────→│  GSD Ceremony Level │
│  (Team Lead) │     │  (Derived)          │     │  (Enforced)         │
└──────────────┘     └────────────────────┘     └─────────────────────┘
```

### Step 1: Repo Tagging (Team Leads)

Team Leads tag repos with up to 4 dimensions. Untagged dimensions fall back to defaults.

| Dimension | Values | Default (if untagged) |
|---|---|---|
| **Subdomain** | `core`, `supporting`, `generic`, `spike` | `supporting` |
| **Size** | `small`, `medium`, `large` (auto-inferred from GitHub stats possible) | `medium` |
| **Greenfield/Brownfield** | `greenfield`, `brownfield` | `brownfield` |
| **Clarity** | `clear`, `ambiguous` | `ambiguous` |

**Fully untagged repos default to:** `supporting` + `medium` + `brownfield` + `ambiguous` → **mid-triangle**.

### Step 2: Derive Triangle Position

| Subdomain | Small+Clear | Medium or Ambiguous | Large+Ambiguous |
|---|---|---|---|
| **Spike** | upper | upper | mid |
| **Generic** | upper | mid | mid |
| **Supporting** | mid | mid | lower |
| **Core** | mid | lower | lower |

### Step 3: Map to GSD Ceremony Level

| Triangle Position | GSD Ceremony | Phases Required | Who Leads |
|---|---|---|---|
| **Upper** (speed, accept epistemic debt) | `/gsd:quick` only | Execute | Any developer |
| **Mid** (balanced) | Discuss → Plan → Execute | Discuss + Plan: TL. Execute: any dev. | TL for spec phases |
| **Lower** (minimize epistemic debt) | Full: Discuss → Plan → Execute → Verify | All phases: TL leads Discuss/Plan/Verify. Execute: any dev. | TL mandatory |

### Per-Repo Configuration

```yaml
# .gsd-policy.yaml (committed to repo root)
subdomain: supporting     # core | supporting | generic | spike
size: medium              # small | medium | large
codebase: brownfield      # greenfield | brownfield
clarity: ambiguous         # clear | ambiguous

# Derived (computed by governance tooling or manually set)
triangle_position: mid    # upper | mid | lower
ceremony: standard        # quick | standard | full

# Workflow ownership
spec_lead: TL             # who runs discuss/plan/verify phases
```

### Worked Example: GSD × Scrum × Jira in Practice

This subsection grounds the governance model in a concrete, end-to-end sprint narrative. It maps Jira ticket types and swimlane transitions to GSD commands, showing how the abstract pipeline — tag → triangle → ceremony — plays out in a real team's daily workflow.

#### The Setting

**Product:** Bloomberg Law's AI Assistant — a legal research platform serving attorneys, paralegals, and compliance professionals. The platform offers AI-powered case law research, docket search (Docket Key), litigation analytics, and brief analysis across federal and 1,800+ state courts.

**The team:**

- **Sarah** (Team Lead, senior) — 8 years in legal tech, owns the AI Assistant's core inference pipeline. Runs discuss/plan/verify phases for mid- and lower-triangle work.
- **Marco** (mid-level, 3 years) — Full-stack, strong on API design. Has graduated past TL-guided discuss on mid-triangle repos. Self-serves `/gsd:quick` on upper-triangle.
- **Priya** (junior, 8 months) — Frontend-focused, still in the execute-only phase of the graduation model. This is her first sprint touching the comparison engine.

**Repo tags (`.gsd-policy.yaml`):**

| Repo | Subdomain | Size | Codebase | Clarity | Triangle | Ceremony |
|---|---|---|---|---|---|---|
| `ai-inference-engine` | `core` | `large` | `brownfield` | `ambiguous` | **lower** | full |
| `comparison-ui` | `supporting` | `medium` | `brownfield` | `ambiguous` | **mid** | standard |
| `export-service` | `supporting` | `small` | `brownfield` | `clear` | **mid** | standard |
| `research-spike-vectordb` | `spike` | `small` | `greenfield` | `ambiguous` | **upper** | quick |

#### The Epic

**BLAW-1200: AI-Powered Jurisdiction Comparison**
> *As a legal researcher using Bloomberg Law, I need to compare statutes, regulations, and case law across multiple jurisdictions in a side-by-side chart, so I can advise clients on multi-state compliance without switching between separate searches.*

Sarah creates the Epic in Jira during quarterly planning. In GSD terms, this maps to a **milestone** — she runs `/gsd:new-milestone "Jurisdiction Comparison v1"` on the `ai-inference-engine` repo to capture the vision, generate requirements, and produce a phased roadmap. The GSD artifacts (PROJECT.md, REQUIREMENTS.md, ROADMAP.md) become the Epic's living specification — linked from the Jira Epic description.

#### The Tickets

Sarah decomposes the Epic into five tickets during backlog creation:

| Jira ID | Type | Summary | Repo | Triangle | Story Points |
|---|---|---|---|---|---|
| BLAW-1201 | **Story** | Compare statutes across jurisdictions in side-by-side chart | `ai-inference-engine` | lower | 13 |
| BLAW-1205 | **Story** | Export comparison charts to PDF/DOCX | `export-service` | mid | 5 |
| BLAW-1210 | **Task** | Add jurisdiction filter dropdown to AI Assistant UI | `comparison-ui` | mid | 3 |
| BLAW-1215 | **Bug** | Docket Key returns duplicate results for multi-district litigation | `ai-inference-engine` | lower | 5 |
| BLAW-1220 | **Spike** | Evaluate vector similarity approaches for cross-jurisdiction statute matching | `research-spike-vectordb` | upper | 3 |

#### GSD Commands by Ticket Type and Lifecycle Stage

The following reference table maps each Jira ticket type to the GSD commands used at each stage of the swimlane progression. The ceremony level (derived from triangle position) determines which phases are required vs. optional.

| Lifecycle Stage | Epic | Story/Task (Lower) | Story/Task (Mid) | Bug | Spike |
|---|---|---|---|---|---|
| **Ticket Created** (→ Backlog) | `/gsd:new-milestone` | Create ticket, link to GSD phase in ROADMAP.md | Create ticket, link to GSD phase | `/gsd:debug` to investigate root cause; create ticket from findings | Create ticket |
| **Grooming** | Review ROADMAP.md phases, reprioritize | `/gsd:discuss-phase` (TL-led) + `/gsd:list-phase-assumptions` | `/gsd:discuss-phase` (TL or self-serve for graduated mids) | `/gsd:debug` findings → refine acceptance criteria | Minimal — define timebox and question to answer |
| **Sprint Planning** (→ Todo) | N/A (Epics span sprints) | `/gsd:plan-phase` (TL-led) → subtasks auto-generated from PLAN.md tasks | `/gsd:plan-phase` → subtasks from PLAN.md | `/gsd:insert-phase` if fix is multi-task; else `/gsd:quick` | No planning needed — `/gsd:quick` at execution |
| **In Progress** | `/gsd:progress` to track across stories | `/gsd:execute-phase` (dev executes TL-prepared plan) | `/gsd:execute-phase` | `/gsd:execute-phase` or `/gsd:quick` (depending on size) | `/gsd:quick` + `/gsd:research-phase` |
| **Blocked** | Escalation | `/gsd:pause-work` → update STATE.md → move swimlane | `/gsd:pause-work` | `/gsd:debug` (resume investigation) | Spike results inform pivot |
| **Reviewing** | N/A | `/gsd:verify-work` (TL-led UAT) + PR review | `/gsd:verify-work` + PR review | PR review + regression test | Document findings, close spike |
| **Accepted / Done** | `/gsd:audit-milestone` + `/gsd:complete-milestone` | Phase verified, SUMMARY.md written, move to Done | Phase verified, move to Done | Fix verified, move to Done | Findings captured in RESEARCH.md, inform Story grooming |

#### The Sprint: Week by Week

**Sprint Goal:** *Deliver statute comparison for 3 pilot jurisdictions (NY, CA, TX) with basic export.*

---

**Week 1 — Grooming and Sprint Planning**

Sarah starts with the **Spike (BLAW-1220)** because its findings will shape the core Story's approach. Marco picks it up — it's upper-triangle, so he self-serves:

```
Marco runs: /gsd:quick
"Evaluate cosine similarity vs. BM25 hybrid for matching equivalent
statutes across jurisdiction-specific codifications."
```

GSD spawns a planner and executor. Marco explores three approaches, writes findings to `.planning/quick/001-vectordb-spike/SUMMARY.md`, and commits. The Spike moves from **Todo → In Progress → Reviewing → Done** within two days. No discuss or verify phases — upper-triangle ceremony accepts the epistemic debt in exchange for speed.

Meanwhile, Sarah grooms the **core Story (BLAW-1201)**. This is lower-triangle — full ceremony is mandatory:

```
Sarah runs: /gsd:discuss-phase 1
GSD asks: "What does 'compare' mean here — textual diff, semantic
similarity, or structured field-by-field comparison?"
Sarah: "Structured field-by-field. Attorneys need to see how specific
provisions (e.g., statute of limitations, burden of proof) differ
across jurisdictions. Not a raw text diff."
```

The discuss phase produces CONTEXT.md — capturing Sarah's intent, boundaries ("no free-text comparison in v1"), and essentials ("must handle jurisdictions with different codification structures"). She then surfaces assumptions:

```
Sarah runs: /gsd:list-phase-assumptions 1
GSD outputs: "I assume we'll use the existing CourtOpinion schema
and extend it with a JurisdictionMapping table..."
Sarah: "No — statutes and court opinions are different entity types.
We need a new StatuteProvision model."
```

This catches an **L3 (architecture) gap** before a single line of code is written — exactly where the cascade cost multiplier is ~10×. Sarah then plans:

```
Sarah runs: /gsd:plan-phase 1
```

GSD spawns a researcher (reads the spike findings from BLAW-1220), then a planner that produces `01-01-PLAN.md` with 6 atomic tasks. A plan-checker agent verifies the plan against requirements. Sarah reviews, approves, and the tasks become **Subtasks** in Jira under BLAW-1201:

| Subtask | Description | Assigned | Wave |
|---|---|---|---|
| BLAW-1201-1 | Create StatuteProvision data model + migrations | Priya | 1 |
| BLAW-1201-2 | Build jurisdiction mapping ingestion pipeline | Marco | 1 |
| BLAW-1201-3 | Implement comparison engine (field-by-field diff) | Marco | 2 |
| BLAW-1201-4 | Build comparison API endpoint | Priya | 2 |
| BLAW-1201-5 | Integration tests for 3 pilot jurisdictions | Priya | 3 |
| BLAW-1201-6 | AI Assistant chat integration ("compare X across Y") | Marco | 3 |

Wave 1 subtasks have no dependencies between them — GSD will execute them in parallel. Wave 2 depends on Wave 1. Wave 3 depends on Wave 2.

---

**Week 2 — Execution**

Priya and Marco begin executing. Sarah moves BLAW-1201 to **In Progress**.

```
Sarah runs: /gsd:execute-phase 1
GSD groups by wave:
  Wave 1: BLAW-1201-1 (Priya) + BLAW-1201-2 (Marco) → parallel
  Wave 2: BLAW-1201-3 + BLAW-1201-4 → parallel (after Wave 1)
  Wave 3: BLAW-1201-5 + BLAW-1201-6 → parallel (after Wave 2)
```

Each task executes in a **fresh 200k-token context** — this is GSD's context rot mitigation. Priya's data model task doesn't inherit noise from Marco's pipeline work. Each task produces an **atomic git commit**, making `git bisect` possible if something breaks later.

Mid-sprint, a **Bug (BLAW-1215)** surfaces: Docket Key returns duplicate results when a case spans multiple federal districts (multi-district litigation). Sarah investigates:

```
Sarah runs: /gsd:debug "Docket Key duplicates for multi-district litigation"
GSD gathers symptoms, creates .planning/debug/docket-key-duplicates.md
Investigation reveals: the deduplication logic uses case_number alone,
but MDL cases share a case_number across transferor and transferee courts.
```

The debug findings inform the Jira ticket's acceptance criteria. The fix is small enough for `/gsd:quick`:

```
Sarah runs: /gsd:quick
"Add court_id to the deduplication composite key in DocketKeyService.
Update the MDL case test fixtures."
```

BLAW-1215 moves **Backlog → Todo → In Progress → Reviewing → Done** within the sprint. The `/gsd:debug` → `/gsd:quick` path keeps the fix lightweight while the debug session preserves the investigation trail in `.planning/debug/`.

Meanwhile, Marco hits a **blocker** on BLAW-1201-3: the comparison engine needs statute text normalization, but the existing NLP pipeline doesn't handle statutory language well. He pauses:

```
Marco runs: /gsd:pause-work
STATE.md updated: "Blocked on statute text normalization.
Existing NLP pipeline optimized for case law, not statutory language.
Need TL decision: extend pipeline or use separate normalizer."
```

BLAW-1201-3 moves to **Blocked**. Sarah reviews the pause context, decides on a separate normalizer, and Marco resumes. The STATE.md trail means no context is lost — if Marco's context window fills up, `/gsd:resume-work` restores full state.

---

**Weeks 3–4 — Reviewing and Acceptance**

Marco submits the **mid-triangle Task (BLAW-1210)** — the jurisdiction filter dropdown for the AI Assistant UI. This is `comparison-ui` repo, mid-triangle, standard ceremony:

```
Marco ran: /gsd:discuss-phase 2  (self-served — graduated mid)
Marco ran: /gsd:plan-phase 2
Marco ran: /gsd:execute-phase 2
Marco now runs: /gsd:verify-work 2
```

GSD walks through testable deliverables: "Filter shows all 50 states + DC + federal," "Selection persists across chat turns," "Filter resets on new comparison request." Marco confirms each. PR goes up. BLAW-1210 moves **Reviewing → Done**.

For the **core Story (BLAW-1201)**, Sarah runs the full verify — lower-triangle demands it:

```
Sarah runs: /gsd:verify-work 1
GSD presents UAT checklist:
  ✓ Compare NY vs CA vs TX statute of limitations for breach of contract
  ✓ Handle jurisdiction with no equivalent provision (graceful "N/A")
  ✓ AI Assistant responds to "compare statute of limitations across NY, CA, TX"
  ✗ Chart rendering breaks when provision text exceeds 2000 characters
```

The verification catches an **L2 (design) gap** — the chart component assumed short provision text. GSD auto-generates a fix plan. Sarah runs `/gsd:execute-phase 1` again (just the fix task). After re-verification, BLAW-1201 moves to **Reviewing**. PR goes up with the full artifact trail linked: CONTEXT.md, PLAN.md, SUMMARY.md, VERIFICATION.md.

The **Export Story (BLAW-1205)** follows the same mid-triangle flow — Marco discuss → plan → execute → verify. BLAW-1205 moves to **Done**.

---

**Sprint Close**

All tickets are **Accepted/Done**. Sarah checks overall Epic health:

```
Sarah runs: /gsd:progress
GSD shows: Phase 1 ✓, Phase 2 ✓, Quick tasks: 2 completed
Milestone: 100% of v1 scope delivered
```

Since this was the final sprint for the milestone:

```
Sarah runs: /gsd:audit-milestone
GSD spawns integration checker: verifies AI Assistant → comparison engine →
export service E2E flow. Creates MILESTONE-AUDIT.md.

Sarah runs: /gsd:complete-milestone 1.0.0
GSD archives artifacts, creates git tag, updates MILESTONES.md.
```

The Epic BLAW-1200 moves to **Done** in Jira.

#### Epistemic Debt Trace

The worked example illustrates how different ceremony levels produce different epistemic debt profiles:

| Ticket | Triangle | Ceremony Used | Epistemic Gaps Caught | When Caught | Cascade Cost Avoided |
|---|---|---|---|---|---|
| BLAW-1201 (Core Story) | Lower | Full | L3: wrong data model assumption; L2: chart text overflow | Discuss phase; Verify phase | ~10× (L3), ~4× (L2) |
| BLAW-1210 (Mid Task) | Mid | Standard | None significant | — | — |
| BLAW-1215 (Bug) | Lower | Debug + Quick | L1: deduplication key incomplete | Debug phase | ~1× |
| BLAW-1220 (Spike) | Upper | Quick only | Not measured (accepted) | — | N/A (debt accepted) |
| BLAW-1205 (Mid Story) | Mid | Standard | None significant | — | — |

The core Story's discuss phase caught an architecture-level misunderstanding (L3) *before planning even began* — saving an estimated 10× rework multiplier. The verify phase caught a design-level gap (L2) *before merge* — saving a 4× multiplier. The spike deliberately accepted epistemic debt at upper-triangle, which is the correct trade-off for exploratory work that will be revisited when the findings feed into a groomed Story.

#### Worked Example 2: Senior-Led Search Overhaul

The first example showed a mixed-seniority team where the TL gates ceremony for junior and mid-level developers. This second example contrasts that dynamic: a senior developer who self-serves most GSD phases, with the TL involved only on the highest-criticality work. The domain is Bloomberg Law's core search infrastructure — the Boolean and natural-language search engine that underpins every product surface, from court opinion retrieval to legislative research and docket discovery.

**The developer:**

- **Daniel** (senior, 10 years) — Search infrastructure specialist. Wrote the original Boolean search parser 4 years ago. Deep expertise in information retrieval, Elasticsearch/Lucene internals, and legal citation graphs. Per the graduation model, Daniel self-serves all GSD phases on mid-triangle repos and self-serves discuss/plan on lower-triangle repos (TL verifies).

**The TL:**

- **Sarah** (same TL from Example 1) — Still gates verify on lower-triangle work. Reviews Daniel's PLAN.md artifacts async rather than co-authoring them.

**Repo tags:**

| Repo | Subdomain | Size | Codebase | Clarity | Triangle | Ceremony |
|---|---|---|---|---|---|---|
| `search-engine-core` | `core` | `large` | `brownfield` | `ambiguous` | **lower** | full |
| `search-api-gateway` | `supporting` | `medium` | `brownfield` | `clear` | **mid** | standard |
| `search-analytics-dashboard` | `generic` | `small` | `brownfield` | `clear` | **upper** | quick |

##### The Epic

**BLAW-1300: Hybrid Search — Boolean + Natural Language Fusion**
> *As a legal researcher, I need search results that combine the precision of Boolean operators (terms & connectors) with the recall of natural language queries, so I can find relevant court opinions even when I don't know the exact statutory citation or legal term of art.*

Bloomberg Law's search currently operates in two modes: a Boolean terms-and-connectors engine (precise but requires expertise — e.g., `"statute of limitations" /s "breach of contract" AND jurisdiction(NY)`) and a natural language engine (broader recall but noisier results). Attorneys frequently switch between both, losing context. The hybrid approach fuses them: the user writes a natural query, the system infers Boolean constraints from context, and results blend precision-ranked and semantically-ranked hits.

Daniel creates the Epic in Jira and runs `/gsd:new-milestone "Hybrid Search v1"` on `search-engine-core`. Because Daniel has deep domain knowledge, his milestone artifacts are unusually rich — the PROJECT.md captures ranking algorithm trade-offs, citation graph weighting strategies, and failure modes he's seen over 4 years with the Boolean parser.

##### The Tickets

| Jira ID | Type | Summary | Repo | Triangle | Story Points |
|---|---|---|---|---|---|
| BLAW-1301 | **Story** | Implement query intent classifier (Boolean vs. NL vs. hybrid) | `search-engine-core` | lower | 8 |
| BLAW-1302 | **Story** | Build hybrid ranking fusion algorithm (RRF + citation weighting) | `search-engine-core` | lower | 13 |
| BLAW-1303 | **Task** | Expose hybrid search mode via API gateway | `search-api-gateway` | mid | 5 |
| BLAW-1304 | **Task** | Add search mode toggle and result provenance badges to UI | `search-api-gateway` | mid | 3 |
| BLAW-1305 | **Bug** | Boolean parser silently drops nested parenthetical groups beyond depth 4 | `search-engine-core` | lower | 5 |
| BLAW-1306 | **Spike** | Benchmark latency impact of hybrid ranking on P95 response times | `search-analytics-dashboard` | upper | 2 |
| BLAW-1307 | **Story** | Update analytics dashboard with hybrid-vs-legacy A/B metrics | `search-analytics-dashboard` | upper | 3 |

##### How a Senior Operates Differently

The key contrast with Example 1: **Daniel runs his own discuss and plan phases.** The TL's role shifts from co-authoring specs to async review and verification gating.

**Spike first — same pattern, faster execution (BLAW-1306):**

Daniel benchmarks latency before committing to an architecture. Upper-triangle, no ceremony needed:

```
Daniel runs: /gsd:quick
"Benchmark hybrid ranking overhead: run 10k sample queries through
Boolean-only, NL-only, and fused RRF pipeline. Measure P50/P95/P99
latency delta. Output results to SUMMARY.md."
```

Results: hybrid adds ~35ms at P95 (within the 200ms SLA). Daniel links the SUMMARY.md from the Spike's Jira ticket and closes it. **Backlog → Todo → In Progress → Done** in half a day.

**Core Story with self-served discuss (BLAW-1301):**

Daniel runs the discuss phase himself — his domain expertise means the intent articulation is precise without TL scaffolding:

```
Daniel runs: /gsd:discuss-phase 1
GSD asks: "What signals determine whether a query is Boolean, natural
language, or should be treated as hybrid?"
Daniel: "Three classifiers in sequence:
  1. Lexical: presence of operators (/s, /p, AND, OR, NOT, quotes)
     triggers Boolean mode.
  2. Structural: parenthetical nesting + field constraints
     (jurisdiction(), court()) trigger Boolean even without explicit
     operators.
  3. Fallback: everything else routes to hybrid. No pure-NL mode
     in v1 — we always inject inferred Boolean constraints from
     jurisdiction context and practice area filters."
```

CONTEXT.md captures not just *what* the classifier does, but *why* pure-NL is excluded in v1 — Daniel knows from experience that unstructured NL queries against the full corpus produce too much noise for attorneys who expect precision. This is the kind of L4 (requirements) clarity that a senior brings without TL mediation.

Daniel then surfaces assumptions — and catches one of his own:

```
Daniel runs: /gsd:list-phase-assumptions 1
GSD outputs: "I assume the lexical classifier runs before query parsing,
operating on the raw input string."
Daniel: "Wrong — it must run after tokenization but before parsing.
The tokenizer normalizes citation formats (e.g., '42 U.S.C. § 1983'
becomes a single token), and the classifier needs to see those
normalized tokens to distinguish citations from Boolean operators."
```

Even a 10-year veteran catches assumptions. The discuss phase's value scales with domain complexity, not inversely with seniority.

```
Daniel runs: /gsd:plan-phase 1
```

GSD produces `01-01-PLAN.md` with 4 atomic tasks. Sarah reviews the plan async — she's not co-authoring, just confirming the approach doesn't conflict with the jurisdiction comparison work (Example 1) that shares the inference pipeline. She approves within hours, not days.

**The critical difference at execution:**

```
Daniel runs: /gsd:execute-phase 1
```

Daniel's subtasks are tighter and more architecturally coherent than a junior's would be — each atomic commit represents a clean abstraction boundary. GSD's fresh 200k-token contexts per task matter *even for seniors*: the search engine codebase is 180k+ LOC, and context rot would degrade output quality regardless of who wrote the prompt.

**Bug with deep historical context (BLAW-1305):**

The Boolean parser bug — silently dropping nested parenthetical groups beyond depth 4 — is one Daniel introduced himself 3 years ago as a deliberate performance guardrail. It was documented nowhere. This is **epistemic debt that predates LLMs** — a human-authored decision whose rationale was lost.

```
Daniel runs: /gsd:debug "Boolean parser drops parenthetical groups at depth > 4"
GSD gathers symptoms.
Daniel: "I wrote this limit in 2023 as a perf guard — deeply nested
Boolean queries caused exponential parse time. But the limit is wrong:
it should be depth 6 (matching the most complex real-world queries
in our usage logs), and it should return a parse error, not silently
truncate."
```

Because this is `search-engine-core` (lower-triangle), even the fix gets ceremony. Daniel uses `/gsd:plan-phase` (not `/gsd:quick`) to ensure the fix includes updated parser tests and a documented depth constant. Sarah verifies:

```
Sarah runs: /gsd:verify-work 3
GSD presents UAT:
  ✓ Depth-5 nested query parses correctly
  ✓ Depth-6 nested query parses correctly
  ✓ Depth-7 query returns explicit parse error with message
  ✓ Performance regression test: no P95 latency increase at depth 6
```

BLAW-1305 moves to **Done**. The debug session's `.planning/debug/boolean-parser-depth.md` preserves the *historical rationale* — converting undocumented epistemic debt into a recoverable artifact.

**Mid-triangle work — full self-service (BLAW-1303, BLAW-1304):**

The API gateway and UI tasks are `search-api-gateway`, mid-triangle. Daniel self-serves the entire flow:

```
Daniel runs: /gsd:discuss-phase 2 → /gsd:plan-phase 2 → /gsd:execute-phase 2 → /gsd:verify-work 2
```

No TL involvement at any stage. The governance model trusts seniors on mid-triangle work completely. Daniel's PRs include linked GSD artifacts, but Sarah only reviews them if she chooses to — no gate.

**Upper-triangle work — minimal ceremony (BLAW-1307):**

The analytics dashboard update is generic subdomain, small, clear. Daniel doesn't even run discuss:

```
Daniel runs: /gsd:quick
"Add hybrid-vs-legacy conversion rate chart to search analytics
dashboard. Data source: existing A/B experiment events table.
Chart type: time series with confidence intervals."
```

Done in under two hours. **Backlog → Done** with one atomic commit.

##### Sprint Flow: Senior vs. Mixed-Seniority Comparison

| Dimension | Example 1 (Mixed Team) | Example 2 (Senior-Led) |
|---|---|---|
| **TL role in discuss** | Co-authors CONTEXT.md | Reviews async |
| **TL role in plan** | Co-authors PLAN.md | Approves/rejects async |
| **TL role in verify** | Runs UAT directly | Runs UAT on lower-triangle only |
| **Developer self-service** | Juniors: execute only. Mids: quick + graduated discuss. | Full self-service on mid; discuss+plan self-service on lower |
| **Ceremony overhead** | Higher — TL synchronous involvement | Lower — TL async checkpoints |
| **Epistemic debt risk** | Lower — TL catches gaps juniors miss | Different — senior catches own gaps, but may have blind spots from over-familiarity |
| **Throughput** | Constrained by TL availability | Constrained by review queue, not authoring |

##### Epistemic Debt Trace

| Ticket | Triangle | Ceremony Used | Epistemic Gaps Caught | When Caught | Cascade Cost Avoided |
|---|---|---|---|---|---|
| BLAW-1301 (Core Story) | Lower | Full (self-served discuss+plan, TL verify) | L3: classifier ordering (post-tokenization, not pre-parse) | Discuss phase (self-caught) | ~10× |
| BLAW-1302 (Core Story) | Lower | Full | None — Daniel's domain expertise produced clean first-pass specs | — | — |
| BLAW-1303 (Mid Task) | Mid | Standard (fully self-served) | None significant | — | — |
| BLAW-1305 (Bug) | Lower | Debug + Plan + Verify | L4: recovered lost rationale from 2023; L2: silent truncation → explicit error | Debug phase; Verify phase | ~30× (L4 recovery), ~4× (L2) |
| BLAW-1306 (Spike) | Upper | Quick only | Not measured (accepted) | — | N/A |
| BLAW-1307 (Upper Task) | Upper | Quick only | Not measured (accepted) | — | N/A |

The standout finding: **BLAW-1305's debug session recovered L4-level epistemic debt that was 3 years old and entirely human-authored.** The GSD debug artifact converted "a decision nobody remembered" into a documented, searchable rationale. This illustrates that epistemic debt is not exclusively an LLM-era problem — LLMs *accelerate* its accumulation, but structured workflows can *recover* pre-existing debt too.

The senior's discuss phase on BLAW-1301 also demonstrates that even deep domain experts benefit from forced intent articulation. Daniel caught his own classifier-ordering assumption — a gap that, had it reached implementation, would have produced subtly wrong search results that passed all tests (circular validation at L3).

---

## TL-Led Workflow: Who Runs What

### The Problem

GSD's discuss phase requires articulating intent clearly. The 70% mid/junior developers may struggle here, leading to "garbage in, garbage out" — poor specs producing poor code. But if TLs must gate every task, they become a bottleneck across hundreds of repos.

### The Solution: Tiered Self-Service

| Triangle Position | TL Involvement | Junior Can Self-Serve? |
|---|---|---|
| **Upper** (`/gsd:quick`) | None required | Yes — any developer runs `/gsd:quick` |
| **Mid** (standard) | TL runs Discuss + Plan, hands off Execute | Juniors execute only. Mids can self-serve Discuss after 3 TL-guided cycles. |
| **Lower** (full) | TL runs Discuss + Plan + Verify | No — TL gates all spec phases. Juniors execute only. |

### Graduation Model

```
Junior developer journey:
1. Start: Execute-only on TL-prepared plans (all triangle positions)
2. After 3 TL-guided cycles: Self-serve /gsd:quick on upper-triangle repos
3. After 5 TL-guided cycles: Self-serve Discuss+Plan on mid-triangle repos (TL reviews async)
4. After 10 cycles with <20% rework rate: Full self-service on mid-triangle
```

This prevents TL bottleneck on Generic/Spike work while maintaining guardrails on Core/Supporting subdomains.

---

## Epistemic Debt Observability via GSD Artifacts

### The Connection: GSD Artifacts as Epistemic Debt Sensors

The epistemic trade-off triangle identifies three vertices — Speed, Understanding, Reliability — with structured workflow as the amplifier that makes lower-triangle positions reachable. GSD's artifact trail provides the first concrete substrate for **measuring** where teams actually operate on the triangle, moving epistemic debt from "invisible until crisis" to observable.

### The Formal Framework

Epistemic debt decomposes across abstraction layers (Rau 2026):

```
Ed = Σₖ ∫₀ᵀ (Cs,k(t) - Gc,k(t)) dt
```

Where k indexes layers with different recovery costs (per Boehm's Cost of Change Curve):

| Layer | Description | Recovery Multiplier (cₖ) | GSD Phase That Addresses It |
|---|---|---|---|
| **L4** (Requirements) | Intent misalignment | 30–70× | **Discuss** (forces intent articulation) |
| **L3** (Architecture) | Structural misfit | ~10× | **Plan** (research + structured task design) |
| **L2** (Design) | Implementation approach | 3–6× | **Plan** (atomic task specs with verification criteria) |
| **L1** (Implementation) | Code-level gaps | ~1× | **Execute** (fresh contexts prevent drift) |

**The cascade cost formula:**

```
Total recovery cost = Σₖ cₖ · τₖ

Where τₖ = recovery time at layer k = (Cs,k(t₀) - Gc,k(t₀)) / rₖ
```

Recovery at layer k triggers rework at *all underlying layers*. A requirements misalignment (L4) caught late costs 30–70× more than an implementation bug (L1). **GSD's phased workflow front-loads detection at higher layers**, where the cascade multiplier is highest — Discuss catches L4 gaps before Plan commits to L3 decisions.

### The Net Benefit Condition

AI-assisted development is a net positive only when:

```
Net benefit = δ (time saved by AI speed) - Σₖ cₖ · τₖ (recovery costs from epistemic gaps)
```

When `Σₖ cₖ · τₖ > δ`, the team is **losing time to epistemic debt recovery faster than AI saves it**. GSD's role is to minimize the right side of this equation by catching gaps early (low cₖ layers) rather than late (high cₖ layers).

### Proxy Metrics from GSD Artifacts

Direct measurement of `Gc(t)` (team cognitive grasp) is impractical. But GSD artifacts produce observable proxies:

| GSD Artifact | Metric | What It Signals | Epistemic Layer |
|---|---|---|---|
| **CONTEXT.md** existence & depth | Discussion depth ratio (CONTEXT.md lines / total feature LOC) | Intent articulation quality — low ratio suggests L4 gaps | L4 (Requirements) |
| **PLAN.md** checker iterations | Plan rejection rate (rejections / total plans) | Ambiguity caught at design time vs. execution time | L3–L2 (Architecture/Design) |
| **Atomic commits** vs rework commits | First-pass success rate (clean commits / total commits) | Understanding during execution — high rework = L1–L2 gaps | L2–L1 (Design/Implementation) |
| **VERIFICATION.md** outcomes | UAT pass rate (passes / total verifications) | Circular validation detection — low pass rate despite green CI = epistemic gap | L4–L1 (All layers) |
| **Discuss-to-LOC ratio** | Spec investment ratio (discuss + plan artifact lines / code LOC) | Epistemic investment proportional to complexity | Cross-layer |
| **Phase skip frequency** | Ceremony compliance (phases executed / phases required by policy) | Whether teams are short-circuiting the workflow under time pressure | Process health |
| `/gsd:quick` usage on lower-triangle repos | Policy violation rate | Teams bypassing ceremony on high-criticality code | Governance compliance |

### Leading vs Lagging Indicators

| Type | Metric | When It Fires |
|---|---|---|
| **Leading** (preventive) | Low discuss depth on Core subdomain | *Before* code is written — intervene now |
| **Leading** (preventive) | High plan rejection rate | *During* design — ambiguity is being caught (this is good) |
| **Leading** (preventive) | Phase skips on lower-triangle repos | *Before* damage — policy non-compliance |
| **Lagging** (detective) | High rework commit ratio | *After* execution — L1/L2 gaps manifested |
| **Lagging** (detective) | Low UAT pass rate despite green CI | *After* execution — circular validation detected |
| **Lagging** (detective) | Incident root cause = "nobody understood this code" | *After* crisis — epistemic debt "default event" |

### Dashboard Sketch

```
┌─────────────────────────────────────────────────────────────────┐
│  EPISTEMIC DEBT OBSERVATORY                                     │
├──────────────────────┬──────────────────────────────────────────┤
│  LEADING INDICATORS  │  LAGGING INDICATORS                      │
│                      │                                          │
│  Discuss Depth       │  Rework Ratio        ████░░░░ 34%        │
│  by subdomain:       │  (target: <20%)                          │
│  Core:    ████████   │                                          │
│  Support: █████░░░   │  UAT Pass Rate       ██████░░ 71%        │
│  Generic: ██░░░░░░   │  (target: >85%)                          │
│                      │                                          │
│  Plan Rejections     │  Policy Violations                       │
│  This sprint: 12     │  /quick on lower-triangle: 3 repos       │
│  (healthy: >0)       │  Phase skips on mid: 7 instances         │
│                      │                                          │
│  Phase Compliance    │  Recovery Cost Estimate                  │
│  Lower: 94%          │  Σ cₖ·τₖ this quarter:                   │
│  Mid:   87%          │  L4 events: 0 (good)                     │
│  Upper: N/A          │  L3 events: 2 (~20× hours)               │
│                      │  L2 events: 8 (~4× hours)                │
│                      │  L1 events: 31 (~1× hours)               │
└──────────────────────┴──────────────────────────────────────────┘
```

### The Cognitive Ratchet

The artifact trail also enables a **Cognitive Ratchet** (Ngabang 2026) — a commit-time gate where developers must demonstrate they can explain AI-generated output before merge. GSD's VERIFICATION.md provides a natural hook for this:

- **Lower-triangle repos:** Verification phase requires the developer (not just the AI) to articulate *why* the implementation satisfies requirements — not just that tests pass.
- **Mid-triangle repos:** Plan review by TL serves as the ratchet — TL confirms the developer understands the plan before handing off execution.
- **Upper-triangle repos:** No ratchet required — epistemic debt is an accepted trade-off.

---

## GSD + Cursor: Bridging the Gap

### Current State

| | Claude Code | Cursor (via [gsd-for-cursor](https://github.com/rmindel/gsd-for-cursor)) |
|---|---|---|
| **All GSD phases** | Full support | Full support (27 slash commands, 11 agents) |
| **Parallel wave execution** | Yes (subagent spawning) | No (sequential execution) |
| **Fresh context per task** | Yes (200k per subagent) | No (shared context window) |
| **Syntax** | `/gsd:command` | `/gsd/command` |
| **Config path** | `~/.claude/` | `~/.cursor/` |
| **Maturity** | Primary, production-grade | Community adapter, 49 stars, early-stage |

### What Cursor Teams Get vs. Don't Get

```
GSD on Claude Code  = full triangle amplifier (Speed + Understanding + Reliability)
GSD on Cursor       = partial amplifier (Understanding + Reliability — less Speed)
```

The discuss → plan → verify phases — which are the epistemic debt reduction mechanisms — work identically. The gap is in execution: no parallel waves, no fresh context isolation. This means:

- **Same spec quality** — discuss/plan/verify produce identical artifacts
- **Slower execution** — no parallelism, sequential task processing
- **Degraded context rot mitigation** — shared context window accumulates noise

### Recommendation for Cursor Teams

For the **80% brownfield, mid-triangle default** profile, the discuss/plan/verify phases are what reduce epistemic debt. Parallel execution is a speed optimization, not the epistemic core. **Cursor teams still get the epistemic debt reduction — they just don't get the velocity boost.**

Options in priority order:

1. **Migrate Cursor teams to Claude Code** (preferred — eliminates the gap entirely)
2. **Use gsd-for-cursor adapter** (acceptable — fork and maintain internally if upstream stalls)
3. **Contribute upstream** to improve GSD's Cursor support

---

## Decision Matrix (Reference)

> This matrix informed the single-tool recommendation above. It remains as reference for edge cases where teams may request exceptions.

### How to Read This Matrix

Each cell shows the theoretically optimal tool based on three axes. The governance model in [Section 6](#governance-model) simplifies this to GSD ceremony levels.

### PoC / Spike

| | Junior | Mid | Senior |
|---|---|---|---|
| **Small + Clear** | None | None | None |
| **Medium** | GSD `/quick` (learning rails) | None or GSD `/quick` | None |
| **Large + Ambiguous** | GSD standard (TL-led discuss) | GSD `/quick` + research agents | None or GSD research only |

### Generic Subdomain

| | Junior | Mid | Senior |
|---|---|---|---|
| **Small + Clear** | GSD `/quick` | None | None |
| **Medium** | GSD `/quick` (TL reviews) | GSD `/quick` | None or GSD `/quick` |
| **Large + Ambiguous** | GSD standard (TL-led) | GSD standard | GSD standard or `/quick` |

### Supporting Subdomain

| | Junior | Mid | Senior |
|---|---|---|---|
| **Small + Clear** | GSD `/quick` | GSD `/quick` or None | None |
| **Medium** | GSD standard (TL-led) | GSD standard | GSD `/quick` |
| **Large + Ambiguous** | GSD full (TL-led) | GSD standard or full | GSD standard |

### Core Subdomain

| | Junior | Mid | Senior |
|---|---|---|---|
| **Small + Clear** | GSD standard (TL-led) | GSD standard | GSD standard |
| **Medium** | GSD full (TL-led) | GSD full | GSD full |
| **Large + Ambiguous** | GSD full (TL-led, mandatory) | GSD full | GSD full |

---

## When to Use No SDD Tool

SDD frameworks add value by reducing rework, catching ambiguity early, and managing context. But they also add overhead. **Skip SDD when:**

1. **Small, well-understood changes** — Bug fixes, config changes, copy updates, one-file refactors. The time to write a spec exceeds the time to write the code.

2. **Spikes under 1 day** — Exploratory work meant to be thrown away. Specs for throwaway code are waste.

3. **Hot fixes in production** — When the system is down, write the fix, not the spec. Document afterward if needed.

4. **Well-established patterns** — Adding another REST endpoint to a CRUD service with 50 existing endpoints. The pattern is the spec.

5. **Pair programming with AI on clear problems** — Conversational back-and-forth with an AI assistant can be more effective than formal specs for small-to-medium, clear problems where the developer has strong domain knowledge.

**The litmus test:** If the change maps to **upper triangle AND small+clear**, skip SDD. The governance model encodes this: upper-triangle repos with small+clear work require no ceremony at all.

**The epistemic debt test:** If `Σₖ cₖ · τₖ` (recovery cost from potential misunderstanding) is less than the time to write a spec — skip the spec. For Generic+Small+Clear, this is almost always true. For Core+Large+Ambiguous, it almost never is.

---

## Sources

### SDD Tool Repositories

- [GSD (Get Shit Done)](https://github.com/gsd-build/get-shit-done) — ~30k stars, MIT
- [GSD for Cursor](https://github.com/rmindel/gsd-for-cursor) — Community adapter, 49 stars, MIT
- [GitHub Spec-Kit](https://github.com/github/spec-kit) — ~77k stars, MIT
- [OpenSpec](https://github.com/Fission-AI/OpenSpec) — ~30k stars, MIT
- [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) — ~41k stars, MIT

### Comparison & Analysis

- [Augment Code: Best Spec-Driven Development Tools](https://www.augmentcode.com/tools/best-spec-driven-development-tools)
- [Martin Fowler: SDD Tools Analysis](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [Rick Hightower: GSD vs Spec-Kit vs OpenSpec](https://medium.com/@richardhightower/agentic-coding-gsd-vs-spec-kit-vs-openspec-vs-taskmaster-ai-where-sdd-tools-diverge-0414dcb97e46)
- [Nosam: OpenSpec vs Spec-Kit vs BMAD](https://www.nosam.com/spec-driven-development-openspec-vs-spec-kit-vs-bmad-which-ones-actually-worth-your-time/)

### Epistemic Debt Framework

- [Rau, A. (2026). "Epistemic Debt: The Math, The Cost"](https://antoninorau.substack.com/p/epistemic-debt-the-math-the-cost) — Layered decomposition, cascade cost multipliers, net benefit condition
- Ngabang, L.A. (2026). "The Illusion of Competence: Defining 'Epistemic Debt' in the Era of LLM-Assisted Software Engineering." *ViXra*. — Formal Ed definition, Cognitive Ratchet methodology
- Rau, A. (2026). "Trade-offs in LLM-Assisted Development: IRIS Learnings" — Epistemic trade-off triangle, domain-based strategy selection, IRIS 1.0 metrics
