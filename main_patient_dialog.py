from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QDate

from dev_functions.database_manager import DatabaseManager
from UI.main_patient_dialog_ui import Ui_PatientDialog


class PatientDialog(QDialog):
    def __init__(self, parent: QWidget, edit: bool=False, patient_id: int=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.edit = edit
        self.patient_id = patient_id
        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_PatientDialog()
        self.ui.setupUi(self)

        self.ui.cmbx_sex.lineEdit().setAlignment(Qt.AlignCenter)

        self.ui.dtedit_birthdate.setMaximumDate(QDate.currentDate())

        self.ui.tblwdgt_doctors.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tblwdgt_doctors.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        if self.edit:
            self.set_patient_data()
            self.popuplate_table()
        else:
            self.set_patient_id()

            self.ui.dtedit_birthdate.setDate(QDate.currentDate())

            self.ui.lbl_doctors.hide()
            self.ui.tblwdgt_doctors.hide()

            self.ui.pshbtn_add_save.setText("Add")
            self.ui.pshbtn_clear_reset.setText("Clear")

        self.connect_functions()

    def set_patient_id(self):
        self.database.connect()

        query = """
            SELECT
                MAX(id)
            FROM
                patients
        """
        self.database.c.execute(query)

        last_patient_id = self.database.c.fetchone()

        self.database.disconnect()
        
        self.patient_id = last_patient_id[0] + 1
        self.ui.lbl_id.setText(f"Patient #{self.patient_id}")

    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def fetch_patient_data(self):
        self.database.connect()

        query = f"""
            SELECT
                name,
                sex,
                birthdate,
                contact_number,
                address
            FROM
                patients
            WHERE
                id = {self.patient_id}
        """
        self.database.c.execute(query)

        patient_data = self.database.c.fetchone()

        self.database.disconnect()

        return patient_data

    def set_patient_data(self):
        name, sex, birthdate, contact_number, address = self.fetch_patient_data()

        self.ui.lbl_id.setText(f"Patient #{self.patient_id}")
        self.ui.lnedit_name.setText(name)
        self.ui.cmbx_sex.setCurrentText(sex)
        self.ui.dtedit_birthdate.setDate(birthdate)
        self.ui.lnedit_contact_number.setText(contact_number)
        self.ui.txtedit_address.setText(address)

    def fetch_doctor_id(self):
        self.database.connect()

        query = f"""
            SELECT
                doctor_id
            FROM
                consultations
            WHERE
                patient_id = {self.patient_id}
            AND
                archived = 0
        """
        self.database.c.execute(query)

        doctor_ids = self.database.c.fetchall()

        self.database.disconnect()

        return doctor_ids

    def fetch_doctor_data(self):
        doctor_ids = self.fetch_doctor_id()

        self.database.connect()

        doctor_datas = []
        for doctor_id in doctor_ids:
            query = f"""
                SELECT
                    u.id,
                    u.name AS doctor_name,
                    p.name AS position_name
                FROM
                    users AS u
                JOIN
                    positions AS p
                ON
                    u.position_id = p.id
                WHERE
                    u.id = {doctor_id[0]}
            """
            self.database.c.execute(query)

            doctor_data = self.database.c.fetchone()
            doctor_datas.append(doctor_data)

        self.database.disconnect()

        return doctor_datas

    def popuplate_table(self):
        self.ui.tblwdgt_doctors.setRowCount(0)

        doctor_datas = self.fetch_doctor_data()

        if doctor_datas:
            for doctor_data in doctor_datas:
                id, name, position = doctor_data

                row = self.ui.tblwdgt_doctors.rowCount()
                self.ui.tblwdgt_doctors.insertRow(row)
                
                self.ui.tblwdgt_doctors.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_doctors.setItem(row, 1, QTableWidgetItem(name))
                self.ui.tblwdgt_doctors.setItem(row, 2, QTableWidgetItem(position))

                for col in range(self.ui.tblwdgt_doctors.columnCount()):
                    item = self.ui.tblwdgt_doctors.item(row, col)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)

    def get_patient_data(self) -> list:
        name = self.ui.lnedit_name.text().strip()
        sex = self.ui.cmbx_sex.currentText()
        birthdate = self.ui.dtedit_birthdate.date().toPyDate()
        contact_number = self.ui.lnedit_contact_number.text().strip()
        address = self.ui.txtedit_address.toPlainText().strip()

        return name, sex, birthdate, contact_number, address
    
    def handle_add_save(self):
        self.ui.pshbtn_add_save.setFocus()
        name, sex, birthdate, contact_number, address = self.get_patient_data()

        if name and contact_number and address:
            patient_data = name, sex, birthdate, contact_number, address
            if self.edit:
                self.update_patient_data(patient_data)
            else:
                self.insert_patient_data(patient_data)
            self.accept()

    def update_patient_data(self, patient_data: list):
        name, sex, birthdate, contact_number, address = patient_data

        self.database.connect()

        query = f"""
            UPDATE
                patients
            SET
                name = '{name}',
                sex = '{sex}',
                birthdate = '{birthdate}',
                contact_number = '{contact_number}',
                address = '{address}'
            WHERE
                id = {self.patient_id}
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def insert_patient_data(self, patient_data: list):
        name, sex, birthdate, contact_number, address = patient_data

        self.database.connect()

        query = f"""
            INSERT INTO
                patients (
                    name,
                    sex,
                    birthdate,
                    contact_number,
                    address
                )
            VALUES (
                '{name}',
                '{sex}',
                '{birthdate}',
                '{contact_number}',
                '{address}'
            )
        """
        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def handle_clear_reset(self):
        def clear_inputs():
            self.ui.lnedit_name.clear()
            self.ui.cmbx_sex.setCurrentText("Female")
            self.ui.dtedit_birthdate.setDate(QDate.currentDate())
            self.ui.lnedit_contact_number.clear()
            self.ui.txtedit_address.clear()

        if self.edit:
            self.set_patient_data()
        else:
            clear_inputs()

    def handle_cancel(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_add_save.clicked.connect(self.handle_add_save)
        self.ui.pshbtn_clear_reset.clicked.connect(self.handle_clear_reset)
        self.ui.pshbtn_cancel.clicked.connect(self.handle_cancel)
