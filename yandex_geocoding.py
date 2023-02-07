from geopy import Yandex
from string import ascii_uppercase
import worksheet


def yandex_geocode(sheet, yandex_api):
    source_column = sheet[ascii_uppercase[0]]

    geocoder = Yandex(api_key=yandex_api)
    country = region = city = street = house_number = postal_code = position = 'NONE'

    for i, cell in enumerate(source_column[1:], start=1):
        place = cell.value
        geocoded = geocoder.geocode(place)
        if geocoded is not None:
            for numb, info in geocoded.raw['metaDataProperty']['GeocoderMetaData']['Address']['Components']:
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
        worksheet.write_in_a_row(sheet, i, parsed_info)