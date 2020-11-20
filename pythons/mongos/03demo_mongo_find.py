from pymongo import MongoClient
from pymongo.database import Database
import datetime

mongo = MongoClient()

db = mongo['test_dev_db']
collection = mongo['test_dev_collection']


def mongo_db_list_all_data():
    print(db.list_collection_names())


def mongo_select_one_data():
    import pprint

    pprint.pprint(db.posts.find_one())


def mongo_select_find_one_data():
    import pprint

    pprint.pprint(db.posts.find_one({'author': 'test'}))


def mongo_find_by_id():
    import pprint

    post = db.posts.find_one({'author': 'test'})

    # id need  str converto obj

    from bson.objectid import ObjectId

    post_id = str(post['_id'])
    # print(post_id)
    post_id = ObjectId(post_id)
    # get by id
    post_dev = db.posts.find_one({'_id': post_id})

    print(post_dev)

    from pprint import pprint
    pprint(db.posts.find({'_id': post_id}).explain())


def mongo_doc_count():
    print(db.posts.count_documents({}))


if __name__ == '__main__':
    # mongo_add_data(db)
    mongo_find_by_id()
