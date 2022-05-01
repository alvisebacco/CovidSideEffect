from manager.operator import DefensiveCode, DatabaseOperations
import json


class ModelCovid:

    @staticmethod
    def get_connection_status():
        return DefensiveCode().checking_connection()

    @staticmethod
    def post_new_user(new_user_data: json):
        return DatabaseOperations().post_new_user(new_user_data)

    @staticmethod
    def login(login_obj: json):
        return DatabaseOperations().login(login_obj)
