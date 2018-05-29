# -*- coding: utf-8 -*-
import scrapy
from ..items import MmjpgItem


class MmjpgSpider(scrapy.Spider):
    """
    经过观察网站结构发现：它的每一个大标题都是根据数字顺序来命名的，所以只需找到第一个（1）和最后一个（1361）并设置为start_url
    """
    name = 'mmjpg'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/mm/' + str(i) for i in range(1, 1362)]

    def parse(self, response):
        """
        又经过观察发现：每一个大标题下面的每一张图片也是根据数字排序来命名的，只需要得到图片总数即可
        :param response:
        :return:
        """
        img_num = int(response.xpath("//div[@class='page']//a/text()").extract()[-2])
        urls = [response.url + "/" + str(i) for i in range(1, img_num + 1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = MmjpgItem()
        item['title'] = response.xpath("//div[@class='article']/h2[1]/text()").extract_first().split("(")[0]
        item['url'] = response.xpath("//div[@class='article']/div[2]/a[1]/img/@src").extract_first()
        item['name'] = item['url'].split("/")[-1]
        yield item
