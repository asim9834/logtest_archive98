# tests/test_inventory.py

import pytest
import os
import tempfile
import json
from game_engine.inventory import Inventory

@pytest.fixture
def temp_inventory_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tf:
        test_data = {
            "test_player": [
                {"id": "sword_001", "name": "Bronze Sword", "type": "weapon", "value": 10},
                {"id": "potion_001", "name": "Health Potion", "type": "consumable", "value": 5}
            ]
        }
        json.dump(test_data, tf, ensure_ascii=False)
        tf_path = tf.name
    yield tf_path
    os.remove(tf_path)

@pytest.fixture
def sample_inventory(temp_inventory_file):
    return Inventory(player_id="test_player", storage_path=temp_inventory_file)

def test_add_item(sample_inventory):
    assert len(sample_inventory.get_items()) == 2
    sample_inventory.add_item({"id": "shield_001", "name": "Wooden Shield", "type": "armor", "value": 8})
    assert len(sample_inventory.get_items()) == 3

def test_remove_item(sample_inventory):
    removed = sample_inventory.remove_item("Bronze Sword")
    assert removed is True
    assert not any(item["name"] == "Bronze Sword" for item in sample_inventory.get_items())

def test_remove_nonexistent_item(sample_inventory):
    removed = sample_inventory.remove_item("nonexistent")
    assert removed is False
    assert len(sample_inventory.get_items()) == 2

def test_to_dict(sample_inventory):
    data = sample_inventory.to_dict()
    assert data["player_id"] == "test_player"
    assert isinstance(data["items"], list)

def test_from_dict():
    data = {
        "player_id": "restore_test",
        "items": [{"id": "ring_001", "name": "Silver Ring", "type": "accessory", "value": 15}]
    }
    inv = Inventory.from_dict(data)
    assert inv.player_id == "restore_test"
    assert len(inv.get_items()) == 1
