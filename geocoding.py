from string import ascii_uppercase
import worksheet
from collections import OrderedDict
from typing import Union
from openpyxl.worksheet.worksheet import Worksheet
from geopy.geocoders.yandex import Yandex
from geopy.geocoders.google import GoogleV3
from geopy.location import Location
from geopy.exc import GeopyError
from pprint import pprint
from time import sleep


def find_address_components(info: dict, keys: list) -> list:
    # print(info)
    for i in keys:
        # print('au')
        info = info.get(i)
    return info


def connect_to_api(geocoder: Union[Yandex, GoogleV3], place: str) -> Union[dict, None]:
    """Connectivity problems sometimes occur, so just in case, the script expects exceptions"""
    try:
        geocoded = geocoder.geocode(place)
        return geocoded
    except GeopyError as err:
        print('!' * 50)
        print(f'{type(err).__name__} is occured. Sleeping for 5 seconds.')
        sleep(5)
        print(f'Continuing. The address {place} is skipped')
        return None


def parsing_raw_data(data, keys, geocoder_type) -> OrderedDict:
    country = region = city = street = house_number = postal_code = None
    if data is not None:
        for info in find_address_components(data.raw, keys['nested_dict']):
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
            postal_code = find_address_components(data.raw, keys.get('postal_code'))
            if geocoder_type == 'google' and postal_code is not None:
                postal_code = postal_code[-6:]

    parsed_info = OrderedDict([
        ('country', country),
        ('region', region),
        ('city', city),
        ('street', street),
        ('house_number', house_number),
        ('postal_code', postal_code),
    ])
    pprint(parsed_info)
    return parsed_info


def geocode(sheet: Worksheet, geocoders: list[dict]) -> None:
    source_column = sheet[ascii_uppercase[0]]
    for i, cell in enumerate(source_column[1:], start=1):
        place = cell.value
        for geocoder in geocoders:
            raw_data = connect_to_api(geocoder['engine'], place)
            parsed_data = parsing_raw_data(raw_data, geocoder['keys'], geocoder['type'])
            if all(parsed_data.values()):
                worksheet.write_in_a_row(sheet, i, parsed_data)
                break
