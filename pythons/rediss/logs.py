import requests
import threading

import pymongo

db = pymongo.MongoClient()['test_device_register']
collection = db['dy_multi']


def pressure_request():
    resp = requests.get('http://127.0.0.1:8080/device/batch/?business=play&device_num=50&user=fs&device_type=dy')
    print(resp.status_code, resp.json())


def restore_device():
    ret = collection.find().limit(1000)

    devices_id = [str(item['_id']) for item in ret]
    form_data = {
        'device_type': 'dy',
        'device_ids': devices_id
    }
    header = {
        'x-csrftoken': 'tARS8aed3SShDz8mrQ0hyNy1qihdKOG7RA2qSBAAgwLXNQbzMBnKVSoDCTBUV5Za'
    }
    resp = requests.post('http://127.0.0.1:8000/device/recovery/', data=form_data, headers=header)
    print(resp.content)


def main():
    task_que = []
    for _ in range(1000):
        task = threading.Thread(target=restore_device)
        task.start()
        task_que.append(task)

    for task in task_que:
        task.join()


if __name__ == '__main__':
    restore_device()
