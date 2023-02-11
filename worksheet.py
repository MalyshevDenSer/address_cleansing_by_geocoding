import openpyxl
from string import ascii_uppercase
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from collections import OrderedDict


def open_wb(path_to_file: str) -> Workbook:
    wb_obj = openpyxl.load_workbook(path_to_file)
    return wb_obj


def write_in_a_row(sheet: Worksheet, i: int, parsed_info: OrderedDict) -> None:
    for letter, key in enumerate(parsed_info, start=1):
        sheet[ascii_uppercase[letter]][i].value = parsed_info[key]


def save_wb(wb: Workbook) -> None:
    print(type(wb))
    wb.save('result.xlsx')


