import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_V3_API = os.getenv('GOOGLE_V3_API')
YANDEX_API = os.getenv('YANDEX_API')
PATH_TO_FILE = os.getenv('PATH_TO_FILE')
MAP_GEOCODER = os.getenv('MAP_GEOCODER')

# keys to parse each item of address in different systems

GOOGLE_KEYS = {'nested_dict': ['address_components'],
               'item': 'types',
               'value': 'long_name',
               'country': 'country',
               'city': 'locality',
               'region': 'administrative_area_level_1',
               'house_number': 'street_number',
               'street': 'route',
               'postal_code': ['formatted_address']
               }

YANDEX_KEYS = {'nested_dict': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'Components'],
               'item': 'kind',
               'value': 'name',
               'country': 'country',
               'city': 'locality',
               'region': 'province',
               'house_number': 'house',
               'street': 'route',
               'postal_code': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'postal_code']
               }
