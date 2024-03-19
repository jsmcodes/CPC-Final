from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

from dev_functions.database_manager import DatabaseManager
from UI.main_services_dialog_ui import Ui_ServiceDialog


class ServiceDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, service_id: int=None, service_name: str=None, service_price: float=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.service_id = service_id
        self.service_name = service_name
        self.service_price = service_price
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_ServiceDialog()
        self.ui.setupUi(self)

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setBottom(0.00)
        self.ui.lnedit_price.setValidator(validator)

        if self.purpose == "Edit":
            self.set_service_data()

            self.ui.pshbtn_add_save.setText("Save")
            self.ui.pshbtn_clear_reset.setText("Reset")
        else:
            self.set_service_id()

        self.connect_functions()

    def set_service_data(self):
        self.ui.lbl_service_id.setText(f"Service #{self.service_id}")
        self.ui.lnedit_service_name.setText(self.service_name)
        self.ui.lnedit_price.setText(self.service_price)

    def set_service_id(self):
        def fetch_last_service_id():
            self.database.connect()

            query = """
                SELECT
                    MAX(id)
                FROM
                    services
            """
            self.database.c.execute(query)

            last_service_id = self.database.c.fetchone()

            self.database.disconnect()

            return last_service_id
        
        last_service_id = fetch_last_service_id()[0]
        if last_service_id is None:
            last_service_id = 0
        self.service_id = last_service_id + 1

        self.ui.lbl_service_id.setText(f"Service #{self.service_id}")
        
    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def handle_add_save(self):
        service_name = self.ui.lnedit_service_name.text().strip()
        price = self.ui.lnedit_price.text().strip()

        if service_name and price:
            if self.purpose == "Edit":
                self.update_service(service_name, price)
            else:
                self.insert_service(service_name, price)
            self.accept()

    def insert_service(self, service_name: str, price: float):
        self.database.connect()

        query = f"""
            INSERT INTO
                services (
                    name,
                    price
                )
            VALUES (
                '{service_name}',
                {price}
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def update_service(self, service_name: str, price: float):
        self.database.connect()

        query = f"""
            UPDATE
                services
            SET
                name = '{service_name}',
                price = {price}
            WHERE
                id = {self.service_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        if self.purpose == "Edit":
            self.ui.lnedit_service_name.setText(self.service_name)
            self.ui.lnedit_price.setText(self.service_price)
        else:
            self.ui.lnedit_service_name.clear()
            self.ui.lnedit_price.clear()

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
