import datetime
import multiprocessing
import time

from pymongo import MongoClient

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection_1']

"""

"""


def mongo_insert_one():
    ret = collection.insert_one({
        'name': 'test python',
        'create_time': datetime.datetime.now(),
        'state': 0
    })

    print(ret)


def mongo_insert_many():
    ret = collection.insert_many([
        {
            'name': 'test %s' % n,
            'create_time': datetime.datetime.now(),
            'state': 0
        }
        for n in range(10000)
    ])
    print(ret)


if __name__ == '__main__':
    mongo_insert_many()
