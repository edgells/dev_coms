from pymongo import MongoClient

client = MongoClient()
db = client['test_dev']
collection = db['test_dev_collection']


def add_batch_cookie():
    cookies = {
        'type'
    }




