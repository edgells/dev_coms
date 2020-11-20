from pymongo import MongoClient
from pymongo.database import Database
import datetime

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection']


def mongo_add_data(db: Database):
    cookies = [{
        'name': 'laowang%s' % n,
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow(),
        'state': 0,
    } for n in range(100)]

    posts = db.posts  # get collection
    post_id = posts.insert_many(cookies)
    ret = db.posts.find({})
    print(post_id.inserted_ids)
    print(len(post_id.inserted_ids))


if __name__ == '__main__':
    mongo_add_data(db)
