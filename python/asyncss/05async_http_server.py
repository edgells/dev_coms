import asyncio


async def handle(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle,
                                        port=8080
                                        )

    addr = server.sockets[0].getsockname()
    print("server on", addr)

    async with server:
        await server.serve_forever()


asyncio.run(main())