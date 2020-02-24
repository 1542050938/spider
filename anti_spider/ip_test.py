# ! -*- encoding:utf-8 -*-
import requests


from scrapy import Selector
from fake_useragent import UserAgent

# 1.阿布云购买和使用动态ip请求网站
# 2.解析页面信息，获取job_list

ua=UserAgent()
headers={
    "User-Agent":ua.random
}
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

def get_html(url):


    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H6DMZTV0XGI8MYND"
    proxyPass = "4CEFD7B6954926AA"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    resp = requests.get(url, proxies=proxies,headers=headers)
    return resp.text

if __name__=='__main__':
    for i in range(2,31):
        url='https://www.lagou.com/zhaopin/Python/{}/?filterOption={}'.format(i,i)
        job_list_html=get_html(url)
        sel=Selector(text=job_list_html)
        job_list=sel.xpath("//div[@class='s_position_list ']//a[@class='position_link']/@href").extract()
        for job_url in job_list:
            try:
                job_html=get_html(job_url)
                job_sel=Selector(text=job_html)
                job_name=job_sel.xpath("//div[@class='position-head']//h1[@class='name']/text()").extract()[0]

                print(i,job_name)
            # 代理是随机的，但不能保不证重复，所以会被拉钩反爬拦住
            except Exception as e:
                print("下载失败")
                pass

    # print(job_list)

    pass

