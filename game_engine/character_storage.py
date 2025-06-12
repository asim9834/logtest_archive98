import json
import os

CHARACTER_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "custom_characters.json")

class CharacterManager:
    def __init__(self, filename="data/custom_characters.json"):
        self.filename = filename

    def load_characters(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_character(self, character_data):
        characters = self.load_characters()
        characters.append(character_data)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(characters, f, ensure_ascii=False, indent=4)

    def delete_character_by_name(self, name):
        characters = self.load_characters()
        characters = [char for char in characters if char["name"] != name]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(characters, f, ensure_ascii=False, indent=4)

    def get_character(self, name):
        characters = self.load_characters()
        for char in characters:
            if char["name"] == name:
                return char
        return None

def save_characters_to_file(characters):
    os.makedirs(os.path.dirname(CHARACTER_FILE_PATH), exist_ok=True)
    with open(CHARACTER_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(characters, file, ensure_ascii=False, indent=4)

def load_custom_characters():
    if not os.path.exists(CHARACTER_FILE_PATH):
        return []
    with open(CHARACTER_FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def delete_character_by_name(name, filename="data/custom_characters.json"):
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

def update_character_by_name(name, new_data, filename="data/custom_characters.json"):
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
    
def add_character(character_data, filename="data/custom_characters.json"):
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