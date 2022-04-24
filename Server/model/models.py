from manager.operator import DefensiveCode, DatabaseOperations


class ModelCovid:

    @staticmethod
    def get_connection_status():
        return DefensiveCode().checking_connection()

    @staticmethod
    def post_new_user(new_user_data):
        return DatabaseOperations().post_new_user(new_user_data)
