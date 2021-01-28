import asyncio
import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("asyncio")


async def say(delay):
    await asyncio.sleep(delay)
    print("say running ...")
    return random.randint(1, 10)


async def main():
    tasks = [asyncio.create_task(say(delay)) for delay in range(10)]
    # 可以根据指定等待时间， 进行任务等待
    done, pending = await asyncio.wait(tasks, timeout=2)
    print(done)
    print(pending)


if __name__ == '__main__':
    asyncio.run(main())
