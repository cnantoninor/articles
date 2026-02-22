from dataclasses import dataclass
from typing import List

try:
    from .event_sourced_model import ShipAggregate, PlankReplaced
except ImportError:
    from event_sourced_model import ShipAggregate, PlankReplaced

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