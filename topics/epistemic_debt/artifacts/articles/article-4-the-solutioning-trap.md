---
title: The Solutioning Trap
subtitle: One concrete way to slow down before the model commits
status: draft
type: article
audience:
- technical professionals
- engineering leaders
- senior practitioners
target_length: 1800
current_length: 1280
estimated_reading_time: 9 min
created: 2026-02-15
last_updated: 2026-04-12
published_date: null
publication_url: ''
social_teasers:
  linkedin: |
    Two moments where LLM-assisted code tends to fail: before the model locks in what you meant, and before it locks in which path to take. I have been experimenting with two small prompt expansions, `<asin>` and `<soltree>`, as deliberate pauses at those moments.

    They are not magic. They are patterns you can paste even without the tiny Claude Code helper I use to inject them. The article is a practical walkthrough with examples, not a pitch.

    If you have your own rituals for slowing the model down, what are they?

    #LLM #SoftwareEngineering #PromptEngineering #AICoding #EpistemicDebt
  twitter: "Two moments where LLM-assisted code goes wrong: before the model interprets the problem, and before it commits to a path. Two macros, `<asin>` and `<soltree>`, one deliberate pause each. I wrote about using them with Claude Code. [article link]"
  instagram_caption: |
    LLM code fails twice: wrong assumptions first, then the first plausible design. Article 4 is about two macros, `<asin>` and `<soltree>`, that force a pause before each mistake.

    Link in bio for the full piece.

    #AICoding #LLM #SoftwareEngineering #DeveloperTools #PromptEngineering #ClaudeCode #VibeCoding #EpistemicDebt #TechReading #CodeQuality #DevLife #AIAssistants
  substack_notes: "Article 4 is up on the solutioning trap. Two small macros, `<asin>` and `<soltree>`, that I use to slow myself down before the model commits to a path I will regret. [article link]"
---

# The Solutioning Trap

*One concrete way to slow down before the model commits*

----

*This is Part 4 of 7 in the series on [epistemic debt — when AI generation outpaces human comprehension](https://antoninorau.substack.com/p/epistemic-debt-when-ai-generation).*

----

The core problem is not inexperience. It is jumping to a solution before clarifying the epistemic scope of the problem, and LLMs make that jump frictionless. Andrej Karpathy popularized the term "vibe coding" in early 2025 as a label for fast, low-checking iteration with models. The mechanism is simple: problem, prompt, code, ship. When the code looks idiomatic and tests pass, the missing step, a shared picture of what the system must assume, is easy to skip.

This is the **solutioning trap**: implementing before you and the model mean the same thing by the problem. Article 3 named four patterns this trap produces in practice: the system boundary gap, the defensive coding gap, the edge case reasoning gap, and the Stochastic Spaghetti Effect, code that works but encodes implicit assumptions in ways that resist human comprehension. The question here is what to do at the keyboard before those patterns harden.

## Why It's So Easy to Fall In

Automation bias names the well-documented tendency to weight machine output more heavily than competing signals, a tendency that strengthens, not weakens, as familiarity grows (Parasuraman & Manzey, 2010). That matters because the first plausible answer from an assistant arrives with high fluency and high finish, so it crowds out the slower work of asking what was never said out loud.

Processing fluency is the companion mechanism. Cleanly formatted, idiomatic code is easier to read, and ease of processing is consistently misattributed as evidence of correctness (Reber & Schwarz, 1999). LLM output is tuned for fluency, which makes the trap feel like competence. In a 2026 Anthropic Fellows randomized controlled trial, developers using AI assistance scored 17 percentage points lower on a quiz covering concepts they had used just minutes earlier (Shen & Tamkin, 2026, arXiv:2601.20245). The biases explain the pull; the quiz gap is one sobering measure of what slips through when we move fast.

## A Concrete Way I Am Trying To Slow Down

pmacros is a small Claude Code tool I have been using. It is a UserPromptSubmit hook that expands short `<tagname>` tags into longer prompt text before Claude sees the prompt, with macros stored per-user or per-project. It is open source in spirit and still rough; nothing here is a product pitch.

I am not pitching pmacros. It is one concrete way I am operationalizing two defenses I keep wishing I had. The macros below are valuable as prompt patterns even if you never install the tool. Adopt them, adapt them, or ignore them. The two macros below are proposed defaults for pmacros and may not yet ship in the upstream tool at the time you read this.

## `<asin>`: Surface What the Model Is About to Assume

The first failure mode is silent assumption-baking and misread intent. `<asin>` interrupts before the model commits. This sits in the same family as Chain-of-Verification (Dhuliawala et al., 2023, arXiv:2309.11495), which shows that forcing a model to externalize its reasoning before committing reduces error. `<asin>` adapts that idea for assumption-baking, before the model commits to a path.

```
Before you answer my substantive request, produce the following four sections, in this exact order, as separate explicit headings or labeled blocks. Use clear labels so I can scan them quickly.

1. **LLM assumptions** — List the assumptions you are about to make based on your training defaults and prior knowledge of similar problems. These are choices you would silently make if I did not stop you.

2. **Prompt-derived assumptions** — List the assumptions you have inferred from my prompt that I did not explicitly state. These are gaps you have filled in by reading between the lines.

3. **Gaps** — List what is missing, unknown, or underspecified that would change your answer if clarified. Do not guess. Mark each item as something I should answer.

4. **User intent (as you understand it)** — Restate, in one or two sentences, what you believe I am actually trying to accomplish. If you are uncertain, say so.

After producing these four sections, STOP. Wait for me to confirm or correct before proceeding to the answer.
```

**Worked example (rate limiting).** Prompt: `Add rate limiting to our API. <asin>`. The model might surface: in-memory token bucket as default (**LLM assumptions**), single-instance and per-IP scope (**Prompt-derived assumptions**), scaling, burst policy, Redis, response shape (**Gaps**), protect downstream without annoying real users (**User intent**). You can correct topology before any middleware exists.

## `<soltree>`: Surface Paths Before Picking One

The second failure mode is collapsing to the first plausible solution. Tree of Thoughts (Yao et al., 2023, arXiv:2305.10601) demonstrated that deliberate consideration of alternative reasoning paths outperforms greedy commitment. `<soltree>` puts that branch decision in the human's hands instead of letting the model search internally.

```
This task is INTERACTIVE and NON-EXHAUSTIVE. You will surface 2 to 4 plausible alternatives only, not an exhaustive tree.

1. Before implementing or recommending any approach, identify the decision point at the root of this problem. State it in one sentence.

2. Surface 2 to 4 plausible alternative paths from this decision point. Do NOT attempt to be exhaustive. Include at least one path that you would NOT have offered by default, something a thoughtful practitioner might consider but that is not the obvious first answer.

3. For each alternative, give: (a) a one-line description, (b) one line on what it optimizes for, (c) one line on its main tradeoff or risk.

4. Do NOT pick. STOP after presenting the alternatives and ask: "Which of these would you like me to pursue, or would you like me to surface different ones?" Wait for my answer before doing anything else.
```

**Worked example (authentication).** Prompt: `Add user authentication to our internal admin app. <soltree>`. Branches might be session cookies with bcrypt, OAuth via an existing IdP, magic link email, and reverse-proxy auth with Authelia or oauth2-proxy (the non-default path a solo model pass might skip). It should end with: Which of these would you like me to pursue, or would you like me to surface different ones? If nginx already terminates TLS, reverse-proxy auth can avoid password storage entirely.

## What These Two Macros Are Really Doing

In the vocabulary of Article 2, both macros are attempts to delay t₀, the moment epistemic debt becomes load-bearing in the system. They move the moment of correction earlier, before the model has committed to a path that future work will build on.

These two macros are local defenses. They are not a strategy. The next article in the series, *The Trade-off Triangle*, asks the larger question: where on the Speed/Understanding/Reliability triangle does this kind of work belong, and how do you choose consciously instead of by default?

----

*If you found this article valuable, I'd love to hear your thoughts. Please leave a comment, share it, and eventually [subscribe for **free**](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

----

## References

- Karpathy, A. (February 2025). "Vibe coding" concept introduction.
- Parasuraman, R. & Manzey, D.H. (2010). "Complacency and Bias in Human Use of Automation." *Human Factors*, 52(3), 381-410.
- Reber, R. & Schwarz, N. (1999). "Effects of perceptual fluency on judgments of truth." *Consciousness and Cognition*, 8(3), 338-342.
- Shen, J. H. & Tamkin, A. (2026). "How AI Impacts Skill Formation." arXiv:2601.20245.
- Dhuliawala, S. et al. (2023). "Chain-of-Verification Reduces Hallucination in Large Language Models." arXiv:2309.11495.
- Yao, S. et al. (2023). "Tree of Thoughts." NeurIPS 2023. arXiv:2305.10601.
