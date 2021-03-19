import time

from pymongo import MongoClient

client = MongoClient(host="server.lan")

user = 'device_user'
password = 'kyyfzx78..'

db = client['device_register']
db.authenticate(user, password)


def create_index(collection, index_list: list):
    return db[collection].create_index(index_list)


if __name__ == '__main__':
    # indexs = [
    #     # ("used", -1),
    #     ("create_time", -1),
    # ]
    # print(create_index("dy_multi", indexs))
    # print(create_index("hs_multi", indexs))
    # print(create_index("gua_multi", indexs))
    # print(create_index("toutiao_multi", indexs))
    result = db['gua_multi'].find_one_and_update({"used": 0, "remark": {'$regex': 'laozhuo'}, "use_count": {"$lt": 3}}, {"$set": {"used": 1, "user": "deng", "get_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}})
    print(result)