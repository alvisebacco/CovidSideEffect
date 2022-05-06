import json
import psycopg2
from configparser import ConfigParser
from colorama import Fore
import hashlib


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
        column_severity = 'severity'
        column_description = 'description'
        column_reporting = 'reporting'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL)" % (table_reaction, column_severity, column_description, column_reporting)

        await self.create_table(sql)

    async def check_and_create_table_reporting(self):
        """ tabella di inserimento dei dati principali"""

        table_reporting = 'reporting'
        column_id = 'id_'
        column_patient = 'patient'
        column_adverse_reaction = 'adv_reaction'
        column_date_of_reaction = 'reaction_date'
        column_date_of_reporting = 'reporting_date'
        column_vaccination_carried_out = 'vaccination_carried_out'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL)" % (table_reporting, column_id, column_patient, column_adverse_reaction,
                                            column_date_of_reaction, column_date_of_reporting,
                                            column_vaccination_carried_out)
        await self.create_table(sql)

    async def check_and_create_table_risk(self):
        """tabella con i dati del rischio"""
        table_user = 'Risk'

        column_id = 'id_'
        column_description = 'Description'
        column_risk_level = 'Risk_level'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL)" % (table_user, column_id, column_description, column_risk_level)
        await self.create_table(sql)

    async def check_and_create_table_vaccination(self):
        """tabella con i dati dei vaccini"""
        table_vaccination = 'vaccination'
        column_id = 'id_'
        column_patient = 'patient'
        column_reporting = 'reporting'
        column_vaccination = 'vaccination'
        column_dose = 'dose'
        column_site = 'site'
        column_vaccination_date = 'vacciantion_date'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) PRIMARY KEY, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL)" % (table_vaccination, column_id, column_patient,
                                            column_reporting, column_vaccination,
                                            column_dose, column_site, column_vaccination_date)

        await self.create_table(sql)

    async def check_and_create_table_patient(self):
        """tabella con i dati del paziente"""

        table_patient = 'patient'
        column_id = 'id_'
        column_year_of_birth = 'date_of_birth'
        column_province_of_residence = 'province_residence'
        column_job = 'job'
        column_risk_factor = 'risk_factor'
        column_previous_vaccinations = 'previous_vaccination'
        column_doctor = 'doctor'

        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) PRIMARY KEY, " \
              "foreign key(doctor) REFERENCES customers(cf));" % (table_patient, column_job, column_risk_factor,
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
