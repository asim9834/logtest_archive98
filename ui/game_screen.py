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

        # Karakter bilgisi paneli
        layout.addWidget(QLabel("Karakter Bilgisi:"))
        self.character_info_box = QTextEdit()
        self.character_info_box.setReadOnly(True)
        self.character_info_box.setText(self.format_character_info())
        layout.addWidget(self.character_info_box)

        # Lokasyon bilgileri paneli
        self.location_label = QLabel()
        self.description_box = QTextEdit()
        self.description_box.setReadOnly(True)

        self.location_dropdown = QComboBox()
        self.location_dropdown.addItems(self.location_manager.get_available_locations())
        self.location_dropdown.setCurrentText(self.location_manager.get_current_location())

        move_button = QPushButton("Konuma Git")
        move_button.clicked.connect(self.change_location)

        back_button = QPushButton("Ana Menüye Dön")
        back_button.clicked.connect(self.on_back_callback)

        layout.addWidget(QLabel("Mevcut Konum:") )
        layout.addWidget(self.location_label)
        layout.addWidget(QLabel("Açıklama:") )
        layout.addWidget(self.description_box)
        layout.addWidget(QLabel("Konum Seç:"))
        layout.addWidget(self.location_dropdown)
        layout.addWidget(move_button)
        layout.addWidget(back_button)

        self.setLayout(layout)
        self.update_location_display()

    def change_location(self):
        selected_location = self.location_dropdown.currentText()
        if self.location_manager.move_to(selected_location):
            self.update_location_display()

    def update_location_display(self):
        current = self.location_manager.get_current_location()
        self.location_label.setText(current)

        info = self.location_manager.get_current_location_info()
        self.description_box.setText(info.get("açıklama", "Bilinmeyen yer."))

    def format_character_info(self):
        lines = []
        for key, value in self.character.items():
            lines.append(f"{key}: {value}")
        return "\n".join(lines)
