from pymongo import MongoClient
from pymongo.database import Database
import datetime

mongo = MongoClient()

db = mongo['test_dev_db']
collection = db['test_dev_collection_update']


# 查询单条
def find_one():
    print(collection.find_one())


# 查询集
def find_many():
    for doc in collection.find({}):
        print(doc)


# 查询操作符
def find_opr():
    """
    query operators
    $in, 在array 内 example: {'name': {'$in': ['python', 'mongodb', 'pymongo']}

    $expr, 字段比较 {'$expr': {'$eq': ['$state', 0]}}
    :return:
    """
    # $in
    # cursor = collection.find({'tags': {'$in': ['python', 'mongodb']}})
    # list_dict_data = list(cursor)
    # print(list_dict_data)
    # print(len(list_dict_data))

    # $expr field compare
    # cursor = collection.find({'$expr': {'$eq': ['$state', 1]}})
    # print(list(cursor))

    # $regex
    # $options i 不区分大小写 x 忽略所有的空白字符 s 允许 . 匹配所有的字符
    # cursor = collection.find({'tags': {'$regex': '^py.*'}})
    # print(list(cursor))

    # $all
    # cursor = collection.find({'tags': {'$all': ['python']}})
    # print(list(cursor))

    # $and
    # cursor = collection.find({'$and': [{'name': 'laowang0'}, {'tags': {'$in': ['python']}}]})

    # $or
    # cursor = collection.find({'$or': [{'name': 'laowang0'}, {'tags': {'$in': ['python']}}]})
    # print(list(cursor))

    # $and + $or
    # cursor = collection.find({
    #     'name': 'laowang0',
    #     '$or': [{'tags': {'$in': ['python', 'mongodb']}}]
    # })
    # print(list(cursor))

    #

if __name__ == '__main__':
    # mongo_add_data(db
    find_opr()
