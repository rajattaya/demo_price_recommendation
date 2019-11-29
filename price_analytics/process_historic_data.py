from copy import deepcopy
from collections import defaultdict
import numpy as np
import pandas as pd

from constants import static_constants
from constants.static_constants import HistoricDataKeys as hist_keys
from utils import common_util


def get_raw_data_from_csv():
    """
    Read data from csv
    :return: dataFrame with raw price data
    """
    data_df = pd.read_csv(static_constants.RAW_DATA_PATH)
    return data_df


def get_valid_unique_tuple_for_data_and_price(data_dict):
    """
    Instead of print we can use a logger to log the error.
    :param data_dict:
    """
    is_valid, res_tuple, unit_price = True, (None, None, None, None, None, None), None
    try:
        src_sub_district = common_util.get_valid_consistent_string(data_dict[hist_keys.SRC_SUB_DISTRICT])
        dst_sub_district = common_util.get_valid_consistent_string(data_dict[hist_keys.DST_SUB_DISTRICT])
        src_city = common_util.get_valid_consistent_string(data_dict[hist_keys.SRC_CITY])
        dst_city = common_util.get_valid_consistent_string(data_dict[hist_keys.DST_CITY])
        price = int(str(data_dict[hist_keys.PRICE]).replace(",", ""))
        shipment_type = str(data_dict[hist_keys.SHIPMENT_TYPE])
        shipper_id = str(data_dict[hist_keys.SHIPPER])
        distance = float(data_dict[hist_keys.DISTANCE])
        unit_price = round(price / distance, 2)
        res_tuple = (src_sub_district, dst_sub_district, src_city, dst_city, shipment_type, shipper_id)
    except Exception as e:
        is_valid = False
        # print(e)
    return is_valid, res_tuple, unit_price


def get_cleaned_price_data(raw_price_df):
    """
    The processed data will be a map.
    Key for the map: tuple (src_sub_district, dst_sub_district, src_city, dst_city, shipment_type, shipper_id)
    value will be a list of price per km
    Global map: for shipment_type and shipment_type and shipper_id with value similar to the processed data map
    :param raw_price_df:
    """
    processed_data = defaultdict(list)
    global_map = defaultdict(list)
    for idx, data_dict in raw_price_df.iterrows():
        is_valid, res_tuple, unit_price = get_valid_unique_tuple_for_data_and_price(data_dict)
        if is_valid:
            processed_data[res_tuple].append(unit_price)
            shipment_type = str(data_dict[hist_keys.SHIPMENT_TYPE])
            shipper_id = str(data_dict[hist_keys.SHIPPER])
            global_map[(shipment_type, shipper_id)].append(unit_price)
            if shipper_id is not None:
                global_map[(shipment_type, None)].append(unit_price)
    return processed_data, global_map


def get_price_range_map(data_map):
    """
    Currently choosing the upper limit as 70 and lower limit as 40. Going further we change these limit based upon the
     result we get after suggestion and deal closer with the shipper.
    Taking range around median will help us to remove the outliers.
    :param data_map:
    """
    res_map = defaultdict(lambda: deepcopy(static_constants.UNIT_PRICE_DEFAULT))
    for key, list_of_price in data_map.items():
        list_of_price.sort()
        lower_price = np.percentile(list_of_price, 40)
        higher_price = np.percentile(list_of_price, 70)
        median_price = np.percentile(list_of_price, 50)
        res_map[key] = {'lower_price': lower_price, 'median_price': median_price, 'higher_price': higher_price}
    return res_map


def create_price_map():
    raw_data_df = get_raw_data_from_csv()
    processed_data_map, global_processed_data_map = get_cleaned_price_data(raw_data_df)
    processed_unit_price_map = get_price_range_map(processed_data_map)
    global_unit_price_map = get_price_range_map(global_processed_data_map)
    # print(global_unit_price_map)
    return processed_unit_price_map, global_unit_price_map


def main():
    create_price_map()


if __name__ == '__main__':
    main()
