import os
import json
import tempfile
import pytest
from game_engine.location_manager import LocationManager

@pytest.fixture
def temp_location_file(monkeypatch):
    # Geçici dosya yolu oluştur
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode='w', encoding="utf-8") as tmp:
        locations = {
            "orman_girisi": {"açıklama": "Yoğun ağaçlarla çevrili karanlık bir ormanın girişi."},
            "gizli_mağara": {"açıklama": "Eski bir efsaneye göre bu mağarada büyülü yaratıklar yaşarmış."}
        }
        json.dump(locations, tmp, ensure_ascii=False)
        tmp_path = tmp.name

    # monkeypatch ile dosya yüklemeyi geçici olarak override et
    monkeypatch.setattr("game_engine.location_manager.LocationManager._load", lambda self: json.load(open(tmp_path, "r", encoding="utf-8")))

    yield tmp_path

    # Test sonunda dosya silinir (Windows kilit problemi çözülür)
    os.remove(tmp_path)

def test_initial_location(temp_location_file):
    manager = LocationManager()
    assert manager.get_current_location() == "orman_girisi"

def test_move_to_location(temp_location_file):
    manager = LocationManager()
    assert manager.move_to("gizli_mağara")
    assert manager.get_current_location() == "gizli_mağara"

def test_get_location_info(temp_location_file):
    manager = LocationManager()
    info = manager.get_current_location_info()
    assert "açıklama" in info
