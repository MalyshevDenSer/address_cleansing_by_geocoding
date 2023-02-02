from geopy import GoogleV3
import os
from dotenv import load_dotenv
from pprint import pprint
import openpyxl

load_dotenv()


wb_obj = openpyxl.load_workbook(os.getenv('PATH_TO_FILE'))
sheet_obj = wb_obj.active
source_row = sheet_obj['A']
google_geocoder = GoogleV3(api_key=os.getenv('GOOGLE_V3_API'), domain='maps.google.ru')

for i, cell in enumerate(source_row[1:], start=1):
    place = cell.value
    geocoded = google_geocoder.geocode(place)
    country = region = city = street = house_number = post_code = position = '!!!ERROR!!!'
    if geocoded is not None:
        for numb, info in enumerate(geocoded.raw['address_components']):
            if 'country' in info['types']:
                country = info['long_name']

    print(country)
