from pymongo import MongoClient
from bson.son import SON
from bson.json_util import dumps
import datetime

mongo = MongoClient()

db = mongo['test_device_register']
collection = db['user']

username = 'hp'
password = 'b5cbcebb956a14cce068a60487db783d'
ret = collection.find_one({'username': username, 'password': password})
print((ret))
