import pytest
from uuid import uuid4
from .basic_entity_model import Ship, Plank

class TestPlank:
    def test_plank_creation(self):
        plank = Plank("oak", 300, 30)
        assert plank.material == "oak"
        assert plank.length_cm == 300
        assert plank.width_cm == 30

    def test_plank_immutability(self):
        plank = Plank("oak", 300, 30)
        with pytest.raises(AttributeError):
            plank.material = "teak"

    def test_plank_equality(self):
        plank1 = Plank("oak", 300, 30)
        plank2 = Plank("oak", 300, 30)
        plank3 = Plank("teak", 300, 30)
        
        assert plank1 == plank2
        assert plank1 != plank3

class TestShip:
    def test_ship_creation(self):
        ship_id = uuid4()
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = Ship(ship_id, "Test Ship", hull)
        
        assert ship.ship_id == ship_id
        assert ship.name == "Test Ship"
        assert len(ship.hull) == 2

    def test_replace_plank_success(self):
        ship_id = uuid4()
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = Ship(ship_id, "Test Ship", hull)
        
        new_plank = Plank("teak", 300, 30)
        ship.replace_plank(0, new_plank)
        
        assert ship.hull[0] == new_plank
        assert ship.hull[1].material == "oak"

    def test_replace_plank_invalid_index(self):
        ship_id = uuid4()
        hull = [Plank("oak", 300, 30)]
        ship = Ship(ship_id, "Test Ship", hull)
        
        new_plank = Plank("teak", 300, 30)
        
        with pytest.raises(IndexError, match="Plank not found at this position in the hull"):
            ship.replace_plank(1, new_plank)

    def test_ship_identity_persistence(self):
        ship_id = uuid4()
        hull = [Plank("oak", 300, 30), Plank("oak", 300, 30)]
        ship = Ship(ship_id, "Test Ship", hull)
        
        original_id = ship.ship_id
        ship.replace_plank(0, Plank("teak", 300, 30))
        
        assert ship.ship_id == original_id

    def test_complete_plank_replacement(self):
        """Test the Ship of Theseus scenario: replace all planks."""
        ship_id = uuid4()
        hull = [Plank("oak", 200, 25), Plank("oak", 200, 25)]
        ship = Ship(ship_id, "Theseus Ship", hull)
        
        original_id = ship.ship_id
        
        # Replace all planks
        ship.replace_plank(0, Plank("teak", 200, 25))
        ship.replace_plank(1, Plank("mahogany", 200, 25))
        
        # Ship identity should remain the same
        assert ship.ship_id == original_id
        # But all materials should be different
        assert all(plank.material != "oak" for plank in ship.hull)