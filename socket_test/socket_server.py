# socket服务端
import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()


# sock:连接通道 addr:地址
def handle_sock(sock, addr):
    recvs = sock.recv(1024)
    print(recvs.decode('utf8'))
    tem_input = input()
    sock.send(tem_input.encode("utf8"))

while True:
    sock, addr = server.accept()
    sock.send("wellcome to server".encode("utf8"))
    client_thread = threading.Thread(target=handle_sock ,args=(sock,addr))
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
server.close()
