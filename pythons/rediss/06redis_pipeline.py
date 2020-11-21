import redis

rds = redis.StrictRedis(port=6378)

"""
    redis pipeline 
"""


rds.set('bing', 'baz')
# create pipeline
pipe = rds.pipeline()

pipe.set('foo', 'bar')
pipe.get('bing')
pipe.set('python', 123)
pipe.get('python')

print(pipe.execute())