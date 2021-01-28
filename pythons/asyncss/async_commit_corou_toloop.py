import asyncio
import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("asyncio")

"""
    先其它线程提交一个协程
"""


async def say(delay):
    await asyncio.sleep(delay)
    print("say running ...")
    return random.randint(1, 10)

# coro = asyncio.sleep(1, result=3)
# fut = asyncio.run_coroutine_threadsafe(coro, lo)

