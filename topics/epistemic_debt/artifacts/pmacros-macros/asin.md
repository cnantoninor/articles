# Macro artifact: `<asin>`

## Section 1: Front-matter

```yaml
---
macro: asin
full_name: assumption + intent surfacing
type: pmacros default macro
injection_mode: manual (expands when `<asin>` appears in prompt)
position: inline
prior_art: "Chain-of-Verification (Dhuliawala et al., 2023, arXiv:2309.11495)"
status: draft
---
```

## Section 2: Purpose

`<asin>` is a defense against the first failure mode of the solutioning trap: silently baked-in assumptions and misread intent. The macro forces the LLM to externalize, before answering, what it is about to assume and what it understands the user wants. It adapts the Chain-of-Verification idea, which forces the model to externalize its reasoning before committing, for interactive use against assumption-baking rather than post-hoc factual hallucination. This is adaptation, not a claim of CoVe novelty.

## Section 3: Macro body (the literal text pmacros injects)

```
Before you answer my substantive request, produce the following four sections, in this exact order, as separate explicit headings or labeled blocks. Use clear labels so I can scan them quickly.

1. **LLM assumptions** — List the assumptions you are about to make based on your training defaults and prior knowledge of similar problems. These are choices you would silently make if I did not stop you.

2. **Prompt-derived assumptions** — List the assumptions you have inferred from my prompt that I did not explicitly state. These are gaps you have filled in by reading between the lines.

3. **Gaps** — List what is missing, unknown, or underspecified that would change your answer if clarified. Do not guess. Mark each item as something I should answer.

4. **User intent (as you understand it)** — Restate, in one or two sentences, what you believe I am actually trying to accomplish. If you are uncertain, say so.

After producing these four sections, STOP. Wait for me to confirm or correct before proceeding to the answer.
```

## Section 4: Worked example

- **Original user prompt:** `Add rate limiting to our API. <asin>`
- **What `<asin>` injects:** The full prompt body from Section 3 (not repeated here).
- **Expected model output (sketch):**
  - **LLM assumptions:** I will use an in-memory token bucket because it is the canonical pattern in tutorials I have seen most often.
  - **Prompt-derived assumptions:** Single-instance deployment, one application server, per-IP limits.
  - **Gaps:** Horizontal scaling? Burst tolerance? Per-user vs per-IP? Is Redis available? What error response is expected on rate-limit exceedance?
  - **User intent (as I understand it):** Protect downstream services from abuse, with low false positives during normal traffic spikes.
- **How this changes the interaction:** You can correct "single instance" to "horizontally scaled, four pods" before any code is generated, instead of discovering the mismatch after the model has already committed to an implementation.

## Section 5: Prior art

Chain-of-Verification (CoVe) is a prompting approach in which Dhuliawala et al. (2023), arXiv:2309.11495, ask the model to draft, plan verification questions, answer them, and then commit to a final answer, reducing factual errors. `<asin>` sits in the same family as CoVe: both force external reasoning before commitment. It differs in two ways: (1) it surfaces assumptions and intent, not only verification questions about a draft, and (2) it operates as an interactive stop point rather than an internal multi-step process. The four-category split and the `<tag>`-based injection are this article's framing; the underlying idea of forcing externalization is borrowed from CoVe.
