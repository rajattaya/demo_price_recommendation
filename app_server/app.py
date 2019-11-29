
from flask import Flask, jsonify, request
import json

from constants import static_constants
from price_analytics import  process_historic_data

from utils import api_util

app = Flask(__name__)

# specific_price_map, global_price_map = process_historic_data.create_price_map()


class InitializeUnitPrice:
    specific_price_map, global_price_map = process_historic_data.create_price_map()


@app.route('/')
def base_function():
    return "The price recommendation is up!"


@app.route('/price_recommendation', methods=['GET'])
def get_price_recommendation():
    response_dict = dict()
    try:
        code = 200
        request_args_dict = dict(request.args)
        is_valid, msg = api_util.validate_the_price_recommendation_request(request_args_dict)
        if is_valid:
            msg = "Recommended prices"
            specific_tuple, global_tuple, distance = api_util.get_data_tuple(request_args_dict)
            unit_price_dict = static_constants.UNIT_PRICE_DEFAULT
            if specific_tuple in InitializeUnitPrice.specific_price_map:
                unit_price_dict = InitializeUnitPrice.specific_price_map[specific_tuple]
            elif global_tuple in InitializeUnitPrice.global_price_map:
                unit_price_dict = InitializeUnitPrice.global_price_map[global_tuple]
            else:
                msg = "No data to recommend price"
            response_dict['lower_price'] = api_util.get_price(unit_price_dict['lower_price'], distance)
            response_dict['median_price'] = api_util.get_price(unit_price_dict['median_price'], distance)
            response_dict['higher_price'] = api_util.get_price(unit_price_dict['higher_price'], distance)
    except Exception as e:
        msg = "Error while getting recommended price"
        code = 503
        print(e)
    response_dict['response_code'] = code
    response_dict['msg'] = msg
    return jsonify(response_dict)


if __name__ == '__main__':
    app.run()
