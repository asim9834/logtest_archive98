class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, description=""):
        item = {"name": item_name, "description": description}
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item["name"] != item_name]

    def get_items(self):
        return self.items

    def has_item(self, item_name):
        return any(item["name"] == item_name for item in self.items)

    def clear(self):
        self.items.clear()
