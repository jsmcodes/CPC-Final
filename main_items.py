from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from dev_functions.database_manager import DatabaseManager
from UI.main_items_ui import Ui_Items
from main_item_dialog import ItemDialog


class Items(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Items()
        self.ui.setupUi(self)

        self.ui.tblwdgt_items.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

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
        def fetch_item_data():
            self.database.connect()

            search_item_name = self.ui.lnedit_item_name.text()

            query = f"""
                SELECT
                    id,
                    name,
                    price
                FROM
                    items
                WHERE
                    name LIKE '%{search_item_name}%'
                AND
                    archived = {self.archived}
            """
            self.database.c.execute(query)

            item_datas = self.database.c.fetchall()

            self.database.disconnect()

            return item_datas
        
        self.ui.tblwdgt_items.setRowCount(0)
        
        item_datas = fetch_item_data()

        if not item_datas:
            return

        for item_data in item_datas:
            id, name, price = item_data

            row = self.ui.tblwdgt_items.rowCount()
            self.ui.tblwdgt_items.insertRow(row)
                
            self.ui.tblwdgt_items.setItem(row, 0, QTableWidgetItem(str(id)))
            self.ui.tblwdgt_items.setItem(row, 1, QTableWidgetItem(name))
            self.ui.tblwdgt_items.setItem(row, 2, QTableWidgetItem(str(price)))

            for col in range(self.ui.tblwdgt_items.columnCount()):
                item = self.ui.tblwdgt_items.item(row, col)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

    def handle_add(self):
        dialog = ItemDialog(self, "Add")
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        selected_item = self.ui.tblwdgt_items.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            item_id = self.ui.tblwdgt_items.item(selected_row, 0).text()
            item_name = self.ui.tblwdgt_items.item(selected_row, 1).text()
            item_price = self.ui.tblwdgt_items.item(selected_row, 2).text()
            self.ui.tblwdgt_items.setFocus()

            dialog = ItemDialog(self, "Edit", item_id, item_name, item_price)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_items.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            item_id = self.ui.tblwdgt_items.item(selected_row, 0).text()

            self.update_item_archived(item_id)
            self.populate_table()

    def update_item_archived(self, item_id) -> None:
        self.database.connect()

        archive = not self.archived

        query = f"""
            UPDATE 
                items 
            SET
                archived = {archive}
            WHERE
                id = {item_id}
        """

        self.database.c.execute(query)

        self.database.conn.commit()

        self.database.disconnect()

    def connect_functions(self):
        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.lnedit_item_name.textChanged.connect(self.populate_table)
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.tblwdgt_items.doubleClicked.connect(self.handle_edit)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()
