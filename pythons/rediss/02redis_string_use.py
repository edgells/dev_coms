import redis
import datetime
import time

now = time.mktime(datetime.datetime.today().timetuple())

print(now)
rds = redis.StrictRedis(port=6378)

# ret1 = rds.setex("test", 10, "python")
# ret2 = rds.setex("test", 10, "python1")

# print(ret1)
# print(ret2)


ret = rds.setbit("user_id_123", 1, now)
print(ret)


def int_dec_inc():
    rds.set('python', 1)
    rds.decr('python'),
    print(rds.get('python'))


if __name__ == '__main__':
    int_dec_inc()
