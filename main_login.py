from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from loguru import logger

from dev_functions.database_manager import DatabaseManager
from UI.main_login_ui import Ui_Login


class Login(QWidget):
    def __init__(self, parent: QMainWindow):
        super().__init__()
        logger.add("Logging/login.log", rotation="1 day", compression="zip", level="INFO")
        self.database = DatabaseManager()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.connect_functions()

    def handle_login(self):
        user_data = self.check_if_user_exists()

        if user_data:
            user_id, user_name, user_position = user_data
            self.parent.content_page.set_user_id_name_position(user_id, user_name, user_position)
            self.clear_inputs()
            self.parent.switch_to_content()

            if user_position == "Receptionist":
                self.parent.content_page.set_navigation_for_receptionists()
            elif user_position == "Administrator":
                self.parent.content_page.set_navigation_for_administrator()
            else:
                self.parent.content_page.set_navigation_for_doctors()
            self.parent.content_page.switch_to_dashboard()
        else:
            self.clear_inputs()

    def clear_inputs(self):
        self.ui.lnedit_username.clear()
        self.ui.lnedit_password.clear()
        self.ui.lnedit_username.setFocus()

    def handle_exit(self):
        self.parent.close()

    def check_if_user_exists(self) -> list:
        input_username = self.ui.lnedit_username.text()
        input_password = self.ui.lnedit_password.text()

        if input_username and input_password:
            self.database.connect()

            query = f"""
                SELECT
                    u.id,
                    u.name,
                    p.name
                FROM
                    users AS u
                JOIN
                    positions AS p
                ON
                    u.position_id = p.id
                WHERE
                    u.username = '{input_username}'
                AND
                    u.password = '{input_password}'
            """
            self.database.c.execute(query)

            user_data = self.database.c.fetchone()

            self.database.disconnect()

            return user_data

    def connect_functions(self):
        self.ui.pshbtn_login.clicked.connect(self.handle_login)

        self.ui.pshbtn_exit.clicked.connect(self.handle_exit)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_login()