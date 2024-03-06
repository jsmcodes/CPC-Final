# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_patients_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Patients(object):
    def setupUi(self, Patients):
        Patients.setObjectName("Patients")
        Patients.resize(941, 658)
        Patients.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Patients)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_search_filter = QtWidgets.QLabel(Patients)
        self.lbl_search_filter.setObjectName("lbl_search_filter")
        self.horizontalLayout.addWidget(self.lbl_search_filter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pshbtn_refresh = QtWidgets.QPushButton(Patients)
        self.pshbtn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_refresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshbtn_refresh.setIcon(icon)
        self.pshbtn_refresh.setObjectName("pshbtn_refresh")
        self.horizontalLayout.addWidget(self.pshbtn_refresh)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.wdgt_search_filter = QtWidgets.QWidget(Patients)
        self.wdgt_search_filter.setObjectName("wdgt_search_filter")
        self.wdgt_search_filter_layout = QtWidgets.QHBoxLayout(self.wdgt_search_filter)
        self.wdgt_search_filter_layout.setContentsMargins(0, 0, 0, 0)
        self.wdgt_search_filter_layout.setSpacing(10)
        self.wdgt_search_filter_layout.setObjectName("wdgt_search_filter_layout")
        self.chkbox_archived = QtWidgets.QCheckBox(self.wdgt_search_filter)
        self.chkbox_archived.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbox_archived.setObjectName("chkbox_archived")
        self.wdgt_search_filter_layout.addWidget(self.chkbox_archived)
        self.lnedit_name = QtWidgets.QLineEdit(self.wdgt_search_filter)
        self.lnedit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_name.setClearButtonEnabled(True)
        self.lnedit_name.setObjectName("lnedit_name")
        self.wdgt_search_filter_layout.addWidget(self.lnedit_name)
        self.wdgt_search_filter_layout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.wdgt_search_filter)
        self.tblwdgt_patients = QtWidgets.QTableWidget(Patients)
        self.tblwdgt_patients.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tblwdgt_patients.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblwdgt_patients.setAlternatingRowColors(True)
        self.tblwdgt_patients.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblwdgt_patients.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblwdgt_patients.setObjectName("tblwdgt_patients")
        self.tblwdgt_patients.setColumnCount(4)
        self.tblwdgt_patients.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_patients.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_patients.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_patients.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_patients.setHorizontalHeaderItem(3, item)
        self.tblwdgt_patients.horizontalHeader().setHighlightSections(False)
        self.tblwdgt_patients.verticalHeader().setVisible(False)
        self.tblwdgt_patients.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tblwdgt_patients)
        self.wdgt_page_buttons = QtWidgets.QWidget(Patients)
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
        self.verticalLayout.addWidget(self.wdgt_page_buttons)

        self.retranslateUi(Patients)
        QtCore.QMetaObject.connectSlotsByName(Patients)

    def retranslateUi(self, Patients):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_search_filter.setText(_translate("Patients", "Search/Filter:"))
        self.chkbox_archived.setText(_translate("Patients", "Archived"))
        self.lnedit_name.setPlaceholderText(_translate("Patients", "Enter name..."))
        item = self.tblwdgt_patients.horizontalHeaderItem(0)
        item.setText(_translate("Patients", "ID"))
        item = self.tblwdgt_patients.horizontalHeaderItem(1)
        item.setText(_translate("Patients", "Name"))
        item = self.tblwdgt_patients.horizontalHeaderItem(2)
        item.setText(_translate("Patients", "Sex"))
        item = self.tblwdgt_patients.horizontalHeaderItem(3)
        item.setText(_translate("Patients", "Age"))
        self.pshbtn_add.setText(_translate("Patients", "Add"))
        self.pshbtn_edit.setText(_translate("Patients", "Edit"))
        self.pshbtn_archive.setText(_translate("Patients", "Archive"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Patients = QtWidgets.QWidget()
    ui = Ui_Patients()
    ui.setupUi(Patients)
    Patients.show()
    sys.exit(app.exec_())
