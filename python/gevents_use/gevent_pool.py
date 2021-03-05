import os
import multiprocessing
import gevent
import gevent.pool
from gevent import monkey

monkey.patch_all()


def coroutine():
    while 1:
        pass


def main():
    pool = gevent.pool.Pool(100)
    gtask = [pool.spawn(coroutine()) for _ in range(100000)]
    gevent.joinall(gtask)


if __name__ == '__main__':
    tasks = []
    for n in range(10):
        process = multiprocessing.Process(target=main)
        tasks.append(process)
        process.start()

    for task in tasks:
        task.join()
