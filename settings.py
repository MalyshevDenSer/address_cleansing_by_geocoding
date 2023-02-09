import os
from pprint import pprint

from dotenv import load_dotenv
from collections import OrderedDict

#




# env variables

load_dotenv()

GOOGLE_V3_API = os.getenv('GOOGLE_V3_API')
YANDEX_API = os.getenv('YANDEX_API')
PATH_TO_FILE = os.getenv('PATH_TO_FILE')
MAP_GEOCODER = os.getenv('MAP_GEOCODER')

# keys to parse each item of address in different systems

DEFAULT_KEYS = OrderedDict([
    ('nested_dict', None),
    ('item', None),
    ('value', None),
    ('country', None),
    ('city', None),
    ('region', None),
    ('house_number', None),
    ('street', None),
    ('postal_code', None)
])

GOOGLE_KEYS = (
    ['address_components'],
    'types',
    'long_name',
    'country',
    'locality',
    'administrative_area_level_1',
    'street_number',
    'route',
    ['formatted_address']
)

YANDEX_KEYS = (
    ['metaDataProperty', 'GeocoderMetaData', 'Address', 'Components'],
    'kind',
    'name',
    'country',
    'locality',
    'province',
    'house',
    'route',
    ['metaDataProperty', 'GeocoderMetaData', 'Address', 'postal_code']
)

keys = {l: GOOGLE_KEYS[k] for k, l in enumerate(DEFAULT_KEYS)}
