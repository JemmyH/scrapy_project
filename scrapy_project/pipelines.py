# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
这里需要注意的是：如果想要下载的文件按照类别存放到不同的文件夹，比如图片，我这里采用的方法是使用shutil包的move方法
"""
import os
import scrapy
import shutil
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import pymysql


class MmjpgItemPipeline(ImagesPipeline):
    # mmjpg 项目的pipeline
    path = get_project_settings().get('IMAGES_STORE')
    file_store = path + "www.mmjpg.com\\"  # 图片储存地址

    def get_media_requests(self, item, info):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'http://www.mmjpg.com/'  # 这个太重要了！！！！！因为mmjpg的反爬虫措施就是根据referer来判断的！一般填写主域名就可以了
        }
        print("开始请求源代码", item['url'])
        print(item['title'], item['name'], item['url'])
        yield scrapy.Request(item['url'], headers=headers)  # 将源文件下载并保存在默认路径的full文件夹里

    def item_completed(self, results, item, info):
        # 每爬完一个项目（下载完成一张图片）
        print("finished")
        file_path = [x["path"] for ok, x in results if ok][0].split("/")
        print(file_path)  # 查找下载的图片在本地full文件夹中的位置和名字 比如['full', '0264d064a89e55b564f773d4b60496499b1a316c.jpg']
        f_p = "{0}{1}".format(self.file_store, item['title'])  # 根据图片的标题创建响应的目录 比如F:\image\www.mmjpg.com\粉嫩妹子一薰白嫩美臀诱惑无比
        print(f_p)
        if not os.path.exists(f_p):
            os.mkdir(f_p)
            print(f_p + "创建成功")
        print(shutil.move(self.path + file_path[0] + "\\" + file_path[1],
                          f_p + "\\" + item['name']))  # 分级创建目录的核心代码，即将图片移动到响应的目录中去
        item['title'] = f_p + "\\" + item['name']
        return item

    def close_spider(self):
        print("爬虫完成")


class MzituItemPipeline(ImagesPipeline):
    # mzitu 项目的pipeline
    path = get_project_settings().get('IMAGES_STORE')
    file_store = path + "www.mzitu.com\\"  # 图片储存地址

    def get_media_requests(self, item, info):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'http://www.mzitu.com/'  # 这个太重要了！！！！！因为mmjpg的反爬虫措施就是根据referer来判断的！一般填写主域名就可以了
        }
        print("开始请求源代码", item['url'])
        print(item['item'], item['title'], item['name'], item['url'])
        yield scrapy.Request(item['url'], headers=headers)  # 将源文件下载并保存在默认路径的full文件夹里

    def item_completed(self, results, item, info):
        # 每爬完一个项目（下载完成一张图片）
        print("finished")
        file_path = [x["path"] for ok, x in results if ok][0].split("/")
        print(file_path)  # 查找下载的图片在本地full文件夹中的位置和名字 比如['full', '0264d064a89e55b564f773d4b60496499b1a316c.jpg']
        f_i_p = "{0}{1}".format(self.file_store, item['item'])
        print(f_i_p)
        if not os.path.exists(f_i_p):
            os.mkdir(f_i_p)
            print(f_i_p + "创建成功")
        f_p = "{0}{1}\{2}\\".format(self.file_store, item['item'],
                                    item['title'])  # 根据图片的标题创建响应的目录 比如F:\image\www.mmjpg.com\qingchun\粉嫩妹子一薰白嫩美臀诱惑无比
        print("f_p:" + f_p)
        if not os.path.exists(f_p):
            os.mkdir(f_p)
            print(f_p + "创建成功")
        print(shutil.move(self.path + file_path[0] + "\\" + file_path[1],
                          f_p + "\\" + item['name']))  # 分级创建目录的核心代码，即将图片移动到响应的目录中去
        item['title'] = f_p + "\\" + item['item'] + "\\" + item['name']
        return item

    def close_spider(self):
        print("爬虫完成")


class PpmsgItemPipeline(ImagesPipeline):
    # ppmsg 项目的pipeline
    path = get_project_settings().get('IMAGES_STORE')
    file_store = path + "www.ppmsg.org\\"  # 图片储存地址

    def get_media_requests(self, item, info):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'http://www.ppmsg.org/'  # 这个太重要了！！！！！因为mmjpg的反爬虫措施就是根据referer来判断的！一般填写主域名就可以了
        }
        print("开始请求源代码", item['url'])
        print(item['item'], item['title'], item['name'], item['url'])
        yield scrapy.Request(item['url'], headers=headers)  # 将源文件下载并保存在默认路径的full文件夹里

    def item_completed(self, results, item, info):
        # 每爬完一个项目（下载完成一张图片）
        print("finished")
        file_path = [x["path"] for ok, x in results if ok][0].split("/")
        print(file_path)  # 查找下载的图片在本地full文件夹中的位置和名字 比如['full', '0264d064a89e55b564f773d4b60496499b1a316c.jpg']
        f_i_p = "{0}{1}".format(self.file_store, item['item'])
        print(f_i_p)
        if not os.path.exists(f_i_p):
            os.mkdir(f_i_p)
            print(f_i_p + "创建成功")
        f_p = "{0}{1}\{2}\\".format(self.file_store, item['item'],
                                    item['title'])  # 根据图片的标题创建响应的目录 比如F:\image\www.mmjpg.com\qingchun\粉嫩妹子一薰白嫩美臀诱惑无比
        print("f_p:" + f_p)
        if not os.path.exists(f_p):
            os.mkdir(f_p)
            print(f_p + "创建成功")
        print(shutil.move(self.path + file_path[0] + "\\" + file_path[1],
                          f_p + "\\" + item['name']))  # 分级创建目录的核心代码，即将图片移动到响应的目录中去
        item['title'] = f_p + "\\" + item['item'] + "\\" + item['name']
        return item

    def close_spider(self):
        print("爬虫完成")


class A192ttItemPipeline(object):
    def open_spider(self, spider):
        print("爬虫开始")
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='hujiaming', passwd='123456', db='python',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        print("数据库连接成功")

    def process_item(self, item, spider):
        sql = "insert into a192tt(item,title,url,name,passwd) values('{0}','{1}','{2}','{3}','{4}');".format(
            item['item'], item['title'], item['url'], item['name'], item['passwd'])
        print(sql)
        self.cursor.execute(sql)
        print("sql 执行成功")
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        print("爬虫结束")
