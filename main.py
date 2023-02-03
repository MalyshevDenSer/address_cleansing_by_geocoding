from dotenv import load_dotenv

import os
import worksheet, google_geocoding

load_dotenv()
wb = worksheet.open_wb(os.getenv('PATH_TO_FILE'))
address_sheet = wb.active
google_geocoding.google_geocode(address_sheet)
worksheet.save_wb(wb)