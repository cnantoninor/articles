# Coding Conventions

**Analysis Date:** 2026-03-14

## Languages & Scope

This repository contains two distinct language ecosystems:

**Python (Primary):** Domain modeling and design frameworks in `topics/ai_craft/code/`
**JavaScript/JSX (Secondary):** Interactive infographics in `topics/epistemic_debt/artifacts/infographics/article-2/`

## Naming Patterns

### Python Files
- **Modules:** snake_case with descriptive names
  - Examples: `basic_entity_model.py`, `event_sourced_model.py`, `assumption_tracking.py`, `socratic_prompting.py`
  - Test files: `test_*.py` prefix (e.g., `test_domain_modeling.py`)
- **Classes:** PascalCase
  - Examples: `DomainInvariant`, `EntityLifecycle`, `ShipAggregate`, `AssumptionStatus`, `ValidationMethod`
  - Value Objects (frozen dataclasses) named directly: `Plank`, `Evidence`, `SocraticQuestion`
  - Builder classes: `DomainModelBuilder`
- **Functions & Methods:** snake_case
  - Examples: `add_invariant()`, `can_transition()`, `risk_score()`, `from_events()`, `_apply()`
  - Private methods: Prefix with underscore (`_apply()`, `_changes`)
- **Constants:** UPPERCASE_WITH_UNDERSCORES for module-level constants
  - Examples: `ASSUMPTION_TEMPLATES`, `ALTERNATIVE_TEMPLATES`, `EDGE_CASE_TEMPLATES`
  - Class attributes (Enum members): lowercase with underscores
    - Examples: `CREATED = "created"`, `ACTIVE = "active"`
- **Variables:** snake_case
  - Type hints always included in function signatures: `name: str`, `likelihood: int`
  - Field defaults in dataclasses clearly specified: `priority: int = 1`

### JavaScript Files
- **Files:** camelCase or PascalCase
  - Components: PascalCase (e.g., `Infographics.js`, `layout.js`)
  - Configuration: lowercase (e.g., `next.config.js`)
- **Functions:** camelCase
  - Examples: `useAnimatedValue()`, `WideningGap()` (component), `useCallback()` hooks
- **Constants:** camelCase (module-level design tokens in objects)
  - Object: `const T = { bg: "...", accent: "..." }` — short keys with semantic meaning
- **React Components:** PascalCase function names
  - Examples: `WideningGap()`, `Infographics`

## Code Style

### Formatting

**Python:**
- No explicit formatter configured (no `.black` or `.pylint` files present)
- Convention: Follow PEP 8 implicitly
  - 4-space indentation (observed in all files)
  - Maximum line length: implicit ~100 characters (observed in docstrings and code)
  - Docstrings: Module-level docstrings on all files with content
- No trailing commas enforced (dataclass definitions vary)

**JavaScript:**
- No explicit `.prettierrc` or `.eslintrc` configured
- Convention: Observed style is modern ES6+
  - Arrow functions preferred
  - Const-first for variable declarations
  - Semicolons present but not enforced

### Linting & Type Checking

**Python:**
- No linter configuration present (no `.flake8`, `pylint.rc`, `pyproject.toml` with tool sections)
- Type hints are used throughout (PEP 484 annotations)
  - All function parameters type-hinted
  - Return types sometimes omitted (especially for void methods)
  - Union types used: `Event = Union[ShipLaunched, PlankReplaced]`

**JavaScript:**
- No linting configuration present
- JSDoc comments minimal (only observed in `next.config.js`)

## Docstrings & Comments

### Python Docstring Pattern
- Module-level docstrings: Always present, triple-quoted, usually 1-2 lines
  - Example: `"""Tests for domain modeling framework"""`
  - TAM reference docstrings: Longer, multi-line
    - Example: `"""Domain Modeling Framework for Vibe Designing\n\nThis module implements the core concepts..."""`

- Class docstrings: Present for major classes, one-line summary
  - Example: `"""A business rule or constraint that must always hold true"""`

- Method docstrings: Present for complex methods, especially public APIs
  - Example from `ShipAggregate.from_events()`:
    ```python
    """Reconstitute the ship's state by replaying its entire history."""
    ```

- Inline comments: Sparse but clear when present
  - Used for non-obvious logic: `# Convert UUID to string for JSON serialization`
  - Section markers: `# --- Define Immutable Events ---`

### Python Comment Conventions
- Comments explain WHY, not WHAT
  - Bad (not found): `# Set ship_id to uuid4()`
  - Good (observed): `# Convert string back to UUID` (explains purpose)
- Comments on complex domain concepts are more detailed
  - Example: `"""A Value Object: defined by its attributes, interchangeable."""` (class docstring)

### JavaScript Comments
- Minimal use observed
- Section headers use commented delimiters:
  ```javascript
  // ─── Shared Design Tokens ───
  // ═══════════════════════════════════════════
  // 1. THE WIDENING GAP
  // ═══════════════════════════════════════════
  ```

## Import Organization

### Python Import Order
1. Standard library imports (dataclasses, typing, uuid, enum, json, datetime)
2. Third-party imports (none observed in test code; pytest imported by tests)
3. Local/relative imports (from module, try-except for flexibility)

Examples observed:
```python
# test_basic_entity_model.py
import pytest
from uuid import uuid4
from .basic_entity_model import Ship, Plank

# event_serialization.py
from dataclasses import asdict
import json
from datetime import datetime
from typing import Dict, Any

try:
    from .event_sourced_model import Event, ShipLaunched, PlankReplaced, Plank, ShipAggregate
except ImportError:
    from event_sourced_model import Event, ShipLaunched, PlankReplaced, Plank, ShipAggregate
```

### Python Path Aliases
- No aliases observed (no `pyproject.toml` path configuration)
- Relative imports preferred for same-package code: `from .module import Class`
- Fallback imports (try-except) for dual import compatibility:
  ```python
  try:
      from .event_sourced_model import ...
  except ImportError:
      from event_sourced_model import ...
  ```

### JavaScript Import Order
```javascript
// React/framework imports first
import { useState, useEffect, useRef, useCallback } from "react";

// Component imports
import Infographics from './Infographics';

// Default exports for Next.js pages
export default function Home() { ... }
```

## Error Handling

### Python Patterns

**Validation in `__post_init__` (dataclass patterns):**
```python
def __post_init__(self):
    if not self.name:
        raise ValueError("Invariant name cannot be empty")
    if not self.description:
        raise ValueError("Invariant description cannot be empty")
```

- Used in: `DomainInvariant`, `EntityLifecycle`, `Evidence`, `Assumption`, `SocraticQuestion`, `DesignAlternative`
- Raises: `ValueError` with descriptive messages

**Range validation:**
```python
if self.confidence not in range(1, 6):
    raise ValueError("Confidence must be 1-5")
```

**Explicit type checking:**
```python
if not isinstance(invariant, DomainInvariant):
    raise TypeError
```

**Custom error types:**
```python
raise IndexError("Plank not found at this position in the hull.")
```

**Try-except for import compatibility:**
```python
try:
    from .event_sourced_model import Event, ShipLaunched, PlankReplaced
except ImportError:
    from event_sourced_model import Event, ShipLaunched, PlankReplaced
```

**Graceful degradation with defaults:**
```python
impact_levels = {"critical": 5, "high": 4, "medium": 3, "low": 2, "minimal": 1}
severity = impact_levels.get(self.impact.lower(), 3)  # defaults to "medium"=3
```

### JavaScript Patterns
- Minimal error handling observed in provided JS samples
- Uses optional chaining and property access guards:
  ```javascript
  const canvas = canvasRef.current;
  if (!canvas) return;
  ```

## Function Design

### Python Function Size & Responsibility
- **Aggregate methods:** Single responsibility, often 5-15 lines
  - Examples: `replace_plank()`, `add_invariant()`, `can_transition()`
- **Factory methods:** Explicit creation patterns
  - `@classmethod` for named constructors: `ShipAggregate.launch()`, `ShipAggregate.from_events()`
  - Example: `create_authentication_model()` factory function

### Python Parameter Patterns
- **Positional parameters:** Always explicitly typed
  ```python
  def replace_plank(self, index_to_replace: int, new_plank: Plank) -> None:
  ```
- **Optional parameters with defaults:** Named, sensible defaults
  ```python
  priority: int = 1
  validation_function: Optional[Callable] = None
  mitigation: Optional[str] = None
  ```
- **Enum parameters:** Type-hinted with enum class
  ```python
  def add_transition(self, from_state: EntityLifecycleState, to_state: EntityLifecycleState):
  ```

### Python Return Patterns
- **Void/None methods:** Often omitted return type in observed code, but `-> None` is used in some methods
- **Chainable builders:** Return `self` for fluent interface
  ```python
  def with_assumption(self, assumption: str) -> "DomainModelBuilder":
      # ... implementation
      return self
  ```
- **Type unions:** Explicitly declared
  ```python
  Event = Union[ShipLaunched, PlankReplaced]
  ```

## Module Design

### Python Module Structure
- **Dataclass-heavy:** All domain models use `@dataclass` decorator
  - Frozen dataclasses for Value Objects: `@dataclass(frozen=True)`
  - Mutable for Entities: `@dataclass` (no frozen)
  - Field factories for collections: `field(default_factory=list)`, `field(default_factory=set)`

- **Enum definitions:** Explicit Enum classes for controlled vocabularies
  - Examples: `EntityLifecycleState`, `AssumptionStatus`, `ValidationMethod`, `QuestionType`
  - Values: lowercase strings matching names (`CREATED = "created"`)

- **Builder pattern:** Fluent API with method chaining
  - Example: `DomainModelBuilder` class with `.with_invariant()`, `.with_edge_case()`, `.build()`
  - Sub-builders: `.with_entity()` returns entity builder, `.and_model()` returns to parent builder

- **Service/utility functions:** Module-level functions for operations
  - Serialization: `serialize_event()`, `deserialize_event()`, `save_events()`, `load_ship_from_file()`
  - Factories: `create_authentication_model()`

### Barrel Files / Re-exports
- Not observed (no `__init__.py` files with explicit exports)

### Initialization Pattern
- Files with runnable examples use:
  ```python
  if __name__ == "__main__":
      # Example usage
  ```

## JavaScript/React Patterns

### Component Structure
- **Functional components:** Arrow functions with hooks
  ```javascript
  export default function Home() {
    return <Infographics />;
  }
  ```

- **Hooks:** Standard React hooks used
  - `useState` for state
  - `useEffect` for side effects
  - `useRef` for DOM references
  - `useCallback` for memoized callbacks

- **Design token pattern:** Centralized object for theme/styling
  ```javascript
  const T = {
    bg: "#0c0e13",
    surface: "#14171e",
    accent: "#f97316",
    font: "'JetBrains Mono', ...",
  };
  ```

- **Next.js metadata:** Exported as constants in layout files
  ```javascript
  export const metadata = { title: '...', description: '...' };
  ```

## Special Patterns

### Dataclass Field Management
- **Private fields:** Underscore prefix with `repr=False` to hide from output
  ```python
  _changes: List[Event] = field(default_factory=list, repr=False)
  ```

### Event Sourcing Pattern Conventions
- Events: Frozen dataclasses with timestamps
- Aggregates: Mutable dataclasses with event tracking
- Replay: `from_events()` classmethod rebuilds state
- Apply: `_apply()` private method mutates state

### Domain-Driven Design Conventions
- Value Objects vs. Entities clearly separated
- Domain invariants explicitly modeled as classes
- Business events reified as dataclasses
- Builder pattern for complex object construction

---

*Convention analysis: 2026-03-14*
