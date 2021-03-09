import time

from openpyxl import load_workbook

start = time.time()
wb = load_workbook("C:\\Users\\pc11\\Desktop\\data.xlsx")


sheet1 = wb['Sheet1']
print(time.time() - start)
for n in sheet1[1:1000]:
    print(n)


print(time.time() - start)
