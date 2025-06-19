# tests/test_game_screen_integration.py

import pytest
from ui.game_screen import GameScreen
from PySide6.QtWidgets import QApplication

@pytest.fixture
def sample_character():
    return {
        "id": "testchar_01",
        "name": "Testman",
        "race": "İnsan",
        "class": "Büyücü",
        "story": "Bir zamanlar bir test dünyasında doğmuştu."
    }

def dummy_callback():
    pass

def test_inventory_widget_attached(qtbot, sample_character):
    game_screen = GameScreen(sample_character, dummy_callback)
    qtbot.addWidget(game_screen)

    inventory_found = hasattr(game_screen, "inventory_widget")
    assert inventory_found, "inventory_widget özelliği game_screen içinde yok."

    assert game_screen.inventory_widget is not None, "inventory_widget None olarak ayarlanmış."
