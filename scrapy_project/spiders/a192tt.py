# -*- coding: utf-8 -*-
import scrapy
from ..items import A192ttItem


class A192ttSpider(scrapy.Spider):
    name = 'a192tt'
    allowed_domains = ['www.192tt.com']
    start_urls = ['https://www.192tt.com/gc/', 'https://www.192tt.com/gq/', 'https://www.192tt.com/hz/',
                  'https://www.192tt.com/zy']

    def parse(self, response):
        item_urls = response.xpath("//ul[@class='clearfix']//li/a/@href").extract()
        for item_url in item_urls:
            yield scrapy.Request(url="https://www.192tt.com" + item_url, callback=self.parse_more, dont_filter=True)
        next_item = response.xpath("//div[@class='page']//a/text()").extract()
        if "下一页" in next_item:
            next_page_url = response.xpath("//div[@class='page']//a/@href").extract()[-2]
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_more(self, response):
        print("parse_more url:", response.url)
        item = {
            'item': response.url.split("/")[3]
        }
        print(response.xpath("//div[@class='pictext']//a/@href").extract()[-1])
        yield scrapy.Request(
            url=response.xpath("//div[@class='pictext']//a/@href").extract()[-1],
            callback=self.parse_details, meta={'item': item}, dont_filter=True)

    def parse_details(self, response):
        item_old = response.meta['item']
        print("parse_detail url:", response.url)
        item = A192ttItem()
        item['item'] = item_old['item']
        item['title'] = response.xpath("//div[@class='v_m']/table[1]/tr[1]/td[2]/text()").extract_first().strip()
        item['url'] = response.xpath("//div[@class='v_m']/table[1]/tr[2]/td[2]/u/text()").extract_first()
        item['name'] = response.xpath("//div[@class='v_m']/table[1]/tr[3]/td[2]/text()").extract_first()
        item['passwd'] = response.xpath("//div[@class='v_m']/table[1]/tr[4]/td[2]/text()").extract_first()[4:8]
        print(item['item'], item['title'], item['url'], item['name'], item['passwd'])
        yield item
