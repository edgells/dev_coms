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
    # 并发运行
    try:
        for ft in asyncio.as_completed(tasks, timeout=3):
            result = await ft
            print(result)

    except TimeoutError as e:
        logger.info("task timeout")

if __name__ == '__main__':
    asyncio.run(main())
