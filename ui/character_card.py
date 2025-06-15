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

        # Ayırıcı
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        content_layout.addWidget(line)

        # Detaylı Bilgi Kutusu
        description = character_data.get("description", "")
        alignment = character_data.get("alignment", "Bilinmiyor")
        level = character_data.get("level", 1)
        stats = character_data.get("stats", {})
        background = character_data.get("background", "")
        personality = character_data.get("personality", "")
        abilities = character_data.get("abilities", [])
        story = character_data.get("story", "Hikaye bulunamadı.")

        # Metin derleme
        detail_text = f"""
▶️ <b>Düzey:</b> {level}
▶️ <b>Hizalanma:</b> {alignment}

<b>Yetenek Puanları:</b>
"""
        for stat, value in stats.items():
            detail_text += f"- {stat.title()}: {value}\n"

        if background:
            detail_text += f"\n<b>Geçmiş:</b>\n{background}"

        if personality:
            detail_text += f"\n<b>Kişilik:</b>\n{personality}"

        if abilities:
            detail_text += "\n<b>Yetenekler:</b>\n"
            for ab in abilities:
                detail_text += f"- {ab}\n"

        detail_text += f"\n<b>Hikaye:</b>\n{story}"

        # Scroll içinde gösterilecek kutu
        info_box = QTextEdit()
        info_box.setReadOnly(True)
        info_box.setText(detail_text.strip())
        info_box.setMinimumHeight(300)
        content_layout.addWidget(info_box)

        self.scroll.setWidget(content)
        layout.addWidget(self.scroll)
