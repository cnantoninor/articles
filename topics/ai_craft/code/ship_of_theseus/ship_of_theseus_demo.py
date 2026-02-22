#!/usr/bin/env python3
"""
Ship of Theseus Demonstration
============================

This script demonstrates the concepts from the Ship of Theseus DDD article:
1. Basic Entity/Value Object pattern
2. Event Sourcing approach
3. Different bounded contexts
4. Event serialization and persistence
"""

from uuid import uuid4
import tempfile
import os

# Handle both direct execution and module import
import sys
from pathlib import Path

# Add the current directory to Python path for direct execution
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))

try:
    from .basic_entity_model import Ship, Plank
    from .event_sourced_model import ShipAggregate
    from .bounded_context_models import MaintenanceShip, FleetShipSpec
    from .event_serialization import save_events, load_ship_from_file
except ImportError:
    # Fallback for direct execution
    from basic_entity_model import Ship, Plank
    from event_sourced_model import ShipAggregate
    from bounded_context_models import MaintenanceShip, FleetShipSpec
    from event_serialization import save_events, load_ship_from_file

def demonstrate_basic_entity_model():
    """Demonstrate the basic Entity/Value Object pattern."""
    print("=== Basic Entity/Value Object Pattern ===")
    
    # Create a ship with planks
    ship_id = uuid4()
    hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
    ship = Ship(ship_id, "Theseus's Ship", hull)
    
    print(f"Original ship: {ship.name}")
    print(f"Ship ID: {ship.ship_id}")
    print(f"Original hull: {[f'{p.material}' for p in ship.hull]}")
    
    # Replace all planks (Ship of Theseus paradox)
    ship.replace_plank(0, Plank("teak", 300, 30))
    ship.replace_plank(1, Plank("mahogany", 300, 30))
    
    print(f"After replacing all planks:")
    print(f"Ship ID: {ship.ship_id} (same)")
    print(f"New hull: {[f'{p.material}' for p in ship.hull]}")
    print("Question: Is it still the same ship?\n")

def demonstrate_event_sourcing():
    """Demonstrate event sourcing approach."""
    print("=== Event Sourcing Pattern ===")
    
    # Create ship with event sourcing
    hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
    ship = ShipAggregate.launch("Theseus's Ship", hull)
    
    print(f"Ship launched: {ship.name}")
    print(f"Initial events: {len(ship._changes)}")
    
    # Replace planks and track events
    ship.replace_plank(0, Plank("teak", 300, 30))
    ship.replace_plank(1, Plank("mahogany", 300, 30))
    
    print(f"After modifications: {len(ship._changes)} events")
    print(f"Event types: {[type(e).__name__ for e in ship._changes]}")
    
    # Demonstrate reconstruction from events
    reconstructed = ShipAggregate.from_events(ship._changes)
    print(f"Reconstructed ship matches: {reconstructed.hull == ship.hull}")
    print("Identity is narrative: the ship is its complete history\n")

def demonstrate_bounded_contexts():
    """Demonstrate different bounded contexts."""
    print("=== Bounded Context Pattern ===")
    
    # Create a ship with some repair history
    hull = [Plank("oak", 300, 40), Plank("oak", 300, 40)]
    ship = ShipAggregate.launch("HMS Victory", hull)
    ship.replace_plank(0, Plank("teak", 300, 40))  # Expensive upgrade
    
    # View in Maintenance Context
    maintenance_view = MaintenanceShip(ship)
    print(f"Maintenance Context:")
    print(f"  Ship needs inspection: {maintenance_view.needs_inspection()}")
    print(f"  Repair history: {len(maintenance_view.repair_history)} repairs")
    
    # View in Fleet Planning Context
    fleet_view = FleetShipSpec.from_aggregate(ship)
    print(f"Fleet Planning Context:")
    print(f"  Cargo capacity: {fleet_view.cargo_capacity}")
    print(f"  Crew size: {fleet_view.crew_size}")
    print(f"  (History irrelevant - only current specs matter)")
    
    print("Same ship, different meanings in different contexts\n")

def demonstrate_event_persistence():
    """Demonstrate event serialization and persistence."""
    print("=== Event Persistence ===")
    
    # Create ship with history
    hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
    original_ship = ShipAggregate.launch("Persistent Ship", hull)
    original_ship.replace_plank(0, Plank("teak", 300, 30))
    original_ship.replace_plank(1, Plank("mahogany", 300, 30))
    
    # Save to file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        filename = f.name
    
    try:
        save_events(original_ship, filename)
        print(f"Saved {len(original_ship._changes)} events to file")
        
        # Load from file
        loaded_ship = load_ship_from_file(filename)
        print(f"Loaded ship: {loaded_ship.name}")
        print(f"Hull matches: {loaded_ship.hull == original_ship.hull}")
        print(f"ID matches: {loaded_ship.ship_id == original_ship.ship_id}")
        print("Perfect persistence of identity through events\n")
        
    finally:
        if os.path.exists(filename):
            os.unlink(filename)

def demonstrate_identity_as_narrative():
    """Demonstrate that identity depends on narrative, not just state."""
    print("=== Identity as Narrative ===")
    
    initial_hull = [Plank("oak", 200, 30), Plank("oak", 200, 30)]
    
    # Ship A: Replace planks in sequence 0, then 1
    ship_a = ShipAggregate.launch("Ship A", initial_hull)
    ship_a.replace_plank(0, Plank("teak", 200, 30))
    ship_a.replace_plank(1, Plank("mahogany", 200, 30))
    
    # Ship B: Replace planks in sequence 1, then 0
    ship_b = ShipAggregate.launch("Ship B", initial_hull)
    ship_b.replace_plank(1, Plank("mahogany", 200, 30))
    ship_b.replace_plank(0, Plank("teak", 200, 30))
    
    print(f"Ship A final hull: {[p.material for p in ship_a.hull]}")
    print(f"Ship B final hull: {[p.material for p in ship_b.hull]}")
    print(f"Same final state: {ship_a.hull == ship_b.hull}")
    
    print(f"Ship A events: {len(ship_a._changes)}")
    print(f"Ship B events: {len(ship_b._changes)}")
    print(f"Same number of events: {len(ship_a._changes) == len(ship_b._changes)}")
    print(f"Different narratives: {ship_a._changes != ship_b._changes}")
    
    print("Conclusion: Identity is not about final state, but about the story")

def main():
    """Run all demonstrations."""
    print("Ship of Theseus: Identity, Memory, and Context in Domain-Driven Design")
    print("=" * 70)
    
    demonstrate_basic_entity_model()
    demonstrate_event_sourcing()
    demonstrate_bounded_contexts()
    demonstrate_event_persistence()
    demonstrate_identity_as_narrative()
    
    print("\nConclusion:")
    print("The choice of how to model identity encodes our values:")
    print("- Simple entities prioritize present simplicity")
    print("- Event sourcing prioritizes historical fidelity")
    print("- Bounded contexts recognize that meaning depends on purpose")
    print("\nWhat story does your domain need to tell?")

if __name__ == "__main__":
    main()