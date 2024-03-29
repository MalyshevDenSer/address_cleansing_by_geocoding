import os

from dotenv import load_dotenv
from collections import OrderedDict
from geopy import GoogleV3, Yandex

# env variables

load_dotenv()

GOOGLE_V3_API = os.getenv('GOOGLE_V3_API')
YANDEX_API = os.getenv('YANDEX_API')
PATH_TO_FILE = os.getenv('PATH_TO_FILE')

# keys to parse each item of address in different APIs

DEFAULT_KEYS = OrderedDict([
    ('nested_dict', None),  # path to the address data in geocoder response
    ('item', None),  # block of info
    ('value', None),  # type of that block
    ('country', None),
    ('city', None),
    ('region', None),
    ('house_number', None),
    ('street', None),
    ('postal_code', None)  # path to postcode in geocoder response
])

GOOGLE_KEYS = (
    ('address_components',),
    'types',
    'long_name',
    'country',
    'locality',
    'administrative_area_level_1',
    'street_number',
    'route',
    ('formatted_address',)
)

YANDEX_KEYS = (
    ('metaDataProperty', 'GeocoderMetaData', 'Address', 'Components'),
    'kind',
    'name',
    'country',
    'locality',
    'province',
    'house',
    'street',
    ('metaDataProperty', 'GeocoderMetaData', 'Address', 'postal_code')
)

# priorities

PRIORITY_ORDER = ('google', 'yandex')

geocoders = list()
for service in PRIORITY_ORDER:
    if service == 'google':
        engine = GoogleV3(api_key=GOOGLE_V3_API, domain='maps.google.ru')
        keys = {l: GOOGLE_KEYS[k] for k, l in enumerate(DEFAULT_KEYS)}
        geocoders.append({'engine': engine, 'keys': keys, 'type': 'google'})

    elif service == 'yandex':
        engine = Yandex(api_key=YANDEX_API)
        keys = {l: YANDEX_KEYS[k] for k, l in enumerate(DEFAULT_KEYS)}
        geocoders.append({'engine': engine, 'keys': keys, 'type': 'yandex'})

    else:
        print('wrong service in variable PRIORITY_ORDER, choose google, yandex or add new geocoder info to settings.py')
        exit()
