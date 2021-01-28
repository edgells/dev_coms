import datetime



"""
时间戳
:param tp: unix 时间戳
:return: 字符串格式时间, 单位到秒
"""
dt = datetime.datetime.now().fromtimestamp(1605862749)
print(dt)
