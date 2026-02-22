from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable, Union, List
from uuid import UUID, uuid4

# Reuse the Plank Value Object
@dataclass(frozen=True)
class Plank:
    material: str
    length_cm: int
    width_cm: int

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