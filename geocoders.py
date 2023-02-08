from geopy import GoogleV3, Yandex
from string import ascii_uppercase
from settings import GOOGLE_V3_API, YANDEX_API, DEFAULT_KEYS, GOOGLE_KEYS, YANDEX_KEYS
import worksheet
from collections import OrderedDict


def find_address_components(dict_to_nest, keys):
    for i in keys:
        dict_to_nest = dict_to_nest.get(i)
    return dict_to_nest


def get_geocoder_data(service):
    geocoder = None
    keys = None

    if service == 'google':
        geocoder = GoogleV3(api_key=GOOGLE_V3_API, domain='maps.google.ru')
        keys = {l: GOOGLE_KEYS[k] for k, l in enumerate(DEFAULT_KEYS)}

    elif service == 'yandex':
        geocoder = Yandex(api_key=YANDEX_API)
        keys = {l: YANDEX_KEYS[k] for k, l in enumerate(DEFAULT_KEYS)}

    else:
        print('wrong service, choose google or yandex')
        exit()

    return keys, geocoder


def geocode(sheet, service):
    source_column = sheet[ascii_uppercase[0]]
    keys, geocoder = get_geocoder_data(service)
    country = region = city = street = house_number = postal_code = 'NONE'

    for i, cell in enumerate(source_column[1:], start=1):
        place = cell.value
        geocoded = geocoder.geocode(place)
        if geocoded is not None:
            for info in find_address_components(geocoded.raw, keys['nested_dict']):
                item = info[keys['item']]
                value = info[keys['value']]
                if keys['country'] in item:
                    country = value
                if keys['city'] in item:
                    city = value
                if keys['region'] in item:
                    region = value
                if keys['house_number'] in item:
                    house_number = value
                if keys['street'] in item:
                    street = value

                postal_code = find_address_components(geocoded.raw, keys.get('postal_code'))[-6:]

        parsed_info = OrderedDict([
            ('country', country),
            ('region', region),
            ('city', city),
            ('street', street),
            ('house_number', house_number),
            ('postal_code', postal_code),
        ])
        worksheet.write_in_a_row(sheet, i, parsed_info)
