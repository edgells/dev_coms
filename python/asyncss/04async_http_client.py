import asyncio


async def main(message):
    reader, writer = await asyncio.open_connection(
        host="127.0.0.1",
        port=8080
    )

    writer.write(message.encode())

    data = await reader.read(100)
    print(data.decode())

    writer.close()


asyncio.run(main("hello world"), debug=True)