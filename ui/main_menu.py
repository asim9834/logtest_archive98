from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class MainMenu(QWidget):
    def __init__(self, start_game_callback):
        super().__init__()
        self.start_game_callback = start_game_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("RPG Game")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 32px; font-weight: bold;")

        new_game_btn = QPushButton("Yeni Oyuna Başla")
        new_game_btn.clicked.connect(self.start_game_callback)

        exit_btn = QPushButton("Çıkış")
        exit_btn.clicked.connect(self.close_app)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(new_game_btn)
        layout.addWidget(exit_btn)
        layout.addStretch()

        self.setLayout(layout)

    def close_app(self):
        self.window().close()
