import geocoding
import worksheet
from settings import PATH_TO_FILE

if __name__ == "__main__":
    wb = worksheet.open_wb(PATH_TO_FILE)
    address_sheet = wb.active
    geocoding.processing(address_sheet)
    worksheet.save_wb(wb)
