from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel
)
from PySide6.QtCore import Qt
import sys

from ui.character_screen import CharacterScreen
from ui.game_screen import GameScreen


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AI RPG")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        title_label = QLabel("AI RPG - Ana Menü")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        new_game_button = QPushButton("Yeni Oyun")
        new_game_button.clicked.connect(self.start_new_game)
        layout.addWidget(new_game_button)

        load_game_button = QPushButton("Oyunu Yükle")
        layout.addWidget(load_game_button)

        quit_button = QPushButton("Çıkış")
        quit_button.clicked.connect(QApplication.instance().quit)
        layout.addWidget(quit_button)

    def start_new_game(self):
        self.character_screen = CharacterScreen(
            on_character_selected_callback=self.launch_game,
            on_back_callback=self.show_main_menu
        )
        self.character_screen.show()
        self.hide()

    def show_main_menu(self):
        self.show()
        if hasattr(self, 'character_screen'):
            self.character_screen.hide()
        if hasattr(self, 'game_screen'):
            self.game_screen.hide()

    def launch_game(self, character):
        self.game_screen = GameScreen(character, self.show_main_menu)
        self.game_screen.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
