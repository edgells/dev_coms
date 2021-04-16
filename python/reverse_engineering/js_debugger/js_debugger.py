import sys

def demo():
    print(sys._getframe().f_code.co_name)


if __name__ == '__main__':
    demo()