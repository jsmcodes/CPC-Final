from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QHeaderView, QCheckBox, QTextEdit
from PyQt5.QtCore import Qt, QDate, QTime

from datetime import datetime

from dev_functions.database_manager import DatabaseManager
from UI.main_dashboard_consultation_dialog_ui import Ui_DoctorConsultationDialog


class DoctorConsultationDialog(QDialog):
    def __init__(self, parent: QWidget, purpose: str, patient_id: int, consultation_id: int=None):
        super().__init__()
        self.database = DatabaseManager()
        self.parent = parent
        self.purpose = purpose
        self.patient_id = patient_id
        self.consultation_id = consultation_id
        self.setup_ui()
        self.setup_window()

    def set_initial_data(self):
        def calculate_age(birthdate):
            current_date = datetime.now()
            birthdate_str = birthdate.strftime("%Y-%m-%d")
            birthdate = QDate.fromString(birthdate_str, "yyyy-MM-dd")

            age_years = current_date.year - birthdate.year()
            age_months = current_date.month - birthdate.month()
            age_days = current_date.day - birthdate.day()

            if age_days < 0:
                age_months -= 1
                days_in_prev_month = (current_date.replace(month=current_date.month - 1) - current_date.replace(day=1)).days
                age_days += days_in_prev_month

            if age_months < 0:
                age_years -= 1
                age_months += 12

            return f"{age_years}y {age_months}m"

        def fetch_initial_data():
            self.database.connect()

            query = f"""
                SELECT
                    name,
                    sex,
                    birthdate
                FROM
                    patients
                WHERE
                    id = {self.patient_id}
            """
            self.database.c.execute(query)

            patient_data = self.database.c.fetchone()

            self.database.disconnect()

            return patient_data
        
        name, sex, birthdate = fetch_initial_data()
        age = calculate_age(birthdate)

        self.ui.lbl_consultation_id.setText(f"Consultation #{self.consultation_id}")

        self.ui.lnedit_name.setText(name)
        self.ui.lnedit_sex.setText(sex)
        self.ui.lnedit_age.setText(age)

        self.ui.dtedit_consultation_date.setDate(QDate.currentDate())
        self.ui.tmedit_consultation_time.setTime(QTime.currentTime())

    def setup_ui(self):
        self.ui = Ui_DoctorConsultationDialog()
        self.ui.setupUi(self)

        if self.purpose == "View":
            self.set_ui_for_view()
        elif self.purpose == "Edit":
            self.set_ui_for_edit()
        else:
            self.set_ui_for_add()
            self.set_initial_data()

        self.connect_functions()
        
    def setup_window(self):
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)

    def set_ui_for_view(self):
        self.ui.wdgt_scrllarea_medical_history.setEnabled(False)
        self.ui.wdgt_scrllarea_patient_record.setEnabled(False)
        self.ui.pshbtn_create_prescription.hide()
        self.ui.pshbtn_finish_consultation.hide()
        self.ui.pshbtn_save.hide()

    def set_ui_for_edit(self):
        self.ui.pshbtn_create_prescription.hide()
        self.ui.pshbtn_finish_consultation.hide()

    def set_ui_for_add(self):
        self.ui.pshbtn_previous.hide()
        self.ui.pshbtn_next.hide()
        self.ui.pshbtn_save.hide()
        self.ui.pshbtn_view_prescription.hide()

    def get_consultation_data(self):
        def get_type_of_delivery():
            type_of_delivery = None
            if self.ui.rdobtn_cs.isChecked():
                type_of_delivery = "CS"
            else:
                type_of_delivery = "NSD"

            return type_of_delivery
        
        def get_admitted_to_nicu():
            admitted_to_nicu = None
            if self.ui.rdobtn_no.isChecked():
                admitted_to_nicu = "No"
            else:
                admitted_to_nicu = "Yes"

            return admitted_to_nicu
        
        def get_consultation_date_time():
            consultation_date = self.ui.dtedit_consultation_date.date().toPyDate()
            consultation_time = self.ui.tmedit_consultation_time.time().toPyTime()

            return (
                consultation_date, 
                consultation_time
            )

        def get_anthropometrics():
            height = self.ui.lnedit_height.text().strip()
            weight = self.ui.lnedit_weight.text().strip()
            head_circumference = self.ui.lnedit_head_circumference.text().strip()
            chest_circumference = self.ui.lnedit_chest_circumference.text().strip()
            abdominal_circumference = self.ui.lnedit_abdominal_circumference.text().strip()

            return (
                height, 
                weight, 
                head_circumference, 
                chest_circumference, 
                abdominal_circumference
            )

        def get_vital_signs():
            blood_pressure = self.ui.lnedit_blood_pressure.text().strip()
            cardiac_rate = self.ui.lnedit_cardiac_rate.text().strip()
            temperature = self.ui.lnedit_temperature.text().strip()

            return (
                blood_pressure, 
                cardiac_rate, 
                temperature
            )

        def get_consultation_remarks():
            chief_complaint = self.ui.txtedit_chief_complaint.toPlainText().strip()
            pertinent_pe = self.ui.txtedit_pertinent_pe.toPlainText().strip()
            management = self.ui.txtedit_management.toPlainText().strip()
            history_of_present_illness = self.ui.txtedit_history_of_present_illness.toPlainText().strip()

            return (
                chief_complaint, 
                pertinent_pe, 
                management, 
                history_of_present_illness
            )

        def get_birth_history():
            mother_age = self.ui.lnedit_mother_age.text().strip()
            g_score = self.ui.lnedit_g_score.text().strip()
            type_of_delivery = get_type_of_delivery()
            if type_of_delivery == "CS":
                if_cs = self.ui.txtedit_if_cs.toPlainText().strip()
            else:
                if_cs = "N/A"
            prematurity = self.ui.chkbx_prematurity.isChecked()
            cord_coil = self.ui.chkbx_cord_coil.isChecked()
            meconium_stained_amniotic_fluid = self.ui.chkbx_meconium.isChecked()
            admitted_to_nicu = get_admitted_to_nicu()
            if admitted_to_nicu == "Yes":
                if_yes = self.ui.txtedit_if_yes.toPlainText().strip()
            else:
                if_yes = "N/A"

            return (
                mother_age, 
                g_score, 
                type_of_delivery, 
                if_cs, 
                prematurity, 
                cord_coil, 
                meconium_stained_amniotic_fluid, 
                admitted_to_nicu, 
                if_yes
            )
        
        def get_past_medical_history():
            previous_admission = self.ui.chkbx_previous_admission.isChecked()
            if previous_admission:
                previous_admission_note = self.ui.txtedit_previous_admission.toPlainText().strip()
            else:
                previous_admission_note = "N/A"

            asthma = self.ui.chkbx_asthma.isChecked()
            if asthma:
                asthma_note = self.ui.txtedit_asthma.toPlainText().strip()
            else:
                asthma_note = "N/A"

            allergies = self.ui.chkbx_allergies.isChecked()
            if allergies:
                allergies_note = self.ui.txtedit_allergies.toPlainText().strip()
            else:
                allergies_note = "N/A"

            primary_kochs_infection = self.ui.chkbx_primary_kochs_infection.isChecked()
            if primary_kochs_infection:
                primary_kochs_infection_note = self.ui.txtedit_primary_kochs_infection.toPlainText().strip()
            else:
                primary_kochs_infection_note = "N/A"

            heart_kidney_lung_condition = self.ui.chkbx_heart_kidney_lung_condition.isChecked()
            if heart_kidney_lung_condition:
                heart_kidney_lung_condition_note = self.ui.txtedit_heart_kidney_lung_condition.toPlainText().strip()
            else:
                heart_kidney_lung_condition_note = "N/A"
            
            surgical_operation = self.ui.chkbx_surgical_operation.isChecked()
            if surgical_operation:
                surgical_operation_note = self.ui.txtedit_surgical_operation.toPlainText().strip()
            else:
                surgical_operation_note = "N/A"

            other_remarks_pmh = self.ui.chkbx_other_remarks_pmh.isChecked()
            if other_remarks_pmh:
                other_remarks_pmh_note = self.ui.txtedit_other_remarks_pmh.toPlainText().strip()
            else:
                other_remarks_pmh_note = "N/A"

            return (
                previous_admission, 
                previous_admission_note, 
                asthma, asthma_note, 
                allergies, 
                allergies_note, 
                primary_kochs_infection, 
                primary_kochs_infection_note, 
                heart_kidney_lung_condition, 
                heart_kidney_lung_condition_note, 
                surgical_operation, 
                surgical_operation_note, 
                other_remarks_pmh, 
                other_remarks_pmh_note
            )
        
        def get_family_medical_history():
            asthma_fmh = self.ui.chkbx_asthma_fmh.isChecked()
            allergies_fmh = self.ui.chkbx_allergies_fmh.isChecked()
            hypertension = self.ui.chkbx_hypertension.isChecked()
            diabetes_mellitus = self.ui.chkbx_diabetes_mellitus.isChecked()
            ptb = self.ui.chkbx_ptb.isChecked()
            cancer = self.ui.chkbx_cancer.isChecked()
            blood_disorder_leukemia = self.ui.chkbx_blood_disorder_leukemia.isChecked()
            autoimmune_diseases = self.ui.chkbx_autoimmune_disease.isChecked()
            other_remarks_fmh = self.ui.chkbx_other_remarks_fmh.isChecked()
            if other_remarks_fmh:
                other_remarks_fmh_note = self.ui.txtedit_other_remarks_fmh.toPlainText().strip()
            else:
                other_remarks_fmh_note = "N/A"

            return (
                asthma_fmh, 
                allergies_fmh, 
                hypertension, 
                diabetes_mellitus, 
                ptb, 
                cancer, 
                blood_disorder_leukemia, 
                autoimmune_diseases, 
                other_remarks_fmh, 
                other_remarks_fmh_note
            )

        def get_environmental_history():
            near_poultry_hog_farm = self.ui.chkbx_near_poultry_hog_farm.isChecked()
            indoor_pets = self.ui.chkbx_indoor_pets.isChecked()
            smokers = self.ui.chkbx_smokers.isChecked()
            poorly_ventilated_house = self.ui.chkbx_poorly_ventilated_house.isChecked()
            other_remarks_emh = self.ui.chkbx_other_remarks_eh.isChecked()
            if other_remarks_emh:
                other_remarks_emh_note = self.ui.txtedit_other_remarks_eh.toPlainText().strip()
            else:
                other_remarks_emh_note = "N/A"

            return (
                near_poultry_hog_farm, 
                indoor_pets, smokers, 
                poorly_ventilated_house, 
                other_remarks_emh, 
                other_remarks_emh_note
            )

        def get_immunization_history():
            shots_bcg = self.ui.spnbx_bcg.text().strip()
            booster_bcg = self.ui.chkbx_bcg.isChecked()
            shots_hepa_b = self.ui.spnbx_hepa_b.text().strip()
            booster_hepa_b = self.ui.chkbx_hepa_b.isChecked()
            shots_penta = self.ui.spnbx_penta.text().strip()
            booster_penta = self.ui.chkbx_penta.isChecked()
            shots_pcv = self.ui.spnbx_pcv.text().strip()
            booster_pcv = self.ui.chkbx_pcv.isChecked()
            shots_opv_ipv = self.ui.spnbx_opv_ipv.text().strip()
            booster_opv_ipv = self.ui.chkbx_opv_ipv.isChecked()
            shots_rotavirus = self.ui.spnbx_rotavirus.text().strip()
            booster_rotavirus = self.ui.chkbx_rotavirus.isChecked()
            shots_flu = self.ui.spnbx_flu.text().strip()
            booster_flu = self.ui.chkbx_flu.isChecked()
            shots_measles = self.ui.spnbx_measles.text().strip()
            booster_measles = self.ui.chkbx_measles.isChecked()
            shots_varicella = self.ui.spnbx_varicella.text().strip()
            booster_varicella = self.ui.chkbx_varicella.isChecked()
            shots_hepa_a = self.ui.spnbx_hepa_a.text().strip()
            booster_hepa_a = self.ui.chkbx_hepa_a.isChecked()
            shots_mmr = self.ui.spnbx_mmr.text().strip()
            booster_mmr = self.ui.chkbx_mmr.isChecked()
            shots_japanese_encephalitis = self.ui.spnbx_japanese_encephalitis.text().strip()
            booster_japanese_encephalitis = self.ui.chkbx_japanese_encephalitis.isChecked()

            return (
                shots_bcg, booster_bcg,
                shots_hepa_b, booster_hepa_b,
                shots_penta, booster_penta,
                shots_pcv, booster_pcv,
                shots_opv_ipv, booster_opv_ipv,
                shots_rotavirus, booster_rotavirus,
                shots_flu, booster_flu,
                shots_measles, booster_measles,
                shots_varicella, booster_varicella,
                shots_hepa_a, booster_hepa_a,
                shots_mmr, booster_mmr,
                shots_japanese_encephalitis, booster_japanese_encephalitis
            )
        
        consultation_date_time = get_consultation_date_time()
        anthropometrics = get_anthropometrics()
        vital_signs = get_vital_signs()
        consultation_remarks = get_consultation_remarks()
        birth_history = get_birth_history()
        past_medical_history = get_past_medical_history()
        family_medical_history = get_family_medical_history()
        environmental_history = get_environmental_history()
        immunization_history = get_immunization_history()

        return (
            consultation_date_time,
            anthropometrics,
            vital_signs,
            consultation_remarks,
            birth_history,
            past_medical_history,
            family_medical_history,
            environmental_history,
            immunization_history
        )

    def handle_finish_consultation(self):
        
        def verify_anthropometrics(data):
            for detail in data:
                if not detail:
                    return False
            
            return True
        
        def verify_vital_signs(data):
            for detail in data:
                if not detail:
                    return False
            
            return True
        
        def verify_consultation_remarks(data):
            for detail in data:
                if not detail:
                    return False
            
            return True
        
        def verify_birth_history(data):
            type_cs = False
            if_yes = False

            for index, detail in enumerate(data):
                if index == 0 or index == 1:
                    if not detail:
                        return False
                if index == 2:
                    if detail == "CS":
                        type_cs = True
                if index == 3 and type_cs:
                    if not detail:
                        return False
                if index == 7:
                    if detail == "Yes":
                        if_yes = True
                if index == 8 and if_yes:
                    if not detail:
                        return False
            
            return True
        
        def verify_past_medical_history(data):
            previous_admission = False
            asthma = False
            allergies = False
            primary_kochs_infection = False
            heart_kidney_lung_condition = False
            surgical_operation = False
            other_remarks = False
            
            for index, detail in enumerate(data):
                if index == 0:
                    if detail:
                        previous_admission = True
                if index == 1 and previous_admission:
                    if not detail:
                        return False
                if index == 2:
                    if detail:
                        asthma = True
                if index == 3 and asthma:
                    if not detail:
                        return False
                if index == 4:
                    if detail:
                        allergies = True
                if index == 5 and allergies:
                    if not detail:
                        return False
                if index == 6:
                    if detail:
                        primary_kochs_infection = True
                if index == 7 and primary_kochs_infection:
                    if not detail:
                        return False
                if index == 8:
                    if detail:
                        heart_kidney_lung_condition = True
                if index == 9 and heart_kidney_lung_condition:
                    if not detail:
                        return False
                if index == 10:
                    if detail:
                        surgical_operation = True
                if index == 11 and surgical_operation:
                    if not detail:
                        return False
                if index == 12:
                    if detail:
                        other_remarks = True
                if index == 13 and other_remarks:
                    if not detail:
                        return False
            
            return True
        
        def verify_family_medical_history(data):
            other_remarks = False

            for index, detail in enumerate(data):
                if index == 8:
                    if detail:
                        other_remarks = True
                if index == 9 and other_remarks:
                    if not detail:
                        return False
            
            return True
        
        def verify_environmental_history(data):
            other_remarks = False

            for index, detail in enumerate(data):
                if index == 4:
                    if detail:
                        other_remarks = True
                if index == 5 and other_remarks:
                    if not detail:
                        return False
            
            return True

        def check_if_inputs_filled(consultation_data):
            consultation_date_time, anthropometrics, vital_signs, consultation_remarks, birth_history, past_medical_history, family_medical_history, environmental_history, immunization_history = consultation_data

            if not verify_anthropometrics(anthropometrics):
                return False

            if not verify_vital_signs(vital_signs):
                return False

            if not verify_consultation_remarks(consultation_remarks):
                return False

            if not verify_birth_history(birth_history):
                return False

            if not verify_past_medical_history(past_medical_history):
                return False

            if not verify_family_medical_history(family_medical_history):
                return False

            if not verify_environmental_history(environmental_history):
                return False
            
            return True

        def insert_consultation_data(consultation_data):
            consultation_date_time, anthropometrics, vital_signs, consultation_remarks, birth_history, past_medical_history, family_medical_history, environmental_history, immunization_history = consultation_data

            age = self.ui.lnedit_age.text()
            consultation_date, consultation_time = consultation_date_time
            height, weight, head_circumference, chest_circumference, abdominal_circumference = anthropometrics
            blood_pressure, cardiac_rate, temperature = vital_signs
            chief_complaint, pertinent_pe, management, history_of_present_illness = consultation_remarks
            mother_age, g_score, type_of_delivery, if_cs, prematurity, cord_coil, meconium_stained_amniotic_fluid, admitted_to_nicu, if_yes = birth_history
            previous_admission, previous_admission_note, asthma, asthma_note, allergies, allergies_note, primary_kochs_infection, primary_kochs_infection_note, heart_kidney_lung_condition, heart_kidney_lung_condition_note, surgical_operation, surgical_operation_note, other_remarks_pmh, other_remarks_pmh_note = past_medical_history
            asthma_fmh, allergies_fmh, hypertension, diabetes_mellitus, ptb, cancer, blood_disorder_leukemia, autoimmune_diseases, other_remarks_fmh, other_remarks_fmh_note = family_medical_history
            near_poultry_hog_farm, indoor_pets, smokers, poorly_ventilated_house, other_remarks_eh, other_remarks_eh_note = environmental_history
            shots_bcg, booster_bcg, shots_hepa_b, booster_hepa_b, shots_penta, booster_penta, shots_pcv, booster_pcv, shots_opv_ipv, booster_opv_ipv, shots_rotavirus, booster_rotavirus, shots_flu, booster_flu, shots_measles, booster_measles, shots_varicella, booster_varicella, shots_hepa_a, booster_hepa_a, shots_mmr, booster_mmr, shots_japanese_encephalitis, booster_japanese_encephalitis = immunization_history

            self.database.connect()

            query = f"""
                INSERT INTO
                    consultation_details (
                        consultation_id,
                        age,
                        consultation_date,
                        consultation_time,
                        height,
                        weight,
                        head_circumference,
                        chest_circumference,
                        abdominal_circumference,
                        blood_pressure,
                        cardiac_rate,
                        temperature,
                        chief_complaint,
                        pertinent_pe,
                        management,
                        history_of_present_illness,
                        mother_age_at_delivery, 
                        g_score, 
                        type_of_delivery, 
                        if_cs, 
                        prematurity, 
                        cord_coil, 
                        meconium_stained_amniotic_fluid, 
                        admitted_to_nicu, 
                        if_yes,
                        previous_admission, 
                        previous_admission_note, 
                        asthma, asthma_note, 
                        allergies, 
                        allergies_note, 
                        primary_kochs_infection, 
                        primary_kochs_infection_note, 
                        heart_kidney_lung_condition, 
                        heart_kidney_lung_condition_note, 
                        surgical_operation, 
                        surgical_operation_note, 
                        other_remark_pmh, 
                        other_remark_pmh_note,
                        asthma_fmh, 
                        allergies_fmh, 
                        hypertension, 
                        diabetes_mellitus, 
                        ptb, 
                        cancer, 
                        blood_disorder_leukemia, 
                        autoimmune_diseases, 
                        other_remark_fmh, 
                        other_remark_fmh_note,
                        near_poultry_hog_farm, 
                        indoor_pets, smokers, 
                        poorly_ventilated_house, 
                        other_remark_eh, 
                        other_remark_eh_note,
                        bcg, 
                        bcg_booster,
                        hepa_b, 
                        hepa_b_booster,
                        penta, 
                        penta_booster,
                        pcv, 
                        pcv_booster,
                        opv_ipv, 
                        opv_ipv_booster,
                        rotavirus, 
                        rotavirus_booster,
                        flu, 
                        flu_booster,
                        measles, 
                        measles_booster,
                        varicella, 
                        varicella_booster,
                        hepa_a, 
                        hepa_a_booster,
                        mmr, 
                        mmr_booster,
                        japanese_encephalitis, 
                        japanese_encephalitis_booster
                    )
                VALUES (
                    {self.consultation_id},
                    '{age}',
                    '{consultation_date}',
                    '{consultation_time}',
                    '{height}',
                    '{weight}',
                    '{head_circumference}',
                    '{chest_circumference}',
                    '{abdominal_circumference}',
                    '{blood_pressure}',
                    '{cardiac_rate}',
                    '{temperature}',
                    '{chief_complaint}',
                    '{pertinent_pe}',
                    '{management}',
                    '{history_of_present_illness}',
                    '{mother_age}',
                    '{g_score}',
                    '{type_of_delivery}',
                    '{if_cs}',
                    {prematurity},
                    {cord_coil},
                    {meconium_stained_amniotic_fluid},
                    '{admitted_to_nicu}',
                    '{if_yes}',
                    {previous_admission},
                    '{previous_admission_note}',
                    {asthma},
                    '{asthma_note}',
                    {allergies},
                    '{allergies_note}',
                    {primary_kochs_infection},
                    '{primary_kochs_infection_note}',
                    {heart_kidney_lung_condition},
                    '{heart_kidney_lung_condition_note}',
                    {surgical_operation},
                    '{surgical_operation_note}',
                    {other_remarks_pmh},
                    '{other_remarks_pmh_note}',
                    {asthma_fmh},
                    {allergies_fmh},
                    {hypertension},
                    {diabetes_mellitus},
                    {ptb},
                    {cancer},
                    {blood_disorder_leukemia},
                    {autoimmune_diseases},
                    {other_remarks_fmh},
                    '{other_remarks_fmh_note}',
                    {near_poultry_hog_farm},
                    {indoor_pets},
                    {smokers},
                    {poorly_ventilated_house},
                    {other_remarks_eh},
                    '{other_remarks_eh_note}',
                    {shots_bcg},
                    {booster_bcg},
                    {shots_hepa_b},
                    {booster_hepa_b},
                    {shots_penta},
                    {booster_penta},
                    {shots_pcv},
                    {booster_pcv},
                    {shots_opv_ipv},
                    {booster_opv_ipv},
                    {shots_rotavirus},
                    {booster_rotavirus},
                    {shots_flu},
                    {booster_flu},
                    {shots_measles},
                    {booster_measles},
                    {shots_varicella},
                    {booster_varicella},
                    {shots_hepa_a},
                    {booster_hepa_a},
                    {shots_mmr},
                    {booster_mmr},
                    {shots_japanese_encephalitis},
                    {booster_japanese_encephalitis}
                )
            """
            self.database.c.execute(query)
            self.database.conn.commit()

            self.database.disconnect()

        def finish_consultation():
            self.database.connect()
            
            query = f"""
                UPDATE
                    consultations
                SET
                    status = 'Done'
                WHERE
                    id = {self.consultation_id}
            """
            self.database.c.execute(query)

            self.database.conn.commit()

            self.database.disconnect()

        if self.purpose == "Add":
            consultation_data = self.get_consultation_data()
            inputs_filled = check_if_inputs_filled(consultation_data)
            if inputs_filled:
                insert_consultation_data(consultation_data)
                finish_consultation()
                self.accept()
        else:
            self.reject()

    def handle_type_of_delivery_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.ui.txtedit_if_cs.setEnabled(True)
        else:
            self.ui.txtedit_if_cs.setEnabled(False)
            self.ui.txtedit_if_cs.clear()

    def handle_admitted_to_nicu(self):
        sender = self.sender()
        if sender.isChecked():
            self.ui.txtedit_if_yes.setEnabled(True)
        else:
            self.ui.txtedit_if_yes.setEnabled(False)
            self.ui.txtedit_if_yes.clear()

    def handle_checkbox_checked(self, state, textedit:QTextEdit):
        if state == Qt.Checked:
            textedit.setEnabled(True)
        else:
            textedit.setEnabled(False)
            textedit.clear()

    def handle_spinbox_changed(self, value, checkbox:QCheckBox):
        if value >= 3:
            checkbox.setEnabled(True)
        else:
            checkbox.setEnabled(False)
            checkbox.setChecked(False)

    def handle_close(self):
        self.reject()

    def connect_functions(self):
        self.ui.rdobtn_cs.toggled.connect(self.handle_type_of_delivery_clicked)
        self.ui.rdobtn_yes.toggled.connect(self.handle_admitted_to_nicu)

        self.ui.chkbx_previous_admission.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_previous_admission))
        self.ui.chkbx_asthma.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_asthma))
        self.ui.chkbx_allergies.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_allergies))
        self.ui.chkbx_primary_kochs_infection.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_primary_kochs_infection))
        self.ui.chkbx_heart_kidney_lung_condition.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_heart_kidney_lung_condition))
        self.ui.chkbx_surgical_operation.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_surgical_operation))
        self.ui.chkbx_other_remarks_pmh.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_other_remarks_pmh))
        self.ui.chkbx_other_remarks_fmh.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_other_remarks_fmh))
        self.ui.chkbx_other_remarks_eh.stateChanged.connect(lambda state: self.handle_checkbox_checked(state, self.ui.txtedit_other_remarks_eh))

        self.ui.spnbx_bcg.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_bcg))
        self.ui.spnbx_hepa_b.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_hepa_b))
        self.ui.spnbx_penta.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_penta))
        self.ui.spnbx_pcv.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_pcv))
        self.ui.spnbx_opv_ipv.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_opv_ipv))
        self.ui.spnbx_rotavirus.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_rotavirus))
        self.ui.spnbx_flu.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_flu))
        self.ui.spnbx_measles.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_measles))
        self.ui.spnbx_varicella.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_varicella))
        self.ui.spnbx_hepa_a.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_hepa_a))
        self.ui.spnbx_mmr.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_mmr))
        self.ui.spnbx_japanese_encephalitis.valueChanged.connect(lambda value: self.handle_spinbox_changed(value, self.ui.chkbx_japanese_encephalitis))

        self.ui.pshbtn_finish_consultation.clicked.connect(self.handle_finish_consultation)
        self.ui.pshbtn_close.clicked.connect(self.handle_close)