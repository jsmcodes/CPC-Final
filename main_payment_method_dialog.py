from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

from dev_functions.database_manager import DatabaseManager
from UI.main_payment_method_dialog_ui import Ui_PaymentMethodDialog


class PaymentMethodDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, method_id: int=None, method_name: str=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.method_id = method_id
        self.method_name = method_name
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_PaymentMethodDialog()
        self.ui.setupUi(self)

        if self.purpose == "Edit":
            self.set_service_data()

            self.ui.pshbtn_add_save.setText("Save")
            self.ui.pshbtn_clear_reset.setText("Reset")
        else:
            self.set_method_id()

        self.connect_functions()

    def set_service_data(self):
        self.ui.lbl_payment_method_id.setText(f"Payment Method #{self.method_id}")
        self.ui.lnedit_payment_method_name.setText(self.method_name)

    def set_method_id(self):
        def fetch_last_method_id():
            self.database.connect()

            query = """
                SELECT
                    MAX(id)
                FROM
                    payment_methods
            """
            self.database.c.execute(query)

            last_method_id = self.database.c.fetchone()

            self.database.disconnect()

            return last_method_id
        
        last_method_id = fetch_last_method_id()[0]
        if last_method_id is None:
            last_method_id = 0
        self.method_id = last_method_id + 1

        self.ui.lbl_payment_method_id.setText(f"Payment Method #{self.method_id}")
        
    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def handle_add_save(self):
        method_name = self.ui.lnedit_payment_method_name.text().strip()

        if method_name:
            if self.purpose == "Edit":
                self.update_method(method_name)
            else:
                self.insert_method(method_name)
            self.accept()

    def insert_method(self, service_name: str):
        self.database.connect()

        query = f"""
            INSERT INTO
                payment_methods (
                    name
                )
            VALUES (
                '{service_name}'
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def update_method(self, service_name: str):
        self.database.connect()

        query = f"""
            UPDATE
                payment_methods
            SET
                name = '{service_name}'
            WHERE
                id = {self.method_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        if self.purpose == "Edit":
            self.ui.lnedit_payment_method_name.setText(self.method_name)
        else:
            self.ui.lnedit_payment_method_name.clear()

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
