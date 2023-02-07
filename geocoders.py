from geopy import GoogleV3, Yandex
from string import ascii_uppercase
import worksheet


def find_address_components(gecoded_raw_data, keys):
    for i in keys:
        gecoded_raw_data = gecoded_raw_data.get(i)
    return gecoded_raw_data


def geocode(sheet, service, api):
    source_column = sheet[ascii_uppercase[0]]
    country = region = city = street = house_number = postal_code = position = 'NONE'
    geocoder = None
    keys = None

    if service == 'google':
        geocoder = GoogleV3(api_key=api, domain='maps.google.ru')
        keys = {'nested_dict': ['address_components'],
                'item': 'types',
                'text': 'long_name',
                'country': 'country',
                'city': 'locality',
                'region': 'administrative_area_level_1',
                'house_number': 'street_number',
                'street': 'route',
                'postal_code': {'postal_code': ['formatted_address']}
                }
    elif service == 'yandex':
        geocoder = Yandex(api_key=api)
        keys = {'nested_dict': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'Components'],
                'item': 'kind',
                'text': 'name',
                'country': 'country',
                'city': 'locality',
                'region': 'province',
                'house_number': 'house',
                'street': 'route',
                'postal_code': {'postal_code': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'postal_code']}
                }
    else:
        print('wrong service, choose google or yandex')
        exit()

    for i, cell in enumerate(source_column[1:], start=1):
        place = cell.value
        geocoded = geocoder.geocode(place)
        if geocoded is not None:
            for info in find_address_components(geocoded.raw, keys['nested_dict']):
                item = info[keys['item']]
                text = info[keys['text']]
                if keys['country'] in item:
                    country = text
                if keys['city'] in item:
                    city = text
                if keys['region'] in item:
                    region = text
                if keys['house_number'] in item:
                    house_number = text
                if keys['street'] in item:
                    street = text

                postal_code = find_address_components(geocoded.raw, keys.get('postal_code').get('postal_code'))[-6:]

        parsed_info = {'country': country,
                       'region': region,
                       'city': city,
                       'street': street,
                       'house_number': house_number,
                       'postal_code': postal_code,
                       'position': position}
        print(parsed_info)
        worksheet.write_in_a_row(sheet, i, parsed_info)
