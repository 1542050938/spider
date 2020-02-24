# socket服务端
import socket
import threading
import json

server = socket.socket()
# 绑定到0.0.0.0:8000端口上
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        # recv方法是阻塞的
        # 文件过大时，消息会接收不到，要*10
        tmp_data = sock.recv(1024*10)
       # 图片文件用utf8转码不了，会显示16进制？
        tmp_data = tmp_data.decode("utf8")
        request_line = tmp_data.splitlines()[0]
        if request_line:
            # 默认按空格区分
            method = request_line.split()[0]
            path = request_line.split()[1]
            if method == "GET":
                # if method == "POST":
                # enctype = "multipart/form-data 表单提交
                # enctype默认是x-www-form-urlencoded，不会解码中文字符
                # 跨域不报错：Access-Control-Allow-Origin: 客户端地址
                response_template = '''HTTP/1.1 200 OK
                
Access-Control-Allow-Origin: http://localhost:63342

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/" method="POST" enctype="multipart/form-data">
    <input type="text" name="name"/>
    <input type="password" name="password">
    <input type="file" name="file">
    <input type="submit" value="登录">
</form>

</body>
</html>

                '''
                sock.send(response_template.encode("utf8"))
                sock.close()
            elif method == "POST":
                # elif method == "GET":
                response_template = '''HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: http://localhost:63342

{}

        '''
                data = [
                    {
                        "name": "django打造在线教育",
                        "teacher": "bobby",
                        "url": "https://coding.imooc.com/class/78.html"
                    },
                    {
                        "name": "python高级编程",
                        "teacher": "bobby",
                        "url": "https://coding.imooc.com/class/200.html"
                    },
                    {
                        "name": "scrapy分布式爬虫",
                        "teacher": "bobby",
                        "url": "https://coding.imooc.com/class/92.html"
                    },
                    {
                        "name": "django rest framework打造生鲜电商",
                        "teacher": "bobby",
                        "url": "https://coding.imooc.com/class/131.html"
                    },
                    {
                        "name": "tornado从入门到精通",
                        "teacher": "bobby",
                        "url": "https://coding.imooc.com/class/290.html"
                    },
                ]
                sock.send(response_template.format(json.dumps(data)).encode("utf8"))
                sock.close()
                break


# 获取客户端连接并启动线程去处理
while True:
    # 阻塞等待连接
    sock, addr = server.accept()

    # 启动一个线程去处理新的用户连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
