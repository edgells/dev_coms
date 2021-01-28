import os
import sys


def main():
    try:
        for _ in range(10000):
            print("y")

            sys.stdout.flush()

    except BrokenPipeError:
        pass


if __name__ == '__main__':
    main()