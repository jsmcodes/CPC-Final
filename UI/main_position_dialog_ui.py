# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_position_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PositionDialog(object):
    def setupUi(self, PositionDialog):
        PositionDialog.setObjectName("PositionDialog")
        PositionDialog.resize(400, 300)
        PositionDialog.setMinimumSize(QtCore.QSize(400, 300))
        PositionDialog.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        PositionDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PositionDialog.setWindowIcon(icon)
        self.main_layout = QtWidgets.QVBoxLayout(PositionDialog)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.lbl_position_id = QtWidgets.QLabel(PositionDialog)
        self.lbl_position_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_position_id.setObjectName("lbl_position_id")
        self.main_layout.addWidget(self.lbl_position_id)
        self.lbl_name = QtWidgets.QLabel(PositionDialog)
        self.lbl_name.setObjectName("lbl_name")
        self.main_layout.addWidget(self.lbl_name)
        self.lnedit_name = QtWidgets.QLineEdit(PositionDialog)
        self.lnedit_name.setMaxLength(100)
        self.lnedit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lnedit_name.setClearButtonEnabled(True)
        self.lnedit_name.setObjectName("lnedit_name")
        self.main_layout.addWidget(self.lnedit_name)
        self.wdgt_dialog_buttons = QtWidgets.QWidget(PositionDialog)
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

        self.retranslateUi(PositionDialog)
        QtCore.QMetaObject.connectSlotsByName(PositionDialog)

    def retranslateUi(self, PositionDialog):
        _translate = QtCore.QCoreApplication.translate
        PositionDialog.setWindowTitle(_translate("PositionDialog", "Chan Pediatric Clinic"))
        self.lbl_position_id.setText(_translate("PositionDialog", "Position #"))
        self.lbl_name.setText(_translate("PositionDialog", "Name:"))
        self.lnedit_name.setPlaceholderText(_translate("PositionDialog", "Enter name..."))
        self.pshbtn_add_save.setText(_translate("PositionDialog", "Save"))
        self.pshbtn_clear_reset.setText(_translate("PositionDialog", "Reset"))
        self.pshbtn_cancel.setText(_translate("PositionDialog", "Cancel"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PositionDialog = QtWidgets.QDialog()
    ui = Ui_PositionDialog()
    ui.setupUi(PositionDialog)
    PositionDialog.show()
    sys.exit(app.exec_())