import os
import json
import tempfile
import pytest
from game_engine.inventory import Inventory


@pytest.fixture
def temp_inventory_file():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    yield tmp.name
    os.remove(tmp.name)


def test_add_and_list_items(temp_inventory_file):
    inv = Inventory("test_player", storage_path=temp_inventory_file)
    inv.add_item({"name": "Kılıç", "type": "weapon", "power": 10})
    items = inv.get_items()
    assert len(items) == 1
    assert items[0]["name"] == "Kılıç"


def test_has_item(temp_inventory_file):
    inv = Inventory("test_player", storage_path=temp_inventory_file)
    inv.add_item({"name": "Kalkan", "type": "armor", "defense": 5})
    assert inv.has_item("Kalkan") is True
    assert inv.has_item("Büyü Kitabı") is False


def test_remove_item(temp_inventory_file):
    inv = Inventory("test_player", storage_path=temp_inventory_file)
    inv.add_item({"name": "İksir", "type": "potion", "effect": "heal"})
    assert inv.has_item("İksir") is True
    inv.remove_item("İksir")
    assert inv.has_item("İksir") is False
