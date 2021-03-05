import httpx
import asyncio


async def tasks():
    async with httpx.AsyncClient() as client:
        res = await client.post("http://localhost:33801")
        print(res.text)


async def main():
    for _ in range(1000):
        loop.create_task(tasks())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
