# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTestPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

# class ScrapyTestPipeline_content(object):
#     def process_item(self, item, spider):
#         item.save_content()
#         return item