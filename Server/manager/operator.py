class DefensiveCode:
    def __init__(self):
        print('[+] Checking connection...')

    @staticmethod
    def checking_connection():
        return 'Connesso'


class DatabaseOperations:
    def __init__(self):
        pass

    def post_new_user(self, new_user_data):
        print(new_user_data)
        return 'New user created!'

