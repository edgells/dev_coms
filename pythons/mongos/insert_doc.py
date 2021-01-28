import pymongo
from bson import ObjectId

db = pymongo.MongoClient(
    host='192.168.100.186',
    port=27017
).device_register
db.authenticate('device_user', 'kyyfzx78..')

docs = db['api_doc']


def add_api_doc(get, post, types, func, req, req_params, resp):
    ret = docs.insert_one(
        {
            'GET': get,
            'POST': post,
            'type': types,
            '功能': func,
            '请求值实例': req,
            '请求参数': req_params,
            '返回值实例': resp,
        }
    )

    print(ret)


def update_api_doc(id, update_data):
    """
    更新api doc
    :param id:
    :param update_data:
        包含文档字段

    :return:
    """
    ret = docs.update_one(
        {'_id': ObjectId(id)},
        {'$set': update_data}
    )


def test_insert_api_doc():
    add_api_doc('http://server.lan:8080/cookie/hs/',
                '',
                'other',
                '批量获取抖音cookie',
                '?business=业务类型&cookie_num=50',
                'http://server.lan:8080/cookie/dy/',
                '{"data": "列表形式的token", "code": "0", "msg": "成功"}')


def test_update_api_doc():
    data = {
        '功能': '批量获取抖音cookie'
    }
    update_api_doc('5fc76a58363d47bf47b450e6', data)


if __name__ == '__main__':
    test_update_api_doc()
