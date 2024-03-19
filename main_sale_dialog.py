from PyQt5.QtWidgets import QDialog, QWidget, QHeaderView
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QDoubleValidator

from dev_functions.database_manager import DatabaseManager
from UI.main_sale_dialog_ui import Ui_SaleDialog


class SaleDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, current_user_name: str=None, sale_id: int=None, sale_date: str=None, patient_name: str=None, user_name: str=None, total_price: str=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.current_user_name = current_user_name
        self.sale_id = sale_id
        self.sale_date = sale_date
        self.patient_name = patient_name
        self.user_name = user_name
        self.total_price = total_price
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_SaleDialog()
        self.ui.setupUi(self)

        self.ui.cmbbx_patient_name.lineEdit().setAlignment(Qt.AlignCenter)
        self.ui.cmbbx_item_name.lineEdit().setAlignment(Qt.AlignCenter)
        self.ui.cmbbx_mode_of_payment.lineEdit().setAlignment(Qt.AlignCenter)

        self.ui.tblwdgt_cart.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.insert_patients()
        self.ui.cmbbx_patient_name.setCurrentIndex(1)

        self.insert_payment_methods()

        if self.purpose == "Add":
            self.set_sale_id()
            current_date = QDate.currentDate().toString("MMM dd, yyyy")
            self.ui.lnedit_date.setText(current_date)
            self.ui.lnedit_receptionist_name.setText(self.current_user_name)

        self.connect_functions()

    def set_sale_data(self):
        self.ui.lnedit_id.setText(self.sale_id)
        self.ui.lnedit_date.setText(self.sale_date)
        self.ui.cmbbx_patient_name.setText(self.patient_name)
        self.ui.lnedit_receptionist_name.setText(self.user_name)
        self.ui.lnedit_total_amount.setText(self.total_price)

    def set_sale_id(self):
        def fetch_last_sale_id():
            self.database.connect()

            query = """
                SELECT
                    MAX(id)
                FROM
                    sales
            """
            self.database.c.execute(query)

            last_sale_id = self.database.c.fetchone()

            self.database.disconnect()

            return last_sale_id
        
        last_sale_id = fetch_last_sale_id()[0]
        if last_sale_id is None:
            last_sale_id = 0
        self.sale_id = last_sale_id + 1

        self.ui.lnedit_id.setText(str(self.sale_id))
        
    def insert_patients(self):
        def fetch_patients():
            self.database.connect()

            query = """
                SELECT
                    name
                FROM
                    patients
                WHERE
                    archived = 0
            """
            self.database.c.execute(query)

            patients = self.database.c.fetchall()

            self.database.disconnect()

            return patients
        
        self.ui.cmbbx_patient_name.clear()
        self.ui.cmbbx_patient_name.addItem("Add New")
        self.ui.cmbbx_patient_name.addItem("Walk-In")
        
        patients = fetch_patients()

        if not patients:
            return

        for patient in patients:
            patient_name = patient[0]

            self.ui.cmbbx_patient_name.addItem(patient_name)

    def insert_payment_methods(self):
        def fetch_payment_methods():
            self.database.connect()

            query = """
                SELECT
                    name
                FROM
                    payment_methods
                WHERE
                    archived = 0
            """
            self.database.c.execute(query)

            payment_methods = self.database.c.fetchall()

            self.database.disconnect()

            return payment_methods
        
        self.ui.cmbbx_mode_of_payment.clear()
        
        payment_methods = fetch_payment_methods()

        if not payment_methods:
            return

        for payment_method in payment_methods:
            payment_method_name = payment_method[0]

            self.ui.cmbbx_mode_of_payment.addItem(payment_method_name)

    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
