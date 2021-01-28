import asyncio
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG)


async def fact(name, number):
    for i in range(1, number + 1):
        print(f"task {name} compute fact ({i}")
        await asyncio.sleep(1)

    return random.randint(1, 10)


async def main():
    # 只是比create task 方便点， 并且， 并发任务结果会以列表形式返回
    result = await asyncio.gather(
        fact("demo1", 2),
        fact("demo2", 3),
        fact("demo3", 4),
    )
    print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(start)
    print(time.time())
