from pymongo import MongoClient
from pymongo.database import Database
import datetime

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection_update']




