import redis

"""
    redis geo operation
    add one item o(logN)
"""

rds = redis.StrictRedis(port=6378)

rds.geoadd("sicily", 13.361389, 38.115556, "palermo", 15.087269, 37.502669, "Catania")

rds.geopos('sicily', 'palermo')  # 返回指定集 member 经纬度

# 计算两个坐标之间的距离 o(logN) 极限下最大误差 5%
print(rds.geodist('sicily', 'palermo', 'Catania', unit='km'), 'km')

# 返回位置元素的hash 表示 o(logN)
print(rds.geohash("sicily", "palermo", 'Catania'))

# 返回给定坐标的半径item
print(rds.georadius("sicily", "palermo", 'Catania', ))