

RAW_DATA_PATH = 'static_data/historic_price_data.csv'


class HistoricDataKeys:
    SHIPPER = "Shipper"
    SRC_SUB_DISTRICT = "Origin Subdistrict"
    DST_SUB_DISTRICT = "Destination Subdistrict"
    SRC_CITY = "Origin City"
    DST_CITY = "Destination City"
    PRICE = "Transporter Pricing"
    SHIPMENT_TYPE = "Shipment Type"
    DISTANCE = "Distance"
    TRIP_STATUS = "Status"


class PricingDataKeys:
    SHIPPER_ID = "shipper_id"
    SRC_SUB_DISTRICT = "src_sub_district"
    DST_SUB_DISTRICT = "dst_sub_district"
    SRC_CITY = "src_city"
    DST_CITY = "dst_city"
    DISTANCE = "distance"
    UNIT_PRICE = "unit_price"
    SHIPMENT_TYPE = "shipment_type"


class ShipmentTypes:
    MT = "mt"
    GT = "gt"
    W2W = "w2w"


VALID_SHIPMENT_TYPES = {ShipmentTypes.MT, ShipmentTypes.GT, ShipmentTypes.W2W}
UNIT_PRICE_DEFAULT = {'lower_price': None, 'median_price': None, 'higher_price': None}
