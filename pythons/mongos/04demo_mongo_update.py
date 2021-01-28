import time

from pymongo import MongoClient

client = MongoClient()
db = client['test_dev_db']
collection = db['test_dev_collection_cookies']


def add_batch_cookie():
    cookies = [{
        'name': 'cookie%d' % n,
        'state': 0
    }
        for n in range(1000)]

    collection.insert_many(cookies)


def update_cookie_by_id(ids=None, status=0):
    ret = collection.update_many(
        {'name': {'$in': ['cookie%d' % n for n in range(1000)]}},
        {'$set': {"state": 1}}
    )

    return ret


def test_update_cookie_by_id():
    ret = update_cookie_by_id()
    assert True, ret.acknowledged


if __name__ == '__main__':
    # add_batch_cookie()
    update_cookie_by_id()
