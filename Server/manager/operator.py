import json
import psycopg2
from configparser import ConfigParser
from colorama import Fore


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

    def post_new_user(self, new_user_data: json) -> str:
        """ inserisco i dati utente nel db """
        name = new_user_data['Nome']
        surname = new_user_data['Cognome']
        role = new_user_data['Ruolo']
        fiscal_code = new_user_data['CF']
        password = new_user_data['Password']

        sql = 'INSERT INTO Users (Nome) VALUES (%s), (Alfonso)'

        cursor = self.connection.cursor()
        cursor.execute(sql)
        _id = cursor.fetchone()[0]
        self.connection.commit()
        self.connection.close()
        return 'New user created!'

    def login(self, login: json) -> str:
        pass

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
