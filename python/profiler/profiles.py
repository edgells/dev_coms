from pyinstrument import Profiler
from pyinstrument.renderers import ConsoleRenderer

profiler = Profiler()
profiler.start()


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


dl = [n for n in fib(10000)]

profiler.stop()

print(profiler.output_text(unicode=True, color=True))
# print(profiler.output(ConsoleRenderer()))
