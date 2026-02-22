# Ship of Theseus - DDD Code Examples

This directory contains the Python code examples from the "Ship of Theseus & The Soul of Software" article, demonstrating different approaches to modeling identity in Domain-Driven Design.

## Files Structure

### Core Models
- **`basic_entity_model.py`** - Simple Entity/Value Object pattern
- **`event_sourced_model.py`** - Event Sourcing implementation
- **`event_serialization.py`** - Event persistence utilities
- **`bounded_context_models.py`** - Different context representations

### Tests
- **`test_basic_entity_model.py`** - Tests for basic Entity/Value Object pattern
- **`test_event_sourced_model.py`** - Tests for Event Sourcing implementation
- **`test_event_serialization.py`** - Tests for event serialization and persistence
- **`test_bounded_context_models.py`** - Tests for bounded context models

### Demo and Configuration
- **`ship_of_theseus_demo.py`** - Interactive demonstration of all concepts
- **`pytest.ini`** - Pytest configuration
- **`requirements.txt`** - Python dependencies
- **`__init__.py`** - Package initialization

## Running the Code

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Demo
```bash
python ship_of_theseus_demo.py
```

### Run Tests
```bash
pytest
```

## Key Concepts Demonstrated

### 1. Entity vs Value Object
The `Plank` class is a **Value Object** - immutable and defined by its attributes. The `Ship` class is an **Entity** - defined by its identity that persists through changes.

### 2. Event Sourcing
Instead of storing current state, we store the sequence of events that shaped the entity. The current state is reconstructed by replaying events.

### 3. Bounded Contexts
The same ship can be viewed differently:
- **Maintenance Context**: Ship as Entity with repair history
- **Fleet Planning Context**: Ship as Value Object with only current specifications

### 4. Identity as Narrative
Event Sourcing treats identity as a story - not the current state, but the complete history of changes.

## The Ship of Theseus Paradox

If all parts of a ship are gradually replaced, is it still the same ship? This ancient paradox maps perfectly onto software design choices:

- **Simple Entities**: Identity persists through change (pragmatic)
- **Event Sourcing**: Identity is the complete narrative (historical)
- **Bounded Contexts**: Identity depends on the context and purpose (contextual)

## Design Trade-offs

| Pattern | Pros | Cons | When to Use |
|---------|------|------|-------------|
| Simple Entity | Easy to implement, fast queries | No audit trail, history lost | Current state is sufficient |
| Event Sourcing | Perfect audit log, temporal queries | Complex, slower reconstruction | Compliance, analytics, debugging |
| Bounded Contexts | Clear domain boundaries | Multiple models to maintain | Complex domains with different needs |

Each pattern encodes different values about what matters most: simplicity, historical fidelity, or contextual clarity.