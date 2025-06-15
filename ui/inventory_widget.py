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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.inventory = Inventory()  # Envanter sınıfından yeni örnek
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
        for item in self.inventory.list_items():
            self.item_list.addItem(item)

    def add_item(self):
        """
        Basit bir örnek: her eklemede seçeceğin veya rastgele bir item ekle.
        İleride karakter ekranından, altın, anahtar, sağlık iksiri gibi somut itemler eklenebilir.
        """
        # Örnek isimle yeni item ekleniyor
        new_item = f"Eşya{len(self.inventory.list_items()) + 1}"
        self.inventory.add_item(new_item)
        self.refresh_list()

    def remove_item(self):
        """Seçili öğeyi envanterden çıkarır"""
        selected = self.item_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek eşyayı seçin.")
            return
        item = selected.text()
        self.inventory.remove_item(item)
        self.refresh_list()
