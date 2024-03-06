# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_orders_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sales(object):
    def setupUi(self, Sales):
        Sales.setObjectName("Sales")
        Sales.resize(1039, 828)
        self.main_layout = QtWidgets.QVBoxLayout(Sales)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.hlo_refresh = QtWidgets.QHBoxLayout()
        self.hlo_refresh.setSpacing(10)
        self.hlo_refresh.setObjectName("hlo_refresh")
        self.lbl_search_filter = QtWidgets.QLabel(Sales)
        self.lbl_search_filter.setObjectName("lbl_search_filter")
        self.hlo_refresh.addWidget(self.lbl_search_filter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlo_refresh.addItem(spacerItem)
        self.pshbtn_refresh = QtWidgets.QPushButton(Sales)
        self.pshbtn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_refresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshbtn_refresh.setIcon(icon)
        self.pshbtn_refresh.setObjectName("pshbtn_refresh")
        self.hlo_refresh.addWidget(self.pshbtn_refresh)
        self.hlo_refresh.setStretch(1, 1)
        self.main_layout.addLayout(self.hlo_refresh)
        self.hlo_search = QtWidgets.QHBoxLayout()
        self.hlo_search.setSpacing(10)
        self.hlo_search.setObjectName("hlo_search")
        self.chkbx_archived = QtWidgets.QCheckBox(Sales)
        self.chkbx_archived.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbx_archived.setObjectName("chkbx_archived")
        self.hlo_search.addWidget(self.chkbx_archived)
        self.chkbx_sales_date = QtWidgets.QCheckBox(Sales)
        self.chkbx_sales_date.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbx_sales_date.setObjectName("chkbx_sales_date")
        self.hlo_search.addWidget(self.chkbx_sales_date)
        self.lnedit_sales_date = QtWidgets.QDateEdit(Sales)
        self.lnedit_sales_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_sales_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.lnedit_sales_date.setCalendarPopup(True)
        self.lnedit_sales_date.setObjectName("lnedit_sales_date")
        self.hlo_search.addWidget(self.lnedit_sales_date)
        self.lnedit_patient_name = QtWidgets.QLineEdit(Sales)
        self.lnedit_patient_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_patient_name.setObjectName("lnedit_patient_name")
        self.hlo_search.addWidget(self.lnedit_patient_name)
        self.lnedit_receptionist_name = QtWidgets.QLineEdit(Sales)
        self.lnedit_receptionist_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_receptionist_name.setObjectName("lnedit_receptionist_name")
        self.hlo_search.addWidget(self.lnedit_receptionist_name)
        self.pshbtn_clear = QtWidgets.QPushButton(Sales)
        self.pshbtn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_clear.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshbtn_clear.setIcon(icon1)
        self.pshbtn_clear.setObjectName("pshbtn_clear")
        self.hlo_search.addWidget(self.pshbtn_clear)
        self.hlo_search.setStretch(2, 1)
        self.hlo_search.setStretch(3, 1)
        self.hlo_search.setStretch(4, 1)
        self.main_layout.addLayout(self.hlo_search)
        self.tblwdgt_sales = QtWidgets.QTableWidget(Sales)
        self.tblwdgt_sales.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tblwdgt_sales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblwdgt_sales.setAlternatingRowColors(True)
        self.tblwdgt_sales.setCornerButtonEnabled(False)
        self.tblwdgt_sales.setObjectName("tblwdgt_sales")
        self.tblwdgt_sales.setColumnCount(5)
        self.tblwdgt_sales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_sales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_sales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_sales.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_sales.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_sales.setHorizontalHeaderItem(4, item)
        self.tblwdgt_sales.horizontalHeader().setHighlightSections(False)
        self.tblwdgt_sales.verticalHeader().setVisible(False)
        self.main_layout.addWidget(self.tblwdgt_sales)
        self.wdgt_page_buttons = QtWidgets.QWidget(Sales)
        self.wdgt_page_buttons.setObjectName("wdgt_page_buttons")
        self.wdgt_page_buttons_layout = QtWidgets.QHBoxLayout(self.wdgt_page_buttons)
        self.wdgt_page_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.wdgt_page_buttons_layout.setSpacing(10)
        self.wdgt_page_buttons_layout.setObjectName("wdgt_page_buttons_layout")
        self.pshbtn_add = QtWidgets.QPushButton(self.wdgt_page_buttons)
        self.pshbtn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_add.setObjectName("pshbtn_add")
        self.wdgt_page_buttons_layout.addWidget(self.pshbtn_add)
        self.pshbtn_edit = QtWidgets.QPushButton(self.wdgt_page_buttons)
        self.pshbtn_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_edit.setObjectName("pshbtn_edit")
        self.wdgt_page_buttons_layout.addWidget(self.pshbtn_edit)
        self.pshbtn_archive = QtWidgets.QPushButton(self.wdgt_page_buttons)
        self.pshbtn_archive.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_archive.setObjectName("pshbtn_archive")
        self.wdgt_page_buttons_layout.addWidget(self.pshbtn_archive)
        self.wdgt_page_buttons_layout.setStretch(0, 1)
        self.wdgt_page_buttons_layout.setStretch(1, 1)
        self.wdgt_page_buttons_layout.setStretch(2, 1)
        self.main_layout.addWidget(self.wdgt_page_buttons)
        self.main_layout.setStretch(2, 1)

        self.retranslateUi(Sales)
        QtCore.QMetaObject.connectSlotsByName(Sales)

    def retranslateUi(self, Sales):
        _translate = QtCore.QCoreApplication.translate
        Sales.setWindowTitle(_translate("Sales", "Form"))
        self.lbl_search_filter.setText(_translate("Sales", "Search/Filter:"))
        self.chkbx_archived.setText(_translate("Sales", "Archived"))
        self.chkbx_sales_date.setText(_translate("Sales", "Date"))
        self.lnedit_sales_date.setDisplayFormat(_translate("Sales", "MMM dd, yyyy"))
        self.lnedit_patient_name.setPlaceholderText(_translate("Sales", "Enter patient..."))
        self.lnedit_receptionist_name.setPlaceholderText(_translate("Sales", "Enter receptionist..."))
        item = self.tblwdgt_sales.horizontalHeaderItem(0)
        item.setText(_translate("Sales", "ID"))
        item = self.tblwdgt_sales.horizontalHeaderItem(1)
        item.setText(_translate("Sales", "Date"))
        item = self.tblwdgt_sales.horizontalHeaderItem(2)
        item.setText(_translate("Sales", "Patient"))
        item = self.tblwdgt_sales.horizontalHeaderItem(3)
        item.setText(_translate("Sales", "Receptionist"))
        item = self.tblwdgt_sales.horizontalHeaderItem(4)
        item.setText(_translate("Sales", "Total"))
        self.pshbtn_add.setText(_translate("Sales", "Add"))
        self.pshbtn_edit.setText(_translate("Sales", "Edit"))
        self.pshbtn_archive.setText(_translate("Sales", "Archive"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sales = QtWidgets.QWidget()
    ui = Ui_Sales()
    ui.setupUi(Sales)
    Sales.show()
    sys.exit(app.exec_())
