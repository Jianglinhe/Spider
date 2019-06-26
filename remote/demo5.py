#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 下午12:38
    @Author:      hezhiqiang
    @FileName:    demo5.py
    @IDE:         PyCharm

    百度翻译的data参数每次请求都是变动的,无法使用
"""

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

data = {
    "query": "人生苦短,我用python",
    "from": "zh",
    "to": "en",
}

post_rul = "https://fanyi.baidu.com/basetrans"

r = requests.post(url=post_rul, data=data, headers=headers)

print(r.content.decode('utf-8'))