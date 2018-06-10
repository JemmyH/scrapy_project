# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmjpgItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()


class MzituItem(scrapy.Item):
    item = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()


class PpmsgItem(scrapy.Item):
    item = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()


class A192ttItem(scrapy.Item):
    item = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()  # 其实就是压缩包的解压密码
    passwd = scrapy.Field()
