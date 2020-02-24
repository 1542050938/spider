# -*- coding: utf-8 -*-
import re
from urllib import parse
from datetime import datetime

import scrapy
from scrapy_test.models import *
from scrapy_test.items import *


# 1.命令行运行scrapy
#     可能需要下载依赖包pywin32
# 2.新建启动文件
# 3.把csdn的下载逻辑拿过来改造
#     1.数据库和包、全局变量
#     2.取html的部分scrapy已经帮我们做好了，不需要再用
#     3.调用的其他函数改成yeild回调函数
# 4.修改robot协议ROBOTSTXT_OBEY为False
# 5.把数据保存拆出去
#     1.item里定义类和数据格式
#     2.实例化item中的类，数据赋值，yeild该实例
#     3.setting中去掉pipeline的注释
#     4.item里定义save方法
#     5.pipeline中调用save方法并return
#     6.把需要设置默认值的都设置一下
# 6.统一加上user-agent中间件
# 7.统一加上ip代理的中间件
class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    # 由于可能爬取到外链url，不是这个域名的，不会被下载
    allowed_domains = ['csdn.net']

    domain = 'https://bbs.csdn.net/'
    domain_blog = 'https://blog.csdn.net/'
    # 起始urls，这是一个list,可以放多个url，对每一个进行下载，下载完成后再进行回调
    # start_urls = ['http://csdn.net/']
    start_urls = ['https://bbs.csdn.net/forums/ios']

    def parse(self, response):
        print("下载完成")

        # # 这里获取的是一个list,获取完的html第一个标签是xpath最后一个
        tbody = response.xpath(".//div[@class='forums_table_c']/table/tbody//tr")
        for tr in tbody:
            # xpath写的时候认真点，别写错了
            # 获取完还要把str转换成对应的类型
            # 注意哪些值会获取不到，且models里没有设置默认值
            # 获取到的详情页和作者页url记得加上domain，方法是parse.urljoin()
            # str转换成date:datetime.strptime()
            # xpath必须加上. 指的是当前路径，
            # xpath是直接拼接的，不加的话下面那段xpath实际直接拼接了上面的，变成//div[@class='forums_table_c']//tr//td[1]/span/text()，返回html下所有的status的list
            # topic = Topic()

            # TopicItem()实质是dict
            topic_item = TopicItem()
            if tr.xpath('.//td[1]/span/text()'):
                status = tr.xpath('.//td[1]/span/text()').extract()[0]
                # topic.status = status
                topic_item["status"] = status

            if tr.xpath('.//td[2]/em/text()'):
                score = tr.xpath('.//td[2]/em/text()').extract()[0]
                # topic.score = int(score)
                topic_item["score"] = int(score)

            if tr.xpath('.//td[3]/a/text()'):
                topic_title = tr.xpath('.//td[3]/a[last()]/text()').extract()[0]
                # topic.title = topic_title
                topic_item["title"] = topic_title
            if tr.xpath('.//td[3]/a/@href'):
                topic_url = parse.urljoin(self.domain, tr.xpath('.//td[3]/a[last()]/@href').extract()[0])
                topic_id = topic_url.split('/')[-1]
                # topic.id = int(topic_id)
                topic_item["id"] = int(topic_id)
            # author = tr.xpath('.//td[4]/a/text()').extract()[0]
            if tr.xpath('.//td[4]/a/@href'):
                author_url_info = tr.xpath('.//td[4]/a/@href').extract()[0]
                # parse.urljoin(domain_blog, tr.xpath('.//td[4]/a/@href').extract()[0])
                author_id = author_url_info.split('/')[-1]
                author_url = parse.urljoin(self.domain_blog, author_id)
                # topic.author = author_id
                topic_item["author"] = author_id
            if tr.xpath('.//td[4]/em/text()'):
                creat_time_str = tr.xpath('.//td[4]/em/text()').extract()[0]
                creat_time = datetime.strptime(creat_time_str, '%Y-%m-%d %H:%M')
                # topic.create_time = creat_time
                topic_item["create_time"] = creat_time
            if tr.xpath('.//td[5]/span/text()'):
                reply = tr.xpath('.//td[5]/span/text()').extract()[0]
                answer_nums = reply.split('/')[0]
                click_nums = reply.split('/')[1]
                # topic.answer_nums = int(answer_nums)
                topic_item["answer_nums"] = int(answer_nums)
                # topic.click_nums = int(click_nums)
                topic_item["click_nums"] = int(click_nums)
            if tr.xpath('.//td[6]/em/text()'):
                last_answer_time_str = tr.xpath('.//td[6]/em/text()').extract()[0]
                last_answer_time = datetime.strptime(last_answer_time_str, '%Y-%m-%d %H:%M')
                # topic.last_answer_time = last_answer_time
                topic_item["last_answer_time"] = last_answer_time
            topic_item["content"] = ""
            # save()默认方式是更新id，设置id为主键后，如果没有找到主键，数据会被过滤掉，需要加上force_insert=True 强制插入
            # existed_topics = Topic.select().where(Topic.id == topic.id)
            # if existed_topics:
            #     # 如果已经存在就更新
            #     topic.save()
            # else:
            #     # 不存在就插入
            #     topic.save(force_insert=True)
            yield topic_item

            # topic.save()
            # print("保存成功")

            # 获取详情和作者信息

            # parse_topic(topic_url, cookies_dict)
            # parse_author(author_url)
            yield scrapy.http.Request(url=topic_url, callback=self.parse_topic)
            yield scrapy.http.Request(url=author_url, callback=self.parse_author)
            # 获取下一页
            # next_page = sel.xpath("//a[@class='pageliststy next_page']/@href")
            # if next_page:
            #     next_page_url = parse.urljoin(domain,next_page.extract()[0])
            #     parse_list(next_page_url)
        next_page_class = response.xpath("//div[@class='page_nav']/a[last()]/@class").extract()
        if (next_page_class and next_page_class[0] == "pageliststy next_page"):
            next_page = response.xpath("//a[@class='pageliststy next_page']/@href")
            next_page_url = parse.urljoin(self.domain, next_page.extract()[-1])

            # parse_list(next_page_url, cookies_dict)
            yield scrapy.http.Request(url=next_page_url, callback=self.parse)

    def parse_topic(self, response):
        url = response.url
        topic = Topic()
        # topic_item = TopicItem()
        topic_id = url.split("/")[-1].split('?')[0]
        topic.id = int(topic_id)
        # topic_item["id"] = int(topic_id)
        topic_items = response.xpath(".//div[@class='mod_topic_wrap post topic']")
        if topic_items:
            content = topic_items.xpath(".//div[@class='post_body post_body_min_h']").extract()[0]
            # topic_item["content"] = content

            praised_nums_str = topic_items.xpath(".//label[@class='red_praise digg']/em/text()").extract()[0]
            praised_nums = int(praised_nums_str)
            # topic_item["praised_nums"] = praised_nums
            jtl_nums = 0

            jtl_str = topic_items.xpath(".//div[@class='close_topic']/text()").extract()[0]
            jtl = re.search("(\d+.\d+)", jtl_str)
            if jtl:
                jtl_nums = float(jtl.group(1))

            # topic_item["jtl"] = jtl_nums

            # yield topic_item
            # 如果topic_id存在的话再插入
            existed_topics = Topic.select().where(Topic.id == topic.id)
            if existed_topics:
                topic = existed_topics[0]
                topic.content = content
                topic.praised_nums = praised_nums
                topic.jtl = jtl_nums
                topic.save()

        answer_item_list = response.xpath(".//div[@class='mod_topic_wrap post']")
        if answer_item_list:
            for answer_items in answer_item_list:
                # author_id取URL里面的比较好
                # creat_time这里到秒，看清楚
                # answer = Answer()
                # answer.topic_id = topic_id
                answer_item = AnswerItem()
                answer_item["topic_id"] = topic_id
                answer_id_str = answer_items.xpath("./@data-post-id").extract()[0]
                answer_id = int(answer_id_str)
                # answer.answer_id = answer_id
                answer_item["answer_id"]=answer_id

                answer_content = answer_items.xpath(".//div[@class='post_body post_body_min_h']").extract()[0]
                # answer.content = answer_content
                answer_item["content"] = answer_content

                answer_praised_nums_str = answer_items.xpath(".//label[@class='red_praise digg']/em/text()").extract()[0]
                answer_praised_nums = int(answer_praised_nums_str)
                # answer.parised_nums = answer_praised_nums
                answer_item["parised_nums"] = answer_praised_nums

                answer_create_time_str = answer_items.xpath(".//label[@class='date_time']/text()").extract()[0]
                answer_create_time = datetime.strptime(answer_create_time_str, "%Y-%m-%d %H:%M:%S")
                # answer.create_time = answer_create_time
                answer_item["create_time"] = answer_create_time

                answer_author_info = answer_items.xpath(".//div[@class='nick_name']/a/@href").extract()[0]
                answer_author_id = answer_author_info.split('/')[-1]
                # answer.author = answer_author_id
                answer_item["author"] = answer_author_id
                yield answer_item

                # existed_answers = Answer.select().where(Answer.answer_id == answer.answer_id)
                # if existed_answers:
                #     answer = existed_answers[0]
                # answer.topic_id = topic_id
                # answer.answer_id = answer_id
                # answer.content = answer_content
                # answer.parised_nums = answer_praised_nums
                # answer.create_time = answer_create_time
                # answer.author = answer_author_id
                # answer.save()
        # 获取下一页
        next_page_class = response.xpath("//div[@class='page_nav']/a[last()]/@class").extract()
        if (next_page_class and next_page_class[0] == "pageliststy next_page"):
            next_page = response.xpath("//a[@class='pageliststy next_page']/@href")
            next_page_url = parse.urljoin(self.domain, next_page.extract()[-1])
            # parse_topic(next_page_url, cookies_dict)
            yield scrapy.http.Request(url=next_page_url, callback=self.parse_topic)
        pass

    def parse_author(self, response):
        url = response.url
        author_info = response.xpath("//div[@id='asideProfile']")
        if author_info:
            # author = Author()
            author_item=AuthorItem()
            # id_info = author_info.xpath("")
            # rank_info=author_info.xpath("//div[@class='grade-box clearfix']")
            title_info = author_info.xpath("//div[@class='data-info d-flex item-tiling']")
            if title_info:
                original_nums = title_info.xpath(".//dl[1]/@title").extract()[0]
                follower_nums = title_info.xpath(".//dl[2]/@title").extract()[0]
                parised_nums = title_info.xpath(".//dl[3]/@title").extract()[0]
                answer_nums = title_info.xpath(".//dl[4]/@title").extract()[0]
                click_nums = title_info.xpath(".//dl[5]/@title").extract()[0]
                # author.original_nums = int(original_nums)
                # author.follower_nums = int(follower_nums)
                # author.parised_nums = int(parised_nums)
                # author.answer_nums = int(answer_nums)
                # author.click_nums = int(click_nums)
                author_item["original_nums"] = int(original_nums)
                author_item["follower_nums"] = int(follower_nums)
                author_item["parised_nums"] = int(parised_nums)
                author_item["answer_nums"] = int(answer_nums)
                author_item["click_nums"] = int(click_nums)

            name = author_info.xpath(".//div[@class='profile-intro d-flex']//a[@id='uid']/@title").extract()[0]
            id = url.split('/')[-1]
            rate = author_info.xpath(".//div[@class='grade-box clearfix']/dl[4]/@title").extract()[0]
            # author.name = name
            # author.id = id
            author_item["name"] = name
            author_item["id"] = id
            try:
                rate = int(rate)
                # author.rate = rate
                author_item["rate"] = rate
            except Exception as e:
                print(e)
                
            yield author_item
            # existed_author = Author.select().where(Author.id == author.id)
            # if existed_author:
            #     # 如果已经存在就更新
            #     author.save()
            # else:
            #     # 不存在就插入
            #     author.save(force_insert=True)
        pass
