# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_doctor_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoctorDialog(object):
    def setupUi(self, DoctorDialog):
        DoctorDialog.setObjectName("DoctorDialog")
        DoctorDialog.resize(500, 720)
        DoctorDialog.setMinimumSize(QtCore.QSize(500, 720))
        DoctorDialog.setMaximumSize(QtCore.QSize(500, 739))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        DoctorDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DoctorDialog.setWindowIcon(icon)
        DoctorDialog.setModal(True)
        self.main_layout = QtWidgets.QVBoxLayout(DoctorDialog)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.lbl_id = QtWidgets.QLabel(DoctorDialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_id.setFont(font)
        self.lbl_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_id.setObjectName("lbl_id")
        self.main_layout.addWidget(self.lbl_id)
        self.lbl_position = QtWidgets.QLabel(DoctorDialog)
        self.lbl_position.setObjectName("lbl_position")
        self.main_layout.addWidget(self.lbl_position)
        self.cmbx_position = QtWidgets.QComboBox(DoctorDialog)
        self.cmbx_position.setEditable(True)
        self.cmbx_position.setCurrentText("")
        self.cmbx_position.setMaxVisibleItems(10)
        self.cmbx_position.setMaxCount(100)
        self.cmbx_position.setObjectName("cmbx_position")
        self.main_layout.addWidget(self.cmbx_position)
        self.lbl_name = QtWidgets.QLabel(DoctorDialog)
        self.lbl_name.setObjectName("lbl_name")
        self.main_layout.addWidget(self.lbl_name)
        self.lnedit_name = QtWidgets.QLineEdit(DoctorDialog)
        self.lnedit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_name.setClearButtonEnabled(True)
        self.lnedit_name.setObjectName("lnedit_name")
        self.main_layout.addWidget(self.lnedit_name)
        self.lbl_sex = QtWidgets.QLabel(DoctorDialog)
        self.lbl_sex.setObjectName("lbl_sex")
        self.main_layout.addWidget(self.lbl_sex)
        self.cmbx_sex = QtWidgets.QComboBox(DoctorDialog)
        self.cmbx_sex.setStyleSheet("")
        self.cmbx_sex.setEditable(True)
        self.cmbx_sex.setMaxVisibleItems(2)
        self.cmbx_sex.setMaxCount(2)
        self.cmbx_sex.setModelColumn(0)
        self.cmbx_sex.setObjectName("cmbx_sex")
        self.cmbx_sex.addItem("")
        self.cmbx_sex.addItem("")
        self.main_layout.addWidget(self.cmbx_sex)
        self.lbl_birthdate = QtWidgets.QLabel(DoctorDialog)
        self.lbl_birthdate.setObjectName("lbl_birthdate")
        self.main_layout.addWidget(self.lbl_birthdate)
        self.dtedit_birthdate = QtWidgets.QDateEdit(DoctorDialog)
        self.dtedit_birthdate.setAlignment(QtCore.Qt.AlignCenter)
        self.dtedit_birthdate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dtedit_birthdate.setProperty("showGroupSeparator", False)
        self.dtedit_birthdate.setCalendarPopup(True)
        self.dtedit_birthdate.setObjectName("dtedit_birthdate")
        self.main_layout.addWidget(self.dtedit_birthdate)
        self.lbl_contact_number = QtWidgets.QLabel(DoctorDialog)
        self.lbl_contact_number.setObjectName("lbl_contact_number")
        self.main_layout.addWidget(self.lbl_contact_number)
        self.lnedit_contact_number = QtWidgets.QLineEdit(DoctorDialog)
        self.lnedit_contact_number.setCursorPosition(0)
        self.lnedit_contact_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_contact_number.setClearButtonEnabled(True)
        self.lnedit_contact_number.setObjectName("lnedit_contact_number")
        self.main_layout.addWidget(self.lnedit_contact_number)
        self.lbl_address = QtWidgets.QLabel(DoctorDialog)
        self.lbl_address.setObjectName("lbl_address")
        self.main_layout.addWidget(self.lbl_address)
        self.txtedit_address = QtWidgets.QTextEdit(DoctorDialog)
        self.txtedit_address.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtedit_address.setTabChangesFocus(True)
        self.txtedit_address.setObjectName("txtedit_address")
        self.main_layout.addWidget(self.txtedit_address)
        self.lbl_username = QtWidgets.QLabel(DoctorDialog)
        self.lbl_username.setObjectName("lbl_username")
        self.main_layout.addWidget(self.lbl_username)
        self.lnedit_username = QtWidgets.QLineEdit(DoctorDialog)
        self.lnedit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_username.setClearButtonEnabled(True)
        self.lnedit_username.setObjectName("lnedit_username")
        self.main_layout.addWidget(self.lnedit_username)
        self.lbl_password = QtWidgets.QLabel(DoctorDialog)
        self.lbl_password.setObjectName("lbl_password")
        self.main_layout.addWidget(self.lbl_password)
        self.lnedit_password = QtWidgets.QLineEdit(DoctorDialog)
        self.lnedit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lnedit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_password.setClearButtonEnabled(True)
        self.lnedit_password.setObjectName("lnedit_password")
        self.main_layout.addWidget(self.lnedit_password)
        self.wdgt_dialog_buttons = QtWidgets.QWidget(DoctorDialog)
        self.wdgt_dialog_buttons.setObjectName("wdgt_dialog_buttons")
        self.wdgt_dialog_buttons_layout = QtWidgets.QHBoxLayout(self.wdgt_dialog_buttons)
        self.wdgt_dialog_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.wdgt_dialog_buttons_layout.setSpacing(10)
        self.wdgt_dialog_buttons_layout.setObjectName("wdgt_dialog_buttons_layout")
        self.pshbtn_add_save = QtWidgets.QPushButton(self.wdgt_dialog_buttons)
        self.pshbtn_add_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_add_save.setObjectName("pshbtn_add_save")
        self.wdgt_dialog_buttons_layout.addWidget(self.pshbtn_add_save)
        self.pshbtn_clear_reset = QtWidgets.QPushButton(self.wdgt_dialog_buttons)
        self.pshbtn_clear_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_clear_reset.setObjectName("pshbtn_clear_reset")
        self.wdgt_dialog_buttons_layout.addWidget(self.pshbtn_clear_reset)
        self.pshbtn_cancel = QtWidgets.QPushButton(self.wdgt_dialog_buttons)
        self.pshbtn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_cancel.setObjectName("pshbtn_cancel")
        self.wdgt_dialog_buttons_layout.addWidget(self.pshbtn_cancel)
        self.wdgt_dialog_buttons_layout.setStretch(0, 1)
        self.wdgt_dialog_buttons_layout.setStretch(1, 1)
        self.wdgt_dialog_buttons_layout.setStretch(2, 1)
        self.main_layout.addWidget(self.wdgt_dialog_buttons)
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 1)
        self.main_layout.setStretch(2, 1)
        self.main_layout.setStretch(3, 1)
        self.main_layout.setStretch(4, 1)
        self.main_layout.setStretch(5, 1)
        self.main_layout.setStretch(6, 1)
        self.main_layout.setStretch(7, 1)
        self.main_layout.setStretch(8, 1)
        self.main_layout.setStretch(9, 1)
        self.main_layout.setStretch(10, 1)
        self.main_layout.setStretch(11, 1)
        self.main_layout.setStretch(12, 1)
        self.main_layout.setStretch(13, 1)
        self.main_layout.setStretch(14, 1)
        self.main_layout.setStretch(15, 1)
        self.main_layout.setStretch(16, 1)

        self.retranslateUi(DoctorDialog)
        self.cmbx_sex.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DoctorDialog)

    def retranslateUi(self, DoctorDialog):
        _translate = QtCore.QCoreApplication.translate
        DoctorDialog.setWindowTitle(_translate("DoctorDialog", "Chan Pediatric Clinic"))
        self.lbl_id.setText(_translate("DoctorDialog", "Doctor #"))
        self.lbl_position.setText(_translate("DoctorDialog", "Position:"))
        self.lbl_name.setText(_translate("DoctorDialog", "Name:"))
        self.lnedit_name.setPlaceholderText(_translate("DoctorDialog", "Enter name..."))
        self.lbl_sex.setText(_translate("DoctorDialog", "Sex:"))
        self.cmbx_sex.setItemText(0, _translate("DoctorDialog", "Female"))
        self.cmbx_sex.setItemText(1, _translate("DoctorDialog", "Male"))
        self.lbl_birthdate.setText(_translate("DoctorDialog", "Birthdate:"))
        self.dtedit_birthdate.setDisplayFormat(_translate("DoctorDialog", "MMM dd, yyyy"))
        self.lbl_contact_number.setText(_translate("DoctorDialog", "Contact Number:"))
        self.lnedit_contact_number.setInputMask(_translate("DoctorDialog", "(+63)\\900-000-0000"))
        self.lnedit_contact_number.setPlaceholderText(_translate("DoctorDialog", "Enter contact number..."))
        self.lbl_address.setText(_translate("DoctorDialog", "Address:"))
        self.txtedit_address.setPlaceholderText(_translate("DoctorDialog", "Enter address..."))
        self.lbl_username.setText(_translate("DoctorDialog", "Username:"))
        self.lnedit_username.setPlaceholderText(_translate("DoctorDialog", "Enter username..."))
        self.lbl_password.setText(_translate("DoctorDialog", "Password:"))
        self.lnedit_password.setPlaceholderText(_translate("DoctorDialog", "Enter password..."))
        self.pshbtn_add_save.setText(_translate("DoctorDialog", "Save"))
        self.pshbtn_clear_reset.setText(_translate("DoctorDialog", "Reset"))
        self.pshbtn_cancel.setText(_translate("DoctorDialog", "Cancel"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DoctorDialog = QtWidgets.QDialog()
    ui = Ui_DoctorDialog()
    ui.setupUi(DoctorDialog)
    DoctorDialog.show()
    sys.exit(app.exec_())