import time

from openpyxl import load_workbook

start = time.time()
wb = load_workbook("C:\\Users\\pc11\\Desktop\\check_system_test_data\\03.17数据.xlsx")

"""
    使用 openpyxl 利用 rows 取读取数据时， 返回每一行的数据， 以tuple 形式返回， 每一个cell 代表一个单元格数据
"""
sheet1 = wb['Sheet1']
print(time.time() - start)
for n in sheet1.rows:
    print(n[9].value, n[26].value, n[29].value, n[40].value, n[46].value)


print(time.time() - start)
