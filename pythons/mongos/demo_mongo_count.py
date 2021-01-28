from pymongo import MongoClient

cli = MongoClient()

db = cli['test_dev_db']
collection = db['test_dev_collection']

print(collection.count_documents({}))