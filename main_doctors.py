from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from dev_functions.database_manager import DatabaseManager
from UI.main_doctors_ui import Ui_Doctors
from main_doctor_dialog import DoctorDialog


class Doctors(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Doctors()
        self.ui.setupUi(self)

        self.ui.tblwdgt_doctors.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tblwdgt_doctors.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.connect_functions()

    def handle_archived_check(self, state) -> None:
        if state == Qt.Checked:
            self.archived = 1
            self.ui.pshbtn_archive.setText("Unarchive")
        else:
            self.archived = 0
            self.ui.pshbtn_archive.setText("Archive")
        self.populate_table()

    def populate_table(self):
        def fetch_doctor_data():
            self.database.connect()

            searched_doctor_name = self.ui.lnedit_name.text()
            searched_doctor_position = self.ui.lnedit_position.text()
            user_position = self.parent.user_position

            if user_position == "Receptionist":
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
                        u.name LIKE '%{searched_doctor_name}%'
                    AND
                        p.name LIKE '%{searched_doctor_position}%'
                    AND
                        p.name <> 'Administrator'
                    AND
                        p.name <> 'Receptionist'
                    AND
                        u.archived = {self.archived}
                """
            else:
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
                        u.name LIKE '%{searched_doctor_name}%'
                    AND
                        p.name LIKE '%{searched_doctor_position}%'
                    AND
                        u.archived = {self.archived}
                """

            self.database.c.execute(query)

            doctor_datas = self.database.c.fetchall()

            self.database.disconnect()

            return doctor_datas
        
        self.ui.tblwdgt_doctors.setRowCount(0)
        
        doctor_datas = fetch_doctor_data()

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

    def handle_clear_filter(self):
        self.ui.chkbx_archived.setChecked(False)
        self.ui.lnedit_name.clear()
        self.ui.lnedit_position.clear()

    def set_ui_for_receptionist(self):
        self.ui.wdgt_page_buttons.hide()

    def reset_ui(self):
        self.ui.wdgt_page_buttons.show()

    def handle_add(self):
        dialog = DoctorDialog(self)
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        user_position = self.parent.user_position
        if user_position == "Administrator":
            selected_item = self.ui.tblwdgt_doctors.selectedItems()

            if selected_item:
                selected_row = selected_item[0].row()
                doctor_id = self.ui.tblwdgt_doctors.item(selected_row, 0).text()
                self.ui.tblwdgt_doctors.setFocus()

                dialog = DoctorDialog(self, True, doctor_id)
                result = dialog.exec_()

                if result == dialog.Accepted:
                    self.populate_table()
                else:
                    dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_doctors.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            doctor_id = self.ui.tblwdgt_doctors.item(selected_row, 0).text()

            self.update_doctor_archived(doctor_id)
            self.populate_table()

    def update_doctor_archived(self, doctor_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE
                users 
            SET
                archived = {archive}
            WHERE
                id = {doctor_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def connect_functions(self):
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.lnedit_name.textChanged.connect(self.populate_table)
        self.ui.lnedit_position.textChanged.connect(self.populate_table)
        self.ui.pshbtn_clear.clicked.connect(self.handle_clear_filter)

        self.ui.tblwdgt_doctors.doubleClicked.connect(self.handle_edit)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()