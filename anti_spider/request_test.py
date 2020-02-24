import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "acw_tc=76b20f4415801414025714165e36a2ffec26eb115f3115e2662fc6b722e3a4; __51cke__=; acw_sc__v2=5e2f0b90b408a6616d670feeefb26a553938a2ae; acw_sc__v3=5e2f0b9076935b9278930913e54874eff70278de; ASPSESSIONIDAGCRTRCC=EDMNBKHDGOPPFMHCLFHDLHLL; __tins__16949115=%7B%22sid%22%3A%201580141403196%2C%20%22vd%22%3A%2010%2C%20%22expires%22%3A%201580143774347%7D; __51laig__=10; Hm_lvt_80f407a85cf0bc32ab5f9cc91c15f88b=1580141406,1580141975; Hm_lpvt_80f407a85cf0bc32ab5f9cc91c15f88b=1580141975",
    "Host": "www.zdaye.com",
    "Referer": "https://www.zdaye.com/",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

url = 'https://www.zdaye.com/dayProxy/ip/318617.html'

if __name__ == '__main__':
    res = requests.get(url, headers=headers,verify=False)
    # 以下两种方式都可以改变编码方式，在html里的搜索charset属性，可以看到编码方式
    # res.encoding='utf-8'
    # print(res.text)

    print(res.content.decode("utf8"))
