
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget,
    QTextEdit, QComboBox, QLineEdit, QMessageBox
)

from game_engine.character_templates import prebuilt_characters
from game_engine.character_storage import CharacterManager
from game_engine.character_ai_generator import generate_character_story
from game_engine.character_storage import load_custom_characters, save_characters_to_file
from game_engine.character_ai_generator import generate_character_with_ai

class CharacterScreen(QWidget):
    def __init__(self, on_character_selected_callback, on_back_callback):
        super().__init__()
        self.on_character_selected_callback = on_character_selected_callback
        self.on_back_callback = on_back_callback
        self.character_manager = CharacterManager()
        self.characters = load_custom_characters()
        self.characters.extend([c.__dict__ for c in prebuilt_characters])

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        self.character_list = QListWidget()
        self.character_list.itemClicked.connect(self.display_character_details)
        main_layout.addWidget(self.character_list, 1)

        self.character_details = QTextEdit()
        self.character_details.setReadOnly(True)
        main_layout.addWidget(self.character_details, 2)

        create_layout = QVBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Karakter adı")
        create_layout.addWidget(self.name_input)

        self.race_combo = QComboBox()
        self.race_combo.addItems(["İnsan", "Elf", "Cüce", "Ejderdoğan", "Ork", "Tiefling", "Goblin", "Tabaxi", "Goliath", "Halfling"])
        create_layout.addWidget(self.race_combo)

        self.class_combo = QComboBox()
        self.class_combo.addItems(["Barbar", "Haydut", "Büyücü", "Savaşçı", "Ozan", "Druid", "Paladin", "Korucu", "Keşiş", "Sihirbaz"])
        create_layout.addWidget(self.class_combo)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Karakterin geçmişine dair bir şeyler yaz.")
        create_layout.addWidget(self.description_input)

        self.create_button = QPushButton("Karakter Yarat")
        self.create_button.clicked.connect(self.create_character)
        create_layout.addWidget(self.create_button)

        self.back_button = QPushButton("Geri")
        self.back_button.clicked.connect(self.on_back_callback)
        create_layout.addWidget(self.back_button)

        self.start_button = QPushButton("Oyuna Başla")
        self.start_button.clicked.connect(self.start_game_with_selected)
        create_layout.addWidget(self.start_button)

        main_layout.addLayout(create_layout, 1)

        self.load_character_list()

    def load_character_list(self):
        self.character_list.clear()

        prebuilt = [c for c in self.characters if "background" in c]
        custom = [c for c in self.characters if "story" in c]

        if prebuilt:
            self.character_list.addItem("--- Hazır Karakterler ---")
            for char in prebuilt:
                info = f"{char['name']} adlı {char['race']} ırkından bir {char['class']}."
                self.character_list.addItem(info)

        if custom:
            self.character_list.addItem("--- Özel Karakterler ---")
            for char in custom:
                info = f"{char['name']} adlı {char['race']} ırkından bir {char['class']}."
                self.character_list.addItem(info)

    def display_character_details(self, item):
        name = item.text().split(" ")[0]
        character = next((c for c in self.characters if c.get("name") == name), None)
        if character:
            if character.get("story"):
                self.character_details.setText(character["story"])
            else:
                details = f"Ad: {character.get('name', '')}\nIrk: {character.get('race', '')}\nSınıf: {character.get('class', '')}\n"
                if "background" in character:
                    details += f"Geçmiş: {character.get('background')}\n"
                if "personality" in character:
                    etails += f"Kişilik: {character.get('personality')}\n"
                if "abilities" in character:
                    details += f"Yetenekler: {', '.join(character.get('abilities', []))}\n"
                if "alignment" in character:
                    details += f"Taraf: {character.get('alignment')}\n"
                self.character_details.setText(details)



    def create_character(self):
        name = self.name_input.text().strip()
        race = self.race_combo.currentText()
        char_class = self.class_combo.currentText()
        description = self.description_input.toPlainText().strip()

        if name and race and char_class:
            story = generate_character_story(name, race, char_class, description)
            self.character_manager.add_character({
                "name": name,
                "race": race,
                "class": char_class,
                "story": story
            })
            self.characters = self.character_manager.load_characters()
            self.load_character_list()
            self.character_details.setText(story)

    def start_game_with_selected(self):
        selected = self.character_list.currentItem()
        if selected:
            name = selected.text().split(" ")[0]
            character = self.character_manager.get_character(name)
            if character:
                self.on_character_selected_callback(character)
