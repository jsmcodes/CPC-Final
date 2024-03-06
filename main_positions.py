from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from dev_functions.database_manager import DatabaseManager
from UI.main_positions_ui import Ui_Positions
from main_position_dialog import PositionDialog


class Positions(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Positions()
        self.ui.setupUi(self)

        self.ui.tblwdgt_positions.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

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
        def fetch_position_data():
            self.database.connect()

            search_position_name = self.ui.lnedit_name.text()

            query = f"""
                SELECT
                    id,
                    name
                FROM
                    positions
                WHERE
                    name LIKE '%{search_position_name}%'
                AND
                    archived = {self.archived}
            """
            self.database.c.execute(query)

            position_datas = self.database.c.fetchall()

            self.database.disconnect()

            return position_datas
        
        self.ui.tblwdgt_positions.setRowCount(0)
        
        position_datas = fetch_position_data()

        for position_data in position_datas:
            id, name = position_data

            row = self.ui.tblwdgt_positions.rowCount()
            self.ui.tblwdgt_positions.insertRow(row)
                
            self.ui.tblwdgt_positions.setItem(row, 0, QTableWidgetItem(str(id)))
            self.ui.tblwdgt_positions.setItem(row, 1, QTableWidgetItem(name))

            for col in range(self.ui.tblwdgt_positions.columnCount()):
                item = self.ui.tblwdgt_positions.item(row, col)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

    def handle_add(self):
        dialog = PositionDialog(self)
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        selected_item = self.ui.tblwdgt_positions.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            position_id = self.ui.tblwdgt_positions.item(selected_row, 0).text()
            position_name = self.ui.tblwdgt_positions.item(selected_row, 1).text()
            self.ui.tblwdgt_positions.setFocus()

            dialog = PositionDialog(self, True, position_id, position_name)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_positions.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            position_id = self.ui.tblwdgt_positions.item(selected_row, 0).text()

            self.update_position_archived(position_id)
            self.populate_table()

    def update_position_archived(self, position_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE 
                positions 
            SET
                archived = {archive}
            WHERE
                id = {position_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def connect_functions(self):
        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.lnedit_name.textChanged.connect(self.populate_table)
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.tblwdgt_positions.doubleClicked.connect(self.handle_edit)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()
