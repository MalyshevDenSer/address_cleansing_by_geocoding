from geopy import GoogleV3, Yandex
from string import ascii_uppercase
from settings import GOOGLE_V3_API, YANDEX_API
import worksheet


def find_address_components(gecoded_raw_data, keys):
    for i in keys:
        gecoded_raw_data = gecoded_raw_data.get(i)
    return gecoded_raw_data


def get_geocoder_data(service):
    geocoder = None
    keys = None

    if service == 'google':
        geocoder = GoogleV3(api_key=GOOGLE_V3_API, domain='maps.google.ru')
        keys = {'nested_dict': ['address_components'],
                'item': 'types',
                'value': 'long_name',
                'country': 'country',
                'city': 'locality',
                'region': 'administrative_area_level_1',
                'house_number': 'street_number',
                'street': 'route',
                'postal_code': ['formatted_address']
                }

    elif service == 'yandex':
        geocoder = Yandex(api_key=YANDEX_API)
        keys = {'nested_dict': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'Components'],
                'item': 'kind',
                'value': 'name',
                'country': 'country',
                'city': 'locality',
                'region': 'province',
                'house_number': 'house',
                'street': 'route',
                'postal_code': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'postal_code']
                }

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

        parsed_info = {'country': country,
                       'region': region,
                       'city': city,
                       'street': street,
                       'house_number': house_number,
                       'postal_code': postal_code
                       }
        print(parsed_info)
        worksheet.write_in_a_row(sheet, i, parsed_info)
