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

    def post_new_user_to_server(self, obj: json):
        api_prefix = r'/api/covid/new_user/'
        api = self.endpoint + api_prefix
        request = requests.post(api, json=obj,
                                headers={"Content-Type": "application/json"})
        print(request.status_code)
