import openpyxl
from string import ascii_uppercase


def open_wb(path_to_file):
    wb_obj = openpyxl.load_workbook(path_to_file)
    return wb_obj


def write_in_a_row(sheet, i, parsed_info):
    for letter, key in enumerate(parsed_info, start=1):
        sheet[ascii_uppercase[letter]][i].value = parsed_info[key]


def save_wb(wb):
    wb.save('result.xlsx')


