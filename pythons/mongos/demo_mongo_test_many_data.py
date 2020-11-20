from pymongo import MongoClient, InsertOne, UpdateOne

cli = MongoClient()

db = cli['test_dev_db']
collection = db['test_dev_collection']


# # collection.insert_many([{'num': i} for i in range(1000)])
# print(collection.count_documents({}))
def test_update():
    pass