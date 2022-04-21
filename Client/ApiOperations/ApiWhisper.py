import requests


class ApiWhisper:
    def __init__(self):
        super().__init__()
        server = r'http://127.0.0.1'
        port = r'5006'
        api_prefix = r'/api/covid/check_connection'
        self.endpoint = server + ':' + port + api_prefix

    def check_connection(self) -> bool:
        try:
            request = requests.get(self.endpoint)
            if request.status_code != 200:
                return False
            return True
        except Exception as e:
            print(e)
