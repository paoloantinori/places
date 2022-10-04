from homeassistant.const import (
    ATTR_GPS_ACCURACY,
    CONF_API_KEY,
    CONF_ICON,
    CONF_NAME,
    CONF_ZONE,
    Platform,
)

DOMAIN = "places"

# Defaults
DEFAULT_ICON = "mdi:map-marker-circle"
DEFAULT_OPTION = "zone, place"
DEFAULT_HOME_ZONE = "zone.home"
DEFAULT_MAP_PROVIDER = "apple"
DEFAULT_MAP_ZOOM = 18
DEFAULT_EXTENDED_ATTR = False
DEFAULT_SHOW_TIME = False

# Settings

TRACKING_DOMAINS = [
    str(Platform.DEVICE_TRACKER),
    str("person"),
    str(Platform.SENSOR),
    "variable",
]
TRACKING_DOMAINS_NEED_LATLONG = [
    str(Platform.SENSOR),
    "variable",
]
HOME_LOCATION_DOMAINS = [CONF_ZONE]

# Config
CONF_DEVICETRACKER_ID = "devicetracker_id"
CONF_HOME_ZONE = "home_zone"
CONF_OPTIONS = "options"
CONF_MAP_PROVIDER = "map_provider"
CONF_MAP_ZOOM = "map_zoom"
CONF_LANGUAGE = "language"
CONF_EXTENDED_ATTR = "extended_attr"
CONF_SHOW_TIME = "show_time"
CONF_YAML_HASH = "yaml_hash"
CONF_NATIVE_VALUE = "native_value"

# Attributes
ATTR_NATIVE_VALUE = "native_value"
ATTR_PREVIOUS_STATE = "previous_state"
ATTR_OPTIONS = CONF_OPTIONS
ATTR_STREET_NUMBER = "street_number"
ATTR_STREET = "street"
ATTR_CITY = "city"
ATTR_POSTAL_TOWN = "postal_town"
ATTR_POSTAL_CODE = "postal_code"
ATTR_REGION = "state_province"
ATTR_STATE_ABBR = "state_abbr"
ATTR_COUNTRY = "country"
ATTR_COUNTY = "county"
ATTR_FORMATTED_ADDRESS = "formatted_address"
ATTR_PLACE_TYPE = "place_type"
ATTR_PLACE_NAME = "place_name"
ATTR_PLACE_CATEGORY = "place_category"
ATTR_PLACE_NEIGHBOURHOOD = "neighbourhood"
ATTR_DEVICETRACKER_ID = "devicetracker_entityid"
ATTR_DEVICETRACKER_ZONE = "devicetracker_zone"
ATTR_DEVICETRACKER_ZONE_NAME = "devicetracker_zone_name"
ATTR_PICTURE = "entity_picture"
ATTR_LATITUDE_OLD = "previous_latitude"
ATTR_LONGITUDE_OLD = "previous_longitude"
ATTR_LATITUDE = "current_latitude"
ATTR_LONGITUDE = "current_longitude"
ATTR_MTIME = "last_changed"
ATTR_DISTANCE_FROM_HOME_KM = "distance_from_home_km"
ATTR_DISTANCE_FROM_HOME_M = "distance_from_home_m"
ATTR_DISTANCE_FROM_HOME_MI = "distance_from_home_mi"
ATTR_DISTANCE_TRAVELED_MI = "distance_traveled_mi"
ATTR_DISTANCE_TRAVELED_M = "distance_traveled_m"
ATTR_HOME_ZONE = "home_zone"
ATTR_HOME_LATITUDE = "home_latitude"
ATTR_HOME_LONGITUDE = "home_longitude"
ATTR_HOME_LOCATION = "home_location"
ATTR_LOCATION_CURRENT = "current_location"
ATTR_LOCATION_PREVIOUS = "previous_location"
ATTR_DIRECTION_OF_TRAVEL = "direction_of_travel"
ATTR_MAP_LINK = "map_link"
ATTR_FORMATTED_PLACE = "formatted_place"
ATTR_OSM_ID = "osm_id"
ATTR_OSM_TYPE = "osm_type"
ATTR_WIKIDATA_ID = "wikidata_id"
ATTR_OSM_DICT = "osm_dict"
ATTR_OSM_DETAILS_DICT = "osm_details_dict"
ATTR_WIKIDATA_DICT = "wikidata_dict"
ATTR_LAST_PLACE_NAME = "last_place_name"
ATTR_UPDATES_SKIPPED = "updates_skipped"
ATTR_INITIAL_UPDATE = "initial_update"
ATTR_JSON_FILENAME = "json_filename"
ATTR_IS_DRIVING = "is_driving"
ATTR_DISPLAY_OPTIONS = "display_options"


# Attribute Lists
CONFIG_ATTRIBUTES_LIST = [
    CONF_DEVICETRACKER_ID,
    CONF_API_KEY,
    CONF_OPTIONS,
    CONF_HOME_ZONE,
    CONF_NAME,
    CONF_MAP_PROVIDER,
    CONF_MAP_ZOOM,
    CONF_LANGUAGE,
    CONF_EXTENDED_ATTR,
    CONF_SHOW_TIME,
    CONF_ICON,
]
RESET_ATTRIBUTE_LIST = [
    ATTR_UPDATES_SKIPPED,
    ATTR_STREET_NUMBER,
    ATTR_STREET,
    ATTR_CITY,
    ATTR_POSTAL_TOWN,
    ATTR_POSTAL_CODE,
    ATTR_REGION,
    ATTR_STATE_ABBR,
    ATTR_COUNTRY,
    ATTR_COUNTY,
    ATTR_FORMATTED_ADDRESS,
    ATTR_PLACE_TYPE,
    ATTR_PLACE_NAME,
    ATTR_PLACE_CATEGORY,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_FORMATTED_PLACE,
    ATTR_MTIME,
    ATTR_MAP_LINK,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
    ATTR_WIKIDATA_ID,
    ATTR_OSM_DICT,
    ATTR_OSM_DETAILS_DICT,
    ATTR_WIKIDATA_DICT,
    ATTR_IS_DRIVING,
]
EXTRA_STATE_ATTRIBUTE_LIST = [
    ATTR_STREET_NUMBER,
    ATTR_STREET,
    ATTR_CITY,
    ATTR_POSTAL_TOWN,
    ATTR_POSTAL_CODE,
    ATTR_REGION,
    ATTR_STATE_ABBR,
    ATTR_COUNTRY,
    ATTR_COUNTY,
    ATTR_FORMATTED_ADDRESS,
    ATTR_PLACE_TYPE,
    ATTR_PLACE_NAME,
    ATTR_PLACE_CATEGORY,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_FORMATTED_PLACE,
    ATTR_LATITUDE_OLD,
    ATTR_LONGITUDE_OLD,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
    ATTR_DEVICETRACKER_ID,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DEVICETRACKER_ZONE_NAME,
    ATTR_HOME_ZONE,
    ATTR_PICTURE,
    ATTR_DISTANCE_FROM_HOME_KM,
    ATTR_DISTANCE_FROM_HOME_M,
    ATTR_DISTANCE_FROM_HOME_MI,
    ATTR_DISTANCE_TRAVELED_M,
    ATTR_DISTANCE_TRAVELED_MI,
    ATTR_MTIME,
    ATTR_LAST_PLACE_NAME,
    ATTR_LOCATION_CURRENT,
    ATTR_LOCATION_PREVIOUS,
    ATTR_HOME_LATITUDE,
    ATTR_HOME_LONGITUDE,
    ATTR_DIRECTION_OF_TRAVEL,
    ATTR_MAP_LINK,
    ATTR_GPS_ACCURACY,
    ATTR_OPTIONS,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
]
IMPORT_ATTRIBUTE_LIST = [
    ATTR_NATIVE_VALUE,
    ATTR_STREET_NUMBER,
    ATTR_STREET,
    ATTR_CITY,
    ATTR_POSTAL_TOWN,
    ATTR_POSTAL_CODE,
    ATTR_REGION,
    ATTR_STATE_ABBR,
    ATTR_COUNTRY,
    ATTR_COUNTY,
    ATTR_FORMATTED_ADDRESS,
    ATTR_PLACE_TYPE,
    ATTR_PLACE_NAME,
    ATTR_PLACE_CATEGORY,
    ATTR_PLACE_NEIGHBOURHOOD,
    ATTR_FORMATTED_PLACE,
    ATTR_LATITUDE_OLD,
    ATTR_LONGITUDE_OLD,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DEVICETRACKER_ZONE_NAME,
    ATTR_DISTANCE_FROM_HOME_KM,
    ATTR_DISTANCE_FROM_HOME_M,
    ATTR_DISTANCE_FROM_HOME_MI,
    ATTR_DISTANCE_TRAVELED_M,
    ATTR_DISTANCE_TRAVELED_MI,
    ATTR_MTIME,
    ATTR_LAST_PLACE_NAME,
    ATTR_LOCATION_CURRENT,
    ATTR_LOCATION_PREVIOUS,
    ATTR_DIRECTION_OF_TRAVEL,
    ATTR_MAP_LINK,
    ATTR_GPS_ACCURACY,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
    ATTR_WIKIDATA_ID,
    ATTR_OSM_DICT,
    ATTR_OSM_DETAILS_DICT,
    ATTR_WIKIDATA_DICT,
]
EVENT_ATTRIBUTE_LIST = [
    ATTR_PLACE_NAME,
    ATTR_MTIME,
    ATTR_LAST_PLACE_NAME,
    ATTR_DISTANCE_FROM_HOME_M,
    ATTR_DISTANCE_FROM_HOME_KM,
    ATTR_DISTANCE_FROM_HOME_MI,
    ATTR_DISTANCE_TRAVELED_M,
    ATTR_DISTANCE_TRAVELED_MI,
    ATTR_DIRECTION_OF_TRAVEL,
    ATTR_DEVICETRACKER_ZONE,
    ATTR_DEVICETRACKER_ZONE_NAME,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
    ATTR_LATITUDE_OLD,
    ATTR_LONGITUDE_OLD,
    ATTR_MAP_LINK,
    ATTR_OSM_ID,
    ATTR_OSM_TYPE,
]
EXTENDED_ATTRIBUTE_LIST = [
    ATTR_WIKIDATA_ID,
    ATTR_OSM_DICT,
    ATTR_OSM_DETAILS_DICT,
    ATTR_WIKIDATA_DICT,
]
