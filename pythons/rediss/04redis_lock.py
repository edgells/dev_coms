import redis
import datetime
import time
import threading

from redis.exceptions import LockError


"""
    redis lock 相当于利用redis 实现的一个轻量级的分布式lock
"""


def rds_lock_test():
    rds = redis.StrictRedis(port=6378)
    """
        timeout: 指获取锁时的超时时间, 如果超过时间, 将会主动释放连接,导致lock 存在
    """
    try:
        # Cannot release a lock that's no longer owned 因为设置的超时时间
        with rds.lock('my-lock-key', timeout=1, blocking_timeout=5) as lock:
            print(threading.get_ident(), "拿到所了")
            time.sleep(5)
            pass
            print("释放锁")

    except LockError as e:
        print(e)


if __name__ == '__main__':
    task1 = threading.Thread(target=rds_lock_test)
    task2 = threading.Thread(target=rds_lock_test)

    task1.start()
    task2.start()

    task1.join()
    task2.join()
