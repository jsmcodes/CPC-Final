# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 849)
        self.wdgt_central = QtWidgets.QWidget(MainWindow)
        self.wdgt_central.setObjectName("wdgt_central")
        self.wdgt_central_layout = QtWidgets.QVBoxLayout(self.wdgt_central)
        self.wdgt_central_layout.setContentsMargins(0, 0, 0, 0)
        self.wdgt_central_layout.setSpacing(0)
        self.wdgt_central_layout.setObjectName("wdgt_central_layout")
        self.stckdwdgt_main = QtWidgets.QStackedWidget(self.wdgt_central)
        self.stckdwdgt_main.setObjectName("stckdwdgt_main")
        self.wdgt_central_layout.addWidget(self.stckdwdgt_main)
        MainWindow.setCentralWidget(self.wdgt_central)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())