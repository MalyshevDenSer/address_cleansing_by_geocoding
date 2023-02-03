from geopy import GoogleV3
import os
from dotenv import load_dotenv
from pprint import pprint
import openpyxl
from string import ascii_uppercase

load_dotenv()

wb_obj = openpyxl.load_workbook(os.getenv('PATH_TO_FILE'))
sheet_obj = wb_obj.active
source_row = sheet_obj[ascii_uppercase[0]]
country_row = sheet_obj[ascii_uppercase[1]]
country_row[0].value = 'Страна'
region_row = sheet_obj[ascii_uppercase[2]]
region_row[0].value = 'Регион'
city_row = sheet_obj[ascii_uppercase[3]]
city_row[0].value = 'Город'
street_row = sheet_obj[ascii_uppercase[4]]
street_row[0].value = 'Улица'
house_row = sheet_obj[ascii_uppercase[5]]
house_row[0].value = 'Дом'
postcode_row = sheet_obj[ascii_uppercase[6]]
postcode_row[0].value = 'Индекс'
position_row = sheet_obj[ascii_uppercase[7]]
position_row[0].value = 'Координаты'

google_geocoder = GoogleV3(api_key=os.getenv('GOOGLE_V3_API'), domain='maps.google.ru')

for i, cell in enumerate(source_row[1:], start=1):
    place = cell.value
    geocoded = google_geocoder.geocode(place)
    country = region = city = street = house_number = post_code = position = 'NONE'
    if geocoded is not None:
        for info in geocoded.raw['address_components']:
            selected_block = info['types']
            if 'country' in selected_block:
                country = info['long_name']
            if 'locality' in selected_block:
                city = info['long_name']
            if 'administrative_area_level_1' in selected_block:
                region = info['long_name']
            if 'street_number' in selected_block:
                house_number = info['long_name']
            if 'route' in selected_block:
                street = info['long_name']
            if 'postal_code' in selected_block:
                post_code = info['long_name']
            position = str(geocoded.raw['geometry']['location']['lat']) + ' ' + str(
                geocoded.raw['geometry']['location']['lng'])

    country_row[i].value = country
    position_row[i].value = position
    city_row[i].value = city
    region_row[i].value = region
    house_row[i].value = house_number
    street_row[i].value = street
    postcode_row[i].value = post_code

    raw_place = [country, region, city, street, house_number, post_code, position]
    print(' '.join(raw_place))
wb_obj.save('result.xlsx')
