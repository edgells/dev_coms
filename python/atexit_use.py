import atexit

def test_func():
    print("program running is over")

atexit.register(test_func)