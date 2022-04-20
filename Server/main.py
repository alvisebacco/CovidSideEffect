# Server per il tracciamento degli effetti
# indesiderati delle vaccinazioni anti Covid-19

# Alvise Bacco
# 20/04/22

# Made with <3

try:
    from flask import Flask
    from flask_cors import CORS
except ImportError:
    raise ImportError('Import error')


def create_app():
    application = Flask(__name__)
    CORS(application)
    from api.apis import api_covid_side_effects
    application.register_blueprint(api_covid_side_effects(), url_prefix='/api')
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5006, use_reloader=False, debug=False)
