import asyncio
import time

"""
    
"""


async def main():
    def consuming(delay):
        time.sleep(delay)
        print("time consuming....")

    # 在不同一线程中， 执行 blocking code
    # TODO: 这里也可以直接使用 Thread 对象执行任务。
    ft = loop.run_in_executor(None, consuming, 5)
    ft1 = loop.run_in_executor(None, consuming, 5)
    ft2 = loop.run_in_executor(None, consuming, 5)
    ft3 = loop.run_in_executor(None, consuming, 5)
    ft4 = loop.run_in_executor(None, consuming, 5)
    await ft, ft1, ft2, ft3, ft4


if __name__ == '__main__':
    print(time.strftime("%X"))
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()      # Run the event loop until stop() is called.