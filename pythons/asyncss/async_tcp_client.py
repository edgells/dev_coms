import asyncio
import logging
import random
import multiprocessing

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("asyncio")


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )

    print(f"send: {message}")
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()} \r')

    print('close the connection')
    writer.close()


if __name__ == '__main__':
    asyncio.run(tcp_echo_client("hello world!"))
