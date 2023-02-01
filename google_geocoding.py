from geopy import GoogleV3
import os
from dotenv import load_dotenv
from pprint import pprint
import openpyxl

load_dotenv()


wb_obj = openpyxl.load_workbook(os.getenv('PATH_TO_FILE'))
sheet_obj = wb_obj.active

source_row = sheet_obj['A']
for i, cell in enumerate(source_row[1:], start=1):
    place = cell.value
    print(place)

# google_geocoder = GoogleV3(api_key=os.getenv('GOOGLE_V3_API'), domain='maps.google.ru')
# # random_place = 'проспект Ленина, 18Б Центр район, Петрозаводск, 185035'
# geocoded = google_geocoder.geocode('проспект Ленина, 18Б Центр район, Петрозаводск, 185035')
# pprint(geocoded.raw['address_components'])
