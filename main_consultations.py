from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QKeyEvent

from datetime import datetime

from dev_functions.database_manager import DatabaseManager
from UI.main_consultations_ui import Ui_Consultations
from main_consultation_dialog import ConsultationDialog
from main_dashboard_consultation_dialog import DoctorConsultationDialog


class Consultations(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Consultations()
        self.ui.setupUi(self)

        self.ui.cmbbx_status.lineEdit().setAlignment(Qt.AlignCenter)

        self.connect_functions()

    def handle_archived_check(self, state) -> None:
        if state == Qt.Checked:
            self.archived = 1
            self.ui.pshbtn_archive.setText("Unarchive")
        else:
            self.archived = 0
            self.ui.pshbtn_archive.setText("Archive")
        self.populate_table()

    def handle_clear(self):
        self.ui.chkbx_archived.setChecked(False)
        self.ui.lnedit_patient_name.clear()
        self.ui.lnedit_doctor_name.clear()
        self.ui.cmbbx_status.setCurrentText("All")

    def populate_table(self):
        def fetch_consultation_data():
            self.database.connect()

            user_position = self.parent.user_position
            searched_patient_name = self.ui.lnedit_patient_name.text()
            searched_doctor_name = self.ui.lnedit_doctor_name.text()
            searched_status = self.ui.cmbbx_status.currentText()
            if searched_status == "All":
                searched_status = ""

            if user_position == "Receptionist" or user_position == "Administrator":
                query = f"""
                    SELECT
                        c.id,
                        p.name AS patient_name,
                        u.name AS doctor_name,
                        c.status
                    FROM
                        consultations AS c
                    JOIN
                        patients AS p
                    ON
                        c.patient_id = p.id
                    JOIN
                        users AS u
                    ON
                        c.doctor_id = u.id
                    WHERE
                        p.name LIKE '%{searched_patient_name}%'
                    AND
                        u.name LIKE '%{searched_doctor_name}%'
                    AND
                        c.status LIKE '%{searched_status}%'
                    AND
                        c.archived = {self.archived}
                    ORDER BY
                        c.id DESC
                """
            else:
                doctor_id = self.parent.user_id
                query = f"""
                    SELECT
                        c.id,
                        p.name,
                        c.status
                    FROM
                        consultations AS c
                    JOIN
                        patients AS p
                    ON
                        c.patient_id = p.id
                    WHERE
                        p.name LIKE '%{searched_patient_name}%'
                    AND
                        c.doctor_id = {doctor_id}
                    AND
                        c.status LIKE '%{searched_status}%'
                    AND
                        c.archived = {self.archived}
                    ORDER BY
                        c.id DESC
                """
            self.database.c.execute(query)

            consultation_datas = self.database.c.fetchall()

            self.database.disconnect()

            return consultation_datas

        self.ui.tblwdgt_consultations.setRowCount(0)

        consultation_datas = fetch_consultation_data()
        user_position = self.parent.user_position

        if not consultation_datas:
            return
        
        for consultation_data in consultation_datas:
            row = self.ui.tblwdgt_consultations.rowCount()
            self.ui.tblwdgt_consultations.insertRow(row)

            if user_position == "Receptionist" or user_position == "Administrator":
                id, patient_name, doctor_name, status = consultation_data
                
                self.ui.tblwdgt_consultations.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_consultations.setItem(row, 1, QTableWidgetItem(patient_name))

                self.ui.tblwdgt_consultations.setColumnCount(4)
                self.ui.tblwdgt_consultations.setHorizontalHeaderItem(2, QTableWidgetItem("Doctor"))
                self.ui.tblwdgt_consultations.setHorizontalHeaderItem(3, QTableWidgetItem("Status"))
                self.ui.tblwdgt_consultations.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
                self.ui.tblwdgt_consultations.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

                self.ui.tblwdgt_consultations.setItem(row, 2, QTableWidgetItem(doctor_name))
                self.ui.tblwdgt_consultations.setItem(row, 3, QTableWidgetItem(status))
            else:
                id, patient_name, status = consultation_data

                self.ui.tblwdgt_consultations.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_consultations.setItem(row, 1, QTableWidgetItem(patient_name))
                self.ui.tblwdgt_consultations.setItem(row, 2, QTableWidgetItem(status))
                self.ui.tblwdgt_consultations.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

            for col in range(self.ui.tblwdgt_consultations.columnCount()):
                item = self.ui.tblwdgt_consultations.item(row, col)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

    def handle_view(self, item):
        selected_row = item.row()
        consultation_id = self.ui.tblwdgt_consultations.item(selected_row, 0).text()
        user_position = self.parent.user_position
        self.ui.tblwdgt_consultations.setFocus()

        if user_position == "Receptionist":
            patient_name = self.ui.tblwdgt_consultations.item(selected_row, 1).text()
            doctor_name = self.ui.tblwdgt_consultations.item(selected_row, 2).text()
            dialog = ConsultationDialog(self, "Edit", consultation_id, user_position, patient_name, doctor_name)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()
        else:
            dialog = DoctorConsultationDialog(self, "View", None, consultation_id)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_add(self):
        user_position = self.parent.user_position
        self.ui.tblwdgt_consultations.setFocus()

        if user_position == "Receptionist" or user_position == "Administrator":
            dialog = ConsultationDialog(self, "Add")
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_consultations.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            consultation_id = self.ui.tblwdgt_consultations.item(selected_row, 0).text()

            self.update_consultation_archived(consultation_id)
            self.populate_table()

    def update_consultation_archived(self, consultation_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE 
                consultations 
            SET
                archived = {archive}
            WHERE
                id = {consultation_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def set_ui_for_doctors(self):
        self.ui.lnedit_doctor_name.hide()
        self.ui.wdgt_page_buttons.hide()

    def reset_ui(self):
        self.ui.wdgt_page_buttons.show()
        self.ui.lnedit_doctor_name.show()

    def connect_functions(self):
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.lnedit_patient_name.textChanged.connect(self.populate_table)
        self.ui.lnedit_doctor_name.textChanged.connect(self.populate_table)
        self.ui.cmbbx_status.currentTextChanged.connect(self.populate_table)
        self.ui.pshbtn_clear.clicked.connect(self.handle_clear)

        self.ui.tblwdgt_consultations.doubleClicked.connect(self.handle_view)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        # self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)