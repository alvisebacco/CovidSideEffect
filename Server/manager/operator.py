import json
import psycopg2
from configparser import ConfigParser
from colorama import Fore
import hashlib
from datetime import datetime
from flask import jsonify


class DefensiveCode:
    def __init__(self):
        print('[+] Checking connection...')

    @staticmethod
    def checking_connection():
        return 'Connesso'


class DatabaseOperations:
    def __init__(self):
        try:
            db_name: str = 'postgresql'
            config = ConfigParser()
            config.read('manager/database.ini')
            if config.has_section(db_name):
                self.username = config.get(db_name, 'user')
                self.password = config.get(db_name, 'passwd')
                self.database = config.get(db_name, 'database')
                self.host = config.get(db_name, 'host')
                self.port = config.get(db_name, 'port')
        except Exception as e:
            print(Fore.RED + '[ERROR] ' + str(e))

        try:
            self.connection = psycopg2.connect('host=' + self.host + ' '
                                                                     'port=' + self.port + ' '
                                                                                           'dbname=' + self.database + ' '
                                                                                                                       'user=' + self.username + ' '
                                                                                                                                                 'password=' + self.password)

            print(Fore.GREEN + '[+] Connected to database: ', self.database)
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as e:
            print(Fore.RED + str(e))

    async def check_and_create_table_reaction(self):
        """tabella di reazione"""
        table_reaction = 'reaction'
        # Ogni fattore di rischio è caratterizzato da un
        # nome univoco,
        # una descrizione e il
        # livello di rischio associato.
        cloumn_id_ = 'id_'
        column_severity = 'severity'  # valore che prendo dalla slide bar
        column_description = 'description'  # descrizione a campo libero
        column_reporting = 'reporting'  # paziente che riporta, Foreign Key
        column_doctor = 'doctor'  # medico che riporta, Foreign Key

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY," \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50), " \
              "%s varchar(50) NOT NULL," \
              "foreign key(reporting) REFERENCES patient(id_), " \
              "%s varchar(50) NOT NULL, foreign key(doctor) REFERENCES customers(cf));" % (
                  table_reaction, cloumn_id_, column_severity, column_description, column_reporting, column_doctor)

        await self.create_table(sql)

    async def check_and_create_table_reporting(self):
        """ tabella di inserimento dei dati principali"""

        table_reporting = 'reporting'

        # Ogni segnalazione è caratterizzata da un

        # codice univoco, column_id
        # dall’indicazione del paziente a cui fa riferimento, column_patient FK
        # dall’indicazione della reazione avversa, column_adverse_reaction
        # dalla data della reazione avversa, column_date_of_reaction
        # dalla data di segnalazione, column_date_reporting
        # e dalle vaccinazioni ricevute nei..., vaccination_carried_out

        column_id = 'id_'
        column_patient = 'patient'
        column_adverse_reaction = 'adv_reaction'
        column_date_of_reaction = 'reaction_date'
        column_date_of_reporting = 'reporting_date'
        column_vaccination_carried_out = 'vaccination_carried_out'
        column_doctor = 'doctor'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s date NOT NULL, " \
              "%s date NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, foreign key(doctor) REFERENCES customers(cf))" % (
                  table_reporting, column_id, column_patient, column_adverse_reaction,
                  column_date_of_reaction, column_date_of_reporting,
                  column_vaccination_carried_out, column_doctor)
        await self.create_table(sql)

    async def check_and_create_table_risk(self):
        """tabella con i dati del rischio"""
        table_user = 'Risk'

        column_id = 'id_'
        column_description = 'Description'
        column_risk_level = 'Risk_level'
        column_doctor = 'Doctor'
        column_patient = 'Patient'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL," \
              "%s varchar(50) NOT NULL," \
              "foreign key(doctor) REFERENCES customers(cf), " \
              "%s varchar(50) NOT NULL, foreign key(patient) REFERENCES patient(id_));" % (table_user, column_id,
                                                                                           column_description,
                                                                                           column_risk_level,
                                                                                           column_doctor,
                                                                                           column_patient)
        await self.create_table(sql)

    async def check_and_create_table_vaccination(self):
        """tabella con i dati dei vaccini"""
        # Ogni vaccinazione è caratterizzata da:

        # paziente a cui si riferisce,
        # segnalazioni a cui è legata,
        # vaccino somministrato (AstraZeneca, Pfizer, Moderna, Sputnik, Sinovac, antinfluenzale, …),
        # tipo della somministrazione (I, II, III o IV dose, dose unica),
        # sede presso la quale è avvenuta la vaccinazione e
        # data di vaccinazione.

        table_vaccination = 'vaccination'
        column_id = 'id_'
        column_patient = 'patient'
        column_reporting = 'reporting'
        column_vaccination = 'vaccination'
        column_dose = 'dose'
        column_site = 'site'
        column_vaccination_date = 'vaccination_date'
        column_doctor = 'doctor'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50), FOREIGN KEY(reporting) REFERENCES  reporting(id_), " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, FOREIGN KEY(doctor) REFERENCES customers(cf));" % (
                  table_vaccination, column_id, column_patient,
                  column_reporting, column_vaccination,
                  column_dose, column_site, column_vaccination_date, column_doctor)

        await self.create_table(sql)

    async def check_and_create_table_patient(self):
        """tabella con i dati del paziente"""

        table_patient = 'patient'
        column_id = 'id_'
        column_year_of_birth = 'date_of_birth'
        column_province_of_residence = 'province_residence'
        column_job = 'job'
        column_previous_vaccinations = 'previous_vaccination'
        column_doctor = 'doctor'

        # Fattori di rischio
        column_is_smoker = 'is_smoker'
        column_is_fatty = 'is_fatty'
        column_cardioonco = 'is_cardioonco'
        column_hyper = 'is_hyper'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50), " \
              "%s varchar(50), " \
              "%s varchar(50), %s varchar(50), %s varchar(50), %s varchar(50)," \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "foreign key(doctor) REFERENCES customers(cf));" % (table_patient, column_job, column_is_smoker,
                                                                  column_is_fatty, column_hyper, column_cardioonco,
                                                                  column_previous_vaccinations,
                                                                  column_year_of_birth,
                                                                  column_province_of_residence, column_id,
                                                                  column_doctor)
        await self.create_table(sql)

    async def check_and_create_table_user(self):
        """ creo le tabelle se non esistono gia' """

        table_user = 'customers'
        column_name = 'Name'
        column_surname = 'Surname'
        column_pass = 'Passwd'
        column_role = 'Role'
        column_cf = 'CF'
        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(128) NOT NULL, " \
              "%s varchar(50) PRIMARY KEY)" % (table_user, column_name, column_surname,
                                               column_role, column_pass, column_cf)
        await self.create_table(sql)

    def post_new_user(self, new_user_data: json) -> str:
        """ inserisco i dati utente nel db """

        name = new_user_data['Nome']
        surname = new_user_data['Cognome']
        role = new_user_data['Ruolo']
        fiscal_code = new_user_data['CF']
        password = new_user_data['Password']
        password = self.get_password_hash(password)

        sql = "INSERT INTO customers (name, surname, role, passwd, cf) VALUES (%s, %s, %s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (name, surname, role, password, fiscal_code))
        self.connection.commit()
        return 'New user created!'

    def post_new_patient(self, patient_data) -> json:
        job = patient_data['job']
        yyyy = patient_data['yyyy']
        city = patient_data['city']
        cf = patient_data['CF']
        med = patient_data['med']

        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM patient WHERE id_='%s'" % cf
            cursor.execute(sql)
            sql_result = cursor.fetchone()
            if sql_result is None:
                sql = "INSERT INTO patient (job, date_of_birth, province_residence, id_, doctor) " \
                      "VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (job, yyyy, city, cf, med))
                self.connection.commit()
                login_success = {'Server': 'Server',
                                 'message': 'Paziente inserito!'}
                return login_success
            else:
                login_failed = {'Server': 'Server',
                                'message': 'Paziente già presente nel database!'}
                return login_failed
        except Exception as e:
            login_failed = {'Server': 'Server exception!',
                            'message': str(e)}
            return login_failed

    def post_new_vaccination(self, vaccination: json) -> json:
        response = {'Server': 'Server',
                    'message': ''}
        vaccination_ = vaccination['vaccination']
        date_ = vaccination['date']
        place_ = vaccination['place']
        dose_ = vaccination['dose']
        patient_ = vaccination['patient']
        doctor_ = vaccination['doctor']
        pk = f'{date_}{vaccination_}{doctor_}'
        reporting = 'Non legata a reazione avversa'
        pk = self.calculate_sha1(pk)
        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO vaccination(id_, patient, vaccination, dose, site, vaccination_date, doctor) 
                     VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (pk, patient_, vaccination_, dose_, place_, date_, doctor_))
            self.connection.commit()
            response = {'Server': 'Server',
                        'message': 'Vaccinazione inserita correttamente!'}
        except Exception as e:
            print(e)
            response = {'Server': 'Server',
                        'message': str(e)}
        finally:
            return response

    def post_new_reaction(self, reaction: json) -> json:
        response = {'Server': 'Server',
                    'message': ''}
        # Tabella paziente
        today = datetime.now()
        is_smoker = reaction['smoker']
        is_fatty = reaction['fatty']
        cardioonco = reaction['cardioonco']
        hypert = reaction['hypert']
        # DAti della reazione
        reaction_date = reaction['reaction_date']
        cf_primary_key = reaction['cf_primary_key']
        all_vaccinations = self.extract_vaccinations(reaction['vaccination_array_of_dict'])
        try:
            cursor = self.connection.cursor()
            sql = """UPDATE patient SET is_smoker=%s, is_fatty=%s, is_hyper=%s, 
            is_cardioonco=%s, previous_vaccination=%s
                  WHERE id_=%s"""
            cursor.execute(sql, (is_smoker, is_fatty, hypert, cardioonco, all_vaccinations, cf_primary_key))
            self.connection.commit()
            sql = """SELECT doctor from patient WHERE id_='%s'""" % cf_primary_key
            cursor.execute(sql)
            sql_result = cursor.fetchone()
            if sql_result is None:
                response = {'Server': 'Server',
                            'message': 'Paziente non trovato! Registra il paziente!'}
                return response
            else:
                for __reaction__ in reaction['vaccination_array_of_dict']:
                    vaccination = __reaction__['vaccination']
                    if vaccination != 'Non':
                        vaccination_date = __reaction__['date']
                        place = __reaction__['place']
                        dose = __reaction__['dose']
                        description = __reaction__['description']
                        severity = __reaction__['severity']
                for tuple_ in sql_result:
                    doctor = tuple_
                pk = f'({vaccination_date}{cf_primary_key}{vaccination}{reaction_date}{dose}{description})'
                pk = self.calculate_sha1(pk)
                sql = """INSERT INTO reporting (id_, patient, adv_reaction, reaction_date, reporting_date,
                 vaccination_carried_out, doctor) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (pk, cf_primary_key, description, reaction_date, today, vaccination, doctor))
                self.connection.commit()
                pk_ = f'({vaccination}{today}{cf_primary_key}{vaccination_date}{cf_primary_key})'
                pk_ = self.calculate_sha1(pk)
                sql = """INSERT INTO vaccination (id_, patient, reporting, vaccination, dose, 
                site, vaccination_date, doctor)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (pk_, cf_primary_key, pk, vaccination, dose, place, vaccination_date, sql_result))
                self.connection.commit()

                # Reazione
                sql = """INSERT INTO reaction (id_, severity, description, reporting, doctor)
                VALUES (%s, %s, %s, %s, %s)"""
                pk__ = f'{severity}{vaccination}{description}{vaccination_date}{cf_primary_key}{today}Reaction'
                pk__ = self.calculate_sha1(pk__)
                cursor.execute(sql, (pk__, str(severity), description, cf_primary_key, doctor))
                self.connection.commit()
                # Rischio
                _pk = f'{vaccination}{severity}{description}{vaccination_date}{vaccination}{today}'
                _pk = self.calculate_sha1(_pk)
                sql = """INSERT INTO risk (id_, description, risk_level, doctor, patient)
                         VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(sql, (_pk, description, severity, sql_result, cf_primary_key))
                self.connection.commit()
                response = {'Server': 'Server',
                            'message': 'Paziente aggiornato e segnalazione inviata!'}
        except (Exception, psycopg2.DatabaseError) as e:
            response = {'Server': 'Server',
                        'message': str(e)}
            print(e)
        finally:
            return response

    def get_all(self, ph):
        sql = """SELECT name from customers WHERE cf='%s'""" % ph
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            name_of_pharma = cursor.fetchone()
        except (Exception, psycopg2.DatabaseError) as e:
            return 'Error'
        requester = name_of_pharma
        sql = """SELECT COUNT(*) id_ FROM reporting"""
        cursor.execute(sql)
        number_of_reporting = cursor.fetchone()
        return_me = {'Number': number_of_reporting}
        return return_me

    def get_all_(self, condition):
        all_sweet_data = []
        cursor = self.connection.cursor()
        tables = ['patient', 'reaction', 'reporting', 'risk', 'vaccination']
        if condition == 'all':
            i = 0
            for table in tables:
                sql = """SELECT * FROM %s""" % table
                cursor.execute(sql)
                data = cursor.fetchall()
                all_sweet_data.append(data)
            my_pretty_database = {
                'patient': all_sweet_data[0],
                'reaction': all_sweet_data[1],
                'reporting': all_sweet_data[2],
                'risk': all_sweet_data[3],
                'vaccination': all_sweet_data[4]
            }
            return my_pretty_database

        elif condition == 'patient':
            sql = """select doctor, id_, previous_vaccination, is_smoker, is_fatty, is_hyper, is_cardioonco, 
            previous_vaccination from patient ORDER BY doctor"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'patient_order_by_vaccination':
            sql = """select previous_vaccination, doctor, is_smoker, is_fatty, is_hyper, is_cardioonco from patient ORDER BY doctor"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'criticality':
            sql = """select patient, doctor, adv_reaction, reaction_date, vaccination_carried_out from reporting"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'vacc':
            sql = """select vaccination_carried_out, patient, doctor, adv_reaction, reaction_date from reporting"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'risk':
            sql = """select risk_level, patient from risk order by risk_level"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'vaccination_info':
            sql = """select patient, vaccination, dose, site, doctor, vaccination_date from vaccination ORDER by patient"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'vaccination_info_':
            sql = """select site, vaccination, vaccination_date from vaccination ORDER by site"""
            data = self.query_to_database(sql)
            return jsonify(data)

        elif condition == 'order_by_vaccination_risks':
            vaccination_array = []
            sql = """select count(id_), vaccination_carried_out from reporting group by vaccination_carried_out"""
            data = self.query_to_database(sql)
            for data_ in data:
                vaccination_array.append(data_)
            all_my_vaccinations = {'Vaccinazioni': vaccination_array}
            return all_my_vaccinations

    def query_to_database(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def get_reactions(self, doctor: str) -> json:
        sql = """SELECT * from reporting WHERE doctor='%s'""" % doctor
        cursor = self.connection.cursor()
        reaction_dictionary = {}
        all_patient = []
        all_reactions = []
        all_date = []
        all_vaccination = []
        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            if results is None:
                return None
            else:
                for result in results:
                    patient = result[1]
                    reaction = result[2]
                    reaction_date = str(result[3])
                    vaccination = result[5]
                    all_patient.append(patient)
                    all_reactions.append(reaction)
                    all_vaccination.append(vaccination)
                    all_date.append(reaction_date)

            reaction_dictionary = {
                'pazienti': all_patient,
                'reazioni': all_reactions,
                'date': all_date,
                'vaccinazioni': all_vaccination
            }

        except (Exception, psycopg2.DatabaseError) as e:
            reaction_dictionary = {}
            print(Fore.RED + str(e))
        finally:
            return reaction_dictionary

    def login(self, credential: json) -> json:
        name, surname = None, None
        password = credential['password']
        password = self.get_password_hash(password)
        fiscal_code = credential['cf']
        # SQL injection
        sql = "SELECT name, surname, role FROM customers WHERE cf='%s' AND passwd='%s'" % (fiscal_code, password)
        # NO SQL injection
        # sql = "SELECT name, surname, role FROM customers WHERE cf=%s AND passwd=%s"
        cursor = self.connection.cursor()
        try:
            # NO SQL injection!
            # cursor.execute(sql, (fiscal_code, password))

            # YES SQL injection
            cursor.execute(sql)
            response = cursor.fetchone()
            self.connection.commit()
            if response is not None:
                name = response[0]
                surname = response[1]
                role = response[2]
                login_success = {'name': name,
                                 'surname': surname,
                                 'role': role}
                return login_success
            else:
                login_fail = {'name': 'Dati per l\'accesso invalidi',
                              'surname': 'Accesso negato'}
                return login_fail
        except (Exception, psycopg2.DatabaseError) as e:
            print(Fore.RED + str(e))

    async def check_database_instance(self) -> bool:
        try:
            cursor = self.connection.cursor()
            print(Fore.GREEN + 'PostgresSQL database version: ')

            # esecuzione dello statement
            cursor.execute('SELECT version()')

            # display
            db_version = cursor.fetchone()
            print(Fore.GREEN + str(db_version))
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False

    async def create_table(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            print(Fore.RED + str(e))

    @staticmethod
    def get_password_hash(password: str) -> str:
        hashed_passwd = hashlib.sha512(password.encode('utf-8')).hexdigest()
        return str(hashed_passwd)

    @staticmethod
    def calculate_sha1(word: str) -> str:
        hashed_pk = hashlib.sha1(word.encode('utf-8')).hexdigest()
        return str(hashed_pk)

    @staticmethod
    def extract_vaccinations(vaccinations: []) -> str:
        all_vaccinations = ''
        for vaccination in vaccinations:
            all_vaccinations += vaccination['vaccination'] + ' '
        return all_vaccinations
