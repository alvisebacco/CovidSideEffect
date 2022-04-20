from flask import Blueprint
from model.models import ModelCovid


def api_covid_side_effects():
    api_covid = Blueprint('covid_api', __name__)

    @api_covid.route('/covid/check_connection', methods=['GET'])
    def check_connection():
        return ModelCovid.get_connection_status()

    return api_covid
