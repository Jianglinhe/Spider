#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 上午11:26
    @Author:      hezhiqiang
    @FileName:    demo4.py
    @IDE:         PyCharm

    request中的post请求的使用
    通过百度翻译实现一个翻译工具
"""
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

data = {
    "from": "zh",
    "to": "en",
    "query": "name",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "106415.359582",
    "token": "cdd13e267040e50af2c6446ccee60bf6" # 电脑版的token每次请求都是变动的,可能是js生成的,使用手机版的来解决
}

post_rul = "https://fanyi.baidu.com/v2transapi"

r = requests.post(url=post_rul, data=data, headers=headers)

print(r.content.decode('utf-8'))