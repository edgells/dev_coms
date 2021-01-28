from pymongo import MongoClient
from bson.son import SON
import datetime

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection_embedded']


def test_data():
    collection.insert_many([
        {"item": "journal",
         "qty": 25,
         "size": SON([("h", 14), ("w", 21), ("uom", "cm")]),
         "status": "A"},
        {"item": "notebook",
         "qty": 50,
         "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
         "status": "A"},
        {"item": "paper",
         "qty": 100,
         "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
         "status": "D"},
        {"item": "planner",
         "qty": 75,
         "size": SON([("h", 22.85), ("w", 30), ("uom", "cm")]),
         "status": "D"},
        {"item": "postcard",
         "qty": 45,
         "size": SON([("h", 10), ("w", 15.25), ("uom", "cm")]),
         "status": "A"}])


def find_embedded():
    # SON 要求完全匹配
    # cursor = collection.find({
    #     'size': SON([('h', 14), ('w', 21), ('uom', 'cm')])
    # })

    # nested field find
    # cursor = collection.find({'size.uom': 'in'})

    # query operator
    # cursor = collection.find({'size.uom': {'$in': ['cm', 'in']}})

    # list_dict_data = list(cursor)
    # print(list_dict_data)
    # print(len(list_dict_data))
    pass


if __name__ == '__main__':
    test_data()
    find_embedded()
