from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QMarginsF, QSize, Qt
from PyQt5.QtGui import QPageLayout, QPageSize, QCursor, QIcon

import sys
import os

from UI.main_prescription_dialog_ui import Ui_PrescriptionDialog

class PrescriptionDialog(QDialog):
    def __init__(self, consultation_id:int, patient_name:str, consultation_date:str, patient_address:str, doctor_name:str):
        super().__init__()
        self.absolute_path = os.path.abspath(__file__)

        self.consultation_id = consultation_id
        self.patient_name = patient_name
        self.consultation_date = consultation_date
        self.patient_address = patient_address
        self.doctor_name = doctor_name

        html_relative_path = r"HTML\prescription.html"
        tentative_relative_path = r"HTML\tentative.html"

        self.html_absolute_path = os.path.join(os.path.dirname(self.absolute_path), html_relative_path)
        self.tentative_absolute_path = os.path.join(os.path.dirname(self.absolute_path), tentative_relative_path)

        self.setup_ui()
        self.setup_window()

    def setup_ui(self):
        self.ui = Ui_PrescriptionDialog()
        self.ui.setupUi(self)

        self.set_consultation_data_in_html()

        self.connect_functions()

    def setup_window(self):
        self.showMaximized()

    def set_consultation_data_in_html(self):
        with open(self.html_absolute_path, "r") as pdf_file:
            html_content = pdf_file.read()

        replacement_texts = {
            'patient_name': self.patient_name,
            'consultation_date': self.consultation_date,
            'patient_address': self.patient_address,
            'doctor_name': self.doctor_name
        }

        for placeholder, replacement in replacement_texts.items():
            html_content = html_content.replace(f'{{{placeholder}}}', replacement)

        with open(self.tentative_absolute_path, "w") as pdf_file:
            pdf_file.write(html_content)

        self.ui.WEV_prescription.setUrl(QUrl.fromLocalFile(self.tentative_absolute_path))

    def handle_save(self):
        self.setFocus()

        page_size = QPageSize(QPageSize.Letter)
        orientation = QPageLayout.Landscape
        margins = QMarginsF()

        page_layout = QPageLayout(page_size, orientation, margins)
        
        pdf_name = f"{self.consultation_id}_{self.patient_name}_{self.consultation_date}.pdf"
        pdf_path = "Prescriptions"
        pdf_save_path = os.path.join(pdf_path, pdf_name)

        self.webEngineView.page().printToPdf(pdf_save_path, page_layout)
        self.accept()

    def handle_close(self):
        self.reject()

    def connect_functions(self):
        self.ui.pshbtn_save.clicked.connect(self.handle_save)
        self.ui.pshbtn_close.clicked.connect(self.handle_close)
