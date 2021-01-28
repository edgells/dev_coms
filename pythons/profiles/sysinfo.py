import sys

#

print(sys.thread_info)


import gc
print(gc.get_debug())
for obj in gc.get_objects():
    print(obj)


print(len(gc.get_objects()))

print(print(gc.get_stats()))

print(gc.get_count())

print(gc.get_threshold())