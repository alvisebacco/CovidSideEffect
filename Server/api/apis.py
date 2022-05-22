from flask import Blueprint, request, jsonify
from model.models import ModelCovid


def api_covid_side_effects():
    api_covid = Blueprint('covid_api', __name__)

    @api_covid.route('/covid/check_connection', methods=['GET'])
    def check_connection():
        return ModelCovid.get_connection_status()

    @api_covid.route('/covid/new_user/', methods=['POST'])
    def new_user_registration():
        new_user_data = request.get_json()
        return ModelCovid.post_new_user(new_user_data)

    @api_covid.route('/covid/login/', methods=['POST'])
    def login():
        login_data = request.get_json()
        return ModelCovid.login(login_data)

    @api_covid.route('/covid/new_patient', methods=['POST'])
    def new_patient():
        patient_data = request.get_json()
        return ModelCovid.post_patient(patient_data)

    @api_covid.route('/covid/new_reaction/', methods=['POST'])
    def new_reaction():
        reaction_data = request.get_json()
        return ModelCovid.post_reaction(reaction_data)

    return api_covid
