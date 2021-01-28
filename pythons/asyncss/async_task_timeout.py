import asyncio
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("asyncio")


async def eternity():
    await asyncio.sleep(3600)
    print("yes !")


async def main():
    try:
        await asyncio.wait_for(eternity(), timeout=1)

    except asyncio.TimeoutError as e:
        logger.info("task timeout")


if __name__ == '__main__':
    asyncio.run(main())