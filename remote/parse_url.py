#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-10 下午8:59
    @Author:      hezhiqiang
    @FileName:    parse_url.py
    @IDE:         PyCharm

    python中的retrying模块,可以进行一些重复的操作
"""

import requests
from retrying import retry  # 如果超时,可以在重复进行请求

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 重试3次
@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):

    print("*"*20)   # 用来说明重新请求了多少次
    if method == "POST":
        response = requests.get(url, headers=headers, data=data, proxies=proxies, timeout=3)
    else:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=3)

    assert response.status_code == 200, "请求失败"
    return response.content.decode('utf-8')



def parse_url(url, method='GET', data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':

    url = "https://www.baidu.com"

    print(parse_url(url))

