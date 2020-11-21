from pymongo import MongoClient
from bson.son import SON
from bson.json_util import dumps
import datetime

mongo = MongoClient()

db = mongo['test_dev']
collection = db['test_dev_collection_cookie']

ret = collection.find({'state': 1}).limit(69).skip(50)
print((dumps(ret)))
