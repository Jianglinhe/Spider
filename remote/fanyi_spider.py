#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 下午2:19
    @Author:      hezhiqiang
    @FileName:    fanyi_spider.py
    @IDE:         PyCharm

    使用post实现一个翻译的小程序,调用金山词霸的翻译接口
    使用这个翻译http://fy.iciba.com/
"""
import requests
import json
import sys

# 通过命令行参数来传递输入
query_string = sys.argv[1]  # 0是.py文件的文件名

headers = {
    "Referer": "http://fy.iciba.com/",
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

data = {
    "f": "auto",
    "t": "auto",
    "w": query_string
}

post_rul = "http://fy.iciba.com/ajax.php?a=fy"

r = requests.post(url=post_rul, data=data, headers=headers)

dict_ret = json.loads(r.content.decode('utf-8'))
# print(r.content.decode('utf-8'))
ret = dict_ret['content']['out']    # 中文翻译英文的时候是在['content']['out']这个路径中,英文翻译中文则不在
print('result is :', ret)
