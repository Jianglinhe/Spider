#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-13 下午12:48
    @Author:      hezhiqiang
    @FileName:    qiushibaike_spider.py
    @IDE:         PyCharm
    爬去糗事百科的内容

"""
import requests
from lxml import etree
import json

class QiubaiSpider(object):

    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        self.session = requests.session()

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        response = self.session.get(url, headers=self.headers)
        assert response.status_code == 200, "返回异常"
        return response.content.decode("utf-8")

    def save_content_list(self, content_list):
        with open("qiushibaike.txt", 'a', encoding='utf-8') as f:
            for content in content_list:
                # print(content)
                f.write(json.dumps(content, ensure_ascii=False))    # 转化为json字符串写入的时候,None被转化为null
                f.write("\n")
            print("保存成功....")


    def get_content_list(self, html_str):   # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div") # 分组
        conent_list = []
        for div in div_list:
            item = {}
            item["content"] = [i.replace("\n", "") for i in div.xpath(".//div[@class='content']/span/text()")]
            item["author_gender"] = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(item["author_gender"])>0 else None
            item["author_age"] = div.xpath(".//div[contains(@class, 'articleGender')]/text()")
            item["author_age"] = item["author_age"][0] if len(item["author_age"])>0 else None

            item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["author_img"] = "https:"+item["author_img"][0] if len(item["author_img"])>0 else None

            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
            conent_list.append(item)

        return conent_list

    def run(self):  # 实现主要的逻辑
        # 1.url_list
        url_list = self.get_url_list()
        # 2.遍历,发送请求,获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)

if __name__ == '__main__':

    qiuba = QiubaiSpider()
    qiuba.run()