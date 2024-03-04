import setup  # noqa: F401
import os
from flask import Flask
from middleware import enforce_rate_limit
from routes.countries import countries_blueprint
import logging

app = Flask(__name__)

app.config['DEBUG'] = not os.getenv('FLASK_ENV') == 'production'

app.before_request(enforce_rate_limit)

app.register_blueprint(countries_blueprint, url_prefix='/countries')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    app.run(debug=True)
