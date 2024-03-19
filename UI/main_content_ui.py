# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\main_content_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Content(object):
    def setupUi(self, Content):
        Content.setObjectName("Content")
        Content.resize(1080, 720)
        Content.setWindowTitle("")
        self.main_layout = QtWidgets.QHBoxLayout(Content)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.wdgt_navigation = QtWidgets.QWidget(Content)
        self.wdgt_navigation.setObjectName("wdgt_navigation")
        self.wdgt_navigation_layout = QtWidgets.QVBoxLayout(self.wdgt_navigation)
        self.wdgt_navigation_layout.setContentsMargins(10, 0, 0, 10)
        self.wdgt_navigation_layout.setSpacing(0)
        self.wdgt_navigation_layout.setObjectName("wdgt_navigation_layout")
        self.wdgt_user = QtWidgets.QWidget(self.wdgt_navigation)
        self.wdgt_user.setObjectName("wdgt_user")
        self.wdgt_user_layout = QtWidgets.QVBoxLayout(self.wdgt_user)
        self.wdgt_user_layout.setContentsMargins(10, 10, 10, 10)
        self.wdgt_user_layout.setSpacing(10)
        self.wdgt_user_layout.setObjectName("wdgt_user_layout")
        self.pxmp_logo = QtWidgets.QLabel(self.wdgt_user)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pxmp_logo.sizePolicy().hasHeightForWidth())
        self.pxmp_logo.setSizePolicy(sizePolicy)
        self.pxmp_logo.setText("")
        self.pxmp_logo.setPixmap(QtGui.QPixmap(":/small_logo.png"))
        self.pxmp_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pxmp_logo.setObjectName("pxmp_logo")
        self.wdgt_user_layout.addWidget(self.pxmp_logo)
        self.lbl_position = QtWidgets.QLabel(self.wdgt_user)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_position.sizePolicy().hasHeightForWidth())
        self.lbl_position.setSizePolicy(sizePolicy)
        self.lbl_position.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_position.setWordWrap(True)
        self.lbl_position.setObjectName("lbl_position")
        self.wdgt_user_layout.addWidget(self.lbl_position)
        self.lbl_name = QtWidgets.QLabel(self.wdgt_user)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setWordWrap(True)
        self.lbl_name.setObjectName("lbl_name")
        self.wdgt_user_layout.addWidget(self.lbl_name)
        self.line = QtWidgets.QFrame(self.wdgt_user)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.wdgt_user_layout.addWidget(self.line)
        self.wdgt_user_layout.setStretch(0, 5)
        self.wdgt_user_layout.setStretch(1, 1)
        self.wdgt_user_layout.setStretch(2, 1)
        self.wdgt_user_layout.setStretch(3, 1)
        self.wdgt_navigation_layout.addWidget(self.wdgt_user)
        self.pshbtn_dashboard = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_dashboard.sizePolicy().hasHeightForWidth())
        self.pshbtn_dashboard.setSizePolicy(sizePolicy)
        self.pshbtn_dashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_dashboard.setFlat(True)
        self.pshbtn_dashboard.setObjectName("pshbtn_dashboard")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_dashboard)
        self.pshbtn_reports = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_reports.sizePolicy().hasHeightForWidth())
        self.pshbtn_reports.setSizePolicy(sizePolicy)
        self.pshbtn_reports.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_reports.setFlat(True)
        self.pshbtn_reports.setObjectName("pshbtn_reports")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_reports)
        self.pshbtn_consultations = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_consultations.sizePolicy().hasHeightForWidth())
        self.pshbtn_consultations.setSizePolicy(sizePolicy)
        self.pshbtn_consultations.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_consultations.setFlat(True)
        self.pshbtn_consultations.setObjectName("pshbtn_consultations")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_consultations)
        self.pshbtn_services = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_services.sizePolicy().hasHeightForWidth())
        self.pshbtn_services.setSizePolicy(sizePolicy)
        self.pshbtn_services.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_services.setFlat(True)
        self.pshbtn_services.setObjectName("pshbtn_services")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_services)
        self.pshbtn_sales = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_sales.sizePolicy().hasHeightForWidth())
        self.pshbtn_sales.setSizePolicy(sizePolicy)
        self.pshbtn_sales.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_sales.setFlat(True)
        self.pshbtn_sales.setObjectName("pshbtn_sales")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_sales)
        self.pshbtn_payment_methods = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_payment_methods.sizePolicy().hasHeightForWidth())
        self.pshbtn_payment_methods.setSizePolicy(sizePolicy)
        self.pshbtn_payment_methods.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_payment_methods.setFlat(True)
        self.pshbtn_payment_methods.setObjectName("pshbtn_payment_methods")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_payment_methods)
        self.pshbtn_items = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_items.sizePolicy().hasHeightForWidth())
        self.pshbtn_items.setSizePolicy(sizePolicy)
        self.pshbtn_items.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_items.setFlat(True)
        self.pshbtn_items.setObjectName("pshbtn_items")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_items)
        self.pshbtn_patients = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_patients.sizePolicy().hasHeightForWidth())
        self.pshbtn_patients.setSizePolicy(sizePolicy)
        self.pshbtn_patients.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_patients.setFlat(True)
        self.pshbtn_patients.setObjectName("pshbtn_patients")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_patients)
        self.pshbtn_doctors = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_doctors.sizePolicy().hasHeightForWidth())
        self.pshbtn_doctors.setSizePolicy(sizePolicy)
        self.pshbtn_doctors.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_doctors.setFlat(True)
        self.pshbtn_doctors.setObjectName("pshbtn_doctors")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_doctors)
        self.pshbtn_positions = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_positions.sizePolicy().hasHeightForWidth())
        self.pshbtn_positions.setSizePolicy(sizePolicy)
        self.pshbtn_positions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_positions.setFlat(True)
        self.pshbtn_positions.setObjectName("pshbtn_positions")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_positions)
        spacerItem = QtWidgets.QSpacerItem(20, 369, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.wdgt_navigation_layout.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(self.wdgt_navigation)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.wdgt_navigation_layout.addWidget(self.line_2)
        self.pshbtn_settings = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_settings.sizePolicy().hasHeightForWidth())
        self.pshbtn_settings.setSizePolicy(sizePolicy)
        self.pshbtn_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_settings.setFlat(True)
        self.pshbtn_settings.setObjectName("pshbtn_settings")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_settings)
        self.pshbtn_logout = QtWidgets.QPushButton(self.wdgt_navigation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshbtn_logout.sizePolicy().hasHeightForWidth())
        self.pshbtn_logout.setSizePolicy(sizePolicy)
        self.pshbtn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pshbtn_logout.setFlat(True)
        self.pshbtn_logout.setObjectName("pshbtn_logout")
        self.wdgt_navigation_layout.addWidget(self.pshbtn_logout)
        self.wdgt_navigation_layout.setStretch(0, 5)
        self.wdgt_navigation_layout.setStretch(1, 1)
        self.wdgt_navigation_layout.setStretch(2, 1)
        self.wdgt_navigation_layout.setStretch(3, 1)
        self.wdgt_navigation_layout.setStretch(4, 1)
        self.wdgt_navigation_layout.setStretch(5, 1)
        self.wdgt_navigation_layout.setStretch(6, 1)
        self.wdgt_navigation_layout.setStretch(7, 1)
        self.wdgt_navigation_layout.setStretch(8, 1)
        self.wdgt_navigation_layout.setStretch(9, 1)
        self.wdgt_navigation_layout.setStretch(10, 1)
        self.wdgt_navigation_layout.setStretch(11, 10)
        self.wdgt_navigation_layout.setStretch(12, 1)
        self.wdgt_navigation_layout.setStretch(13, 1)
        self.wdgt_navigation_layout.setStretch(14, 1)
        self.main_layout.addWidget(self.wdgt_navigation)
        self.stckdwdgt_content = QtWidgets.QStackedWidget(Content)
        self.stckdwdgt_content.setObjectName("stckdwdgt_content")
        self.main_layout.addWidget(self.stckdwdgt_content)
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 9)

        self.retranslateUi(Content)
        QtCore.QMetaObject.connectSlotsByName(Content)

    def retranslateUi(self, Content):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_position.setText(_translate("Content", "[POSITION HERE]"))
        self.lbl_name.setText(_translate("Content", "[NAME HERE]"))
        self.pshbtn_dashboard.setText(_translate("Content", "Dashboard"))
        self.pshbtn_reports.setText(_translate("Content", "Reports"))
        self.pshbtn_consultations.setText(_translate("Content", "Consultations"))
        self.pshbtn_services.setText(_translate("Content", "Services"))
        self.pshbtn_sales.setText(_translate("Content", "Sales"))
        self.pshbtn_payment_methods.setText(_translate("Content", "Payment Methods"))
        self.pshbtn_items.setText(_translate("Content", "Items"))
        self.pshbtn_patients.setText(_translate("Content", "Patients"))
        self.pshbtn_doctors.setText(_translate("Content", "Doctors"))
        self.pshbtn_positions.setText(_translate("Content", "Positions"))
        self.pshbtn_settings.setText(_translate("Content", "Settings"))
        self.pshbtn_logout.setText(_translate("Content", "Logout"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Content = QtWidgets.QWidget()
    ui = Ui_Content()
    ui.setupUi(Content)
    Content.show()
    sys.exit(app.exec_())
