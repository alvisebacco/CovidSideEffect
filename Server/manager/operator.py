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
                print(self.username)
        except Exception as e:
            print(Fore.RED + '[ERROR] ' + str(e))

        try:
            self.connection = psycopg2.connect('host=' + self.host + ' '
                                               'port=' + self.port + ' '
                                               'dbname=' + self.database + ' '
                                               'user=' + self.username + ' '
                                               'password=' + self.password)

            print(Fore.GREEN + '[+] Connected to database: ', self.database)
        except (Exception, psycopg2.DatabaseError) as e:
            print(Fore.RED + str(e))

    async def check_and_create_tables(self):
        """ creo le tabelle se non esistono gia' """

        cursor = self.connection.cursor()
        table_user = r'Customers'
        column_name = r'Name'
        column_surname = r'Surname'
        column_pass = r'Passwd'
        column_role = r'Role'
        column_cf = r'CF'
        sql = "CREATE TABLE IF NOT EXISTS %s " \
              "(%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(50) NOT NULL, " \
              "%s varchar(128) NOT NULL, " \
              "%s varchar(50) PRIMARY KEY)" % (table_user, column_name, column_surname,
                                               column_role, column_pass, column_cf)
        try:
            cursor.execute(sql)
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as e:
            print(Fore.RED + str(e))

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
        #sql = "SELECT name, surname, role FROM customers WHERE cf=%s AND passwd=%s"
        cursor = self.connection.cursor()
        try:
            # NO SQL injection!
            #cursor.execute(sql, (fiscal_code, password))

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

    @staticmethod
    def get_password_hash(password: str) -> str:
        hashed_passwd = hashlib.sha512(password.encode('utf-8')).hexdigest()
        return str(hashed_passwd)
