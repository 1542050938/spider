# http socket 客户端
# socket客户端

import socket

client = socket.socket()
# 域名可以代替ip
client.connect(('www.baidu.com', 80))
# 加密str到bytes
# tem_rec = client.recv(1024).decode('utf8')
# print("server response: {}".format(tem_rec))

if __name__ == '__main__':
    # tem_input = input()

    # 协议和版本之间有一个/
    # 每个字段后面也要加上\r\n
    # Connection: close关闭连接，这样才能停止接收数据
    client_template = "GET / HTTP/1.1\r\nConnection:close\r\n\r\n"
    client.send(client_template.encode('utf8'))
    data = b""
    while True:
        tem_rec = client.recv(1024)
        if tem_rec:
            data += tem_rec
        else:
            break
    # 接收完了再转码
    print(data.decode('utf8'))
    client.close()
