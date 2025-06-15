import json
import os
from game_engine.character_ai_generator import generate_character_story

CHARACTER_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "custom_characters.json")

class CharacterManager:
    def __init__(self, filename=CHARACTER_FILE_PATH):
        self.filename = filename
        self.characters = self.load_characters()

    def load_characters(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_characters(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.characters, f, ensure_ascii=False, indent=4)

    def add_character(self, character):
        self.characters.append(character)
        self.save_characters()

    def delete_character(self, name):
        self.characters = [char for char in self.characters if char.get("name") != name]
        self.save_characters()

    def get_character(self, name):
        for char in self.characters:
            if char.get("name") == name:
                return char
        return None

    def update_character(self, name, updated_data):
        for idx, char in enumerate(self.characters):
            if char.get("name") == name:
                self.characters[idx].update(updated_data)
                self.save_characters()
                return True
        return False

    def get_all_custom_characters(self):
        return self.characters


# AI destekli karakter oluşturucu (character_screen ile uyumlu)
def generate_character_with_ai(name, race, char_class, description):
    story = generate_character_story(name, race, char_class, description)
    return {
        "name": name,
        "race": race,
        "class": char_class,
        "description": description,
        "story": story
    }
