import mysql.connector
from loguru import logger

import sqlite3

class DatabaseManager:
    def __init__(self, local:bool=False):
        logger.add("Logging/database_manager.log", rotation="1 day", compression="zip", level="INFO")
        self.local = local
        self.database_name = "database"
        if self.local:
            self.database_tables = {
                "patients": (
                    """
                        id INT PRIMARY KEY,
                        name VARCHAR(255),
                        sex VARCHAR(6),
                        birthdate DATE,
                        contact_number VARCHAR(17),
                        address VARCHAR(255),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "users": (
                    """
                        id INT PRIMARY KEY,
                        position_id INT,
                        name VARCHAR(255),
                        sex VARCHAR(6),
                        birthdate DATE,
                        contact_number VARCHAR(17),
                        address VARCHAR(255),
                        username VARCHAR(50),
                        password VARCHAR(50),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "positions": (
                    """
                        id INT PRIMARY KEY,
                        name VARCHAR(100),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "login_history": (
                    """
                        id INT PRIMARY KEY,
                        user_id INT,
                        name VARCHAR(255),
                        position VARCHAR(12),
                        date DATE DEFAULT CURRENT_DATE,
                        time TIME DEFAULT CURRENT_TIME
                    """
                ),
                "consultations": (
                    """
                        id INT PRIMARY KEY,
                        patient_id INT,
                        doctor_id INT,
                        status VARCHAR(7) DEFAULT 'Waiting',
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "consultation_details": (
                    """
                        id INT PRIMARY KEY,
                        consultation_id INT,
                        age VARCHAR(255),
                        consultation_date DATE,
                        consultation_time TIME,
                        height VARCHAR(255),
                        weight VARCHAR(255),
                        head_circumference VARCHAR(255),
                        chest_circumference VARCHAR(255),
                        abdominal_circumference VARCHAR(255),
                        blood_pressure VARCHAR(255),
                        cardiac_rate VARCHAR(255),
                        temperature VARCHAR(255),
                        chief_complaint VARCHAR(255),
                        pertinent_pe VARCHAR(255),
                        management VARCHAR(255),
                        history_of_present_illness VARCHAR(255),
                        mother_age_at_delivery VARCHAR(255),
                        g_score VARCHAR(255),
                        type_of_delivery VARCHAR(3),
                        if_cs VARCHAR(255),
                        prematurity BIT(1) DEFAULT 0,
                        cord_coil BIT(1) DEFAULT 0,
                        meconium_stained_amniotic_fluid BIT(1) DEFAULT 0,
                        admitted_to_nicu VARCHAR(3),
                        if_yes VARCHAR(255),
                        previous_admission BIT(1) DEFAULT 0,
                        previous_admission_note VARCHAR(255),
                        asthma BIT(1) DEFAULT 0,
                        asthma_note VARCHAR(255),
                        allergies BIT(1) DEFAULT 0,
                        allergies_note VARCHAR(255),
                        primary_kochs_infection BIT(1) DEFAULT 0,
                        primary_kochs_infection_note VARCHAR(255),
                        heart_kidney_lung_condition BIT(1) DEFAULT 0,
                        heart_kidney_lung_condition_note VARCHAR(255),
                        surgical_operation BIT(1) DEFAULT 0,
                        surgical_operation_note VARCHAR(255),
                        other_remark_pmh BIT(1) DEFAULT 0,
                        other_remark_pmh_note VARCHAR(255),
                        asthma_fmh BIT(1) DEFAULT 0,
                        allergies_fmh BIT(1) DEFAULT 0,
                        hypertension BIT(1) DEFAULT 0,
                        diabetes_mellitus BIT(1) DEFAULT 0,
                        ptb BIT(1) DEFAULT 0,
                        cancer BIT(1) DEFAULT 0,
                        blood_disorder_leukemia BIT(1) DEFAULT 0,
                        autoimmune_diseases BIT(1) DEFAULT 0,
                        other_remark_fmh BIT(1) DEFAULT 0,
                        other_remark_fmh_note VARCHAR(255),
                        near_poultry_hog_farm BIT(1) DEFAULT 0,
                        indoor_pets BIT(1) DEFAULT 0,
                        smokers BIT(1) DEFAULT 0,
                        poorly_ventilated_house BIT(1) DEFAULT 0,
                        other_remark_eh BIT(1) DEFAULT 0,
                        other_remark_eh_note VARCHAR(255),
                        bcg INT,
                        bcg_booster BIT(1) DEFAULT 0,
                        hepa_b INT,
                        hepa_b_booster BIT(1) DEFAULT 0,
                        penta INT,
                        penta_booster BIT(1) DEFAULT 0,
                        pcv INT,
                        pcv_booster BIT(1) DEFAULT 0,
                        opv_ipv INT,
                        opv_ipv_booster BIT(1) DEFAULT 0,
                        rotavirus INT,
                        rotavirus_booster BIT(1) DEFAULT 0,
                        flu INT,
                        flu_booster BIT(1) DEFAULT 0,
                        measles INT,
                        measles_booster BIT(1) DEFAULT 0,
                        varicella INT,
                        varicella_booster BIT(1) DEFAULT 0,
                        hepa_a INT,
                        hepa_a_booster BIT(1) DEFAULT 0,
                        mmr INT,
                        mmr_booster BIT(1) DEFAULT 0,
                        japanese_encephalitis INT,
                        japanese_encephalitis_booster BIT(1) DEFAULT 0
                    """
                ),
                "services": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        price DOUBLE,
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "payment_methods": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "items": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        price DOUBLE,
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "sales": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        sale_date DATE,
                        patient_id INT,
                        user_id INT,
                        total_price DOUBLE,
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "sale_details": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        sale_id INT,
                        item_id INT,
                        price DOUBLE,
                        quantity INT,
                        total_price DOUBLE
                    """
                )
            }
        else:
            self.database_tables = {
                "patients": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        sex VARCHAR(6),
                        birthdate DATE,
                        contact_number VARCHAR(17),
                        address VARCHAR(255),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "users": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        position_id INT,
                        name VARCHAR(255),
                        sex VARCHAR(6),
                        birthdate DATE,
                        contact_number VARCHAR(17),
                        address VARCHAR(255),
                        username VARCHAR(50),
                        password VARCHAR(50),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "positions": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(100),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "login_history": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        user_id INT,
                        name VARCHAR(255),
                        position VARCHAR(12),
                        date DATE DEFAULT CURRENT_DATE,
                        time TIME DEFAULT CURRENT_TIME
                    """
                ),
                "consultations": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        patient_id INT,
                        doctor_id INT,
                        status VARCHAR(7) DEFAULT 'Waiting',
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "consultation_details": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        consultation_id INT,
                        age VARCHAR(255),
                        consultation_date DATE,
                        consultation_time TIME,
                        height VARCHAR(255),
                        weight VARCHAR(255),
                        head_circumference VARCHAR(255),
                        chest_circumference VARCHAR(255),
                        abdominal_circumference VARCHAR(255),
                        blood_pressure VARCHAR(255),
                        cardiac_rate VARCHAR(255),
                        temperature VARCHAR(255),
                        chief_complaint VARCHAR(255),
                        pertinent_pe VARCHAR(255),
                        management VARCHAR(255),
                        history_of_present_illness VARCHAR(255),
                        mother_age_at_delivery VARCHAR(255),
                        g_score VARCHAR(255),
                        type_of_delivery VARCHAR(255),
                        if_cs VARCHAR(255),
                        prematurity VARCHAR(255),
                        cord_coil VARCHAR(255),
                        meconium_stained_amniotic_fluid VARCHAR(255),
                        admitted_to_nicu VARCHAR(255),
                        if_yes VARCHAR(255),
                        previous_admission BIT(1) DEFAULT 0,
                        previous_admission_note VARCHAR(255),
                        asthma BIT(1) DEFAULT 0,
                        asthma_note VARCHAR(255),
                        allergies BIT(1) DEFAULT 0,
                        allergies_note VARCHAR(255),
                        primary_kochs_infection BIT(1) DEFAULT 0,
                        primary_kochs_infection_note VARCHAR(255),
                        heart_kidney_lung_condition BIT(1) DEFAULT 0,
                        heart_kidney_lung_condition_note VARCHAR(255),
                        surgical_operation BIT(1) DEFAULT 0,
                        surgical_operation_note VARCHAR(255),
                        other_remark_pmh BIT(1) DEFAULT 0,
                        other_remark_pmh_note VARCHAR(255),
                        asthma_fmh BIT(1) DEFAULT 0,
                        allergies_fmh BIT(1) DEFAULT 0,
                        hypertension BIT(1) DEFAULT 0,
                        diabetes_mellitus BIT(1) DEFAULT 0,
                        ptb BIT(1) DEFAULT 0,
                        cancer BIT(1) DEFAULT 0,
                        blood_disorder_leukemia BIT(1) DEFAULT 0,
                        autoimmune_diseases BIT(1) DEFAULT 0,
                        other_remark_fmh BIT(1) DEFAULT 0,
                        other_remark_fmh_note VARCHAR(255),
                        near_poultry_hog_farm BIT(1) DEFAULT 0,
                        indoor_pets BIT(1) DEFAULT 0,
                        smokers BIT(1) DEFAULT 0,
                        poorly_ventilated_house BIT(1) DEFAULT 0,
                        other_remark_eh BIT(1) DEFAULT 0,
                        other_remark_eh_note VARCHAR(255),
                        bcg INT,
                        bcg_booster BIT(1) DEFAULT 0,
                        hepa_b INT,
                        hepa_b_booster BIT(1) DEFAULT 0,
                        penta INT,
                        penta_booster BIT(1) DEFAULT 0,
                        pcv INT,
                        pcv_booster BIT(1) DEFAULT 0,
                        opv_ipv INT,
                        opv_ipv_booster BIT(1) DEFAULT 0,
                        rotavirus INT,
                        rotavirus_booster BIT(1) DEFAULT 0,
                        flu INT,
                        flu_booster BIT(1) DEFAULT 0,
                        measles INT,
                        measles_booster BIT(1) DEFAULT 0,
                        varicella INT,
                        varicella_booster BIT(1) DEFAULT 0,
                        hepa_a INT,
                        hepa_a_booster BIT(1) DEFAULT 0,
                        mmr INT,
                        mmr_booster BIT(1) DEFAULT 0,
                        japanese_encephalitis INT,
                        japanese_encephalitis_booster BIT(1) DEFAULT 0
                    """
                ),
                "services": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        price DOUBLE,
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "payment_methods": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "items": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        price DOUBLE,
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "sales": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        sale_date DATE,
                        patient_id INT,
                        user_id INT,
                        total_price DOUBLE,
                        archived BIT(1) DEFAULT 0
                    """
                ),
                "sale_details": (
                    """
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        sale_id INT,
                        item_id INT,
                        price DOUBLE,
                        quantity INT,
                        total_price DOUBLE
                    """
                )
            }
        self.conn = None
        self.c = None
        self.host = ""
        self.user = "all"
        self.password = "allpass"

    def connect(self):
        try:
            if self.local:
                self.conn = sqlite3.connect("Database/data.db")
                self.c = self.conn.cursor()
            else:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )
                self.c = self.conn.cursor()
                query = f"USE `{self.database_name}`"
                self.c.execute(query)
                
            # logger.info("Connected to the database.")
            
        except mysql.connector.Error as err:
            logger.error(f"Error connecting to the database: {err}")

    def disconnect(self):
        if self.conn:
            self.c.close()
            self.conn.close()
            # logger.info("Disconnected from the database.")
    
    def create_database(self):
        try:
            self.connect()
            create_db_query = f"CREATE DATABASE IF NOT EXISTS `{self.database_name}`"
            self.c.execute(create_db_query)
            self.conn.commit()
            logger.info(f"Database '{self.database_name}' created successfully.")
        except Exception as e:
            logger.error(f"Error in create_database: {e}")
        finally:
            self.disconnect()

    def create_tables(self):
        try:
            self.connect()

            for table_name, table_structure in self.database_tables.items():
                create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({table_structure})"
                self.c.execute(create_table_query)

            self.conn.commit()
            logger.info("Database tables created successfully.")
        except Exception as e:
            logger.error(f"Error in create_tables: {e}")
        finally:
            self.disconnect()

    def insert_positions(self):
        self.connect()

        positions = ("Administrator", "Receptionist", "Pediatrician", "OB/GYN")

        for position in positions:
            query = f"""
                INSERT INTO positions (
                    name
                )
                VALUES (
                    '{position}'
                )
            """
            self.c.execute(query)


        self.conn.commit()
        self.disconnect()

    def insert_users(self):
        self.connect()

        users = (
            (1, "test_admin", "Male", "2000-02-10", "(+63)998-765-4321", "Admin Address", "admin", "adminpass"),
            (2, 'test_receptionist', 'Female', '1999-07-28', '(+63)912-345-3215', 'Test Address 3', 'recep', 'receppass'),
            (3, 'test_pedia', 'Male', '2000-02-20', '(+63)912-345-6789', 'Test Address 1', 'user3', 'pass3'),
            (4, 'test_obgyn', 'Female', '1976-09-20', '(+63)912-345-7856', 'Test Address 2', 'user4', 'pass4')
        )

        for user in users:
            query = f"""
                INSERT INTO users (
                    position_id,
                    name,
                    sex,
                    birthdate,
                    contact_number,
                    address,
                    username,
                    password
                )
                VALUES (
                    {user[0]},
                    '{user[1]}',
                    '{user[2]}',
                    '{user[3]}',
                    '{user[4]}',
                    '{user[5]}',
                    '{user[6]}',
                    '{user[7]}'
                )
            """
            self.c.execute(query)


        self.conn.commit()
        self.disconnect()

    def insert_values(self):
        self.connect()

        query = """
            INSERT INTO patients (
                name,
                sex,
                birthdate,
                contact_number,
                address
            )
            VALUES (
                'Jasper Sampang',
                'Male',
                '2000-02-10',
                '(+63)961-639-3688',
                'B19 L1 Camella General Trias, Brgy San Francisco, General Trias City, Cavite'
            )
        """
        self.c.execute(query)

        self.conn.commit()
        self.disconnect()


def main():
    database = DatabaseManager()
    database.create_database()
    database.create_tables()
    database.insert_positions()
    database.insert_users()
    database.insert_values()


if __name__ == "__main__":
    main()