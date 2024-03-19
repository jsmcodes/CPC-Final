from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from dev_functions.database_manager import DatabaseManager
from UI.main_payment_methods_ui import Ui_PaymentMethods
from main_payment_method_dialog import PaymentMethodDialog


class PaymentMethods(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_PaymentMethods()
        self.ui.setupUi(self)

        self.ui.tblwdgt_payment_methods.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

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
        def fetch_payment_method_data():
            self.database.connect()

            search_name = self.ui.lnedit_payment_method_name.text()

            query = f"""
                SELECT
                    id,
                    name
                FROM
                    payment_methods
                WHERE
                    name LIKE '%{search_name}%'
                AND
                    archived = {self.archived}
            """
            self.database.c.execute(query)

            method_datas = self.database.c.fetchall()

            self.database.disconnect()

            return method_datas
        
        self.ui.tblwdgt_payment_methods.setRowCount(0)
        
        method_datas = fetch_payment_method_data()

        if method_datas:
            for method_data in method_datas:
                id, name = method_data

                row = self.ui.tblwdgt_payment_methods.rowCount()
                self.ui.tblwdgt_payment_methods.insertRow(row)
                    
                self.ui.tblwdgt_payment_methods.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_payment_methods.setItem(row, 1, QTableWidgetItem(name))

                for col in range(self.ui.tblwdgt_payment_methods.columnCount()):
                    item = self.ui.tblwdgt_payment_methods.item(row, col)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)

    def handle_add(self):
        dialog = PaymentMethodDialog(self, "Add")
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        selected_item = self.ui.tblwdgt_payment_methods.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            method_id = self.ui.tblwdgt_payment_methods.item(selected_row, 0).text()
            method_name = self.ui.tblwdgt_payment_methods.item(selected_row, 1).text()
            self.ui.tblwdgt_payment_methods.setFocus()

            dialog = PaymentMethodDialog(self, "Edit", method_id, method_name)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_payment_methods.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            method_id = self.ui.tblwdgt_payment_methods.item(selected_row, 0).text()

            self.update_method_archived(method_id)
            self.populate_table()

    def update_method_archived(self, method_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE 
                payment_methods 
            SET
                archived = {archive}
            WHERE
                id = {method_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def connect_functions(self):
        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.lnedit_payment_method_name.textChanged.connect(self.populate_table)
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.tblwdgt_payment_methods.doubleClicked.connect(self.handle_edit)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()
