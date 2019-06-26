#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 上午8:52
    @Author:      hezhiqiang
    @FileName:    demo1.py
    @IDE:         PyCharm
"""

import requests

# 创建请求头(和浏览器一样的请求头),模拟浏览器,欺骗服务器
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

resp = requests.get(url='https://www.baidu.com', headers=headers)   # 将请求头添加到请求中

# 使用assert来确定响应是否成功
assert resp.status_code == 200, '返回状态失败'

print(resp.status_code)     # 查看请求状态
print(resp.headers)     # 查看响应头

print(resp.request.url)     # 查看请求响应的url
print(resp.request.headers)     # 查看请求头

with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.content.decode('utf-8'))
