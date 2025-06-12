import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_engine.character_storage import CharacterManager

def test_save_and_load():
    manager = CharacterManager("tests/temp_characters.json")
    test_char = {"name": "Test", "race": "Elf", "class": "Hunter"}
    manager.save_character(test_char)
    chars = manager.load_characters()
    assert any(c["name"] == "Test" for c in chars)
