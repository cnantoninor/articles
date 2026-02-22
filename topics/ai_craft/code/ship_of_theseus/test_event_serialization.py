import pytest
import json
import tempfile
import os
from datetime import datetime
from uuid import UUID
from .event_serialization import serialize_event, deserialize_event, save_events, load_ship_from_file
from .event_sourced_model import ShipAggregate, ShipLaunched, PlankReplaced, Plank

class TestEventSerialization:
    def test_serialize_ship_launched_event(self):
        ship_id = UUID('12345678-1234-5678-1234-567812345678')
        hull = [Plank("oak", 300, 30), Plank("teak", 250, 25)]
        event = ShipLaunched(ship_id, "Test Ship", hull)
        
        serialized = serialize_event(event)
        
        assert serialized["event_type"] == "ShipLaunched"
        assert serialized["ship_id"] == str(ship_id)
        assert serialized["name"] == "Test Ship"
        assert len(serialized["initial_hull"]) == 2
        assert isinstance(serialized["occurred_at"], str)

    def test_serialize_plank_replaced_event(self):
        ship_id = UUID('12345678-1234-5678-1234-567812345678')
        new_plank = Plank("mahogany", 280, 32)
        event = PlankReplaced(ship_id, 1, new_plank)
        
        serialized = serialize_event(event)
        
        assert serialized["event_type"] == "PlankReplaced"
        assert serialized["ship_id"] == str(ship_id)
        assert serialized["plank_index"] == 1
        assert serialized["new_plank"]["material"] == "mahogany"
        assert isinstance(serialized["occurred_at"], str)

    def test_deserialize_ship_launched_event(self):
        ship_id = UUID('12345678-1234-5678-1234-567812345678')
        occurred_at = datetime.now()
        data = {
            "event_type": "ShipLaunched",
            "ship_id": str(ship_id),
            "name": "Test Ship",
            "initial_hull": [
                {"material": "oak", "length_cm": 300, "width_cm": 30},
                {"material": "teak", "length_cm": 250, "width_cm": 25}
            ],
            "occurred_at": occurred_at.isoformat()
        }
        
        event = deserialize_event(data)
        
        assert isinstance(event, ShipLaunched)
        assert event.ship_id == ship_id
        assert event.name == "Test Ship"
        assert len(event.initial_hull) == 2
        assert event.initial_hull[0] == Plank("oak", 300, 30)
        assert event.occurred_at == occurred_at

    def test_deserialize_plank_replaced_event(self):
        ship_id = UUID('12345678-1234-5678-1234-567812345678')
        occurred_at = datetime.now()
        data = {
            "event_type": "PlankReplaced",
            "ship_id": str(ship_id),
            "plank_index": 1,
            "new_plank": {"material": "mahogany", "length_cm": 280, "width_cm": 32},
            "occurred_at": occurred_at.isoformat()
        }
        
        event = deserialize_event(data)
        
        assert isinstance(event, PlankReplaced)
        assert event.ship_id == ship_id
        assert event.plank_index == 1
        assert event.new_plank == Plank("mahogany", 280, 32)
        assert event.occurred_at == occurred_at

    def test_unknown_event_type_raises_error(self):
        data = {
            "event_type": "UnknownEvent",
            "occurred_at": datetime.now().isoformat()
        }
        
        with pytest.raises(ValueError, match="Unknown event type: UnknownEvent"):
            deserialize_event(data)

    def test_roundtrip_serialization(self):
        """Test that events can be serialized and deserialized without loss."""
        ship_id = UUID('12345678-1234-5678-1234-567812345678')
        
        # Test ShipLaunched
        launch_event = ShipLaunched(ship_id, "Test Ship", [Plank("oak", 300, 30)])
        serialized = serialize_event(launch_event)
        deserialized = deserialize_event(serialized)
        
        assert deserialized == launch_event
        
        # Test PlankReplaced
        replace_event = PlankReplaced(ship_id, 0, Plank("teak", 300, 30))
        serialized = serialize_event(replace_event)
        deserialized = deserialize_event(serialized)
        
        assert deserialized == replace_event

class TestFilePersistence:
    def test_save_and_load_ship(self):
        """Test saving ship events to file and loading them back."""
        # Create a ship with some history
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = ShipAggregate.launch("Theseus", hull)
        ship.replace_plank(0, Plank("teak", 300, 30))
        ship.replace_plank(1, Plank("mahogany", 300, 30))
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            filename = f.name
        
        try:
            save_events(ship, filename)
            
            # Load back from file
            loaded_ship = load_ship_from_file(filename)
            
            # Verify the loaded ship matches the original
            assert loaded_ship.ship_id == ship.ship_id
            assert loaded_ship.name == ship.name
            assert loaded_ship.hull == ship.hull
        
        finally:
            # Clean up
            if os.path.exists(filename):
                os.unlink(filename)

    def test_save_events_creates_valid_json(self):
        """Test that saved events are valid JSON."""
        hull = [Plank("oak", 300, 30)]
        ship = ShipAggregate.launch("Test Ship", hull)
        ship.replace_plank(0, Plank("teak", 300, 30))
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            filename = f.name
        
        try:
            save_events(ship, filename)
            
            # Verify file contains valid JSON
            with open(filename, 'r') as f:
                data = json.load(f)
            
            assert isinstance(data, list)
            assert len(data) == 2  # ShipLaunched + PlankReplaced
            assert all("event_type" in event for event in data)
        
        finally:
            if os.path.exists(filename):
                os.unlink(filename)

    def test_empty_ship_serialization(self):
        """Test serializing a ship with no changes."""
        ship = ShipAggregate.from_events([])
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            filename = f.name
        
        try:
            save_events(ship, filename)
            
            with open(filename, 'r') as f:
                data = json.load(f)
            
            assert data == []  # No events
        
        finally:
            if os.path.exists(filename):
                os.unlink(filename)