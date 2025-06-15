# game_engine/inventory.py

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        """Envantere bir eşya ekle"""
        self.items.append(item)

    def remove_item(self, item: str):
        """Eşyayı envanterden çıkar (varsa)"""
        if item in self.items:
            self.items.remove(item)

    def has_item(self, item: str) -> bool:
        """Belirli bir eşya envanterde var mı?"""
        return item in self.items

    def list_items(self) -> list:
        """Tüm eşyaları döndür"""
        return self.items

    def clear(self):
        """Tüm eşyaları temizle"""
        self.items.clear()
