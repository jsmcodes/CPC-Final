# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_consultations_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Consultations(object):
    def setupUi(self, Consultations):
        Consultations.setObjectName("Consultations")
        Consultations.resize(1037, 782)
        Consultations.setWindowTitle("")
        self.main_layout = QtWidgets.QVBoxLayout(Consultations)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.hlo_refresh = QtWidgets.QHBoxLayout()
        self.hlo_refresh.setSpacing(10)
        self.hlo_refresh.setObjectName("hlo_refresh")
        self.lbl_search_filter = QtWidgets.QLabel(Consultations)
        self.lbl_search_filter.setObjectName("lbl_search_filter")
        self.hlo_refresh.addWidget(self.lbl_search_filter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlo_refresh.addItem(spacerItem)
        self.pshbtn_refresh = QtWidgets.QPushButton(Consultations)
        self.pshbtn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_refresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshbtn_refresh.setIcon(icon)
        self.pshbtn_refresh.setObjectName("pshbtn_refresh")
        self.hlo_refresh.addWidget(self.pshbtn_refresh)
        self.hlo_refresh.setStretch(1, 1)
        self.main_layout.addLayout(self.hlo_refresh)
        self.hlo_search_filter = QtWidgets.QHBoxLayout()
        self.hlo_search_filter.setSpacing(10)
        self.hlo_search_filter.setObjectName("hlo_search_filter")
        self.chkbx_archived = QtWidgets.QCheckBox(Consultations)
        self.chkbx_archived.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbx_archived.setObjectName("chkbx_archived")
        self.hlo_search_filter.addWidget(self.chkbx_archived)
        self.lnedit_patient_name = QtWidgets.QLineEdit(Consultations)
        self.lnedit_patient_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_patient_name.setClearButtonEnabled(True)
        self.lnedit_patient_name.setObjectName("lnedit_patient_name")
        self.hlo_search_filter.addWidget(self.lnedit_patient_name)
        self.lnedit_doctor_name = QtWidgets.QLineEdit(Consultations)
        self.lnedit_doctor_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_doctor_name.setClearButtonEnabled(True)
        self.lnedit_doctor_name.setObjectName("lnedit_doctor_name")
        self.hlo_search_filter.addWidget(self.lnedit_doctor_name)
        self.cmbbx_status = QtWidgets.QComboBox(Consultations)
        self.cmbbx_status.setEditable(True)
        self.cmbbx_status.setMaxVisibleItems(4)
        self.cmbbx_status.setMaxCount(4)
        self.cmbbx_status.setObjectName("cmbbx_status")
        self.cmbbx_status.addItem("")
        self.cmbbx_status.addItem("")
        self.cmbbx_status.addItem("")
        self.cmbbx_status.addItem("")
        self.hlo_search_filter.addWidget(self.cmbbx_status)
        self.pshbtn_clear = QtWidgets.QPushButton(Consultations)
        self.pshbtn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_clear.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pshbtn_clear.setIcon(icon1)
        self.pshbtn_clear.setObjectName("pshbtn_clear")
        self.hlo_search_filter.addWidget(self.pshbtn_clear)
        self.hlo_search_filter.setStretch(1, 1)
        self.hlo_search_filter.setStretch(2, 1)
        self.hlo_search_filter.setStretch(3, 1)
        self.main_layout.addLayout(self.hlo_search_filter)
        self.tblwdgt_consultations = QtWidgets.QTableWidget(Consultations)
        self.tblwdgt_consultations.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tblwdgt_consultations.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblwdgt_consultations.setAlternatingRowColors(True)
        self.tblwdgt_consultations.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblwdgt_consultations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblwdgt_consultations.setObjectName("tblwdgt_consultations")
        self.tblwdgt_consultations.setColumnCount(3)
        self.tblwdgt_consultations.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_consultations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_consultations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwdgt_consultations.setHorizontalHeaderItem(2, item)
        self.tblwdgt_consultations.horizontalHeader().setHighlightSections(False)
        self.tblwdgt_consultations.verticalHeader().setVisible(False)
        self.main_layout.addWidget(self.tblwdgt_consultations)
        self.wdgt_page_buttons = QtWidgets.QWidget(Consultations)
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
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 1)
        self.main_layout.setStretch(2, 18)

        self.retranslateUi(Consultations)
        QtCore.QMetaObject.connectSlotsByName(Consultations)

    def retranslateUi(self, Consultations):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_search_filter.setText(_translate("Consultations", "Search/Filter:"))
        self.chkbx_archived.setText(_translate("Consultations", "Archived"))
        self.lnedit_patient_name.setPlaceholderText(_translate("Consultations", "Enter patient\'s name..."))
        self.lnedit_doctor_name.setPlaceholderText(_translate("Consultations", "Enter doctor\'s name..."))
        self.cmbbx_status.setItemText(0, _translate("Consultations", "All"))
        self.cmbbx_status.setItemText(1, _translate("Consultations", "Done"))
        self.cmbbx_status.setItemText(2, _translate("Consultations", "Ongoing"))
        self.cmbbx_status.setItemText(3, _translate("Consultations", "Waiting"))
        item = self.tblwdgt_consultations.horizontalHeaderItem(0)
        item.setText(_translate("Consultations", "ID"))
        item = self.tblwdgt_consultations.horizontalHeaderItem(1)
        item.setText(_translate("Consultations", "Patient"))
        item = self.tblwdgt_consultations.horizontalHeaderItem(2)
        item.setText(_translate("Consultations", "Status"))
        self.pshbtn_add.setText(_translate("Consultations", "Add"))
        self.pshbtn_edit.setText(_translate("Consultations", "Edit"))
        self.pshbtn_archive.setText(_translate("Consultations", "Archive"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Consultations = QtWidgets.QWidget()
    ui = Ui_Consultations()
    ui.setupUi(Consultations)
    Consultations.show()
    sys.exit(app.exec_())