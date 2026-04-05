# Glossary

Shared terminology and definitions used across articles in this repository. AI assistants should reference these definitions for consistent language.

---

## General Terms

### Epistemic
Relating to knowledge—how we know what we know, the justification for beliefs, and the conditions under which we can claim to understand something.

### Epistemic Warrant
The justification or grounding for claiming to understand something. In software, this traditionally came from the causal chain of authorship—you know the code because you wrote it.

### Epistemic Opacity
A state where the reasoning behind a system's behavior is hidden or inaccessible. Code can be epistemically opaque when developers cannot explain why it works.

---

## Epistemic Debt Topic

> **Note on framework status:** The epistemic debt framework presented in this series is a **theoretical model**, not an empirically validated one. The existing research base is small, with limited population sizes and data points. Some studies cited come from companies with commercial interests in LLM-assisted coding. The framework should be understood as an initial conceptual lens for reasoning about comprehension gaps in AI-assisted development — useful for guardrailing and iterative learning, but not yet established as empirical science. Terms below marked *(Author's term)* are introduced by the series author; terms marked *(Preprint)* come from non-peer-reviewed sources.

### Epistemic Debt
(Author's framework.) Code that works but nobody understands. Analogous to technical debt, but instead of future maintenance cost, it represents future comprehension cost. Epistemic debt accumulates when developers accept code without fully understanding its behavior. The formal model (Ed integral, cascade multipliers, layer taxonomy) is a theoretical construct introduced in this series, drawing on Ngabang (2026, preprint) for notation.

**Contrast with Technical Debt:**
- **Technical debt**: Code that works but is hard to change
- **Epistemic debt**: Code that works but nobody understands

### Solutioning Trap
(Author's term.) The pattern of jumping to implementation before adequately defining the problem. LLMs exacerbate this by reducing friction between idea and code, making it trivially easy to generate solutions before understanding the problem's epistemic scope.

### Construction Paradigm
(Author's term.) The traditional model of software development where the engineer is the architect of every decision. The developer constructs the logical artifact, and understanding derives from the labor of creation.

### Curation Paradigm
(Author's term.) The emerging model where developers review and select from probabilistically-generated suggestions rather than constructing code directly. Understanding must be actively established rather than assumed from authorship.

### Epistemic Boundary
(Author's term.) Points in the software development lifecycle where meaning must be translated from one form to another:
1. **Intent → Specification**: User needs become requirements
2. **Specification → Implementation**: Requirements become code
3. **Implementation → Validation**: Code is tested against intent

Epistemic debt can accumulate at each boundary.

### Circular Validation
(Author's term.) When LLM-generated tests validate LLM-generated code, creating a closed loop that may not validate actual intent. The tests pass, but they don't cross an epistemic boundary to verify the code does what humans intended. Related to what IBM Research's Kush Varshney calls the "validating validators" problem — the challenge of ensuring AI evaluators don't amplify their own errors in a feedback loop (Pan et al., 2024; Varshney in IBM Think, 2025).

### Velocity Trap
(Author's term.) The tendency to optimize for speed of code generation while accumulating epistemic debt. LLMs enable generating entire features quickly, but understanding may not keep pace, leading to compounding gaps before teams notice.

### Epistemic Credit
A formal measure of the justification or warrant for a claim; in epistemic-debt discourse, often used to contrast with epistemic debt (credit as positive warrant, debt as deficit of understanding).

### Automation Bias
The tendency to over-trust or over-rely on automated systems (e.g. LLM suggestions) and under-weight contradictory human judgment, leading to uncritical acceptance of generated output.

### Stochastic Spaghetti Effect
(Ngabang, 2026 — viXra preprint, not peer-reviewed.) The entanglement of probabilistically generated code and dependencies such that cause-effect and ownership become hard to trace, compounding epistemic opacity. The viXra admin note on this paper suggests it may have been AI-generated; the term is used in this series as a descriptive label, not as an endorsement of the source's methodology.

### Context Window Amnesia
(Ngabang, 2026 — viXra preprint, not peer-reviewed.) The limitation that LLMs have no persistent memory outside the current context window, so earlier decisions or constraints can be "forgotten" within a long session or document.

### Vibe Coding
(Karpathy, 2025.) Coding by iterating on LLM output until it "feels right" or passes tests, without necessarily establishing causal understanding of how the code works.

### Vibe Designing
(Author's term.) Using AI as a cognitive lever for deeper problem modeling and intentional design rather than rapid code generation. Emphasizes pre-prompting (domain invariants, edge cases, entity lifecycles), Socratic questioning of assumptions, and design exploration; positions AI as a thinking partner rather than a replacement for judgment.

### Spec-Driven Development
(Thoughtworks, 2025.) An approach where specifications are written and maintained as the source of truth, and code (including LLM-generated code) is validated against them to preserve epistemic boundaries.

### Epistemia
(Quattrociocchi et al., 2025.) A proposed measure or framework for epistemic quality or reliability of information (e.g. in socio-technical systems), relevant to assessing understanding and trust.

### Rubber-Stamp Culture
The pattern of approving or merging LLM-generated or suggested changes without substantive review, which accelerates delivery but can increase epistemic debt and automation bias.

### Trade-off Triangle
(Author's framework.) The framework that pits three competing goals — speed, ownership/understanding, and quality — such that optimizing one constrains the others; used to reason about epistemic debt vs. velocity. This is a theoretical construct, not an empirically measured relationship.

### Bus Factor
The number of people who must be unavailable before a project or codebase loses critical knowledge; in epistemic-debt terms, low bus factor plus opaque code increases risk.

---

## Guardrails & Practices

### Domain-Driven Design (DDD)
A software design approach that emphasizes modeling the domain with a ubiquitous language shared between developers and domain experts. In the context of epistemic debt, DDD front-loads epistemic work into problem definition and creates verification criteria.

### Ubiquitous Language
A shared vocabulary between developers and stakeholders that precisely defines domain concepts. Serves as an epistemic anchor when LLMs generate code—the code should express the domain's shared language.

### E2E Integration Testing
End-to-end tests that validate system behavior against requirements rather than implementation details. Crosses epistemic boundaries by verifying that the system does what users intended, not just that code matches other code.

---

## Publication & Distribution

### Cross-posting
Publishing or promoting content across multiple platforms with platform-specific adaptations in tone, format, and length.

### Social Teaser
A short, platform-adapted excerpt designed to drive traffic to the primary publication (Substack).

### Substack Notes
Substack's native short-form posting feature, used for organic discovery within the Substack ecosystem.

### Distribution Layer
The workflow stage between content export and audience reach — encompasses publishing, cross-posting, and promotion across channels.

---

## Usage Notes for AI

When writing about these topics:
- Use "epistemic debt" as the primary accessible framing (more actionable than "epistemic warrant")
- Prefer "understanding" over "knowledge" when discussing developer comprehension
- Frame guardrails as "practices worth examining" rather than prescriptive solutions
- Acknowledge the velocity vs. ownership trade-off without being prescriptive
- **Theoretical status:** The epistemic debt framework is a theoretical model with early-stage empirical signals, not established science. Present evidence as "initial confirmation" or "consistent with the model," not as proof
- **Attribution:** Distinguish between (a) author-introduced terms, (b) Ngabang (2026, viXra preprint — not peer-reviewed), and (c) peer-reviewed/established sources. Never cite Ngabang without the preprint disclosure
- **Research limitations:** The evidence base has small sample sizes, limited populations, and potential conflicts of interest from companies with commercial stakes in LLM-assisted coding. Acknowledge these limitations when presenting data
