from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QKeyEvent

from dev_functions.database_manager import DatabaseManager
from UI.main_sales_ui import Ui_Sales
from main_sale_dialog import SaleDialog


class Sales(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.parent = parent
        self.database = DatabaseManager()
        self.archived = 0
        self.on_date = False
        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_Sales()
        self.ui.setupUi(self)

        self.ui.tblwdgt_sales.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tblwdgt_sales.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.connect_functions()

    def handle_archived_check(self, state) -> None:
        if state == Qt.Checked:
            self.archived = 1
            self.ui.pshbtn_archive.setText("Unarchive")
        else:
            self.archived = 0
            self.ui.pshbtn_archive.setText("Archive")
        self.populate_table()

    def handle_date_check(self, state) -> None:
        if state == Qt.Checked:
            self.on_date = True
            self.ui.dtedit_sales_date.setEnabled(True)
        else:
            self.on_date = False
            self.ui.dtedit_sales_date.setEnabled(False)
        self.populate_table()

    def handle_clear(self):
        self.ui.dtedit_sales_date.setDate(QDate.currentDate())
        self.ui.lnedit_patient_name.clear()
        self.ui.lnedit_receptionist_name.clear()

    def populate_table(self):
        def fetch_sale_data():
            self.database.connect()

            search_patient_name = self.ui.lnedit_patient_name.text()
            search_receptionist_name = self.ui.lnedit_receptionist_name.text()
            search_sale_date = self.ui.dtedit_sales_date.date().toString("yyyy-MM-dd")

            if self.on_date:
                sale_date_condition = f"""
                                        AND
                                            s.sale_date = '{search_sale_date}'
                                    """
            else:
                sale_date_condition = ""

            query = f"""
                SELECT
                    s.id,
                    s.sale_date,
                    p.name AS patient_name,
                    u.name AS user_name,
                    s.total_price
                FROM
                    sales AS s
                JOIN
                    patients AS p
                ON
                    s.patient_id = p.id
                JOIN
                    users AS u
                ON
                    s.user_id = u.id
                WHERE
                    p.name LIKE '%{search_patient_name}%'
                AND
                    u.name LIKE '%{search_receptionist_name}%'
                {sale_date_condition}
                AND
                    s.archived = {self.archived}
            """
            self.database.c.execute(query)

            sale_datas = self.database.c.fetchall()

            self.database.disconnect()

            return sale_datas
        
        self.ui.tblwdgt_sales.setRowCount(0)
        
        sale_datas = fetch_sale_data()

        if sale_datas:
            for sale_data in sale_datas:
                id, sale_date, patient_name, user_name, total_price = sale_data

                row = self.ui.tblwdgt_sales.rowCount()
                self.ui.tblwdgt_sales.insertRow(row)
                    
                self.ui.tblwdgt_sales.setItem(row, 0, QTableWidgetItem(str(id)))
                self.ui.tblwdgt_sales.setItem(row, 1, QTableWidgetItem(sale_date))
                self.ui.tblwdgt_sales.setItem(row, 2, QTableWidgetItem(patient_name))
                self.ui.tblwdgt_sales.setItem(row, 3, QTableWidgetItem(user_name))
                self.ui.tblwdgt_sales.setItem(row, 4, QTableWidgetItem(total_price))

                for col in range(self.ui.tblwdgt_sales.columnCount()):
                    item = self.ui.tblwdgt_sales.item(row, col)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)

    def handle_add(self):
        user_name = self.parent.user_name
        
        dialog = SaleDialog(self, "Add", user_name)
        result = dialog.exec_()

        if result == dialog.Accepted:
            self.populate_table()
        else:
            dialog.close()

    def handle_edit(self):
        selected_item = self.ui.tblwdgt_sales.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            service_id = self.ui.tblwdgt_sales.item(selected_row, 0).text()
            service_name = self.ui.tblwdgt_sales.item(selected_row, 1).text()
            service_price = self.ui.tblwdgt_sales.item(selected_row, 2).text()
            self.ui.tblwdgt_sales.setFocus()

            dialog = SaleDialog(self, "Edit", service_id, service_name, service_price)
            result = dialog.exec_()

            if result == dialog.Accepted:
                self.populate_table()
            else:
                dialog.close()

    def handle_archive(self) -> None:
        selected_item = self.ui.tblwdgt_sales.selectedItems()

        if selected_item:
            selected_row = selected_item[0].row()
            service_id = self.ui.tblwdgt_sales.item(selected_row, 0).text()

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
        self.ui.pshbtn_refresh.clicked.connect(self.populate_table)

        self.ui.chkbx_archived.stateChanged.connect(self.handle_archived_check)
        self.ui.chkbx_sales_date.stateChanged.connect(self.handle_date_check)
        self.ui.dtedit_sales_date.dateChanged.connect(self.populate_table)
        self.ui.lnedit_patient_name.textChanged.connect(self.populate_table)
        self.ui.lnedit_receptionist_name.textChanged.connect(self.populate_table)
        self.ui.pshbtn_clear.clicked.connect(self.handle_clear)

        self.ui.tblwdgt_sales.doubleClicked.connect(self.handle_edit)

        self.ui.pshbtn_add.clicked.connect(self.handle_add)
        self.ui.pshbtn_edit.clicked.connect(self.handle_edit)
        self.ui.pshbtn_archive.clicked.connect(self.handle_archive)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_edit()
