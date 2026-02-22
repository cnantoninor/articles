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

# --- Usage Example ---
if __name__ == "__main__":
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