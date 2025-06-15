# ui/character_card.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QTextEdit, QFrame
)
from PySide6.QtCore import Qt


class CharacterCard(QWidget):
    def __init__(self, character_data: dict, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        content = QWidget()
        content_layout = QVBoxLayout(content)

        # Başlık
        name = character_data.get("name", "Bilinmeyen")
        race = character_data.get("race", "Bilinmeyen")
        char_class = character_data.get("class", "Bilinmeyen")

        title = QLabel(f"<h2>{name}</h2><b>{race} - {char_class}</b>")
        title.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(title)

        # Ayırıcı çizgi
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        content_layout.addWidget(line)

        # Açıklama (backstory)
        backstory = character_data.get("story", "Hikaye bulunamadı.")
        story_box = QTextEdit()
        story_box.setReadOnly(True)
        story_box.setText(backstory)
        story_box.setMinimumHeight(200)
        content_layout.addWidget(story_box)

        self.scroll.setWidget(content)
        layout.addWidget(self.scroll)
