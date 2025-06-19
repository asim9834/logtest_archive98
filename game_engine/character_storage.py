import json
import os

DEFAULT_CHARACTER_FILE = "data/custom_characters.json"

class CharacterManager:
    def __init__(self, storage_path=None):
        self.storage_path = storage_path or DEFAULT_CHARACTER_FILE
        self._ensure_file()

    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.isfile(self.storage_path):
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)

    def load_characters(self):
        with open(self.storage_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_characters(self, characters):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(characters, f, indent=4, ensure_ascii=False)

    def add_character(self, character_data):
        characters = self.load_characters()
        characters.append(character_data)
        self.save_characters(characters)

    def get_character(self, name):
        characters = self.load_characters()
        return next((c for c in characters if c["name"] == name), None)

    def delete_character(self, name):
        characters = self.load_characters()
        characters = [c for c in characters if c["name"] != name]
        self.save_characters(characters)
