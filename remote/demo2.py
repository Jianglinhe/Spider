#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 上午9:37
    @Author:      hezhiqiang
    @FileName:    demo2.py
    @IDE:         PyCharm
"""

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 设置带参数的请求
params = {
    'wd': '中国'
}

response = requests.get(url='https://www.baidu.com/s', headers=headers, params=params)  # s后面可以带?,也可以不带?,自动添加?
print(response.request.url)     # 查看请求的url地址 https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD 经过url编码的


resp = requests.get(url='https://www.baidu.com/s?wd={}'.format('中国'), headers=headers)  # 使用字符串格式化的方法来实现url地址的拼接
print(resp.status_code)
print(resp.request.url)