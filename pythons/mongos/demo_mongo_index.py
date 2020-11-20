from pymongo import MongoClient
from pymongo import ASCENDING

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection_1']


def mongo_create_index():
    # create single index
    collection.create_index([('name', 1)], unique=True)

    # # create compound index
    # collection.create_index({
    #     'name': 1,
    #     'create_time': 1
    # })


if __name__ == '__main__':
    print(list(collection.index_information()))

    mongo_create_index()
    print(list(collection.index_information()))

