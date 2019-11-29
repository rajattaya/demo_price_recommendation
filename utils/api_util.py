
from constants import static_constants
from constants.static_constants import PricingDataKeys as p_keys
from utils import common_util


def validate_the_price_recommendation_request(request_dict):
    is_valid, msg = True, "valid input"
    must_keys = {p_keys.SRC_CITY, p_keys.DST_CITY, p_keys.DISTANCE, p_keys.SHIPMENT_TYPE}
    request_keys = set(request_dict.keys())
    set_diff = must_keys - request_keys
    if set_diff:
        is_valid, msg = False, f"missing required keys: {set_diff}"
    else:
        shipment_type = str(request_dict[p_keys.SHIPMENT_TYPE])
        if shipment_type not in static_constants.VALID_SHIPMENT_TYPES:
            is_valid, msg = False, f"{shipment_type} not a valid shipment type"
        try:
            distance = float(request_dict[p_keys.DISTANCE])
        except Exception as e:
            is_valid, msg = False, "Not a valid distance"
    return is_valid, msg


def get_data_tuple(request_dict):
    """
    We can have a common function to  make a tuple from here and historic data.
    :param request_dict:
    :return:
    """
    src_dist = common_util.get_valid_consistent_string(request_dict.get(p_keys.SRC_SUB_DISTRICT))
    dst_dist = common_util.get_valid_consistent_string(request_dict.get(p_keys.DST_SUB_DISTRICT))
    src_city = common_util.get_valid_consistent_string(request_dict.get(p_keys.SRC_CITY))
    dst_city = common_util.get_valid_consistent_string(request_dict.get(p_keys.DST_CITY))
    shipment_type = common_util.get_valid_consistent_string(request_dict.get(p_keys.SHIPMENT_TYPE))
    shipper_id = common_util.get_valid_consistent_string(request_dict.get(p_keys.SHIPPER_ID))
    distance = float(request_dict[p_keys.DISTANCE])
    return (src_dist, dst_dist, src_city, dst_city, shipment_type, shipper_id), (shipment_type, shipper_id), distance


def get_price(unit_price, distance):
    if unit_price:
        return int(unit_price * distance)
    else:
        return None
