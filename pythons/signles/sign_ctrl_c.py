import signal
import time


def test(signum, frame):
    # 信号在命令行触发
    print('信号触发了')
    print(signum)
    print(frame)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, test)
    while 1:
        print('wait for signal')
        try:
            time.sleep(5)

        except InterruptedError:
            pass
