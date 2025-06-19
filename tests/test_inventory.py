# tests/test_inventory.py

import pytest
from game_engine.inventory import Inventory

@pytest.fixture
def sample_inventory():
    inv = Inventory(player_id="test_player")
    inv.add_item({"id": "sword_001", "name": "Iron Sword", "type": "weapon", "value": 10})
    inv.add_item({"id": "potion_001", "name": "Health Potion", "type": "consumable", "value": 5})
    return inv

def test_add_item(sample_inventory):
    assert len(sample_inventory.items) == 2
    assert sample_inventory.items[0]["name"] == "Iron Sword"
    assert sample_inventory.items[1]["name"] == "Health Potion"

def test_remove_item(sample_inventory):
    removed = sample_inventory.remove_item("sword_001")
    assert removed is True
    assert len(sample_inventory.items) == 1
    assert sample_inventory.items[0]["id"] == "potion_001"

def test_remove_nonexistent_item(sample_inventory):
    removed = sample_inventory.remove_item("nonexistent")
    assert removed is False
    assert len(sample_inventory.items) == 2

def test_to_dict(sample_inventory):
    data = sample_inventory.to_dict()
    assert data["player_id"] == "test_player"
    assert isinstance(data["items"], list)
    assert data["items"][0]["id"] == "sword_001"

def test_from_dict():
    data = {
        "player_id": "restore_test",
        "items": [{"id": "ring_001", "name": "Silver Ring", "type": "accessory", "value": 15}]
    }
    inv = Inventory.from_dict(data)
    assert inv.player_id == "restore_test"
    assert len(inv.items) == 1
    assert inv.items[0]["name"] == "Silver Ring"
