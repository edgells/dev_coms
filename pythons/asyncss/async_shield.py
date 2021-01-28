import asyncio
import logging
import time
from asyncio import CancelledError, Future


async def hello(delay):
    await asyncio.sleep(delay)
    print("hello running...")


async def cancel_ft(fut: Future):
    fut.cancel()
    return


async def main():
    fut = asyncio.create_task(hello(2))

    await cancel_ft(fut)

    try:
        res = await asyncio.shield(fut)

    except CancelledError as e:
        print("cancel ")


if __name__ == '__main__':
    asyncio.run(main())
