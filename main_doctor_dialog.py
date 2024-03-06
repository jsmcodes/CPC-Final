from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate

from dev_functions.database_manager import DatabaseManager
from UI.main_doctor_dialog_ui import Ui_DoctorDialog
from main_position_dialog import PositionDialog


class DoctorDialog(QDialog):
    def __init__(self, parent: QWidget, edit: bool=False, user_id: int=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.edit = edit
        self.user_id = user_id
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_DoctorDialog()
        self.ui.setupUi(self)

        self.ui.cmbx_position.lineEdit().setAlignment(Qt.AlignCenter)
        self.ui.cmbx_sex.lineEdit().setAlignment(Qt.AlignCenter)
        self.ui.dtedit_birthdate.setMaximumDate(QDate.currentDate())

        self.insert_positions()

        if self.edit:
            self.set_user_data()
        else:
            self.set_user_id()
            self.ui.cmbx_position.setCurrentIndex(1)
            self.ui.pshbtn_add_save.setText("Add")
            self.ui.pshbtn_clear_reset.setText("Clear")
        
        self.connect_functions()

    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def insert_positions(self):
        def fetch_positions():
            self.database.connect()

            query = """
                SELECT
                    name
                FROM
                    positions
                WHERE
                    archived = 0
            """
            self.database.c.execute(query)

            positions = self.database.c.fetchall()

            self.database.disconnect()

            return positions
        
        self.ui.cmbx_position.clear()
        self.ui.cmbx_position.addItem("Add New")
        self.ui.cmbx_position.addItem("Select position...")
        self.ui.cmbx_position.model().item(1).setEnabled(False)

        positions = fetch_positions()

        for position in positions:
            self.ui.cmbx_position.addItem(position[0])

    def handle_add_position(self, index):
        if index == 0:
            self.ui.cmbx_position.setCurrentIndex(1)
            dialog = PositionDialog(self)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.ui.cmbx_position.disconnect()
                self.insert_positions()
                self.ui.cmbx_position.currentIndexChanged.connect(self.handle_add_position)
                self.ui.cmbx_position.setCurrentIndex(1)
            else:
                dialog.close()

    def set_user_id(self):
        self.database.connect()

        query = """
            SELECT
                MAX(id)
            FROM
                users
        """
        self.database.c.execute(query)

        last_user_id = self.database.c.fetchone()

        self.database.disconnect()
        
        self.user_id = last_user_id[0] + 1
        self.ui.lbl_id.setText(f"User #{self.user_id}")

    def set_user_data(self):
        def fetch_user_data():
            self.database.connect()

            query = f"""
                SELECT
                    p.name AS position_name,
                    u.name AS user_name,
                    sex,
                    birthdate,
                    contact_number,
                    address,
                    username,
                    password
                FROM
                    users AS u
                JOIN
                    positions AS p
                ON
                    u.position_id = p.id
                WHERE
                    u.id = {self.user_id}
            """
            self.database.c.execute(query)

            user_data = self.database.c.fetchone()

            self.database.disconnect()

            return user_data
        
        position, name, sex, birthdate, contact_number, address, username, password = fetch_user_data()

        self.ui.lbl_id.setText(f"User #{self.user_id}")
        self.ui.cmbx_position.setCurrentText(position)
        self.ui.lnedit_name.setText(name)
        self.ui.cmbx_sex.setCurrentText(sex)
        self.ui.dtedit_birthdate.setDate(birthdate)
        self.ui.lnedit_contact_number.setText(contact_number)
        self.ui.txtedit_address.setText(address)
        self.ui.lnedit_username.setText(username)
        self.ui.lnedit_password.setText(password)

    def handle_add_save(self):
        def get_position_id(position_name: str):
            self.database.connect()

            query = f"""
                SELECT
                    id
                FROM
                    positions
                WHERE
                    name = '{position_name}'
            """
            self.database.c.execute(query)

            position_id = self.database.c.fetchone()

            self.database.disconnect()

            return position_id

        def get_user_data():
            position_name = self.ui.cmbx_position.currentText()
            name = self.ui.lnedit_name.text().strip()
            sex = self.ui.cmbx_sex.currentText()
            birthdate = self.ui.dtedit_birthdate.date().toPyDate()
            contact_number = self.ui.lnedit_contact_number.text().strip()
            address = self.ui.txtedit_address.toPlainText().strip()
            username = self.ui.lnedit_username.text().strip()
            password = self.ui.lnedit_password.text().strip()

            return position_name, name, sex, birthdate, contact_number, address, username, password
        
        self.ui.pshbtn_add_save.setFocus()

        position_name, name, sex, birthdate, contact_number, address, username, password = get_user_data()

        if position_name != "Add New" and name and contact_number and address and username and password:
            position_id = get_position_id(position_name)
            user_data = position_id[0], name, sex, birthdate, contact_number, address, username, password
            if self.edit:
                self.update_user_data(user_data)
            else:
                self.insert_user_data(user_data)
            self.accept()

    def update_user_data(self, user_data: list):
        self.database.connect()

        position_id, name, sex, birthdate, contact_number, address, username, password = user_data

        query = f"""
            UPDATE
                users
            SET
                position_id = {position_id},
                name = '{name}',
                sex = '{sex}',
                birthdate = '{birthdate}',
                contact_number = '{contact_number}',
                address = '{address}',
                username = '{username}',
                password = '{password}'
            WHERE
                id = {self.user_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def insert_user_data(self, user_data: list):
        self.database.connect()

        position_id, name, sex, birthdate, contact_number, address, username, password = user_data

        query = f"""
            INSERT INTO
                users (
                    position_id,
                    name,
                    sex,
                    birthdate,
                    contact_number,
                    address,
                    username,
                    password
                )
            VALUES (
                {position_id},
                '{name}',
                '{sex}',
                '{birthdate}',
                '{contact_number}',
                '{address}',
                '{username}',
                '{password}'
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        if self.edit:
            self.set_user_data()
        else:
            self.ui.cmbx_position.setCurrentIndex(1)
            self.ui.lnedit_name.clear()
            self.ui.cmbx_sex.setCurrentIndex(0)
            self.ui.dtedit_birthdate.setDate(QDate.currentDate())
            self.ui.lnedit_contact_number.clear()
            self.ui.txtedit_address.clear()
            self.ui.lnedit_username.clear()
            self.ui.lnedit_password.clear()

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.cmbx_position.currentIndexChanged.connect(self.handle_add_position)

        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
