import asyncio
import time


async def says(delay):
    await asyncio.sleep(delay)
    print("says running ...")


async def main():
    # 使用 task factory 创建人物， 如果不行， 使用 asyncio.Task 对象创建
    task1 = asyncio.create_task(
        says(1)
    )

    task2 = asyncio.create_task(
        says(2)
    )

    task3 = asyncio.create_task(
        says(2)
    )
    task4 = asyncio.create_task(
        says(2)
    )
    task5 = asyncio.create_task(
        says(5)
    )

    await task1
    await task2
    await task3
    await task4
    await task5


if __name__ == '__main__':
    print(time.time())
    asyncio.run(main())
    print(time.time())
