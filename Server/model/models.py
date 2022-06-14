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

    @staticmethod
    def post_patient(patient_data: json):
        return DatabaseOperations().post_new_patient(patient_data)

    @staticmethod
    def post_reaction(reaction: json):
        return DatabaseOperations().post_new_reaction(reaction)

    @staticmethod
    def post_vaccination(vaccination_data: json):
        return DatabaseOperations().post_new_vaccination(vaccination_data)

    @staticmethod
    def get_reactions(doctor):
        return DatabaseOperations().get_reactions(doctor)

    @staticmethod
    def get_all(pharma_cf):
        return DatabaseOperations().get_all(pharma_cf)

    @staticmethod
    def get_all_(condition):
        return DatabaseOperations().get_all_(condition)
