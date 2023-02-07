from geopy import GoogleV3, Yandex
from string import ascii_uppercase
import worksheet

def find_address_components(gecoded_raw_data, keys):
    for i in keys:
        gecoded_raw_data = gecoded_raw_data.get(i)
    return gecoded_raw_data


def geocode(sheet, service, api):
    source_column = sheet[ascii_uppercase[0]]
    country = region = city = street = house_number = post_code = position = 'NONE'
    geocoder = None
    keys = None

    if service == 'google':
        geocoder = GoogleV3(api_key=api, domain='maps.google.ru')
        keys = {'nested_dict': ['address_components'],
                'address_item': 'types',
                'address_text': 'long_name'}
    elif service == 'yandex':
        geocoder = Yandex(api_key=api)
        keys = {'nested_dict': ['metaDataProperty', 'GeocoderMetaData', 'Address', 'Components'],
                'address_item': 'kind',
                'address_text': 'name'}
    else:
        print('wrong service, choose google or yandex')
        exit()

    for i, cell in enumerate(source_column[1:], start=1):
        place = cell.value
        geocoded = geocoder.geocode(place)
        if geocoded is not None:
            for info in find_address_components(geocoded.raw, keys['nested_dict']):
                selected_block = keys['address_item']
                if 'country' in selected_block:
                    country = info['address_text']
                if 'locality' in selected_block:
                    city = info['address_text']
                if 'administrative_area_level_1' in selected_block:
                    region = info['address_text']
                if 'street_number' in selected_block:
                    house_number = info['address_text']
                if 'route' in selected_block:
                    street = info['address_text']
                if 'postal_code' in selected_block:
                    post_code = info['address_text']
                position = str(geocoded.raw['geometry']['location']['lat']) + ' ' + str(
                    geocoded.raw['geometry']['location']['lng'])

        parsed_info = {'country': country,
                       'region': region,
                       'city': city,
                       'street': street,
                       'house_number': house_number,
                       'postal_code': post_code,
                       'position': position}
        worksheet.write_in_a_row(sheet, i, parsed_info)
