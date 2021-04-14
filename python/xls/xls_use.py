import json
import os
import time
import pathlib

from openpyxl import load_workbook

start = time.time()
path = "C:\\Users\\pc11\\Desktop\\check_system_test_data\\03.21data.xlsx"
wb = load_workbook(path)

"""
    使用 openpyxl 利用 rows 取读取数据时， 返回每一行的数据， 以tuple 形式返回， 每一个cell 代表一个单元格数据
"""
sheet1 = wb['Sheet1']
print(time.time() - start)

good_list = []
follow_list = []
for n in sheet1[1:].rows:
    print(n[26].value, n[9].value, n[40].value, n[46].value)
    # continue
    # uid = n[40].value
    # print(type(uid))
    print(n[46].value)
    if n[29].value == "good":
        good = {
            'business': n[26].value,
            'uid': n[9].value,
            'create_time': n[46].value.strftime("%Y/%m/%d %H:%M:%S"),
        }

        good_list.append(good)

    elif n[29].value == "follow":
        follow = {
            'business': n[26].value,
            'uid': n[9].value,
            'create_time': n[46].value.strftime("%Y/%M/%D %h:%m:%s"),
        }

        follow_list.append(follow)

with open(os.path.dirname(path) + os.path.splitext(os.path.basename(path))[0] + ".good" + ".json", 'w')as f:
    json.dump(good_list, f)

with open(os.path.dirname(path) + os.path.splitext(os.path.basename(path))[0] + ".follow" + ".json", 'w')as f:
    json.dump(follow_list, f)

print(time.time() - start)
