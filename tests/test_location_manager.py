# tests/test_location_manager.py

import os
import json
import tempfile
import pytest
from game_engine.location_manager import LocationManager

@pytest.fixture
def temp_location_file():
    locations = {
        "orman_girisi": {"açıklama": "Yoğun ağaçlarla çevrili karanlık bir ormanın girişi."},
        "gizli_mağara": {"açıklama": "Eski bir efsaneye göre bu mağarada büyülü yaratıklar yaşarmış."}
    }
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    with open(tmp_file.name, "w", encoding="utf-8") as f:
        json.dump(locations, f, ensure_ascii=False)
    yield tmp_file.name
    os.remove(tmp_file.name)

def test_initial_location(temp_location_file, monkeypatch):
    monkeypatch.setattr("game_engine.location_manager.LocationManager._load", lambda self: json.load(open(temp_location_file, "r", encoding="utf-8")))
    manager = LocationManager()
    assert manager.get_current_location() == "orman_girisi"

def test_move_to_location(temp_location_file, monkeypatch):
    monkeypatch.setattr("game_engine.location_manager.LocationManager._load", lambda self: json.load(open(temp_location_file, "r", encoding="utf-8")))
    manager = LocationManager()
    assert manager.move_to("gizli_mağara")
    assert manager.get_current_location() == "gizli_mağara"

def test_get_location_info(temp_location_file, monkeypatch):
    monkeypatch.setattr("game_engine.location_manager.LocationManager._load", lambda self: json.load(open(temp_location_file, "r", encoding="utf-8")))
    manager = LocationManager()
    info = manager.get_current_location_info()
    assert "açıklama" in info
