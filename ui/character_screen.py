from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QTextEdit, QComboBox, QLineEdit, QMessageBox,
    QScrollArea, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from game_engine.character_storage import CharacterManager
from game_engine.character_ai_generator import generate_character_with_ai
from game_engine.character_templates import CHARACTER_CLASSES, CHARACTER_RACES
from game_engine.character import Character
from game_engine.prebuilt_characters import prebuilt_characters
from ui.character_card import CharacterCard


class CharacterScreen(QWidget):
    def __init__(self, on_character_selected_callback, on_back_callback):
        super().__init__()
        self.on_character_selected_callback = on_character_selected_callback
        self.on_back_callback = on_back_callback
        self.character_manager = CharacterManager()
        self.custom_characters = self.character_manager.load_characters()

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        # === SOL PANEL ===
        left_panel = QVBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("NAME")
        left_panel.addWidget(self.name_input)

        self.race_combo = QComboBox()
        self.race_combo.addItems(CHARACTER_RACES)
        left_panel.addWidget(self.race_combo)

        self.class_combo = QComboBox()
        self.class_combo.addItems(CHARACTER_CLASSES)
        left_panel.addWidget(self.class_combo)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Backstory")
        left_panel.addWidget(self.description_input)

        self.create_button = QPushButton("create")
        self.create_button.clicked.connect(self.create_character)
        left_panel.addWidget(self.create_button)

        self.random_button = QPushButton("random")
        self.random_button.clicked.connect(self.generate_random_character)
        left_panel.addWidget(self.random_button)

        self.save_button = QPushButton("save")
        self.save_button.clicked.connect(self.save_character)
        left_panel.addWidget(self.save_button)

        self.back_button = QPushButton("back")
        self.back_button.clicked.connect(self.on_back_callback)
        left_panel.addWidget(self.back_button)

        self.start_button = QPushButton("start")
        self.start_button.clicked.connect(self.start_game_with_selected)
        left_panel.addWidget(self.start_button)

        main_layout.addLayout(left_panel, 1)

        # === ORTA PANEL ===
        center_panel = QVBoxLayout()
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("assets/default_portrait.png").scaled(200, 200, Qt.KeepAspectRatio))
        self.image_label.setAlignment(Qt.AlignCenter)
        center_panel.addWidget(self.image_label)

        self.character_card_container = QVBoxLayout()
        self.character_card_widget = CharacterCard({})
        self.character_card_container.addWidget(self.character_card_widget)
        center_panel.addLayout(self.character_card_container)

        main_layout.addLayout(center_panel, 2)

        # === SAĞ PANEL ===
        right_panel = QVBoxLayout()

        self.prebuilt_list = QListWidget()
        self.prebuilt_list.addItem("--- PREBUILT CHARACTERS ---")
        for c in prebuilt_characters:
            self.prebuilt_list.addItem(f"{c.name}")
        self.prebuilt_list.itemClicked.connect(self.display_prebuilt)

        self.custom_list = QListWidget()
        self.custom_list.addItem("--- CUSTOM CHARACTERS ---")
        for c in self.custom_characters:
            self.custom_list.addItem(f"{c['name']}")
        self.custom_list.itemClicked.connect(self.display_custom)

        right_panel.addWidget(self.prebuilt_list)
        right_panel.addWidget(self.custom_list)

        main_layout.addLayout(right_panel, 1)

    def create_character(self):
        name = self.name_input.text().strip()
        race = self.race_combo.currentText()
        class_ = self.class_combo.currentText()
        description = self.description_input.toPlainText().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Please enter a name.")
            return

        character = generate_character_with_ai(name, race, class_, description)
        self.temp_character = character
        self.display_character_card(character)

    def generate_random_character(self):
        import random
        if not self.name_input.text():
            self.name_input.setText(f"Hero{random.randint(100,999)}")
        if not self.description_input.toPlainText():
            self.description_input.setPlainText("A mysterious adventurer...")
        self.race_combo.setCurrentIndex(random.randint(0, len(CHARACTER_RACES)-1))
        self.class_combo.setCurrentIndex(random.randint(0, len(CHARACTER_CLASSES)-1))
        self.create_character()

    def save_character(self):
        if hasattr(self, "temp_character"):
            self.character_manager.add_character(self.temp_character)
            self.custom_list.addItem(self.temp_character["name"])
            QMessageBox.information(self, "Saved", "Character saved successfully.")
        else:
            QMessageBox.warning(self, "Warning", "No character to save.")

    def display_character_card(self, character_dict):
        # Var olan kartı temizle ve yeni kartı ekle
        for i in reversed(range(self.character_card_container.count())):
            widget = self.character_card_container.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.character_card_widget = CharacterCard(character_dict)
        self.character_card_container.addWidget(self.character_card_widget)

    def display_prebuilt(self, item):
        name = item.text()
        character = next((c for c in prebuilt_characters if c.name == name), None)
        if character:
            self.display_character_card(character.to_dict())

    def display_custom(self, item):
        name = item.text()
        character = self.character_manager.get_character(name)
        if character:
            self.display_character_card(character)

    def start_game_with_selected(self):
        # Öncelik sırası: hazır karakter → özel karakter
        selected_prebuilt = self.prebuilt_list.currentItem()
        selected_custom = self.custom_list.currentItem()
        character = None

        if selected_prebuilt and selected_prebuilt.text() != "--- PREBUILT CHARACTERS ---":
            name = selected_prebuilt.text()
            found = next((c for c in prebuilt_characters if c.name == name), None)
            if found:
                character = found.to_dict()

        elif selected_custom and selected_custom.text() != "--- CUSTOM CHARACTERS ---":
            name = selected_custom.text()
            found = self.character_manager.get_character(name)
            if found:
                character = found

        if character:
            self.on_character_selected_callback(character)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a character before starting.")

