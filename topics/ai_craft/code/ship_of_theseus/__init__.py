"""
Ship of Theseus Domain-Driven Design Example
===========================================

This package contains the code examples from the Ship of Theseus DDD article,
demonstrating different approaches to modeling identity in software systems.

Modules:
- basic_entity_model: Simple Entity/Value Object pattern
- event_sourced_model: Event Sourcing implementation
- event_serialization: Event persistence utilities
- bounded_context_models: Different context representations
"""

from .basic_entity_model import Ship, Plank
from .event_sourced_model import ShipAggregate, ShipLaunched, PlankReplaced, Event
from .bounded_context_models import MaintenanceShip, FleetShipSpec

__all__ = [
    'Ship', 'Plank',
    'ShipAggregate', 'ShipLaunched', 'PlankReplaced', 'Event',
    'MaintenanceShip', 'FleetShipSpec'
]