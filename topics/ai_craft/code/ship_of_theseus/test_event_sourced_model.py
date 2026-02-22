import pytest
from datetime import datetime, timedelta
from uuid import UUID
from .event_sourced_model import (
    ShipAggregate,
    ShipLaunched,
    PlankReplaced,
    Plank,
)


class TestEventSourcingModel:
    def test_ship_launch(self):
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = ShipAggregate.launch("Test Ship", hull)

        assert ship.name == "Test Ship"
        assert len(ship.hull) == 2
        assert len(ship._changes) == 1
        assert isinstance(ship._changes[0], ShipLaunched)

    def test_plank_replacement(self):
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = ShipAggregate.launch("Test Ship", hull)

        new_plank = Plank("teak", 300, 30)
        ship.replace_plank(0, new_plank)

        assert ship.hull[0] == new_plank
        assert len(ship._changes) == 2
        assert isinstance(ship._changes[1], PlankReplaced)

    def test_event_reconstruction(self):
        """Test that ship can be reconstructed from events."""
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        original_ship = ShipAggregate.launch("Theseus", hull)
        original_ship.replace_plank(0, Plank("teak", 300, 30))
        original_ship.replace_plank(1, Plank("mahogany", 300, 30))

        # Reconstruct from events
        reconstructed = ShipAggregate.from_events(original_ship._changes)

        assert reconstructed.ship_id == original_ship.ship_id
        assert reconstructed.name == original_ship.name
        assert reconstructed.hull == original_ship.hull

    def test_identity_is_narrative(self):
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
        assert ship_a._changes != ship_b._changes  # But different stories


class TestShipLaunchedEvent:
    def test_event_creation(self):
        ship_id = UUID("12345678-1234-5678-1234-567812345678")
        hull = [Plank("oak", 300, 30)]
        event = ShipLaunched(ship_id, "Test Ship", hull)

        assert event.ship_id == ship_id
        assert event.name == "Test Ship"
        assert event.initial_hull == hull
        assert isinstance(event.occurred_at, datetime)

    def test_event_immutability(self):
        ship_id = UUID("12345678-1234-5678-1234-567812345678")
        hull = [Plank("oak", 300, 30)]
        event = ShipLaunched(ship_id, "Test Ship", hull)

        with pytest.raises(AttributeError):
            event.ship_id = UUID("87654321-4321-8765-4321-876543218765")


class TestPlankReplacedEvent:
    def test_event_creation(self):
        ship_id = UUID("12345678-1234-5678-1234-567812345678")
        new_plank = Plank("teak", 300, 30)
        event = PlankReplaced(ship_id, 0, new_plank)

        assert event.ship_id == ship_id
        assert event.plank_index == 0
        assert event.new_plank == new_plank
        assert isinstance(event.occurred_at, datetime)


class TestEventOrdering:
    def test_events_maintain_order(self):
        """Test that events are processed in chronological order."""
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = ShipAggregate.launch("Test Ship", hull)

        # Add some delay between events to ensure different timestamps
        import time

        time.sleep(0.001)
        ship.replace_plank(0, Plank("teak", 300, 30))
        time.sleep(0.001)
        ship.replace_plank(1, Plank("mahogany", 300, 30))

        # Verify events are in chronological order
        events = ship._changes
        assert len(events) == 3
        for i in range(1, len(events)):
            assert events[i - 1].occurred_at <= events[i].occurred_at

    def test_empty_event_stream_reconstruction(self):
        """Test reconstruction from empty event stream."""
        ship = ShipAggregate.from_events([])

        assert ship.ship_id == UUID("00000000-0000-0000-0000-000000000000")
        assert ship.name == ""
        assert ship.hull == []
