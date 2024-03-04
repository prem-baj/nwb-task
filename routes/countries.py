from flask import request, jsonify, Blueprint
from database import countries_collection
from services.countries import compare_countries, CountryInfoNotFoundError, InvalidCriteriaError
import pymongo
import logging

countries_blueprint = Blueprint('countries', __name__)
logger = logging.getLogger(__name__)


@countries_blueprint.route('/<cca2>', methods=['GET'])
def get_country_info(cca2):
    try:
        country_info = countries_collection.find_one({'cca2': cca2})
        if country_info:
            country_info.pop("_id")
            return jsonify(country_info)
        else:
            return jsonify({'message': 'Country not found'}), 404
    except pymongo.errors.PyMongoError as e:
        logger.error(f'MongoDB error: {str(e)}')
        return jsonify({'message': 'An unexpected error occurred. Please try again later.'}), 500


@countries_blueprint.route('/compare', methods=['GET'])
async def get_compare_countries():
    country1 = request.args.get('country1')
    country2 = request.args.get('country2')
    criteria = request.args.get('criteria')

    try:
        result = await compare_countries(country1, country2, criteria)
        return jsonify(result)
    except CountryInfoNotFoundError as e:
        return jsonify({'message': str(e)}), 404
    except InvalidCriteriaError as e:
        return jsonify({'message': str(e)}), 400
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except pymongo.errors.PyMongoError as e:
        logger.error(f'MongoDB error: {str(e)}')
        return jsonify({'message': 'An unexpected error occurred. Please try again later.'}), 500
