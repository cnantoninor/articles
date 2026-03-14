# Testing Patterns

**Analysis Date:** 2026-03-14

## Test Framework

### Runner
- **Framework:** pytest
- **Version:** Implied from imports (python >= 3.13 required, see `pyproject.toml`)
- **Config:** `.planning/codebase/pytest.ini`

### Configuration
```ini
[pytest]
testpaths =
    topics/ai_craft/code/vibe_designing
    topics/ai_craft/code/ship_of_theseus
python_files = test_*.py
python_functions = test_*
python_classes = Test*
addopts = -v --tb=short
pythonpath =
    topics/ai_craft/code/vibe_designing
    topics/ai_craft/code/ship_of_theseus
```

Key settings:
- **Test discovery:** Files matching `test_*.py`, functions matching `test_*`, classes matching `Test*`
- **Verbosity:** `-v` flag (verbose output)
- **Traceback:** `--tb=short` (shorter error messages)
- **Python path:** Direct imports from vibe_designing and ship_of_theseus modules

### Assertion Library
- **Standard:** Python's built-in `assert` keyword with `pytest.raises()` for exception testing
- **No external library:** No additional assertion library observed

### Run Commands
```bash
# Run all tests in configured paths
pytest

# Run specific test file
pytest topics/ai_craft/code/vibe_designing/test_domain_modeling.py

# Run specific test class
pytest topics/ai_craft/code/vibe_designing/test_domain_modeling.py::TestDomainModel

# Run specific test function
pytest topics/ai_craft/code/vibe_designing/test_domain_modeling.py::TestDomainModel::test_add_invariant

# Watch mode (requires pytest-watch plugin, not observed in current setup)
# No watch mode configured

# Coverage (no coverage config observed)
# Not currently set up
```

## Test File Organization

### Location Pattern
- **Co-located:** Test files are in the same directory as source code
  - Source: `topics/ai_craft/code/ship_of_theseus/basic_entity_model.py`
  - Test: `topics/ai_craft/code/ship_of_theseus/test_basic_entity_model.py`

- **Paths tested:**
  ```
  topics/ai_craft/code/vibe_designing/
  ├── domain_modeling.py
  ├── test_domain_modeling.py
  ├── assumption_tracking.py
  ├── test_assumption_tracking.py
  ├── socratic_prompting.py
  ├── test_socratic_prompting.py
  ├── design_exploration.py
  ├── test_design_exploration.py
  └── [demo files]

  topics/ai_craft/code/ship_of_theseus/
  ├── basic_entity_model.py
  ├── test_basic_entity_model.py
  ├── event_sourced_model.py
  ├── test_event_sourced_model.py
  ├── event_serialization.py
  ├── test_event_serialization.py
  ├── bounded_context_models.py
  ├── test_bounded_context_models.py
  └── [demo files]
  ```

### Naming Convention
- **Pattern:** `test_<module_name>.py`
- All test files use this pattern consistently

## Test Structure

### Test Class Organization
```python
class TestEntityName:
    """Test class for entity/module"""

    def test_operation_or_scenario(self):
        # Arrange
        input_data = ...

        # Act
        result = operation(input_data)

        # Assert
        assert result == expected
```

### Observed Structure Pattern
- **Setup:** Arrange phase creates test data inline or with minimal fixtures
- **Execution:** Act phase calls methods under test
- **Verification:** Assert phase uses simple assertions

**Example from `test_basic_entity_model.py`:**
```python
class TestShip:
    def test_ship_creation(self):
        ship_id = uuid4()
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = Ship(ship_id, "Test Ship", hull)

        assert ship.ship_id == ship_id
        assert ship.name == "Test Ship"
        assert len(ship.hull) == 2
```

### Multi-Assertion Tests
- Multiple assertions in single test method (not separated into individual methods)
- Example from `test_domain_modeling.py`:
```python
def test_add_invariant(self):
    model = DomainModel("Test", "Test")
    invariant = DomainInvariant("test", "test desc", "test rule")

    model.add_invariant(invariant)
    assert len(model.invariants) == 1
    assert model.invariants[0] == invariant
```

### Docstring Usage
- Test methods sometimes have docstrings explaining scenario
- **Example from `test_event_sourced_model.py`:**
```python
def test_event_reconstruction(self):
    """Test that ship can be reconstructed from events."""
    hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
    original_ship = ShipAggregate.launch("Theseus", hull)
    # ... test logic
```

## Mocking

### Framework
- **No mocking observed:** No unittest.mock, pytest-mock, or similar imports in test files
- Tests use real objects (domain models, dataclasses, enums)

### Approach
- **Immutable test doubles:** Frozen dataclasses used as value objects
  - Example: `Plank("oak", 300, 30)` directly instantiated, reused across tests
- **Real aggregates:** Event sourcing tests use actual `ShipAggregate` with real events
- **No patching:** No observed use of `@patch`, `MagicMock`, or `Mock`

### What NOT to Mock (Observed Pattern)
- Domain entities (test with real objects)
- Value objects (immutable, safe to reuse)
- Event streams (test serialization/deserialization with real data)
- State transitions (test actual state machine behavior)

### Test Data
- Inline creation: Most tests create simple test data directly
  ```python
  ship_id = uuid4()
  hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
  ship = Ship(ship_id, "Test Ship", hull)
  ```

## Fixtures and Factories

### Factory Functions
- **Observed:** `create_authentication_model()` in `test_domain_modeling.py`
  - Returns fully-configured domain model with invariants, edge cases, entities, assumptions
  - Used as test precondition rather than as a fixture

- **Builder usage:** `DomainModelBuilder` used within tests to construct complex models
  ```python
  model = (DomainModelBuilder("Test", "Test")
          .with_assumption("Test assumption")
          .build())
  ```

### Test Fixtures
- **No pytest fixtures observed:** No `@pytest.fixture` decorators found
- **Inline setup:** All test data created in test methods
- **Reuse pattern:** Simple immutable objects reused (e.g., `Plank` instances)

### Example Precondition Setup
From `test_domain_modeling.py`:
```python
def test_builder_with_invariant(self):
    model = (DomainModelBuilder("Test", "Test")
            .with_invariant("test_inv", "test desc", "test rule", priority=2)
            .build())

    assert len(model.invariants) == 1
    assert model.invariants[0].name == "test_inv"
    assert model.invariants[0].priority == 2
```

## Coverage

### Coverage Requirements
- **Not enforced:** No pytest-cov configuration or coverage threshold observed
- **Not measured:** No `.coveragerc` or coverage settings in `pytest.ini`

### View Coverage
Not configured. To add coverage:
```bash
# Install pytest-cov
pip install pytest-cov

# Run with coverage
pytest --cov=topics/ai_craft/code/vibe_designing --cov=topics/ai_craft/code/ship_of_theseus --cov-report=term-missing

# Or configure in pytest.ini
# [pytest]
# addopts = --cov=... --cov-report=html
```

## Test Types

### Unit Tests (Primary)
- **Scope:** Individual classes and methods
- **Approach:** Dataclass instantiation, method calls, assertion of results
- **Examples:**
  - `test_plank_creation()` — tests `Plank` value object construction
  - `test_ship_replace_plank()` — tests single method behavior
  - `test_invariant_validation()` — tests validation logic in `__post_init__`

### Integration Tests (Secondary)
- **Scope:** Workflows spanning multiple classes or subsystems
- **Approach:** Build complex objects, test state transitions, verify side effects
- **Examples:**
  - `test_complete_plank_replacement()` — full ship lifecycle with multiple replacements
  - `test_event_reconstruction()` — event sourcing round-trip (save → load → verify)
  - `test_builder_with_entity()` — builder fluent API chaining

### Behavior Tests (Domain-Focused)
- **Scope:** Business logic and domain invariants
- **Approach:** Assert business rules hold true
- **Examples:**
  - `test_ship_identity_persistence()` — ship ID unchanged after plank replacement
  - `test_identity_is_narrative()` — same final state but different event histories
  - `test_risk_score_calculation()` — business formula for risk scoring

### E2E Tests
- **Not observed:** No end-to-end or system integration tests present
- **Not applicable:** This is a library/framework codebase, not an application

## Common Patterns

### Exception Testing
**Pattern using `pytest.raises()`:**
```python
def test_plank_immutability(self):
    plank = Plank("oak", 300, 30)
    with pytest.raises(AttributeError):
        plank.material = "teak"

def test_replace_plank_invalid_index(self):
    ship_id = uuid4()
    hull = [Plank("oak", 300, 30)]
    ship = Ship(ship_id, "Test Ship", hull)

    new_plank = Plank("teak", 300, 30)

    with pytest.raises(IndexError, match="Plank not found at this position in the hull"):
        ship.replace_plank(1, new_plank)
```

- `pytest.raises()` context manager for exception assertion
- Optional `match=` parameter for exception message regex matching
- Exceptions tested in methods with explicit error handling

### Error Message Validation
```python
def test_invariant_validation(self):
    with pytest.raises(ValueError, match="name cannot be empty"):
        DomainInvariant("", "desc", "rule")

    with pytest.raises(ValueError, match="description cannot be empty"):
        DomainInvariant("name", "", "rule")
```

- Regex matching on exception message
- Tests that validation errors have descriptive messages

### Type Checking Tests
```python
def test_add_invalid_invariant(self):
    model = DomainModel("Test", "Test")

    with pytest.raises(TypeError):
        model.add_invariant("not an invariant")
```

### Async Testing
- **Not observed:** No async/await patterns in tested code
- **Not applicable:** Synchronous domain models

### Time-Based Testing
- **Minimal:** One test uses `time.sleep()` for timestamp ordering
  ```python
  def test_events_maintain_order(self):
      """Test that events are processed in chronological order."""
      import time

      time.sleep(0.001)
      ship.replace_plank(0, Plank("teak", 300, 30))
      time.sleep(0.001)
      ship.replace_plank(1, Plank("mahogany", 300, 30))

      # Verify events are in chronological order
      events = ship._changes
      for i in range(1, len(events)):
          assert events[i - 1].occurred_at <= events[i].occurred_at
  ```

### State Machine Testing
```python
def test_add_transition(self):
    entity = EntityLifecycle("Order")
    entity.add_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)

    assert entity.can_transition(EntityLifecycleState.CREATED, EntityLifecycleState.ACTIVE)
    assert not entity.can_transition(EntityLifecycleState.ACTIVE, EntityLifecycleState.CREATED)
```

- Tests valid transitions exist
- Tests invalid transitions are rejected

### Enumeration Testing
```python
def test_create_entity(self):
    entity = EntityLifecycle("User")
    assert entity.entity_name == "User"
    assert EntityLifecycleState.CREATED in entity.states
    assert EntityLifecycleState.ACTIVE in entity.states
```

- Verifies enum values are in collections
- Tests default state sets

### Serialization Testing
From `test_event_serialization.py`:
- Serialization round-trip (object → dict → json → dict → object)
- UUID conversion (object UUID → string → object UUID)
- DateTime serialization (datetime → ISO string → datetime)

### Factory Testing
```python
def test_auth_model_has_critical_invariants(self):
    model = create_authentication_model()
    critical = model.get_critical_invariants()

    assert len(critical) >= 2
    invariant_names = [inv.name for inv in critical]
    assert "unique_email" in invariant_names
    assert "password_strength" in invariant_names
```

- Tests that factory creates correctly configured objects
- Verifies invariants, entities, assumptions are populated

## Test Data Patterns

### Immutable Value Objects
Reused across tests due to immutability:
```python
# Widely reused in ship_of_theseus tests
Plank("oak", 300, 30)
Plank("teak", 300, 30)
Plank("mahogany", 200, 25)
```

### Random IDs
Uses Python's `uuid4()` for unique identifiers:
```python
from uuid import uuid4
ship_id = uuid4()
```

### Hardcoded UUIDs
For deterministic testing:
```python
ship_id = UUID("12345678-1234-5678-1234-567812345678")
```

### Default Values in Tests
Builder pattern provides sensible defaults:
```python
model = DomainModel("Test System", "Test description")
# Automatically gets empty lists for invariants, edge_cases, entities, assumptions
```

## Testing Philosophy Observed

1. **Test behavior, not implementation:** Tests verify what objects do, not how
2. **Clear test names:** Method names clearly describe what is being tested
3. **Single responsibility:** Each test exercises one assertion focus
4. **Real objects:** No mocking; domain objects are simple enough to instantiate
5. **Explicit setup:** Test data created inline, not hidden in fixtures
6. **Domain-driven:** Tests verify business rules and invariants
7. **Deterministic:** No randomness; same test always produces same result

---

*Testing analysis: 2026-03-14*
