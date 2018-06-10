# _*_ coding:utf-8 _*_
__author__ = "JemmyH"
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 想执行哪个取消注释就行
"""
其实这里你也许也想到了，那就是能不能让多个爬虫同时执行。
答案是可以，但时间原因不写了，这里有个思路就行了
（可以把几个爬虫放在同一个spider类中，然后像类似多线程的使用方法一样去调用启动即可。
"""
# execute(["scrapy", "crawl", "mzitu"])
# execute(["scrapy", "crawl", "ppmsg"])
execute(["scrapy", "crawl", "a192tt"])
# execute(["scrapy", "crawl", "mmjpg"])
