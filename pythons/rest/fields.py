from abc import ABCMeta


class MyAbcs(ABCMeta):
    pass

class MyAbc:
    pass


import sys

# 返回解释器
print(sys._debugmallocstats())
# 返回当前解释器已经分配的内存块数
print(sys.getallocatedblocks())

ab = MyAbc()
print(sys.getrefcount(ab))  # result + 1
print(sys.getsizeof('h'))   # obj size
print(sys.getswitchinterval())  # 返回线程 切换时间 0.05
print(sys.implementation)   # 
print(sys.modules)      # 显示已经加载的模块
