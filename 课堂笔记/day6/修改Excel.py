from xlutils import copy
import xlrd

book = xlrd.open_workbook('students.xlsx')
sheet = book.sheet_by_index(0)

new_book = copy.copy(book)
copy_sheet = new_book.get_sheet(0)

for row in range(1, sheet.nrows-1):
    addr = sheet.cell(row, 2).value
    addr = addr.replace('beijing', '北京').replace('shanghai', '上海')
    copy_sheet.write(row,2,addr)

new_book.save('students.xlsx')
