from redis import sentinel


"""
    TODO: 完成redis sentinel

    redis master/slave
    
    redis_sentinel conf    
    logfile /va/log/redis-sentinel.log
    daemonize yes
    port num
    bind ""
    sentinel monitor mymaster ip port 2
    sentinel 
    
"""

REDIS_SENTINELS = [
    ('127.0.0.1', '26379'),
    ('127.0.0.1', '26378'),
    ('127.0.0.1', '26377'),

]


REDIS_SENTINEL_SERVICE_NAME = 'mymaster'

_sentinel = sentinel.Sentinel(REDIS_SENTINELS)
redis_master = _sentinel.master_for(REDIS_SENTINEL_SERVICE_NAME)    # rw
redis_slave = _sentinel.slave_for(REDIS_SENTINEL_SERVICE_NAME)      # r

