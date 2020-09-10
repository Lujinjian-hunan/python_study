import xlrd
book = xlrd.open_workbook('students.xlsx')

# sheet = book.sheet_by_index(0)
sheet = book.sheet_by_name('sheet1')
print(book.sheets())  # 所有的sheet页，返回的是一个list，list里面就是每个sheet对象

for s in book.sheets():
    print(s.row_values(2))  # 获取第三行的数据

print(sheet.cell(0,0).value)   # 获取第一个单元格的数据

print(sheet.row_values(0))  # 获取第一行的数据
print(sheet.row_values(1))  # 获取第二行的数据

print(sheet.col_values(0))  # 获取第一列的数据
print(sheet.col_values(1))  # 获取第二列的数据

print(sheet.nrows)  # 打印行数
print(sheet.ncols)  # 打印列数
