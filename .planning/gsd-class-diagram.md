# GSD Entity Class Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GSD ENTITY MODEL                                  │
│                    Logical Class Diagram & Workflow Map                      │
└─────────────────────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════════════
 0. DOMAIN GLOSSARY
══════════════════════════════════════════════════════════════════════════════

  ── ENTITIES ──────────────────────────────────────────────────────────────

  PROJECT        The root entity. Captures what is being built, why it
                 matters (core value), constraints, and key decisions.
                 One per repository. All other entities trace back here.
                 Artifact: .planning/PROJECT.md

  ROADMAP        The ordered sequence of phases that deliver the project.
                 Scoped to a single milestone at a time. Contains the
                 progress table that tracks overall completion.
                 Artifact: .planning/ROADMAP.md

  REQUIREMENTS   The full set of scoped requirements (v1 / v2 / out-of-
                 scope) with unique IDs (e.g. SECT2-01, CROSS-03). Each
                 requirement is mapped to one or more phases and marked
                 complete when its SUMMARY ships.
                 Artifact: .planning/REQUIREMENTS.md

  MILESTONE      A named, versioned release boundary (e.g. v1.0.0). When
                 completed, the current ROADMAP + REQUIREMENTS + phase
                 directories are archived, a git tag is created, and the
                 workspace resets for the next milestone.
                 Artifact: .planning/MILESTONES.md (log of all completed)

  PHASE          A unit of deliverable work within a milestone. Identified
                 by number (integer for planned work, decimal for urgent
                 insertions like 5.1). Each phase has a goal, success
                 criteria, requirement mappings, and its own directory
                 containing all sub-artifacts (Context → Plan → Summary).
                 Artifact: .planning/phases/NN-<name>/

  CONTEXT        The user's articulated vision for a phase — locked
                 decisions, boundaries, tone, specifics, and deferred
                 ideas. Created through discussion before planning.
                 Locked decisions are MANDATORY: downstream planning and
                 research cannot override them.
                 Artifact: .planning/phases/NN-<name>/NN-CONTEXT.md

  RESEARCH       Domain and ecosystem knowledge gathered before planning.
                 Covers standard stack, architecture patterns, pitfalls,
                 and alternatives. Bounded by CONTEXT locked decisions.
                 Artifact: .planning/phases/NN-<name>/NN-RESEARCH.md

  PLAN           An executable, task-level specification for work within a
                 phase. Contains ordered tasks, file targets, verification
                 checks, and success criteria. Multiple plans per phase
                 are supported (NN-01, NN-02, ...) and grouped into
                 parallelization waves.
                 Artifact: .planning/phases/NN-<name>/NN-YY-PLAN.md

  SUMMARY        The record of what was actually built when a plan was
                 executed. Captures commits, decisions made, deviations
                 from plan, metrics, and requirement coverage. Triggers
                 STATE and REQUIREMENTS updates upon creation.
                 Artifact: .planning/phases/NN-<name>/NN-YY-SUMMARY.md

  VERIFICATION   A goal-backward audit that checks whether the phase
                 actually achieved what it promised. Evaluates observable
                 truths, required artifacts, wiring between components,
                 and anti-patterns. Gates advancement to the next phase.
                 Artifact: .planning/phases/NN-<name>/NN-VERIFICATION.md

  UAT            User Acceptance Testing session. Created when VERIFICATION
                 flags items that require human judgment (subjective
                 quality, visual appearance, UX flow). Tracks individual
                 tests with pass/issue/skipped results and diagnoses gaps.
                 Artifact: .planning/phases/NN-<name>/NN-UAT.md

  STATE          The single source of truth for where the project stands
                 right now. Tracks current phase/plan, progress percentage,
                 velocity metrics, recent decisions, pending todos, and
                 session continuity. Updated after every significant action.
                 Kept under 100 lines — a digest, not an archive.
                 Artifact: .planning/STATE.md

  CONFIG         Runtime settings that control GSD behavior: workflow mode
                 (interactive/yolo), model profile (quality/balanced/budget),
                 parallelization toggles, verification gates, and git
                 branching strategy.
                 Artifact: .planning/config.json

  DEBUG SESSION  A persistent investigation record for systematic
                 debugging. Tracks symptoms, hypotheses, and evidence
                 using the scientific method. Survives /clear and is
                 archived to resolved/ when fixed.
                 Artifact: .planning/debug/<slug>.md

  CODEBASE MAP   A 7-document snapshot of an existing codebase created for
                 brownfield projects. Covers stack, architecture, structure,
                 conventions, testing, integrations, and known concerns.
                 Artifact: .planning/codebase/*.md

  TODO           A lightweight captured idea or task, stored as a file in
                 pending/ and moved to done/ when work begins. Tracked
                 in STATE.md as a count.
                 Artifact: .planning/todos/pending/<slug>.md

  ── WORKFLOWS ─────────────────────────────────────────────────────────────

  /gsd:new-project       Full initialization: questioning → optional
                         research → requirements → roadmap. Creates all
                         root artifacts (PROJECT, ROADMAP, REQUIREMENTS,
                         STATE, CONFIG).

  /gsd:map-codebase      Parallel analysis of an existing codebase.
                         Creates CODEBASE MAP. Run before new-project
                         on brownfield repos.

  /gsd:discuss-phase     Conversational exploration of a phase's vision.
                         Produces CONTEXT with locked decisions and
                         boundaries.

  /gsd:research-phase    Deep ecosystem research for specialized domains.
                         Produces RESEARCH bounded by CONTEXT constraints.

  /gsd:list-phase-       Displays Claude's intended approach for a phase
    assumptions          without creating files. Conversational only.

  /gsd:plan-phase        Creates executable PLAN(s) for a phase. Reads
                         CONTEXT + RESEARCH if available. Runs plan-
                         checker to verify quality before finalizing.

  /gsd:execute-phase     Runs all PLANs in a phase (grouped by wave).
                         Produces SUMMARY per plan, then VERIFICATION
                         for the phase. Updates STATE + REQUIREMENTS.

  /gsd:verify-work       Interactive UAT session. Presents tests from
                         VERIFICATION's human-needed items one at a time.
                         Diagnoses failures and creates fix plans.

  /gsd:quick             Lightweight path for small, well-understood tasks.
                         Planner + executor only (no researcher, checker,
                         or verifier). Lives in .planning/quick/.

  /gsd:add-phase         Appends a new phase to the end of the current
                         milestone in ROADMAP.

  /gsd:insert-phase      Inserts a decimal phase (e.g. 5.1) between
                         existing phases for urgent work.

  /gsd:remove-phase      Deletes a future phase and renumbers subsequent
                         ones.

  /gsd:audit-milestone   Reads all VERIFICATION files, checks requirement
                         coverage, and spawns integration checker. Produces
                         MILESTONE-AUDIT.md with gaps and tech debt.

  /gsd:plan-milestone-   Groups audit gaps into new phases, adds them to
    gaps                 ROADMAP, ready for plan-phase.

  /gsd:complete-         Archives the current milestone (ROADMAP,
    milestone            REQUIREMENTS, phases/) and creates a MILESTONES
                         entry with stats and git tag.

  /gsd:new-milestone     Starts a new milestone cycle. Mirrors new-project
                         flow for existing projects.

  /gsd:progress          Visual progress display from STATE. Routes to
                         next action (plan or execute).

  /gsd:add-todo          Captures an idea as a TODO file in pending/.

  /gsd:check-todos       Lists pending TODOs, optionally filtered by area.

  /gsd:debug             Starts or resumes a persistent DEBUG SESSION.

  /gsd:pause-work        Saves session context to .continue-here.md and
                         updates STATE continuity section.

  /gsd:resume-work       Restores context from STATE continuity and
                         .continue-here.md.

  /gsd:settings          Interactive configuration of CONFIG toggles and
                         model profile.

  /gsd:set-profile       Quick switch: quality | balanced | budget.


══════════════════════════════════════════════════════════════════════════════
 1. CLASS DIAGRAM
══════════════════════════════════════════════════════════════════════════════

┌──────────────────────────┐         ┌──────────────────────────┐
│        PROJECT            │         │         CONFIG            │
│ .planning/PROJECT.md      │         │ .planning/config.json     │
├──────────────────────────┤         ├──────────────────────────┤
│ - coreValue: string       │         │ - mode: interactive|yolo  │
│ - whatThisIs: string      │         │ - modelProfile: string    │
│ - context: string         │         │ - granularity: string     │
│ - constraints: Constraint[]│        │ - workflow: WorkflowFlags │
│ - keyDecisions: Decision[] │        │ - parallelization: Opts   │
│ - lastUpdated: date       │         │ - git: GitStrategy        │
├──────────────────────────┤         ├──────────────────────────┤
│ + init()                  │         │ + load(): Config          │
│ + updateDecisions()       │         │ + setProfile(p)           │
└──────────┬───────────────┘         └──────────────────────────┘
           │ defines                          loaded by all commands
           │ scope &
           │ vision
           ▼
┌──────────────────────────┐    maps to    ┌──────────────────────────┐
│      REQUIREMENTS         │◄────────────►│        ROADMAP            │
│ .planning/REQUIREMENTS.md │              │ .planning/ROADMAP.md      │
├──────────────────────────┤              ├──────────────────────────┤
│ - coreValue: string       │              │ - overview: string        │
│ - milestone: string       │              │ - progressTable: Row[]    │
│ - sections: Section[]     │              │ - currentMilestone: str   │
│ - outOfScope: Item[]      │              ├──────────────────────────┤
│ - traceability: Trace[]   │              │ + addPhase(desc)          │
│ - coverage: Stats         │              │ + insertPhase(after,desc) │
├──────────────────────────┤              │ + removePhase(n)          │
│ + markComplete(reqId)     │              └──────────┬───────────────┘
│ + getUnmapped(): Req[]    │                         │
└──────────────────────────┘                         │ contains 1..*
                                                      ▼
                                 ┌──────────────────────────────────┐
                                 │          PHASE (directory)        │
                                 │  .planning/phases/NN-<name>/     │
                                 ├──────────────────────────────────┤
                                 │ - number: int | decimal           │
                                 │ - name: string (slug)             │
                                 │ - goal: string                    │
                                 │ - dependsOn: Phase[]              │
                                 │ - requirements: ReqID[]           │
                                 │ - successCriteria: string[]       │
                                 │ - status: PhaseStatus             │
                                 ├──────────────────────────────────┤
                                 │ + discuss() → Context             │
                                 │ + research() → Research           │
                                 │ + plan() → Plan                   │
                                 │ + execute() → Summary             │
                                 │ + verify() → Verification         │
                                 └───┬──────┬──────┬──────┬─────┬───┘
                                     │      │      │      │     │
              ┌──────────────────────┘      │      │      │     └──────────────────┐
              ▼                             ▼      │      ▼                        ▼
┌─────────────────────┐  ┌─────────────────────┐  │  ┌─────────────────────┐  ┌──────────────┐
│      CONTEXT         │  │      RESEARCH        │  │  │   VERIFICATION      │  │     UAT      │
│  NN-CONTEXT.md       │  │  NN-RESEARCH.md      │  │  │  NN-VERIFICATION.md │  │  NN-UAT.md   │
├─────────────────────┤  ├─────────────────────┤  │  ├─────────────────────┤  ├──────────────┤
│ - gathered: date     │  │ - researched: date   │  │  │ - verified: date    │  │ - status:    │
│ - status: string     │  │ - domain: string     │  │  │ - status:           │  │   testing|   │
│ - decisions: []      │  │ - confidence:        │  │  │   passed|           │  │   complete|  │
│ - specifics: {}      │  │   HIGH|MED|LOW       │  │  │   gaps_found|       │  │   diagnosed  │
│ - deferred: []       │  │ - lockedDecisions:[] │  │  │   human_needed      │  │ - tests: []  │
│ - phaseBoundary: str │  │ - stack: StackInfo   │  │  │ - score: string     │  │ - gaps: []   │
├─────────────────────┤  │ - patterns: []       │  │  │ - truths: Truth[]   │  │ - summary:   │
│ Locked decisions     │  │ - alternatives: []   │  │  │ - artifacts: Art[]  │  │   Stats      │
│ are MANDATORY for    │  ├─────────────────────┤  │  │ - antiPatterns: []  │  ├──────────────┤
│ downstream planning  │  │ Informs plan tasks   │  │  │ - humanChecks: []   │  │ Captures     │
└──────────┬──────────┘  └──────────┬──────────┘  │  ├─────────────────────┤  │ user feedback│
           │ constrains             │ informs      │  │ Gates phase          │  │ on features  │
           ▼                        ▼              │  │ advancement          │  └──────┬───────┘
           └────────────►┌─────────────────────┐◄──┘  └──────────┬──────────┘         │
                         │        PLAN          │                 ▲                     │
                         │  NN-YY-PLAN.md       │                 │ verifies             │
                         ├─────────────────────┤                 │                     │
                         │ - phase: string      │     ┌──────────┴──────────┐          │
                         │ - plan: string (YY)  │     │      SUMMARY         │          │
                         │ - type: PlanType     │     │  NN-YY-SUMMARY.md    │          │
                         │ - wave: int          │     ├─────────────────────┤          │
                         │ - dependsOn: Plan[]  │     │ - phase: string      │          │
                         │ - filesModified: []  │     │ - plan: string       │          │
                         │ - autonomous: bool   │     │ - subsystem: string  │          │
                         │ - requirements: []   │     │ - status:            │          │
                         │ - mustHaves: {}      │     │   complete|partial|  │          │
                         │ - tasks: Task[]      │     │   blocked            │          │
                         │ - verification: []   │     │ - completed: date    │          │
                         │ - successCriteria:[] │     │ - techStack: {}      │          │
                         ├─────────────────────┤     │ - keyFiles: {}       │          │
                         │ + execute() → Summary│     │ - decisions: []      │          │
                         └──────────┬──────────┘     │ - metrics: {}        │          │
                                    │                 │ - deviations: []     │          │
                                    │ produces        ├─────────────────────┤          │
                                    └────────────────►│ Updates STATE &      │          │
                                                      │ marks REQUIREMENTS   │──────────┘
                                                      │ complete             │ issues feed
                                                      └─────────────────────┘ back to UAT


┌──────────────────────────┐         ┌──────────────────────────┐
│         STATE             │         │       MILESTONE           │
│ .planning/STATE.md        │         │ .planning/MILESTONES.md   │
├──────────────────────────┤         ├──────────────────────────┤
│ - currentPhase: int       │         │ - version: string         │
│ - currentPlan: int        │         │ - name: string            │
│ - status: PhaseStatus     │         │ - delivered: string       │
│ - lastActivity: date      │         │ - phasesCompleted: Range  │
│ - progress: Percentage    │         │ - accomplishments: []     │
│ - velocity: Metrics       │         │ - stats: Stats            │
│ - decisions: Decision[]   │         │ - gitRange: string        │
│ - pendingTodos: Todo[]    │         ├──────────────────────────┤
│ - blockers: Blocker[]     │         │ + archive(version)        │
│ - sessionContinuity: {}   │         │ Archives: ROADMAP,        │
├──────────────────────────┤         │ REQUIREMENTS, phases/     │
│ + updatePosition()        │         │ to milestones/ directory  │
│ + recordDecision()        │         └──────────────────────────┘
│ Single source of truth    │
│ for current position      │                ┌──────────────────┐
│ Updated after every       │                │   CODEBASE MAP    │
│ significant action        │                │ .planning/codebase│
└──────────────────────────┘                ├──────────────────┤
                                             │ - STACK.md        │
        ┌──────────────────────┐             │ - ARCHITECTURE.md │
        │     DEBUG SESSION     │             │ - STRUCTURE.md    │
        │ .planning/debug/     │             │ - CONVENTIONS.md  │
        │       <slug>.md      │             │ - TESTING.md      │
        ├──────────────────────┤             │ - INTEGRATIONS.md │
        │ - symptoms: []        │             │ - CONCERNS.md     │
        │ - hypotheses: []      │             ├──────────────────┤
        │ - evidence: []        │             │ Brownfield only   │
        │ - resolution: string  │             │ Created by        │
        ├──────────────────────┤             │ /gsd:map-codebase │
        │ Survives /clear       │             └──────────────────┘
        │ Archived to resolved/ │
        └──────────────────────┘


══════════════════════════════════════════════════════════════════════════════
 2. ENUMERATIONS
══════════════════════════════════════════════════════════════════════════════

  «enum» PhaseStatus              «enum» PlanType
  ┌─────────────────┐             ┌─────────────────┐
  │ Ready to plan    │             │ execute          │
  │ Planning         │             │ research         │
  │ Ready to execute │             │ validate         │
  │ In progress      │             └─────────────────┘
  │ Complete         │
  └─────────────────┘             «enum» VerifyStatus
                                  ┌─────────────────┐
  «enum» SummaryStatus            │ passed           │
  ┌─────────────────┐             │ gaps_found       │
  │ complete         │             │ human_needed     │
  │ partial          │             └─────────────────┘
  │ blocked          │
  └─────────────────┘             «enum» UATStatus
                                  ┌─────────────────┐
  «enum» ModelProfile             │ testing          │
  ┌─────────────────┐             │ complete         │
  │ quality          │             │ diagnosed        │
  │ balanced         │             └─────────────────┘
  │ budget           │
  └─────────────────┘


══════════════════════════════════════════════════════════════════════════════
 3. RELATIONSHIP SUMMARY
══════════════════════════════════════════════════════════════════════════════

  PROJECT ──defines──► REQUIREMENTS (scope & boundaries)
  PROJECT ──defines──► ROADMAP (phases & milestones)
  ROADMAP ──contains 1..*──► PHASE
  PHASE ──maps to 1..*──► REQUIREMENT (via reqId)
  PHASE ──contains 0..1──► CONTEXT
  PHASE ──contains 0..1──► RESEARCH
  PHASE ──contains 1..*──► PLAN
  PLAN ──produces 1──► SUMMARY
  SUMMARY ──triggers──► VERIFICATION
  VERIFICATION ──may create──► UAT (if human_needed)
  UAT ──feeds issues back to──► PLAN (gap closure)
  SUMMARY ──updates──► STATE (position, metrics)
  SUMMARY ──marks complete──► REQUIREMENT
  MILESTONE ──archives──► PHASE[] + ROADMAP + REQUIREMENTS
  CONTEXT ──constrains──► RESEARCH (locked decisions)
  CONTEXT ──constrains──► PLAN (mandatory decisions)
  RESEARCH ──informs──► PLAN (stack, patterns)
  CONFIG ──configures──► all workflows
  DEBUG ──diagnoses──► VERIFICATION gaps
  CODEBASE MAP ──informs──► RESEARCH (brownfield context)


══════════════════════════════════════════════════════════════════════════════
 4. WORKFLOW → ENTITY MAPPING
══════════════════════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────┐
  │                        WORKFLOW LIFECYCLE                           │
  │                                                                     │
  │   INITIALIZATION                                                    │
  │   ══════════════                                                    │
  │   /gsd:new-project ──creates──► PROJECT + ROADMAP + REQUIREMENTS   │
  │                                 + STATE + CONFIG                    │
  │   /gsd:map-codebase ──creates──► CODEBASE MAP (7 documents)        │
  │                                                                     │
  │   PHASE PREPARATION (optional, per phase)                          │
  │   ═════════════════                                                 │
  │   /gsd:discuss-phase N ──creates──► CONTEXT                        │
  │   /gsd:research-phase N ──creates──► RESEARCH                      │
  │   /gsd:list-phase-assumptions N ──reads──► CONTEXT (display only)  │
  │                                                                     │
  │   PHASE EXECUTION (per phase)                                      │
  │   ═══════════════                                                   │
  │   /gsd:plan-phase N ──creates──► PLAN(s)                           │
  │   /gsd:execute-phase N ──creates──► SUMMARY + VERIFICATION         │
  │                          ──updates──► STATE + REQUIREMENTS          │
  │   /gsd:verify-work N ──updates──► UAT                              │
  │                                                                     │
  │   MILESTONE LIFECYCLE                                               │
  │   ══════════════════                                                │
  │   /gsd:audit-milestone ──reads──► all VERIFICATION files           │
  │   /gsd:plan-milestone-gaps ──creates──► new PHASE(s) for gaps      │
  │   /gsd:complete-milestone ──creates──► MILESTONE entry             │
  │                             ──archives──► ROADMAP + REQUIREMENTS   │
  │                             ──moves──► PHASE dirs to milestones/   │
  │   /gsd:new-milestone ──resets──► ROADMAP + REQUIREMENTS            │
  │                                                                     │
  │   ONGOING                                                           │
  │   ═══════                                                           │
  │   /gsd:progress ──reads──► STATE                                   │
  │   /gsd:add-todo ──updates──► STATE (pending todos)                 │
  │   /gsd:debug ──creates──► DEBUG SESSION                            │
  │   /gsd:pause-work ──updates──► STATE (session continuity)          │
  │   /gsd:resume-work ──reads──► STATE (session continuity)           │
  └─────────────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════════════
 5. PHASE INTERNAL FLOW (entity lifecycle within a single phase)
══════════════════════════════════════════════════════════════════════════════

                    ┌──────────┐
                    │ discuss  │ (optional)
                    └────┬─────┘
                         │ creates
                         ▼
                    ┌──────────┐
                    │ CONTEXT  │──constrains──┐
                    └────┬─────┘              │
                         │                    │
                    ┌────▼─────┐              │
                    │ research │ (optional)   │
                    └────┬─────┘              │
                         │ creates            │
                         ▼                    │
                    ┌──────────┐              │
                    │ RESEARCH │──informs──┐  │
                    └──────────┘           │  │
                                           ▼  ▼
                    ┌──────────┐      ┌──────────┐
                    │plan-phase│─────►│  PLAN(s)  │
                    └──────────┘      └────┬─────┘
                                           │ execute
                                           ▼
                                      ┌──────────┐     ┌──────────┐
                                      │ SUMMARY  │────►│  STATE   │
                                      └────┬─────┘     │ (update) │
                                           │            └──────────┘
                                           │ triggers
                                           ▼
                                   ┌──────────────┐
                                   │ VERIFICATION │
                                   └──────┬───────┘
                                          │
                          ┌───────────────┼───────────────┐
                          ▼               ▼               ▼
                    ┌──────────┐   ┌──────────┐   ┌──────────┐
                    │  passed  │   │gaps_found│   │human_need│
                    │ → next   │   │ → debug/ │   │ → UAT    │
                    │   phase  │   │   replan │   │   tests  │
                    └──────────┘   └──────────┘   └────┬─────┘
                                                       │
                                                       ▼
                                                 ┌──────────┐
                                                 │  issues?  │
                                                 │ → replan  │
                                                 └──────────┘


══════════════════════════════════════════════════════════════════════════════
 6. MULTI-DEVELOPER PARALLEL WORK WITH JIRA
══════════════════════════════════════════════════════════════════════════════

  GSD was designed for solo agentic development — one developer, one
  Claude Code session, sequential phases. But it can be adapted for a
  team of 4 developers working in parallel on Jira tickets by treating
  each developer as an independent GSD instance operating on isolated
  branches within a shared project structure.

  ── CONCEPTUAL MAPPING: JIRA → GSD ───────────────────────────────────

    Jira Concept        GSD Equivalent         Notes
    ──────────────────  ─────────────────────  ─────────────────────────
    Epic                Milestone              A versioned release goal
    Story / Task        Phase                  A deliverable unit of work
    Sub-task            Plan (NN-YY-PLAN.md)   A concrete execution step
    Sprint              Wave of phases         Time-boxed parallel work
    Acceptance Criteria Success Criteria       Observable truths per phase
    Definition of Done  Verification (passed)  Gate before merge

  ── REPOSITORY STRUCTURE (shared) ─────────────────────────────────────

    .planning/
    ├── PROJECT.md              ← shared, rarely changes
    ├── REQUIREMENTS.md         ← shared, updated on merge
    ├── ROADMAP.md              ← shared, phases assigned to developers
    ├── STATE.md                ← each dev updates on merge to main
    ├── config.json             ← shared settings
    └── phases/
        ├── 01-auth/            ← Developer A (JIRA-101)
        ├── 02-data-model/      ← Developer B (JIRA-102)
        ├── 03-api-endpoints/   ← Developer C (JIRA-103)
        └── 04-ui-components/   ← Developer D (JIRA-104)

  ── BRANCHING STRATEGY ────────────────────────────────────────────────

    Enable per-phase branching in config.json:

    {
      "git": {
        "branching_strategy": "per-phase",
        "phase_branch_template": "gsd/phase-{phase}-{slug}"
      }
    }

    Each developer works on their own branch:

    main
     ├── gsd/phase-01-auth              ← Dev A
     ├── gsd/phase-02-data-model        ← Dev B
     ├── gsd/phase-03-api-endpoints     ← Dev C
     └── gsd/phase-04-ui-components     ← Dev D

    Phases with no cross-dependencies can proceed in parallel.
    Phases with dependencies (dependsOn field) must wait for their
    dependency to merge before starting execution.

  ── WORKFLOW: 4 DEVELOPERS IN PARALLEL ────────────────────────────────

    STEP 1 — SHARED SETUP (Tech Lead / all devs together)
    ═══════════════════════════════════════════════════════

    One developer (or tech lead) initializes the shared project:

      /gsd:new-project          ← creates PROJECT, ROADMAP, REQUIREMENTS
      /gsd:map-codebase         ← if brownfield

    The ROADMAP is designed with parallelizable phases. Tag each phase
    in ROADMAP.md with the assigned developer and Jira ticket:

      ## Phase 1: Authentication (JIRA-101, @alice)
      ## Phase 2: Data Model (JIRA-102, @bob)
      ## Phase 3: API Endpoints (JIRA-103, @carol)
      ## Phase 4: UI Components (JIRA-104, @dave)

    Push .planning/ to main. All devs pull.

    STEP 2 — PARALLEL PLANNING (each dev, own branch)
    ══════════════════════════════════════════════════

    Each developer creates their feature branch and plans their phase:

      Dev A:  git checkout -b gsd/phase-01-auth
              /gsd:discuss-phase 1      ← optional
              /gsd:plan-phase 1

      Dev B:  git checkout -b gsd/phase-02-data-model
              /gsd:plan-phase 2

      Dev C:  git checkout -b gsd/phase-03-api-endpoints
              /gsd:plan-phase 3

      Dev D:  git checkout -b gsd/phase-04-ui-components
              /gsd:plan-phase 4

    Each dev only modifies files inside their own phase directory
    (.planning/phases/NN-*/) and the actual source code for their
    feature. This avoids merge conflicts in .planning/.

    STEP 3 — PARALLEL EXECUTION (each dev, own branch)
    ══════════════════════════════════════════════════

      Dev A:  /gsd:execute-phase 1      ← works on auth code
      Dev B:  /gsd:execute-phase 2      ← works on data model
      Dev C:  /gsd:execute-phase 3      ← works on API
      Dev D:  /gsd:execute-phase 4      ← works on UI

    Each execution produces:
    - Source code changes (in feature branch)
    - NN-YY-SUMMARY.md (in phase directory)
    - NN-VERIFICATION.md (in phase directory)

    STEP 4 — MERGE & INTEGRATE (sequential, coordinated)
    ════════════════════════════════════════════════════

    As each developer's phase passes VERIFICATION:

      1. Create PR from feature branch → main
      2. PR includes source code + .planning/phases/NN-*/ artifacts
      3. On merge, update shared ROADMAP.md (mark phase complete)
      4. Update shared STATE.md (advance position)
      5. Mark REQUIREMENTS complete for covered req IDs

    Merge order follows the dependency graph. Independent phases
    merge in any order. Dependent phases merge after their
    prerequisites.

  ── HANDLING DEPENDENCIES ─────────────────────────────────────────────

    When phases have dependencies, use this pattern:

    ROADMAP.md:
      Phase 2: Data Model          ← depends on: nothing
      Phase 3: API Endpoints       ← depends on: Phase 2
      Phase 5: Integration Tests   ← depends on: Phase 2, 3, 4

    ┌───────────┐   ┌───────────┐
    │ Phase 1   │   │ Phase 2   │
    │ Auth      │   │ Data Model│
    │ @alice    │   │ @bob      │
    └─────┬─────┘   └─────┬─────┘
          │               │
          │               │ dependency
          │               ▼
          │         ┌───────────┐   ┌───────────┐
          │         │ Phase 3   │   │ Phase 4   │
          │         │ API       │   │ UI        │
          │         │ @carol    │   │ @dave     │
          │         └─────┬─────┘   └─────┬─────┘
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                    ┌───────────┐
                    │ Phase 5   │
                    │ Integration│
                    │ @alice    │
                    └───────────┘

    Dev C (@carol) can plan Phase 3 while Dev B (@bob) executes
    Phase 2, but must wait for Phase 2 to merge before executing
    Phase 3. During that wait, Carol can:
    - /gsd:discuss-phase 3       ← refine context
    - /gsd:research-phase 3      ← gather ecosystem knowledge
    - /gsd:plan-phase 3          ← create execution plan
    - Work on other tickets

  ── CONFLICT AVOIDANCE RULES ──────────────────────────────────────────

    1. SHARED FILES — Only modify on merge to main, not in branches:
       - .planning/ROADMAP.md (progress table)
       - .planning/STATE.md (current position)
       - .planning/REQUIREMENTS.md (traceability table)

    2. PHASE-SCOPED FILES — Each dev owns their phase directory:
       - .planning/phases/NN-*/ → only modified by assigned dev

    3. SOURCE CODE — Coordinate via Jira ticket scope:
       - Each Jira story defines the code ownership boundary
       - Shared files (e.g. schema, routes index) require
         communication or interface contracts agreed upfront

    4. PLANNING ARTIFACTS — Each dev commits their own:
       - PLAN.md, SUMMARY.md, VERIFICATION.md stay in phase dir
       - No cross-phase file edits during execution

  ── JIRA INTEGRATION WORKFLOW ─────────────────────────────────────────

    Jira Status        GSD Command                  GSD State
    ────────────────   ─────────────────────────     ──────────────────
    To Do              —                             Phase in ROADMAP
    In Progress        /gsd:plan-phase N             Planning
    In Progress        /gsd:execute-phase N          In progress
    In Review          PR created                    Verification passed
    Done               PR merged, ROADMAP updated    Phase complete

    Automation hooks (optional):
    - On Jira → "In Progress": dev runs /gsd:plan-phase
    - On VERIFICATION passed: dev creates PR, moves Jira → "In Review"
    - On PR merge: script updates ROADMAP + STATE, moves Jira → "Done"

  ── EXAMPLE: SPRINT WITH 4 DEVELOPERS ────────────────────────────────

    Week 1 — Planning
    ┌──────────────────────────────────────────────────────────────┐
    │  Mon   Tech lead: /gsd:new-project (all devs present)      │
    │  Tue   All devs: create branches, /gsd:plan-phase N        │
    │  Wed   All devs: review each other's PLANs                 │
    │  Thu   All devs: /gsd:execute-phase N (begin)              │
    └──────────────────────────────────────────────────────────────┘

    Week 2 — Execution
    ┌──────────────────────────────────────────────────────────────┐
    │  Mon   Dev A finishes Phase 1 → PR → merge                 │
    │  Tue   Dev B finishes Phase 2 → PR → merge                 │
    │        Dev C starts executing Phase 3 (was blocked on 2)   │
    │  Wed   Dev D finishes Phase 4 → PR → merge                 │
    │  Thu   Dev C finishes Phase 3 → PR → merge                 │
    │  Fri   Dev A: /gsd:execute-phase 5 (integration tests)    │
    │        All devs: /gsd:audit-milestone                      │
    └──────────────────────────────────────────────────────────────┘

  ── LIMITATIONS & WORKAROUNDS ─────────────────────────────────────────

    GSD Limitation              Workaround for Teams
    ─────────────────────────   ──────────────────────────────────────
    STATE.md is single-writer   Each dev updates STATE only on merge
                                to main, not in feature branches.

    ROADMAP.md progress table   Update progress table as part of the
    assumes one writer          PR merge checklist (or automate with
                                a post-merge hook).

    No built-in Jira sync       Use branch naming convention
                                (gsd/phase-NN-jira-KEY) and PR
                                descriptions to maintain traceability.

    /gsd:progress shows global  Each dev can run /gsd:progress on
    state, not per-developer    main to see overall project status.

    Verification is per-phase,  Use /gsd:audit-milestone after all
    not cross-phase             phases merge to catch integration
                                gaps. Add a dedicated integration
                                phase at the end.
```
