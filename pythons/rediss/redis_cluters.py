from rediscluter import StrictRedisCluter


REDIS_CLUSTER = [
    {'host': '192.168.110.128', 'port': '7000'},
    {'host': '192.168.110.128', 'port': '7001'},
    {'host': '192.168.110.128', 'port': '7002'},

]


"""
    TODO: redis cluster
    cluster 不支持事务
    cluster 不支持批量操作
    
    使用slot 的概念将数据分片， 65535
    每个node 承担一部分slot，所以每个node 应该保证HA。这样即使node 中master 不可用， 其它slave可以主动承担node slot 的作用范围
"""

# cluster 和普通的客户端没有什么区别
redis_cluster = StrictRedisCluter(REDIS_CLUSTER)
