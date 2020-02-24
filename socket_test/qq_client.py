import socket
import json
import threading

client = socket.socket()
client.connect(('192.168.183.1', 8000))
user = "bobby1"
# 登录
login_template = {
    "action": "login",
    "user": user
}
client.send(json.dumps(login_template).encode('utf8'))
login_status = client.recv(1024).decode('utf8')
print("登录状态:{}".format(login_status))

get_user_template = {
    "action": "list_user"
}
client.send(json.dumps(get_user_template).encode('utf8'))
user_list = json.loads(client.recv(1024).decode('utf8'))
print("在线用户:{}".format(user_list))

offline_msg_template = {
    "action": "history_msg",
    "user": user,
}
client.send(json.dumps(offline_msg_template).encode('utf8'))
# 需要解析json
history_msge = json.loads(client.recv(1024).decode('utf8'))
print("历史消息:{}".format(history_msge))
#
# client close之后让这个线程也关闭
exit=False
def handle_client_recv():
    while True:
        if not exit:
            # 获取不到的时候，可能是client已经close了，这里就可以退出了
            if not exit:
                try:
                    recv_mage = client.recv(1024).decode('utf8')
                except:

                    break

                # 判断是接收的json还是普通的消息
                try:
                    recv_mage_json = json.loads(recv_mage)
                    print("接收到来自({})的消息:{}".format(recv_mage_json['from'], recv_mage_json['data']))
                except:
                    print(recv_mage)


def handle_client_send():
    while True:
        input_num = int(input("请选择操作:1.发消息,2.退出登录,3.获取在线用户\n"))
        if input_num != 1 and input_num != 2 and input_num != 3:
            print("输入错误，请重新输入")
            continue
        elif input_num == 1:
            to_user = input("请输入接收者:")
            messge = input("请输入消息内容:")
            send_data_template = {
                "action": "send_msg",
                "to": to_user,
                "from": user,
                "data": messge
            }
            client.send(json.dumps(send_data_template).encode('utf8'))
        elif input_num == 2:
            exit_template = {
                "action": "exit",
                "user": user
            }
            client.send(json.dumps(exit_template).encode('utf8'))
            # 关闭连接同时break退出
            exit=True
            client.close()
            break
        elif input_num == 3:
            client.send(json.dumps(get_user_template).encode('utf8'))


if __name__ == "__main__":
    th = threading.Thread(target=handle_client_send)
    thr = threading.Thread(target=handle_client_recv)
    th.start()
    thr.start()
