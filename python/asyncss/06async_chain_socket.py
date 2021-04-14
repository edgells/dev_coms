import asyncio
import socket

# 向一个打开的socket 写入数据
async def main():
    loop = asyncio.get_event_loop()

    rsock, wsock = socket.socketpair()

    reader, writer = await asyncio.open_connection(sock=rsock)
    # 在 1秒后使用 wsock 发送数据
    loop.call_soon(wsock.send, "hello world old sock".encode())

    data = await reader.read(100)

    print(data.decode())

    writer.close()
    wsock.close()


asyncio.run(main())