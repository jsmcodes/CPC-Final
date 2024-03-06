from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate

from dev_functions.database_manager import DatabaseManager
from UI.main_consultation_dialog_ui import Ui_ConsultationDialog
from main_patient_dialog import PatientDialog
from main_doctor_dialog import DoctorDialog


class ConsultationDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, consultation_id: int=None, user_position: str=None, patient_name: str=None, doctor_name: str=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.consultation_id = consultation_id
        self.user_position = user_position
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_ConsultationDialog()
        self.ui.setupUi(self)

        self.ui.cmbbx_patient_name.lineEdit().setAlignment(Qt.AlignCenter)
        self.ui.cmbbx_doctor_name.lineEdit().setAlignment(Qt.AlignCenter)

        self.insert_patients()
        self.insert_doctors()

        if self.purpose == "Add":
            self.set_consultation_id()
            self.set_add_ui()
        else:
            self.ui.lbl_consultation_id.setText(f"Consultation #{self.consultation_id}")
            self.set_consultation_data()

        self.connect_functions()

    def set_consultation_id(self):
        def fetch_last_consultation_id():
            self.database.connect()

            query = """
                SELECT
                    MAX(id)
                FROM
                    consultations
            """
            self.database.c.execute(query)

            last_consultation_id = self.database.c.fetchone()

            self.database.disconnect()

            return last_consultation_id
        
        self.consultation_id = fetch_last_consultation_id()[0] + 1

        self.ui.lbl_consultation_id.setText(f"Consultation #{self.consultation_id}")

    def set_add_ui(self):
        self.ui.pshbtn_add_save.setText("Add")
        self.ui.pshbtn_clear_reset.setText("Clear")

    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def insert_patients(self):
        def fetch_patient_names():
            self.database.connect()

            query = f"""
                SELECT
                    name
                FROM
                    patients
                WHERE
                    archived = 0
            """
            self.database.c.execute(query)

            patient_names = self.database.c.fetchall()

            self.database.disconnect()

            return patient_names
        
        self.ui.cmbbx_patient_name.clear()
        self.ui.cmbbx_patient_name.addItem("Add New")
        self.ui.cmbbx_patient_name.addItem("Select patient...")
        self.ui.cmbbx_patient_name.model().item(1).setEnabled(False)

        patient_names = fetch_patient_names()

        for patient_name in patient_names:
            self.ui.cmbbx_patient_name.addItem(patient_name[0])

        self.ui.cmbbx_patient_name.setCurrentIndex(1)

    def handle_add_patient(self, index):
        if index == 0:
            self.ui.cmbbx_patient_name.setCurrentIndex(1)
            dialog = PatientDialog(self)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.ui.cmbbx_patient_name.disconnect()
                self.insert_patients()
                self.ui.cmbbx_patient_name.currentIndexChanged.connect(self.handle_add_patient)
                self.ui.cmbbx_patient_name.setCurrentIndex(1)
            else:
                dialog.close()

    def insert_doctors(self):
        def fetch_doctor_names():
            self.database.connect()

            query = f"""
                SELECT
                    u.name
                FROM
                    users AS u
                JOIN
                    positions AS p
                ON
                    u.position_id = p.id
                WHERE
                    p.name <> "Receptionist"
                AND
                    p.name <> "Administrator"
                AND
                    u.archived = 0
            """
            self.database.c.execute(query)

            doctor_names = self.database.c.fetchall()

            self.database.disconnect()

            return doctor_names
        
        self.ui.cmbbx_doctor_name.clear()
        self.ui.cmbbx_doctor_name.addItem("Add New")
        self.ui.cmbbx_doctor_name.addItem("Select doctor...")
        self.ui.cmbbx_doctor_name.model().item(1).setEnabled(False)

        doctor_names = fetch_doctor_names()

        for doctor_name in doctor_names:
            self.ui.cmbbx_doctor_name.addItem(doctor_name[0])

        self.ui.cmbbx_doctor_name.setCurrentIndex(1)

    def handle_add_doctor(self, index):
        if index == 0:
            self.ui.cmbbx_doctor_name.setCurrentIndex(1)
            dialog = DoctorDialog(self)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.ui.cmbbx_doctor_name.disconnect()
                self.insert_doctors()
                self.ui.cmbbx_doctor_name.currentIndexChanged.connect(self.handle_add_doctor)
                self.ui.cmbbx_doctor_name.setCurrentIndex(1)
            else:
                dialog.close()

    def set_consultation_data(self):
        self.ui.cmbbx_patient_name.setCurrentText(self.patient_name)
        self.ui.cmbbx_doctor_name.setCurrentText(self.doctor_name)
    
    def handle_add_save(self):
        if self.ui.cmbbx_patient_name.currentText() != "Select patient..." and self.ui.cmbbx_doctor_name.currentText() != "Select doctor...":
            if self.purpose == "Add":
                self.insert_consultation_data()
            else:
                self.update_consultation_data()
            self.accept()

    def get_consultation_data(self):
        patient_name = self.ui.cmbbx_patient_name.currentText()
        doctor_name = self.ui.cmbbx_doctor_name.currentText()

        return patient_name, doctor_name
    
    def fetch_patient_id(self, patient_name):
        self.database.connect()

        query = f"""
            SELECT
                id
            FROM
                patients
            WHERE
                name = '{patient_name}'
        """
        self.database.c.execute(query)

        patient_id = self.database.c.fetchone()

        self.database.disconnect()

        return patient_id
    
    def fetch_doctor_id(self, doctor_name):
        self.database.connect()

        query = f"""
            SELECT
                id
            FROM
                users
            WHERE
                name = '{doctor_name}'
        """
        self.database.c.execute(query)

        doctor_id = self.database.c.fetchone()

        self.database.disconnect()

        return doctor_id
    
    def insert_consultation_data(self):
        patient_name, doctor_name = self.get_consultation_data()

        patient_id = self.fetch_patient_id(patient_name)[0]
        doctor_id = self.fetch_doctor_id(doctor_name)[0]

        self.database.connect()

        query = f"""
            INSERT INTO
                consultations (
                    patient_id,
                    doctor_id
                )
            VALUES (
                {patient_id},
                {doctor_id}
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()
    
    def update_consultation_data(self):
        patient_name, doctor_name = self.get_consultation_data()

        patient_id = self.fetch_patient_id(patient_name)[0]
        doctor_id = self.fetch_doctor_id(doctor_name)[0]

        self.database.connect()

        query = f"""
            UPDATE
                consultations
            SET
                patient_id = {patient_id},
                doctor_id = {doctor_id}
            WHERE
                id = {self.consultation_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        if self.purpose == "Add":
            self.ui.cmbbx_patient_name.setCurrentIndex(1)
            self.ui.cmbbx_doctor_name.setCurrentIndex(1)
        else:
            self.ui.cmbbx_patient_name.setCurrentText(self.patient_name)
            self.ui.cmbbx_doctor_name.setCurrentText(self.doctor_name)

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.cmbbx_patient_name.currentIndexChanged.connect(self.handle_add_patient)
        self.ui.cmbbx_doctor_name.currentIndexChanged.connect(self.handle_add_doctor)

        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
