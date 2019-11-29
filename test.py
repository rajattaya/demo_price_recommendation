import unittest

from app_server import app
from constants.static_constants import PricingDataKeys as p_keys, ShipmentTypes
from utils import api_util


class PriceRecommendationTest(unittest.TestCase):

    def assert_validation_response(self, request_dict, valid_bool):
        resp_bool, resp_msg = api_util.validate_the_price_recommendation_request(request_dict)
        self.assertEqual(resp_bool, valid_bool)

    def test_input_validation(self):
        """
        We can uncomment to check that the commented test case if failing
        """
        self.assert_validation_response({p_keys.SRC_CITY: "abc", p_keys.DST_CITY: "csde"}, False)
        # self.assert_validation_response({p_keys.SRC_CITY: "abc", p_keys.DST_CITY: "csde"}, True)
        self.assert_validation_response({p_keys.SRC_CITY: "abc", p_keys.DST_CITY: "csde", p_keys.DISTANCE: 1234,
                                         p_keys.SHIPMENT_TYPE: ShipmentTypes.W2W}, True)


if __name__ == '__main__':
    unittest.main()
