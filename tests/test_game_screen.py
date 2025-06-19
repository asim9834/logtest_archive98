# test_game_screen.py
# Testler: Oyun ekranı (GameScreen) arayüz bileşenleri ve lokasyon yönetimi

import pytest
from PySide6.QtWidgets import QApplication
from ui.game_screen import GameScreen

@pytest.fixture
def app(qtbot):
    dummy_character = {"name": "Test", "race": "Elf", "class": "Mage", "story": "A test subject."}
    test_widget = GameScreen(dummy_character, lambda: None)
    qtbot.addWidget(test_widget)
    return test_widget

def test_game_screen_ui_elements(app):
    assert app.character_info_box.toPlainText() != ""
    assert app.location_dropdown.count() > 0
    assert app.description_box.isReadOnly()
