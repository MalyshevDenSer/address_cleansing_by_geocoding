import openpyxl
from string import ascii_uppercase


def open_wb(path_to_file):
    wb_obj = openpyxl.load_workbook(path_to_file)
    return wb_obj


def write_in_a_row(sheet, i, parsed_info):
    sheet[ascii_uppercase[1]][i].value = parsed_info['country']
    sheet[ascii_uppercase[2]][i].value = parsed_info['region']
    sheet[ascii_uppercase[3]][i].value = parsed_info['city']
    sheet[ascii_uppercase[4]][i].value = parsed_info['street']
    sheet[ascii_uppercase[5]][i].value = parsed_info['house_number']
    sheet[ascii_uppercase[6]][i].value = parsed_info['postal_code']


def save_wb(wb):
    wb.save('result.xlsx')
