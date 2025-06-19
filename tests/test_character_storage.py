# tests/test_character_storage.py

import os
import json
import shutil
import tempfile
import pytest

from game_engine.character_storage import CharacterManager

@pytest.fixture
def temp_data_dir():
    # Geçici test klasörü
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_add_and_get_character(temp_data_dir):
    cm = CharacterManager(storage_path=os.path.join(temp_data_dir, "test_chars.json"))
    
    character = {
        "name": "TestMan",
        "race": "Elf",
        "class": "Büyücü",
        "story": "Efsanevi bir savaşçı."
    }

    cm.add_character(character)
    retrieved = cm.get_character("TestMan")

    assert retrieved["name"] == "TestMan"
    assert retrieved["race"] == "Elf"
    assert retrieved["class"] == "Büyücü"
    assert "Efsanevi" in retrieved["story"]

def test_delete_character(temp_data_dir):
    cm = CharacterManager(storage_path=os.path.join(temp_data_dir, "delete_chars.json"))
    
    character = {"name": "Silinecek", "race": "İnsan", "class": "Savaşçı"}
    cm.add_character(character)
    assert cm.get_character("Silinecek") is not None

    cm.delete_character("Silinecek")
    assert cm.get_character("Silinecek") is None

def test_load_multiple_characters(temp_data_dir):
    path = os.path.join(temp_data_dir, "multi_chars.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump([
            {"name": "A", "race": "Cüce", "class": "Barbar"},
            {"name": "B", "race": "Elf", "class": "Büyücü"}
        ], f, ensure_ascii=False)

    cm = CharacterManager(storage_path=path)
    chars = cm.load_characters()
    names = [c["name"] for c in chars]

    assert "A" in names
    assert "B" in names
