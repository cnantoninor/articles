# Macro artifact: `<soltree>`

## Section 1: Front-matter

```yaml
---
macro: soltree
full_name: solution tree exploration
type: pmacros default macro
injection_mode: manual (expands when `<soltree>` appears in prompt)
position: inline
prior_art: "Tree of Thoughts (Yao et al., 2023, NeurIPS, arXiv:2305.10601)"
status: draft
---
```

## Section 2: Purpose

`<soltree>` is a defense against the second failure mode of the solutioning trap: collapsing to the first plausible solution and never revealing that alternatives existed. The macro forces the LLM to surface two to four plausible alternative paths from the problem root, name their tradeoffs briefly, and STOP, waiting for the user to pick one before proceeding. The contract is INTERACTIVE: the model must wait, not auto-pick. It is NON-EXHAUSTIVE: two to four branches, not a full search. It adapts the Tree of Thoughts insight, that deliberate alternative-path exploration outperforms greedy commitment, into an interactive single-shot format. This is adaptation, not a claim of ToT novelty.

## Section 3: Macro body (the literal text pmacros injects)

```
This task is INTERACTIVE and NON-EXHAUSTIVE. You will surface 2 to 4 plausible alternatives only, not an exhaustive tree.

1. Before implementing or recommending any approach, identify the decision point at the root of this problem. State it in one sentence.

2. Surface 2 to 4 plausible alternative paths from this decision point. Do NOT attempt to be exhaustive. Include at least one path that you would NOT have offered by default, something a thoughtful practitioner might consider but that is not the obvious first answer.

3. For each alternative, give: (a) a one-line description, (b) one line on what it optimizes for, (c) one line on its main tradeoff or risk.

4. Do NOT pick. STOP after presenting the alternatives and ask: "Which of these would you like me to pursue, or would you like me to surface different ones?" Wait for my answer before doing anything else.
```

## Section 4: Worked example

- **Original user prompt:** `Add user authentication to our internal admin app. <soltree>`
- **What `<soltree>` injects:** The full prompt body from Section 3 (not repeated here).
- **Expected model output:**
  - **Decision point:** Whether to own credentials inside the app or delegate identity to something the organization already runs.
  - **Branch 1 (session cookies + bcrypt):** (a) Classic session cookies with server-side sessions and bcrypt password hashes. (b) Optimizes for full control and simple mental model on one host. (c) Tradeoff: you own password storage, rotation, and breach response.
  - **Branch 2 (OAuth via existing IdP):** (a) OAuth against Google Workspace or similar IdP the company already pays for. (b) Optimizes for no password storage and SSO alignment. (c) Tradeoff: dependency on IdP uptime and OAuth flow complexity.
  - **Branch 3 (magic link email):** (a) Passwordless magic links sent by email. (b) Optimizes for low user friction and no password resets. (c) Tradeoff: email deliverability and token expiry edge cases.
  - **Branch 4 (reverse-proxy auth, non-default):** (a) Terminate auth at nginx with Authelia or oauth2-proxy in front of the app. (b) Optimizes for zero credential logic inside the app when a reverse proxy already exists. (c) Tradeoff: operational coupling to proxy config and header trust boundaries.
  - **Verbatim stop signal:** Which of these would you like me to pursue, or would you like me to surface different ones?
- **How this changes the interaction:** You can choose reverse-proxy auth because the app already sits behind nginx, avoiding password storage entirely. The model might not have surfaced that branch without the macro's non-default path requirement.

## Section 5: Prior art

Tree of Thoughts (ToT) is a framework in which Yao et al. (2023), NeurIPS, arXiv:2305.10601, explore multiple reasoning paths as a tree rather than a single chain, improving performance on tasks where greedy first answers fail. ToT showed that deliberate consideration of alternatives outperforms greedy commitment to the first plausible solution. `<soltree>` adapts that insight by exposing branch points to the human as a decision moment instead of letting the model search internally. The interactive stop-and-ask contract and the two-to-four alternative budget are this artifact's framing; ToT is the conceptual ancestor.
