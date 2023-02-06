from geopy import Yandex
from pprint import pprint
from main import YANDEX_API
# YANDEX PARSER

place = "Москва, Скатертный переулок 2/7"
location_yan = Yandex(api_key=YANDEX_API).geocode(place)

pprint(location_yan.raw)

for numb, info in enumerate(location_yan.raw['metaDataProperty']['GeocoderMetaData']['Address']['Components']):
    selected_block = info['kind']
    if 'country' in selected_block:
        country = info['name']
    if 'province' in selected_block:
        province = info['name']
    if 'street' in selected_block:
        street = info['name']
    if 'house' in selected_block:
        street_number = info['name']
    if 'locality' in selected_block:
        city = info['name']
    postal_code = location_yan.raw['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
    position = location_yan.raw['Point']['pos'].split()[1] + ' ' + location_yan.raw['Point']['pos'].split()[0]
print(f'{street}, дом {street_number}, {city}, координаты: {position}, {country} {province} {postal_code}')