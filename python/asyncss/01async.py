import asyncio

# 获取事件循环
import time

loop = asyncio.get_event_loop()
loop.set_debug(True)


async def task():
    print("hello")
    await asyncio.sleep(1)
    print("world")


async def main():
    # 顺序执行任务
    tasks = await asyncio.gather(
        task(),
        task(),
        task(),
        task(),
        task(),

    )

# 运行一个完整的异步任务
print(f"started at {time.strftime('%X')}")
loop.run_until_complete(main())
print(f"end at {time.strftime('%X')}")
