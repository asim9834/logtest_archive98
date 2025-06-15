import sys
from PySide6.QtWidgets import QApplication, QStackedWidget

from ui.main_menu import MainMenu
from ui.character_screen import CharacterScreen
from ui.game_screen import GameScreen

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG Project")
        self.setFixedSize(1000, 600)

        self.main_menu = MainMenu(self.start_new_game)
        self.addWidget(self.main_menu)

        self.character_screen = None
        self.game_screen = None

        self.setCurrentWidget(self.main_menu)

    def start_new_game(self):
        self.character_screen = CharacterScreen(
            on_character_selected_callback=self.launch_game,
            on_back_callback=self.return_to_main_menu
        )
        self.addWidget(self.character_screen)
        self.setCurrentWidget(self.character_screen)

    def return_to_main_menu(self):
        self.setCurrentWidget(self.main_menu)

    def launch_game(self, selected_character):
        self.game_screen = GameScreen(selected_character, self.return_to_main_menu)
        self.addWidget(self.game_screen)
        self.setCurrentWidget(self.game_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
