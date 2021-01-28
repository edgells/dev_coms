import asyncio
import time


async def task1(delay):
    print("hello")
    await asyncio.sleep(delay)
    print("world")


async def main():
    await task1(1)
    await task1(2)
    await task1(2)      # 在协程函数内部调用其他的协程只是相当于函数调用而已， 不同的事会在底层将协程挂起

# asyncio.run 用来运行协程函数
print(time.time())
asyncio.run(main())

print(time.time())
