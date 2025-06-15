# game_engine/location_manager.py

import json
import os

class LocationManager:
    def __init__(self):
        self.path = "data/locations_data.json"
        self.locations = self._load()
        self.current = next(iter(self.locations))  # İlk konumu varsayılan olarak al

    def _load(self):
        if not os.path.exists(self.path):
            return {}

        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_current_location(self) -> str:
        return self.current

    def move_to(self, location_name: str) -> bool:
        if location_name in self.locations:
            self.current = location_name
            return True
        return False

    def get_current_location_info(self) -> dict:
        return self.locations.get(self.current, {})

    def get_available_locations(self) -> list:
        return list(self.locations.keys())

    def go_to_next(self, current: str) -> dict:
        keys = list(self.locations.keys())
        if current in keys:
            idx = keys.index(current)
            next_idx = (idx + 1) % len(keys)
            self.current = keys[next_idx]
            return self.locations[self.current]
        return {}

    def get_location_display_name(self, loc_key: str) -> str:
        # "orman_girisi" → "Orman Girişi"
        return loc_key.replace("_", " ").title()
