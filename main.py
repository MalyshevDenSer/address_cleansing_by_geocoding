import geocoding
import worksheet
from settings import geocoders, PATH_TO_FILE

# OOP
wb = worksheet.open_wb(PATH_TO_FILE)
address_sheet = wb.active
geocoding.geocode(address_sheet, geocoders)
worksheet.save_wb(wb)
