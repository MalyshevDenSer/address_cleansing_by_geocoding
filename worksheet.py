import openpyxl
from string import ascii_uppercase

def open_wb(path_to_file):
    wb_obj = openpyxl.load_workbook(path_to_file)
    # sheet_obj = wb_obj.active
    return wb_obj

def write_in_a_row(sheet, i, parsed_info):
    sheet[ascii_uppercase[1]][i].value = parsed_info['country']
    sheet[ascii_uppercase[2]][i].value = parsed_info['region']
    sheet[ascii_uppercase[3]][i].value = parsed_info['city']
    sheet[ascii_uppercase[4]][i].value = parsed_info['street']
    sheet[ascii_uppercase[5]][i].value = parsed_info['house_number']
    sheet[ascii_uppercase[6]][i].value = parsed_info['post_code']
    sheet[ascii_uppercase[7]][i].value = parsed_info['position']

def save_wb(wb):
    wb.save('result.xlsx')


# source_row = sheet_obj[ascii_uppercase[0]]
# country_row = sheet_obj[ascii_uppercase[1]]
# country_row[0].value = 'Страна'
# region_row = sheet_obj[ascii_uppercase[2]]
# region_row[0].value = 'Регион'
# city_row = sheet_obj[ascii_uppercase[3]]
# city_row[0].value = 'Город'
# street_row = sheet_obj[ascii_uppercase[4]]
# street_row[0].value = 'Улица'
# house_row = sheet_obj[ascii_uppercase[5]]
# house_row[0].value = 'Дом'
# postcode_row = sheet_obj[ascii_uppercase[6]]
# postcode_row[0].value = 'Индекс'
# position_row = sheet_obj[ascii_uppercase[7]]
# position_row[0].value = 'Координаты'