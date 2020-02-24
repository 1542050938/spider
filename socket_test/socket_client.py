# socket客户端
import socket

client = socket.socket()
client.connect(('192.168.0.110', 8000))
# 加密str到bytes
tem_rec = client.recv(1024).decode('utf8')
print("server response: {}".format(tem_rec))

while True:
    tem_input = input()
    client.send(tem_input.encode('utf8'))
    tem_rec = client.recv(1024).decode('utf8')
    print("server response: {}".format(tem_rec))
client.close()
 