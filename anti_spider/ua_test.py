

import requests
from fake_useragent import UserAgent
# 随机Aser_Agent
ua=UserAgent()
headers={
    "User-Agent":ua.random
}
res=requests.get("http://127.0.0.1:8000",headers=headers)
print(res.text)
pass

