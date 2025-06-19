# test_character_screen.py
# Testler: Karakter ekranı (CharacterScreen) arayüz bileşenleri ve etkileşimler

import pytest
from PySide6.QtWidgets import QApplication
from ui.character_screen import CharacterScreen

@pytest.fixture
def app(qtbot):
    test_widget = CharacterScreen(lambda c: None, lambda: None)
    qtbot.addWidget(test_widget)
    return test_widget

def test_character_screen_ui_elements(app):
    assert app.name_input is not None
    assert app.race_combo is not None
    assert app.class_combo is not None
    assert app.create_button.text().lower() == "create"
    assert app.start_button.text().lower() == "start"
    assert app.custom_list.count() >= 1  # Başlık dahil
