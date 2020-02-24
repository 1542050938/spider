# http socket 服务端
import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()


# sock:连接通道 addr:地址
def handle_sock(sock, addr):
    recvs = sock.recv(1024)
    print(recvs.decode('utf8'))
    # tem_input = input()
    http_template = """HTTP/1.1 200 OK

<html>
  <head>
    <title>Build A Web Server</title>
  </head>
  <body>
    Hello World, this is a very simple HTML document.
  </body>
</html>"""
    sock.send(http_template.encode("utf8"))


while True:
    sock, addr = server.accept()
    # 网页无法解析没有协议头的内容
    # sock.send("wellcome to server".encode("utf8"))
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
# 一次接收数 据的大小
# data = ""
# while True:
#     sock.send("wellcome to server".encode("utf8"))

# if recvs:
#     # 解密bytes到str
#     data += recvs.decode('utf8')
#     # if recvs.decode('utf8').endswith("#"):
#     #     break
# else:
#     break
# print(data)


# server.close()

