from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel

class InventoryWidget(QWidget):
    def __init__(self, items):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Envanter:"))
        
        self.list_widget = QListWidget()
        for item in items:
            self.list_widget.addItem(item)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)
