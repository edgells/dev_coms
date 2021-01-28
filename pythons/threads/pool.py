import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

pool = ThreadPoolExecutor()


def print_time(delay):
    time.sleep(delay)
    print("%s running " % threading.currentThread().ident)


start = time.time()
for _ in range(10000):
    pool.submit(print_time, 0.1)

print(start)
print(time.time())

pool.shutdown(wait=True)  # 等待所有任务执行完成
