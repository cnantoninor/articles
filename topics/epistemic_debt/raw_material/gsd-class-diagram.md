# GSD Entity Class Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GSD ENTITY MODEL                                  │
│                    Logical Class Diagram & Workflow Map                      │
└─────────────────────────────────────────────────────────────────────────────┘


══════════════════════════════════════════════════════════════════════════════
 0. DOMAIN GLOSSARY
══════════════════════════════════════════════════════════════════════════════

  ── JIRA ↔ GSD QUICK REFERENCE ────────────────────────────────────────

    Jira                GSD                 Notes
    ──────────────────  ──────────────────  ──────────────────────────────
    Project             PROJECT             One root entity per repo
    Epic                MILESTONE           Versioned release boundary
    Story / Task        PHASE               Assignable unit of work
    Sub-task            PLAN                Executable step within a phase
    Acceptance Criteria Success Criteria    Observable truths per phase
    Definition of Done  VERIFICATION        Gate before merge / advance
    Sprint              Wave of phases      Time-boxed parallel batch
    Sprint Board        STATE + ROADMAP     Progress tracking
    Backlog Item        TODO                Captured idea, not yet planned
    Bug (investigation) DEBUG SESSION       Scientific-method diagnosis
    Component / Label   Subsystem tag       In SUMMARY frontmatter

  ── ENTITIES ──────────────────────────────────────────────────────────────

  PROJECT        The root entity. Captures what is being built, why it
                 matters (core value), constraints, and key decisions.
                 One per repository. All other entities trace back here.
                 Jira equivalent: Project
                 Artifact: .planning/PROJECT.md

  ROADMAP        The ordered sequence of phases that deliver the project.
                 Scoped to a single milestone at a time. Contains the
                 progress table that tracks overall completion.
                 Jira equivalent: Board / Sprint plan (phase ordering)
                 Artifact: .planning/ROADMAP.md

  REQUIREMENTS   The full set of scoped requirements (v1 / v2 / out-of-
                 scope) with unique IDs (e.g. SECT2-01, CROSS-03). Each
                 requirement is mapped to one or more phases and marked
                 complete when its SUMMARY ships.
                 Jira equivalent: Requirements linked to Epics/Stories
                 Artifact: .planning/REQUIREMENTS.md

  MILESTONE      A named, versioned release boundary (e.g. v1.0.0). When
                 completed, the current ROADMAP + REQUIREMENTS + phase
                 directories are archived, a git tag is created, and the
                 workspace resets for the next milestone.
                 Constraint: Only ONE milestone is active at a time. For
                 parallel Epics, either flatten them into one milestone
                 or isolate via branches/worktrees (see Section 6).
                 Jira equivalent: Epic (a group of stories toward a goal)
                 Artifact: .planning/MILESTONES.md (log of all completed)

  PHASE          A unit of deliverable work within a milestone. Identified
                 by number (integer for planned work, decimal for urgent
                 insertions like 5.1). Each phase has a goal, success
                 criteria, requirement mappings, and its own directory
                 containing all sub-artifacts (Context → Plan → Summary).
                 Jira equivalent: Story / Task (assignable ticket)
                 Artifact: .planning/phases/NN-<name>/

  CONTEXT        The user's articulated vision for a phase — locked
                 decisions, boundaries, tone, specifics, and deferred
                 ideas. Created through discussion before planning.
                 Locked decisions are MANDATORY: downstream planning and
                 research cannot override them.
                 Jira equivalent: Story description / design doc linked
                 Artifact: .planning/phases/NN-<name>/NN-CONTEXT.md

  RESEARCH       Domain and ecosystem knowledge gathered before planning.
                 Covers standard stack, architecture patterns, pitfalls,
                 and alternatives. Bounded by CONTEXT locked decisions.
                 Jira equivalent: Spike ticket output
                 Artifact: .planning/phases/NN-<name>/NN-RESEARCH.md

  PLAN           An executable, task-level specification for work within a
                 phase. Contains ordered tasks, file targets, verification
                 checks, and success criteria. Multiple plans per phase
                 are supported (NN-01, NN-02, ...) and grouped into
                 parallelization waves.
                 Jira equivalent: Sub-task (concrete work item)
                 Artifact: .planning/phases/NN-<name>/NN-YY-PLAN.md

  SUMMARY        The record of what was actually built when a plan was
                 executed. Captures commits, decisions made, deviations
                 from plan, metrics, and requirement coverage. Triggers
                 STATE and REQUIREMENTS updates upon creation.
                 Jira equivalent: Work log / PR description
                 Artifact: .planning/phases/NN-<name>/NN-YY-SUMMARY.md

  VERIFICATION   A goal-backward audit that checks whether the phase
                 actually achieved what it promised. Evaluates observable
                 truths, required artifacts, wiring between components,
                 and anti-patterns. Gates advancement to the next phase.
                 Jira equivalent: Definition of Done / QA checklist
                 Artifact: .planning/phases/NN-<name>/NN-VERIFICATION.md

  UAT            User Acceptance Testing session. Created when VERIFICATION
                 flags items that require human judgment (subjective
                 quality, visual appearance, UX flow). Tracks individual
                 tests with pass/issue/skipped results and diagnoses gaps.
                 Jira equivalent: QA test execution (manual testing)
                 Artifact: .planning/phases/NN-<name>/NN-UAT.md

  STATE          The single source of truth for where the project stands
                 right now. Tracks current phase/plan, progress percentage,
                 velocity metrics, recent decisions, pending todos, and
                 session continuity. Updated after every significant action.
                 Kept under 100 lines — a digest, not an archive.
                 Jira equivalent: Sprint board + velocity chart
                 Artifact: .planning/STATE.md

  CONFIG         Runtime settings that control GSD behavior: workflow mode
                 (interactive/yolo), model profile (quality/balanced/budget),
                 parallelization toggles, verification gates, and git
                 branching strategy.
                 Jira equivalent: Project settings / workflow scheme
                 Artifact: .planning/config.json

  DEBUG SESSION  A persistent investigation record for systematic
                 debugging. Tracks symptoms, hypotheses, and evidence
                 using the scientific method. Survives /clear and is
                 archived to resolved/ when fixed.
                 Jira equivalent: Bug ticket (investigation type)
                 Artifact: .planning/debug/<slug>.md

  CODEBASE MAP   A 7-document snapshot of an existing codebase created for
                 brownfield projects. Covers stack, architecture, structure,
                 conventions, testing, integrations, and known concerns.
                 Jira equivalent: (no equivalent — architecture docs)
                 Artifact: .planning/codebase/*.md

  TODO           A lightweight captured idea or task, stored as a file in
                 pending/ and moved to done/ when work begins. Tracked
                 in STATE.md as a count.
                 Jira equivalent: Backlog item (ungroomed)
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
│ Jira: Project             │         │ Jira: Project Settings    │
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
│ Jira: Linked Requirements │              │ Jira: Board / Sprint Plan │
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
                                 │  Jira: Story / Task (ticket)     │
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
│  Jira: Story desc    │  │  Jira: Spike output  │  │  │  Jira: DoD / QA     │  │  Jira: QA    │
│        / design doc  │  │        / tech note   │  │  │        checklist    │  │  test exec   │
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
                         │  Jira: Sub-task      │                 │                     │
                         ├─────────────────────┤                 │                     │
                         │ - phase: string      │     ┌──────────┴──────────┐          │
                         │ - plan: string (YY)  │     │      SUMMARY         │          │
                         │ - type: PlanType     │     │  NN-YY-SUMMARY.md    │          │
                         │ - wave: int          │     │  Jira: Work log / PR │          │
                         │ - dependsOn: Plan[]  │     ├─────────────────────┤          │
                         │ - filesModified: []  │     │ - phase: string      │          │
                         │ - autonomous: bool   │     │ - plan: string       │          │
                         │ - requirements: []   │     │ - subsystem: string  │          │
                         │ - mustHaves: {}      │     │ - status:            │          │
                         │ - tasks: Task[]      │     │   complete|partial|  │          │
                         │ - verification: []   │     │   blocked            │          │
                         │ - successCriteria:[] │     │ - completed: date    │          │
                         ├─────────────────────┤     │ - techStack: {}      │          │
                         │ + execute() → Summary│     │ - keyFiles: {}       │          │
                         └──────────┬──────────┘     │ - decisions: []      │          │
                                    │                 │ - metrics: {}        │          │
                                    │                 │ - deviations: []     │          │
                                    │ produces        ├─────────────────────┤          │
                                    └────────────────►│ Updates STATE &      │          │
                                                      │ marks REQUIREMENTS   │──────────┘
                                                      │ complete             │ issues feed
                                                      └─────────────────────┘ back to UAT


┌──────────────────────────┐         ┌──────────────────────────┐
│         STATE             │         │       MILESTONE           │
│ .planning/STATE.md        │         │ .planning/MILESTONES.md   │
│ Jira: Board + Velocity    │         │ Jira: Epic               │
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
        │ Jira: Bug (investig.)│             │ - INTEGRATIONS.md │
        ├──────────────────────┤             │ - CONCERNS.md     │
        │ - symptoms: []        │             │ (no Jira equiv.)  │
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

  ── PARALLEL EPICS (MULTIPLE MILESTONES AT ONCE) ─────────────────────

    GSD natively supports only ONE active milestone at a time. A single
    ROADMAP.md, a single STATE.md, a single current position. When a
    milestone completes, it archives before the next one starts.

    For teams that need multiple Epics in flight simultaneously, three
    strategies exist — each with different trade-offs:

    ┌─────────────────────────────────────────────────────────────────┐
    │  STRATEGY A — FLATTEN EPICS INTO ONE MILESTONE (recommended)   │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │  Treat the milestone as a "Release" or "Sprint" that contains  │
    │  phases from multiple Epics. Tag each phase with its Epic:     │
    │                                                                 │
    │    ROADMAP.md:                                                  │
    │      ## Phase 1: User Auth        (EPIC-A, @alice)             │
    │      ## Phase 2: Payment Flow     (EPIC-B, @bob)               │
    │      ## Phase 3: Auth Roles       (EPIC-A, @alice)             │
    │      ## Phase 4: Checkout UI      (EPIC-B, @dave)              │
    │      ## Phase 5: Search Index     (EPIC-C, @carol)             │
    │      ## Phase 6: Integration      (ALL, @alice)                │
    │                                                                 │
    │  Phases from different Epics interleave freely. Dependencies   │
    │  are expressed via the dependsOn field as usual.               │
    │                                                                 │
    │  Pros: Single ROADMAP, single STATE, no tooling workarounds.   │
    │        Cross-Epic dependencies are visible and enforced.       │
    │        /gsd:progress shows true overall status.                │
    │        /gsd:audit-milestone catches gaps across all Epics.     │
    │                                                                 │
    │  Cons: ROADMAP grows large with many Epics.                    │
    │        Epic-level progress requires filtering by tag.          │
    │        Completing one Epic doesn't trigger milestone archive — │
    │        you wait until the full release ships.                  │
    │                                                                 │
    │  Best for: Teams shipping a single release with multiple       │
    │  feature tracks. Most common real-world scenario.              │
    └─────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────┐
    │  STRATEGY B — EPIC-PER-BRANCH (isolated .planning/ per Epic)   │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │  Each Epic lives on its own long-lived branch with its own     │
    │  independent .planning/ state:                                 │
    │                                                                 │
    │    main                                                        │
    │     ├── epic/user-auth       ← own ROADMAP, STATE, phases/    │
    │     ├── epic/payments        ← own ROADMAP, STATE, phases/    │
    │     └── epic/search          ← own ROADMAP, STATE, phases/    │
    │                                                                 │
    │  Each developer checks out their Epic branch, runs the full   │
    │  GSD lifecycle independently (/gsd:plan-phase, execute, etc). │
    │  On completion, the Epic branch merges to main — source code  │
    │  merges, but .planning/ can be gitignored or discarded.       │
    │                                                                 │
    │  Setup per Epic branch:                                        │
    │    git checkout -b epic/user-auth                              │
    │    /gsd:new-project          ← scoped to this Epic only       │
    │    /gsd:plan-phase 1                                           │
    │    /gsd:execute-phase 1                                        │
    │    ...                                                         │
    │    /gsd:complete-milestone 1.0.0                               │
    │    git merge epic/user-auth → main (source code only)         │
    │                                                                 │
    │  Pros: Full GSD lifecycle per Epic (plan, execute, verify,    │
    │        audit, complete). Clean isolation — no conflicts.       │
    │        Each Epic has its own progress, velocity, state.        │
    │                                                                 │
    │  Cons: Cross-Epic dependencies are invisible to GSD.           │
    │        No unified progress view across Epics.                  │
    │        Integration gaps only surface on merge to main.         │
    │        Requires discipline: rebase Epic branches regularly.    │
    │                                                                 │
    │  Best for: Truly independent feature tracks with minimal      │
    │  shared code. Open-source projects with parallel workstreams.  │
    └─────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────┐
    │  STRATEGY C — GIT WORKTREES (parallel directories, same repo)  │
    ├─────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │  Use git worktrees to have multiple checkouts of the same repo │
    │  on disk, each with its own .planning/ and branch:             │
    │                                                                 │
    │    ~/project/              ← main worktree (integration)       │
    │    ~/project-auth/         ← worktree for Epic A               │
    │    ~/project-payments/     ← worktree for Epic B               │
    │    ~/project-search/       ← worktree for Epic C               │
    │                                                                 │
    │  Setup:                                                        │
    │    git worktree add ../project-auth epic/user-auth             │
    │    git worktree add ../project-payments epic/payments          │
    │    cd ../project-auth && /gsd:new-project                     │
    │                                                                 │
    │  Each developer opens Claude Code in their worktree directory. │
    │  Full GSD lifecycle runs independently per worktree.           │
    │                                                                 │
    │  Pros: Physical isolation — no accidental cross-contamination. │
    │        Each dev has their own terminal, own Claude session.    │
    │        Same repo, shared git history, easy cherry-picks.       │
    │                                                                 │
    │  Cons: Same drawbacks as Strategy B (no cross-Epic visibility).│
    │        Disk space: full checkout per worktree.                  │
    │        Worktree management adds operational overhead.          │
    │                                                                 │
    │  Best for: Large codebases where devs need full isolation.    │
    │  Teams already using worktrees in their git workflow.          │
    └─────────────────────────────────────────────────────────────────┘

    ── DECISION GUIDE ──────────────────────────────────────────────

    Are your Epics          ──YES──►  Strategy A: Flatten
    shipping in the                   One milestone, phases tagged
    same release?                     by Epic. Simplest path.
         │
         NO
         │
    Do Epics share          ──YES──►  Strategy A: Flatten
    code (models,                     You need cross-Epic dependency
    APIs, schemas)?                   tracking. Flatten is safest.
         │
         NO
         │
    Do you already          ──YES──►  Strategy C: Worktrees
    use git worktrees?                Familiar workflow, add GSD.
         │
         NO
         │
         └──────────────────────────► Strategy B: Epic-per-branch
                                      Lightweight, branch-based.

    ── HYBRID APPROACH ─────────────────────────────────────────────

    In practice, most teams land on a hybrid:

    - Use Strategy A (flatten) for the CURRENT release — all Epics
      that will ship together live in one milestone.
    - Use Strategy B (epic-per-branch) for FUTURE Epics that are in
      early exploration/research but not yet committed to a release.
    - When a future Epic is ready, merge its phases into the active
      milestone via /gsd:add-phase.

    Timeline:
      Sprint N:    Milestone "v2.0" contains Epics A + B (flattened)
                   Epic C explored on separate branch (Strategy B)
      Sprint N+1:  Epic C phases added to "v2.0" via /gsd:add-phase
                   All three Epics now in one milestone (Strategy A)


  ── STRATEGY D — gsd-teams PLUGIN (shared team visibility) ───────────

    github.com/ianwsperber/gsd-teams (v0.1.2, MIT, 2026-02-06)

    A Claude Code plugin that adds a shared layer on top of GSD's
    local-only .planning/. It does NOT replace Strategies A–C — it
    complements them by making each developer's planning state
    visible to the rest of the team.

    Problem it solves: .planning/ is gitignored and local. When 4
    developers each run GSD independently (per-branch or per-
    worktree), there is no way to see each other's progress,
    milestones, or status without asking.

    Architecture — two directories:

      .planning/           ← local, gitignored (each dev's private state)
      .planning-shared/    ← committed to git (shared team state)

    .planning-shared/ structure:

      .planning-shared/
      ├── CHANGELOG.md              ← audit log of all share operations
      ├── MILESTONES.md             ← consolidated milestones (all devs)
      ├── STATUS.md                 ← consolidated status table
      ├── last_consolidated.json    ← version tracking (incremental)
      └── team/
          ├── alice/                ← flat snapshot of Alice's .planning/
          ├── bob/                  ← flat snapshot of Bob's .planning/
          └── ian/sessions/
              └── green/            ← parallel session (worktree support)

    Three commands:

      /gsd-teams:init
        Configures member identity and sync preferences.
        Sets member name and sync mode (full or shallow) in
        .planning/config.json under a "team" key.

      /gsd-teams:share
        Copies local .planning/ → .planning-shared/team/<member>/.
        Supports slash notation for parallel sessions:
          member "ian/green" → team/ian/sessions/green/
        Maintains audit trail in CHANGELOG.md.
        Same-day re-shares replace previous entry (no duplicates).

      /gsd-teams:consolidate
        Reads all member directories under .planning-shared/team/.
        Generates unified MILESTONES.md and STATUS.md.
        Incremental extraction (only new milestones since last run).
        Cleans stale sessions based on max_session_age_days config.

    Sync modes:
      full    — all planning files (default)
      shallow — summaries only (excludes codebase/, research/, debug/)

    Installation:

      /plugin marketplace add ianwsperber/gsd-teams
      /plugin install gsd-teams@gsd-teams

    How it fits with the strategies:

      Strategy A (flatten) + gsd-teams:
        All devs share one milestone, but each dev's branch-local
        .planning/ state is synced to .planning-shared/ for visibility.
        /gsd-teams:consolidate produces a unified STATUS.md.

      Strategy B/C (branch or worktree) + gsd-teams:
        Each dev has independent .planning/ per Epic. After each
        significant milestone, /gsd-teams:share pushes a snapshot.
        The consolidated view shows cross-Epic progress.

    Limitations:
      - Very young (all versions released on the same day)
      - Read-only consolidation — no conflict resolution
      - No bidirectional sync (share is one-way: local → shared)
      - No Jira integration (traceability via branch naming only)

  ── STRATEGY E — WORKSTREAM NAMESPACING (not yet shipped) ────────────

    Status: NOT AVAILABLE in GSD v1.22.4 (current installed version).

    Workstream namespacing (.planning/workstreams/) has been discussed
    as a potential GSD feature that would allow parallel milestones
    natively — each workstream maintaining its own ROADMAP.md,
    STATE.md, and phases/ under a namespace:

      .planning/
      ├── workstreams/
      │   ├── auth/
      │   │   ├── ROADMAP.md        ← independent milestone
      │   │   ├── STATE.md          ← independent progress
      │   │   └── phases/           ← independent phases
      │   ├── payments/
      │   │   ├── ROADMAP.md
      │   │   ├── STATE.md
      │   │   └── phases/
      │   └── search/
      │       ├── ROADMAP.md
      │       ├── STATE.md
      │       └── phases/
      ├── PROJECT.md                ← shared across workstreams
      ├── REQUIREMENTS.md           ← shared or per-workstream
      └── config.json               ← shared settings

    If/when shipped, this would eliminate the "one active milestone"
    constraint and make Strategies B/C unnecessary for most teams.
    Each /gsd:* command would accept a --workstream flag or infer
    the active workstream from the current working context.

    Until this ships, use Strategies A–D above.

    Check for availability:
      npx get-shit-done-cc@latest    ← update GSD
      /gsd:help                      ← look for workstream commands

  ── UPDATED DECISION GUIDE (with D and E) ────────────────────────────

    Are your Epics          ──YES──►  Strategy A: Flatten
    shipping in the                   One milestone, phases tagged
    same release?                     by Epic. Simplest path.
         │
         NO
         │
    Do Epics share          ──YES──►  Strategy A: Flatten
    code (models,                     Cross-Epic dependencies need
    APIs, schemas)?                   a single ROADMAP.
         │
         NO
         │
    Do you need team        ──YES──►  Add Strategy D: gsd-teams
    visibility across                 Install the plugin. Use with
    developers?                       any of A/B/C below.
         │
         │ (always consider D as an add-on, not a replacement)
         │
    Do you already          ──YES──►  Strategy C: Worktrees + D
    use git worktrees?                Familiar workflow, add GSD
         │                            + gsd-teams for visibility.
         NO
         │
         └──────────────────────────► Strategy B: Epic-per-branch + D
                                      Lightweight, branch-based,
                                      share snapshots via gsd-teams.


══════════════════════════════════════════════════════════════════════════════
 7. MID-SPRINT CHANGES: HANDLING NEW WORK IN AN AGILE WAY
══════════════════════════════════════════════════════════════════════════════

  Agile accepts that new work arrives mid-sprint. The question is never
  "can we prevent interruptions?" but "how do we triage, absorb, and
  track them without losing momentum on committed work?"

  GSD provides a different command for each type of arrival:

  ── TRIAGE DECISION TREE ─────────────────────────────────────────────

    New work arrives
         │
         ▼
    Is it urgent?  ──NO──►  Can it wait     ──YES──►  /gsd:add-todo
    (blocks users,          for next sprint?           Capture & park.
     security, SLA)                                    Review at sprint
         │                       │                     planning.
        YES                      NO
         │                       │
         ▼                       ▼
    Is it a bug    ──YES──► /gsd:debug
    requiring                Start investigation.
    investigation?           If fix is small → /gsd:quick
         │                   If fix is large → /gsd:insert-phase
         NO
         │
         ▼
    How big is     ──SMALL──► /gsd:quick
    the work?                 (< half day, well-understood)
         │
       MEDIUM                 A new phase within
         │                    current milestone.
         ▼
    Does it block  ──YES──► /gsd:insert-phase N "description"
    current work?            Creates Phase N.1 (urgent,
         │                   runs before Phase N+1)
         NO
         │
         ▼
    /gsd:add-phase "description"
    Appends to end of ROADMAP.
    Picked up after current work.

  ── PATTERN 1: CAPTURE & PARK (backlog grooming) ─────────────────────

    Most mid-sprint arrivals should NOT disrupt the current sprint.
    The Agile response: acknowledge, capture, defer.

    GSD command: /gsd:add-todo

    Scenario: Product owner reports a new feature request mid-sprint.

      Developer:  /gsd:add-todo "Add CSV export to reports (PM request)"
      Later:      /gsd:check-todos           ← during sprint planning
                  → Select todo → route to /gsd:add-phase or discard

    The todo is captured in .planning/todos/pending/ with context from
    the current conversation. STATE.md todo count increments. No sprint
    disruption.

    Jira parallel: Move ticket to backlog, tag for next sprint review.

  ── PATTERN 2: QUICK FIX (small, well-understood) ────────────────────

    For work that is clearly small (< half day) and doesn't need
    research, planning verification, or cross-phase coordination.

    GSD command: /gsd:quick

    Scenario: A typo in the API error message. A missing env variable
    in the deploy config. A CSS fix for mobile.

      Developer:  /gsd:quick
                  → Describe the task
                  → GSD creates a plan in .planning/quick/NNN-slug/
                  → Executes immediately with atomic commits
                  → Updates STATE.md

    Quick tasks live in .planning/quick/, separate from milestone
    phases. They don't touch ROADMAP.md or REQUIREMENTS.md.

    Jira parallel: Sub-task or Bug with "Quick Fix" label, done
    within the sprint without formal sprint scope change.

  ── PATTERN 3: URGENT INSERTION (blocks current sprint) ──────────────

    For work that MUST happen before the next planned phase — security
    patches, critical bugs, compliance fixes, production incidents.

    GSD command: /gsd:insert-phase <after> "description"

    Scenario: Security audit reveals an auth vulnerability. The team
    is mid-sprint, currently executing Phase 5. This must be fixed
    before Phase 6 (which depends on auth being solid).

      Tech lead:  /gsd:insert-phase 5 "Fix auth token validation (SEC-42)"
                  → Creates Phase 5.1 in ROADMAP
                  → Directory: .planning/phases/5.1-fix-auth-token/

      Developer:  /gsd:plan-phase 5.1
                  /gsd:execute-phase 5.1
                  → Phase 6 now depends on 5 AND 5.1

    ROADMAP after insertion:

      Phase 5:   API Endpoints          [x] complete
      Phase 5.1: Fix Auth Token (SEC-42) [ ] ← INSERTED, URGENT
      Phase 6:   Integration Tests       [ ] depends on: 5, 5.1

    The decimal numbering (5.1) preserves the existing phase order
    without renumbering. Multiple insertions stack: 5.1, 5.2, etc.

    Jira parallel: Add ticket to current sprint, flag as blocker,
    re-prioritize sprint backlog.

  ── PATTERN 4: NEW EPIC ARRIVES (scope expansion) ────────────────────

    A new Epic surfaces mid-sprint. Too large for a quick fix, but
    the business wants it in the current release.

    GSD commands: /gsd:add-phase (multiple times) + tag with Epic

    Scenario: Sales closes a deal contingent on a "Single Sign-On"
    feature. The team is mid-milestone with 3 phases remaining.

      Step 1 — Capture without disrupting:
        /gsd:add-todo "SSO Epic: SAML + OAuth integration (DEAL-99)"

      Step 2 — At next standup/planning, scope it:
        /gsd:add-phase "SSO: SAML Provider Setup (EPIC-D, @alice)"
        /gsd:add-phase "SSO: OAuth Flow (EPIC-D, @bob)"
        /gsd:add-phase "SSO: Account Linking (EPIC-D, @carol)"

      Step 3 — ROADMAP now shows existing + new phases:
        Phase 7:  Search Indexing     (EPIC-C, @carol)   [current]
        Phase 8:  Admin Dashboard     (EPIC-C, @dave)
        Phase 9:  SSO: SAML Setup     (EPIC-D, @alice)   ← NEW
        Phase 10: SSO: OAuth Flow     (EPIC-D, @bob)     ← NEW
        Phase 11: SSO: Account Link   (EPIC-D, @carol)   ← NEW
        Phase 12: Integration Tests   (ALL, @alice)

      Step 4 — If SSO is more urgent than remaining EPIC-C work,
      use /gsd:insert-phase to prioritize it higher, or simply
      re-order phases in ROADMAP.md manually.

    Jira parallel: Create new Epic with Stories, add to current
    sprint or plan for next sprint depending on priority.

  ── PATTERN 5: BUG INVESTIGATION (unknown scope) ─────────────────────

    A bug is reported but the root cause is unclear. The fix might be
    a one-liner or might require a phase of rework.

    GSD command: /gsd:debug "description"

    Scenario: Users report intermittent 500 errors on checkout.

      Step 1 — Start investigation:
        /gsd:debug "Intermittent 500 on checkout flow"
        → Creates .planning/debug/intermittent-500-checkout.md
        → GSD gathers symptoms, forms hypotheses, tests them

      Step 2 — Investigation reveals the scope:

        IF small fix:
          /gsd:quick                    ← fix inline, atomic commit
          Debug session archived to .planning/debug/resolved/

        IF medium fix (affects one phase's code):
          /gsd:insert-phase 5 "Fix checkout race condition"
          /gsd:plan-phase 5.1
          /gsd:execute-phase 5.1

        IF large fix (cross-cutting, needs rearchitecting):
          /gsd:add-phase "Refactor checkout state management"
          /gsd:add-phase "Checkout integration tests"
          → Plan and execute as regular phases

    Debug sessions persist across /clear — if context fills up,
    run /gsd:debug with no args to resume from where you left off.

    Jira parallel: Bug ticket starts as investigation, then spawns
    sub-tasks or new stories depending on discovered scope.

  ── TEAM COORDINATION: WHO HANDLES WHAT? ─────────────────────────────

    Arrival Type        Who Decides         Who Executes
    ──────────────────  ──────────────────  ──────────────────────────
    Todo (park it)      Any developer       Deferred to sprint planning
    Quick fix           Developer + lead    Developer on current branch
    Urgent insertion    Tech lead / PO      Developer with capacity
    New Epic            PO + tech lead      Planned at team level
    Bug investigation   Developer who       Same dev, escalate if large
                        encounters it

    Sprint ceremonies that map to GSD:

    Daily standup:
      Each dev runs /gsd:progress on their branch to report status.
      Blocked devs surface blockers from STATE.md.

    Mid-sprint review (if scope changes):
      Tech lead reviews ROADMAP.md with new insertions/additions.
      Team agrees on re-prioritization.
      Update phase assignments (tags in ROADMAP.md).

    Sprint planning:
      /gsd:check-todos to review captured ideas.
      Promote todos → phases via /gsd:add-phase.
      Assign phases to developers, set dependencies.

    Sprint retrospective:
      Review .planning/quick/ — were too many quick fixes needed?
      Review .planning/debug/resolved/ — recurring bug patterns?
      Check decimal phases (5.1, 7.1) — too many urgent insertions
      suggests upstream planning gaps.

  ── PROTECTING SPRINT COMMITMENTS ────────────────────────────────────

    The Agile principle: the team commits to sprint scope, and scope
    changes require explicit trade-offs. GSD enforces this through
    separation of mechanisms:

    ┌────────────────────┬────────────────────┬────────────────────┐
    │ Mechanism          │ Touches ROADMAP?   │ Disrupts sprint?   │
    ├────────────────────┼────────────────────┼────────────────────┤
    │ /gsd:add-todo      │ No                 │ No — just captures │
    │ /gsd:quick         │ No                 │ Minimal — small    │
    │ /gsd:insert-phase  │ Yes (adds N.1)     │ Yes — explicit     │
    │ /gsd:add-phase     │ Yes (appends)      │ No — future work   │
    │ /gsd:debug         │ No (until scoped)  │ Depends on outcome │
    └────────────────────┴────────────────────┴────────────────────┘

    Rule of thumb:
    - If it doesn't touch ROADMAP.md, it's not a sprint scope change.
    - If it inserts a decimal phase, it IS a scope change — requires
      tech lead / PO sign-off.
    - If it appends to the end, it's future work — discuss at next
      sprint planning.

  ── VELOCITY IMPACT TRACKING ─────────────────────────────────────────

    To measure how much mid-sprint work affects velocity:

    1. Planned phases:  Integer-numbered (1, 2, 3, ...)
       → Count toward sprint commitment velocity.

    2. Inserted phases: Decimal-numbered (5.1, 7.2, ...)
       → Track separately as "unplanned work."

    3. Quick tasks:     In .planning/quick/
       → Track separately as "interrupt-driven work."

    Sprint health metric:
      planned_phases_completed / total_phases_completed

    If this ratio drops below 0.7, the team is spending more than
    30% of capacity on unplanned work — a signal to improve upstream
    planning, backlog grooming, or production stability.

    STATE.md velocity section tracks per-phase duration. Compare:
    - Average duration of planned phases vs. inserted phases
    - Trend over sprints: is unplanned work increasing?
```
