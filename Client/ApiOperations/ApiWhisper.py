import requests
import json


class ApiWhisper:
    def __init__(self):
        super().__init__()
        server = r'http://127.0.0.1'
        port = r'5006'
        self.endpoint = server + ':' + port

    def check_connection(self) -> bool:
        try:
            api_prefix = r'/api/covid/check_connection'
            api = self.endpoint + api_prefix
            request = requests.get(api)
            if request.status_code != 200:
                return False
            return True
        except Exception as e:
            print(e)

    def post_new_user_to_server(self, obj: json) -> bool:
        try:
            api_prefix = r'/api/covid/new_user/'
            api = self.endpoint + api_prefix
            request = requests.post(api, json=obj,
                                    headers={"Content-Type": "application/json"})
            if request.status_code == 200:
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def post_to_server(self, obj: json, api_prefix: str) -> tuple:
        try:
            api = self.endpoint + api_prefix
            request = requests.post(api, json=obj,
                                    headers={"Content-Type": "application/json"})
            if request.status_code == 200:
                response = request.text
                response = json.loads(response)
                server = response['Server']
                message = response['message']
                return server, message
        except Exception as e:
            print(e)

    def authenticate(self, obj: json) -> tuple:
        name = None
        surname = None
        role = None
        login_access = False
        try:
            api_prefix = f'/api/covid/login/'
            api = self.endpoint + api_prefix
            request = requests.post(api, json=obj,
                                    headers={"Content-Type": "application/json"})
            if request.status_code == 200:
                response = request.text
                response = json.loads(response)
                name = response['name']
                surname = response['surname']
                role = response['role']
                if surname != 'Accesso negato':
                    login_access = True
                return name, surname, role, login_access
        except Exception as e:
            print(e)
            return name, surname, role, login_access

    def get_reactions_from_doctor(self, api_prefix) -> json:
        request = 'Error'
        try:
            api = self.endpoint + api_prefix
            request = requests.get(api)
            request = json.loads(request.text)
        except Exception as e:
            print(e)
        finally:
            return request


