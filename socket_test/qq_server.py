# qq服务器
# 1.转发消息
# 2.处理登录
# 3.处理退出
# 4.维护历史消息，维护在线用户和用户连接

import socket
import json
from collections import defaultdict
import threading

server = socket.socket()

server.bind(('0.0.0.0', 8000))

server.listen()

online_user = defaultdict(dict)

user_megs = defaultdict(list)


def handle_information(sock, addr):
    while True:
        recvs = sock.recv(1024).decode('utf8')
        recvs_dict = json.loads(recvs)
        action=recvs_dict.get('action',"")
        if action == 'login':
            # defaultdict查找不到key时，会自动添加上这个key-velue
            online_user[recvs_dict['user']] = sock
            sock.send("登录成功".encode('utf8'))
        elif action == 'list_user':
            user_name = [user for user, online_sock in online_user.items()]
            sock.send(json.dumps(user_name).encode("utf8"))
        elif action == 'history_msg':
            if recvs_dict['user'] in user_megs:
                sock.send(json.dumps(user_megs[recvs_dict['user']]).encode("utf8"))
            else:
                # 如果没有的话,要传个空
                sock.send("[]".encode('utf8'))
        elif action == "send_msg":
            if recvs_dict['to'] in online_user:
                # 跟谁连接就发送给谁
                online_user[recvs_dict['to']].send(json.dumps(recvs_dict).encode("utf8"))
            # 历史消息不需要判断是否在线
            user_megs[recvs_dict['to']].append(recvs_dict)
        elif action == "exit":
            del online_user[recvs_dict['user']]
            # print(online_user)
            # sock.send("退出登录成功！".encode('utf8'))

# while True这样就不会关闭连接了
while True:
    sock, addr = server.accept()
    th = threading.Thread(target=handle_information, args=(sock, addr))
    th.start()
