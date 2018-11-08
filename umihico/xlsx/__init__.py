import xlsxwriter as _xlsxwriter
import xlrd as _xlrd


def load_xlsx(filename):
    xl_workbook = _xlrd.open_workbook(filename)
    xl_sheet = xl_workbook.sheet_by_index(0)
    nrows = xl_sheet.nrows
    ncols = xl_sheet.ncols
    rows = [[str(xl_sheet.cell(row_index, col_index).value)
             for col_index in range(0, ncols)] for row_index in range(0, nrows)]
    return rows


def to_xlsx(filename, list_of_list):
    workbook = _xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    for row_index, row in enumerate(list_of_list):
        for col_index, cell in enumerate(row):
            worksheet.write(row_index, col_index, cell)
    workbook.close()
