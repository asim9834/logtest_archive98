# game_engine/inventory.py

import json
import os


class Inventory:
    def __init__(self, player_id, storage_path="data/inventories.json"):
        self.player_id = player_id
        self.storage_path = storage_path
        self.inventories = self._load_inventories()

    def _load_inventories(self):
        if not os.path.exists(self.storage_path):
            return {}

        with open(self.storage_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_inventories(self):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(self.inventories, f, indent=2, ensure_ascii=False)

    def get_items(self):
        return self.inventories.get(self.player_id, [])

    def add_item(self, item):
        if self.player_id not in self.inventories:
            self.inventories[self.player_id] = []

        self.inventories[self.player_id].append(item)
        self._save_inventories()

    def remove_item(self, item_name):
        if self.player_id in self.inventories:
            original_len = len(self.inventories[self.player_id])
            self.inventories[self.player_id] = [
                item for item in self.inventories[self.player_id]
                if item.get("name") != item_name
            ]
            self._save_inventories()
            return len(self.inventories[self.player_id]) < original_len
        return False


    def has_item(self, item_name):
        return any(item.get("name") == item_name for item in self.get_items())

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "items": self.get_items()
        }

    @classmethod
    def from_dict(cls, data):
        inv = cls(data.get("player_id", "unknown"))
        inv.inventories[inv.player_id] = data.get("items", [])
        inv._save_inventories()
        return inv
