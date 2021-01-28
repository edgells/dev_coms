import json
import os
import random
import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor

import redis
import pymongo

"""
    invalid cookie 使用 redis queue 异步处理
    
"""

mongo = pymongo.MongoClient()
db = mongo['test_dev_db']
docs = db['test_dev_collection_cookies']


def publish():
    rds = redis.StrictRedis(port=6378)
    count = 0
    while count < 10:
        time.sleep(0.1)
        ret = rds.publish("invalid_cookies", json.dumps([random.randint(10, 100) for n in range(100)]))
        print(threading.get_ident(), "publish message", ret)
        count += 1


class InvalidCookieHandle:

    executor = ThreadPoolExecutor(thread_name_prefix="invalid_cookie_handle",
                                  max_workers=os.cpu_count() * 2 + 1)

    def __init__(self, redis_host='127.0.0.1', redis_port=6378):
        self.rds = redis.StrictRedis(host=redis_host, port=redis_port)
        self.subs = self.rds.pubsub()

        self.subs_init()

    def subs_init(self):
        self.subs.subscribe("invalid_cookies")

    def run(self):
        while 1:
            for message in self.subs.listen():
                if message['type'] != 'message':
                    print(message)
                    continue

                print(threading.get_ident(), "recv_message", )

                cookie_ids = json.loads(message['data'].decode())


def recv_message():
    invalid = InvalidCookieHandle()
    invalid.run()


if __name__ == '__main__':
    # push_task = threading.Thread(target=publish)
    recv_task = threading.Thread(target=recv_message)

    # push_task.start()
    recv_task.start()
    # push_task.join()
    recv_task.join()
