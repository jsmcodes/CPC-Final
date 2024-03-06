from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate

from dev_functions.database_manager import DatabaseManager
from UI.main_dashboard_consultation_dialog_ui import Ui_DoctorConsultationDialog


class DoctorConsultationDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, patient_id: int, consultation_id: int=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.patient_id = patient_id
        self.consultation_id = consultation_id
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_DoctorConsultationDialog()
        self.ui.setupUi(self)

        if self.purpose == "View":
            self.set_ui_for_view()
        elif self.purpose == "Edit":
            self.set_ui_for_edit()
        else:
            self.set_ui_for_add()

        self.connect_functions()
        
    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def set_ui_for_view(self):
        self.ui.wdgt_scrllarea_medical_history.setEnabled(False)
        self.ui.wdgt_scrllarea_patient_record.setEnabled(False)
        self.ui.pshbtn_create_prescription.hide()
        self.ui.pshbtn_finish_consultation.hide()
        self.ui.pshbtn_save.hide()

    def set_ui_for_edit(self):
        self.ui.pshbtn_create_prescription.hide()
        self.ui.pshbtn_finish_consultation.hide()

    def set_ui_for_add(self):
        self.ui.pshbtn_previous.hide()
        self.ui.pshbtn_next.hide()
        self.ui.pshbtn_save.hide()
        self.ui.pshbtn_view_prescription.hide()

    def handle_finish_close(self):
        def finish_consultation():
            self.database.connect()
            
            query = f"""
                UPDATE
                    consultations
                SET
                    status = 'Done'
                WHERE
                    id = {self.consultation_id}
            """
            self.database.c.execute(query)

            self.database.conn.commit()

            self.database.disconnect()

        if self.purpose == "Add":
            finish_consultation()
            self.accept()
        else:
            self.reject()

    def handle_close(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_finish_consultation.clicked.connect(self.handle_finish_close)
        self.ui.pshbtn_close.clicked.connect(self.handle_close)