import xlrd


workbook = xlrd.open_workbook("C:\\Users\\pc11\\Desktop\\test_data.xls")
worksheet = workbook.sheet_by_index(0)

print(worksheet.nrows)  # 总行数

for i in range(1, 1001):
    print(worksheet.cell_value(i, 26), end='\t')
    print(worksheet.cell_value(i, 39), end='\t')
    print(worksheet.cell_value(i, 45))
