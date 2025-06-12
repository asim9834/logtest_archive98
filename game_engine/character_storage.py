
import json
import os
import random
from game_engine.character_templates import CHARACTER_CLASSES
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

# Eski standalone fonksiyonlar korunuyor:
def save_characters_to_file(characters):
    os.makedirs(os.path.dirname(CHARACTER_FILE_PATH), exist_ok=True)
    with open(CHARACTER_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(characters, file, ensure_ascii=False, indent=4)

def load_custom_characters():
    if not os.path.exists(CHARACTER_FILE_PATH):
        return []
    with open(CHARACTER_FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def delete_character_by_name(name, filename=CHARACTER_FILE_PATH):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            characters = json.load(f)
        characters = [char for char in characters if char.get("name") != name]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(characters, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Silme hatası: {e}")
        return False

def update_character_by_name(name, new_data, filename=CHARACTER_FILE_PATH):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            characters = json.load(f)
        updated = False
        for char in characters:
            if char.get("name") == name:
                char.update(new_data)
                updated = True
                break
        if updated:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(characters, f, ensure_ascii=False, indent=4)
        return updated
    except Exception as e:
        print(f"Güncelleme hatası: {e}")
        return False

def add_character(character_data, filename=CHARACTER_FILE_PATH):
    try:
        characters = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                characters = json.load(f)
        characters.append(character_data)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(characters, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Ekleme hatası: {e}")
        return False

# AI destekli karakter oluşturucu
def generate_character_with_ai(name, race, char_class, description):
    story = generate_character_story(name, race, char_class, description)
    return {
        "name": name,
        "race": race,
        "class": char_class,
        "description": description,
        "story": story
    }
