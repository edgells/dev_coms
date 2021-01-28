import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect(('www.baidu.com', 80))
sock.close()

# socket 关闭了之后就不能再使用
sock.connect(("cn.vuejs.org", 443))
sock.close()