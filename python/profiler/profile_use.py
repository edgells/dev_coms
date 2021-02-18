import cProfile, pstats, io
from pstats import SortKey

pr = cProfile.Profile()


def profile_state(func):
    def wraps(num):
        pr.enable()
        ret = func(num)
        pr.disable()

        return ret

    return wraps


@profile_state
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


dl = [n for n in fib(1000)]
# print()

s = io.StringIO()

sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
pr.print_stats()
print(s.getvalue())
