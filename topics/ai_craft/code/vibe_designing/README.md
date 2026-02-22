# Vibe Designing - TAM4 Code Examples

This directory contains the Python code examples from the "From Vibe Coding to Vibe Designing" article, demonstrating tools for systematic design exploration and AI-assisted problem modeling.

## Files Structure

### Core Frameworks
- **`domain_modeling.py`** - Domain modeling framework for pre-prompting analysis
- **`socratic_prompting.py`** - Socratic questioning system for challenging assumptions  
- **`assumption_tracking.py`** - Assumption validation and evidence tracking
- **`design_exploration.py`** - Design alternative exploration and comparison tools

### Demo and Tests
- **`vibe_designing_demo.py`** - Interactive demonstration of the complete workflow
- **`test_*.py`** - Comprehensive test suites for each module
- **`requirements.txt`** - Python dependencies
- **`__init__.py`** - Package initialization

## Running the Code

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Interactive Demo
```bash
python vibe_designing_demo.py
```

### Run All Tests
```bash
pytest -v
```

### Run Specific Test Module
```bash
pytest test_domain_modeling.py -v
pytest test_socratic_prompting.py -v
pytest test_assumption_tracking.py -v
pytest test_design_exploration.py -v
```

## Key Concepts Demonstrated

### 1. Domain Modeling (Before Prompting - 3 minutes)
The `domain_modeling.py` module shows how to systematically capture:
- **Domain Invariants**: Business rules that must always hold
- **Edge Cases**: Potential failure modes and their mitigations
- **Entity Lifecycles**: State transitions and business events
- **Assumptions**: Things we believe but haven't validated

```python
from domain_modeling import DomainModelBuilder, EntityLifecycleState

model = (DomainModelBuilder("User Auth System", "Secure user authentication")
    .with_invariant("unique_email", "Each user must have unique email", 
                   "No duplicate emails allowed", priority=1)
    .with_edge_case("Password enumeration attack", "high", 4, 
                   "Implement rate limiting and consistent response times")
    .with_assumption("Users will remember passwords most of the time")
    .with_entity("User")
        .with_states(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
        .with_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
        .and_model()
    .build())
```

### 2. Socratic Questioning (While Prompting - 2 minutes)
The `socratic_prompting.py` module generates structured questions to:
- **Challenge Assumptions**: "What if users don't want to remember passwords?"
- **Explore Alternatives**: "What are 3 completely different authentication approaches?"
- **Discover Edge Cases**: "What happens when OAuth provider goes down?"
- **Validate Constraints**: "Is the 200ms response requirement actually negotiable?"

```python
from socratic_prompting import SocraticSession

session = SocraticSession("Design user authentication system")
session.add_assumption("Passwords are secure enough")
session.add_constraint("Must support OAuth")

questions = session.generate_questions()
# Generates targeted questions for AI dialogue
```

### 3. Assumption Tracking (Throughout Process)
The `assumption_tracking.py` module helps:
- **Track Assumptions**: Systematically record what we believe
- **Gather Evidence**: Collect supporting/contradicting evidence
- **Validation Tasks**: Create concrete steps to test assumptions
- **Status Management**: Track validation progress over time

```python
from assumption_tracking import AssumptionRegistry, Evidence, ValidationMethod

registry = AssumptionRegistry("Auth System")
assumption = registry.create_assumption(
    "user_patience", 
    "Users will wait 3 seconds for login",
    "Performance planning discussion",
    "Increased bounce rate if wrong"
)

assumption.add_evidence(Evidence(
    "Google study shows 53% abandon after 3s",
    "Think with Google research",
    supports=True,
    confidence=4
))
```

### 4. Design Exploration (After Prompting - 1 minute) 
The `design_exploration.py` module enables:
- **Alternative Comparison**: Score designs across multiple dimensions
- **Pattern Application**: Apply proven design patterns to problems
- **Hybrid Generation**: Combine strengths of different approaches
- **Improvement Suggestions**: Identify areas for enhancement

```python
from design_exploration import DesignExplorer, DesignDimension

explorer = DesignExplorer("User authentication system")
explorer.set_evaluation_criteria({
    DesignDimension.SECURITY: 0.4,
    DesignDimension.USER_EXPERIENCE: 0.3,
    DesignDimension.MAINTAINABILITY: 0.3
})

alt1 = explorer.create_alternative("oauth", "OAuth Integration", 
                                 "Use Google/GitHub OAuth", "Redirect to provider")
alt1.add_score(DesignDimension.SECURITY, 4, 4, "Proven OAuth security")
alt1.add_score(DesignDimension.USER_EXPERIENCE, 4, 3, "Convenient, no new passwords")

rankings = explorer.rank_alternatives()
```

## The Complete Vibe Designing Process

The demo (`vibe_designing_demo.py`) walks through the full 6-minute workflow:

**Before Prompting (3 minutes):**
1. Model domain invariants and business rules
2. Identify potential edge cases and failure modes
3. Sketch entity lifecycles and state transitions

**While Prompting (2 minutes):**
1. Generate Socratic questions to challenge assumptions
2. Use AI dialogue to explore alternative approaches
3. Discover new edge cases and validate constraints

**After Prompting (1 minute):**
1. Compare discovered alternatives systematically
2. Track new assumptions and insights
3. Create validation tasks for critical assumptions

## Design Philosophy

This approach transforms AI from a "code vending machine" into a "Socratic partner":

- **Vibe Coding**: Ask AI to generate code quickly
- **Vibe Designing**: Ask AI to help you think more clearly about problems

### Key Insights

> *"Good prompting is a result of deep understanding, not a substitute for it."*

- The bottleneck isn't typing speed—it's problem comprehension
- Better problem modeling leads to better prompts and solutions
- AI's value is in exploration and questioning, not just code generation
- Systematic design thinking prevents costly assumptions and oversights

### Competitive Advantage

> *"The teams that win won't just be the fastest—they'll be the clearest."*

- **Clarity over speed**: Understanding problems deeply before solving them
- **Design intentionality**: Making conscious choices about trade-offs
- **Assumption validation**: Testing beliefs before building on them
- **Alternative exploration**: Considering multiple approaches systematically

## Use Cases

This framework is valuable for:
- **System architecture decisions**: Comparing architectural patterns
- **Feature design**: Understanding user needs and edge cases
- **Technical debt management**: Validating assumptions about current systems
- **Team alignment**: Shared understanding of constraints and trade-offs
- **AI collaboration**: Structured approaches to AI-assisted design

## Integration with AI Tools

These tools are designed to enhance AI collaboration:
1. Use domain models to provide better context in prompts
2. Apply Socratic questions in AI conversations
3. Track assumptions surfaced during AI dialogue
4. Compare alternatives discovered through AI exploration

The result: More thoughtful, intentional, and robust software design.

## Connect

Part of [The AI Alchemical Mirror](https://antoninorau.substack.com/) - exploring the intersection of code and philosophy.

---

*"In an age of infinite code generation, the scarce resource isn't implementation speed—it's the wisdom to know what should be implemented at all."*