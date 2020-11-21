from pymongo import MongoClient
from bson.son import SON
import datetime

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection_array']


def test_data():
    collection.insert_many([
        {"item": "journal",
         "qty": 25,
         "tags": ["blank", "red"],
         "dim_cm": [14, 21]},
        {"item": "notebook",
         "qty": 50,
         "tags": ["red", "blank"],
         "dim_cm": [14, 21]},
        {"item": "paper",
         "qty": 100,
         "tags": ["red", "blank", "plain"],
         "dim_cm": [14, 21]},
        {"item": "planner",
         "qty": 75,
         "tags": ["blank", "red"],
         "dim_cm": [22.85, 30]},
        {"item": "postcard",
         "qty": 45,
         "tags": ["blue"],
         "dim_cm": [10, 15.25]}])


def find_array():
    # cursor = collection.find({
    #     'tags': ['blank', 'red']
    # })

    # $all 包含指定数据元素的
    # cursor = collection.find({
    #     'tags': {
    #         '$all': ['red', 'blank']
    #     }
    # })

    # find array item
    # cursor = collection.find({'tags': 'red'})

    # multiple array elements range query or
    # cursor = collection.find({'dim_cm': {
    #     '$gt': 15, '$lt': 20
    # }})

    # multiple array elements range query and
    # cursor = collection.find({
    #     'dim_cm': {
    #         '$elemMatch': {'$gt': 25, '$lt': 30}
    #     }
    # })

    # array index item
    # cursor = collection.find({
    #     'dim_cm.1': {'$gt': 25}
    # })

    # array length
    # cursor = collection.find({
    #     'dim_cm': {'$size': 2}
    # })

    # list_dict_data = list(cursor)
    # print(list_dict_data)
    # print(len(list_dict_data))
    pass


if __name__ == '__main__':
    test_data()
    find_array()
