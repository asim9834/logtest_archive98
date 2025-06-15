from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit
)
from game_engine.location_manager import LocationManager


class GameScreen(QWidget):
    def __init__(self, character_data, on_back_callback):
        super().__init__()
        self.character = character_data
        self.on_back_callback = on_back_callback

        self.location_manager = LocationManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 🧙 Karakter Bilgisi
        layout.addWidget(QLabel("🔸 Karakter Bilgisi:"))
        self.character_info_box = QTextEdit()
        self.character_info_box.setReadOnly(True)
        self.character_info_box.setText(self.format_character_info())
        layout.addWidget(self.character_info_box)

        # 📍 Lokasyon Bilgisi
        layout.addWidget(QLabel("🔸 Mevcut Konum:"))
        self.location_label = QLabel()
        layout.addWidget(self.location_label)

        layout.addWidget(QLabel("🔸 Açıklama:"))
        self.description_box = QTextEdit()
        self.description_box.setReadOnly(True)
        layout.addWidget(self.description_box)

        # 🔀 Konum Seçme
        layout.addWidget(QLabel("🔸 Konum Seç:"))
        self.location_dropdown = QComboBox()
        self.location_dropdown.addItems(self.location_manager.get_available_locations())
        self.location_dropdown.setCurrentText(self.location_manager.get_current_location())
        layout.addWidget(self.location_dropdown)

        # 🎮 Butonlar
        move_button = QPushButton("Konuma Git")
        move_button.clicked.connect(self.change_location)
        layout.addWidget(move_button)

        back_button = QPushButton("Ana Menüye Dön")
        back_button.clicked.connect(self.on_back_callback)
        layout.addWidget(back_button)

        self.setLayout(layout)
        self.update_location_display()

    def format_character_info(self):
        """Karakter sözlüğünü güzel biçimlendirir."""
        info = []
        for key, value in self.character.items():
            info.append(f"{key.capitalize()}: {value}")
        return "\n".join(info)

    def change_location(self):
        selected = self.location_dropdown.currentText()
        if self.location_manager.move_to(selected):
            self.update_location_display()

    def update_location_display(self):
        current = self.location_manager.get_current_location()
        self.location_label.setText(current)

        info = self.location_manager.get_current_location_info()
        self.description_box.setText(info.get("açıklama", "Açıklama bulunamadı."))
