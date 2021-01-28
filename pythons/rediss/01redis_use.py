import redis


"""
    redis 内存型数据库, 内部业务线程为单线程处理， 天生线程安全
"""

rds = redis.StrictRedis(port=6378)

# test
rds.set("python", 'test')
print(rds.get('python'))