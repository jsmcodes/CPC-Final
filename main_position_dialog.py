from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt

from dev_functions.database_manager import DatabaseManager
from UI.main_position_dialog_ui import Ui_PositionDialog


class PositionDialog(QDialog):
    def __init__(self, parent: QWidget, edit: bool=False, position_id: int=None, position_name: str=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.edit = edit
        self.position_id = position_id
        self.position_name = position_name
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_PositionDialog()
        self.ui.setupUi(self)

        if self.edit:
            self.set_patient_data()
        else:
            self.set_patient_id()

            self.ui.pshbtn_add_save.setText("Add")
            self.ui.pshbtn_clear_reset.setText("Clear")

        self.connect_functions()

    def set_patient_data(self):
        self.ui.lbl_position_id.setText(f"Position #{self.position_id}")
        self.ui.lnedit_name.setText(self.position_name)

    def set_patient_id(self):
        self.database.connect()

        query = """
            SELECT
                MAX(id)
            FROM
                positions
        """
        self.database.c.execute(query)

        last_position_id = self.database.c.fetchone()

        self.database.disconnect()
        
        self.position_id = last_position_id[0] + 1
        self.ui.lbl_position_id.setText(f"Position #{self.position_id}")

        self.database.disconnect()
        
    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def handle_add_save(self):
        position_name = self.ui.lnedit_name.text().strip()

        if position_name:
            if self.edit:
                self.update_position_name(position_name)
            else:
                self.insert_position_name(position_name)
            self.accept()

    def insert_position_name(self, position_name: str):
        self.database.connect()

        query = f"""
            INSERT INTO
                positions (
                    name
                )
            VALUES (
                '{position_name}'
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def update_position_name(self, position_name: str):
        self.database.connect()

        query = f"""
            UPDATE
                positions
            SET
                name = '{position_name}'
            WHERE
                id = {self.position_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        if self.edit:
            self.ui.lnedit_name.setText(self.position_name)
        else:
            self.ui.lnedit_name.clear()

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
