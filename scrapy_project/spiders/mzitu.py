# -*- coding: utf-8 -*-
import scrapy
from ..items import MzituItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/xinggan', 'http://www.mzitu.com/japan', 'http://www.mzitu.com/taiwan',
                  'http://www.mzitu.com/mm']

    def parse(self, response):
        print(response.url)
        item = {
            'item': response.url.split("/")[-2]
        }
        page_num = int(response.xpath("//div[@class='nav-links']//a/text()").extract()[-2])
        page_urls = [response.url + "page/" + str(i) for i in range(1, page_num + 1)]
        for page_url in page_urls:  # 每一页的url
            yield scrapy.Request(url=page_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):  # 获取每一个item
        item = response.meta['item']
        item_urls = response.xpath("//ul[@id='pins']//li/a/@href").extract()
        for item_url in item_urls:
            yield scrapy.Request(url=item_url, callback=self.parse_image, meta={'item': item})

    def parse_image(self, response):
        item = response.meta['item']
        img_num = int(response.xpath("//div[@class='pagenavi']//span/text()").extract()[-2])
        img_urls = [response.url + "/" + str(i) for i in range(1, img_num + 1)]
        for img_url in img_urls:
            yield scrapy.Request(url=img_url, callback=self.parse_every_image, meta={'item': item})

    def parse_every_image(self, response):
        item = MzituItem()
        item_old = response.meta['item']
        item['item'] = item_old['item']
        item['title'] = response.xpath("//h2[@class='main-title']/text()").extract_first().replace("(", "（").split("（")[
            0]
        item['url'] = response.xpath("//div[@class='main-image']/p[1]/a/img/@src").extract_first()
        item['name'] = item['url'].split("/")[-1]
        print("item信息：" + item['item'], item['title'], item['name'], item['url'])
        yield item
