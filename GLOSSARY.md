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

### Epistemic Debt
Code that works but nobody understands. Analogous to technical debt, but instead of future maintenance cost, it represents future comprehension cost. Epistemic debt accumulates when developers accept code without fully understanding its behavior.

**Contrast with Technical Debt:**
- **Technical debt**: Code that works but is hard to change
- **Epistemic debt**: Code that works but nobody understands

### Solutioning Trap
The pattern of jumping to implementation before adequately defining the problem. LLMs exacerbate this by reducing friction between idea and code, making it trivially easy to generate solutions before understanding the problem's epistemic scope.

### Construction Paradigm
The traditional model of software development where the engineer is the architect of every decision. The developer constructs the logical artifact, and understanding derives from the labor of creation.

### Curation Paradigm
The emerging model where developers review and select from probabilistically-generated suggestions rather than constructing code directly. Understanding must be actively established rather than assumed from authorship.

### Epistemic Boundary
Points in the software development lifecycle where meaning must be translated from one form to another:
1. **Intent → Specification**: User needs become requirements
2. **Specification → Implementation**: Requirements become code
3. **Implementation → Validation**: Code is tested against intent

Epistemic debt can accumulate at each boundary.

### Circular Validation
When LLM-generated tests validate LLM-generated code, creating a closed loop that may not validate actual intent. The tests pass, but they don't cross an epistemic boundary to verify the code does what humans intended.

### Velocity Trap
The tendency to optimize for speed of code generation while accumulating epistemic debt. LLMs enable generating entire features quickly, but understanding may not keep pace, leading to compounding gaps before teams notice.

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
