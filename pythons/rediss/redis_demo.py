
import redis

rds = redis.StrictRedis(port=6378, db=2)


ret = rds.get('ky_executor_paly_cookies')
print(ret)
print(int(ret))