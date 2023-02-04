import os

from dotenv import load_dotenv

import google_geocoding
import worksheet

load_dotenv()

GOOGLE_V3_API = os.getenv('GOOGLE_V3_API')
PATH_TO_FILE = os.getenv('PATH_TO_FILE')

wb = worksheet.open_wb(PATH_TO_FILE)
address_sheet = wb.active
google_geocoding.google_geocode(address_sheet)
worksheet.save_wb(wb)
