from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QTreeWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from datetime import datetime

from dev_functions.database_manager import DatabaseManager
from UI.main_dashboard_ui import Ui_Dashboard
from main_consultation_dialog import ConsultationDialog
from main_dashboard_consultation_dialog import DoctorConsultationDialog


class Dashboard(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        
        self.ui.trwdgt_dashboard.header().setSectionResizeMode(0, QHeaderView.Stretch)

        self.ui.tblwdgt_dashboard.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.connect_functions()

    def set_ui_for_receptionists(self):
        self.ui.tblwdgt_dashboard.hide()
        self.ui.pshbtn_start_consultation.hide()

    def set_ui_for_doctors(self):
        self.ui.trwdgt_dashboard.hide()
        self.ui.pshbtn_new_consultation.hide()

    def set_ui_for_administrators(self):
        self.ui.tblwdgt_dashboard.hide()
        self.ui.pshbtn_start_consultation.hide()

    def reset_ui(self):
        self.ui.trwdgt_dashboard.show()
        self.ui.tblwdgt_dashboard.show()
        self.ui.pshbtn_start_consultation.show()
        self.ui.pshbtn_new_consultation.show()

    def populate_tree(self):
        def fetch_doctors():
            self.database.connect()

            query = """
                SELECT
                    u.name AS doctor_name,
                    p.name AS position_name
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
                ORDER BY
                    u.name ASC
            """
            self.database.c.execute(query)

            doctors = self.database.c.fetchall()

            self.database.disconnect()

            return doctors
        
        def fetch_patients_for_doctor(doctor_name):
            self.database.connect()

            get_doctor_id = f"""
                SELECT
                    id
                FROM
                    users
                WHERE
                    name = '{doctor_name}'
            """
            self.database.c.execute(get_doctor_id)
            doctor_id = self.database.c.fetchone()

            query = f"""
                SELECT
                    p.name,
                    c.status
                FROM
                    consultations AS c
                JOIN
                    patients AS p
                ON
                    c.patient_id = p.id
                WHERE
                    c.doctor_id = {doctor_id[0]}
                AND
                    c.status <> 'Done'
                AND
                    c.archived = 0
                ORDER BY
                    c.id ASC
            """
            self.database.c.execute(query)
            patients = self.database.c.fetchall()

            self.database.disconnect()

            return patients
        
        def add_tree_item(name, status, parent=None):
            item = QTreeWidgetItem(parent)
            item.setText(0, name)
            item.setText(1, status)

            if parent is None:
                self.ui.trwdgt_dashboard.addTopLevelItem(item)
                item.setExpanded(True)
                item.setBackground(0, QColor(200, 220, 255))
                item.setBackground(1, QColor(200, 220, 255))
            else:
                item.setTextAlignment(0, Qt.AlignCenter)
                item.setTextAlignment(1, Qt.AlignCenter)

            return item

        doctors = fetch_doctors()

        self.ui.trwdgt_dashboard.clear()
        self.ui.trwdgt_dashboard.setRootIsDecorated(False)
        self.ui.trwdgt_dashboard.setStyleSheet(
            """
                QTreeWidget::item { 
                    padding: 10px;
                }
            """
        )

        for doctor in doctors:
            doctor_name, position_name = doctor

            doctor_item = add_tree_item(doctor_name, position_name)

            patients = fetch_patients_for_doctor(doctor_name)

            for patient in patients:
                patient_name, status = patient

                add_tree_item(patient_name, status, doctor_item)

    def populate_table(self):
        def fetch_consultations():
            self.database.connect()

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
                    c.doctor_id = {doctor_id}
                AND
                    c.status <> 'Done'
                AND
                    c.archived = 0
                ORDER BY
                    c.id ASC
            """
            self.database.c.execute(query)

            consultations = self.database.c.fetchall()

            self.database.disconnect()

            return consultations
        
        consultations = fetch_consultations()

        self.ui.tblwdgt_dashboard.setRowCount(0)
    
        for consultation in consultations:
            consultation_id, patient_name, status = consultation

            row = self.ui.tblwdgt_dashboard.rowCount()
            self.ui.tblwdgt_dashboard.insertRow(row)
                
            self.ui.tblwdgt_dashboard.setItem(row, 0, QTableWidgetItem(str(consultation_id)))
            self.ui.tblwdgt_dashboard.setItem(row, 1, QTableWidgetItem(patient_name))
            self.ui.tblwdgt_dashboard.setItem(row, 2, QTableWidgetItem(status))

            for col in range(self.ui.tblwdgt_dashboard.columnCount()):
                item = self.ui.tblwdgt_dashboard.item(row, col)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

    def handle_new_consultation(self):
        user_position = self.parent.user_position

        if user_position == "Receptionist" or user_position == "Administrator":
            dialog = ConsultationDialog(self, "Add")
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_tree()
            else:
                dialog.close()

    def handle_start_consultation(self):
        def check_for_ongoing_consultation():
            rows = self.ui.tblwdgt_dashboard.rowCount()
            ongoing = False
            row_id = None

            for row in range(rows):
                status = self.ui.tblwdgt_dashboard.item(row, 2).text()

                if status == "Ongoing":
                    ongoing = True
                    row_id = row

            return ongoing, row_id

        def consultation_started(consultation_id: int):
            self.database.connect()

            query = f"""
                UPDATE
                    consultations
                SET
                    status = 'Ongoing'
                WHERE
                    id = {consultation_id}
            """
            self.database.c.execute(query)

            self.database.conn.commit()

            self.database.disconnect()
            
        def fetch_patient_id(patient_name: str):
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
        
        selected_items = self.ui.tblwdgt_dashboard.selectedItems()
        self.ui.tblwdgt_dashboard.selectRow(0)

        row = self.ui.tblwdgt_dashboard.rowCount()

        if row == 0:
            return

        if row > 0:
            ongoing, row_id = check_for_ongoing_consultation()

            if not ongoing:
                if selected_items:
                    selected_row = selected_items[0].row()
                    consultation_id = self.ui.tblwdgt_dashboard.item(selected_row, 0).text()
                    patient_name = self.ui.tblwdgt_dashboard.item(selected_row, 1).text()
                else:
                    consultation_id = self.ui.tblwdgt_dashboard.item(0, 0).text()
                    patient_name = self.ui.tblwdgt_dashboard.item(0, 1).text()
            else:
                consultation_id = self.ui.tblwdgt_dashboard.item(row_id, 0).text()
                patient_name = self.ui.tblwdgt_dashboard.item(row_id, 1).text()

        patient_id = fetch_patient_id(patient_name)[0]

        consultation_started(consultation_id)
        self.populate_table()
        dialog = DoctorConsultationDialog(self, "Add", patient_id, consultation_id)
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def connect_functions(self):
        self.ui.pshbtn_start_consultation.clicked.connect(self.handle_start_consultation)
        self.ui.pshbtn_new_consultation.clicked.connect(self.handle_new_consultation)
