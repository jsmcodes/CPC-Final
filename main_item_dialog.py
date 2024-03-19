from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

from dev_functions.database_manager import DatabaseManager
from UI.main_item_dialog_ui import Ui_ItemDIalog


class ItemDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, item_id: int=None, item_name: str=None, item_price: float=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_ItemDIalog()
        self.ui.setupUi(self)

        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setBottom(0.00)
        self.ui.lnedit_item_price.setValidator(validator)

        if self.purpose == "Edit":
            self.set_item_data()

            self.ui.pshbtn_add_save.setText("Save")
            self.ui.pshbtn_clear_reset.setText("Reset")
        else:
            self.set_item_id()

        self.connect_functions()

    def set_item_data(self):
        self.ui.lbl_item_id.setText(f"Item #{self.item_id}")
        self.ui.lnedit_item_name.setText(self.item_name)
        self.ui.lnedit_item_price.setText(self.item_price)

    def set_item_id(self):
        def fetch_last_item_id():
            self.database.connect()

            query = """
                SELECT
                    MAX(id)
                FROM
                    items
            """
            self.database.c.execute(query)

            last_item_id = self.database.c.fetchone()

            self.database.disconnect()

            return last_item_id
        
        last_item_id = fetch_last_item_id()[0]
        if last_item_id is None:
            last_item_id = 0
        self.item_id = last_item_id + 1

        self.ui.lbl_item_id.setText(f"Item #{self.item_id}")
        
    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def handle_add_save(self):
        item_name = self.ui.lnedit_item_name.text().strip()
        item_price = self.ui.lnedit_item_price.text().strip()

        if item_name and item_price:
            if self.purpose == "Edit":
                self.update_item(item_name, item_price)
            else:
                self.insert_item(item_name, item_price)
            self.accept()

    def insert_item(self, item_name: str, item_price: float):
        self.database.connect()

        query = f"""
            INSERT INTO
                items (
                    name,
                    price
                )
            VALUES (
                '{item_name}',
                {item_price}
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def update_item(self, item_name: str, item_price: float):
        self.database.connect()

        query = f"""
            UPDATE
                items
            SET
                name = '{item_name}',
                price = {item_price}
            WHERE
                id = {self.item_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        if self.purpose == "Edit":
            self.ui.lnedit_item_name.setText(self.service_name)
            self.ui.lnedit_item_price.setText(self.service_price)
        else:
            self.ui.lnedit_item_name.clear()
            self.ui.lnedit_item_price.clear()

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
