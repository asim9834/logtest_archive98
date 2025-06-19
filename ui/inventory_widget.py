# ui/inventory_widget.py

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout, QMessageBox
)
from game_engine.inventory import Inventory


class InventoryWidget(QWidget):
    """
    Envanter listesini gösteren ve yönetimini sağlayan GUI bileşeni.
    - Eşyaları liste olarak gösterir
    - Ekle/Sil butonları ile etkileşim sağlar
    """

    def __init__(self, player_id="test_player", parent=None):
        super().__init__(parent)
        self.player_id = player_id
        self.inventory = Inventory(player_id=self.player_id)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Envanteriniz:"))  # Başlık

        self.item_list = QListWidget()
        layout.addWidget(self.item_list, 1)

        # Ekle–Sil butonlarını yatay ekliyoruz
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Ekle")
        remove_btn = QPushButton("Sil")
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(remove_btn)
        layout.addLayout(btn_layout)

        # Butonların işlevleri
        add_btn.clicked.connect(self.add_item)
        remove_btn.clicked.connect(self.remove_item)

        self.refresh_list()

    def refresh_list(self):
        """Envanter güncellemelerini listeye yansıtır"""
        self.item_list.clear()
        for item in self.inventory.get_items():
            # Eşya dict ise 'name' göster, değilse direkt yaz
            display = item.get("name") if isinstance(item, dict) else str(item)
            self.item_list.addItem(display)

    def add_item(self):
        """Basit bir örnek: her eklemede rastgele bir test item eklenir"""
        index = len(self.inventory.get_items()) + 1
        new_item = {
            "id": f"item_{index}",
            "name": f"Deneme Eşyası {index}",
            "type": "misc",
            "value": 0
        }
        self.inventory.add_item(new_item)
        self.refresh_list()

    def remove_item(self):
        """Seçili öğeyi envanterden çıkarır"""
        selected = self.item_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek eşyayı seçin.")
            return

        name = selected.text()
        success = self.inventory.remove_item(name)
        if not success:
            QMessageBox.warning(self, "Hata", f"{name} envanterde bulunamadı.")
        self.refresh_list()
