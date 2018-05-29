# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import PpmsgItem


class PpmsgSpider(scrapy.Spider):
    name = 'ppmsg'
    allowed_domains = ['www.ppmsg.org']
    start_urls = ['http://www.ppmsg.org' + i for i in
                  ['/meituimote/', '/zhanhuimote/', '/xingganchemo/', '/qingchunmeinv/', '/meinvzipai/', '/siwameitui/',
                   '/mingxingxiezhen/', '/jiepaimeinv/']]

    def parse(self, response):
        print("开始请求：" + response.url)
        page_num = int(
            re.findall(r"\d+", response.xpath("//ul[@class='page']/text()").extract_first().split(" /")[-1])[0])
        print(page_num)
        item_urls = ["/".join(response.url.split("/")[:4]) + "/" + i for i in
                     response.xpath("//ul[@class='image']//li/a/@href").extract()]
        for item_url in item_urls:
            yield scrapy.Request(url=item_url, callback=self.parse_item)
        last_page_url = "/".join(response.url.split("/")[:4]) + "/" + str(page_num) + ".html"
        next_page_url = "/".join(response.url.split("/")[:4]) + "/" + response.xpath(
            "//ul[@class='page']/a[3]/@href").extract_first()
        if next_page_url != last_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_item(self, response):
        print("开始请求：" + response.url)
        img_urls = [i.strip() for i in
                    response.xpath("//div[@id='imagelist']/img/@src").extract()]  # 这是一个防盗链，后面加了一个"\r"，所以我们请求的时候得过滤掉
        for img_url in img_urls:
            item = PpmsgItem()
            item['item'] = response.url.split("/")[3]
            item['title'] = response.xpath("//h2/text()").extract_first()
            item['url'] = img_url
            item['name'] = img_url.split("/")[-1]
            print("item信息：" + item['item'], item['title'], item['name'], item['url'])
            yield item
        image_page_num = int(response.xpath("//ul[@class='image']/strong/text()").extract_first())
        if response.url.find("_") > -1:
            last_image_page_url = (response.url.split("_")[0]) + "_{0}.html".format(image_page_num)
        else:
            last_image_page_url = ".".join(response.url.split(".")[:-1]) + "_{0}.html".format(image_page_num)
        next_image_page_url = "/".join(response.url.split("/")[:4]) + "/" + response.xpath("//ul[@class='image']/a/@href").extract()[-1]
        if last_image_page_url != next_image_page_url:
            print("下一页：", next_image_page_url)
            yield scrapy.Request(next_image_page_url, callback=self.parse_item)
