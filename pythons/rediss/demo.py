import datetime
import threading
from concurrent.futures import ThreadPoolExecutor

import redis
import pymongo
import json

from bson import ObjectId


# 准备 db 和 rds
def state_env(mongo_settings: dict, redis_settings):
    db_name = mongo_settings.pop('db')
    username = mongo_settings.pop('user')
    password = mongo_settings.pop('password')

    db = pymongo.MongoClient(
        **mongo_settings
    )[db_name]
    db.authenticate(username, password)
    rds = redis.StrictRedis(**redis_settings)
    return db, rds


# 推送服务
class PublishServer:
    tag = ""

    def __init__(self, device_type, device_collection_name, rds, db):
        self.rds = rds
        self._device_type = device_type
        self.collection = db[device_collection_name]
        self.dy_device_key = "_".join(['ky_admin', 'executor', device_type, self.tag])

    def pop_item(self, device_num):
        pipe = self.rds.pipeline()
        for n in range(device_num):
            pipe.rpop(self.dy_device_key)

        result = pipe.execute()
        pipe.close()
        return result

    @staticmethod
    def id_to_ojb(value):
        return ObjectId(value)

    def push_item(self, month=1):
        """
        :param month: 1 代表一个月前的数据
        :return:
        """
        today = datetime.datetime.today()
        tt_day = today.replace(day=today.day - 10).strftime("%Y-%m-%d/%H:%M:%S")
        ret = self.collection.find({"create_time": {"$gt": tt_day}}).sort([("create_time", 1)])

        device_ids = []
        for item in ret:
            item['_id'] = str(item['_id'])
            print(item["_id"])
            device_ids.append(item['_id'])
            self.rds.lpush(self.dy_device_key, json.dumps(item))

        self.collection.update_many({"_id": {"$in": [item for item in map(self.id_to_ojb, device_ids)]}},
                                    {
                                        "$set": {
                                            "used": 0
                                        }
                                    })

    def get_total_device_num(self):
        return self.collection.find({}).count()

    def publish_device(self):
        self.push_item()
        print(self.dy_device_key, "push 结束")


class PublishDevice(PublishServer):
    tag = "device"


class PublishToken(PublishServer):
    tag = 'token'


def device_task(device_type, device_collection_name, rds, db):
    device = PublishDevice(device_type, device_collection_name, rds, db)
    device.publish_device()


def token_task(device_type, device_collection_name, rds, db):
    token = PublishToken(device_type, device_collection_name, rds, db)
    token.publish_device()


def main(mongo_collections):
    mongo_settings = {
        'host': '192.168.100.186',
        'port': 27017,
        'db': 'device_register',
        'user': 'device_user',
        'password': 'kyyfzx78..',
    }
    redis_settings = {
        'host': '192.168.100.186',
        'port': 6379,
        'db': 6
    }

    db, rds = state_env(mongo_settings,
                        redis_settings)
    task_que = []

    for device in mongo_collections.items():
        device_task(device[0], device[1], rds, db)


if __name__ == '__main__':
    mongo_collection = {
        'dy': 'dy_multi',
        'hs': 'hs_multi',
        'gua': 'gua_multi',
    }
    main(mongo_collection)
