---
description: "Command: Start Planning in detail a specific phase of a plan with dependency checking and assumption analysis. DO not execute the detailed plan, only plan it. Create Trade Off analysis and assumptions as a table in the plan file."
alwaysApply: false
---

# Create Execution Plan for Phase

Reusable command to plan a specific phase from a plan file in detail. Replace
the placeholders before invoking.

## Placeholders

| Placeholder          | Description                                  | Example                                                                  |
| -------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| `{{PLAN_FILE}}`      | Path to the plan file                        | `.cursor/plans/substack_publication_workflow_a205b421.plan.md`            |
| `{{PHASE_NUMBER}}`   | Phase number to plan in detail                      | `3`                                                                      |

## Prompt

I want to start planning in detail **Phase {{PHASE_NUMBER}}** of the plan in
`{{PLAN_FILE}}`.

Before we begin, complete the following checks and then discuss the phase
with me interactively. Do not execute the detailed plan, only plan it. Create Trade Off analysis and assumptions as a table in the plan file.

---

### 1. Dependency Check

**Intra-plan (within the plan file):**

- Read the plan file and identify every phase prior to Phase {{PHASE_NUMBER}}.
- Confirm each prior phase is marked as completed (e.g., status ✅ COMPLETED)
  or is explicitly not a prerequisite for Phase {{PHASE_NUMBER}}.
- If any prerequisite phase is incomplete, list what remains and ask whether
  to proceed anyway or address the dependency first.

**Cross-plan (across all plan files):**

- Scan all other plan files in `.cursor/plans/` for tasks or phases that
  Phase {{PHASE_NUMBER}} depends on -- shared resources, configuration outputs,
  generated files, or documented prerequisites.
- Flag any unmet cross-plan dependencies and explain the risk of proceeding
  without them.

---

### 2. Step-by-Step Discussion

Walk me through each step or task within Phase {{PHASE_NUMBER}}:

- What it involves and what its deliverable is.
- Which files, directories, or external resources it touches.
- Any decisions I need to make or trade-offs to consider.
- Ask me clarifying questions before proceeding with planning.

Do **not** start planning until we have discussed all steps and I give
explicit approval to plan.

---

### 3. Assumptions and Unknowns

After the discussion, compile three lists:

- **Assumptions** -- things we are taking for granted about the environment,
  existing state, available tools, credentials, or conventions.
- **Known unknowns** -- things we know we don't know yet and need to resolve
  (e.g., missing credentials, undecided formats, unclear requirements).
- **Unknown unknowns** -- potential blind spots, edge cases, or risks that
  are not explicitly addressed by the plan but could surface during planning.
