#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-20 下午5:25
    @Author:      hezhiqiang
    @FileName:    qiubai_queue_spider.py
    @IDE:         PyCharm

    使用多线程来实现糗事百科的爬虫

"""

import requests
from lxml import etree
import json
import threading
from queue import Queue



class QiubaiSpider(object):

    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 14)]
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):

        while True:
            url = self.url_queue.get()  # 从队列中获取url
            print(url)
            response = requests.get(url, headers=self.headers)
            assert response.status_code == 200, "返回异常"

            self.html_queue.put(response.content.decode("utf-8"))
            self.url_queue.task_done()  # get才会减一


    def get_content_list(self):  # 提取数据
        while True:
            html_str = self.html_queue.get()

            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")  # 分组
            conent_list = []
            for div in div_list:
                item = {}
                item["content"] = [i.replace("\n", "") for i in div.xpath(".//div[@class='content']/span/text()")]
                item["author_gender"] = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
                item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(
                    item["author_gender"]) > 0 else None
                item["author_age"] = div.xpath(".//div[contains(@class, 'articleGender')]/text()")
                item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None

                item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
                item["author_img"] = "https:" + item["author_img"][0] if len(item["author_img"]) > 0 else None

                item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
                item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
                conent_list.append(item)

            self.content_queue.put(conent_list)

            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get() # get完成后都需要task_done()一下
            with open("qiushibaike_queue.txt", 'a', encoding='utf-8') as f:
                for content in content_list:
                    # print(content)
                    f.write(json.dumps(content, ensure_ascii=False))    # 转化为json字符串写入的时候,None被转化为null
                    f.write("\n")
                print("保存成功....")
            self.content_queue.task_done()


    def run(self):  # 实现主要的逻辑
        thread_list = []

        # 1.url_list
        t_url = threading.Thread(target=self.get_url_list)  # target=self.get_url_list调用函数不能加括号
        thread_list.append(t_url)

        # 2.遍历,发送请求,获取响应
        for i in range(5):  # 让获取响应这块使用多个线程
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        # 3.提取数据
        t_html = threading.Thread(target=self.get_content_list)
        thread_list.append(t_html)

        # 4.保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for t in thread_list:
            t.setDaemon(True)   # 将子线程设置为守护线程,该线程不重要,主线程结束,子线程结束,必须在start低矮用之前调用
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()    # 让主线程等待阻塞,等待队列的任务完成之后再完成


        print("主线程结束")

if __name__ == '__main__':

    qiuba = QiubaiSpider()
    qiuba.run()