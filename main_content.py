from PyQt5.QtWidgets import QMainWindow, QWidget

from dev_functions.database_manager import DatabaseManager
from UI.main_content_ui import Ui_Content
from main_dashboard import Dashboard
from main_consultations import Consultations
from main_services import Services
from main_sales import Sales
from main_payment_methods import PaymentMethods
from main_items import Items
from main_patients import Patients
from main_doctors import Doctors
from main_positions import Positions


class Content(QWidget):
    def __init__(self, parent: QMainWindow):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.user_id: int = None
        self.user_name: str = None
        self.user_position: str = None
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Content()
        self.ui.setupUi(self)

        self.dashbord_page = Dashboard(self)
        self.consultations_page = Consultations(self)
        self.services_page = Services(self)
        self.sales_page = Sales(self)
        self.payment_methods_page = PaymentMethods(self)
        self.items_page = Items(self)
        self.patients_page = Patients(self)
        self.doctors_page = Doctors(self)
        self.positions_page = Positions(self)

        self.add_pages(self.dashbord_page, 
                       self.consultations_page, 
                       self.services_page, 
                       self.sales_page, 
                       self.payment_methods_page, 
                       self.items_page, 
                       self.patients_page, 
                       self.doctors_page, 
                       self.positions_page)

        self.connect_functions()

    def add_pages(self, *pages: QWidget) -> None:
        for page in pages:
            self.ui.stckdwdgt_content.addWidget(page)

    def switch_to_dashboard(self):
        self.ui.stckdwdgt_content.setCurrentIndex(0)

        if self.user_position == "Receptionist" or self.user_position == "Administrator":
            self.dashbord_page.populate_tree()
        else:
            self.dashbord_page.populate_table()

    def switch_to_consultations(self):
        self.ui.stckdwdgt_content.setCurrentIndex(1)
        self.consultations_page.populate_table()

    def switch_to_services(self):
        self.ui.stckdwdgt_content.setCurrentIndex(2)
        self.services_page.populate_table()

    def switch_to_sales(self):
        self.ui.stckdwdgt_content.setCurrentIndex(3)
        self.sales_page.populate_table()

    def switch_to_payment_methods(self):
        self.ui.stckdwdgt_content.setCurrentIndex(4)
        self.payment_methods_page.populate_table()

    def switch_to_items(self):
        self.ui.stckdwdgt_content.setCurrentIndex(5)
        self.items_page.populate_table()

    def switch_to_patients(self):
        self.ui.stckdwdgt_content.setCurrentIndex(6)
        self.patients_page.populate_table()

    def switch_to_doctors(self):
        self.ui.stckdwdgt_content.setCurrentIndex(7)
        self.doctors_page.populate_table()

    def switch_to_positions(self):
        self.ui.stckdwdgt_content.setCurrentIndex(8)
        self.positions_page.populate_table()

    def set_user_id_name_position(self, user_id: int, user_name: str, user_position: str) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.user_position = user_position

        self.ui.lbl_name.setText(self.user_name)
        self.ui.lbl_position.setText(self.user_position)

    def set_navigation_for_receptionists(self):
        self.ui.pshbtn_payment_methods.hide()
        self.ui.pshbtn_sales.hide()
        self.ui.pshbtn_services.hide()
        self.ui.pshbtn_settings.hide()
        self.ui.pshbtn_reports.hide()
        self.ui.pshbtn_positions.hide()
        self.dashbord_page.set_ui_for_receptionists()
        self.doctors_page.set_ui_for_receptionist()

    def set_navigation_for_administrator(self):
        self.ui.pshbtn_doctors.setText("Users")
        self.dashbord_page.set_ui_for_administrators()

    def set_navigation_for_doctors(self):
        self.ui.pshbtn_reports.hide()
        self.ui.pshbtn_services.hide()
        self.ui.pshbtn_sales.hide()
        self.ui.pshbtn_payment_methods.hide()
        self.ui.pshbtn_positions.hide()
        self.ui.pshbtn_doctors.hide()
        self.ui.pshbtn_items.hide()
        self.ui.pshbtn_settings.hide()
        self.dashbord_page.set_ui_for_doctors()
        self.consultations_page.set_ui_for_doctors()
        self.patients_page.set_ui_for_doctors()

    def handle_logout(self):
        self.dashbord_page.reset_ui()
        self.consultations_page.reset_ui()
        self.doctors_page.reset_ui()
        self.patients_page.reset_ui()
        self.reset_all_navigation()
        self.parent.switch_to_login()

    def reset_all_navigation(self):
        self.ui.pshbtn_reports.show()
        self.ui.pshbtn_services.show()
        self.ui.pshbtn_sales.show()
        self.ui.pshbtn_payment_methods.show()
        self.ui.pshbtn_items.show()
        self.ui.pshbtn_doctors.show()
        self.ui.pshbtn_positions.show()
        self.ui.pshbtn_settings.show()
        self.ui.pshbtn_doctors.setText("Doctors")

    def connect_functions(self):
        self.ui.pshbtn_dashboard.clicked.connect(self.switch_to_dashboard)
        self.ui.pshbtn_consultations.clicked.connect(self.switch_to_consultations)
        self.ui.pshbtn_services.clicked.connect(self.switch_to_services)
        self.ui.pshbtn_sales.clicked.connect(self.switch_to_sales)
        self.ui.pshbtn_payment_methods.clicked.connect(self.switch_to_payment_methods)
        self.ui.pshbtn_items.clicked.connect(self.switch_to_items)
        self.ui.pshbtn_patients.clicked.connect(self.switch_to_patients)
        self.ui.pshbtn_doctors.clicked.connect(self.switch_to_doctors)
        self.ui.pshbtn_positions.clicked.connect(self.switch_to_positions)
        self.ui.pshbtn_logout.clicked.connect(self.handle_logout)
