from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QKeyEvent

from datetime import datetime

from dev_functions.database_manager import DatabaseManager
from UI.main_patients_ui import Ui_Patients
from main_patient_dialog import PatientDialog
from main_dashboard_consultation_dialog import DoctorConsultationDialog


class Patients(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Patients()
        self.ui.setupUi(self)

        self.ui.tblwdgt_patients.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.connect_functions()

    def handle_archived_check(self, state) -> None:
        if state == Qt.Checked:
            self.archived = 1
            self.ui.pshbtn_archive.setText("Unarchive")
        else:
            self.archived = 0
            self.ui.pshbtn_archive.setText("Archive")
        self.populate_table()

    def fetch_patient_data(self):
        def get_patient_ids():
            user_id = self.parent.user_id

            query = f"""
                SELECT
                    patient_id
                FROM
                    consultations
                WHERE
                    doctor_id = {user_id}
                ORDER BY
                    patient_id ASC
            """
            self.database.c.execute(query)

            patient_ids = self.database.c.fetchall()

            return patient_ids

        user_position = self.parent.user_position

        self.database.connect()

        search_patient_name = self.ui.lnedit_name.text()
        patients_data = []

        if user_position == "Administrator" or user_position == "Receptionist":
            query = f"""
                SELECT
                    id,
                    name,
                    sex,
                    birthdate
                FROM
                    patients
                WHERE
                    name LIKE '%{search_patient_name}%'
                AND
                    archived = {self.archived}
                ORDER BY
                    id ASC
            """
            self.database.c.execute(query)

            patients_data = self.database.c.fetchall()
        else:
            patient_ids = get_patient_ids()

            for patient_id in patient_ids:
                patient_id = patient_id[0]

                query = f"""
                    SELECT
                        id,
                        name,
                        sex,
                        birthdate
                    FROM
                        patients
                    WHERE
                        name LIKE '%{search_patient_name}%'
                    AND
                        id = {patient_id}
                    AND
                        archived = {self.archived}
                    ORDER BY
                        id ASC
                """
                self.database.c.execute(query)

                patient_data = self.database.c.fetchone()
                patients_data.append(patient_data)

        self.database.disconnect()

        return patients_data

    def populate_table(self) -> None:
        def calculate_age(birthdate):
            current_date = datetime.now()
            birthdate_str = birthdate.strftime("%Y-%m-%d")
            birthdate = QDate.fromString(birthdate_str, "yyyy-MM-dd")

            age_years = current_date.year - birthdate.year()
            age_months = current_date.month - birthdate.month()
            age_days = current_date.day - birthdate.day()

            if age_days < 0:
                age_months -= 1
                days_in_prev_month = (current_date.replace(month=current_date.month - 1) - current_date.replace(day=1)).days
                age_days += days_in_prev_month

            if age_months < 0:
                age_years -= 1
                age_months += 12

            return f"{age_years}y {age_months}m"
        
        self.ui.tblwdgt_patients.setRowCount(0)
        patients = self.fetch_patient_data()
        try:
            for patient in patients:
                id, name, sex, birthdate = patient
                age = calculate_age(birthdate)

                row = self.ui.tblwdgt_patients.rowCount()
                self.ui.tblwdgt_patients.insertRow(row)
                
                self.ui.tblwdgt_patients.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_patients.setItem(row, 1, QTableWidgetItem(name))
                self.ui.tblwdgt_patients.setItem(row, 2, QTableWidgetItem(sex))
                self.ui.tblwdgt_patients.setItem(row, 3, QTableWidgetItem(age))

                for col in range(self.ui.tblwdgt_patients.columnCount()):
                    item = self.ui.tblwdgt_patients.item(row, col)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)
        except Exception as e:
            self.ui.tblwdgt_patients.setRowCount(0)
            print(f"Error in populate_table: {e}")

    def handle_add(self):
        dialog = PatientDialog(self)
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_view(self, item):
        selected_row = item.row()
        patient_id = self.ui.tblwdgt_patients.item(selected_row, 0).text()
        user_position = self.parent.user_position
        self.ui.tblwdgt_patients.setFocus()

        if user_position == "Receptionist":
            dialog = PatientDialog(self, True, patient_id)
        elif user_position == "Administrator":
            dialog = DoctorConsultationDialog(self, "View", patient_id)
        else:
            dialog = DoctorConsultationDialog(self, "View", patient_id)

        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        selected_item = self.ui.tblwdgt_patients.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            patient_id = self.ui.tblwdgt_patients.item(selected_row, 0).text()
            user_position = self.parent.user_position
            self.ui.tblwdgt_patients.setFocus()

            if user_position == "Receptionist":
                dialog = PatientDialog(self, True, patient_id)
            elif user_position == "Administrator":
                dialog = DoctorConsultationDialog(self, "Edit", patient_id)
            else:
                dialog = DoctorConsultationDialog(self, "View", patient_id)

            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_patients.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            patient_id = self.ui.tblwdgt_patients.item(selected_row, 0).text()

            self.update_patient_archived(patient_id)
            self.populate_table()

    def update_patient_archived(self, patient_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE patients 
            SET
                archived = {archive}
            WHERE
                id = {patient_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def set_ui_for_doctors(self):
        self.ui.wdgt_page_buttons.hide()

    def reset_ui(self):
        self.ui.wdgt_page_buttons.show()

    def connect_functions(self):
        self.ui.tblwdgt_patients.doubleClicked.connect(self.handle_view)

        self.ui.chkbox_archived.stateChanged.connect(self.handle_archived_check)

        self.ui.lnedit_name.textChanged.connect(self.populate_table)
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()
