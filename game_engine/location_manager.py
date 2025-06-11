
import json
import os

class LocationManager:
    def __init__(self, data_path=None):
        if data_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(base_dir, "..", "data", "locations_data.json")
        self.data_path = data_path
        self.locations = {}
        self.current_location = None
        self.load_locations()

    def load_locations(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r', encoding='utf-8') as f:
                self.locations = json.load(f)
            if self.locations:
                self.current_location = list(self.locations.keys())[0]
        else:
            self.locations = {}

    def get_current_location(self):
        return self.current_location

    def get_current_location_info(self):
        if self.current_location:
            return self.locations.get(self.current_location, {})
        return {}

    def get_available_locations(self):
        return list(self.locations.keys())

    def move_to(self, location_name):
        if location_name in self.locations:
            self.current_location = location_name
            return True
        return False
