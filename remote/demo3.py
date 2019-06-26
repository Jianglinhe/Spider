#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 上午9:54
    @Author:      hezhiqiang
    @FileName:    demo3.py
    @IDE:         PyCharm

    实现任意贴吧的爬虫,保存网页到本地
    使用time.sleep()来解决频繁请求被拒绝的要求

"""

import requests
import time

class TiebaSpider(object):

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw=' + tieba_name + '&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def get_url_list(self):  # 构造url列表
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list

        # 更加简洁方便
        return [self.url_temp.format(i*50) for i in range(1000)]


    def parse_url(self, url):  # 发送请求,获取响应内容
        print(url)
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode('utf-8')

    def save_html(self, html_str, page_num):  # 保存html字符串
        file_path = '{}_第{}页.html'.format(self.tieba_name, page_num)
        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(html_str)

    def run(self):  # 实现主要的逻辑

        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历发送请求,获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.实现页面的保存
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)

            if int(page_num) % 9 == 0:  # 在每个请求间增加延时可以减少大部分请求拒绝,解决频繁请求问题,可以间隔设置高一点,让程序在后台自己运行
                time.sleep(0.5)


if __name__ == '__main__':
    print('开始爬取......')
    tieba_spider = TiebaSpider(tieba_name='lol')     # 实现任意贴吧的前1000页的爬取
    tieba_spider.run()
    print('完成爬取......')