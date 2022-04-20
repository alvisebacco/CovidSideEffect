from manager.operator import DefensiveCode


class ModelCovid:

    @staticmethod
    def get_connection_status():
        return DefensiveCode().checking_connection()