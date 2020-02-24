import requests

params = {
    "username": "bobby哈",
    "password": "10086"
}

# res = requests.get("https://www.baidu.com/")
# print(res.text)
# 本地端口的话，要用http，加s的话，服务端utf8会解码不了
# 用data，服务器端接收的数据：username=bobby%E5%93%88&password=10086
# 用json，服务器端接收的数据：{"username": "bobby\\u54c8", "password": "10086"}
# res = requests.post("http://127.0.0.1:8000",data=params)
res = requests.post("http://127.0.0.1:8000",json=params)
print(res.json())
print(res.status_code)
