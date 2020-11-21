import redis

rds = redis.StrictRedis(port=6378)


# 返回服务器处理的命令
redis_monitor = rds.monitor()
redis_monitor.listen()