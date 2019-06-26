#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-12 下午3:12
    @Author:      hezhiqiang
    @FileName:    douban_spider.py
    @IDE:         PyCharm

    爬取豆瓣上所有的电视剧

"""
import requests
import json


class DoubanSpider(object):

    def __init__(self):

        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?start={}&count=18&loc_id=108288"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer': 'https://m.douban.com/tv/chinese'
        }

    def parse_url(self, url):
        print(url)  # 将当前想要获取响应的url打印出来
        response = requests.get(url, headers=self.headers)
        return response.content.decode('utf-8').replace(";jsonp1(", "").replace(");", "")
        # 返回一个json_str,此处的replace

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)     # 将json数据转化为字典
        content_list = dict_ret["subject_collection_items"]
        return content_list

    def save_content_list(self, content_list):
        with open("douban3.txt", 'a', encoding='utf-8') as f:   # 以追加的方式写入
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")   # 写入换行符进行换
        print("保存成功...........")

    def run(self):  # 实现主要逻辑
        num = 0 # 起始位置

        while True:
            # 1.start url
            url = self.url_temp.format(num)
            # 2.发送请求,获取响应
            json_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(json_str)
            # 4.保存
            self.save_content_list(content_list)

            if len(content_list) < 18:  # 最后一页不够18条记录
                break

            # 5.构造下一页的url地址,进入循环
            num += 18


if __name__ == '__main__':

    douban_spider = DoubanSpider()
    douban_spider.run()

