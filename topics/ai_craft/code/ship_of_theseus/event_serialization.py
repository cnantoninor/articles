from dataclasses import asdict
import json
from datetime import datetime
from typing import Dict, Any

try:
    from .event_sourced_model import Event, ShipLaunched, PlankReplaced, Plank, ShipAggregate
except ImportError:
    from event_sourced_model import Event, ShipLaunched, PlankReplaced, Plank, ShipAggregate

def serialize_event(event: Event) -> Dict[str, Any]:
    """Convert event to JSON-serializable dictionary."""
    data = asdict(event)
    data["event_type"] = event.__class__.__name__
    data["occurred_at"] = data["occurred_at"].isoformat()
    # Convert UUID to string for JSON serialization
    if "ship_id" in data:
        data["ship_id"] = str(data["ship_id"])
    return data

def deserialize_event(data: Dict[str, Any]) -> Event:
    """Reconstruct event from stored dictionary."""
    from uuid import UUID
    
    event_type = data.pop("event_type")
    data["occurred_at"] = datetime.fromisoformat(data["occurred_at"])
    
    # Convert string back to UUID
    if "ship_id" in data:
        data["ship_id"] = UUID(data["ship_id"])
    
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