from redis import StrictRedis


redis = StrictRedis()


class Ranking:

    def __init__(self, rds: StrictRedis):
        self._rds = rds

    def add_ranking(self, key, value, scope):
        pass

    def get_ranking(self, key, value):
        pass
