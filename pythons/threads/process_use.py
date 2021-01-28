import os
import time
from multiprocessing import Pool, Process


def f(x):
    while 1:
        print("current process %s" % os.getpid(), process.name)
        time.sleep(2)


def main():
    with Pool(5) as pool:
        print(pool.map(f, [1, 2, 3, 4]))


if __name__ == '__main__':
    process = Process(target=f, args=(2,), name="测试")
    process.start()
    process.join()
