from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from dev_functions.database_manager import DatabaseManager
from UI.main_services_ui import Ui_Services
from main_services_dialog import ServiceDialog


class Services(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Services()
        self.ui.setupUi(self)

        self.ui.tblwdgt_services.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

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
        def fetch_service_data():
            self.database.connect()

            search_service_name = self.ui.lnedit_name.text()

            query = f"""
                SELECT
                    id,
                    name,
                    price
                FROM
                    services
                WHERE
                    name LIKE '%{search_service_name}%'
                AND
                    archived = {self.archived}
            """
            self.database.c.execute(query)

            position_datas = self.database.c.fetchall()

            self.database.disconnect()

            return position_datas
        
        self.ui.tblwdgt_services.setRowCount(0)
        
        service_datas = fetch_service_data()

        if service_datas:
            for service_data in service_datas:
                id, name, price = service_data

                row = self.ui.tblwdgt_services.rowCount()
                self.ui.tblwdgt_services.insertRow(row)
                    
                self.ui.tblwdgt_services.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_services.setItem(row, 1, QTableWidgetItem(name))
                self.ui.tblwdgt_services.setItem(row, 2, QTableWidgetItem(str(price)))

                for col in range(self.ui.tblwdgt_services.columnCount()):
                    item = self.ui.tblwdgt_services.item(row, col)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)

    def handle_add(self):
        dialog = ServiceDialog(self, "Add")
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        selected_item = self.ui.tblwdgt_services.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            service_id = self.ui.tblwdgt_services.item(selected_row, 0).text()
            service_name = self.ui.tblwdgt_services.item(selected_row, 1).text()
            service_price = self.ui.tblwdgt_services.item(selected_row, 2).text()
            self.ui.tblwdgt_services.setFocus()

            dialog = ServiceDialog(self, "Edit", service_id, service_name, service_price)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_services.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            service_id = self.ui.tblwdgt_services.item(selected_row, 0).text()

            self.update_service_archived(service_id)
            self.populate_table()

    def update_service_archived(self, service_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE 
                services 
            SET
                archived = {archive}
            WHERE
                id = {service_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def connect_functions(self):
        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.lnedit_name.textChanged.connect(self.populate_table)
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.tblwdgt_services.doubleClicked.connect(self.handle_edit)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()
