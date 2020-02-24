# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_test.models import *


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TopicItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    id = scrapy.Field()
    author = scrapy.Field()
    create_time = scrapy.Field()
    answer_nums = scrapy.Field()
    click_nums = scrapy.Field()
    praised_nums = scrapy.Field()
    jtl = scrapy.Field()  # 结帖率
    score = scrapy.Field()  # 赏分
    status = scrapy.Field()  # 状态
    last_answer_time = scrapy.Field()

    def save(self):
        topic = Topic()
        topic.title = self["title"]
        topic.content = self["content"]
        topic.id = self["id"]
        topic.author = self["author"]
        topic.create_time = self["create_time"]
        topic.answer_nums = self.get("answer_nums", 0)
        topic.click_nums = self.get("click_nums", 0)
        topic.praised_nums = self.get("praised_nums", 0)
        topic.jtl = self.get("jtl", 0.0)
        topic.score = self.get("score", 0)
        topic.status = self["status"]
        topic.last_answer_time = self["last_answer_time"]

        existed_topics = Topic.select().where(Topic.id == topic.id)
        if existed_topics:
            topic.save()
        else:
            # 不存在就插入
            topic.save(force_insert=True)

    # def save_content(self):
    #     topic = Topic()
    #     topic.id = self["id"]
    #     existed_topics = Topic.select().where(Topic.id == topic.id)
    #     if existed_topics:
    #         topic = existed_topics[0]
    #         topic.content = self.get("content")
    #         topic.praised_nums = self.get("praised_nums", 0)
    #         topic.jtl = self.get("jtl", 0.0)
    #         topic.save()


class AnswerItem(scrapy.Item):
    topic_id = scrapy.Field()
    answer_id = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    create_time = scrapy.Field()
    parised_nums = scrapy.Field()  # 点赞数

    def save(self):
        answer = Answer()
        answer.answer_id = self["answer_id"]
        existed_answers = Answer.select().where(Answer.answer_id == answer.answer_id)
        if existed_answers:
            answer = existed_answers[0]
        answer.topic_id = self["topic_id"]
        answer.answer_id = self["answer_id"]
        answer.content = self["content"]
        answer.parised_nums = self["parised_nums"]
        answer.create_time = self["create_time"]
        answer.author = self["author"]
        answer.save()


class AuthorItem(scrapy.Item):
    name = scrapy.Field()  # 博客
    id = scrapy.Field()  # 博客
    click_nums = scrapy.Field()  # 访问数 博客
    original_nums = scrapy.Field()  # 原创数 博客
    forward_nums = scrapy.Field()  # 转发数 无
    rate = scrapy.Field()  # 排名 博客
    answer_nums = scrapy.Field()  # 评论数 博客
    parised_nums = scrapy.Field()  # 获赞数 博客
    desc = scrapy.Field()  # 主页
    industry = scrapy.Field()  # 无
    location = scrapy.Field()  # 无
    follower_nums = scrapy.Field()  # 粉丝数 博客
    following_nums = scrapy.Field()  # 关注数 主页

    def save(self):
        author = Author(self)
        author.name = self["name"]  # 博客
        author.id = self["id"]  # 博客
        author.click_nums = self.get("click_nums", 0)  # 访问数 博客
        author.original_nums = self.get("original_nums", 0)  # 原创数 博客
        author.forward_nums = self.get("forward_nums", 0)  # 转发数 无
        author.rate = self.get("rate", -1)  # 排名 博客
        author.answer_nums = self.get("answer_nums", 0)  # 评论数 博客
        author.parised_nums = self.get("parised_nums", 0)  # 获赞数 博客
        author.desc = self.get("desc", "")  # 主页
        author.industry = self.get("industry", "")  # 无
        author.location = self.get("location", "")  # 无
        author.follower_nums = self.get("follower_nums", 0)  # 粉丝数 博客
        author.following_nums = self.get("following_nums", 0)
        # print(author.id,author.name)
        existed_author = Author.select().where(Author.id == author.id)
        if existed_author:
            # 如果已经存在就更新
            author.save()
        else:
            # 不存在就插入
            author.save(force_insert=True)
