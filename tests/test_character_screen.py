# tests/test_character_screen.py
# Testler: Karakter ekranı (CharacterScreen) arayüz bileşenleri ve etkileşimler

import pytest
from PySide6.QtWidgets import QApplication, QPushButton
from ui.character_screen import CharacterScreen

@pytest.fixture
def app(qtbot):
    test_widget = CharacterScreen(lambda c: None, lambda: None)
    qtbot.addWidget(test_widget)
    return test_widget

def test_character_screen_ui_elements(app):
    # Temel alanlar var mı?
    assert app.name_input is not None
    assert app.race_combo is not None
    assert app.class_combo is not None
    assert app.description_input is not None

    # Temel butonlar var mı?
    assert app.create_button.text().lower() == "create"
    assert app.start_button.text().lower() == "start"
    assert app.random_button.text().lower() == "random"
    assert app.back_button.text().lower() == "back"

    # Liste alanları
    assert app.custom_list.count() >= 1
    assert app.prebuilt_list.count() >= 1

def test_character_screen_advanced_buttons_exist(app):
    # objectName'leri ile doğrudan erişim sağlanıyor mu?
    save_btn = app.findChild(QPushButton, "save_button")
    edit_btn = app.findChild(QPushButton, "edit_button")
    delete_btn = app.findChild(QPushButton, "delete_button")

    assert save_btn is not None
    assert edit_btn is not None
    assert delete_btn is not None

    assert save_btn.text().lower() == "save"
    assert edit_btn.text().lower() == "edit"
    assert delete_btn.text().lower() == "delete"
