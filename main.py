import os

from dotenv import load_dotenv

import google_geocoding, yandex_geocoding
import worksheet

load_dotenv()

GOOGLE_V3_API = os.getenv('GOOGLE_V3_API')
YANDEX_API = os.getenv('YANDEX_API')
PATH_TO_FILE = os.getenv('PATH_TO_FILE')
MAP_GEOCODER = os.getenv('MAP_GEOCODER')


wb = worksheet.open_wb(PATH_TO_FILE)
address_sheet = wb.active
if MAP_GEOCODER == 'GOOGLE':
    google_geocoding.google_geocode(address_sheet, GOOGLE_V3_API)
elif MAP_GEOCODER == 'YANDEX':
    yandex_geocoding.yandex_geocode(address_sheet, YANDEX_API)
else:
    print(f"record to .env service (YANDEX OR GOOGLE) and its api")
worksheet.save_wb(wb)
