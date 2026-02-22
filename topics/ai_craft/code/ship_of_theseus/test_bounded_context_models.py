import pytest
from .event_sourced_model import ShipAggregate, Plank
from .bounded_context_models import MaintenanceShip, FleetShipSpec

class TestMaintenanceShip:
    def test_maintenance_ship_creation(self):
        """Test creating a maintenance view of a ship."""
        hull = [Plank("oak", 300, 40), Plank("oak", 300, 40)]
        ship_aggregate = ShipAggregate.launch("HMS Victory", hull)
        
        maintenance_ship = MaintenanceShip(ship_aggregate)
        
        assert maintenance_ship.ship_id == ship_aggregate.ship_id
        assert maintenance_ship.name == ship_aggregate.name
        assert maintenance_ship.hull == ship_aggregate.hull
        assert len(maintenance_ship.repair_history) == 0

    def test_maintenance_ship_with_repairs(self):
        """Test maintenance ship tracking repair history."""
        hull = [Plank("oak", 300, 40), Plank("oak", 300, 40)]
        ship_aggregate = ShipAggregate.launch("HMS Victory", hull)
        ship_aggregate.replace_plank(0, Plank("teak", 300, 40))  # Expensive upgrade
        ship_aggregate.replace_plank(1, Plank("mahogany", 300, 40))  # Another repair
        
        maintenance_ship = MaintenanceShip(ship_aggregate)
        
        assert len(maintenance_ship.repair_history) == 2
        assert maintenance_ship.needs_inspection() == True

    def test_maintenance_ship_no_repairs_no_inspection(self):
        """Test that ships with no repairs don't need inspection."""
        hull = [Plank("oak", 300, 40), Plank("oak", 300, 40)]
        ship_aggregate = ShipAggregate.launch("New Ship", hull)
        
        maintenance_ship = MaintenanceShip(ship_aggregate)
        
        assert maintenance_ship.needs_inspection() == False

class TestFleetShipSpec:
    def test_fleet_ship_spec_creation(self):
        """Test creating a fleet specification from ship aggregate."""
        hull = [Plank("oak", 300, 40), Plank("teak", 300, 40)]
        ship_aggregate = ShipAggregate.launch("Fleet Ship", hull)
        
        fleet_spec = FleetShipSpec.from_aggregate(ship_aggregate)
        
        # One teak plank = 100 cargo capacity
        assert fleet_spec.cargo_capacity == 100
        assert fleet_spec.crew_size == 20

    def test_fleet_ship_spec_with_multiple_teak_planks(self):
        """Test fleet spec calculation with multiple teak planks."""
        hull = [Plank("teak", 300, 40), Plank("teak", 300, 40), Plank("oak", 300, 40)]
        ship_aggregate = ShipAggregate.launch("Strong Ship", hull)
        
        fleet_spec = FleetShipSpec.from_aggregate(ship_aggregate)
        
        # Two teak planks = 200 cargo capacity
        assert fleet_spec.cargo_capacity == 200
        assert fleet_spec.crew_size == 20

    def test_fleet_ship_spec_no_teak_planks(self):
        """Test fleet spec with no teak planks."""
        hull = [Plank("oak", 300, 40), Plank("mahogany", 300, 40)]
        ship_aggregate = ShipAggregate.launch("Basic Ship", hull)
        
        fleet_spec = FleetShipSpec.from_aggregate(ship_aggregate)
        
        # No teak planks = 0 cargo capacity
        assert fleet_spec.cargo_capacity == 0
        assert fleet_spec.crew_size == 20

    def test_fleet_ship_spec_immutability(self):
        """Test that FleetShipSpec is immutable."""
        hull = [Plank("teak", 300, 40)]
        ship_aggregate = ShipAggregate.launch("Test Ship", hull)
        fleet_spec = FleetShipSpec.from_aggregate(ship_aggregate)
        
        with pytest.raises(AttributeError):
            fleet_spec.cargo_capacity = 500

class TestBoundedContextDemonstration:
    def test_bounded_context_modeling(self):
        """Shows how the same ship appears differently across contexts."""
        # Create a ship with rich history
        ship = ShipAggregate.launch("HMS Victory", [
            Plank("oak", 300, 40),
            Plank("oak", 300, 40)
        ])
        ship.replace_plank(0, Plank("teak", 300, 40))  # Expensive upgrade
        
        maintenance_view = MaintenanceShip(ship)
        fleet_view = FleetShipSpec.from_aggregate(ship)
        
        # In maintenance context, history matters
        assert maintenance_view.needs_inspection() == True
        assert len(maintenance_view.repair_history) == 1
        
        # In fleet context, only current specs matter
        assert fleet_view.cargo_capacity == 100     # Only current capability
        assert fleet_view.crew_size == 20
        
        # Same ship, different perspectives
        assert maintenance_view.ship_id == ship.ship_id
        # Fleet view doesn't even track ship identity - it's just specs

    def test_context_independence(self):
        """Test that different contexts can coexist independently."""
        # Two ships with same final state but different histories
        hull = [Plank("oak", 300, 40), Plank("oak", 300, 40)]
        
        ship_a = ShipAggregate.launch("Ship A", hull)
        ship_a.replace_plank(0, Plank("teak", 300, 40))
        ship_a.replace_plank(1, Plank("teak", 300, 40))
        
        ship_b = ShipAggregate.launch("Ship B", hull)
        ship_b.replace_plank(1, Plank("teak", 300, 40))
        ship_b.replace_plank(0, Plank("teak", 300, 40))
        
        # Maintenance context: Different histories matter
        maintenance_a = MaintenanceShip(ship_a)
        maintenance_b = MaintenanceShip(ship_b)
        
        assert maintenance_a.ship_id != maintenance_b.ship_id
        assert len(maintenance_a.repair_history) == len(maintenance_b.repair_history)
        # But the repair events happened in different order (though we can't directly test that here)
        
        # Fleet context: Same capabilities, history irrelevant
        fleet_a = FleetShipSpec.from_aggregate(ship_a)
        fleet_b = FleetShipSpec.from_aggregate(ship_b)
        
        assert fleet_a == fleet_b  # Same specifications
        assert fleet_a.cargo_capacity == fleet_b.cargo_capacity == 200

    def test_context_boundary_demonstration(self):
        """Demonstrate clear boundaries between contexts."""
        hull = [Plank("oak", 300, 40)]
        ship = ShipAggregate.launch("Test Ship", hull)
        ship.replace_plank(0, Plank("teak", 300, 40))
        
        # Maintenance context cares about repair history
        maintenance = MaintenanceShip(ship)
        repair_count = len(maintenance.repair_history)
        
        # Fleet context only cares about current capabilities  
        fleet = FleetShipSpec.from_aggregate(ship)
        capacity = fleet.cargo_capacity
        
        # Add more repairs
        ship.replace_plank(0, Plank("mahogany", 300, 40))
        
        # Create new views
        new_maintenance = MaintenanceShip(ship)
        new_fleet = FleetShipSpec.from_aggregate(ship)
        
        # Maintenance view sees the change in history
        assert len(new_maintenance.repair_history) == repair_count + 1
        
        # Fleet view sees the change in capability (mahogany != teak for capacity)
        assert new_fleet.cargo_capacity != capacity