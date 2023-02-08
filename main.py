import geocoders
import worksheet
from settings import PATH_TO_FILE, MAP_GEOCODER


wb = worksheet.open_wb(PATH_TO_FILE)
address_sheet = wb.active
geocoders.geocode(address_sheet, MAP_GEOCODER)
worksheet.save_wb(wb)
