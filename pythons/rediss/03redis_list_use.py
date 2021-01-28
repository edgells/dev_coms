import random

import redis

# create redis client
rds = redis.StrictRedis(port=6378)

rl = [random.randint(10, 100) for _ in range(100)]

ret = rds.lpush("invalid_cookie", *rl)

print(ret)