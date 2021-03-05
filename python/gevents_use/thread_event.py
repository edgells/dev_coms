import threading
import time

event = threading.Event()


def workerman(event):
    while 1:
        event.wait()
        print("this is thread:", threading.currentThread())


def main(event):
    event.set()

    # while 1:
    time.sleep(3)
    print("threading stop", threading.currentThread())
    event.clear()

    time.sleep(10)
    print("threading start")
    event.set()


if __name__ == '__main__':
    t1 = threading.Thread(target=workerman, args=(event,), name='worker')
    t2 = threading.Thread(target=workerman, args=(event,), name='worker')
    mainT = threading.Thread(target=main, args=(event,), name='main')
    # main()
    t1.start()
    t2.start()

    time.sleep(1)
    mainT.start()
    event.set()
    #
    # time.sleep(5)
    event.clear()
    t1.join()
    t2.join()
    mainT.join()
