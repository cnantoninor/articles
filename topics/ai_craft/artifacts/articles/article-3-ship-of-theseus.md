---
title: The Ship of Theseus & The Soul of Software
subtitle: Identity, Lifecycle, Memory, and Context in Software Engineering
status: published
type: article
audience:
- technical professionals
- software architects
- developers practicing DDD
target_length: 0
current_length: 2700
estimated_reading_time: 11 min
created: 2026-02-22
last_updated: 2026-02-22
published_date: 2025-08-24
publication_url: https://antoninorau.substack.com/p/the-ship-of-theseus-and-the-soul
social_teasers:
  linkedin: 'Every time you update a user''s email address in your database, you''re
    participating in a 2,500-year-old philosophical debate.

    The Ship of Theseus paradox asks: if every plank is replaced, is it still the
    same ship?

    In software, this translates to: Is a User entity defined by its current attributes,
    or by its entire history of changes?

    Domain-Driven Design offers sophisticated answers—from simple Entities to Event
    Sourcing, where identity becomes a narrative of immutable facts.

    The choice isn''t just technical. It''s about what stories our systems can tell.

    '
  twitter: ''
  instagram_caption: ''
  substack_notes: 'Starting the morning with an ancient question that''s surprisingly
    modern:

    If you replace every component of a system, is it still the same system?

    This isn''t just philosophy—it''s the core challenge of software migration, refactoring,
    and system evolution.

    Domain-Driven Design offers a sophisticated framework for thinking about identity,
    memory, and change in our digital systems.'
---



# The Ship of Theseus & The Soul of Software

*Identity, Memory, and Context in Domain-Driven Design*

## What an ancient paradox reveals about identity, memory, and context in Domain-Driven Design—and the stories our architectures tell.

---

## TL;DR

• The ancient Ship of Theseus paradox—is an object the same if all its parts are replaced?—provides a powerful metaphor for modeling identity in software.

• Domain-Driven Design (DDD) offers a ladder of concepts for this, moving from simple Entities vs. Value Objects (the ship vs. its planks) to more nuanced models like Event Sourcing, which treats identity as a continuous narrative of change.

• Ultimately, a model's "truth" is not absolute; it is defined by its Bounded Context, reminding us that identity in software is a pragmatic choice, not a metaphysical one.

---

## The Ancient Paradox: A Question Across Millennia

Every time you update a user's email address in your database, you're participating in a 2,500-year-old philosophical debate.

The question comes to us from antiquity, carried across millennia by Plutarch. The citizens of Athens, in reverent preservation, maintained the ship that had carried their hero Theseus home from Crete. As the wooden planks began to rot, they were meticulously replaced, one by one, with new, strong timber. Over the years, a moment arrived when not a single original plank remained.

And so the question was posed: was it still the same ship?

Some argued its form and history granted it continuous identity. Others, followers of a stricter logic, countered that a complete change of components made it an entirely new object. This paradox, a vessel for contemplating identity, has sailed through the minds of Hobbes, Locke, and modern philosophers.

But what does this ancient thought experiment whisper to us now, as we build systems not of wood and sail, but of logic and light?

It turns out, it asks the most fundamental question of software design.

---

## The Ship and Its Planks: Entities & Value Objects

In the vocabulary of Domain-Driven Design (DDD), we begin with a crucial distinction that Plutarch would have recognized:

• **An Entity** is an object defined not by its attributes, but by its thread of continuity and identity over time.

• **A Value Object** is an object defined by its attributes; any change to its value creates an entirely new object. It has no conceptual identity.

Evans defines this core pattern in Chapter 5 of *Domain-Driven Design*: Entities have conceptual identity that persists through changes, while Value Objects are defined only by their attributes. For a deeper dive, see Martin Fowler's analysis of [ValueObject patterns](https://martinfowler.com/bliki/ValueObject.html).

The paradox maps cleanly onto this first rung of our cognitive ladder:

• **The Ship of Theseus** is the quintessential Entity. It persists through change, decay, and repair. Its identity is a story.

• **The planks of wood** are Value Objects. One oaken plank of a certain dimension is interchangeable with another. They are defined by their characteristics (material, length), not their history.

We can model this distinction with a simple sketch. This represents one rung on what we called the cognitive ladder for understanding software systems. To climb from pistis ("Pattern Matching" - AI level) to noesis (real reasoning and understanding of the business domain as software engineers superior to AI).

### Code Sketch: An Entity Holding Value Objects

Here, the Ship is an Entity with a unique identifier (ship_id). The Plank is a Value Object—immutable (frozen=True) and defined purely by its attributes. We can swap its parts, but the ship's identity persists.

```python
from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4

# A Value Object: defined by its attributes, interchangeable.
@dataclass(frozen=True)
class Plank:
    material: str
    length_cm: int
    width_cm: int

# An Entity: defined by a persistent, unique identifier.
@dataclass
class Ship:
    ship_id: UUID
    name: str
    hull: List[Plank]
    
    def replace_plank(self, index_to_replace: int, new_plank: Plank) -> None:
        """The Ship's identity remains; its parts (Value Objects) are mutable."""
        if 0 <= index_to_replace < len(self.hull):
            self.hull[index_to_replace] = new_plank
        else:
            raise IndexError("Plank not found at this position in the hull.")

# --- Usage ---
ship_id = uuid4()
theseus_ship = Ship(
    ship_id=ship_id,
    name="Theseus's Ship",
    hull=[Plank("oak", 300, 30), Plank("oak", 300, 30)]
)

# We replace a plank. The ship's ID remains the same.
theseus_ship.replace_plank(0, Plank("teak", 300, 30))
print(f"Ship ID: {theseus_ship.ship_id}")  # The ID is constant.
print(f"Hull configuration: {theseus_ship.hull}")
```

A simple model distinguishing the persistent identity of the ship from its replaceable parts. This first step is clarifying. But it only captures a single snapshot in time. It answers *what* the ship is, but not *how* it continues to be.

How do we model the process of becoming?

---

## The Ship as Narrative: Identity Through Event Sourcing

A more profound answer comes from a pattern known as Event Sourcing. Instead of storing only the current state of an entity, we store the full sequence of events that shaped it. The current state is merely a projection, a temporary summary of its history.

This pattern, extensively documented in Fowler's [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) article, treats the event stream as the single source of truth—what Evans calls the 'append-only' approach to domain modeling.

This reframes the paradox entirely. Remember, a model is always a metaphor—and here we're choosing to model identity as narrative rather than substance.

**The Ship of Theseus is the Ship of Theseus not because of its current planks, but because we possess an unbroken memory of every replacement.** The identity is not in the material, but in the story.

An event-sourced model doesn't store the ship's final configuration. It stores the immutable facts: `ShipLaunched`, `PlankReplaced`, `MastRepaired`. The ship is the sum of its lived history.

### Code Sketch: Rebuilding Identity from Events

Here, the ShipAggregate is reconstructed by replaying its history. Two ships could end up with identical hulls, but if their histories—the sequence and timing of plank replacements—differ, their identities are fundamentally distinct.

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable, List, Union

# --- Define Immutable Events ---
@dataclass(frozen=True)
class ShipLaunched:
    ship_id: UUID
    name: str
    initial_hull: List[Plank]
    occurred_at: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class PlankReplaced:
    ship_id: UUID
    plank_index: int
    new_plank: Plank
    occurred_at: datetime = field(default_factory=datetime.utcnow)

Event = Union[ShipLaunched, PlankReplaced]

# --- Define the Aggregate ---
@dataclass
class ShipAggregate:
    ship_id: UUID
    name: str
    hull: List[Plank]
    _changes: List[Event] = field(default_factory=list, repr=False)
    
    @classmethod
    def launch(cls, name: str, hull: List[Plank]) -> "ShipAggregate":
        """Create a new ship by recording a launch event."""
        ship_id = uuid4()
        event = ShipLaunched(ship_id, name, hull)
        ship = cls(ship_id=ship_id, name=name, hull=list(hull))
        ship._changes.append(event)
        return ship
    
    def replace_plank(self, index: int, new_plank: Plank) -> None:
        """Record the intent to replace a plank as an event."""
        event = PlankReplaced(self.ship_id, index, new_plank)
        self._apply(event)
        self._changes.append(event)
    
    @classmethod
    def from_events(cls, events: Iterable[Event]) -> "ShipAggregate":
        """Reconstitute the ship's state by replaying its entire history."""
        ship = cls(ship_id=UUID('00000000-0000-0000-0000-000000000000'), name="", hull=[])
        for e in events:
            ship._apply(e)
        return ship
    
    def _apply(self, event: Event) -> None:
        """Apply an event to mutate the internal state."""
        if isinstance(event, ShipLaunched):
            self.ship_id = event.ship_id
            self.name = event.name
            self.hull = list(event.initial_hull)
        elif isinstance(event, PlankReplaced):
            self.hull[event.plank_index] = event.new_plank
```

In DDD terms, our Ship is an Aggregate Root—the single entry point for maintaining consistency within its boundary. See Evans' Chapter 6 on Aggregates for the theoretical foundation.

Identity here is not a state, but a story reconstructed from immutable historical facts. This is a higher level of understanding, one that mirrors a more mature view of identity itself. We are not who we are at this instant, but the integrated sum of our past choices and transformations. We have moved from a static belief (*pistis*) to a form of reasoned, historical knowledge (*dianoia*).

### Event Sourcing: The Performance Trade-off

**The Reality Check**: Event Sourcing's perfect memory comes with computational costs. Rebuilding a Ship's current state by replaying 10,000 `PlankReplaced` events becomes prohibitively slow. The standard solution is **snapshotting**—periodically saving the aggregate's state and only replaying events since the last snapshot. Think of it as creating save points in a video game.

Additionally, event streams grow indefinitely, requiring archival strategies and careful consideration of storage costs. A user with 100,000 profile updates over five years creates significant storage overhead compared to a simple state table. Query complexity also increases: finding "all ships with teak planks" requires either maintaining projection tables or scanning entire event streams.

As Fowler notes in his Event Sourcing analysis, this pattern shines for audit-heavy domains (finance, healthcare) but may be overkill for simple CRUD operations. The trade-off is clear: perfect historical fidelity versus computational efficiency.

### When to Choose Each Pattern

**Choose simple Entity models when:**
- Current state is all that matters
- Performance and simplicity are priorities  
- Audit trails aren't critical

**Choose Event Sourcing when:**
- You need perfect audit logs
- "How did we get here?" questions are common
- Legal/regulatory compliance requires event history
- You're building analytical systems that benefit from temporal queries

---

## The Final Arbiter: Bounded Context

But DDD offers one final, crucial lesson. The "identity" of the ship is not a universal, philosophical truth. It is a pragmatic choice determined by the questions we are asking. This is the wisdom of the **Bounded Context**.

This is perhaps Evans' most crucial insight from Chapter 14: the same concept can have completely different meanings across contexts. Fowler's [BoundedContext](https://martinfowler.com/bliki/BoundedContext.html) article provides practical guidance on identifying these boundaries.

A Bounded Context is a specific responsibility boundary within a larger software system, where a particular domain model applies. The meaning of "ship" can change dramatically across these boundaries:

• **In the Maintenance Context**, the Ship is an Entity. Its unique history of repairs, voyages, and material fatigue is paramount. It has a life story. `ship_id` is everything.

• **In the Fleet Logistics Context**, that same ship might become a Value Object. What matters are its specifications: cargo capacity, speed, crew size. It is interchangeable with any other ship that has the same specs for a given route. Its unique history is irrelevant.

• **In an Insurance Context**, the same ship becomes a Risk Assessment with age, condition, accident history. The identity question becomes: "Is this the same risk after major repairs?"

This is the ultimate resolution of the paradox from a designer's perspective: **it depends on the context**. The way we model the ship encodes the values and priorities of the problem we are trying to solve.

Is identity a historical narrative or a set of functional attributes? The software architect's answer must be: **For whom? For what purpose?**

---

## Design Note: Trade-Offs Encoded in Metaphors

Choosing how to model identity is not a neutral act. Each pattern encodes a set of trade-offs:

• **State-based Models (simple Entity)**: This is the simplest approach. It's easy to implement and query. But it treats history as a destructive process; old states are forgotten. It embodies a "presentist" view of the world. Its cost is memory loss.

• **Event Sourcing**: This model offers a perfect audit log and preserves history completely. It allows us to ask questions about the past and debug systems by replaying events. Its cost is complexity. Rebuilding state from a long event stream can be slow, requiring snapshots and other optimizations. It is a commitment to the past.

The choice between them is a choice of what matters more: the simplicity of the present, or the fidelity of the past.

---

## Conclusion: The Coder as Custodian of Stories

The Ship of Theseus is more than an academic puzzle; it is a mirror reflecting the choices we make when we give a piece of software a memory, a history, an identity.

It teaches us that identity is not merely the sum of its parts. It is the narrative continuity that we, the narrators, impose upon it. It emerges from the memory of events we choose to preserve and the context through which we interpret them.

As software developers, we are not just assembling components. We are custodians of identity. We build systems that must remember who a user is, what an order was, and how a transaction unfolded, preserving coherence through the inevitable flux of time and change.

The true design challenge, then, is not defending static things from a changing world. It is navigating the tension between stability and transformation, between the parts that are replaceable and the stories that are not.

The next time you're debating whether to store state or events, ask: **What story does your domain need to tell?**

---

## Call to Action

What are your thoughts? I'm genuinely curious.

• When has a simple state-based model failed you, forcing you to think more about an entity's history?
• Do you see Event Sourcing as a powerful tool for storytelling or an over-engineered complexity?
• What other philosophical puzzles do you see reflected in the daily practice of software design?

Leave a comment below and let's explore this together.

---



---

*If you found this article valuable, I'd love to hear your thoughts. Please [leave a comment](https://antoninorau.substack.com/comments), [share it](https://antoninorau.substack.com), and eventually [subscribe](https://antoninorau.substack.com/subscribe) to The AI Mirror for more explorations at the intersection of AI, software engineering and a bit of philosophy.*

---
## References

- Plutarch. *Vita Thesei* (Life of Theseus), in *Vitae Parallelae*.
- Hobbes, Thomas. *De Corpore*. 1655.
- Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003.
- Fowler, Martin. "Event Sourcing." martinfowler.com, 2005.
- Fowler, Martin. "ValueObject." martinfowler.com, 2016.
- Fowler, Martin. "BoundedContext." martinfowler.com, 2014.
- Vernon, Vaughn. *Implementing Domain-Driven Design*. Addison-Wesley, 2013.

---

## Technical Appendix: Complete Implementation

### Event Serialization and Storage

For production systems, events need persistence. Here's how to serialize and deserialize our ship events:

```python
from dataclasses import asdict
import json

def serialize_event(event: Event) -> dict:
    """Convert event to JSON-serializable dictionary."""
    data = asdict(event)
    data["event_type"] = event.__class__.__name__
    data["occurred_at"] = data["occurred_at"].isoformat()
    return data

def deserialize_event(data: dict) -> Event:
    """Reconstruct event from stored dictionary."""
    event_type = data.pop("event_type")
    data["occurred_at"] = datetime.fromisoformat(data["occurred_at"])
    
    if event_type == "ShipLaunched":
        data["initial_hull"] = [Plank(**p) for p in data["initial_hull"]]
        return ShipLaunched(**data)
    elif event_type == "PlankReplaced":
        data["new_plank"] = Plank(**data["new_plank"])
        return PlankReplaced(**data)
    
    raise ValueError(f"Unknown event type: {event_type}")

# Example usage with file storage
def save_events(ship: ShipAggregate, filename: str) -> None:
    events_data = [serialize_event(e) for e in ship._changes]
    with open(filename, 'w') as f:
        json.dump(events_data, f, indent=2)

def load_ship_from_file(filename: str) -> ShipAggregate:
    with open(filename, 'r') as f:
        events_data = json.load(f)
    events = [deserialize_event(data) for data in events_data]
    return ShipAggregate.from_events(events)
```

### Identity Through History: Advanced Test Cases

```python
def test_identity_is_narrative():
    """Demonstrates that identity depends on history, not just final state."""
    initial_hull = [Plank("oak", 200, 30), Plank("oak", 200, 30)]
    
    # Ship A: Replace planks in sequence
    ship_a = ShipAggregate.launch("Theseus A", initial_hull)
    ship_a.replace_plank(0, Plank("teak", 200, 30))
    ship_a.replace_plank(1, Plank("mahogany", 200, 30))
    
    # Ship B: Replace same planks, different order
    ship_b = ShipAggregate.launch("Theseus B", initial_hull) 
    ship_b.replace_plank(1, Plank("mahogany", 200, 30))
    ship_b.replace_plank(0, Plank("teak", 200, 30))
    
    # Rebuild from events to verify persistence
    reconstructed_a = ShipAggregate.from_events(ship_a._changes)
    reconstructed_b = ShipAggregate.from_events(ship_b._changes)
    
    # Same final state, different identities
    assert reconstructed_a.hull == reconstructed_b.hull  # Same materials
    assert len(ship_a._changes) == len(ship_b._changes)  # Same number of events
    assert ship_a._changes != ship_b._changes           # But different stories
    
    print(f"Ship A events: {[type(e).__name__ for e in ship_a._changes]}")
    print(f"Ship B events: {[type(e).__name__ for e in ship_b._changes]}")
    # Both print: ['ShipLaunched', 'PlankReplaced', 'PlankReplaced']
    # But the PlankReplaced events have different indices and timestamps

def test_bounded_context_modeling():
    """Shows how the same ship appears differently across contexts."""
    # Create a ship with rich history
    ship = ShipAggregate.launch("HMS Victory", [
        Plank("oak", 300, 40),
        Plank("oak", 300, 40)
    ])
    ship.replace_plank(0, Plank("teak", 300, 40))  # Expensive upgrade
    
    # In Maintenance Context: Ship is an Entity with full history
    class MaintenanceShip:
        def __init__(self, aggregate: ShipAggregate):
            self.ship_id = aggregate.ship_id
            self.name = aggregate.name
            self.hull = aggregate.hull
            self.repair_history = [
                e for e in aggregate._changes 
                if isinstance(e, PlankReplaced)
            ]
            
        def needs_inspection(self) -> bool:
            return len(self.repair_history) > 0
    
    # In Fleet Planning Context: Ship becomes a Value Object
    @dataclass(frozen=True)
    class FleetShipSpec:
        cargo_capacity: int
        crew_size: int
        
        @classmethod
        def from_aggregate(cls, ship: ShipAggregate) -> "FleetShipSpec":
            # History irrelevant; only current capabilities matter
            hull_strength = len([p for p in ship.hull if p.material == "teak"])
            return cls(
                cargo_capacity=hull_strength * 100,
                crew_size=20
            )
    
    maintenance_view = MaintenanceShip(ship)
    fleet_view = FleetShipSpec.from_aggregate(ship)
    
    assert maintenance_view.needs_inspection()  # History matters
    assert fleet_view.cargo_capacity == 100     # Only specs matter
```

**Key Insight**: The same ship aggregate serves both contexts, but each extracts different aspects of identity—historical narrative versus functional specification.
