from geopy import Yandex
from pprint import pprint
from string import ascii_uppercase
from main import YANDEX_API, PATH_TO_FILE
import openpyxl
# YANDEX PARSER

wb_obj = openpyxl.load_workbook(PATH_TO_FILE)
address_sheet = wb_obj.active
source_column = address_sheet[ascii_uppercase[0]]
geocoder = Yandex(api_key=YANDEX_API)
country = region = city = street = house_number = post_code = position = 'NONE'

for i, cell in enumerate(source_column[1:], start=1):
    place = cell.value
    geocoded = geocoder.geocode(place)
    if geocoded is not None:
        for numb, info in enumerate(geocoded.raw['metaDataProperty']['GeocoderMetaData']['Address']['Components']):
            selected_block = info['kind']
            if 'country' in selected_block:
                country = info['name']
            if 'province' in selected_block:
                region = info['name']
            if 'street' in selected_block:
                street = info['name']
            if 'house' in selected_block:
                house_number = info['name']
            if 'locality' in selected_block:
                city = info['name']

            postal_code = geocoded.raw['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
            position = geocoded.raw['Point']['pos'].split()[1] + ' ' + geocoded.raw['Point']['pos'].split()[0]

    parsed_info = {'country': country,
                   'region': region,
                   'city': city,
                   'street': street,
                   'house_number': house_number,
                   'postal_code': postal_code,
                   'position': position}
    pprint(parsed_info)