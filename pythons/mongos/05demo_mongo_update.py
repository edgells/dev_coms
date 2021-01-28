import time

import pymongo
import redis

from pythons.loggers.loggers import logger

client = pymongo.MongoClient()
db = client['test_device_register']
collection = db['dy_multi']

rds = redis.StrictRedis(port=6378)
key = 'ky_executor_dy_play_device'
num = 10


# 批量获取device
def batch_device():
    # 同一批 device 同一时刻只能一个使用者获取 offset 解决
    # 获取同时， 需要将获取的 device used 更新为使用状态

    ret = rds.get(key)

    # first get device
    if ret is None:
        logger.info("first get device")
        rds.incrby(key, num)
        device_ret = collection.find({'used': 0}).limit(num)

        up_ret = batch_update_device(device_ret)
        logger.info(up_ret.raw_result)

        return device_ret

    else:

        # non first get device
        logger.info("non first get device")
        old_device_num = rds.incrby(key, num)
        # 不是第一次获取, 直接incr by offset
        device_ret = collection.find({'used': 0}).limit(num).skip(old_device_num)

        up_ret = batch_update_device(device_ret)
        logger.info(up_ret.raw_result)

        return device_ret


def batch_update_device(devices):
    device_ids = [item['_id'] for item in devices]
    ret = collection.update_many(
        {'_id': {"$in": device_ids}},
        {'$set': {'used': 1}}
    )

    if ret.matched_count != ret.modified_count or ret.matched_count != len(device_ids):
        logger.error("device update error")

    return ret


def batch_recv_device(devices_id):
    """
    批量更新设备使用状态
    :param devices_id:
    :return:
    """
    result = collection.update_many(
        {'_id': {'$in': devices_id}},
        {'$set': {'used': 0}}
    )

    return result


def restore_device_offset(devices):
    """
    还原设备的偏移量
    :param devices:
    :return:
    """
    devices_id = [item['_id'] for item in devices]
    device_num = len(devices_id)
    # restore device offset
    result = rds.incrby(key, device_num)
    return result


if __name__ == '__main__':
    ret = collection.find({'used': 1}).limit(10)

    def dict_str(item):
        item['_id'] = str(item['_id'])
        return item

    devices = [item['dv']['iid'] for item in ret]
    print(devices)
    print(time.time())
    ret = collection.update_many(
        {
            'dv.iid': {
                '$in': devices
            }
        },
        {
            "$set": {
                'used': 1
            }
        }
    )

    print(time.time())
    print(ret.matched_count)
    print(ret.modified_count)
