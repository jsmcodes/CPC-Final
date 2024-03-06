from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt

import sys

from dev_functions.database_manager import DatabaseManager
from UI.main_ui import Ui_MainWindow
from main_login import Login
from main_content import Content


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database = DatabaseManager()
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.login_page = Login(self)
        self.content_page = Content(self)

        self.add_pages(self.login_page, self.content_page)

    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def add_pages(self, *pages: QWidget) -> None:
        for page in pages:
            self.ui.stckdwdgt_main.addWidget(page)

    def switch_to_login(self):
        self.ui.stckdwdgt_main.setCurrentIndex(0)

    def switch_to_content(self):
        self.ui.stckdwdgt_main.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
