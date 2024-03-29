# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_prescription_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrescriptionDialog(object):
    def setupUi(self, PrescriptionDialog):
        PrescriptionDialog.setObjectName("PrescriptionDialog")
        PrescriptionDialog.resize(694, 541)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PrescriptionDialog.setWindowIcon(icon)
        PrescriptionDialog.setModal(True)
        self.main_layout = QtWidgets.QVBoxLayout(PrescriptionDialog)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName("main_layout")
        self.scrllarea_prescription = QtWidgets.QScrollArea(PrescriptionDialog)
        self.scrllarea_prescription.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrllarea_prescription.setWidgetResizable(True)
        self.scrllarea_prescription.setAlignment(QtCore.Qt.AlignCenter)
        self.scrllarea_prescription.setObjectName("scrllarea_prescription")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 443))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrllarea_prescription.setWidget(self.scrollAreaWidgetContents)
        self.main_layout.addWidget(self.scrllarea_prescription)
        self.pshbtn_save = QtWidgets.QPushButton(PrescriptionDialog)
        self.pshbtn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pshbtn_save.setObjectName("pshbtn_save")
        self.main_layout.addWidget(self.pshbtn_save)
        self.pshbtn_close = QtWidgets.QPushButton(PrescriptionDialog)
        self.pshbtn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pshbtn_close.setObjectName("pshbtn_close")
        self.main_layout.addWidget(self.pshbtn_close)
        self.main_layout.setStretch(0, 1)

        self.retranslateUi(PrescriptionDialog)
        QtCore.QMetaObject.connectSlotsByName(PrescriptionDialog)

    def retranslateUi(self, PrescriptionDialog):
        _translate = QtCore.QCoreApplication.translate
        PrescriptionDialog.setWindowTitle(_translate("PrescriptionDialog", "Chan Pediatric Clinic"))
        self.pshbtn_save.setText(_translate("PrescriptionDialog", "Save"))
        self.pshbtn_close.setText(_translate("PrescriptionDialog", "Close"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrescriptionDialog = QtWidgets.QDialog()
    ui = Ui_PrescriptionDialog()
    ui.setupUi(PrescriptionDialog)
    PrescriptionDialog.show()
    sys.exit(app.exec_())
